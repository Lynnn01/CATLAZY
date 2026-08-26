# Implementation Plan: Integrate `/catlazy9-tree` Pre-audit across 6 Catlazy Skills

**Date:** 2026-08-26
**Status:** APPROVED & EXECUTED

## 1. Goal & Pre-condition {P}

- **Pre-condition {P}:** Catlazy skills (`catlazy2-review`, `catlazy3-architecture`, `catlazy4-interface`, `catlazy5-experience`, `catlazy6-audit`, `catlazy8-agent`) currently perform inspections directly on code files without an explicit preliminary directory mapping step.
- **Goal:** Integrate `/catlazy9-tree` as an explicit preliminary discovery step across all 6 skills, with tailored `scope`, `depth`, and `format` parameters for each skill domain.
- **Affected Files:**
  - `skills/catlazy2-review/SKILL.md` [MODIFY]
  - `skills/catlazy3-architecture/SKILL.md` [MODIFY]
  - `skills/catlazy4-interface/SKILL.md` [MODIFY]
  - `skills/catlazy5-experience/SKILL.md` [MODIFY]
  - `skills/catlazy6-audit/SKILL.md` [MODIFY]
  - `skills/catlazy8-agent/SKILL.md` [MODIFY]
  - `docs/plans/2026-08-26-integrate-catlazy9-tree-across-skills.md` [NEW]

---

## 2. Proposed Changes & Statement {S}

### Parameter Tailoring Matrix

| Skill | SDLC | Domain | `--scope` | `--depth` | `--format` | Purpose |
| :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| `catlazy2-review` | 2 | Git Diff | `<changed-dir>` | `2` | `normal` | Localized module context |
| `catlazy3-architecture` | 3 | Architecture | `.` | `4` | `strict` | 4-layer & shared structure mapping |
| `catlazy4-interface` | 4 | UI Tokens | `src/presentation/`, `components/` | `3` | `normal` | UI components & assets hierarchy |
| `catlazy5-experience` | 5 | UX Flows | `pages/`, `views/`, `routes/` | `3` | `normal` | User journey & screen coverage |
| `catlazy6-audit` | 6 | Repo Audit | `.` | `5` | `strict` | Deep search for empty/dead folders |
| `catlazy8-agent` | 8 | Rules | `.rules/`, `skills/`, `.cursor/` | `2` | `normal` | Governance & config directory scan |

### Core Modifications:
Inject the designated `/catlazy9-tree` pre-audit step into the `### ⚙️ Core Rules` or `### Review Scope` of each skill.

---

## 3. Post-condition {Q} & Verification Plan

- **Post-condition {Q}:** All 6 skill definitions explicitly incorporate `/catlazy9-tree` pre-auditing and pass formal verification with exit code 0.

### Verification Commands:
```bash
python tools/run_formal_engine.py --all
```

**Rollback:** Revert modifications in `skills/` and resync with host plugins directory.
