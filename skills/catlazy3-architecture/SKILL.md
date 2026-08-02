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
