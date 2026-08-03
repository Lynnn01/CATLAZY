---
name: catlazy1-design
description: Brainstorm before implementation — the Catlazy three-step design gate
---

# Catlazy Design (Brainstorm Before Code)

Use this skill before every type of work, including frontend, backend, UI/UX, and bug fixes. It prevents unnecessary code and keeps the change aligned with the project design system.

> Even a small bug or UI fix requires the Lazy Gate. Never edit source files arbitrarily.

---

## ⚙️ Three Steps (The Lazy 3-Step)

### Step 1 — Lazy Explore (60 seconds)

Quickly inspect the project:

- Read `AGENTS.md` and relevant `.rules/` files.
- Check the applicable layers in `docs/architecture/` and `docs/design/`.
- Inspect the likely files to understand boundaries, existing APIs, and reuse opportunities.

**Catlazy rules:**

- If the task is obviously small and clear, skip directly to the Lazy Gate; Step 2 is optional.
- If it is complex, ambiguous, or touches multiple files, use **Observe → Decide → Plan → Apply → Verify → Continue** and resolve only one issue per round.
- **Decomposition:** if the request is too large, such as “build the entire feature,” split it into smaller tasks and bring only the first task through this design process.

### Step 2 — Interactive Interview (Grill-me and Lazy Options)

For complex or unclear requirements, interview the user one decision at a time:

1. Ask only one question per message.
2. Offer A/B/C choices for every question:

   ```text
   A) [Laziest approach] — approximately N lines / trade-off: ... (recommended)
   B) [Standard approach] — approximately N lines / trade-off: ...
   C) [Complete approach] — approximately N lines / trade-off: ...
   ```

3. Use the host’s question UI when available.
4. Search and verify answers from the codebase first; do not ask the user about facts that can be discovered locally.

**Blast-radius check:** if the shortest approach forces changes across many unrelated files or loses isolation, it is not truly lazy. Find a safer boundary instead.

### Step 3 — Lazy Gate ✋ (Implementation Plan Artifact)

Before creating the plan, silently complete all four Lazy Verification checks in Section 5 of `AGENTS.md`—including repository-wide reference search and inspection of real component APIs.

Then use the host’s file-writing capability to create `docs/plans/YYYY-MM-DD-<topic>.md`. Do not write a long plan in chat. The artifact must include:

1. **Goal:** a concise statement of the change.
2. **Affected files and layers:** every file to create, edit, or delete.
3. **Core code snippets:** the most important actual snippets or diffs that will be implemented, so the user can see the intended code or UI.
4. **Verification status:** a short confirmation that Lazy Verification passed.
5. **Decision trail (when needed):** concise Observation, Decision, Planned Action, and Verification; small tasks may use only Planned Action and Verification.

Wait for the user to read the artifact and press **Proceed/Approve** before writing any planned source changes.

### Task Context for Follow-up Work

For work that will be reviewed or fixed later, record a minimal task context in the plan artifact:

```json
{
  "base": "origin/main",
  "scope": "ui",
  "files": ["src/features/example"],
  "format": "normal",
  "validationProfile": "ui"
}
```

This context is optional. It may be saved as `.catlazy/task.json` only when the user wants the task to persist across messages. Otherwise, keep it in the approved plan and command arguments. Never infer that every dirty worktree file belongs to the active task.

## 🚫 Anti-Patterns

- Do not offer more than three choices.
- Do not write a multi-page specification for a simple task.
- Do not create a visual mockup or browser preview as a substitute for implementation planning.
- Do not skip the Lazy Gate, even for a bug fix or UI tweak.
- Do not ask several questions at once.

## ✅ Principles

- Small task → short plan artifact with the intended code change, then wait for approval.
- Complex task → Lazy Explore and Lazy Options, then a more detailed artifact.
- Apply YAGNI first: remove unnecessary scope before it becomes code.
- **UI/UX feedback:** every user interaction needs a visible response, such as loading, success/error notification, or hover/pressed state. Never design a control that goes silent after activation.
- **Large-task specification:** if a complex task needs extra explanation, record it at `docs/design/YYYY-MM-DD-[topic].md`, no longer than one page, so another agent can continue it.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

You MUST create the Implementation Plan artifact in `docs/plans/` with the host’s file-writing capability. Do not write the plan as a long chat message. Wait for user approval before touching source files.

### 🔎 Inspection Summary

- Confirm all four Lazy Verification checks: repository search, component inspection, i18n check, and design-document check.
- Evaluate the Ladder of Laziness: YAGNI → Reuse → Stdlib → Native → Dependency → One-line → Minimum.
- For complex tasks, record Observation → Decision → Planned Action → Verification; for small tasks, Plan → Apply → Verify is enough.

Then create the artifact and wait for Proceed before writing code.

**⚠️ CRITICAL RULE FOR AI:**

NEVER write source code before creating an Implementation Plan artifact and receiving user approval. This applies to every task type, including bug fixes and minor UI changes. Early source edits are forbidden.
