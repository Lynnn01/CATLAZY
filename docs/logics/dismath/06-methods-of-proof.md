# 06. Methods of Proof

A **mathematical proof** is a valid deductive argument that establishes the absolute truth of a mathematical theorem, using axioms, definitions, previously proven theorems, and formal rules of inference.

---

## 1. Terminology

- **Theorem:** A mathematical statement that has been proven to be true.
- **Axiom (or Postulate):** A foundational assumption accepted without proof.
- **Lemma:** A minor theorem used as a stepping stone to prove a major theorem.
- **Corollary:** A direct proposition that follows immediately from a proven theorem.
- **Conjecture:** A statement proposed to be true, but not yet proven or disproven.

---

## 2. Standard Proof Techniques for Conditionals ($p \to q$)

### 2.1 Direct Proof
- **Strategy:**
  1. Assume the hypothesis $p$ is **True ($T$)**.
  2. Use axioms, definitions, algebraic rules, and theorems.
  3. Deduce that the conclusion $q$ must be **True ($T$)**.
- **Example:** Prove that *"If $n$ is an odd integer, then $n^2$ is an odd integer."*
  - *Proof:* Assume $n$ is odd. By definition, $n = 2k + 1$ for some integer $k$.
  - Then $n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.
  - Let $m = 2k^2 + 2k \in \mathbb{Z}$. Thus $n^2 = 2m + 1$, which is odd by definition. $\blacksquare$

---

### 2.2 Proof by Contraposition (Indirect Proof)
- **Strategy:**
  - Relies on the equivalence $p \to q \equiv \neg q \to \neg p$.
  1. Assume the conclusion is false ($\neg q$ is True).
  2. Deduce through direct reasoning that the hypothesis must be false ($\neg p$ is True).
- **Example:** Prove that *"If $3n + 2$ is an odd integer, then $n$ is an odd integer."*
  - *Proof by Contraposition:* Assume $n$ is not odd (i.e., $n$ is even, so $n = 2k$ for $k \in \mathbb{Z}$).
  - Then $3n + 2 = 3(2k) + 2 = 6k + 2 = 2(3k + 1)$.
  - Since $3k + 1 \in \mathbb{Z}$, $3n + 2$ is even ($\neg p$).
  - Having proven $\neg q \to \neg p$, the original implication $p \to q$ is true. $\blacksquare$

---

### 2.3 Proof by Contradiction (*Reductio ad Absurdum*)
- **Strategy:**
  - To prove proposition $p$:
  1. Assume the statement is **False** ($\neg p$ is True).
  2. Derive a logical **contradiction** of the form $r \land \neg r$ or a contradiction of a known axiom.
  3. Conclude that the assumption $\neg p$ is impossible, hence $p$ is True.
- **Classic Example:** Prove that *$\sqrt{2}$ is irrational.*
  - *Proof by Contradiction:* Assume $\sqrt{2}$ is rational. Then $\sqrt{2} = \frac{a}{b}$ where $a, b \in \mathbb{Z}, b \ne 0$, and $\gcd(a, b) = 1$ (irreducible fraction).
  - Squaring both sides: $2 = \frac{a^2}{b^2} \implies a^2 = 2b^2 \implies a^2$ is even $\implies a$ is even ($a = 2k$).
  - Substituting: $(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2 \implies b^2$ is even $\implies b$ is even.
  - If both $a$ and $b$ are even, they share a common factor of $2$, contradicting $\gcd(a, b) = 1$.
  - Therefore, $\sqrt{2}$ must be irrational. $\blacksquare$

---

## 3. Specialized Proof Techniques

### 3.1 Vacuous Proof
If the hypothesis $p$ is known to be **False ($F$)**, the conditional $p \to q$ is vacuously true, because $\mathbf{F} \to q \equiv \mathbf{T}$.

### 3.2 Trivial Proof
If the conclusion $q$ is known to be **True ($T$)**, the conditional $p \to q$ is trivially true, because $p \to \mathbf{T} \equiv \mathbf{T}$.

### 3.3 Proof by Cases
When a statement covers multiple scenarios $(p_1 \lor p_2 \lor \dots \lor p_n) \to q$, prove that each individual case implies $q$:
$$(p_1 \to q) \land (p_2 \to q) \land \dots \land (p_n \to q)$$

### 3.4 Exhaustive Proof
For finite domains, verify the truth of the proposition for every single element in the domain individually.
