# 05. Rules of Inference and Valid Arguments

An **argument** in propositional logic is a sequence of propositions ending with a conclusion. The initial propositions are called **premises (or hypotheses: $p_1, p_2, \dots, p_n$)**, and the final proposition is the **conclusion ($q$)**.

An argument is **valid** if and only if the truth of all premises forces the conclusion to be true. Formally:

$$(p_1 \land p_2 \land \dots \land p_n) \to q \quad \text{is a tautology.}$$

---

## 1. Rules of Inference for Propositional Logic

| Rule of Inference | Underlying Tautology | Name of Rule |
| :---: | :---: | :--- |
| $\begin{aligned} &p \\ &\underline{p \to q} \\ \therefore &q \end{aligned}$ | $[p \land (p \to q)] \to q$ | **Modus Ponens** (Law of Detachment) |
| $\begin{aligned} &\neg q \\ &\underline{p \to q} \\ \therefore &\neg p \end{aligned}$ | $[\neg q \land (p \to q)] \to \neg p$ | **Modus Tollens** (Law of Contraposition) |
| $\begin{aligned} &p \to q \\ &\underline{q \to r} \\ \therefore &p \to r \end{aligned}$ | $[(p \to q) \land (q \to r)] \to (p \to r)$ | **Hypothetical Syllogism** (Chain Rule) |
| $\begin{aligned} &p \lor q \\ &\underline{\neg p} \\ \therefore &q \end{aligned}$ | $[(p \lor q) \land \neg p] \to q$ | **Disjunctive Syllogism** |
| $\begin{aligned} &\underline{p} \\ \therefore &p \lor q \end{aligned}$ | $p \to (p \lor q)$ | **Addition** |
| $\begin{aligned} &\underline{p \land q} \\ \therefore &p \end{aligned}$ | $(p \land q) \to p$ | **Simplification** |
| $\begin{aligned} &p \\ &\underline{q} \\ \therefore &p \land q \end{aligned}$ | $[(p) \land (q)] \to (p \land q)$ | **Conjunction** |
| $\begin{aligned} &p \lor q \\ &\underline{\neg p \lor r} \\ \therefore &q \lor r \end{aligned}$ | $[(p \lor q) \land (\neg p \lor r)] \to (q \lor r)$ | **Resolution** (Core of Automated Theorem Proving) |

---

## 2. Common Logical Fallacies

Invalid arguments (fallacies) arise when an incorrect deductive step is taken:

### 2.1 Fallacy of Affirming the Conclusion
- Invalid Schema: $p \to q$ and $q$, concluding $p$.
- *Example:* "If it rains, the street is wet. The street is wet. Therefore, it rained." (Invalid: street could be wet from a fire hydrant).

### 2.2 Fallacy of Denying the Hypothesis
- Invalid Schema: $p \to q$ and $\neg p$, concluding $\neg q$.
- *Example:* "If you study hard, you pass. You did not study hard. Therefore, you failed." (Invalid: you might pass due to prior knowledge).

---

## 3. Rules of Inference for Quantified Statements

When reasoning with predicates and quantifiers ($\forall, \exists$), specific rules govern variable instantiation and generalization:

| Rule of Inference | Name | Condition / Applicability |
| :---: | :--- | :--- |
| $\begin{aligned} &\underline{\forall x P(x)} \\ \therefore &P(c) \end{aligned}$ | **Universal Instantiation (UI)** | For an arbitrary or specific element $c$ in the domain. |
| $\begin{aligned} &\underline{P(c) \text{ for an arbitrary } c} \\ \therefore &\forall x P(x) \end{aligned}$ | **Universal Generalization (UG)** | $c$ must be an arbitrary, generic element with no special assumptions. |
| $\begin{aligned} &\underline{\exists x P(x)} \\ \therefore &P(c) \text{ for some element } c \end{aligned}$ | **Existential Instantiation (EI)** | $c$ must be a fresh, newly introduced constant not used previously. |
| $\begin{aligned} &\underline{P(c) \text{ for some known } c} \\ \therefore &\exists x P(x) \end{aligned}$ | **Existential Generalization (EG)** | At least one valid witness $c$ is known to satisfy $P(c)$. |
