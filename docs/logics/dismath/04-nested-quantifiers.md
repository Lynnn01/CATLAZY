# 04. Nested Quantifiers

When mathematical propositions involve multiple variables (such as predicates with two or more arguments $Q(x, y)$), we use **nested quantifiers** (e.g., $\forall x \exists y Q(x, y)$).

---

## 1. Semantics and Quantifier Ordering

The order in which quantifiers appear is critical to the truth value and meaning of a mathematical statement:

### 1.1 Homogeneous Quantifiers: $\forall x \forall y$ and $\exists x \exists y$
- **$\forall x \forall y P(x, y) \equiv \forall y \forall x P(x, y)$:** $P(x, y)$ is true for every possible pair $(x, y)$. Order does not alter the meaning.
- **$\exists x \exists y P(x, y) \equiv \exists y \exists x P(x, y)$:** There exists at least one pair $(x, y)$ for which $P(x, y)$ is true. Order does not alter the meaning.

### 1.2 Heterogeneous Quantifiers: $\forall x \exists y$ vs $\exists y \forall x$

> ⚠️ **Crucial Distinction:** $\forall x \exists y P(x, y)$ is **NOT logically equivalent** to $\exists y \forall x P(x, y)$.

- **$\forall x \exists y P(x, y)$:**
  - *"For every $x$, there exists a $y$ (which may depend on $x$) such that $P(x, y)$ is true."*
  - *Example (Domain = $\mathbb{R}$):* $\forall x \exists y (x + y = 0)$ $\longrightarrow$ **True ($T$)**, because for any chosen $x$, we can pick $y = -x$.
- **$\exists y \forall x P(x, y)$:**
  - *"There exists a single, fixed $y$ such that for all $x$, $P(x, y)$ is true."*
  - *Example (Domain = $\mathbb{R}$):* $\exists y \forall x (x + y = 0)$ $\longrightarrow$ **False ($F$)**, because there is no single real number $y$ that can be added to every $x$ to yield zero.

---

## 2. Master Truth Conditions for Nested Quantifiers

| Statement | True Condition | False Condition |
| :--- | :--- | :--- |
| $\forall x \forall y P(x, y)$ | $P(x, y)$ is true for every pair $(x, y)$. | There is at least one pair $(x, y)$ for which $P(x, y)$ is false. |
| $\forall x \exists y P(x, y)$ | For every $x$, there is a $y$ for which $P(x, y)$ is true. | There is an $x$ such that $P(x, y)$ is false for all $y$. |
| $\exists x \forall y P(x, y)$ | There is an $x$ for which $P(x, y)$ is true for all $y$. | For every $x$, there is a $y$ for which $P(x, y)$ is false. |
| $\exists x \exists y P(x, y)$ | There is at least one pair $(x, y)$ for which $P(x, y)$ is true. | $P(x, y)$ is false for all pairs $(x, y)$. |

---

## 3. Negating Nested Quantifiers

Negations are applied successively from left to right using De Morgan's laws for quantifiers:
- Flip each $\forall$ to $\exists$
- Flip each $\exists$ to $\forall$
- Negate the inner predicate $P$

### Canonical Examples:
$$\neg \forall x \exists y P(x, y) \equiv \exists x \neg(\exists y P(x, y)) \equiv \exists x \forall y \neg P(x, y)$$

$$\neg \forall x \forall y \exists z P(x, y, z) \equiv \exists x \exists y \forall z \neg P(x, y, z)$$

---

## 4. Translating Natural Language into Nested Quantifiers

Let $L(x, y)$ denote "$x$ loves $y$", with the domain consisting of all people:
- *"Everybody loves somebody":* $\forall x \exists y L(x, y)$
- *"There is somebody who loves everybody":* $\exists x \forall y L(x, y)$
- *"There is somebody whom everybody loves":* $\exists y \forall x L(x, y)$
- *"Nobody loves everybody":* $\neg \exists x \forall y L(x, y) \equiv \forall x \exists y \neg L(x, y)$
- *"Everybody loves nobody":* $\forall x \forall y \neg L(x, y)$
