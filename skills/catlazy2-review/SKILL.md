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

### Standards Resolution

Before reviewing, resolve Catlazy standards in this order:

1. Use the target repository’s `docs/architecture/`, `docs/design/user_interface/`, and `docs/design/user_experience/` when they exist.
2. If any of those directories are absent, use the matching canonical directories in the installed Catlazy bundle: the `docs/` directory beside the bundle’s `skills/` directory.
3. Do not replace a missing target-repository document with generic Clean Architecture or product principles when the bundled Catlazy document is available.
4. State which source of standards was used in the Inspection Summary.

### Task Context and Modes

Resolve the task context before inspecting a diff. Accept these optional arguments:

```text
catlazy2-review [report|fix-safe] [--scope ui|backend|api|docs|full]
                [--base <commit-or-ref>] [--files <path,...>]
                [--format normal|strict] [--language <code>]
```

Resolve values in this order: explicit arguments, optional `.catlazy/task.json`, files explicitly named by the user, then candidate changed files. Candidate changes include tracked and untracked files. If the final fallback contains unrelated dirty changes, show the candidate file list and ask for confirmation before reviewing.

Resolve and announce the mode once before inspection. The mode is locked for that review run: do not rename a `fix-safe` pass to `report` afterward. If `fix-safe` edits anything, finish that pass and start a new final `report` review against the resulting diff.

Treat the resolved `files` as the approved write scope when the task context was approved. Compare task changes against `base`, report any task edit outside `files`, and do not count pre-existing unrelated dirty files as task output. `report` may read outside scope for evidence but must not write.

- `report` is the default and never edits files.
- `fix-safe` may repair only local, low-risk findings inside the resolved scope, then reruns this review and the selected validation profile.
- Never auto-fix data changes, authentication/authorization, public contracts, dependencies, migrations, generated files, or anything outside scope.
- `normal` uses concise summary, findings, and fixes. `strict` uses the full checklist.
- State the resolved mode, scope, baseline, file list, standards source, and output language before reporting findings.

### Validation Profiles

Resolve the profile from an explicit argument, the optional task manifest, then the selected scope. Discover actual project scripts before running anything; never guess commands.

- `ui`: relevant typecheck and lint.
- `backend`: relevant lint, tests, and build.
- `api`: relevant lint, tests, and contract/type checks.
- `docs`: available skill/frontmatter, link, Markdown, JSON, and diff checks; runtime lint, tests, and build are `N/A` unless the changed files affect runtime behavior.
- `full`: all applicable profiles for the resolved files.

An implementation or `fix-safe` pass runs applicable validation after its last edit and records the evidence. A final `report` review consumes that current evidence; it may run a confirmed non-mutating check when evidence is missing, but must say that the report ran it. Never run a mutating check in `report` mode. Keep validation inside the resolved scope where the tool supports file targeting, and report unavailable commands rather than substituting unrelated checks.

Build an expected-check list from the resolved profile and files. Report every expected check as `PASS`, `FAIL`, or `N/A`; every `N/A` must include the concrete reason. A mutating lint script may be `N/A` when it cannot be safely scoped, but do not treat that as a pass or silently replace it.

For `ultra`, add the smallest relevant negative-path validation for critical calculations, financial logic, authorization, parsers, validators, or regression fixes. Run a fault probe only when the approved task explicitly requests one. Prefer an existing mutation tool or disposable copy; never mutate a live dirty worktree, and verify that no probe artifact remains.

### Hollow Implementation Check

Inspect task-introduced code for completion-shaped placeholders. Search heuristically, then inspect context before reporting a finding:

- new `TODO` or `FIXME` markers that defer required behavior;
- `pass`, `NotImplementedError`, empty handlers, or swallowed exceptions;
- hard-coded success responses or production paths returning fake data;
- UI controls without their promised action;
- skipped tests or assertions that cannot fail meaningfully;
- mocks, fixtures, or placeholder values leaking into production paths.

Do not flag intentional framework hooks, documented Catlazy deferrals, test doubles confined to tests, or unrelated pre-existing code. A hollow implementation that prevents the requested behavior from working is at least P2 and prevents `CATLAZY_DONE`.

### Catlazy Finish Contract

Use one final status for the resolved task:

- `CATLAZY_DONE`: the approved scope is respected, all required validation passes, the evidence is current, the final diff is reviewed, generated files are accounted for, and no P1 or P2 finding remains.
- `CATLAZY_BLOCKED: <reason>`: an external dependency or required decision prevents completion.
- `CATLAZY_UNVERIFIED: <missing check>`: the implementation may be complete, but required validation is missing, stale, unavailable, or failing.

Use `CATLAZY_BLOCKED` when an external dependency or required user decision prevents progress. Otherwise use `CATLAZY_UNVERIFIED` for missing or stale evidence; do not use both for one run.

Keep the evidence lightweight. For each applicable validation, report the command, result or exit status, and run time. In `report` mode, use only evidence available from the current task and do not imply that review-only inspection executed validation.

For any build or generator evidence, state whether tracked generated paths were snapshotted before the command and whether the final diff contains generated churn. Missing generated-output accounting prevents `CATLAZY_DONE` when such a command ran. If no build or generator ran because none applies to the resolved files, report generated output as `N/A` with that reason.

Apply the last-edit rule: validation counts only when it ran after the last relevant edit in the resolved files. If `fix-safe` changes a file after validation, rerun only the affected profile. If freshness cannot be established, use `CATLAZY_UNVERIFIED`.

Catlazy is a workflow guardrail, not filesystem enforcement. Verify the final diff against the resolved file list and report any out-of-scope change without claiming ownership of unrelated dirty files.

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
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [hollow-implementation] ...
- `🐈 ✅` / `🐈 ❌` / `🐈 ⚪` [Architecture] ...

### 🐈 Catlazy Finish Check

Report scope, validation, freshness, diff review, generated files, and unresolved P1/P2 findings as `PASS`, `FAIL`, or `N/A`. Give a concrete reason for every `N/A`. Include the lightweight evidence and end with exactly one Catlazy status.

If an item fails, include file and line, reason, violated rule, and the smallest Catlazy fix. Always output all three required sections. For a clean review, include **“The code is simple and follows the project rules.”** before the final Catlazy status.
