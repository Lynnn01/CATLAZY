# 04. ตรรกะการประเมินสถานะแบบลำดับความสำคัญ (Deterministic Priority State Machine)

หัวข้อนี้อธิบายถึงตรรกะ State Transition และการตัดสินสถานะรวมของระบบที่มีข้อย่อยจำนวนมาก (เช่น เอกสารตรวจสอบคุณภาพ หรือ Checklist หลายข้อย่อย) ตามหลัก **Cascade Priority และกฎ Veto**

---

## 1. ลำดับชั้นสถานะและการประเมินผลรวม (Cascading State Resolution)

### ปัญหาที่แก้
ในใบงานหรือเอกสารตรวจสอบที่มีข้อย่อยหลายสิบข้อ แต่ละข้ออาจมีสถานะที่แตกต่างกัน เช่น บางข้อตรวจผ่านแล้ว (Approved), บางข้อรอการอนุมัติล่วงหน้า (Pre-Approved), บางข้ออยู่ระหว่างตรวจสอบ (Verified), และบางข้อถูกปฏิเสธ (Rejected)

ผู้พัฒนาสร้างฟังก์ชันประเมินสถานะรวมที่ใช้ **กฎสิทธิ์ขาดตามลำดับขั้น (Priority Rule Chain)**:

```
[1. Has Any Rejection? (Reject > 0)] ───Yes───> REJECT (Veto Rule)
                  │ No
[2. All Sub-items Approved?] ───────────Yes───> APPROVE
                  │ No
[3. All Current Items Pre-Approved?] ───Yes───> PRE_APPROVE
                  │ No
[4. All Current Items Verified?] ───────Yes───> VERIFY
                  │ No
                  └───────────────────────────> IN_PROGRESS
```

---

## 2. โค้ดตัวอย่างการตัดสินสถานะรวม (Cascade Priority Evaluation)

```typescript
export enum InspectionStatus {
  IN_PROGRESS = 'IN_PROGRESS',
  VERIFY = 'VERIFY',
  PRE_APPROVE = 'PRE_APPROVE',
  APPROVE = 'APPROVE',
  REJECT = 'REJECT',
}

interface StatusCounter {
  inProgress: number;
  verify: number;
  preApprove: number;
  approve: number;
  reject: number;
}

/**
 * ประเมินสถานะภาพรวมจากจำนวนสถานะของข้อย่อยทั้งหมดตามลำดับความสำคัญ
 */
export const evaluateAggregatedStatus = (
  statusCounts: StatusCounter[],
  expectedTotalSubsections: number,
): InspectionStatus => {
  const inProgress = statusCounts.reduce((sum, item) => sum + item.inProgress, 0);
  const verify = statusCounts.reduce((sum, item) => sum + item.verify, 0);
  const preApprove = statusCounts.reduce((sum, item) => sum + item.preApprove, 0);
  const approve = statusCounts.reduce((sum, item) => sum + item.approve, 0);
  const reject = statusCounts.reduce((sum, item) => sum + item.reject, 0);
  const totalRecorded = inProgress + verify + preApprove + approve + reject;

  // 1. กฎ Veto: ถ้ามีข้อย่อยใดถูก Reject แม้แต่ข้อเดียว สถานะภาพรวมจะกลายเป็น REJECT ทันที
  if (reject > 0) {
    return InspectionStatus.REJECT;
  }

  // 2. สถานะ APPROVE: ข้อย่อยทั้งหมดต้องถูก Approve ครบทุกข้อตามเกณฑ์
  if (approve > 0 && approve === expectedTotalSubsections) {
    return InspectionStatus.APPROVE;
  }

  // 3. สถานะ PRE_APPROVE: ข้อมูลที่มีทั้งหมดในปัจจุบันได้รับการ Pre-approve ครบทุกข้อ
  if (preApprove > 0 && preApprove === totalRecorded) {
    return InspectionStatus.PRE_APPROVE;
  }

  // 4. สถานะ VERIFY: ข้อมูลที่มีทั้งหมดในปัจจุบันได้รับการ Verify ครบทุกข้อ
  if (verify > 0 && verify === totalRecorded) {
    return InspectionStatus.VERIFY;
  }

  // 5. ค่าเริ่มต้น: หากไม่เข้าเงื่อนไขสมบูรณ์ ให้ถือว่าอยู่ในระหว่างดำเนินการ
  return InspectionStatus.IN_PROGRESS;
};
```

---

## 3. การนับและจัดกลุ่มสถานะข้อย่อย (Single-Pass Multi-Counting)

### แนวคิด
นับและจัดหมวดหมู่ Detail พร้อมจำนวน (`counts`) ในการ Loop เพียงรอบเดียว:

```typescript
interface TopicHistoryItem {
  historyType: InspectionStatus;
  comment?: string;
  Topics: {
    topicKey: string;
    description?: string;
  }[];
}

/**
 * วิเคราะห์และแยกกลุ่มรายการข้อย่อยพร้อมนับจำนวนสถานะในรอบเดียว (Single Pass)
 */
export const analyzeSubItemStatuses = (
  histories: TopicHistoryItem[],
  targetItemKeys: string[],
) => {
  type DetailItem = { key: string; description: string };
  const categorizedItems: Record<InspectionStatus, DetailItem[]> = {
    [InspectionStatus.IN_PROGRESS]: [],
    [InspectionStatus.VERIFY]: [],
    [InspectionStatus.PRE_APPROVE]: [],
    [InspectionStatus.APPROVE]: [],
    [InspectionStatus.REJECT]: [],
  };

  const counts: StatusCounter = {
    inProgress: 0,
    verify: 0,
    preApprove: 0,
    approve: 0,
    reject: 0,
  };

  targetItemKeys.forEach((key) => {
    // หาประวัติล่าสุดที่เกี่ยวข้องกับหัวข้อนี้
    const matchedHistory = histories.find((h) =>
      h.Topics.some((t) => t.topicKey === key),
    );

    if (matchedHistory) {
      const topicData = matchedHistory.Topics.find((t) => t.topicKey === key);
      const description = topicData?.description || matchedHistory.comment || '';
      const entry: DetailItem = { key, description };

      // อัปเดตตัวนับและหมวดหมู่ตาม Type
      switch (matchedHistory.historyType) {
        case InspectionStatus.IN_PROGRESS:
          counts.inProgress++;
          categorizedItems[InspectionStatus.IN_PROGRESS].push(entry);
          break;
        case InspectionStatus.VERIFY:
          counts.verify++;
          categorizedItems[InspectionStatus.VERIFY].push(entry);
          break;
        case InspectionStatus.PRE_APPROVE:
          counts.preApprove++;
          categorizedItems[InspectionStatus.PRE_APPROVE].push(entry);
          break;
        case InspectionStatus.APPROVE:
          counts.approve++;
          categorizedItems[InspectionStatus.APPROVE].push(entry);
          break;
        case InspectionStatus.REJECT:
          counts.reject++;
          categorizedItems[InspectionStatus.REJECT].push(entry);
          break;
      }
    }
  });

  return { counts, categorizedItems };
};
```
