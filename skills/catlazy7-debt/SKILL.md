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

### 📐 Formal Basis (DISMATH Reasoning Foundation)

Technical debt tracking is formally grounded in:
- **Ch. 08 (Hoare Triples on Deferred State):** A debt marker represents $\{P: \text{input} \le \text{ceiling}\} \, S_{\text{simplified}} \, \{Q\}$. When $\text{input} > \text{ceiling}$, the post-condition $\{Q\}$ is no longer guaranteed, triggering the $\{S_{\text{upgrade}}\}$ statement. Reference: [`docs/logics/dismath/08-program-correctness-and-hoare-logic.md`](../../docs/logics/dismath/08-program-correctness-and-hoare-logic.md).
- **Ch. 06 (Vacuous Proof for Infinite Deferrals):** If the operational boundary guarantees that $\text{input} \le \text{ceiling}$ is invariant for the entire system lifecycle, paying down the debt is vacuously unnecessary ($P \to Q \equiv \mathbf{T}$). Reference: [`docs/logics/dismath/06-methods-of-proof.md`](../../docs/logics/dismath/06-methods-of-proof.md).

### Task Context and Approved Changes

Accept standardized input arguments:
```text
catlazy7-debt [report|fix-safe] [--scope ui|backend|api|docs|full]
              [--base <commit-or-ref>] [--files <path,...>]
              [--format normal|strict] [--language <code>]
```
Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. If the user approves ledger or marker edits, show the approved files, treat them as the write scope, and stop before expanding it. Validate after the last edit, inspect the final diff against the task baseline, and apply the Catlazy Finish Contract.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user's language.

### 🔎 Inspection Summary

- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`docs/`) or bundled fallback standards were used.
- **Observation:** concise summary of debt marker scan.

### 📋 Inspection Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[debt-scan]` (Scan for `catlazy:` markers)

If debt markers exist, report each one:
- **Target:** `[file:line]`
- **Tag & Rule:** `[catlazy-marker]`
- **Simplification:** `<simplification>`
- **Ceiling:** `<current limit>`
- **Upgrade:** `<trigger to revisit>`

### 🐈 Catlazy Finish Check

- **Scope & Safety:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Validation & Freshness:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Diff & Side-effects:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Verdict:** If everything passes, output **“Debt ledger is up to date.”**
- **Status:** Conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.
