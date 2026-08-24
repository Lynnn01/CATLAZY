# 01. Defensive Guarding & Predicate Logic (Predicate Logic & Proofs)

## 1. Overview & Problem Statement
In multi-tenant, role-based backend architectures, data leakage often occurs when an unauthenticated or partially authorized request passes empty filter arrays to database queries, inadvertently selecting all records. Furthermore, runtime mutations may target non-existent or inaccessible entities if the system does not assert access boundaries before updating. This chapter formalizes defensive guarding, boundary predicates, row-level security (RLS), and two-step mutation protocols.

## 2. DISMATH Theoretical Foundation
- **Propositional Logic (`01`):** Truth values, boolean invariants, and short-circuiting implications ($p \to q$).
- **Predicate Logic & Quantifiers (`03`):** Universal quantification ($\forall x \in \mathcal{I}, P(x)$) over input collections and existential witnesses ($\exists x$).
- **Proof by Contradiction (`06`):** Proof that deadlock contradiction tokens guarantee zero record disclosure ($p \land \neg q \to \mathbf{F}$).
- **Hoare Logic (`08`):** Pre-condition and post-condition assertions ($\{P\} S \{Q\}$) for safe database mutations.

## 3. Formal Mathematical Specifications

### 3.1 Non-Empty Tuple Type-Guard ($\text{hasItems}$)
Let $A$ be an array representing an ordered sequence $\langle a_1, a_2, \dots, a_n \rangle$ of elements from universe $\mathcal{U}$.
- **Predicate Definition:**
  $$\text{HasItems}(A) \iff A \ne \emptyset \land |A| \ge 1 \iff \exists x \in A, x = a_1$$
- **Type Narrowing Invariant:**
  $$\text{HasItems}(A) \vdash A \in \mathcal{U} \times \mathcal{U}^*$$

### 3.2 Boundary Containment & Short-Circuit Predicate ($\text{validateAccessBoundary}$)
Let $\mathcal{I} \subseteq \mathcal{U}$ be user-submitted inputs, $\mathcal{B} \subseteq \mathcal{U}$ be the allowed security boundary, and $R \in \text{Roles}$ be the user's role.
- **Short-Circuit Rule (Early Exit):**
  $$\text{BypassCondition}(\mathcal{I}, R, \mathcal{B}) \iff (\mathcal{I} = \emptyset) \lor (R = \text{SUPER\_ADMIN}) \lor (\text{'ALL'} \in \mathcal{B})$$
- **Universal Boundary Quantification:**
  $$\text{AccessGranted}(\mathcal{I}, \mathcal{B}) \iff \text{BypassCondition} \lor (\forall x \in \mathcal{I}, x \in \mathcal{B})$$
- **Security Rejection Condition:**
  $$\text{Reject}(\mathcal{I}, \mathcal{B}) \iff \neg \text{BypassCondition} \land (\exists x \in \mathcal{I}, x \notin \mathcal{B})$$

## 4. Invariants & Mathematical Proofs

### 4.1 Anti-Leak Deadlock Invariant (Proof by Contradiction)
- **Theorem:** When assigned boundary $\mathcal{B} = \emptyset$, database queries guarded by $\text{createSafeBoundaryFilter}$ will never leak records.
- **Proof:**
  1. Let $\mathcal{D}$ be the database table with existing keys $\mathcal{K} \subset \mathcal{U}$.
  2. The deadlock filter injects token $\tau = \text{'BLOCK\_ACCESS'}$, where $\tau \notin \mathcal{K}$ by invariant axiom.
  3. Assume a record $r \in \mathcal{D}$ with key $k_r$ is returned.
  4. For $r$ to be returned, the query condition requires $k_r \in \{\tau\} \implies k_r = \tau$.
  5. But $k_r \in \mathcal{K}$ and $\tau \notin \mathcal{K}$, implying $\tau \in \mathcal{K}$, which contradicts axiom (2).
  6. Therefore, no record can be returned: $|\mathcal{D}_{\text{filtered}}| = 0$. $\blacksquare$

### 4.2 Two-Step Mutation Protocol (Hoare Triple Specification)
For any mutation statement $S_{\text{mutate}}(r_{\text{id}})$:
$$\{\text{Exists}(r_{\text{id}}) \land \text{CanAccess}(\text{ctx}, r_{\text{id}})\} \quad S_{\text{mutate}}(r_{\text{id}}) \quad \{\text{Updated}(r_{\text{id}}) \land \text{AuditLogged}(r_{\text{id}})\}$$

## 5. Sanitized Generic Implementation

```typescript
import { ForbiddenException, NotFoundException } from '@nestjs/common';
import { FindOperator, In, Repository } from 'typeorm';

export interface UserSessionContext {
  user: {
    id: string;
    role: 'SUPER_ADMIN' | 'ADMIN' | 'MANAGER' | 'OPERATOR';
  };
  assignedBoundaries: {
    tenants: string[];
    groups: string[];
  };
}

/**
 * Custom Type-Guard: Verifies array non-emptiness with TypeScript compiler narrowing
 */
export function hasItems<T>(arr?: T[]): arr is [T, ...T[]] {
  return Boolean(arr && arr.length > 0);
}

const DEADLOCK_BLOCK_TOKEN = '___BLOCK_ACCESS___';

/**
 * Deadlock Safe Filter: Generates an unsatisfiable query condition if bounds are empty
 */
export const createSafeBoundaryFilter = (assignedItems?: string[]): FindOperator<string> => {
  return hasItems(assignedItems) ? In(assignedItems) : In([DEADLOCK_BLOCK_TOKEN]);
};

/**
 * Boundary Guard: Short-circuits for super-admins or validates universal containment
 */
export const validateAccessBoundary = (
  ctx: UserSessionContext,
  inputs: string[],
  allowedList: string[] = [],
  errorMessage: string = 'Access denied: Out of boundary',
): void => {
  if (
    !inputs.length ||
    ctx.user.role === 'SUPER_ADMIN' ||
    allowedList.includes('ALL')
  ) {
    return;
  }

  const isAllAllowed = inputs.every((item) => allowedList.includes(item));
  if (!isAllAllowed) {
    throw new ForbiddenException(errorMessage);
  }
};
```

## 6. Complexity & Algebraic Properties
- **Time Complexity:** $O(1)$ on short-circuit; $O(|\mathcal{I}| \times |\mathcal{B}|)$ or $O(|\mathcal{I}|)$ with Hash Set lookup.
- **Space Complexity:** $O(1)$ auxiliary space.
- **Soundness Guarantee:** Universal quantification guarantees zero false-positive access permissions.
