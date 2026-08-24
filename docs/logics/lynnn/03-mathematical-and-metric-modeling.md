# 03. ตรรกะการคำนวณและสร้างโมเดลตัวชี้วัด (Mathematical & Metric Modeling)

หัวข้อนี้อธิบายถึงสูตรคณิตศาสตร์ การแปลงหน่วยเวลา การกำหนดกรอบเวลาแบบไดนามิก และโครงสร้างข้อมูลตัวชี้วัด (Metric Structure) ที่ผู้พัฒนาออกแบบไว้

---

## 1. การปรับค่าเวลาให้เป็นมาตรฐาน (Standard Time Normalization)

### แนวคิด
การคำนวณระยะเวลาในเชิงธุรกิจ (Service Agreement, เวลาตอบสนอง, เวลาแก้ไขปัญหา) มีความเสี่ยงต่อการผิดพลาดจากหน่วยเวลาที่กระจัดกระจาย (มิลลิวินาที, วินาที, นาที, ชั่วโมง) 

ผู้พัฒนาเลือกแปลงผลต่างของเวลาทุกคู่ให้อยู่ในหน่วย **นาที (Floating-point Minutes)** เป็นค่ามาตรฐานกลาง:

$$\Delta t = \frac{\text{differenceInSeconds}(T_{\text{end}}, T_{\text{start}})}{60}$$

```typescript
import { differenceInSeconds } from 'date-fns';

/**
 * คำนวณความต่างของเวลาสองจุดให้ออกมาเป็นหน่วยนาที (ทศนิยม)
 */
export const minutesDiffSeconds = (dateLeft: Date, dateRight: Date): number =>
  differenceInSeconds(dateLeft, dateRight) / 60;
```

---

## 2. Dynamic Time Thresholding (กรอบเวลาเตือนภัยและสถานะ Agreement)

### แนวคิดและสูตรคำนวณ
กำหนดให้ $D_{\text{target}}$ คือระยะเวลาเป้าหมายที่กำหนด (นาที) และ $k = 0.6$ (เกณฑ์เร่งด่วน $60\%$):

1. **สถานะเกินกำหนด (Overdue / Breached):**
   $$\Delta t \ge D_{\text{target}}$$
2. **สถานะใกล้เกินกำหนด / เร่งด่วน (Almost Overdue / Warning Window):**
   $$0.6 \times D_{\text{target}} \le \Delta t < D_{\text{target}}$$
3. **สถานะปกติ (Normal Operation):**
   $$\text{status} \in \text{UnresolvedStatuses} \land \Delta t < 0.6 \times D_{\text{target}}$$

```typescript
const WARNING_THRESHOLD_RATIO = 0.6; // 60% ของกรอบเวลาทั้งหมด

export const isTimeOverdue = (targetDuration: number, date: { create: Date; now: Date }): boolean => {
  const elapsed = minutesDiffSeconds(date.now, date.create);
  return elapsed >= targetDuration;
};

export const isTimeInWarningWindow = (targetDuration: number, date: { create: Date; now: Date }): boolean => {
  const elapsed = minutesDiffSeconds(date.now, date.create);
  return elapsed >= targetDuration * WARNING_THRESHOLD_RATIO && elapsed < targetDuration;
};
```

---

## 3. สูตรคำนวณค่าปรับส่วนเกินเวลา (Penalty Formula)

### แนวคิดและสูตรคำนวณ
เมื่อเวลาดำเนินการเกินกว่าเป้าหมายที่ตกลงไว้ ระบบจะคำนวณค่าปรับตามชั่วโมงส่วนเกิน โดยกำหนดอัตรา $\text{RATE\_PER\_HOUR}$:

$$\text{OverdueMinutes} = \max(0, \Delta t - D_{\text{target}})$$
$$\text{Penalty}(\text{Item}) = \left( \frac{\text{OverdueMinutes}}{60} \right) \times \text{RATE\_PER\_HOUR}$$

