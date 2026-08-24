# 09. วงจรการยืนยันตัวตนและตรรกะ 2FA OTP (Auth Lifecycle & 2FA Token Logic)

หัวข้อนี้อธิบายถึงตรรกะการยืนยันตัวตน (Authentication), การออก JWT Token พร้อม Assigned Boundary Context, การสร้าง/ตรวจสอบรหัส 2FA OTP, การสร้าง Bypass สำหรับ Development, และการจัดการหน่วยความจำของ OTP ที่หมดอายุ

---

## 1. การประกอบ TokenPayload พร้อมสิทธิ์ขอบเขตพื้นที่ (Assigned Scope Extraction)

### แนวคิด
เมื่อผู้ใช้ Login สำเร็จ ระบบจะไม่เพียงแค่ sign ข้อมูล user พื้นฐานลงใน JWT แต่จะทำการเชื่อมโยงขอบเขตที่ได้รับมอบหมาย (`assignedScopes`) ผ่าน User Scope Entity ทันที:

```typescript
export interface SessionTokenPayload {
  user: {
    userId: string;
    accountCode: string;
    role: string;
  };
  assigned: {
    tenantIds: string[];
    groupScopeIds: string[];
    subScopeIds: string[];
  };
}

async generateUserSessionToken(user: UserAccountEntity): Promise<AuthTokensResponse> {
  // ค้นหาขอบเขตสิทธิ์ที่ user ได้รับมอบหมายจากฐานข้อมูล
  const userScopeRecord = await this.scopeRepository.findOne({
    where: { userId: user.id },
    relations: { Tenants: true, Groups: true, SubGroups: true },
  });

  const extractedScope = {
    tenantIds: pluck(userScopeRecord?.Tenants, 'id'),
    groupScopeIds: pluck(userScopeRecord?.Groups, 'id'),
    subScopeIds: pluck(userScopeRecord?.SubGroups, 'id'),
  };

  const payload: SessionTokenPayload = {
    user: {
      userId: user.id,
      accountCode: user.code,
      role: user.role,
    },
    assigned: extractedScope,
  };

  return {
    accessToken: await this.jwtService.signAsync(payload, { expiresIn: '15m' }),
    refreshToken: await this.jwtService.signAsync(payload, { expiresIn: '7d' }),
  };
}
```

---

## 2. ตรรกะการสร้าง 2FA OTP และ Development Bypass

### แนวคิดและปัญหาที่แก้
1. ใน Production: รหัส OTP ต้องเป็นตัวเลขสุ่ม 6 หลัก (`100000 - 999999`) และ Ref ID เป็น Alphanumeric 6 ตัวอักษร
2. ใน Development / Test: การต้องเปิดดูอีเมลทุกรอบการ Test ทำให้การพัฒนาล่าช้า ผู้พัฒนาจึงสร้าง **Deterministic Bypass Mode** โดยใช้ค่าคงที่ (`000000` / `BYPASS`) เมื่อ `NODE_ENV` เป็น `development` หรือ `test`
3. อายุของ OTP: กำหนดให้หมดอายุภายใน 5 นาทีแบบตายตัว (`now + 5 * 60000`)

```typescript
const OTP_DEV_PASSCODE = '000000';
const OTP_DEV_REF_ID = 'BYPASS';
const OTP_LIFETIME_MS = 5 * 60 * 1000; // 5 นาที

export async function generateOtpChallenge(
  username: string,
  environment: string,
) {
  const now = new Date();
  const expireTime = new Date(now.getTime() + OTP_LIFETIME_MS);

  const isDevelopment = ['development', 'test'].includes(environment);

  const code = isDevelopment
    ? OTP_DEV_PASSCODE
    : Math.floor(100000 + Math.random() * 900000).toString();

  const refId = isDevelopment
    ? OTP_DEV_REF_ID
    : Math.random().toString(36).substring(2, 8).toUpperCase();

  const otpRecord = await this.otpRepository.save({
    code,
    refId,
    username,
    expire: expireTime,
  });

  return {
    refId: otpRecord.refId,
    expire: otpRecord.expire,
  };
}
```

---

## 3. Single-Use Invariant & Expired Cleanup

### แนวคิด
- **Single-Use Guard:** เมื่อผู้ใช้กรอก OTP ถูกต้องแล้ว รหัสจะต้องถูกลบออกจากฐานข้อมูลทันที (`delete(record.id)`) เพื่อป้องกันการนำกลับมาใช้ซ้ำ (Replay Attack)
- **Batch Expired Cleanup:** มีฟังก์ชันลบขยะ OTP ที่หมดอายุด้วยเงื่อนไข `LessThan(now)` แบบเป็นชุด

```typescript
async verifyOtpChallenge(dto: VerifyOtpDto): Promise<void> {
  const otpRecord = await this.otpRepository.findOne({
    where: {
      code: dto.code,
      refId: dto.refId,
      username: dto.username,
    },
  });

  if (!otpRecord) {
    throw new BadRequestException('Invalid OTP passcode or reference ID');
  }

  if (otpRecord.expire < new Date()) {
    throw new BadRequestException('OTP passcode has expired');
  }

  // ลบทันทีหลังจากยืนยันตัวตนสำเร็จ (Single-Use Invariant)
  await this.otpRepository.delete(otpRecord.id);
}

async cleanExpiredOtps(): Promise<void> {
  const now = new Date();
  const expiredRecords = await this.otpRepository.find({
    where: { expire: LessThan(now) },
    take: 5000,
  });

  if (expiredRecords.length > 0) {
    await this.otpRepository.delete(expiredRecords.map((r) => r.id));
  }
}
```
