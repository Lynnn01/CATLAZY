---
name: catlazy3-architecture
description: Audit the codebase against docs/architecture/
---
# Catlazy Architecture Audit

When invoked with `/catlazy3-architecture`, inspect the entire repository and compare its structure and code against **`docs/architecture/`**, with emphasis on Clean Architecture and Domain-Driven Design (DDD).

### ⚙️ Core Rules

1. **Do not edit immediately (critical):** scan the repository and present findings first. Wait for the user to approve the findings or select fixes before editing files.
2. Order findings from the most severe architectural risk to the least severe.
3. Use the following tags:
   - `[arch-leak]`: framework, database, or infrastructure code leaks into the Domain layer.
   - `[arch-bypass]`: Presentation calls infrastructure or a database directly instead of going through the Application layer.
   - `[arch-anemic]`: a Domain entity has only getters/setters and no meaningful business behavior.
   - `[arch-coupling]`: modules are too tightly coupled and should communicate through ports or explicit contracts.

### Standards Resolution

Resolve `docs/architecture/` in this order before auditing:

1. Use the target repository’s `docs/architecture/` when it exists.
2. Otherwise, use the canonical `docs/architecture/` directory in the installed Catlazy bundle, beside its `skills/` directory.
3. Do not fall back to generic Clean Architecture advice while the bundled standard is available.
4. State whether project or bundled standards were used in the Inspection Summary.

### Task Context

Accept `--scope ui|backend|api|full`, `--base <commit-or-ref>`, and `--files <path,...>`. Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. Show the resolved candidate files before a broad audit. For `ui` scope, mark backend-only architecture checks as not applicable unless the selected UI files cross a boundary.

If the user approves fixes, treat the approved `files` as the write scope, stop before expanding it, and compare the final task diff with `base`. Run affected validation after the last edit and apply the Catlazy Finish Contract from the target or bundled `.rules/AGENTS.md`. A read-only audit keeps the audit format and does not claim implementation completion.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user’s language unless the user requests another language.

### 🔎 Inspection Summary

- Analyze the relevant files and architecture with concise evidence.
- Check `[arch-leak]`, `[arch-bypass]`, `[arch-anemic]`, and `[arch-coupling]`.

### 📋 Audit Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[arch-leak]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[arch-bypass]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[arch-anemic]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[arch-coupling]` ...

If any item is `[FAIL]`, list details:

- **[Tag] `[file/path]`**
  - **Reason:** explain the architectural violation and cite the relevant rule.
  - **Recommendation:** propose the smallest Clean Architecture fix.

Even when everything is correct, always output both required sections. Early returns are forbidden.

If everything passes, end with: **“Clean Architecture. The code follows `docs/architecture/` correctly.”**
