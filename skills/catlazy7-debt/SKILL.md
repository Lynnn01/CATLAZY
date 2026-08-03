---
name: catlazy7-debt
description: Collect Catlazy comments into a technical-debt ledger
---
# Catlazy Debt Ledger

Scan the repository for intentional `catlazy:` comments and maintain a concise debt ledger.

### ⚙️ Workflow

1. Search all relevant source files for `catlazy:` markers.
2. Parse each marker as `catlazy: <simplification> | ceiling: <current limit> | upgrade: <trigger to revisit>`.
3. Report file, line, simplification, current ceiling, and upgrade trigger.
4. Do not edit production code while collecting debt. Ask for approval before changing or removing a marker.

If the user approves ledger or marker edits, show the approved files, treat them as the write scope, and stop before expanding it. Validate after the last edit, inspect the final diff against the task baseline, and apply the Catlazy Finish Contract. A scan-only run keeps the debt-ledger format and does not claim implementation completion.

### 🚨 STRICT OUTPUT FORMAT

Start with `### 🔎 Inspection Summary`, then include `### 📋 Debt Ledger` with `[PASS]`, `[FAIL]`, or `[N/A]` status for the scan. Always show both sections, even when no debt markers exist. Respond in the user’s language.
