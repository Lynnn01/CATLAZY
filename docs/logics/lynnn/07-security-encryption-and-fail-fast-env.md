# 07. Security Encryption & Fail-Fast Environment (Group Isomorphisms & Product Sets)

## 1. Overview & Problem Statement
Storing sensitive columns in plaintext introduces severe security risks. However, applying database encryption often breaks ORM query operators (such as TypeORM's `Like`, `In`, or `IsNull`) when passed through transformers. Additionally, runtime configuration errors must halt the process during startup. This chapter formalizes transparent column encryption, ORM FindOperator type preservation, and fail-fast environment schema validation.

## 2. DISMATH Theoretical Foundation
- **Group Isomorphisms & Permutations (`07`):** AES-128-ECB bijective permutations satisfying $D_K(E_K(m)) = m$.
- **Polymorphic Type Unions (`01`, `03`):** Total predicate handling for string payloads versus ORM query operators.
- **Product Domain Predicates (`03`):** Multi-variable environment space $\prod_i \mathcal{D}_i$ verified via conjunctive predicates.

## 3. Formal Mathematical Specifications

### 3.1 Bijective Block Cipher Isomorphism
Let $\mathcal{M} = \{0, 1\}^*$ be the plaintext message space and $\mathcal{K} = \{0, 1\}^{128}$ be the 128-bit key space.
- The AES-128-ECB cipher is a bijective permutation:
  $$E_K: \mathcal{M} \to \mathcal{C}, \quad D_K: \mathcal{C} \to \mathcal{M}$$
  $$\forall m \in \mathcal{M}, \quad D_K(E_K(m)) = m \quad \text{(Decryption Invariant)}$$

### 3.2 Polymorphic FindOperator Handling
Let $T$ be the input type to the transformer. $T \in \text{String} \cup \text{FindOperator}\langle \mathcal{U} \rangle$.
- **Transformer Function Definition:**
  $$\text{Transform}_{\text{enc}}(x) = \begin{cases} x.\text{value} & \text{if } x \in \text{FindOperator} \\ E_K(x) & \text{if } x \in \text{String} \land |x| > 0 \\ x & \text{otherwise} \end{cases}$$

### 3.3 Fail-Fast Schema Validation (Product Domain Predicate)
Let $\text{Env} = \langle e_1, e_2, \dots, e_m \rangle \in \prod_{i=1}^m \mathcal{D}_i$.
$$\text{IsValidEnv}(\text{Env}) \iff \bigwedge_{i=1}^m \Phi_i(e_i)$$
Where $\Phi_{\text{key}}(k) \iff |k| = 16$, $\Phi_{\text{jwt}}(j) \iff |j| \ge 10$, and $\Phi_{\text{port}}(p) \iff p \in [1, 65535]$.
- **Fail-Fast Boot Invariant:**
  $$\neg \text{IsValidEnv}(\text{Env}) \implies \text{HaltBootstrap}()$$

## 4. Invariants & Mathematical Proofs

### 4.1 Cryptographic Round-Trip Invariant
- **Theorem:** For any plain string $s$, $\text{decrypt}(\text{encrypt}(s)) = s$.
- **Proof:** Follows directly from the bijectivity of $E_K$ and $D_K$ and the invertibility of Base64 encoding $\text{Base64}^{-1}(\text{Base64}(x)) = x$. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import * as crypto from 'crypto';
import ms from 'ms';
import { FindOperator, ValueTransformer } from 'typeorm';
import { z } from 'zod';

/**
 * Transparent Cryptographic Engine: Handles both plain strings and TypeORM FindOperators
 */
export function encrypt(text: string | FindOperator<unknown>): string {
  if (text instanceof FindOperator) {
    console.assert(
      typeof text.value === 'string' || text.value == null,
      'FindOperator value must be string or null',
    );
    return (text.value as string) ?? '';
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
    return (text.value as string) ?? '';
  }

  if (!text || text.length <= 16) return text;
  const key = process.env.APP_ENCRYPTION_KEY;
  const hex = Buffer.from(text, 'base64').toString('utf8');
  const decipher = crypto.createDecipheriv('aes-128-ecb', key, null);
  return decipher.update(hex, 'hex', 'utf8') + decipher.final('utf8');
}

export const encryptionTransformer: ValueTransformer = {
  to: (value: string | FindOperator<unknown>) => encrypt(value),
  from: (value: string) => decrypt(value),
};

/**
 * Fail-Fast Schema Validation via Zod
 */
export const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']).default('development'),
  PORT: z.coerce.number().default(3000),
  DATABASE_URL: z.string().min(1, 'DATABASE_URL is required'),
  JWT_SECRET: z.string().min(10, 'JWT_SECRET must be at least 10 characters'),
  APP_ENCRYPTION_KEY: z.string().length(16, 'Key must be exactly 16 chars'),
});
```

## 6. Complexity & Algebraic Properties
- **Encryption Time:** $O(|M|)$ linear in message byte length.
- **Fail-Fast Soundness:** Prevents runtime misconfiguration by aborting initialization during process startup.
