---
name: catlazy0-help
description: Quick reference for Catlazy levels, skills, and commands
---

# Catlazy Quick Reference

Display the one-shot quick reference for `catlazy`.

**Important:** this command only prints information. It must not change the mode, create flag files, or persist any setting.

### 🎚️ Intensity Levels

- **`lite`:** final diff plus an honest statement of checks not run.
- **`full` (default):** approved write scope, applicable validation, last-edit freshness, and the Catlazy finish status.
- **`ultra`:** `full` plus hollow review, relevant negative-path validation, and an optional approved fault probe for critical logic.
- **`off`:** disable extra Catlazy behavior without disabling project safety rules.
- **Incremental Decision Trail:** complex work proceeds one issue at a time through Observe → Decide → Plan → Apply → Verify → Continue; small work uses Plan → Apply → Verify.

### 🐈 Finish Status

- `CATLAZY_DONE`: scope, current validation, final diff, generated files, and P1/P2 review pass.
- `CATLAZY_BLOCKED: <reason>`: an external dependency or required decision prevents completion.
- `CATLAZY_UNVERIFIED: <missing check>`: required evidence is missing, stale, unavailable, or failing.

### 🛠️ Commands

- **`/catlazy0-help`:** display this guide.
- **`/catlazy1-design`:** brainstorm before writing code for any work, including UI, UX, and bug fixes.
- **`/catlazy2-review`:** review the latest changes for over-engineering and rule violations.
- **`/catlazy3-architecture`:** check the code against Clean Architecture and Reusable-First guidance in `docs/architecture/`.
- **`/catlazy4-interface`:** check UI against the design-token rules in `docs/design/user_interface/`.
- **`/catlazy5-experience`:** check UX usability and clarity of feedback using `docs/design/user_experience/`.
- **`/catlazy6-audit`:** audit the repository for over-engineering, with emphasis on reducing unnecessary code.
- **`/catlazy7-debt`:** collect `catlazy:` comments into the debt ledger.
- **`/catlazy8-agent`:** review and update project rules into a simpler, consistent structure.
- **`/catlazy9-tree`:** scan project directory structure and report an annotated folder tree with purpose descriptions.
- **`/catlazy10-loop`:** force the agent to continuously execute a task until validated multiple times without findings.

### 🧠 Formal Logic Foundation (DISMATH)

All skills and planning are mathematically grounded in Discrete Mathematics (`docs/logics/dismath/`):
- **Planning:** Hoare Triples $\{P\} S \{Q\}$ (Ch. 08) & YAGNI Modus Tollens (Ch. 05)
- **Architecture:** Predicate Logic $\forall f, \forall d$ (Ch. 03–04) & Transitive Syllogism
- **Review & Diff:** Resolution Refutation & Proof by Contradiction (Ch. 05, 06, 10)
- **Debt & Loop:** Inductive Sequences, Well-Ordering, and Loop Variants $V(i)$ (Ch. 07)

### ⚙️ Stop and Configure

- **Stop:** type `stop catlazy`, `normal mode`, or `/catlazy off`.
- **Enable again:** type `/catlazy` at any time.
- **Default:** the initial level is `full`.
