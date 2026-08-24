# 01. ตรรกะการป้องกันและการคัดกรองข้อมูล (Defensive Guarding & Predicate Logic)

หัวข้อนี้อธิบายถึงตรรกะและกระบวนการคิดในการคัดกรองข้อมูล การตรวจสอบสิทธิ์ และการป้องกันความผิดพลาดเชิงรุก (Defensive Programming) โดยใช้ตัวอย่างโค้ดเชิงนามธรรม

---

## 1. Type-Guarded Validation (การตรวจสอบพร้อมบีบ Type ให้แคบลง)

### แนวคิดและปัญหาที่แก้
การตรวจสอบความยาวของ Array ทั่วไป เช่น `if (arr.length > 0)` แม้จะทำให้เรารู้ว่ามีข้อมูล แต่ในเชิง Type System ของ TypeScript ตัวแปร `arr` ยังคงเป็น `string[]` ทั่วไป ซึ่ง Compiler ยังไม่อาจการันตีการเข้าถึง index แรกได้อย่างสมบูรณ์

ผู้พัฒนาจึงสร้างฟังก์ชันตรวจสอบที่เป็น **Custom Type Guard** เพื่อยืนยันว่า `arr` เป็น Tuple ที่มีสมาชิกตัวแรกแน่นอน (`[string, ...string[]]`):

```typescript
/**
 * ตรวจสอบว่า Array มีสมาชิกอย่างน้อย 1 ตัว พร้อมทำ Type Narrowing เป็น Non-empty Tuple
 */
export function hasItems<T>(arr?: T[]): arr is [T, ...T[]] {
  return Boolean(arr && arr.length > 0);
}
```

**ประโยชน์:**
- ปลอดภัยจากการเกิด `undefined` เมื่อเข้าถึงสมาชิกตัวแรก (`arr[0]`)
- นำไปใช้เป็นเงื่อนไขสัจพจน์ (Boolean Invariant) ในการประเมินสิทธิ์ระดับบทบาท (Role Requirements)

---

## 2. Short-Circuiting & Boundary Validation (การตัดจบแบบรวดเร็ว)

### แนวคิดและปัญหาที่แก้
เมื่อต้องตรวจสอบสิทธิ์ของผู้ใช้กับรายการข้อมูลจำนวนมาก การวนลูปตรวจสอบทุกครั้งจะสิ้นเปลืองทรัพยากร และสร้างโค้ดที่ซับซ้อน ผู้พัฒนาใช้หลักการ **Short-Circuiting (Early Exit)** เพื่อข้ามการคำนวณทั้งหมดหากตรงเงื่อนไขสิทธิ์สูงสุด หรือเมื่อไม่มี Input:

```typescript
export interface UserSessionContext {
  user: {
    id: string;
    role: 'SUPER_ADMIN' | 'ADMIN' | 'MANAGER' | 'OPERATOR';
  };
  allowedBoundaries: {
    tenants: string[];
    groups: string[];
    scopes: string[];
  };
}

/**
 * ตรวจสอบว่ารายการ input ที่ส่งเข้ามา อยู่ในขอบเขตที่ผู้ใช้ได้รับอนุญาตทั้งหมดหรือไม่
 */
export const validateAccessBoundary = (
  ctx: UserSessionContext,
  inputs: string[],
  allowedList: string[] = [],
  errorMessage: string = 'Access denied: Out of boundary',
) => {
  // 1. Short-Circuit: ถ้าไม่มี input หรือเป็น Super Admin หรือมีสิทธิ์ครอบคลุม 'ALL' ให้ผ่านทันที
  if (
    !inputs.length ||
    ctx.user.role === 'SUPER_ADMIN' ||
    allowedList.includes('ALL')
  ) {
    return;
  }

  // 2. Validate: ตรวจสอบว่าทุก input อยู่ใน allowed list หรือไม่
  const isAllAllowed = inputs.every((item) => allowedList.includes(item));
  if (!isAllAllowed) {
    throw new ForbiddenException(errorMessage);
  }
};
```

---

## 3. Deadlock Token / Safe Fallback Injection (การบล็อกเมื่อขาด Context)

### แนวคิดและปัญหาที่แก้
ปัญหาคลาสสิกของระบบ Multi-tenant / Row-Level Security (RLS) คือเมื่อผู้ใช้ไม่มีรายการขอบเขตที่ได้รับมอบหมาย (`assigned = []`) หากนำ Array ว่างไปประกอบคำสั่ง SQL `WHERE id IN ()` อาจทำให้เกิด SQL Syntax Error หรือหากเผลอไม่ใส่เงื่อนไข อาจหลุดไป Query ข้อมูลทั้งหมด (Data Leakage)

