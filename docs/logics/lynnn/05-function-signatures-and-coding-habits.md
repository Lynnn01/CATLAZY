# 05. ลายเซ็นฟังก์ชันและโครงสร้างการจัดวางโค้ด (Function Signature & Coding Habits)

หัวข้อนี้รวบรวมมาตรฐาน ลายเซ็นฟังก์ชัน (Function Signatures) กฎการตั้งชื่อ และข้อตกลงการเขียนโค้ด (Coding Conventions) ที่ปรากฏในโปรเจกต์ของผู้พัฒนา

---

## 1. Context-First Parameter Rule (ส่งผ่าน Context สม่ำเสมอ)

### ข้อตกลง
ในทุก Controller, Service, และ Helper ฟังก์ชันที่เกี่ยวข้องกับการเข้าถึงข้อมูล ต้องรับ Context ของผู้ใช้ (`ctx: UserSessionContext`) เป็น **พารามิเตอร์ตัวแรกเสมอ**:

```typescript
// Controller Layer
@Get(':id')
async findOne(@Req() ctx: UserSessionContext, @Param('id') id: string) { ... }

@Post()
async create(@Req() ctx: UserSessionContext, @Body() dto: CreateResourceDto) { ... }

// Service Layer
async findOne(ctx: UserSessionContext, id: number) { ... }
async create(ctx: UserSessionContext, dto: CreateResourceDto) { ... }

// Helper Layer
async validateAndAssignScopes(ctx: UserSessionContext, dto: CreateResourceDto, entity: ResourceEntity) { ... }
```

**ประโยชน์:**
- ไม่เกิดความสับสนเรื่องลำดับ Argument เมื่อส่งต่อ Context ข้าม Layer
- ป้องกันการลืมส่งข้อมูลสิทธิ์และขอบเขตความปลอดภัย (RLS)

---

## 2. Separation of Data Mappings & Logic Files (แยกข้อมูลออกจากอัลกอริทึม)

### ข้อตกลง
สำหรับ Feature ที่มีข้อมูลคงที่ (Constants) หรือการจับคู่ (Mappings) ขนาดใหญ่ ให้แยกออกเป็นไฟล์ `.mapping.ts` เสมอ เพื่อให้ไฟล์ `.helper.ts` มีเฉพาะ Pure Function และ Algorithmic Logic:

```
src/modules/core/task-workflow/
├── helper/
│   ├── task-workflow.mapping.ts   # บรรจุ Record / Array Mappings ขนาดใหญ่
│   └── task-workflow.helper.ts    # บรรจุฟังก์ชันคำนวณและประมวลผล (Pure Logic)
├── task-workflow.controller.ts
├── task-workflow.service.ts
└── task-workflow.module.ts
```

---

## 3. No-Class Static Wrappers (ใช้ Plain Exported Functions)

### ข้อตกลง
หลีกเลี่ยงการสร้าง Class ที่มีแต่ `static` methods (เช่น `class DateUtils { static format() }`) แต่ให้ใช้การ `export const format = () => ...` เป็น Plain Functions แทน:

```typescript
// ✅ สไตล์ที่คุณใช้: Plain Exported Functions
export const minutesDiffSeconds = (dateLeft: Date, dateRight: Date): number =>
  differenceInSeconds(dateLeft, dateRight) / 60;

export const createMetric = (title: string, value: string | number, unit: string) => ({
  title,
  value,
  unit,
});

// ❌ สิ่งที่ไม่ใช้: Class Wrapper ที่ไม่จำเป็น
export class UtilityHelper {
  public static minutesDiffSeconds(dateLeft: Date, dateRight: Date): number {
    return differenceInSeconds(dateLeft, dateRight) / 60;
  }
}
```

**ประโยชน์:**
- ลด Overhead ของ Class Declaration ใน JavaScript Engine
- ช่วยให้ Bundler ทำ Tree-Shaking ตัดโค้ดที่ไม่ถูกเรียกใช้ทิ้งได้ง่าย

---

## 4. หลีกเลี่ยง Fallback ปลอมและการ Fail-Fast (No Fake Fallbacks)

### ข้อตกลง
ไม่ใส่ค่า Default หลอกๆ เพื่อให้โค้ดผ่านไปได้โดยไร้การตรวจสอบ เช่น `updated_by: currentUserId || 'system'` หากข้อมูลตัวตนเป็นสิ่งจำเป็น ต้องตรวจสอบตั้งแต่ระดับ Guard หรือโยน Exception ทันที:

```typescript
// ✅ สไตล์ที่คุณใช้: ชัดเจนและ Fail-Fast
const userId = ctx.user.id;
await this.repository.update(id, { updated_by: userId });

// ❌ สิ่งที่หลีกเลี่ยง:
await this.repository.update(id, { updated_by: userId || 'system' });
```

---

## 5. Standard Mutation Return Protocol (`Promise<void>`)

### ข้อตกลง
ฟังก์ชัน `update()` และ `remove()` ทั้งใน Controller และ Service จะคืนค่าเป็น `Promise<void>` (HTTP 200/204) เท่านั้น ไม่ return Entity ออกไปโดยไม่จำเป็น เพื่อลด Network Payload Churn และรักษาความเร็วของ API
