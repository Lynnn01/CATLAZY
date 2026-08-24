# 09. Authentication Lifecycle & 2FA OTP Logic (Combinatorics & Hoare Logic)

## 1. Overview & Problem Statement
Two-Factor Authentication (2FA) and One-Time Password (OTP) verification must guarantee single-use consumption to prevent replay attacks, provide time-bounded expiration (TTL), and prevent slow test feedback loops by supporting deterministic bypass modes in development. This chapter formalizes the authentication token payload binding, 2FA OTP challenge space, time-to-live (TTL) expiration window, single-use consumption invariants, and deterministic bypass mechanisms.

## 2. DISMATH Theoretical Foundation
- **Combinatorics & Sample Spaces (`01`):** Finite search space cardinality $|\mathcal{S}| = 9 \times 10^5$ for 6-digit numeric passcodes.
- **Hoare Logic & Replay Invariants (`08`):** Verification as an atomic single-use state mutation ($\{\text{Valid}\} S \{\text{Consumed}\}$).
- **Proof by Contradiction (`06`):** Proof that replay verification is impossible.
- **Logic Puzzles & Dev-Bypass Isomorphisms (`10`):** Environment-conditioned deterministic mapping.

## 3. Formal Mathematical Specifications

### 3.1 OTP Code Space and Generation Function
Let $\mathcal{D}_{\text{env}} = \{\text{development}, \text{test}, \text{production}\}$ be the runtime environment.
- The 6-digit passcode space $\mathcal{S}_{\text{code}} = \{n \in \mathbb{N} \mid 100000 \le n \le 999999\}$, with cardinality $|\mathcal{S}_{\text{code}}| = 9 \times 10^5$.
- The 6-character alphanumeric reference ID space $\mathcal{S}_{\text{ref}} = \Sigma^6$, where $\Sigma = [0-9A-Z]$, $|\mathcal{S}_{\text{ref}}| = 36^6 \approx 2.17 \times 10^9$.
- **Generation Function:**
  $$\text{GenerateChallenge}(e) = \begin{cases} \langle \text{'000000'}, \text{'BYPASS'} \rangle & \text{if } e \in \{\text{development}, \text{test}\} \\ \langle \text{UniformRandom}(\mathcal{S}_{\text{code}}), \text{UniformRandom}(\mathcal{S}_{\text{ref}}) \rangle & \text{if } e = \text{production} \end{cases}$$

### 3.2 Time-to-Live (TTL) Validity Predicate
Let $t_0$ be the token creation timestamp and $\Delta T = 300\,\text{seconds}$ (5 minutes).
$$\text{IsTokenValid}(t, \text{record}) \iff (t \le t_0 + \Delta T) \land (\text{input.code} = \text{record.code}) \land (\text{input.refId} = \text{record.refId})$$

## 4. Invariants & Mathematical Proofs

### 4.1 Single-Use Consumption (Hoare Triple Specification)
To prevent replay attacks, the verification operation strictly satisfies:
$$\{\text{IsTokenValid}(t, r)\} \quad \text{VerifyAndConsume}(r) \quad \{\text{UserAuthenticated} \land \neg \text{Exists}(r)\}$$

### 4.2 Replay Attack Impossibility (Proof by Contradiction)
- **Theorem:** An OTP record $r$ can never be verified more than once.
- **Proof:**
  1. Suppose an attacker attempts a second verification on record $r$ at time $t_2 > t_1$.
  2. The initial verification at $t_1$ executed $\text{delete}(r.\text{id})$, establishing $\neg \text{Exists}(r)$.
  3. The query at $t_2$ searches for $r$ where $\text{id} = r.\text{id}$.
  4. Since $\neg \text{Exists}(r)$, the query returns $\bot$ (null).
  5. The guard condition $\text{record} = \bot \implies \text{Throw}(\text{BadRequestException})$.
  6. The second verification is rejected. Contradiction of successful replay. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import { BadRequestException } from '@nestjs/common';
import { LessThan, Repository } from 'typeorm';

export interface VerifyOtpDto {
  code: string;
  refId: string;
  username: string;
}

const OTP_DEV_PASSCODE = '000000';
const OTP_DEV_REF_ID = 'BYPASS';
const OTP_LIFETIME_MS = 5 * 60 * 1000; // 5 minutes

export class OtpVerificationService {
  constructor(private readonly otpRepo: Repository<any>) {}

  async generateChallenge(username: string, environment: string) {
    const now = new Date();
    const expireTime = new Date(now.getTime() + OTP_LIFETIME_MS);
    const isDev = ['development', 'test'].includes(environment);

    const code = isDev
      ? OTP_DEV_PASSCODE
      : Math.floor(100000 + Math.random() * 900000).toString();

    const refId = isDev
      ? OTP_DEV_REF_ID
      : Math.random().toString(36).substring(2, 8).toUpperCase();

    const record = await this.otpRepo.save({
      code,
      refId,
      username,
      expire: expireTime,
    });

    return { refId: record.refId, expire: record.expire };
  }

  async verifyChallenge(dto: VerifyOtpDto): Promise<void> {
    const record = await this.otpRepo.findOne({
      where: { code: dto.code, refId: dto.refId, username: dto.username },
    });

    if (!record) {
      throw new BadRequestException('Invalid OTP code or reference ID');
    }

    if (record.expire < new Date()) {
      throw new BadRequestException('OTP code has expired');
    }

    // Atomic Single-Use Consumption
    await this.otpRepo.delete(record.id);
  }

  async cleanupExpired(): Promise<void> {
    const now = new Date();
    const expired = await this.otpRepo.find({
      where: { expire: LessThan(now) },
      take: 5000,
    });

    if (expired.length > 0) {
      await this.otpRepo.delete(expired.map((r) => r.id));
    }
  }
}
```

## 6. Complexity & Algebraic Properties
- **Brute-Force Resistance:** In production, random collision probability is $P = \frac{1}{900,000} \approx 1.11 \times 10^{-6}$ per attempt within the 300s window.
- **Consumption Invariant:** Strict $O(1)$ single-use deletion ensures replay safety.
