---
name: catlazy5-experience
description: Audit the codebase against docs/design/user_experience/
---
# Catlazy Experience Audit

When invoked with `/catlazy5-experience`, inspect UI/frontend flows against **`docs/design/user_experience/`**.

### ⚙️ Core Rules

1. **Do not edit immediately (critical):** scan the flow and present findings first. Wait for user approval or a selected fix before editing.
2. Use these tags:
   - `[ux-clutter]`: excessive information density that violates progressive disclosure.
   - `[ux-silent]`: missing hover/active/disabled feedback, loading state, success/error notification, or other response to an action.
   - `[ux-empty]`: no contextual empty state when a list or screen has no data.
   - `[ux-inconsistent]`: action placement or terminology conflicts with the rest of the product and violates familiar or internal consistency.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Do not output conversational text before `### 🔎 Inspection Summary`. Respond in the user’s language unless another language is requested.

### 🔎 Inspection Summary

- Analyze the UX flow with concise file and state evidence.
- Check `[ux-clutter]`, `[ux-silent]`, `[ux-empty]`, and `[ux-inconsistent]`.

### 📋 Audit Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-clutter]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-silent]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-empty]` ...
- `[PASS]` / `[FAIL]` / `[N/A]` `[ux-inconsistent]` ...

For each failure, include the file, reason, violated rule, and the smallest UX recommendation, such as a skeleton, empty state, or retry path. Always output both required sections, even when the UX is perfect.

If everything passes, end with: **“Seamless Experience. The UX follows `docs/design/user_experience/`.”**
