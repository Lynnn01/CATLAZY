# 07. Mathematical Induction and Recursion

Mathematical induction is a powerful proof technique used to establish that a predicate $P(n)$ is true for all positive integers $n \in \mathbb{Z}^+$ (or for all integers starting from a base index $n_0$).

---

## 1. Principle of Mathematical Induction

To prove that $\forall n P(n)$ is true for all positive integers $n = 1, 2, 3, \dots$, we establish two essential steps:

1. **Basis Step (Base Case):**
   - Verify that $P(1)$ is **True ($T$)**.
2. **Inductive Step:**
   - Prove that the conditional statement $P(k) \to P(k+1)$ is **True ($T$)** for all positive integers $k$.
   - *Inductive Hypothesis:* Assume $P(k)$ is true, and deduce that $P(k+1)$ must also be true.

$$\mathbf{[P(1) \land \forall k (P(k) \to P(k+1))] \longrightarrow \forall n P(n)}$$

### Classic Example: Summation of the First $n$ Positive Integers
Prove that for all $n \ge 1$:
$$1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$$

- **Basis Step ($n = 1$):**
  - $\text{LHS} = 1$, $\text{RHS} = \frac{1(1+1)}{2} = 1$. The base case holds.
- **Inductive Step:**
  - *Inductive Hypothesis:* Assume $P(k)$ holds: $1 + 2 + \dots + k = \frac{k(k+1)}{2}$.
  - Must show $P(k+1)$ holds: $1 + 2 + \dots + k + (k+1) = \frac{(k+1)(k+2)}{2}$.
  - Evaluating LHS:
    $$[1 + 2 + \dots + k] + (k+1) = \frac{k(k+1)}{2} + (k+1) = (k+1)\left(\frac{k}{2} + 1\right) = \frac{(k+1)(k+2)}{2}$$
  - Since $P(k+1)$ is true, by mathematical induction, $P(n)$ is true for all $n \ge 1$. $\blacksquare$

---

## 2. Strong Induction

In some proofs, assuming $P(k)$ alone is insufficient to prove $P(k+1)$; instead, we require the assumption that $P(j)$ is true for **all preceding values** $1 \le j \le k$:

- **Basis Step:** Prove $P(1)$ (or multiple base cases $P(1), \dots, P(b)$).
- **Inductive Step:** Prove that $[P(1) \land P(2) \land \dots \land P(k)] \to P(k+1)$ holds for all $k \ge 1$.

$$\mathbf{[P(1) \land \forall k ((P(1) \land \dots \land P(k)) \to P(k+1))] \longrightarrow \forall n P(n)}$$

---

## 3. Recursive Definitions

A recursive (or inductive) definition specifies an object (function, sequence, or set) in terms of itself:
1. **Basis Step:** Specify the initial values or base elements (e.g., $f(0) = 1$).
2. **Recursive Step:** Provide a rule for constructing new elements from previous ones (e.g., $f(n+1) = (n+1) \cdot f(n)$ for $n!$).

### Example: Fibonacci Sequence
- $f_0 = 0, \quad f_1 = 1$
- $f_n = f_{n-1} + f_{n-2}$ for all $n \ge 2$

---

## 4. Structural Induction

Structural induction is used to prove properties of recursively defined structures (such as binary trees, strings, or mathematical expressions):
- **Basis Step:** Prove the property holds for all base elements specified in the basis step of the recursive definition.
- **Recursive Step:** Prove that if the property holds for the existing elements, it must also hold for any new element constructed via the recursive step.
