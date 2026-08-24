# 04. Deterministic Priority State Machine (State Machines & Transition Systems)

## 1. Overview & Problem Statement
In workflow systems and inspection checklists consisting of dozens of sub-items, aggregating heterogeneous sub-item statuses (e.g. pending, verified, pre-approved, approved, rejected) into a single overall status requires a deterministic, conflict-free resolution mechanism. This chapter formalizes the cascade priority state machine, veto resolution rules, and single-pass status reductions.

## 2. DISMATH Theoretical Foundation
- **State Machines & Transition Systems (`04`, `08`):** Deterministic Finite Transition tuples $M = \langle \mathcal{S}, \Sigma, \delta, s_0, \mathcal{F} \rangle$.
- **Veto Rules & Invariants (`06`):** Absorbing states where a single failure overrides all other positive conditions ($c_{\text{reject}} > 0 \implies \text{REJECT}$).
- **Vector Space Partitions (`03`):** Single-pass reduction over status count vectors $\vec{C} \in \mathbb{N}^5$.

## 3. Formal Mathematical Specifications

### 3.1 State Set and Counter Vector
Let the set of document/checklist states be:
$$\mathcal{S} = \{\text{IN\_PROGRESS}, \text{VERIFY}, \text{PRE\_APPROVE}, \text{APPROVE}, \text{REJECT}\}$$

Let $\vec{C} = \langle c_p, c_v, c_{pa}, c_a, c_r \rangle \in \mathbb{N}^5$ be the vector representing counts of in-progress, verify, pre-approve, approve, and reject items respectively.
- Total recorded items: $N_{\text{rec}} = c_p + c_v + c_{pa} + c_a + c_r$.
- Expected total items: $N_{\text{total}} \in \mathbb{N}^+$.

### 3.2 State Transition Function ($\delta: \mathbb{N}^5 \times \mathbb{N}^+ \to \mathcal{S}$)
The aggregated status resolution follows a strict cascade priority with a **Veto Invariant**:

$$\delta(\vec{C}, N_{\text{total}}) = \begin{cases} \text{REJECT} & \text{if } c_r > 0 \quad \text{(Veto Rule)} \\ \text{APPROVE} & \text{if } c_r = 0 \land c_a > 0 \land c_a = N_{\text{total}} \\ \text{PRE\_APPROVE} & \text{if } c_r = 0 \land c_{pa} > 0 \land c_{pa} = N_{\text{rec}} \\ \text{VERIFY} & \text{if } c_r = 0 \land c_v > 0 \land c_v = N_{\text{rec}} \\ \text{IN\_PROGRESS} & \text{otherwise (Default Base State)} \end{cases}$$

## 4. Invariants & Mathematical Proofs

### 4.1 Determinism and Exclusivity
- **Theorem:** The transition function $\delta(\vec{C}, N_{\text{total}})$ is deterministic (every input vector maps to exactly one state).
- **Proof:**
  1. The guards are mutually exclusive by construction (ordered cascade with early termination).
  2. If $c_r > 0$, the state is immediately $\text{REJECT}$, suppressing all subsequent evaluations.
  3. The default fallback $\text{IN\_PROGRESS}$ catches all remaining vectors $\vec{C}$, guaranteeing total coverage.
  4. Therefore, $\delta$ is a well-defined total function. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
export enum InspectionStatus {
  IN_PROGRESS = 'IN_PROGRESS',
  VERIFY = 'VERIFY',
  PRE_APPROVE = 'PRE_APPROVE',
  APPROVE = 'APPROVE',
  REJECT = 'REJECT',
}

export interface StatusCounter {
  inProgress: number;
  verify: number;
  preApprove: number;
  approve: number;
  reject: number;
}

/**
 * Deterministic Priority State Machine: Resolves overall status using priority cascade & veto rules
 */
export const evaluateAggregatedStatus = (
  statusCounts: StatusCounter[],
  expectedTotalSubsections: number,
): InspectionStatus => {
  const inProgress = statusCounts.reduce((sum, item) => sum + item.inProgress, 0);
  const verify = statusCounts.reduce((sum, item) => sum + item.verify, 0);
  const preApprove = statusCounts.reduce((sum, item) => sum + item.preApprove, 0);
  const approve = statusCounts.reduce((sum, item) => sum + item.approve, 0);
  const reject = statusCounts.reduce((sum, item) => sum + item.reject, 0);
  const totalRecorded = inProgress + verify + preApprove + approve + reject;

  // 1. Veto Invariant: Any rejection forces overall REJECT immediately
  if (reject > 0) {
    return InspectionStatus.REJECT;
  }

  // 2. Full Approval: All required items must be approved
  if (approve > 0 && approve === expectedTotalSubsections) {
    return InspectionStatus.APPROVE;
  }

  // 3. Pre-Approval: All currently recorded items are pre-approved
  if (preApprove > 0 && preApprove === totalRecorded) {
    return InspectionStatus.PRE_APPROVE;
  }

  // 4. Verification: All currently recorded items are verified
  if (verify > 0 && verify === totalRecorded) {
    return InspectionStatus.VERIFY;
  }

  // 5. Default Base State
  return InspectionStatus.IN_PROGRESS;
};
```

## 6. Complexity & Algebraic Properties
- **Time Complexity:** $O(K)$ where $K$ is the number of status groups (single reduction pass).
- **Space Complexity:** $O(1)$ scalar counter accumulators.
- **Safety Invariant:** A single failing item ($c_r \ge 1$) can never leak into an approved state.
