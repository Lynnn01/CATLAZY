# 10. Logic Puzzle Modeling and Boolean Satisfiability (SAT)

Logic puzzle modeling and the Boolean Satisfiability problem (SAT) form the bridge between theoretical logic, artificial intelligence, automated reasoning, and formal verification.

---

## 1. Modeling Knights and Knaves Puzzles

On the Island of Knights and Knaves (originated by logician Raymond Smullyan):
- **Knights ($A = T$):** Always tell the truth.
- **Knaves ($A = F$):** Always lie.

### 1.1 Invariant Formulation Rule:
If inhabitant $A$ makes a statement $S$, the logical relation is strictly captured by the biconditional equivalence:
$$\mathbf{A \longleftrightarrow S}$$

### 1.2 Worked Example 1 (Two Inhabitants):
Inhabitant $A$ says: *"At least one of us is a knave."*
Inhabitant $B$ says nothing.

- **Variables:**
  - $A$: "$A$ is a knight" ($A = T$ if knight, $A = F$ if knave).
  - $B$: "$B$ is a knight" ($B = T$ if knight, $B = F$ if knave).
- **Statement Formulation:**
  - $S_A$: "At least one of us is a knave" $\equiv \neg A \lor \neg B$.
- **System Equation:**
  $$A \longleftrightarrow (\neg A \lor \neg B)$$
- **Truth Analysis:**
  - Case 1 ($A = F$): If $A = F$, the left-hand side is $F$. The right-hand side becomes $(\neg F \lor \neg B) = (T \lor \neg B) = T$. This gives $F \leftrightarrow T$, which is a contradiction ($F$).
  - Case 2 ($A = T$): If $A = T$, the left-hand side is $T$. The right-hand side becomes $(\neg T \lor \neg B) = (F \lor \neg B) = \neg B$. For the biconditional $T \leftrightarrow \neg B$ to be true, we must have $\neg B = T \implies B = F$.
- **Conclusion:** $A$ is a **Knight**, and $B$ is a **Knave**.

---

## 2. The Boolean Satisfiability Problem (SAT)

A propositional formula $\phi$ is **satisfiable** if there exists at least one truth assignment to its variables such that $\phi$ evaluates to **True ($T$)**. If no such assignment exists, $\phi$ is **unsatisfiable** (a contradiction).

### 2.1 CNF Formulation (Conjunctive Normal Form)
A formula $\phi$ in CNF is a conjunction of clauses:
$$\phi = C_1 \land C_2 \land \dots \land C_m$$
where each clause $C_i$ is a disjunction of literals:
$$C_i = (l_{i,1} \lor l_{i,2} \lor \dots \lor l_{i,k})$$

### 2.2 $k$-SAT Classification:
- **2-SAT:** Every clause has at most 2 literals. (Solvable in polynomial time $O(V + E)$ using Strongly Connected Components / Implication Graphs).
- **3-SAT:** Every clause has 3 literals. (Proven by Stephen Cook in 1971 to be **NP-Complete** — the Cook-Levin Theorem).

---

## 3. Automated Theorem Proving via Resolution Refutation

To prove that a set of premises $\{P_1, P_2, \dots, P_n\}$ entails conclusion $Q$ ($P_1 \land \dots \land P_n \models Q$):
1. Convert all premises $P_1, \dots, P_n$ to CNF clauses.
2. Negate the target conclusion: $\neg Q$, and convert to CNF clauses.
3. Form the set of all clauses: $\mathcal{S} = \{C_1, C_2, \dots, C_m, \neg Q\}$.
4. Iteratively apply the **Resolution Rule**:
   $$\frac{A \lor l \quad \text{and} \quad B \lor \neg l}{\therefore A \lor B}$$
5. If the **empty clause $\Box$ (Contradiction)** is derived, then $\mathcal{S}$ is unsatisfiable, proving that $Q$ is a logically valid consequence.
