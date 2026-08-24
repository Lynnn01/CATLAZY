# 03. Mathematical & Metric Modeling (Metric Spaces & Induction)

## 1. Overview & Problem Statement
In mission-critical monitoring, analytics, and Service Level Agreement (SLA) enforcement, heterogeneous time units (milliseconds, seconds, hours) cause subtle rounding discrepancies and calculation errors. In addition, nested metrics require recursive serialization. This chapter formalizes time normalization in metric spaces, dynamic threshold partitioning, SLA penalty calculus, and recursive metric tree structures.

## 2. DISMATH Theoretical Foundation
- **Metric Spaces (`03`):** Metric distance functions $d: X \times X \to \mathbb{R}^+$ satisfying identity, symmetry, and triangle inequality.
- **Mathematical Induction (`07`):** Inductive construction of arbitrary-depth metric trees.
- **Piecewise Functions (`03`):** Monotonic cost and penalty growth functions.
- **Order Theory & Clamping (`06`):** Lattices and bounded intervals $[a, b]$.

## 3. Formal Mathematical Specifications

### 3.1 Time Normalization Metric Space
Let $\mathcal{T}$ be the continuous temporal domain. We define the normalized difference function $d_{\text{min}}: \mathcal{T} \times \mathcal{T} \to \mathbb{R}$:
$$d_{\text{min}}(t_{\text{now}}, t_{\text{start}}) = \frac{\text{differenceInSeconds}(t_{\text{now}}, t_{\text{start}})}{60}$$
- **Metric Invariant:** $d_{\text{min}}(t, t) = 0$ and $d_{\text{min}}(t_2, t_1) = -d_{\text{min}}(t_1, t_2)$.

### 3.2 Dynamic SLA Thresholding & Partitioning
Let $D_{\text{target}} \in \mathbb{R}^+$ be the target SLA duration in minutes and $\alpha = 0.6$ be the urgency coefficient.
- The temporal state of an active task is partitioned into three mutually exclusive subsets:
  $$\text{State}(\Delta t) = \begin{cases} \text{OVERDUE} & \text{if } \Delta t \ge D_{\text{target}} \\ \text{WARNING} & \text{if } \alpha \cdot D_{\text{target}} \le \Delta t < D_{\text{target}} \\ \text{NORMAL} & \text{if } \Delta t < \alpha \cdot D_{\text{target}} \end{cases}$$

### 3.3 Piecewise SLA Penalty Function
Let $R_{\text{hour}} \in \mathbb{R}^+$ be the penalty rate per hour. The penalty function $\mathcal{P}: \mathbb{R} \times \mathbb{R}^+ \to \mathbb{R}^{\ge 0}$ is:
$$\mathcal{P}(\Delta t, D_{\text{target}}) = \left( \frac{\max(0, \Delta t - D_{\text{target}})}{60} \right) \times R_{\text{hour}}$$

### 3.4 Recursive Metric Tree Grammar
A hierarchical metric node $\mathcal{M}$ is defined inductively:
$$\mathcal{M} \Coloneqq \langle \text{Title}: \Sigma^*, \text{Value}: \mathbb{R} \cup \Sigma^* \cup \mathcal{M}^*, \text{Description}: \Sigma^*, \text{Unit}: \Sigma^* \rangle$$

## 4. Invariants & Mathematical Proofs

### 4.1 Monotonicity of Penalty Growth
- **Theorem:** For any fixed $D_{\text{target}}$, the penalty $\mathcal{P}(\Delta t)$ is a monotonically non-decreasing function of $\Delta t$.
- **Proof:**
  1. Let $\Delta t_1 \le \Delta t_2$.
  2. $\Delta t_1 - D_{\text{target}} \le \Delta t_2 - D_{\text{target}}$.
  3. Since $f(x) = \max(0, x)$ is monotonically non-decreasing, $\max(0, \Delta t_1 - D_{\text{target}}) \le \max(0, \Delta t_2 - D_{\text{target}})$.
  4. Multiplying by non-negative constant $\frac{R_{\text{hour}}}{60} \ge 0$ preserves the inequality: $\mathcal{P}(\Delta t_1) \le \mathcal{P}(\Delta t_2)$. $\blacksquare$

### 4.2 Pagination Clamping Bounds
- **Theorem:** The clamped query parameters $(\text{page}, \text{limit})$ strictly satisfy $\text{page} \ge 1$ and $1 \le \text{limit} \le 5000$.
- **Proof:** Derived directly from the clamp functions $\max(1, p)$ and $\min(5000, \max(1, l))$. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import { differenceInSeconds } from 'date-fns';
import _ from 'lodash';

/**
 * Standard Time Normalization (Minutes as floating point)
 */
export const minutesDiffSeconds = (dateLeft: Date, dateRight: Date): number =>
  differenceInSeconds(dateLeft, dateRight) / 60;

const WARNING_THRESHOLD_RATIO = 0.6;
const DEFAULT_PENALTY_RATE_PER_HOUR = 500;

export const isTimeOverdue = (targetDuration: number, date: { create: Date; now: Date }): boolean => {
  const elapsed = minutesDiffSeconds(date.now, date.create);
  return elapsed >= targetDuration;
};

export const isTimeInWarningWindow = (targetDuration: number, date: { create: Date; now: Date }): boolean => {
  const elapsed = minutesDiffSeconds(date.now, date.create);
  return elapsed >= targetDuration * WARNING_THRESHOLD_RATIO && elapsed < targetDuration;
};

export const calculatePenalty = (
  elapsedMinutes: number,
  targetDurationMinutes: number,
  ratePerHour: number = DEFAULT_PENALTY_RATE_PER_HOUR,
): number => {
  const overdueMinutes = Math.max(0, elapsedMinutes - targetDurationMinutes);
  return (overdueMinutes / 60) * ratePerHour;
};

/**
 * Recursive Metric Node Construction
 */
export type ContextSubMetric = {
  label: string;
  value: string | number | ContextSubMetric[];
  unit?: string;
};

export const createMetric = (
  title: string,
  value: string | number | ContextSubMetric[],
  description: string | number,
  unit: string,
) => ({
  title,
  value: Array.isArray(value) ? value : String(value),
  description: String(description),
  unit,
});

export const createSubMetric = (
  label: string,
  value: string | number | ContextSubMetric[],
  unit?: string,
): ContextSubMetric => ({
  label,
  value,
  unit,
});
```

## 6. Complexity & Algebraic Properties
- **Time Difference & Penalty:** $O(1)$ scalar evaluation time.
- **Metric Tree Construction:** $O(N)$ linear time in the number of metric nodes.
- **Space Complexity:** $O(D)$ where $D$ is the maximum recursion depth of sub-metrics.
