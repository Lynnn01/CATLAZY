# 03. Predicate Logic and Quantifiers

Propositional logic is insufficient to express mathematical statements involving variables (e.g., "$x > 3$" or "Every integer has an additive inverse"). **Predicate logic (First-Order Logic)** extends propositional logic by introducing predicates, functions, and quantifiers.

---

## 1. Predicates and Propositional Functions

A statement such as "$x > 3$" consists of two parts:
1. **Subject / Variable:** $x$
2. **Predicate:** "$> 3$" (the property that the subject can have)

We denote this as a propositional function $P(x)$, where $P$ is the predicate "$> 3$":
- $P(x)$ is not a proposition on its own because its truth value depends on the value of $x$.
- When $x = 4$, $P(4)$ is the statement "$4 > 3$", which is a proposition with truth value **True ($T$)**.
- When $x = 2$, $P(2)$ is the statement "$2 > 3$", which is a proposition with truth value **False ($F$)**.

### Domain of Discourse (Universe of Discourse)
The domain is the set of all possible values that can be assigned to the variable $x$ (e.g., all integers $\mathbb{Z}$, all real numbers $\mathbb{R}$, or all elements in a database).

---

## 2. Quantifiers

A propositional function $P(x)$ can be converted into a proposition via:
1. Assigning a concrete value to $x$ (e.g., $P(4)$)
2. Applying a **quantifier**

### 2.1 Universal Quantifier ($\forall$)
The statement $\forall x P(x)$ reads: *"For all $x$, $P(x)$ is true."*
- **True ($T$):** If and only if $P(x)$ is true for **every** element $x$ in the domain.
- **False ($F$):** If there exists **at least one** element $x$ in the domain for which $P(x)$ is false. Such an element is called a **counterexample**.

*Example:* Domain = $\mathbb{R}$ (all real numbers)
- $\forall x (x^2 \ge 0)$ is **True ($T$)**.
- $\forall x (x^2 > 0)$ is **False ($F$)**, with counterexample $x = 0$ ($0^2 \not> 0$).

### 2.2 Existential Quantifier ($\exists$)
The statement $\exists x P(x)$ reads: *"There exists an $x$ such that $P(x)$ is true."*
- **True ($T$):** If there is **at least one** element $x$ in the domain for which $P(x)$ is true.
- **False ($F$):** If and only if $P(x)$ is false for **every** element $x$ in the domain.

*Example:* Domain = $\mathbb{Z}$ (all integers)
- $\exists x (x + 3 = 10)$ is **True ($T$)** (witnessed by $x = 7$).
- $\exists x (x = x + 1)$ is **False ($F$)**.

### 2.3 Uniqueness Quantifier ($\exists!$)
The statement $\exists! x P(x)$ reads: *"There exists a unique $x$ such that $P(x)$."* It is true if and only if exactly one element in the domain satisfies $P(x)$.

---

## 3. Finite Domain Equivalence

If the domain consists of finite elements $\{x_1, x_2, \dots, x_n\}$:
- $\forall x P(x) \equiv P(x_1) \land P(x_2) \land \dots \land P(x_n)$
- $\exists x P(x) \equiv P(x_1) \lor P(x_2) \lor \dots \lor P(x_n)$

---

## 4. De Morgan's Laws for Quantifiers (Negating Quantified Statements)

The rules for pushing negations through quantifiers:

$$\neg \forall x P(x) \equiv \exists x \neg P(x)$$
$$\neg \exists x P(x) \equiv \forall x \neg P(x)$$

### Natural Language Translations:
- Negation of *"Every student submitted the homework"* ($\neg \forall x P(x)$)
  - is *"There is a student who did not submit the homework"* ($\exists x \neg P(x)$).
- Negation of *"There exists a flying dog"* ($\neg \exists x P(x)$)
  - is *"Every dog cannot fly"* ($\forall x \neg P(x)$).
