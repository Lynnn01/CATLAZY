# 02. Functional Transformations & Lookup Engines (Functions & Relations)

## 1. Overview & Problem Statement
Imperative nested `switch-case` and `if-else` branching creates cognitive complexity, increases cyclomatic complexity, and makes testing error-prone. Additionally, linear searching across relational records yields $O(N \times M)$ overhead. This chapter formalizes table-driven boolean mappings, monadic plucking, injective lookup maps, and multi-predicate partitioning.

## 2. DISMATH Theoretical Foundation
- **Boolean Functions (`01`, `09`):** Total mapping functions from finite domain sets to truth values ($M: \text{Roles} \to \{0, 1\}$).
- **Functions and Relations (`03`):** Injective mappings (one-to-one hash maps) $f: \text{Keys} \hookrightarrow \text{Values}$.
- **Monoids & Left-Folds (`07`):** Inductive collection reduction ($\text{foldl}$) for property extraction.
- **Partitioning Calculus (`03`):** Disjoint predicate grouping over collections.

## 3. Formal Mathematical Specifications

### 3.1 Boolean Role Requirement Function ($M_{\text{req}}$)
Let $\text{Roles} = \{\text{SUPER\_ADMIN}, \text{ADMIN}, \text{MANAGER}, \text{OPERATOR}\}$ and $\text{Scope} = \langle \mathcal{O}, \mathcal{D}, \mathcal{T} \rangle$.
- Define indicator predicates: $h_O \iff \text{HasItems}(\mathcal{O})$, $h_D \iff \text{HasItems}(\mathcal{D})$, $h_T \iff \text{HasItems}(\mathcal{T})$.
- The requirement mapping is a total function $M_{\text{req}}: \text{Roles} \to \{0, 1\}$:
  $$M_{\text{req}}(r) = \begin{cases} 1 & \text{if } r = \text{SUPER\_ADMIN} \\ h_O & \text{if } r = \text{ADMIN} \\ h_O \land h_D & \text{if } r = \text{MANAGER} \\ h_O \land h_D \land h_T & \text{if } r = \text{OPERATOR} \end{cases}$$

### 3.2 Monadic Property Extraction ($\text{pluck}$ as Left-Fold)
Given an array $A = \langle x_1, x_2, \dots, x_n \rangle$ where each $x_i \in \text{Record}$ and property key $k \in \text{Keys}(\text{Record})$:
$$\text{pluck}(A, k) \Coloneqq \text{foldl}\left(\lambda \text{acc}, x \to \begin{cases} \text{acc} \mathbin{\Vert} \langle x.k \rangle & \text{if } x.k \ne \text{null} \land x.k \ne \text{undefined} \\ \text{acc} & \text{otherwise} \end{cases}, \langle \rangle, A\right)$$

### 3.3 Fast Lookup Injective Mapping ($\text{buildLookupEngine}$)
Let $\mathcal{I}_{\text{raw}} = \{(k_i, v_i)\}$ be input image/metric pairs.
$$\mathcal{M}_{\text{lookup}}: \text{Keys} \hookrightarrow \text{Values} \cup \{\bot\}$$
$$\mathcal{M}_{\text{lookup}}(k) = \begin{cases} v & \text{if } (k, v) \in \mathcal{I}_{\text{raw}} \\ \bot & \text{otherwise} \end{cases}$$

## 4. Invariants & Mathematical Proofs

### 4.1 Monotonicity of Role Permissions
- **Theorem:** Let the hierarchy order be $\text{SUPER\_ADMIN} \prec \text{ADMIN} \prec \text{MANAGER} \prec \text{OPERATOR}$. The requirement constraint is strictly monotonic:
  $$r_1 \prec r_2 \implies M_{\text{req}}(r_1) \impliedby M_{\text{req}}(r_2)$$
- **Proof:**
  1. For $r_1 = \text{SUPER\_ADMIN}$, $M_{\text{req}}(r_1) = 1$. The proposition $X \implies 1$ is a tautology.
  2. For $r_1 = \text{ADMIN}$ and $r_2 = \text{MANAGER}$, $M_{\text{req}}(r_2) = (h_O \land h_D) \implies h_O = M_{\text{req}}(r_1)$ by simplification rule.
  3. By hypothetical syllogism, monotonicity holds across all ranks. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import _ from 'lodash';

type RoleType = 'SUPER_ADMIN' | 'ADMIN' | 'MANAGER' | 'OPERATOR';

interface ScopeContext {
  organizationIds?: string[];
  departmentIds?: string[];
  teamIds?: string[];
}

/**
 * Functional Role Mapping Table: Replaces nested if-else with a deterministic Record lookup
 */
export function hasRequiredScopeByRole(role: RoleType, scope: ScopeContext): boolean {
  const { organizationIds, departmentIds, teamIds } = scope;

  const hasOrg = Boolean(organizationIds?.length);
  const hasDept = Boolean(departmentIds?.length);
  const hasTeam = Boolean(teamIds?.length);

  const roleRequirementsMap: Record<RoleType, boolean> = {
    SUPER_ADMIN: true,
    ADMIN: hasOrg,
    MANAGER: hasOrg && hasDept,
    OPERATOR: hasOrg && hasDept && hasTeam,
  };

  return Boolean(roleRequirementsMap[role]);
}

/**
 * Safe Property Plucking via Left Fold (.reduce) with Type Narrowing
 */
export function pluck<T, K extends keyof T>(
  arr: T[] | undefined,
  key: K,
): NonNullable<T[K]>[] {
  return (arr ?? []).reduce((acc: NonNullable<T[K]>[], item: T) => {
    if (item[key] != null) acc.push(item[key] as NonNullable<T[K]>);
    return acc;
  }, []);
}

/**
 * Multi-Predicate Partitioning Engine (ZipObject of Predicate Filters)
 */
export function filterGroupBy<T, K extends string | number | symbol>(
  items: T[],
  keys: K[],
  predicateMap: Partial<Record<K, (item: T) => boolean>>,
): Record<K, T[]> {
  return _.zipObject(
    keys,
    keys.map((key) =>
      predicateMap[key] ? _.filter(items, predicateMap[key]) : [],
    ),
  ) as Record<K, T[]>;
}
```

## 6. Complexity & Algebraic Properties
- **`hasRequiredScopeByRole`:** $O(1)$ evaluation time and $O(1)$ memory.
- **`pluck`:** $O(N)$ linear time complexity and $O(M)$ output memory ($M \le N$).
- **Lookup Access:** $O(1)$ average-case retrieval via Hash Map bijection.
