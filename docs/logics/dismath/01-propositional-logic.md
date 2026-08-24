# 01. Propositional Logic

Propositional logic (also called *sentential logic* or *propositional calculus*) is the branch of mathematical logic that studies the truth values of propositions and compound statements formed via logical connectives.

---

## 1. Definition of a Proposition

A **proposition** is a declarative statement that is either **true ($T$)** or **false ($F$)**, but not both. The truth value of a proposition $p$ is denoted $\text{val}(p) \in \{T, F\}$ or $\text{val}(p) \in \{1, 0\}$.

### 1.1 Valid Propositions:
- $p$: "$\pi > 3$" ($\text{val}(p) = T$)
- $q$: "$2 + 2 = 5$" ($\text{val}(q) = F$)
- $r$: "Every prime number greater than 2 is odd." ($\text{val}(r) = T$)
- $s$: "The moon is made of green cheese." ($\text{val}(s) = F$)

### 1.2 Non-Propositions (Invalid):
- "What time is it?" (Interrogative — has no truth value)
- "Read this book carefully." (Imperative / Command)
- "$x + y = z$" (Open sentence / Predicate with unquantified free variables)
- "This statement is false." (Paradox / Liar's Paradox — cannot consistently be assigned $T$ or $F$)

---

## 2. Logical Connectives and Formal Operators

Let $p$ and $q$ be propositions. Compound propositions are formed using logical connectives:

### 2.1 Negation (NOT: $\neg p$ or $\sim p$)
The negation of $p$ is true if and only if $p$ is false:
$$\text{val}(\neg p) = \begin{cases} T & \text{if } \text{val}(p) = F \\ F & \text{if } \text{val}(p) = T \end{cases}$$

### 2.2 Conjunction (AND: $p \land q$)
The conjunction of $p$ and $q$ is true if and only if both $p$ and $q$ are true:
$$\text{val}(p \land q) = \min(\text{val}(p), \text{val}(q))$$

### 2.3 Disjunction (Inclusive OR: $p \lor q$)
The disjunction of $p$ and $q$ is false if and only if both $p$ and $q$ are false:
$$\text{val}(p \lor q) = \max(\text{val}(p), \text{val}(q))$$

### 2.4 Exclusive OR (XOR: $p \oplus q$)
The exclusive disjunction is true if and only if exactly one of $p$ and $q$ is true:
$$p \oplus q \equiv (p \lor q) \land \neg(p \land q) \equiv (p \land \neg q) \lor (\neg p \land q)$$

### 2.5 Conditional Statement / Implication ($p \to q$)
The statement "$p$ implies $q$" or "If $p$, then $q$".
- $p$ is called the **hypothesis**, **antecedent**, or **premise**.
- $q$ is called the **conclusion** or **consequence**.

$$\text{val}(p \to q) = \begin{cases} F & \text{if } \text{val}(p) = T \text{ and } \text{val}(q) = F \\ T & \text{otherwise} \end{cases}$$

#### Linguistic Variations of $p \to q$:
- "If $p$, then $q$"
- "$p$ implies $q$"
- "$q$ if $p$"
- "$p$ only if $q$" (means $p \to q$, NOT $q \to p$)
- "$p$ is sufficient for $q$"
- "$q$ is necessary for $p$"
- "$q$ whenever $p$"
- "$q$ follows from $p$"

### 2.6 Biconditional Statement ($p \leftrightarrow q$)
The biconditional statement "$p$ if and only if $q$" (abbreviated *iff*) is true when $p$ and $q$ have identical truth values:
$$p \leftrightarrow q \equiv (p \to q) \land (q \to p)$$

---

## 3. Master Truth Table

| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$ | $p \oplus q$ | $p \to q$ | $q \to p$ | $p \leftrightarrow q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $T$ | $T$ | $F$ | $T$ | $T$ | $F$ | $T$ | $T$ | $T$ |
| $T$ | $F$ | $F$ | $F$ | $T$ | $T$ | $F$ | $T$ | $F$ |
| $F$ | $T$ | $T$ | $F$ | $T$ | $T$ | $T$ | $F$ | $F$ |
| $F$ | $F$ | $T$ | $F$ | $F$ | $F$ | $T$ | $T$ | $T$ |

---

## 4. Operator Precedence and Parentheses

When expressions omit parentheses, operators are evaluated in the following strict order of precedence (highest to lowest):

1. **$\neg$** (Negation)
2. **$\land$** (Conjunction)
3. **$\lor$** (Disjunction)
4. **$\to$** (Conditional)
5. **$\leftrightarrow$** (Biconditional)

$$\neg p \land q \to r \equiv ((\neg p) \land q) \to r$$

---

## 5. Applications: System Specifications & Consistency

In system design, a set of system requirements must be **consistent** (satisfiable). A system specification is consistent if there exists at least one truth assignment that makes all specification propositions true simultaneously.

### Example:
- $S_1$: "The diagnostic message is stored in the buffer or it is retransmitted." ($p \lor q$)
- $S_2$: "The diagnostic message is not stored in the buffer." ($\neg p$)
- $S_3$: "If the diagnostic message is stored in the buffer, then it is retransmitted." ($p \to q$)
- **Consistency Analysis:** If $p = F$ and $q = T$:
  - $S_1: F \lor T = T$
  - $S_2: \neg F = T$
  - $S_3: F \to T = T$
  - Since all specifications evaluate to $T$ simultaneously under $(p=F, q=T)$, the system specification is **consistent**.

---

## 6. Bitwise Logic and Computer Words

A **bit** is a binary digit $\{0, 1\}$ representing $\{F, T\}$. A **bit string** is a sequence of zero or more bits.

Logical operations extended to $n$-bit words:
```
Bit string A:  1 0 1 1 0 0 1 0
Bit string B:  1 1 0 1 1 0 0 0
------------------------------
A AND B:       1 0 0 1 0 0 0 0
A OR  B:       1 1 1 1 1 0 1 0
A XOR B:       0 1 1 0 1 0 1 0
NOT A (8-bit): 0 1 0 0 1 1 0 1
```
