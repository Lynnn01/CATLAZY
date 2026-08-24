# 08. Program Correctness and Hoare Logic

Program verification uses mathematical logic to formally prove that an algorithm or code segment behaves correctly according to its specification for all valid inputs.

---

## 1. Program Specifications and Hoare Triples

A program or code fragment $S$ is formally specified using two logical assertions:
1. **Pre-condition ($p$):** A predicate that must hold true before program execution begins.
2. **Post-condition ($q$):** A predicate that must hold true after program execution terminates.

### Hoare Triple Notation:
$$\mathbf{\{p\}\ S\ \{q\}}$$

**Meaning:** If the pre-condition $p$ is true before the execution of code segment $S$, and if $S$ terminates, then the post-condition $q$ is guaranteed to be true upon termination (Partial Correctness).

---

## 2. Axiomatic Inference Rules for Program Statements

### 2.1 Assignment Rule
For an assignment statement $x := \text{expr}$:
$$\mathbf{\{p[x / \text{expr}]\}\ x := \text{expr}\ \{p\}}$$
*Example:* To guarantee $\{x > 5\}$ after executing $x := x + 1$, the required pre-condition is $\{x + 1 > 5\} \equiv \{x > 4\}$.

### 2.2 Composition Rule (Sequential Execution)
If statement $S_1$ transforms state $p$ into $q$, and $S_2$ transforms state $q$ into $r$:
$$\frac{\{p\}\ S_1\ \{q\} \quad \land \quad \{q\}\ S_2\ \{r\}}{\therefore \{p\}\ S_1; S_2\ \{r\}}$$

### 2.3 Conditional Rule (`if-then-else`)
For a branching statement `if condition then S1 else S2`:
$$\frac{\{p \land \text{condition}\}\ S_1\ \{q\} \quad \land \quad \{p \land \neg\text{condition}\}\ S_2\ \{q\}}{\therefore \{p\}\ \text{if condition then } S_1 \text{ else } S_2\ \{q\}}$$

---

## 3. Loop Invariants

To prove the correctness of a loop `while condition do S`, we identify a logical assertion $I$ called the **loop invariant**.

### Three Core Invariant Properties:
1. **Initialization:** The invariant $I$ must be **True** prior to the first iteration of the loop.
2. **Maintenance:** If $I$ is true before an iteration, and the loop guard $\text{condition}$ holds, then $I$ remains **True** after executing the loop body $S$:
   $$\{I \land \text{condition}\}\ S\ \{I\}$$
3. **Termination:** When the loop terminates ($\neg\text{condition}$ is true), the conjunction of the invariant and the negated guard must establish the intended post-condition $q$:
   $$\{I\}\ \text{while condition do } S\ \{I \land \neg\text{condition}\} \implies q$$

---

## 4. Total Correctness

$$\text{Total Correctness} = \text{Partial Correctness (Soundness of Output)} + \text{Termination (Guaranteed Halting)}$$

To guarantee loop termination, we define a **loop variant (ranking function)** $V$, which maps the program state to a non-negative integer ($\mathbb{Z}^{\ge 0}$) that strictly decreases on each iteration, bounding the execution steps via the Well-Ordering Property.
