# 10. ตรรกะการประมวลผลพร้อมกันและการรวมสถิติ Dashboard (Concurrent Aggregation & Dashboard Patterns)

หัวข้อนี้อธิบายถึงรูปแบบการดึงข้อมูลสถิติจากหลายโดเมนพร้อมกัน (Concurrent Data Fetching ด้วย `Promise.all`), การคิดคำนวณสัดส่วนเปอร์เซ็นต์อย่างปลอดภัยจาก Zero-Division, และตรรกะการประมวลผลความสัมพันธ์แบบ Higher-Order Function

---

## 1. Concurrent Multi-Domain Aggregation (`Promise.all`)

### แนวคิดและปัญหาที่แก้
Dashboard กลางจำเป็นต้องรวบรวมข้อมูลจากหลาย Service ที่ไม่เกี่ยวข้องกัน (ข้อมูลรายการทรัพยากร, รอบการประมวลผลล่าสุด, รายการงานที่เกินกำหนดเวลา) การเรียกทีละคำสั่งแบบเรียงลำดับ (Sequential Await) จะทำให้เวลาตอบสนองรวมของ Dashboard ช้ามาก

ผู้พัฒนาใช้ `Promise.all` ยิง Request พร้อมกันแบบ Non-blocking Concurrency:

```typescript
import { differenceInDays } from 'date-fns';
import _ from 'lodash';

export class SummaryDashboardService {
  async getDashboardSummary(ctx: UserSessionContext) {
    // ยิง Query 3 Domain พร้อมกันในเวลาเดียวแบบ Concurrency
    const [resources, latestCycle, overdueItems] = await Promise.all([
      this.resourceService.findAll(ctx),
      this.cycleService.getLatestActiveCycle(ctx),
      this.taskService.findOverdueTasks(ctx),
    ]);

    const logsInCycle = await this.logService.findByCycle(ctx, latestCycle);
    const totalResources = resources.length;

    // คำนวณเปอร์เซ็นต์พร้อมดัก Zero-Division
    const activeResources = resources.filter((r) => r.isActive).length;
    const activePercentage = totalResources > 0
      ? ((activeResources / totalResources) * 100).toFixed(2)
      : '0.00';

    // คำนวณความต่างของวันที่อัปเดตล่าสุด
    const now = new Date();
    const latestUpdateDate = _.maxBy(logsInCycle, 'updated_at')?.updated_at;
    let daysSinceLastUpdate = 'N/A';
    if (latestUpdateDate) {
      daysSinceLastUpdate = String(differenceInDays(now, latestUpdateDate));
    }

    return {
      resourceMetric: createMetric(
        'จำนวนทรัพยากรทั้งหมด',
        totalResources,
        `เปิดใช้งาน ${activePercentage}%`,
        'รายการ',
      ),
      activeCountMetric: createMetric(
        'จำนวนที่เปิดใช้งาน',
        activeResources,
        0,
        'รายการ',
      ),
      cycleLogMetric: createMetric(
        'บันทึกในรอบปัจจุบัน',
        logsInCycle.length,
        `อัปเดตล่าสุด ${daysSinceLastUpdate} วันที่แล้ว`,
        'รายการ',
      ),
      criticalOverdueMetric: createMetric(
        'รายการเกินกำหนด SLA',
        overdueItems.length,
        'ต้องการการตอบสนองด่วน',
        'วิกฤติ',
      ),
    };
  }
}
```

---

## 2. Higher-Order Section Processor สำหรับการเชื่อมโยง Relation แบบขนาน

### แนวคิดและปัญหาที่แก้
ในการผูกความสัมพันธ์หลายมิติของ Entity แต่ละส่วนต้องมีการตรวจสอบขอบเขตสิทธิ์ (`validateAccessBoundary`) และการ Query ข้อมูลเพื่อเซ็ตค่าลง Relation

ผู้พัฒนาสร้างฟังก์ชันระดับสูง `processSection` แล้วรันด้วย `Promise.all` เพื่อให้การผูกข้อมูลทุกมิติทำพร้อมกันโดยไม่เกิดโค้ดซ้ำซ้อน:

```typescript
export async function assignMultiDimensionalScopes(
  ctx: UserSessionContext,
  inputDto: {
    tenants?: string[];
    groups?: string[];
    teams?: string[];
  },
  targetEntity: BaseScopeEntity,
) {
  const { tenantIds, groupScopeIds, subScopeIds } = ctx.assigned;

  const boundaryMap = {
    tenants: tenantIds,
    groups: groupScopeIds,
    teams: subScopeIds,
  };

  // Higher-Order Function สำหรับประมวลผลและตรวจสอบสิทธิ์ทีละ Section
  const processSection = async (
    sectionKey: keyof typeof boundaryMap,
    assignRelationCallback: (validInputs: string[]) => Promise<void>,
  ) => {
    const values = inputDto[sectionKey];
    if (values === undefined) return;
    if (values.length === 0) {
      await assignRelationCallback([]);
      return;
    }

    // ตรวจสอบขอบเขตความปลอดภัย
    validateAccessBoundary(
      ctx,
      values,
      boundaryMap[sectionKey],
      `Access denied: ${sectionKey} is out of boundary`,
    );

    await assignRelationCallback(values);
  };

  // รันการตรวจสอบและ Assign Relation ทั้งหมดพร้อมกันแบบขนาน
  await Promise.all([
    processSection('tenants', async (inputs) => {
      targetEntity.Tenants = inputs.length
        ? await this.tenantRepository.find({ where: { id: In(inputs) }, take: 5000 })
        : [];
    }),
    processSection('groups', async (inputs) => {
      targetEntity.Groups = inputs.length
        ? await this.groupRepository.find({ where: { id: In(inputs) }, take: 5000 })
        : [];
    }),
    processSection('teams', async (inputs) => {
      targetEntity.Teams = inputs.length
        ? await this.teamRepository.find({ where: { id: In(inputs) }, take: 5000 })
        : [];
    }),
  ]);
}
```
