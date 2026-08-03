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

### Standards Resolution

Resolve `docs/design/user_experience/` in this order before auditing:

1. Use the target repository’s `docs/design/user_experience/` when it exists.
2. Otherwise, use the canonical `docs/design/user_experience/` directory in the installed Catlazy bundle, beside its `skills/` directory.
3. Do not fall back to generic UX or product principles while the bundled standard is available.
4. State whether project or bundled standards were used in the Inspection Summary.

### Task Context

Accept `--base <commit-or-ref>` and `--files <path,...>` to isolate the current task. Resolve explicit arguments first, then optional `.catlazy/task.json`, then user-named files. Show the resolved files before inspection. Do not inspect unrelated dirty worktree files.

If the user approves fixes, treat the approved `files` as the write scope, stop before expanding it, and compare the final task diff with `base`. Run affected validation after the last edit and apply the Catlazy Finish Contract from the target or bundled `.rules/AGENTS.md`. A read-only audit keeps the audit format and does not claim implementation completion.

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
