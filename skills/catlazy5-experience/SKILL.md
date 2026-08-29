---
name: catlazy5-experience
description: Audit the codebase against docs/design/user_experience/
---
# Catlazy Experience Audit

When invoked with `/catlazy5-experience`, inspect UI/frontend flows against **`docs/design/user_experience/`**.

### ⚙️ Core Rules

1. **Pre-audit UX Flow Tree:** before inspecting UX interactions, run or simulate `/catlazy9-tree report --scope <routes-or-pages-path> --depth 3 --format normal` (e.g. `pages/`, `views/`, `routes/`, `features/`) to map user journeys, page hierarchies, and navigation paths.
2. **Do not edit immediately (critical):** scan the flow and present findings first. Wait for user approval or a selected fix before editing.
3. Use these tags:
   - `[ux-clutter]`: excessive information density that violates progressive disclosure.
   - `[ux-silent]`: missing hover/active/disabled feedback, loading state, success/error notification, or other response to an action.
   - `[ux-empty]`: no contextual empty state when a list or screen has no data.
   - `[ux-inconsistent]`: action placement or terminology conflicts with the rest of the product and violates familiar or internal consistency.

### 📐 Formal Basis (DISMATH Reasoning Foundation)

User experience state auditing is mathematically grounded in:
- **Ch. 01–02 (Propositional State Completeness & Invariants):** Every interactive control must satisfy the completeness proposition: $\forall \text{Action}, \text{State}_{\text{loading}} \lor \text{State}_{\text{feedback}} \lor \text{State}_{\text{error}} \not\equiv \mathbf{F}$. If an action transitions to a silent state ($\neg \text{Feedback} \land \neg \text{Loading}$), it triggers $[ux\text{-}silent]$. Reference: [`docs/logics/dismath/01-propositional-logic.md`](../../docs/logics/dismath/01-propositional-logic.md), [`02-logical-equivalences.md`](../../docs/logics/dismath/02-logical-equivalences.md).

### Standards Resolution

Resolve `docs/design/user_experience/` in this order before auditing:

1. Use the target repository’s `docs/design/user_experience/` when it exists.
2. Otherwise, use the canonical `docs/design/user_experience/` directory in the installed Catlazy bundle, beside its `skills/` directory.
3. Do not fall back to generic UX or product principles while the bundled standard is available.
4. State whether project or bundled standards were used in the Inspection Summary.

### Task Context

Accept standardized input arguments:
```text
catlazy5-experience [report|fix-safe] [--scope ui|backend|api|docs|full]
                   [--base <commit-or-ref>] [--files <path,...>]
                   [--format normal|strict] [--language <code>]
```
Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. Show the resolved files before inspection. Do not inspect unrelated dirty worktree files.

If the user approves fixes, treat the approved `files` as the write scope, stop before expanding it, and compare the final task diff with `base`. Run affected validation after the last edit and apply the Catlazy Finish Contract from the target or bundled `.rules/AGENTS.md`.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Do not output conversational text before `### 🔎 Inspection Summary`. Respond in the user’s language unless another language is requested.

### 🔎 Inspection Summary

- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`docs/design/user_experience/`) or bundled fallback standards were used.
- **Observation:** concise UX flow analysis with file and state evidence across `[ux-clutter]`, `[ux-silent]`, `[ux-empty]`, and `[ux-inconsistent]`.

### 📋 Inspection Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-clutter]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-silent]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-empty]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-inconsistent]` ...

If any item is `[FAIL]`, list details:
- **Target:** `[file:line]`
- **Tag & Rule:** `[ux-*]` (citing the relevant user experience guideline)
- **Evidence:** reason and observed interaction failure
- **Smallest Fix:** smallest recommended UX action (e.g. skeleton, empty state, or retry path)

### 🐈 Catlazy Finish Check

- **Scope & Safety:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Validation & Freshness:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Diff & Side-effects:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Verdict:** If everything passes, output **“Seamless Experience. The UX follows `docs/design/user_experience/`.”**
- **Status:** Conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.
