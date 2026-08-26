---
name: catlazy6-audit
description: Audit the repository for over-engineering and deletion candidates
---
# Catlazy Repository Audit

Inspect the entire repository for dead code, duplication, unnecessary dependencies, stale configuration, and abstractions that do not protect a real boundary.

### ⚙️ Core Rules

1. **Pre-audit Full Repository Tree:** before inspecting code, run or simulate `/catlazy9-tree report --scope . --depth 5 --format strict` to scan the full directory tree for `[tree-empty-dir]`, `[tree-deep-nesting]`, dead folders, and duplicate utility directories.
2. Read repository rules and the relevant architecture/design docs first.
3. Search all references before recommending deletion or renaming.
4. Do not edit immediately; present findings and wait for approval.
5. Never recommend deleting security, accessibility, data-loss handling, tests, or required architecture layers merely to reduce line count.
6. Classify findings as deletion, consolidation into central `shared/` modules, reuse, dependency removal, or intentional complexity.

### Task Context and Approved Changes

Accept standardized input arguments:
```text
catlazy6-audit [report|fix-safe] [--scope ui|backend|api|docs|full]
               [--base <commit-or-ref>] [--files <path,...>]
               [--format normal|strict] [--language <code>]
```
Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. A repository-wide read does not authorize repository-wide writes. If the user approves cleanup, treat the approved files as the write scope, stop before expanding it, validate after the last edit, review the final diff against the baseline, and apply the Catlazy Finish Contract.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user's language.

### 🔎 Inspection Summary

- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`docs/`) or bundled fallback standards were used.
- **Observation:** concise repository analysis and over-engineering audit evidence.

### 📋 Inspection Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[audit-deadcode]` (Dead code)
- `[PASS]` / `[FAIL]` / `[N/A]` `[audit-duplication]` (Duplication)
- `[PASS]` / `[FAIL]` / `[N/A]` `[audit-deps]` (Unnecessary dependencies)
- `[PASS]` / `[FAIL]` / `[N/A]` `[audit-config]` (Stale configuration)
- `[PASS]` / `[FAIL]` / `[N/A]` `[audit-arch]` (Over-engineered abstractions)
- `[PASS]` / `[FAIL]` / `[N/A]` `[audit-risk]` (Complexity risk)

If any item is `[FAIL]`, list details:
- **Target:** `[file:line]` or `[component/layer]`
- **Tag & Rule:** `[audit-*]` (citing over-engineering rule)
- **Evidence:** explain why it fails and provide evidence
- **Smallest Fix:** propose the smallest safe deletion or consolidation action

### 🐈 Catlazy Finish Check

- **Scope & Safety:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Validation & Freshness:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Diff & Side-effects:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Verdict:** If everything passes, output **“Repository is lean. No over-engineering detected.”**
- **Status:** Conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.
