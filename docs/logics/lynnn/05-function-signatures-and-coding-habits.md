# 05. Function Signatures & Coding Conventions (Function Currying & Algebra)

## 1. Overview & Problem Statement
Inconsistent parameter orders, fake fallback values (e.g. `userId || 'system'`), and redundant class boilerplate degrade maintainability and obscure security contexts. This chapter formalizes context-first curried function signatures, strict separation of pure mapping data from algorithmic helpers, plain exported functions over class static wrappers, and fail-fast mutation invariants.

## 2. DISMATH Theoretical Foundation
- **Function Currying (`01`, `03`):** Transforming multi-argument functions into monadic context injection chains $f: \mathcal{C} \to (\mathcal{A} \to \mathcal{R})$.
- **Command-Query Separation (CQS) (`08`):** Distinguishing side-effecting operations (returning Unit $() \equiv \text{Promise}\langle \text{void} \rangle$) from pure mathematical queries.
- **Fail-Fast Invariants (`06`):** Absence of speculative defaults preventing unauthorized privilege escalation.

## 3. Formal Mathematical Specifications

### 3.1 Context-First Function Signatures as Monadic Currying
Let $\mathcal{C}$ be the space of authenticated user session contexts ($\text{UserSessionContext}$), $\mathcal{A}$ be the argument domain, and $\mathcal{R}$ be the return range.
- Every state-dependent or boundary-guarded operation is formalized as a curried function:
  $$f: \mathcal{C} \to (\mathcal{A} \to \mathcal{R})$$
- **Positional Invariant:** The context parameter $\text{ctx} \in \mathcal{C}$ is strictly fixed as the first argument in the product domain $\mathcal{C} \times \mathcal{A} \to \mathcal{R}$.

### 3.2 Separation of Data Mappings and Pure Functions
Let a domain feature $\mathcal{F}$ be partitioned into two disjoint entities:
$$\mathcal{F} = \langle \mathcal{M}_{\text{static}}, \mathcal{H}_{\text{pure}} \rangle$$
- $\mathcal{M}_{\text{static}} \in \text{Record}\langle \mathcal{K}, \mathcal{V} \rangle$ is an immutable lookup table stored in `.mapping.ts`.
- $\mathcal{H}_{\text{pure}} \subset (\mathcal{X} \to \mathcal{Y})$ is a set of side-effect-free pure functions stored in `.helper.ts`.

### 3.3 Standard Mutation Protocol (Command-Query Separation)
State mutation commands $\text{Cmd}$ adhere to the Command-Query Separation (CQS) principle:
$$\text{Cmd}: \text{State} \times \mathcal{A} \to \text{State} \times ()$$
The return value is strictly the unit type $() \equiv \text{Promise}\langle \text{void} \rangle$, minimizing payload churn.

## 4. Invariants & Mathematical Proofs

### 4.1 Context Invariance across Execution Layers
- **Theorem:** For any call chain $\text{Controller} \to \text{Service} \to \text{Helper}$, the authenticated identity $\text{ctx.user.id}$ remains invariant.
- **Proof:**
  1. Let $\text{ctx}_0$ be injected at the Controller entry point via authenticated Guard.
  2. Since $\text{ctx}$ is passed as the first parameter to $\text{Service}(ctx, \dots)$ and $\text{Helper}(ctx, \dots)$ without reassignment or mutation:
     $$\text{ctx}_{\text{Controller}} \equiv \text{ctx}_{\text{Service}} \equiv \text{ctx}_{\text{Helper}}$$
  3. Therefore, identity and security boundaries are invariant throughout the call stack. $\blacksquare$

### 4.2 Anti-Fallback Soundness (Fail-Fast Invariant)
- **Theorem:** Omitting fallback literals (`user_id || 'system'`) guarantees that unauthenticated mutations cannot execute.
- **Proof:** If $\text{user\_id} = \bot$, direct assignment $\text{updated\_by} = \text{user\_id}$ causes an immediate runtime or database null constraint violation, preventing unauthorized anonymous writes. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import { Body, Controller, Get, Param, Post, Req } from '@nestjs/common';

export interface UserSessionContext {
  user: { id: string; role: string };
  assignedBoundaries: { tenants: string[]; groups: string[] };
}

export interface CreateResourceDto {
  title: string;
  payload: Record<string, unknown>;
}

// Controller Layer: Context-First Rule
@Controller('resources')
export class ResourceController {
  constructor(private readonly service: ResourceService) {}

  @Get(':id')
  async findOne(@Req() ctx: UserSessionContext, @Param('id') id: string) {
    return this.service.findOne(ctx, Number(id));
  }

  @Post()
  async create(@Req() ctx: UserSessionContext, @Body() dto: CreateResourceDto): Promise<void> {
    return this.service.create(ctx, dto);
  }
}

// Service Layer: Strict Promise<void> for mutations
export class ResourceService {
  async findOne(ctx: UserSessionContext, id: number) {
    // Pure query
  }

  async create(ctx: UserSessionContext, dto: CreateResourceDto): Promise<void> {
    const userId = ctx.user.id; // Fail-fast: No fake fallback 'system'
    // Mutation logic
  }
}
```

## 6. Complexity & Algebraic Properties
- **Function Invocation Overhead:** $O(1)$ direct function invocation (zero class instantiation overhead for helpers).
- **Tree-Shaking Efficiency:** Exported plain functions allow modern JavaScript bundlers to eliminate $100\%$ of unused helper code.
