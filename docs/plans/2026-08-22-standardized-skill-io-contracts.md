# Standardized Skill Input and Output Contracts

## Goal

Standardize command input parameters and response report structures across all Catlazy skills, audits, reviews, and automation loops to ensure deterministic execution, automated parsing compatibility, and uniform developer experience.

## Affected files

- `.rules/AGENTS.md`
- `docs/plans/2026-08-22-standardized-skill-io-contracts.md`
- `skills/catlazy2-review/SKILL.md`
- `skills/catlazy3-architecture/SKILL.md`
- `skills/catlazy4-interface/SKILL.md`
- `skills/catlazy5-experience/SKILL.md`
- `skills/catlazy6-audit/SKILL.md`
- `skills/catlazy7-debt/SKILL.md`
- `skills/catlazy8-agent/SKILL.md`

## Standard Input Contract

All Catlazy skills accept a standardized input argument contract:

```text
catlazy<N>-<skill> [report|fix-safe] [--scope ui|backend|api|docs|full]
                   [--base <commit-or-ref>] [--files <path,...>]
                   [--format normal|strict] [--language <code>]
```

### Precedence Order
1. Explicit command arguments.
2. Optional `.catlazy/task.json` manifest.
3. Explicit user-named files.
4. Candidate changed files (with explicit user confirmation if dirty worktree contains unrelated changes).

## Standard Output Contract (Universal 3-Section Format)

All Catlazy skills, reviews, audits, and reports MUST output using the exact 3-section structure without conversational filler before the first heading:

### 1. `### 🔎 Inspection Summary`
- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`docs/`) or bundled fallback standards were used.
- **Observation:** concise evidence and key findings summary.

### 2. `### 📋 Inspection Checklist`
- Report all items using standardized status badges: `[PASS]`, `[FAIL]`, or `[N/A]`. Every `[N/A]` must state the concrete reason.
- For any failure or finding, format details using the unified finding structure:
  - **Target:** `[file:line]` or `[component/layer]`
  - **Tag & Rule:** `[tag-name]` citing the violated guideline
  - **Evidence:** observed code or behavior evidence
  - **Smallest Fix:** smallest non-overengineered remediation

### 3. `### 🐈 Catlazy Finish Check`
- Report `[PASS]`, `[FAIL]`, or `[N/A]` for:
  - `Scope & Safety`
  - `Validation & Freshness`
  - `Diff & Side-effects`
- **Verdict:** concise one-line verdict statement.
- **Terminal Status:** conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.

## Verification

- Inspect `.rules/AGENTS.md` to confirm the rules are updated.
- Verify consistency with the Catlazy philosophy (simplicity, strict boundaries, no premature abstractions).
