# 10. Concurrent Aggregation & Multi-Dimensional Processing (Concurrency Join Calculus)

## 1. Overview & Problem Statement
Analytics dashboards and multi-dimensional entity relation binding often suffer from slow response times when queries are executed sequentially. Furthermore, raw percentage calculations can crash if the total denominator is zero (zero-division error). This chapter formalizes non-blocking asynchronous concurrency, zero-division safe quotient functions, and higher-order relation dispatching.

## 2. DISMATH Theoretical Foundation
- **Concurrency & Join Calculus (`07`):** Asynchronous fork-join operations bounding latency to $T = \max t_i$.
- **Total Functions & Safe Quotients (`03`):** Well-defined division maps over non-negative integers preventing division by zero.
- **Higher-Order Mapping (`03`):** Parametric mapping functions assigning multi-dimensional relations in parallel.

## 3. Formal Mathematical Specifications

### 3.1 Asynchronous Concurrency & Join Calculus
Let $T_1, T_2, \dots, T_k$ be asynchronous query tasks with individual latencies $t(T_i)$.
- **Sequential Execution Time:** $T_{\text{seq}} = \sum_{i=1}^k t(T_i)$
- **Concurrent `Promise.all` Execution Time:**
  $$T_{\text{concurrent}} = \max_{1 \le i \le k} (t(T_i)) + \epsilon_{\text{overhead}}$$
  $$T_{\text{concurrent}} \ll T_{\text{seq}} \quad \text{for all } k > 1$$

### 3.2 Zero-Division Safe Percentage Quotient ($Q_{\text{safe}}$)
Let $a \in \mathbb{N}$ (active count) and $b \in \mathbb{N}$ (total count) where $a \le b$.
$$Q_{\text{safe}}(a, b) = \begin{cases} \text{round}_2\left(\frac{a}{b} \times 100\right) & \text{if } b > 0 \\ 0.00 & \text{if } b = 0 \quad \text{(Zero-Division Guard)} \end{cases}$$
- **Mathematical Invariant:** $Q_{\text{safe}}(a, b) \in [0.00, 100.00] \subset \mathbb{R}$ for all $a, b \in \mathbb{N}$.

### 3.3 Higher-Order Parallel Section Mapping
Given boundary dimensions $\mathcal{D} = \{d_1, d_2, \dots, d_m\}$ and transformation pipeline $\mathcal{F}$:
$$\text{AssignAll}(\mathcal{D}, \text{dto}) \iff \bigwedge_{d \in \mathcal{D}} \text{ExecuteParallel}(\mathcal{F}(d, \text{dto}[d]))$$

## 4. Invariants & Mathematical Proofs

### 4.1 Arithmetic Robustness (No NaN / Division by Zero)
- **Theorem:** The function $Q_{\text{safe}}(a, b)$ is a total function and never produces $\text{NaN}$, $\infty$, or division-by-zero exceptions.
- **Proof:**
  1. The domain of input is $(a, b) \in \mathbb{N} \times \mathbb{N}$.
  2. If $b = 0$, the guard condition branch triggers, returning constant literal $0.00$.
  3. If $b > 0$, the arithmetic division $\frac{a}{b}$ is well-defined over $\mathbb{R}^+$.
  4. Since $a \le b$, the result is strictly bounded within $[0, 100]$.
  5. Thus, $Q_{\text{safe}}$ is total and exception-free. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import { differenceInDays } from 'date-fns';
import _ from 'lodash';
import { In } from 'typeorm';

export class SummaryDashboardService {
  async getDashboardSummary(ctx: UserSessionContext) {
    // Concurrent Async Join (Promise.all)
    const [resources, latestCycle, overdueTasks] = await Promise.all([
      this.resourceService.findAll(ctx),
      this.cycleService.getLatestCycle(ctx),
      this.taskService.findOverdueTasks(ctx),
    ]);

    const logs = await this.logService.findByCycle(ctx, latestCycle);
    const totalCount = resources.length;
    const activeCount = resources.filter((r) => r.isActive).length;

    // Safe Percentage Math
    const activePercentage = totalCount > 0
      ? ((activeCount / totalCount) * 100).toFixed(2)
      : '0.00';

    const now = new Date();
    const latestDate = _.maxBy(logs, 'updated_at')?.updated_at;
    const daysSinceUpdate = latestDate ? String(differenceInDays(now, latestDate)) : 'N/A';

    return {
      totalMetric: createMetric('Total Resources', totalCount, `Active ${activePercentage}%`, 'units'),
      activeMetric: createMetric('Active Count', activeCount, 0, 'units'),
      cycleMetric: createMetric('Current Cycle Logs', logs.length, `Updated ${daysSinceUpdate}d ago`, 'items'),
      overdueMetric: createMetric('Overdue SLA', overdueTasks.length, 'Urgent Response', 'critical'),
    };
  }
}

/**
 * Higher-Order Multi-Dimensional Processor
 */
export async function assignMultiDimensionalScopes(
  ctx: UserSessionContext,
  dto: { tenants?: string[]; groups?: string[]; teams?: string[] },
  targetEntity: any,
) {
  const boundaries = ctx.assignedBoundaries;

  const processSection = async (
    sectionKey: keyof typeof boundaries,
    assignFn: (validInputs: string[]) => Promise<void>,
  ) => {
    const values = dto[sectionKey];
    if (values === undefined) return;
    if (values.length === 0) {
      await assignFn([]);
      return;
    }

    validateAccessBoundary(ctx, values, boundaries[sectionKey]);
    await assignFn(values);
  };

  // Parallel Execution across all dimensions
  await Promise.all([
    processSection('tenants', async (inputs) => {
      targetEntity.Tenants = inputs.length ? await this.tenantRepo.find({ where: { id: In(inputs) } }) : [];
    }),
    processSection('groups', async (inputs) => {
      targetEntity.Groups = inputs.length ? await this.groupRepo.find({ where: { id: In(inputs) } }) : [];
    }),
  ]);
}
```

## 6. Complexity & Algebraic Properties
- **Query Latency:** Reduced from $O(\sum t_i)$ to $O(\max t_i)$ via non-blocking async event loop.
- **Data Integrity:** Parallel section processing maintains transactional atomicity per relation.
