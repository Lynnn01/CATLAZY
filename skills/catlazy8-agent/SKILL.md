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

### 🚨 STRICT OUTPUT FORMAT

Start with `### 🔎 Inspection Summary`, then include `### 📋 Rule Update Report`. Cover duplication, contradictions, stale references, missing safeguards, and proposed changes. Always show both sections and respond in the user’s language.
