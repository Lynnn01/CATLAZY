# 11. Catlazy Formal Methods — DISMATH Applied to Catlazy

This document maps each chapter of the DISMATH curriculum to its concrete implementation in the **Catlazy Formal Engine** (`tools/formal/`).

---

## 🗺️ DISMATH → Tooling Traceability Matrix

| DISMATH Chapter | Core Theory | Catlazy Formal Engine Module |
| :---: | :--- | :--- |
| 01 | Propositional Logic | [Module 2](../../../tools/formal/02_rule_sat_consistency.py) — SAT Consistency: each rule is a proposition literal in φ |
| 02 | Logical Equivalences (De Morgan, Contradiction) | [Module 2](../../../tools/formal/02_rule_sat_consistency.py) — Contradiction pairs use De Morgan negation |
| 03 | Predicate Logic $P(x)$ & Domain of Discourse | [Module 1](../../../tools/formal/01_invariant_checker.py) — $\text{Layer}(f)$, $\text{Imports}(f)$ as propositional functions |
| 04 | Nested Quantifiers $\forall x \forall y$ | [Module 1](../../../tools/formal/01_invariant_checker.py) — $\forall f \in \text{Layer}, \forall d \in \text{Imports}(f)$ |
| 05 | Rules of Inference & Resolution Rule | [Module 4](../../../tools/formal/04_resolution_reviewer.py) — Resolution Refutation on git diff |
| 06 | Methods of Proof (Direct, Contradiction) | [Module 3](../../../tools/formal/03_hoare_plan_validator.py) — Hoare logic is a form of Direct Proof |
| 07 | Mathematical Induction & Well-Ordering | CLI Loop Termination — `run_formal_engine.py` terminates in finite module steps (Loop Variant = `|mods| - i`) |
| 08 | Program Correctness & Hoare Logic $\{P\} S \{Q\}$ | [Module 3](../../../tools/formal/03_hoare_plan_validator.py) — validates {P}S{Q} in `docs/plans/*.md` |
| 09 | Boolean Algebra & CNF/DNF | [Module 2](../../../tools/formal/02_rule_sat_consistency.py) — φ represented in CNF (conjunction of contradiction clauses) |
| 10 | SAT Problem & Resolution Refutation | [Module 2](../../../tools/formal/02_rule_sat_consistency.py) + [Module 4](../../../tools/formal/04_resolution_reviewer.py) |

---

## 🔧 Module Reference

| Module | File | Skill Integration |
| :--- | :--- | :--- |
| 1 — Architecture Invariant Checker | [`01_invariant_checker.py`](../../../tools/formal/01_invariant_checker.py) | `catlazy3-architecture` |
| 2 — Rule SAT Consistency | [`02_rule_sat_consistency.py`](../../../tools/formal/02_rule_sat_consistency.py) | `catlazy` (after `--embed`) |
| 3 — Hoare Plan Validator | [`03_hoare_plan_validator.py`](../../../tools/formal/03_hoare_plan_validator.py) | `catlazy1-design` |
| 4 — Resolution Refutation | [`04_resolution_reviewer.py`](../../../tools/formal/04_resolution_reviewer.py) | `catlazy2-review` |

**CLI:** [`tools/run_formal_engine.py`](../../../tools/run_formal_engine.py)

---

## ⚡ Quick Reference Commands

```bash
# Run all modules
python tools/run_formal_engine.py --all

# catlazy3-architecture gate
python tools/run_formal_engine.py --module 1 .

# catlazy2-review gate (before submitting diff)
python tools/run_formal_engine.py --module 4 --base main

# catlazy1-design gate (validate plan before approve)
python tools/run_formal_engine.py --module 3 docs/plans/

# catlazy embed gate (after --embed across platforms)
python tools/run_formal_engine.py --module 2

# CI/CD pre-commit
python tools/run_formal_engine.py --module 1,4
```

---

## 📐 Upgrade Path

| Module | Current (catlazy: minimal) | Upgrade Trigger |
| :--- | :--- | :--- |
| Module 1 | regex-based import scan | Add 2nd language requiring AST |
| Module 2 | pattern-pair heuristics | Rule corpus grows to 50+ items → use `python-sat` |
| Module 3 | section-header detection | Add JSON schema for machine-readable plans |
| Module 4 | Module 1 as oracle | Need formal proof chain → integrate `z3-solver` |
