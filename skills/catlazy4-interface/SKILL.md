---
name: catlazy4-interface
description: Audit the codebase against docs/design/user_interface/
---
# Catlazy Interface Audit

When invoked with `/catlazy4-interface`, inspect all UI and frontend code against **`docs/design/user_interface/`**.

### ⚙️ Core Rules

1. **Pre-audit UI Tree:** before inspecting styling details, run or simulate `/catlazy9-tree report --scope <ui-path> --depth 3 --format normal` (e.g. `src/presentation/`, `components/`, `ui/`, `styles/`) to map atomic UI components, design tokens, and layout hierarchy.
2. **Do not edit immediately (critical):** scan the UI and present findings first. Wait for user approval or a selected fix before editing.
3. Use these tags:
   - `[ui-color]`: raw hex colors or colors that conflict with the defined design tokens.
   - `[ui-layout]`: fixed dimensions that break responsive behavior or cause horizontal scrolling.
   - `[ui-a11y]`: contrast below 4.5:1, missing `alt`, removed focus rings, or another accessibility failure.
   - `[ui-motion]`: animation longer than 300ms, purposeless motion, or no `prefers-reduced-motion` support.
   - `[ui-spacing]`: cramped layout or spacing that violates the project grid.

### Standards Resolution

Resolve `docs/design/user_interface/` in this order before auditing:

1. Use the target repository’s `docs/design/user_interface/` when it exists.
2. Otherwise, use the canonical `docs/design/user_interface/` directory in the installed Catlazy bundle, beside its `skills/` directory.
3. Do not fall back to generic UI advice while the bundled standard is available.
4. State whether project or bundled standards were used in the Inspection Summary.

### Task Context

Accept standardized input arguments:
```text
catlazy4-interface [report|fix-safe] [--scope ui|backend|api|docs|full]
                   [--base <commit-or-ref>] [--files <path,...>]
                   [--format normal|strict] [--language <code>]
```
Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. Show the resolved files before inspection. Do not inspect unrelated dirty worktree files.

If the user approves fixes, treat the approved `files` as the write scope, stop before expanding it, and compare the final task diff with `base`. Run affected validation after the last edit and apply the Catlazy Finish Contract from the target or bundled `.rules/AGENTS.md`.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Do not output conversational text before `### 🔎 Inspection Summary`. Respond in the user’s language unless another language is requested.

### 🔎 Inspection Summary

- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`docs/design/user_interface/`) or bundled fallback standards were used.
- **Observation:** concise UI analysis with file-based evidence across `[ui-color]`, `[ui-layout]`, `[ui-a11y]`, `[ui-motion]`, and `[ui-spacing]`.

### 📋 Inspection Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-color]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-layout]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-a11y]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-motion]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-spacing]` ...

If any item is `[FAIL]`, list details:
- **Target:** `[file:line]`
- **Tag & Rule:** `[ui-*]` (citing the relevant design-token or layout rule)
- **Evidence:** reason and observed styling violation
- **Smallest Fix:** smallest recommended style or component fix

### 🐈 Catlazy Finish Check

- **Scope & Safety:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Validation & Freshness:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Diff & Side-effects:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Verdict:** If everything passes, output **“Premium UI. The interface follows `docs/design/user_interface/`.”**
- **Status:** Conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.
