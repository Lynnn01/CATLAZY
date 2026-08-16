# Project Guidelines (AGENTS.md)

Welcome. These rules apply to projects using the Catlazy architecture and skills.

## 1. Catlazy Philosophy (The Lazy Senior Dev)

- **Simplicity first:** avoid over-engineering and write only the code required for the current problem.
- **Architecture is not over-engineering (critical):** the unified Domain, Application, Infrastructure, and Presentation layers are foundational requirements. Do not flatten, merge, or delete them in the name of simplicity.
- **The ladder of laziness:** first ask whether code is needed, whether existing code can be reused, and whether a standard-library or native feature already solves the problem.
- **Catlazy mark:** when intentionally simplifying or deferring a complex implementation, add `catlazy: <simplification> | ceiling: <current limit> | upgrade: <trigger to revisit>` so the debt ledger can track it.

## 2. Unified Architecture

- Follow the principles in `docs/architecture/`.
- Keep strict boundaries between Domain, Application, Infrastructure, and Presentation. Catlazy agents must not delete these layers.
- Framework-specific code must not leak into the Domain layer.

## 3. Design Systems (Strict UI/UX Compliance)

- **No guessing (critical):** do not invent UI or UX styles. Follow `docs/design/user_interface/` and `docs/design/user_experience/`.
- Use the project’s designated color tokens, grid, component, and motion guidance.
- Always design for accessibility and clear feedback, including loading, toast, empty, and error states.

## 4. Lazy Communication (Before Writing Code)

- **Global planning gate (critical):** before any code, frontend, backend, UI, UX, or bug-fix change, create `docs/plans/YYYY-MM-DD-<topic>.md`. Include the goal, affected files, and actual core snippets or diffs. Wait for user approval before editing planned files.
- **Mode lifetime:** the selected Catlazy mode applies until the user changes it or the task ends. Safety, security, accessibility, and this planning gate always take priority.
- **One question at a time:** ask one clarifying question per message, preferably with A/B/C choices when a question is necessary.
- **YAGNI check:** before proposing a solution, ask whether there is a lazier path, whether it can be one line, and whether the feature needs to exist at all.
- **Incremental decision trail:** for complex or multi-file work, resolve one issue at a time: **Observe → Decide → Plan → Apply → Verify → Continue**. Show concise evidence and decisions, never private chain-of-thought. For small, clear work, use **Plan → Apply → Verify**.

## 5. Lazy Verification (Before Any Edit)

Complete these checks before writing code:

- **Blast-radius check:** before renaming or deleting a variable or function, search the repository for all usages. Never delete until remaining references are understood.
- **Component-contract check:** before using a custom component such as `<Modal>`, `<Button>`, or `<Card>`, inspect its real props and API. Never guess prop names.
- **Design-consistency check:** before adding a UI element, inspect how the same element is used elsewhere. Never invent a new icon, color, spacing, or animation without checking existing patterns.
- **Golden-rules check:** before writing user-facing text, check whether the project uses i18n such as `t()`. Before adding data-fetching logic, check whether RLS or auth filters apply.
- **External-CLI gate:** before using an external subcommand that has not been verified in the current environment, inspect `<command> --help` (and subcommand help when available). Do not infer a command from another CLI or version.
- **Generated-output guard:** before running a build or generator that may touch tracked output, record the clean/dirty state and tracked generated paths. Prefer disposable output; otherwise verify and restore only task-created generated churn.

## 6. Communication and Language

- Use concise progress updates for multi-step work and report evidence from verification.
- Respond in the user’s language unless the user explicitly requests another language. English is the canonical language for repository rules, skills, and documentation.

## 7. Task Scope and Safe Automation

- Before writing, reviewing, auditing, formatting, or automatically fixing, resolve the task scope from explicit arguments, an optional `.catlazy/task.json`, or user-named files. Show the approved file list before the first implementation edit.
- After the user approves the task, treat `files` as the approved write scope. Reading outside that scope is allowed for discovery; writing outside it is not. If implementation requires another path, stop before writing it, explain why, and obtain approval to expand the scope.
- Compare the final task diff with the recorded baseline and approved files. Do not attribute pre-existing or unrelated dirty files to the task.
- Review mode is explicit and locked for one review run: `report` does not edit; `fix-safe` may change only local, low-risk items within the approved scope. Never relabel a run afterward; after `fix-safe`, start a new final `report` review.
- Do not auto-fix data changes, auth, public contracts, dependencies, migrations, generated files, or unrelated dirty worktree files.
- Use UTF-8 for text reads and writes. If encoding is uncertain or text is mojibake, stop and inspect the encoding before patching.
- Run validation and formatting only for files in scope. Keep formatting-only changes separate from functional changes.
- Keep operational commands single-purpose. Separate secret retrieval, connection construction, ignored-env writing, migration/import, and verification; do not print secrets or combine the steps into one opaque shell command.
- On a policy rejection, change mechanism immediately. After two equivalent operational failures, stop retrying that command pattern and simplify it or use a different mechanism.

## 8. Catlazy Finish Contract

- Report `CATLAZY_DONE` only when the approved scope is respected, every required validation passes, the final diff is reviewed, generated files are accounted for, and no unresolved P1 or P2 finding remains.
- Report `CATLAZY_BLOCKED: <reason>` when an external dependency or required decision prevents completion. Report `CATLAZY_UNVERIFIED: <missing check>` when the change may be implemented but required evidence is missing, stale, unavailable, or failing.
- Keep a short evidence trail in the approved plan, optional `.catlazy/task.json`, or final report: validation command, result or exit status, and when it ran. Never imply that an unavailable or skipped check passed.
- Report every expected validation as `PASS`, `FAIL`, or `N/A`. Every `N/A` must name the concrete reason, such as no applicable files or a project script that mutates files outside the approved scope.
- **Last-edit rule (critical):** validation is current only when it ran after the last relevant edit in its scope. After a later edit, rerun only the affected validation profile before reporting `CATLAZY_DONE`.
- These rules and skills are workflow guardrails, not filesystem enforcement. If the host cannot enforce an edit boundary, state that limitation and verify the final diff against the approved scope.
