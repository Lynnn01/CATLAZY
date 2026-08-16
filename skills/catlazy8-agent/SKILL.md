---
name: catlazy8-agent
description: Review and simplify the project agent rules
---
# Catlazy Agent Update

Review `.rules/AGENTS.md` and related project rules for duplication, contradictions, stale instructions, and unnecessary complexity.

### ⚙️ Workflow

1. Read the current rules and identify the smallest set of authoritative instructions.
2. Search the repository for rules that reference the same behavior and check for conflicts.
3. Report proposed simplifications first; do not edit without user approval.
4. When approved, update the rule files, preserve safety/security/accessibility requirements, and verify every referenced path.
5. Record what changed and run a final consistency check.

For approved updates, show the rule files, treat them as the write scope, and stop before expanding it. Validate after the last edit, inspect the final diff against the task baseline, and apply the Catlazy Finish Contract. A report-only run keeps the rule-update format and does not claim implementation completion.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user's language.

### 🔎 Inspection Summary

- Analyze the rule files for duplication, contradictions, and stale instructions.

### 📋 Rule Update Report

- `[PASS]` / `[FAIL]` / `[N/A]` Duplication
- `[PASS]` / `[FAIL]` / `[N/A]` Contradictions
- `[PASS]` / `[FAIL]` / `[N/A]` Stale references
- `[PASS]` / `[FAIL]` / `[N/A]` Missing safeguards

If any item is `[FAIL]`, detail the proposed changes. Always show both sections.
