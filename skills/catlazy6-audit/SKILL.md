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

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user's language.

### 🔎 Inspection Summary

- Analyze the repository state with concise evidence.

### 📋 Audit Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` Dead code
- `[PASS]` / `[FAIL]` / `[N/A]` Duplication
- `[PASS]` / `[FAIL]` / `[N/A]` Dependencies
- `[PASS]` / `[FAIL]` / `[N/A]` Configuration
- `[PASS]` / `[FAIL]` / `[N/A]` Architecture
- `[PASS]` / `[FAIL]` / `[N/A]` Risk

If any item is `[FAIL]`, list details:
- **File:** `[file/path]`
- **Evidence:** explain why it fails.
- **Impact:** explain the negative impact.
- **Action:** propose the smallest safe action.

Even when everything is correct, always output both required sections.
