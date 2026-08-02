---
name: catlazy2-review
description: Review current changes against project rules and guidelines
---
# Catlazy Code Review

When invoked, review only the latest changes (`git diff` or uncommitted changes) against `AGENTS.md`, `.rules/`, architecture docs, and design docs.

### Review Scope

1. Confirm the change is limited to the requested behavior and does not introduce over-engineering.
2. For UI code, check accessibility contrast, accessible names, focus, touch targets, semantic tokens, responsive layout, and reduced motion.
3. For UX, check progressive disclosure, loading/error/empty feedback, recovery, and consistent terminology.
4. Perform lazy verification: search references before deletions, inspect custom component contracts, reuse existing styles, check i18n before hard-coded user text, and verify auth/RLS filters before data access.
5. Check security, data-loss handling, and layer boundaries.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Do not output conversational text before the required headings. Respond in the user’s language unless another language is requested.

### 🔎 Inspection Summary

Analyze the changed files with evidence and check each applicable UI, UX, architecture, and lazy-verification rule. For follow-up work, state the next **Observation → Decision → Planned Action → Verification** step.

### 📋 Review Checklist

- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [P1-Accessibility] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [UX-Feedback] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [grep-miss] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [api-guess] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [style-invent] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [hardcode-text] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [Architecture] ...

If an item fails, include file and line, reason, violated rule, and the smallest Catlazy fix. Even when everything passes, always output both required sections. End a clean review with: **“The code is simple and follows the project rules.”**
