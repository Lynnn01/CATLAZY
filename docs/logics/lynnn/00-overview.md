# ภาพรวมตรรกะและรูปแบบการเขียนโค้ด (Developer Coding DNA & Logic Overview)

เอกสารชุดนี้รวบรวม **Logic การคิด, การออกแบบอัลกอริทึม, โครงสร้างข้อมูล และสไตล์การเขียนโค้ด** ของผู้พัฒนา (`lynnn`) โดยมุ่งเน้นที่วิธีคิดเชิงตรรกศาสตร์ (Formal & Predicate Logic), การป้องกันข้อผิดพลาดเชิงรุก (Defensive Programming), และการเขียนโค้ดแบบ Functional Programming ที่กระชับ ตรงประเด็น และมีประสิทธิภาพสูงสุด โดยใช้ตัวอย่างโค้ดเชิงนามธรรมที่เป็นกลาง (Sanitized / Generalized Code Patterns) ไม่ผูกติดกับบริบททางธุรกิจขององค์กรใดองค์กรหนึ่ง

---

## 🌟 ปรัชญาและหัวใจหลักของ Logic (Core Philosophies)

1. **Predicate & Type-Safe First:**
   - ทุกเงื่อนไขต้องพิสูจน์ได้เชิงตรรกะ ไม่มีการเดาข้อมูล
   - ใช้ TypeScript Type Guard (`arr is [string, ...string[]]`, `isPatternSuccess`) เพื่อบีบ Type ให้แคบลงจริงในระดับ Compiler
2. **Defensive by Default (ปลอดภัยไว้ก่อน):**
   - เมื่อข้อมูลสิทธิ์หรือ Context ขาดหาย ระบบจะฉีดเงื่อนไขที่เป็นไปไม่ได้ (`BLOCK_ACCESS` หรือ `1 = 0`) เพื่อป้องกัน Data Leak ทันที
   - การแก้ไขหรือลบข้อมูลต้องใช้กฎ **Find-Before-Mutate** (ตรวจการมีอยู่และสิทธิ์ก่อนอัปเดตเสมอ)
3. **Data-Driven & Table Mappings:**
   - หลีกเลี่ยง `if-else` หรือ `switch-case` ซ้อนกันหลายชั้น โดยแปลงเป็น `Record<Key, Value>` หรือ `Map` Lookup Tables
   - แยกข้อมูลขนาดใหญ่ไปไว้ใน `.mapping.ts` และเก็บเฉพาะ Pure Logic ไว้ใน `.helper.ts`
4. **Deterministic Priority Chains:**
   - การประเมินสถานะของระบบจะใช้กฎลำดับความสำคัญชัดเจน (Cascade Priority) โดยมีกฎ Veto สำหรับข้อผิดพลาด
5. **AST-Level Quality Enforcement:**
   - ควบคุมมาตรฐานความปลอดภัยและ Immutability ถึงระดับ Syntax Tree ผ่าน Custom ESLint Rules
6. **Fail-Fast & Transparent Security:**
   - ตรวจสอบความถูกต้องของ Environment Variables ทันทีตอนเริ่มบูตระบบ (Fail-Fast)
   - จัดการเข้ารหัสข้อมูลระดับ Column ในฐานข้อมูลแบบโปร่งใส (Transparent Column Transformer)
7. **Concurrency & Non-blocking Aggregation:**
   - รวบรวมข้อมูลจากหลายโดเมนพร้อมกันด้วย `Promise.all`
   - ป้องกันข้อผิดพลาดทางคณิตศาสตร์ เช่น Zero-Division ในทุกสูตรคำนวณ

---

## 📑 สารบัญเอกสาร (Documentation Index)

| ลำดับ | ไฟล์เอกสาร | คำอธิบายหัวข้อ |
| :--- | :--- | :--- |
| 01 | [`01-defensive-guarding-and-predicate-logic.md`](./01-defensive-guarding-and-predicate-logic.md) | ตรรกะการป้องกัน สิทธิ์ และการคัดกรองข้อมูลระดับแถว (RLS & Type Guards) |
| 02 | [`02-functional-transformation-and-lookup-engines.md`](./02-functional-transformation-and-lookup-engines.md) | การแปลงข้อมูล Functional, Mapping Tables และ Lookup Engines |
| 03 | [`03-mathematical-and-metric-modeling.md`](./03-mathematical-and-metric-modeling.md) | สูตรคณิตศาสตร์ การ Normalize เวลา และโมเดลตัวชี้วัด (SLA & Metrics) |
| 04 | [`04-deterministic-priority-state-machine.md`](./04-deterministic-priority-state-machine.md) | State Machine เชิงลำดับความสำคัญและกฎ Veto (Status Cascade Logic) |
| 05 | [`05-function-signatures-and-coding-habits.md`](./05-function-signatures-and-coding-habits.md) | มาตรฐาน Parameter, ความเรียบง่าย และนิสัยการเขียนโค้ด (Coding Conventions) |
| 06 | [`06-custom-ast-linter-rules.md`](./06-custom-ast-linter-rules.md) | การสร้าง Custom Linter กฎ AST เพื่อบังคับใช้มาตรฐานอัตโนมัติ (ESLint Rules) |
| 07 | [`07-security-encryption-and-fail-fast-env.md`](./07-security-encryption-and-fail-fast-env.md) | การเข้ารหัส AES-128-ECB, Column Transformer และ Fail-Fast Zod Env |
| 08 | [`08-http-interception-and-error-normalization.md`](./08-http-interception-and-error-normalization.md) | Idempotent Response Wrapping และ Global Error Normalization |
| 09 | [`09-auth-lifecycle-and-2fa-token-logic.md`](./09-auth-lifecycle-and-2fa-token-logic.md) | วงจรการยืนยันตัวตน, Assigned Context, 2FA OTP และ Development Bypass |
| 10 | [`10-concurrent-aggregation-and-dashboard-patterns.md`](./10-concurrent-aggregation-and-dashboard-patterns.md) | การประมวลผลพร้อมกัน (Concurrency `Promise.all`), การป้องกัน Zero-Division และ Higher-Order Processors |
