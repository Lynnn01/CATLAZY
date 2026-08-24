# 07. การเข้ารหัสความปลอดภัยและการตรวจ Environment แบบ Fail-Fast (Security Encryption & Fail-Fast Env)

หัวข้อนี้อธิบายถึงตรรกะการเข้ารหัสข้อมูลที่ละเอียดอ่อนระดับ Column ในฐานข้อมูล, การรองรับ TypeORM FindOperator, และการตรวจสอบ Environment Variables แบบ Fail-Fast ด้วย Zod

---

## 1. Transparent Crypto Engine & FindOperator Assertion

### แนวคิดและปัญหาที่แก้
เมื่อข้อมูลในฐานข้อมูลถูกเข้ารหัส (AES-128-ECB) ฟังก์ชัน Encrypt/Decrypt ในชั้น Service หรือ Transformer มักจะพบปัญหาเมื่อถูกเรียกด้วย ORM `FindOperator` (เช่น `Like`, `In`, `IsNull`) แทนที่จะเป็น `string` ธรรมดา

ผู้พัฒนาออกแบบฟังก์ชัน `encrypt`, `decrypt`, และ `hashPassword` ให้รองรับทั้งสองกรณี พร้อมใส่ `console.assert` เพื่อตรวจจับความผิดปกติของโครงสร้างข้อมูลตั้งแต่ช่วง Development:

```typescript
import * as crypto from 'crypto';
import { FindOperator } from 'typeorm';

/**
 * ฟังก์ชันเข้ารหัสที่รองรับทั้ง String ธรรมดา และ ORM FindOperator
 */
export function encrypt(text: string | FindOperator<unknown>): string {
  if (text instanceof FindOperator) {
    console.assert(
      typeof text.value === 'string' || text.value == null,
      'Encrypt FindOperator value must be string, null, or undefined but got ' +
        (Array.isArray(text.value) ? 'array' : typeof text.value),
    );
    // @ts-expect-error : passthrough
    return text.value ?? '';
  }

  if (!text) return text;
  const key = process.env.APP_ENCRYPTION_KEY;
  if (!key || key.length !== 16) {
    throw new Error('Encryption key must be exactly 16 characters');
  }

  const cipher = crypto.createCipheriv('aes-128-ecb', key, null);
  const hex = cipher.update(text, 'utf8', 'hex') + cipher.final('hex');
  return Buffer.from(hex.toUpperCase()).toString('base64');
}

export function decrypt(text: string | FindOperator<unknown>): string {
  if (text instanceof FindOperator) {
    if (process.env.NODE_ENV !== 'production') {
      console.assert(
        typeof text.value === 'string' || text.value == null,
        'Decrypt FindOperator value must be string, null, or undefined',
      );
    }
    // @ts-expect-error : passthrough
    return text.value ?? '';
  }

  if (!text || text.length <= 16) return text;
  const key = process.env.APP_ENCRYPTION_KEY;
  const hex = Buffer.from(text, 'base64').toString('utf8');
  const decipher = crypto.createDecipheriv('aes-128-ecb', key, null);
  return decipher.update(hex, 'hex', 'utf8') + decipher.final('utf8');
}
```

---

## 2. ORM ValueTransformer Integration

### แนวคิด
ผูกฟังก์ชัน `encrypt` และ `decrypt` เข้ากับ Decorator `@Column` ของ Entity เพื่อให้การอ่านและเขียนข้อมูลถูกแปลงอัตโนมัติ (Transparent Encryption) โดยที่ Business Logic ไม่ต้องเรียกฟังก์ชันเข้ารหัสด้วยตนเอง:

```typescript
export const encryptionTransformer: ValueTransformer = {
  to: (value: string | FindOperator<unknown>) => encrypt(value),
  from: (value: string) => decrypt(value),
};

// การใช้งานใน Entity:
@Column({ transformer: encryptionTransformer })
secret_token: string;
```

---

## 3. Fail-Fast Environment Validation ด้วย Zod

### แนวคิดและปัญหาที่แก้
การที่เซิร์ฟเวอร์เปิดขึ้นมาโดยที่ขาด Configuration สำคัญ (เช่น Secret Key สั้นเกินไป, Database URL หาย) อาจทำให้ระบบทำงานผิดพลาดกลางคันหรือเกิดช่องโหว่ความปลอดภัย

ผู้พัฒนาจึงใช้ **Fail-Fast Boot Strategy**: ตรวจสอบ Schema ของ Environment Variables ทั้งหมดตั้งแต่จังหวะเริ่ม Bootstrap ผ่าน `envSchema.safeParse()`:

```typescript
import ms from 'ms';
import { z } from 'zod';

export const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']).default('development'),
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().min(1, 'DATABASE_URL is required'),
  JWT_SECRET: z.string().min(10, 'JWT_SECRET must be at least 10 characters'),
  APP_ENCRYPTION_KEY: z
    .string()
    .min(16, 'APP_ENCRYPTION_KEY must be exactly 16 characters')
    .max(16, 'APP_ENCRYPTION_KEY must be exactly 16 characters'),
  JWT_EXPIRES_IN: z
    .custom<ms.StringValue>((val) => {
      if (val == null || val === '') return false;
      if (typeof val === 'number' || typeof val === 'string') {
        return ms(val as ms.StringValue) !== undefined;
      }
      return false;
    })
    .default('24h'),
});

export function validateEnv(config: NodeJS.ProcessEnv) {
  const parsed = envSchema.safeParse(config);

  if (!parsed.success) {
    console.error(
      '❌ Invalid environment variables:',
      parsed.error.flatten().fieldErrors,
    );
    throw new Error('Invalid environment variables: Server startup aborted'); // หยุดการทำงานทันที
  }

  return parsed.data;
}
```
