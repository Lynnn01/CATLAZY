# 02. ตรรกะการแปลงและการจัดการข้อมูล (Functional Transformation & Lookup Engines)

หัวข้อนี้สรุปรูปแบบการประมวลผลข้อมูล การจัดกลุ่ม และการแปลงข้อมูลแบบ Functional Programming ของผู้พัฒนา ที่เน้นการลดความซับซ้อนของ Code Branch และเพิ่มประสิทธิภาพในการค้นหาข้อมูล

---

## 1. Pure Mapping Table Pattern (แทนที่ `switch-case` และ `if-else`)

### แนวคิดและปัญหาที่แก้
การเขียน `switch-case` หรือ `if-else` หลายชั้นทำให้โค้ดยาว อ่านยาก และเสี่ยงต่อการลืม `break` หรือครอบคลุมไม่ครบทุกเคส ผู้พัฒนาเลือกแปลงเงื่อนไขทั้งหมดให้กลายเป็น **Data Structure แบบ `Record<Key, Value>`**

```typescript
type RoleType = 'SUPER_ADMIN' | 'ADMIN' | 'MANAGER' | 'OPERATOR';

interface ScopeContext {
  organizationIds?: string[];
  departmentIds?: string[];
  teamIds?: string[];
}

/**
 * ตรวจสอบความพร้อมของข้อมูลขอบเขตตามที่แต่ละบทบาทต้องการ ด้วย Mapping Table
 */
export function hasRequiredScopeByRole(role: RoleType, scope: ScopeContext): boolean {
  const { organizationIds, departmentIds, teamIds } = scope;

  const hasOrg = hasItems(organizationIds);
  const hasDept = hasItems(departmentIds);
  const hasTeam = hasItems(teamIds);

  // Mapping Table กำหนดเงื่อนไขเชิงตรรกะของแต่ละ Role
  const roleRequirementsMap: Record<RoleType, boolean> = {
    ADMIN: hasOrg,
    MANAGER: hasOrg && hasDept,
    OPERATOR: hasOrg && hasDept && hasTeam,
    SUPER_ADMIN: true,
  };

  return Boolean(roleRequirementsMap[role]);
}
```

และสำหรับการจับคู่ Filter เงื่อนไข Query:
```typescript
export const buildRoleFilterCondition = (role: RoleType, scope: ScopeContext) => {
  const orgFilter = createSafeBoundaryFilter(scope.organizationIds);
  const deptFilter = createSafeBoundaryFilter(scope.departmentIds);
  const teamFilter = createSafeBoundaryFilter(scope.teamIds);

  const roleFilterMap: Record<RoleType, object> = {
    ADMIN: { Organization: { id: orgFilter } },
    MANAGER: { Organization: { id: orgFilter }, Department: { id: deptFilter } },
    OPERATOR: { Organization: { id: orgFilter }, Department: { id: deptFilter }, Team: { id: teamFilter } },
    SUPER_ADMIN: {},
  };

  return roleFilterMap[role] ?? {};
};
```

---

## 2. Functional Property Extraction (`pluck` ด้วย `.reduce`)

### แนวคิดและปัญหาที่แก้
เมื่อต้องการดึง Property เฉพาะจาก Array ของ Objects โดยต้องการกรองค่าที่เป็น `null` หรือ `undefined` ออก พร้อมรักษา Type Safety ไว้อย่างแม่นยำ:

```typescript
/**
 * สกัดค่า Property ที่ต้องการจาก Array ของ Objects โดยตัด null/undefined และคืนค่า Type ปลอดภัย
 */
export function pluck<T, K extends keyof T>(
  arr: T[] | undefined,
  key: K,
): NonNullable<T[K]>[] {
  return (arr ?? []).reduce((acc: NonNullable<T[K]>[], item: T) => {
    if (item[key] != null) acc.push(item[key]);
    return acc;
  }, []);
}

// ตัวอย่างการใช้งานสกัด IDs:
export function extractScopeContext(userProfile: UserProfileWithRelations | null) {
  return {
    organizationIds: pluck(userProfile?.Organizations, 'id'),
    departmentIds: pluck(userProfile?.Departments, 'id'),
    teamIds: pluck(userProfile?.Teams, 'id'),
  };
}
```

