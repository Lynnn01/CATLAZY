<div align="center">
  <h1>🐈 Catlazy Agent Architecture</h1>
  <p><strong>The Lazy Senior Dev Philosophy — Formally Grounded in Discrete Mathematics (DISMATH)</strong></p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![AI: Antigravity](https://img.shields.io/badge/AI_Agent-Antigravity-blue.svg)]()
  [![Logic: DISMATH](https://img.shields.io/badge/Logic-DISMATH_Ch.01--10-blueviolet.svg)](docs/logics/dismath/00-overview.md)
  [![Architecture: Clean_DDD](https://img.shields.io/badge/Architecture-Clean__DDD-success.svg)](docs/architecture/)
</div>

---

## 🧭 Table of Contents

1. [What is Catlazy?](#-what-is-catlazy)
2. [🧠 DISMATH: The Formal Reasoning Core](#-dismath-the-formal-reasoning-core)
3. [🛠️ DISMATH × Skill Integration (Ch. 01–11)](#️-dismath--skill-integration-ch-0111)
4. [🏗️ Project Structure](#️-project-structure)
5. [🎚️ Operating Modes & Intensity](#️-operating-modes--intensity)
6. [🌐 Cross-Platform Embedding](#-cross-platform-embedding-catlazy---embed)
7. [📋 Universal 3-Section Output Format](#-universal-3-section-output-format)
8. [💡 Practical Workflow Example](#-practical-workflow-example)
9. [🚀 Installation & Quick Start](#-installation--quick-start)

---

## 🐱 What is Catlazy?

**Catlazy** is an agent architecture, rule system, and skill suite for AI coding assistants (Google Antigravity, Claude, Cursor, Windsurf, GitHub Copilot). It trains AI agents to operate as **Lazy Senior Developers** — solving problems directly, avoiding speculative complexity, and making every decision traceable back to a formal mathematical argument.

**Core operating principle — The Ladder of Laziness:**

```text
1. YAGNI        → Does this feature need to exist today?           (Ch.05 Modus Tollens)
2. Reuse        → Does a solution already exist in shared/?        (Ch.03 Existential ∃)
3. Stdlib       → Can the standard library solve this?             (Ch.06 Direct Proof)
4. Native       → Can native platform features handle this?        (Ch.06 Direct Proof)
5. Dependency   → If a package is needed, pick the leanest.        (Ch.06 Proof by Cases)
6. One-line     → Can this logic be expressed in one clear line?   (Ch.09 Minimization)
7. Minimum Impl → Write the smallest code fulfilling requirements. (Ch.08 Hoare {P} S {Q})
```

---

## 🧠 DISMATH: The Formal Reasoning Core

Every action, plan, and judgment made by a Catlazy agent is grounded in **Kenneth H. Rosen's Discrete Mathematics (Ch. 01–10)**. This is not decoration — it is the actual formal foundation that governs how agents reason, prove, and make decisions.

### Why Formal Logic Matters in AI Agents

Without formal grounding, AI agents reason by pattern-matching: they write code that "looks right" but can't be verified. DISMATH changes this. Every Catlazy skill operates using a precisely defined formal model:

```text
Plan     →  {P} S {Q}         (Hoare Triple, Ch. 08)
Review   →  Σ ∪ {¬Q} ⊢ □     (Resolution Refutation, Ch. 10)
Arch     →  ∀f∈Domain, ∀d∈Imports(f): d ∉ {Infra}   (Predicate, Ch. 03–04)
Loop     →  V(i) = TARGET – CURRENT ≥ 0 ↓ strictly  (Well-Ordering, Ch. 07)
YAGNI    →  ¬IsNeeded(F) ∴ ¬Build(F)               (Modus Tollens, Ch. 05)
```

### DISMATH Curriculum Map

| Chapter | DISMATH Topic | Formal Notation |
|:---:|---|---|
| **01** | Propositional Logic | $p, q, \neg p, p \land q, p \lor q, p \to q$ |
| **02** | Logical Equivalences | $P_{\text{old}} \equiv P_{\text{new}}$, De Morgan, Contrapositive |
| **03** | Predicate Logic & Quantifiers | $\forall x\, P(x)$, $\exists x\, P(x)$ |
| **04** | Nested Quantifiers | $\forall f \in D,\, \forall d \in \text{Imports}(f)\, [Q(f,d)]$ |
| **05** | Rules of Inference | Modus Ponens, Modus Tollens, Resolution |
| **06** | Methods of Proof | Direct, Contradiction, Contraposition, Vacuous |
| **07** | Mathematical Induction | $V(i) > 0,\ V(i+1) < V(i)$, Well-Ordering |
| **08** | Hoare Logic / Program Correctness | $\{P\}\, S\, \{Q\}$, Loop Invariants $\{I\}$ |
| **09** | Boolean Algebra & Minimization | De Morgan, Absorption, DNF/CNF simplification |
| **10** | SAT Modeling & Resolution Refutation | $\varphi \not\equiv \mathbf{F}$, Resolution $\frac{p \lor q,\ \neg p \lor r}{q \lor r}$ |

📖 Full reference: [`docs/logics/dismath/00-overview.md`](docs/logics/dismath/00-overview.md)  
🔗 Integration bridge: [`docs/logics/dismath/11-catlazy-formal-methods.md`](docs/logics/dismath/11-catlazy-formal-methods.md)

---

## 🛠️ DISMATH × Skill Integration (Ch. 01–11)

Each Catlazy skill maps directly to one or more DISMATH chapters. Below is the authoritative mapping:

---

### `/catlazy` — Configure Intensity & Embed

**DISMATH Ch. 01–02:** Propositional Logic & Logical Equivalences

The mode configuration system checks that the selected rule set is **satisfiable** (not contradictory) before activating. The `--embed` command applies logical equivalence checks across platform rule files to guarantee consistent behavior.

```text
Formal Check: φ_rules ≢ F  (Rule set is SAT — Ch. 01)
Equivalence:  rules_A ≡ rules_B across Claude / Cursor / Windsurf  (Ch. 02)
```

---

### `/catlazy0-help` — Quick Reference Guide

**DISMATH Ch. 01:** Propositional Logic (Reference)

Provides a complete, unambiguous propositional specification of all commands, intensity levels, and operating rules — ensuring agents receive logically consistent instructions.

---

### `/catlazy1-design` — Brainstorm & Plan with Hoare Triples

**DISMATH Ch. 05 (Modus Tollens), Ch. 06 (Proof by Contradiction), Ch. 08 (Hoare Logic)**

Before any code is written, this skill runs a **3-step interview gate** grounded in formal logic:

1. **YAGNI Filter (Modus Tollens — Ch. 05):**

   $$\text{Premise 1: } \text{IsNeeded}(F) \implies \text{Build}(F)$$
   $$\text{Premise 2: } \neg\text{IsNeeded}(F)$$
   $$\therefore\; \neg\text{Build}(F) \quad (\text{Modus Tollens})$$

2. **Necessity Proof (Proof by Contradiction — Ch. 06):**  
   To justify a new abstraction $A$, prove that $\neg A \implies \text{Failure}$ (achieving the goal without $A$ is impossible).

3. **Hoare Plan Generation (Ch. 08):**  
   Output a formal plan as: $\{P\}\, S\, \{Q\}$ saved to `docs/plans/YYYY-MM-DD-*.md`.
   
   | Component | Meaning |
   |---|---|
   | **Pre-condition $P$** | Current verified state of the codebase before changes |
   | **Statement $S$** | Minimal, approved sequence of atomic modifications |
   | **Post-condition $Q$** | Verifiable assertions that must hold after $S$ |
   | **Invariant $I$** | Architecture boundaries & safety constraints that never break |

   $$\{P \land I\}\, S\, \{Q \land I\}$$

---

### `/catlazy2-review` — Diff Review by Resolution Refutation

**DISMATH Ch. 05 (Rules of Inference), Ch. 06 (Proof Methods), Ch. 08 (Hoare Diffs), Ch. 10 (Resolution)**

Given a Git diff $\Delta$, the agent constructs a knowledge base $\Sigma = \{I, P, \Delta\}$ and verifies correctness by Resolution Refutation:

$$\text{Assume negation: } \neg Q$$
$$\text{Apply Resolution: } \frac{p \lor q,\quad \neg p \lor r}{q \lor r}$$
$$\text{If } \Sigma \cup \{\neg Q\} \vdash \Box\; (\text{contradiction}), \text{ then } \Delta \text{ is correct.}$$

**Fallacy Guard (Ch. 05):** The reviewer is explicitly forbidden from all 4 informal fallacies:
- **Affirming the Consequent** ($p \to q, q \vdash p$): "It uses Clean Architecture → it must be correct."
- **Denying the Antecedent** ($p \to q, \neg p \vdash \neg q$): "Without Redis → the task is impossible."
- **Circular Reasoning / Begging the Question** ($p \vdash p$): "It's over-engineered because it has too much engineering."
- **False Dilemma** ($p \lor q$ when $\exists r$): "We must rewrite entirely or leave the bug." (Missing: targeted one-line patch.)

**Hollow Implementation Detection (Ch. 06 — Vacuous Proof guard):**  
`TODO` stubs, fake returns, and empty handlers are flagged as vacuously true (trivially passing) code — a proof technique that proves nothing meaningful.

---

### `/catlazy3-architecture` — Layer Invariant Audit

**DISMATH Ch. 03 (Predicate Logic), Ch. 04 (Nested Quantifiers)**

Architecture compliance is defined as a **universally quantified predicate** over all source files:

$$\text{Inv}_{\text{Domain}}: \forall f \in U,\; [\text{Layer}(f) = \text{Domain}] \implies \forall d \in \text{Imports}(f)\; [\text{Layer}(d) \notin \{\text{Infra}, \text{Pres}\}]$$

$$\text{Inv}_{\text{Pres}}: \forall f \in U,\; [\text{Layer}(f) = \text{Pres}] \implies \forall d \in \text{Imports}(f)\; [\text{Layer}(d) \neq \text{Infra}]$$

An **architecture violation** is a formal **counterexample** that falsifies the predicate:

$$\exists f \in \text{Domain},\; \exists d \in \text{Imports}(f): \text{Layer}(d) = \text{Infra} \implies \texttt{[arch-leak]}$$

---

### `/catlazy4-interface` — UI State Completeness Audit

**DISMATH Ch. 01 (Propositional Logic), Ch. 02 (Logical Equivalences)**

UI states are modeled as propositions. For each interactive control, the audit checks that all required state propositions are satisfied:

$$\text{Button}(B) \implies (\text{hasLoading}(B) \land \text{hasDisabled}(B) \land \text{hasAriaLabel}(B))$$

A UI finding ($\texttt{[ui-silent]}$, $\texttt{[ui-contrast]}$) is a **falsified propositional constraint** — the conjunction fails for some component.

---

### `/catlazy5-experience` — UX Flow Audit

**DISMATH Ch. 01 (Propositional Logic), Ch. 02 (Logical Equivalences)**

UX interactions are validated as propositional state completeness rules:

$$\text{AsyncAction}(A) \implies (\text{hasSkeleton}(A) \lor \text{hasSpinner}(A)) \land \text{hasEmptyState}(A) \land \text{hasErrorState}(A)$$

Any $\texttt{[ux-silent]}$ finding means a user-visible state transition is undefined — an incomplete truth table for the component's behavior.

---

### `/catlazy6-audit` — Dead Code & Duplication Audit

**DISMATH Ch. 09 (Boolean Minimization), Ch. 10 (SAT Reachability)**

Dead code detection uses **SAT reachability**: if a code path $P$ cannot be reached by any satisfying assignment of program inputs, it is unreachable and safe to delete:

$$\nexists\, \vec{x}: \text{Reach}(P, \vec{x}) \equiv \mathbf{T} \implies P \text{ is dead code}$$

Duplication is reduced using **Boolean Absorption** (Ch. 09):

$$A \lor (A \land B) \equiv A \quad \text{(absorb redundant condition)}$$

---

### `/catlazy7-debt` — Technical Debt Ledger

**DISMATH Ch. 07 (Mathematical Induction), Ch. 06 (Vacuous Proof), Ch. 08 (Deferred Hoare)**

Each `catlazy:` marker defines an **inductively bounded state** with a trigger condition:

```text
catlazy: <simplification> | ceiling: <limit> | upgrade: <trigger>
```

- **Base Case $C_0$:** Simplification holds while $x \le C_0$.
- **Inductive Step:** When $x > C_k$, the `upgrade:` trigger fires, escalating to the full implementation.
- **Vacuous Safety:** If $x \le C_0$ is guaranteed for the system's entire lifecycle, the deferral is **vacuously safe** ($P \to Q \equiv \mathbf{T}$ when $P$ is always false).

---

### `/catlazy8-agent` — Agent Rules SAT Audit

**DISMATH Ch. 01–02 (SAT Consistency), Ch. 05 (Entailment)**

The agent rule file (`.rules/AGENTS.md`) is audited for logical consistency:

$$\text{Requirement: } \varphi_{\text{rules}} \not\equiv \mathbf{F} \quad \text{(rules must be satisfiable)}$$

If two rules $R_1$ and $R_2$ entail a contradiction ($R_1 \land R_2 \equiv \mathbf{F}$), the conflicting pair is flagged as `[rule-conflict]`. Redundant rules where $R_1 \vdash R_2$ (R2 is entailed by R1) are flagged as `[rule-redundant]`.

---

### `/catlazy9-tree` — Architecture Tree Scanner

**DISMATH Ch. 03 (Predicate Logic — Classification)**

Each directory is classified by applying the predicate function $\text{Layer}: U \to L$:

$$\forall d \in \text{Dirs}:\; \text{Layer}(d) \in \{\text{Domain}, \text{Application}, \text{Infra}, \text{Presentation}, \text{Shared}, \text{Config}\}$$

Directories that cannot be classified are flagged as `[unclassified]` — a gap in the predicate's domain.

---

### `/catlazy10-loop` — Continuous Loop with Termination Proof

**DISMATH Ch. 07 (Mathematical Induction & Well-Ordering)**

The continuous loop is formally guaranteed to terminate via a **Well-Ordering Loop Variant**:

$$V(i) = \text{TargetCounter} - \text{CurrentCounter},\quad V(i) \in \mathbb{N}$$

- $V(0) = \text{TargetCounter} > 0$
- On each clean (no-findings) iteration: $V(i+1) = V(i) - 1 \quad (\text{strictly decreasing})$
- On each findings iteration: $\text{CurrentCounter} \leftarrow 0,\; V$ resets (reset is permitted by the variant — only net progress increments it)
- **By the Well-Ordering Property of** $\mathbb{N}$: $V(i)$ must reach 0 in finite steps

The loop also maintains the **Hoare Loop Invariant** (Ch. 08):

$$\{I:\; \text{TaskInvariantsSatisfied} \land 0 \le \text{CurrentCounter} \le \text{TargetCounter}\}$$

---

### `/catlazy11-flow` — End-to-End Flow Tracing & Formal Verification

**DISMATH Ch. 01, 03–05, 07, 08, 10 (Multi-chapter Synthesis)**

This skill proves that an execution flow is logically sound and vulnerability-free by applying six formal methods simultaneously. The core guarantee: every step's Post-condition entails the next step's Pre-condition — **logic does not stumble**.

**Hoare Chain Composition (Ch. 08):**

$$\frac{\{P_1\}\, S_1\, \{Q_1\} \;\land\; \{Q_1\}\, S_2\, \{Q_2\}}{\{P_1\}\, S_1; S_2\, \{Q_2\}} \quad \text{valid iff } Q_i \implies P_{i+1} \text{ for all } i$$

A broken link $Q_i \not\implies P_{i+1}$ is a `[flow-gap]` or `[flow-hoare-mismatch]` finding.

**Trust Guard Predicates (Ch. 03–04):**

$$\forall r \in \text{Routes}:\; \neg\text{HasAuthGuard}(r) \implies \texttt{[flow-vuln-auth]}$$

**Branch Completeness (Ch. 01–02):** All conditional outcomes (success, validation-error, auth-failure, not-found, server-error) must be handled. Missing cases are `[flow-branch-incomplete]`.

**Loop Termination (Ch. 07):** Retry/polling flows require a Well-Ordering Variant $V(i) \in \mathbb{N}$. Absence is `[flow-loop-unbounded]`.

**SAT Reachability (Ch. 10):** $\nexists \vec{x}: \text{Reach}(\text{State}, \vec{x}) \equiv \mathbf{T}$ identifies dead paths as `[flow-unreachable]`.

---

## 🏗️ Project Structure

```text
├── .rules/              # Agent operating rules & guardrails
│   └── AGENTS.md        # Canonical operating instructions (SAT-consistent, Ch.01)
├── docs/
│   ├── architecture/    # Clean Architecture + Reusable-First (predicate invariants, Ch.03–04)
│   ├── design/          # UI tokens + UX interaction rules (propositional, Ch.01–02)
│   ├── logics/dismath/  # DISMATH formal reasoning (Ch.01–10 + integration bridge Ch.11)
│   └── plans/           # Hoare-Triple implementation plans {P} S {Q} (Ch.08)
├── skills/              # Catlazy SDLC skills (0–11)
│   ├── catlazy/         # Intensity configuration & cross-platform embed
│   ├── catlazy0-help/   # Reference guide
│   ├── catlazy1-design/ # YAGNI gate + Hoare planning (Ch.05,06,08)
│   ├── catlazy2-review/ # Resolution refutation diff review (Ch.05,06,08,10)
│   ├── catlazy3-architecture/ # Predicate layer invariant audit (Ch.03,04)
│   ├── catlazy4-interface/    # Propositional UI state audit (Ch.01,02)
│   ├── catlazy5-experience/   # UX state completeness audit (Ch.01,02)
│   ├── catlazy6-audit/        # SAT reachability + Boolean minimization (Ch.09,10)
│   ├── catlazy7-debt/         # Inductive debt bounds + vacuous safety (Ch.06,07,08)
│   ├── catlazy8-agent/        # Rule SAT consistency + entailment (Ch.01,02,05)
│   ├── catlazy9-tree/         # Predicate layer classification (Ch.03)
│   ├── catlazy10-loop/        # Well-Ordering termination loop (Ch.07,08)
│   └── catlazy11-flow/        # E2E flow trace + vulnerability detection (Ch.01,03-05,07,08,10)
└── plugin.json          # Plugin manifest for host AI environments
```

---

## 🎚️ Operating Modes & Intensity

| Mode | Behavior |
|---|---|
| **`lite`** | Review final diff; report missing checks. |
| **`full`** *(Default)* | Approved write scopes, validation evidence, freshness tracking, finish contracts. |
| **`ultra`** | Full + hollow implementation detection (vacuous proofs, fake returns, TODO stubs) and negative-path validation for critical logic. |
| **`off`** | Disable extra workflows; preserve core safety boundaries. |

---

## 🌐 Cross-Platform Embedding (`/catlazy --embed`)

```text
/catlazy --embed
```

Injects the standard Catlazy guardrail snippet into all AI host environments:

| Platform | Target File |
|---|---|
| **Google Antigravity** | `.rules/AGENTS.md` |
| **Anthropic Claude** | `CLAUDE.md` |
| **Cursor IDE** | `.cursorrules` & `.cursor/rules/catlazy.mdc` |
| **Windsurf (Cascade)** | `.windsurfrules` |
| **GitHub Copilot** | `.github/copilot-instructions.md` |
| **OpenAI Codex** | `AGENTS.md` |

---

## 📋 Universal 3-Section Output Format

```markdown
### 🔎 Inspection Summary
- **Target / Scope:** Mode, baseline, and file scope.
- **Standards Source:** docs/ or bundled fallback.
- **Observation:** Concise factual findings.

### 📋 Inspection Checklist
- `[PASS]` / `[FAIL]` / `[N/A]` `[tag]` Description
  - **Target:** `file:line`
  - **Evidence:** Observed behavior
  - **Smallest Fix:** Minimal non-overengineered remediation

### 🐈 Catlazy Finish Check
- **Scope & Safety:** [PASS]
- **Validation & Freshness:** [PASS]
- **Diff & Side-effects:** [PASS]
- **Terminal Status:** `CATLAZY_DONE` | `CATLAZY_BLOCKED: <reason>` | `CATLAZY_UNVERIFIED: <check>`
```

---

## 💡 Practical Workflow Example

```text
1. /catlazy1-design "Add JWT authentication"
   → YAGNI check:  ¬IsNeeded today? → stop (Modus Tollens)
   → YAGNI passes: Proof by contradiction: ¬JWT → auth impossible
   → Plan saved:   docs/plans/2026-01-01-jwt-auth.md  {P} S {Q}

2. Implement within approved scope
   → Write code in src/domain/, src/application/, src/shared/ only

3. /catlazy2-review report
   → Resolution refutation:  Σ ∪ {¬Q} ⊢ □ → diff is sound
   → Fallacy guard:  no affirming-the-consequent reasoning
   → Invariants: ∀f∈Domain, Imports(f) ∩ Infra = ∅ ✓

4. /catlazy3-architecture
   → Predicate scan: no arch-leak counterexample found
   → CATLAZY_DONE 🐈💤
```

---

## 🚀 Installation & Quick Start

```bash
# Clone into Antigravity plugin directory
git clone https://github.com/Lynnn01/CATLAZY.git ~/.gemini/config/plugins/CATLAZY
```

Then in your AI chat session:
```text
/catlazy0-help    → View all commands and operating rules
/catlazy          → Confirm current operating mode
/catlazy --embed  → Inject rules into your project files
```

---

<div align="center">
  <p><i>Write less. Prove more. Reason formally. 🐈💤</i></p>
</div>
