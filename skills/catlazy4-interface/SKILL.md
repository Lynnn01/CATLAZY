---
name: catlazy4-interface
description: Audit the codebase against docs/design/user_interface/
---
# Catlazy Interface Audit

When invoked with `/catlazy4-interface`, inspect all UI and frontend code against **`docs/design/user_interface/`**.

### ⚙️ Core Rules

1. **Do not edit immediately (critical):** scan the UI and present findings first. Wait for user approval or a selected fix before editing.
2. Use these tags:
   - `[ui-color]`: raw hex colors or colors that conflict with the defined design tokens.
   - `[ui-layout]`: fixed dimensions that break responsive behavior or cause horizontal scrolling.
   - `[ui-a11y]`: contrast below 4.5:1, missing `alt`, removed focus rings, or another accessibility failure.
   - `[ui-motion]`: animation longer than 300ms, purposeless motion, or no `prefers-reduced-motion` support.
   - `[ui-spacing]`: cramped layout or spacing that violates the project grid.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Do not output conversational text before `### 🔎 Inspection Summary`. Respond in the user’s language unless another language is requested.

### 🔎 Inspection Summary

- Analyze the UI components with file-based evidence.
- Check `[ui-color]`, `[ui-layout]`, `[ui-a11y]`, `[ui-motion]`, and `[ui-spacing]`.

### 📋 Audit Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-color]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-layout]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-a11y]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-motion]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ui-spacing]` ...

For each failure, include the file, reason, violated rule, and the smallest recommended style or component fix. Always output both required sections, even when the UI is perfect.

If everything passes, end with: **“Premium UI. The interface follows `docs/design/user_interface/`.”**
