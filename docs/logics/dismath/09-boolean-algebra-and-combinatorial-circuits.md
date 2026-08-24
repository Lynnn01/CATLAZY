# 09. Boolean Algebra and Combinatorial Circuits

Boolean algebra provides the mathematical framework for modeling digital logic circuits, digital signal processing, and propositional formulas.

---

## 1. Axiomatic Definition of Boolean Algebra

A **Boolean algebra** is an algebraic structure $\langle B, +, \cdot, -, 0, 1 \rangle$ where $B$ is a set containing at least two distinct elements $0$ and $1$, equipped with two binary operations $+$ (OR) and $\cdot$ (AND), and one unary operation $-$ (NOT / Complement), satisfying the following Huntington Postulates for all $x, y, z \in B$:

1. **Closure:** $x + y \in B$ and $x \cdot y \in B$.
2. **Identity Elements:**
   $$x + 0 = x \quad \text{and} \quad x \cdot 1 = x$$
3. **Commutative Laws:**
   $$x + y = y + x \quad \text{and} \quad x \cdot y = y \cdot x$$
4. **Distributive Laws:**
   $$x \cdot (y + z) = (x \cdot y) + (x \cdot z) \quad \text{and} \quad x + (y \cdot z) = (x + y) \cdot (x + z)$$
5. **Complement Laws:**
   $$x + \overline{x} = 1 \quad \text{and} \quad x \cdot \overline{x} = 0$$

### Duality Principle
Any true identity in a Boolean algebra remains true if:
- $+$ and $\cdot$ are interchanged
- $0$ and $1$ are interchanged

---

## 2. Canonical Normal Forms

Any Boolean function $f(x_1, x_2, \dots, x_n)$ can be uniquely expressed in standard canonical normal forms:

### 2.1 Minterms and Disjunctive Normal Form (DNF / Sum-of-Products)
A **minterm** of $n$ variables is a product (conjunction) of $n$ literals, with each variable appearing exactly once (either complemented or uncomplemented).
- **Disjunctive Normal Form (DNF):** A disjunction of distinct minterms where the function evaluates to $1$.

*Example:* $f(x, y, z) = 1$ when $(x, y, z) \in \{(1, 1, 0), (0, 1, 1)\}$
$$\text{DNF} = (x y \overline{z}) + (\overline{x} y z)$$

### 2.2 Maxterms and Conjunctive Normal Form (CNF / Product-of-Sums)
A **maxterm** of $n$ variables is a sum (disjunction) of $n$ literals.
- **Conjunctive Normal Form (CNF):** A conjunction of maxterms where the function evaluates to $0$.

$$\text{CNF} = \prod (\text{Maxterms where } f = 0)$$

---

## 3. Functional Completeness

A set of logical operators is **functionally complete** if every possible Boolean function can be expressed solely using operators from that set.

### 3.1 Standard Functionally Complete Sets:
- $\{\neg, \land, \lor\}$
- $\{\neg, \land\}$ (since $p \lor q \equiv \neg(\neg p \land \neg q)$)
- $\{\neg, \lor\}$ (since $p \land q \equiv \neg(\neg p \lor \neg q)$)

### 3.2 Single-Operator Complete Sets (Universal Gates):
1. **NAND (Sheffer Stroke $\mid$):** $p \mid q \equiv \neg(p \land q)$
   - $\neg p \equiv p \mid p$
   - $p \land q \equiv (p \mid q) \mid (p \mid q)$
   - $p \lor q \equiv (p \mid p) \mid (q \mid q)$
2. **NOR (Peirce Arrow $\downarrow$):** $p \downarrow q \equiv \neg(p \lor q)$
   - $\neg p \equiv p \downarrow p$
   - $p \lor q \equiv (p \downarrow q) \downarrow (p \downarrow q)$
   - $p \land q \equiv (p \downarrow p) \downarrow (q \downarrow q)$

---

## 4. Digital Logic Gates and Combinatorial Arithmetic

### 4.1 Basic Logic Gates

| Gate Name | Boolean Expression | Graphic Symbol Representation |
| :---: | :---: | :--- |
| **AND** | $x \cdot y$ | Multiplies binary inputs; output is $1$ iff all inputs are $1$. |
| **OR** | $x + y$ | Sums binary inputs; output is $1$ if at least one input is $1$. |
| **NOT (Inverter)** | $\overline{x}$ | Inverts input bit ($0 \to 1, 1 \to 0$). |
| **NAND** | $\overline{x \cdot y}$ | Inverted AND gate; output is $0$ iff all inputs are $1$. |
| **NOR** | $\overline{x + y}$ | Inverted OR gate; output is $1$ iff all inputs are $0$. |
| **XOR** | $x \oplus y$ | Output is $1$ iff inputs differ. |

---

### 4.2 Arithmetic Circuit Design: Half Adder and Full Adder

#### Half Adder (Adds two bits $x$ and $y$):
- **Sum ($S$):** $S = x \oplus y$
- **Carry ($C$):** $C = x \cdot y$

```
   x ──┬─────────( XOR )──── Sum (S)
       │            ▲
   y ──┼──────┬─────┘
       │      │
       └──────┼──( AND )──── Carry (C)
              └─────┘
```

#### Full Adder (Adds two bits $x, y$ plus an incoming Carry $C_{\text{in}}$):
- **Sum ($S$):** $S = x \oplus y \oplus C_{\text{in}}$
- **Carry Out ($C_{\text{out}}$):** $C_{\text{out}} = (x \cdot y) + (C_{\text{in}} \cdot (x \oplus y))$