```typescript
const PENALTY_RATE_PER_HOUR = 500; // อัตราค่าปรับมาตรฐานต่อชั่วโมง

export const calculatePenalty = (elapsedMinutes: number, targetDurationMinutes: number): number => {
  const overdueMinutes = Math.max(0, elapsedMinutes - targetDurationMinutes);
  return (overdueMinutes / 60) * PENALTY_RATE_PER_HOUR;
};
```

และในระดับ SQL Aggregation:
```sql
COALESCE(SUM((EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - record.create_date)) / 60 - record.duration_minutes) / 60 * :penaltyRatePerHour), 0)
```

---

## 4. เวลาเริ่มตอบสนองแรกและเวลาเสร็จสิ้นครั้งแรก (Response & Completion Time)

### 1. เวลาเริ่มตอบสนองแรก (First Action Response)
ค้นหา Transition Log ที่เปลี่ยนสถานะเป็น "กำลังดำเนินการ" ที่เกิดขึ้นเร็วที่สุด:
$$t_{\text{action}} = \min_{s \in \text{Logs}, s.\text{status}=\text{IN\_PROGRESS}} (T_{s.\text{create\_date}})$$
$$t_{\text{response}} = \frac{t_{\text{action}} - T_{\text{create}}}{60} \quad (\text{นาที})$$

```typescript
export const getFirstResponseMinutes = (item: IncidentItem): number | null => {
  const actionDate = _.minBy(
    item.StatusLogs.filter((log) => log.status === STATUS_IN_PROGRESS),
    (log) => new Date(log.create_date).getTime(),
  )?.create_date;

  if (!actionDate || actionDate < item.create_date) return null;
  return minutesDiffSeconds(actionDate, item.create_date);
};
```

### 2. เวลาที่แก้ไขปัญหาเสร็จสมบูรณ์ครั้งแรก (First Completion Date)
ค้นหา Transition Log ที่เปลี่ยนสถานะเป็น "เสร็จสิ้น" ที่มีวันที่ยืนยันไม่น้อยกว่าเวลาสร้าง:
```typescript
export const getFirstCompletionDate = (item: IncidentItem): Date | undefined => {
  const completedStatus = _.minBy(
    item.StatusLogs.filter(
      (log) =>
        log.status === STATUS_COMPLETED &&
        new Date(log.confirm_date).getTime() >= new Date(item.create_date).getTime(),
    ),
    (log) => new Date(log.confirm_date).getTime(),
  );

  return completedStatus ? new Date(completedStatus.confirm_date) : undefined;
};
```

---

## 5. Hierarchical Metric Data Structure (โมเดลตัวชี้วัดแบบมีโครงสร้าง)

### แนวคิด
ไม่ส่งข้อมูลสถิติเป็นแค่ตัวเลขหรือสตริงเดี่ยวๆ แต่จัดโครงสร้างให้มี Title/Label, Value, Description, และ Unit ชัดเจน เพื่อความยืดหยุ่นในการแสดงผล Dashboard:

```typescript
export type ContextSubMetric = {
  label: string;
  value: string | number | ContextSubMetric[];
  unit?: string;
};

export const createMetric = (
  title: string,
  value: string | number | ContextSubMetric[],
  description: string | number,
  unit: string,
) => ({
  title,
  value: Array.isArray(value) ? value : String(value),
  description: String(description),
  unit,
});

export const createSubMetric = (
  label: string,
  value: string | number | ContextSubMetric[],
  unit?: string,
): ContextSubMetric => ({
  label,
  value,
  unit,
});
```

---

## 6. Math Clamping Operations (การควบคุมขอบเขตตัวเลข)

### แนวคิด
ป้องกันการส่งค่า Page ที่ติดลบ หรือค่า Limit ที่มากเกินไปจนทำให้หน่วยความจำเซิร์ฟเวอร์เต็ม (Memory Exhaustion) ด้วย Math Clamp:

```typescript
const MAX_QUERY_LIMIT = 5000;

export const clampPaginationParams = ({ page, limit }: { page?: number; limit?: number }) => {
  const safePage = Math.max(page || 1, 1);
  const safeLimit = Math.min(Math.max(limit || 10, 1), MAX_QUERY_LIMIT);

  return { safePage, safeLimit };
};
```