---

## 3. Lookup Engine ด้วย `new Map()` สำหรับการจับคู่หลายหมวดหมู่

### แนวคิดและปัญหาที่แก้
เมื่อต้องประกอบข้อมูลจากหลายตารางย่อยเข้ากับ Template หรือ Section การวนลูปค้นหาทีละ Record จะทำให้ความเร็วตกเป็น $O(N \times M)$

ผู้พัฒนาแก้ปัญหานี้โดยการสร้าง **Data Lookup Map** เพียงครั้งเดียว แล้วดึงข้อมูลด้วย $O(1)$:

```typescript
interface DataRecordItem {
  categoryKey: string;
  payload: string | null;
  kind: 'image' | 'text' | 'numeric';
}

/**
 * สร้าง Map Lookup เพื่อการเข้าถึงข้อมูลที่เชื่อมโยงกันด้วย O(1)
 */
export const buildLookupEngine = (
  rawImages: { key: string; path: string }[],
  rawMetrics: { key: string; value: string | number }[],
): Map<string, { value: string | null; type: 'image' | 'text' }> => {
  const lookup = new Map<string, { value: string | null; type: 'image' | 'text' }>();

  // จับคู่ข้อมูลประเภทรูปภาพ
  rawImages.forEach((img) => {
    if (img.key) {
      lookup.set(img.key, { value: img.path, type: 'image' });
    }
  });

  // จับคู่ข้อมูลประเภทข้อความ/สถิติ
  rawMetrics.forEach((metric) => {
    if (metric.key) {
      lookup.set(metric.key, { value: String(metric.value), type: 'text' });
    }
  });

  return lookup;
};
```

---

## 4. Multi-Predicate Partitioning (`filterGroupBy`)

### แนวคิดและปัญหาที่แก้
เมื่อต้องการแยกกลุ่มข้อมูลก้อนเดียวออกเป็นหลายหมวดหมู่ตามฟังก์ชันเงื่อนไข (Predicate) ที่แตกต่างกัน โดยไม่ต้องเขียน `filter` ซ้ำหลายรอบ:

```typescript
import _ from 'lodash';

/**
 * จัดกลุ่มข้อมูลตามรายการ Predicate Map หลายๆ เงื่อนไขในคำสั่งเดียว
 */
export function filterGroupBy<T, K extends string | number | symbol>(
  items: T[],
  keys: K[],
  predicateMap: Partial<Record<K, (item: T) => boolean>>,
): Record<K, T[]> {
  return _.zipObject(
    keys,
    keys.map((key) =>
      predicateMap[key] ? _.filter(items, predicateMap[key]) : [],
    ),
  ) as Record<K, T[]>;
}
```

**ตัวอย่างการนำไปใช้:**
```typescript
enum TaskExecutionStatus {
  ON_SCHEDULE = 'ON_SCHEDULE',
  BEHIND_SCHEDULE = 'BEHIND_SCHEDULE',
}

const EXECUTION_PREDICATE_MAP: Record<TaskExecutionStatus, (t: TaskItem) => boolean> = {
  [TaskExecutionStatus.ON_SCHEDULE]: (t) => t.isDelayed === false,
  [TaskExecutionStatus.BEHIND_SCHEDULE]: (t) => t.isDelayed === true,
};

const { ON_SCHEDULE, BEHIND_SCHEDULE } = filterGroupBy(
  completedTasks,
  [TaskExecutionStatus.ON_SCHEDULE, TaskExecutionStatus.BEHIND_SCHEDULE],
  EXECUTION_PREDICATE_MAP,
);
```