ผู้พัฒนาแก้ปัญหานี้ด้วย **Deadlock Fallback Pattern**: หากไม่มีข้อมูล ให้ฉีด Token ที่ไม่มีวันตรงกับข้อมูลจริงในฐานข้อมูล (`___BLOCK_ACCESS___` หรือ `1 = 0`):

```typescript
const DEADLOCK_BLOCK_TOKEN = '___BLOCK_ACCESS___';

/**
 * สร้าง FindOperator หรือเงื่อนไขที่ปลอดภัย ป้องกันการรั่วไหลของข้อมูลเมื่อ context ว่างเปล่า
 */
export const createSafeBoundaryFilter = (assignedItems?: string[]): FindOperator<string> => {
  return hasItems(assignedItems) ? In(assignedItems) : In([DEADLOCK_BLOCK_TOKEN]);
};
```

ในระดับ QueryBuilder ใช้หลักการเดียวกัน:
```typescript
if (!hasRequiredScope(user.role, user.assignedBoundaries)) {
  // บล็อกการ Query ทั้งหมดทันทีด้วยเงื่อนไขสัจพจน์เท็จ (Contradiction)
  queryBuilder.andWhere('1 = 0');
  return queryBuilder;
}
```

---

## 4. Role Hierarchy Level Guard (การป้องกันการยกระดับสิทธิ์)

### แนวคิดและปัญหาที่แก้
ป้องกันช่องโหว่ที่ผู้ใช้ในระดับเดียวกันหรือต่ำกว่า พยายามแก้ไขข้อมูลของผู้ใช้ที่มียศสูงกว่า ผ่านการเปรียบเทียบระดับน้ำหนักของบทบาท (Role Level Comparison):

```typescript
const ROLE_WEIGHT: Record<string, number> = {
  SUPER_ADMIN: 0, // สิทธิ์สูงสุด (ค่าน้อย = อำนาจสูง)
  ADMIN: 1,
  MANAGER: 2,
  OPERATOR: 3,
};

/**
 * ป้องกันไม่ให้ผู้ใช้แก้ไขข้อมูลของผู้อื่นที่มี Role เท่ากันหรือสูงกว่า
 */
export const validateRoleHierarchy = (currentUserRole: string, targetUserRole: string) => {
  // ถ้าไม่ใช่ Super Admin และผู้เรียกมีน้ำหนักมากกว่าหรือเท่ากับเป้าหมาย (ระดับต่ำกว่าหรือเท่ากัน)
  if (
    ROLE_WEIGHT[currentUserRole] >= ROLE_WEIGHT[targetUserRole] &&
    currentUserRole !== 'SUPER_ADMIN'
  ) {
    throw new ForbiddenException('Access denied: Insufficient role hierarchy');
  }
};
```

---

## 5. Two-Step Mutation Protocol (ค้นหาเพื่อพิสูจน์สิทธิ์ก่อนอัปเดต/ลบ)

### แนวคิดและปัญหาที่แก้
ORM หลายตัวอาจมีพฤติกรรมละเลยเงื่อนไขที่ซับซ้อน (เช่น Array Operator หรือ Nested Join) ในคำสั่ง `update()` หรือ `delete()` ซึ่งเสี่ยงต่อการอัปเดตข้อมูลผิด Record

ผู้พัฒนาจึงกำหนดกฎเหล็ก **Find-Before-Mutate**:
1. ทำการ `findOne` พร้อมเงื่อนไขสิทธิ์ RLS เพื่อยืนยันว่ามี Record นั้นอยู่จริง และผู้ใช้มีสิทธิ์เข้าถึง
2. หากไม่พบให้โยน `NotFoundException`
3. สั่ง `update` หรือ `delete` โดยระบุ ID ที่ค้นพบโดยตรง

```typescript
async updateResource(
  ctx: UserSessionContext,
  resourceId: number,
  dto: UpdateResourceDto,
): Promise<void> {
  const currentUserId = ctx.user.id;

  // ขั้นที่ 1: ค้นหาพร้อมตรวจสอบสิทธิ์การเข้าถึง (RLS Filter)
  const existingRecord = await this.repository.findOne({
    where: {
      id: resourceId,
      status: ACTIVE_STATUS,
      ...buildUserAccessFilter(ctx),
    },
    relations: { Owner: true },
  });

  if (!existingRecord) {
    throw new NotFoundException('Resource not found or access denied');
  }

  // ขั้นที่ 2: ตรวจสอบความปลอดภัยตามลำดับขั้น
  validateRoleHierarchy(ctx.user.role, existingRecord.Owner.role);

  // ขั้นที่ 3: สั่งอัปเดตข้อมูลผ่าน ID โดยตรง
  await this.repository.update(resourceId, {
    ...dto,
    status: ACTIVE_STATUS,
    updated_by: currentUserId,
  });
}
```
