# Implementation Plan: New Skill `catlazy9-tree` (Project Directory Map & Purpose Explainer)

**Date:** 2026-08-26
**Status:** APPROVED & EXECUTED

## 1. Goal & Pre-condition {P}

- **Pre-condition {P}:** The Catlazy skill catalog has skills 0–8 and 10, with slot 9 available. Developers/agents need a dedicated skill to scan and report the project directory tree with functional/architectural purpose descriptions for each folder.
- **Affected Files:**
  - `skills/catlazy9-tree/SKILL.md` [NEW]
  - `skills/catlazy0-help/SKILL.md` [MODIFY]
  - `README.md` [MODIFY]
  - `docs/plans/2026-08-26-catlazy9-tree-skill.md` [NEW]

---

## 2. Proposed Changes & Statement {S}

### Component: Catlazy Skills (`skills/`)

#### [NEW] `skills/catlazy9-tree/SKILL.md`
- Scans directories recursively (ignoring `.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`).
- Outputs visual ASCII tree.
- Annotates each directory with Purpose / Description and Architectural Layer (Domain, Application, Infrastructure, Presentation, Shared, Config, Docs, Tools).
- Detects directory health issues (empty directories, excessive nesting > 5 levels, improper layer placement).

#### [MODIFY] `skills/catlazy0-help/SKILL.md`
- Add `/catlazy9-tree` entry to the quick reference table.

#### [MODIFY] `README.md`
- Add `/catlazy9-tree` to the SDLC workflow commands table.

---

## 3. Post-condition {Q} & Verification Plan

- **Post-condition {Q}:**
  - `/catlazy9-tree` is fully registered in `skills/catlazy9-tree/SKILL.md`.
  - All formal verification checks (`python tools/run_formal_engine.py --all`) pass with exit code 0.

### Verification Commands:
```bash
python tools/run_formal_engine.py --all
```

**Rollback:** Delete `skills/catlazy9-tree/` and revert edits to `skills/catlazy0-help/SKILL.md` and `README.md`.
