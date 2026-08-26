---
name: catlazy8-agent
description: Review and simplify the project agent rules
---
# Catlazy Agent Update

Review `.rules/AGENTS.md` and related project rules for duplication, contradictions, stale instructions, and unnecessary complexity.

### ⚙️ Workflow

1. **Pre-audit Governance Tree:** before modifying rules, run or simulate `/catlazy9-tree report --scope .rules/ --depth 2 --format normal` (along with `skills/`, `.cursor/`, `.github/`) to map all rule governance and configuration locations.
2. Read the current rules and identify the smallest set of authoritative instructions.
3. Search the repository for rules that reference the same behavior and check for conflicts.
4. Report proposed simplifications first; do not edit without user approval.
5. When approved, update the rule files, preserve safety/security/accessibility requirements, and verify every referenced path.
6. Record what changed and run a final consistency check.

### Task Context and Approved Changes

Accept standardized input arguments:
```text
catlazy8-agent [report|fix-safe] [--scope ui|backend|api|docs|full]
               [--base <commit-or-ref>] [--files <path,...>]
               [--format normal|strict] [--language <code>]
```
Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. For approved updates, show the rule files, treat them as the write scope, and stop before expanding it. Validate after the last edit, inspect the final diff against the task baseline, and apply the Catlazy Finish Contract.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user's language.

### 🔎 Inspection Summary

- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`.rules/`) or bundled fallback standards were used.
- **Observation:** concise agent rules analysis and evidence across duplication, contradictions, and stale instructions.

### 📋 Inspection Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[rule-duplication]` (Duplication)
- `[PASS]` / `[FAIL]` / `[N/A]` `[rule-conflict]` (Contradictions)
- `[PASS]` / `[FAIL]` / `[N/A]` `[rule-stale]` (Stale references)
- `[PASS]` / `[FAIL]` / `[N/A]` `[rule-safeguard]` (Missing safeguards)

If any item is `[FAIL]`, list details:
- **Target:** `[file:line]`
- **Tag & Rule:** `[rule-*]`
- **Evidence:** explain the contradiction or stale instruction
- **Smallest Fix:** proposed minimal rule simplification

### 🐈 Catlazy Finish Check

- **Scope & Safety:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Validation & Freshness:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Diff & Side-effects:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Verdict:** If everything passes, output **“Rules are concise and consistent.”**
- **Status:** Conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.
