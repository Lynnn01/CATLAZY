---
name: catlazy6-audit
description: Audit the repository for over-engineering and deletion candidates
---
# Catlazy Repository Audit

Inspect the entire repository for dead code, duplication, unnecessary dependencies, stale configuration, and abstractions that do not protect a real boundary.

### ⚙️ Core Rules

1. Read repository rules and the relevant architecture/design docs first.
2. Search all references before recommending deletion or renaming.
3. Do not edit immediately; present findings and wait for approval.
4. Never recommend deleting security, accessibility, data-loss handling, tests, or required architecture layers merely to reduce line count.
5. Classify findings as deletion, consolidation, reuse, dependency removal, or intentional complexity.

### Task Context and Approved Changes

Accept `--base <commit-or-ref>` and `--files <path,...>`. Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. A repository-wide read does not authorize repository-wide writes. If the user approves cleanup, treat the approved files as the write scope, stop before expanding it, validate after the last edit, review the final diff against the baseline, and apply the Catlazy Finish Contract. A read-only audit does not claim implementation completion.

### 🚨 STRICT OUTPUT FORMAT

Start with `### 🔎 Inspection Summary`, then show `### 📋 Audit Checklist` with `[PASS]`, `[FAIL]`, or `[N/A]` for dead code, duplication, dependencies, configuration, architecture, and risk. For every failure include file, evidence, impact, and the smallest safe action. Always show both sections and respond in the user’s language.
