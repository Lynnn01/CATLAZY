# 02. Logical Equivalences

Logical equivalences are foundational tools for simplifying compound statements, refactoring boolean expressions in software, verifying circuit designs, and establishing mathematical proofs.

---

## 1. Classifications of Compound Propositions

1. **Tautology ($\mathbf{T}$):** A compound proposition that is always **true** across all possible assignments of truth values to its variables (e.g., $p \lor \neg p$).
2. **Contradiction ($\mathbf{F}$):** A compound proposition that is always **false** across all possible assignments of truth values to its variables (e.g., $p \land \neg p$).
3. **Contingency:** A compound proposition that is neither a tautology nor a contradiction (it can be true in some cases and false in others).

---

## 2. Definition of Logical Equivalence ($p \equiv q$)

Two compound propositions $p$ and $q$ are called **logically equivalent**, denoted $p \equiv q$ or $p \Leftrightarrow q$, if and only if the biconditional statement **$p \leftrightarrow q$ is a tautology**. 

In other words, $p$ and $q$ yield identical truth values in every row of their truth table.

---

## 3. Fundamental Laws of Logical Equivalences

Let $\mathbf{T}$ denote a tautology and $\mathbf{F}$ denote a contradiction:

| Law Name | Equivalence Forms |
| :--- | :--- |
| **Identity Laws** | $p \land \mathbf{T} \equiv p$ <br> $p \lor \mathbf{F} \equiv p$ |
| **Domination Laws** | $p \lor \mathbf{T} \equiv \mathbf{T}$ <br> $p \land \mathbf{F} \equiv \mathbf{F}$ |
| **Idempotent Laws** | $p \lor p \equiv p$ <br> $p \land p \equiv p$ |
| **Double Negation Law** | $\neg(\neg p) \equiv p$ |
| **Commutative Laws** | $p \lor q \equiv q \lor p$ <br> $p \land q \equiv q \land p$ |
| **Associative Laws** | $(p \lor q) \lor r \equiv p \lor (q \lor r)$ <br> $(p \land q) \land r \equiv p \land (q \land r)$ |
| **Distributive Laws** | $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ <br> $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$ |
| **De Morgan's Laws** | $\neg(p \land q) \equiv \neg p \lor \neg q$ <br> $\neg(p \lor q) \equiv \neg p \land \neg q$ |
| **Absorption Laws** | $p \lor (p \land q) \equiv p$ <br> $p \land (p \lor q) \equiv p$ |
| **Negation Laws** | $p \lor \neg p \equiv \mathbf{T}$ <br> $p \land \neg p \equiv \mathbf{F}$ |

---

## 4. Conditional Equivalences

### 4.1 Fundamental Conditional Law
$$p \to q \equiv \neg p \lor q$$

### 4.2 Contrapositive Equivalence
$$p \to q \equiv \neg q \to \neg p$$

### 4.3 Other Standard Conditional Identities:
- $p \lor q \equiv \neg p \to q$
- $p \land q \equiv \neg(p \to \neg q)$
- $\neg(p \to q) \equiv p \land \neg q$
- $(p \to q) \land (p \to r) \equiv p \to (q \land r)$
- $(p \to r) \land (q \to r) \equiv (p \lor q) \to r$
- $(p \to q) \lor (p \to r) \equiv p \to (q \lor r)$
- $(p \to r) \lor (q \to r) \equiv (p \land q) \to r$

---

## 5. Variations of Conditional Statements

Given a primary conditional statement $p \to q$:

1. **Converse:** $q \to p$
2. **Inverse:** $\neg p \to \neg q$
3. **Contrapositive:** $\neg q \to \neg p$

> 💡 **Equivalence Invariant:**
> - A conditional statement is **always logically equivalent to its contrapositive**:
>   $$p \to q \equiv \neg q \to \neg p$$
> - The converse and inverse are equivalent to each other:
>   $$q \to p \equiv \neg p \to \neg q$$
> - A conditional statement is **NOT generally equivalent to its converse**:
>   $$p \to q \not\equiv q \to p$$
