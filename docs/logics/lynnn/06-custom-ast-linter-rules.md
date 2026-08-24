# 06. การควบคุมคุณภาพโค้ดระดับ AST (Custom AST Linter Rules)

หัวข้อนี้อธิบายถึง Custom ESLint Rules เพื่อบังคับใช้มาตรฐานโค้ด สัจพจน์ความปลอดภัย และ Immutability อัตโนมัติในระดับ Abstract Syntax Tree (AST)

---

## 1. รายการ Custom AST Rules ที่สร้างขึ้น

| ชื่อ Rule | หมวดหมู่ | วัตถุประสงค์และการตรวจสอบ |
| :--- | :--- | :--- |
| `nestjs-readonly-injectables` | Immutability | บังคับให้ Injected Dependency ใน Constructor ต้องเป็น `private readonly` (รองรับ Auto-fix) |
| `typeorm-joint-column-fk` | Constraint Naming | บังคับให้ Relation Foreign Key ระบุชื่อ Constraint ชัดเจน `{table}_{column}_fkey` |
| `nestjs-kebab-case-routes` | API Convention | บังคับให้ HTTP Route Path ทั้งหมดใช้รูปแบบ `kebab-case` |
| `typeorm-safe-transaction` | Reliability | บังคับโครงสร้าง Transaction ให้มี try/commit/catch/rollback/finally/release ครบถ้วน |
| `typeorm-enforce-pagination` | Memory Safety | บังคับให้ Query (`find`, `getMany`) ต้องมี `take` หรือ `limit` เสมอ เพื่อป้องกัน OOM |
| `typeorm-introspected-entity` | Database Invariant | ควบคุม Invariants ใน Entity (ห้าม `@Unique` บน Column ทั่วไป, บังคับ Timestamp Precision 3) |
| `typeorm-new-relation` | Data Integrity | ควบคุมมาตรฐานการตั้งชื่อ Property และ Decorator Relations |

---

## 2. ตัวอย่างการเขียน AST Rule และ Auto-Fixer

### `nestjs-readonly-injectables`
ตรวจจับ Constructor Parameter Properties ในคลาสที่มี `@Injectable` หรือ `@Controller` หากขาดคีย์เวิร์ด `readonly` จะแจ้งเตือนพร้อม Auto-fix เติม `readonly` ให้ทันที:

```javascript
import { AST_NODE_TYPES, ESLintUtils } from '@typescript-eslint/utils';

const createRule = ESLintUtils.RuleCreator((name) => `custom/${name}`);

export const nestjsReadonlyInjectablesRule = createRule({
  name: 'nestjs-readonly-injectables',
  meta: {
    type: 'suggestion',
    docs: {
      description: 'Enforce readonly modifier for injected dependencies in NestJS classes',
    },
    fixable: 'code',
    messages: {
      missingReadonly: 'Dependency injection "{{name}}" should be marked as readonly.',
    },
    schema: [],
  },
  defaultOptions: [],
  create(context) {
    return {
      ClassDeclaration(node) {
        // ตรวจสอบว่าคลาสมี @Injectable หรือ @Controller
        const hasNestDecorator = node.decorators && node.decorators.some((d) => {
          if (d.expression.type === AST_NODE_TYPES.CallExpression) {
            const callee = d.expression.callee;
            return callee.type === AST_NODE_TYPES.Identifier &&
              (callee.name === 'Injectable' || callee.name === 'Controller');
          }
          return false;
        });

        if (!hasNestDecorator) return;

        // หา Constructor
        const ctor = node.body.body.find(
          (el) => el.type === AST_NODE_TYPES.MethodDefinition && el.kind === 'constructor',
        );
        if (!ctor) return;

        // ตรวจสอบพารามิเตอร์แต่ละตัว
        for (const param of ctor.value.params) {
          if (param.type === AST_NODE_TYPES.TSParameterProperty && !param.readonly) {
            let paramName = param.parameter.type === AST_NODE_TYPES.Identifier ? param.parameter.name : 'unknown';

            context.report({
              node: param,
              messageId: 'missingReadonly',
              data: { name: paramName },
              fix(fixer) {
                const sourceCode = context.sourceCode;
                const tokens = sourceCode.getTokens(param);
                const modifierToken = tokens.find(
                  (t) => t.value === 'private' || t.value === 'protected' || t.value === 'public',
                );
                if (modifierToken) {
                  return fixer.insertTextAfter(modifierToken, ' readonly');
                }
                return null;
              },
            });
          }
        }
      },
    };
  },
});
```

---

## 3. การลงทะเบียน Custom Rules ใน ESLint Config

```javascript
export const customRulesPlugin = {
  rules: {
    'nestjs-readonly-injectables': nestjsReadonlyInjectablesRule,
    'nestjs-kebab-case-routes': nestjsKebabCaseRoutesRule,
    'typeorm-joint-column-fk': typeormJointColumnFkRule,
    'typeorm-safe-transaction': typeormSafeTransactionRule,
    'typeorm-enforce-pagination': typeormEnforcePaginationRule,
    'typeorm-introspected-entity': typeormIntrospectedEntityRule,
    'typeorm-new-relation': typeormNewRelationRule,
  },
};
```
