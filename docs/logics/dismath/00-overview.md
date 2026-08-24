# Discrete Mathematics Logic Overview (DISMATH)

This documentation provides a comprehensive, rigorous reference for **Mathematical Logic and Methods of Proof** based on the standard curriculum of **Discrete Mathematics and its Applications** (by *Kenneth H. Rosen*). It serves as a theoretical foundation for computational problem-solving, software engineering, formal verification, and algorithmic reasoning.

---

## 🌟 Table of Contents & Curriculum Map

| Chapter | Document | Core Coverage & Theoretical Topics |
| :---: | :--- | :--- |
| 01 | [`01-propositional-logic.md`](./01-propositional-logic.md) | **Propositional Logic:** Propositions, truth values, 6 fundamental connectives ($\neg, \land, \lor, \oplus, \to, \leftrightarrow$), master truth table, operator precedence, system consistency, and bitwise operations. |
| 02 | [`02-logical-equivalences.md`](./02-logical-equivalences.md) | **Logical Equivalences:** Tautologies, contradictions, contingencies, comprehensive equivalence laws (De Morgan, Distributive, Absorption, Conditional Laws), and conditional variations (converse, inverse, contrapositive). |
| 03 | [`03-predicate-logic-and-quantifiers.md`](./03-predicate-logic-and-quantifiers.md) | **Predicate Logic & Quantifiers:** Predicates, propositional functions $P(x)$, domain of discourse, universal ($\forall$), existential ($\exists$), and uniqueness ($\exists!$) quantifiers, De Morgan's laws for quantifiers. |
| 04 | [`04-nested-quantifiers.md`](./04-nested-quantifiers.md) | **Nested Quantifiers:** Multi-variable quantification, semantic differences between $\forall x \exists y$ and $\exists y \forall x$, translating natural language statements, and quantifier negation. |
| 05 | [`05-rules-of-inference.md`](./05-rules-of-inference.md) | **Rules of Inference & Valid Arguments:** Modus Ponens, Modus Tollens, Syllogisms, Resolution, logical fallacies (affirming the conclusion, denying the hypothesis), and quantifier inference rules (UI, UG, EI, EG). |
| 06 | [`06-methods-of-proof.md`](./06-methods-of-proof.md) | **Methods of Proof:** Direct proof, proof by contraposition, proof by contradiction ($p \land \neg q \to \mathbf{F}$), vacuous & trivial proofs, proof by cases, and exhaustive proofs. |
| 07 | [`07-mathematical-induction-and-recursion.md`](./07-mathematical-induction-and-recursion.md) | **Mathematical Induction & Recursion:** Principle of mathematical induction (basis & inductive step), strong induction, well-ordering property, recursive definitions, and structural induction. |
| 08 | [`08-program-correctness-and-hoare-logic.md`](./08-program-correctness-and-hoare-logic.md) | **Program Correctness & Hoare Logic:** Hoare triples $\{P\} S \{Q\}$, pre/post-conditions, assignment rule, composition rule, conditional rule, and loop invariants (initialization, maintenance, termination). |
| 09 | [`09-boolean-algebra-and-combinatorial-circuits.md`](./09-boolean-algebra-and-combinatorial-circuits.md) | **Boolean Algebra & Digital Circuits:** Huntington postulates, duality principle, canonical forms (DNF/CNF), functional completeness (NAND/NOR), logic gates, and half/full adders. |
| 10 | [`10-puzzle-solving-and-sat-modeling.md`](./10-puzzle-solving-and-sat-modeling.md) | **Logic Puzzles & SAT Modeling:** Smullyan's Knights and Knaves biconditional modeling, Boolean satisfiability (SAT / 3-SAT NP-completeness), and resolution refutation theorem proving. |

---

## 📐 Mathematical Logic Notation Reference

| Symbol | Formal Name | Meaning / Operation | Canonical Example |
| :---: | :--- | :--- | :---: |
| $\neg$ or $\sim$ | Negation | NOT | $\neg p$ |
| $\land$ | Conjunction | AND | $p \land q$ |
| $\lor$ | Disjunction | OR (Inclusive) | $p \lor q$ |
| $\oplus$ | Exclusive OR | XOR | $p \oplus q$ |
| $\to$ | Conditional | Implication (If... then...) | $p \to q$ |
| $\leftrightarrow$ | Biconditional | If and only if (iff) | $p \leftrightarrow q$ |
| $\equiv$ or $\Leftrightarrow$ | Logical Equivalence | Logically equivalent | $p \to q \equiv \neg p \lor q$ |
| $\forall$ | Universal Quantifier | For all / For every | $\forall x P(x)$ |
| $\exists$ | Existential Quantifier | There exists / For some | $\exists x P(x)$ |
| $\exists!$ | Uniqueness Quantifier | There exists a unique | $\exists! x P(x)$ |
| $\vdash$ or $\implies$ | Logical Entailment | Infers / Yields | $p, p \to q \vdash q$ |
| $\{P\} S \{Q\}$ | Hoare Triple | Program specification | $\{\text{Pre}\} \text{ Code } \{\text{Post}\}$ |
| $\mid$ | Sheffer Stroke | NAND operator | $p \mid q \equiv \neg(p \land q)$ |
| $\downarrow$ | Peirce Arrow | NOR operator | $p \downarrow q \equiv \neg(p \lor q)$ |
