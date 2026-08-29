# Project Guidelines (AGENTS.md)

Welcome. These rules apply to projects using the Catlazy architecture and skills.

## 1. Catlazy Philosophy (The Lazy Senior Dev)

- **Simplicity first:** avoid over-engineering and write only the code required for the current problem.
- **Architecture is not over-engineering (critical):** the unified Domain, Application, Infrastructure, and Presentation layers are foundational requirements. Do not flatten, merge, or delete them in the name of simplicity.
- **The ladder of laziness:** first ask whether code is needed, whether existing code can be reused, and whether a standard-library or native feature already solves the problem.
- **Reusable-first policy (critical):** when creating new files or features, extract helper functions, pure calculations, formatters, and common invariants into layer-aligned central shared folders (`shared/utils/`, `shared/domain/`, etc.) instead of writing inline duplicates.
- **Catlazy mark:** when intentionally simplifying or deferring a complex implementation, add `catlazy: <simplification> | ceiling: <current limit> | upgrade: <trigger to revisit>` so the debt ledger can track it.
- **Cross-platform persistence:** Catlazy rules are universal across AI assistants (Antigravity, Claude, Codex, Cursor, Windsurf, Copilot). Use `/catlazy --embed` to persist the standard rule snippet into host-specific configuration files.

## 2. Unified Architecture

- Follow the principles in `docs/architecture/` (including `08-shared-and-reusable-modules.md`).
- Keep strict boundaries between Domain, Application, Infrastructure, and Presentation. Catlazy agents must not delete these layers.
- Shared modules (`shared/` or `core/`) must follow layer separation and NEVER import feature-specific code.
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

- **Reusability check:** before creating a new helper or utility, search existing `shared/` folders for reusable implementations. If new logic will be needed by multiple callers, place it in `shared/` rather than inlining it in a local feature file.
- **Blast-radius check:** before renaming or deleting a variable or function, search the repository for all usages. Never delete until remaining references are understood.
- **Component-contract check:** before using a custom component such as `<Modal>`, `<Button>`, or `<Card>`, inspect its real props and API. Never guess prop names.
- **Design-consistency check:** before adding a UI element, inspect how the same element is used elsewhere. Never invent a new icon, color, spacing, or animation without checking existing patterns.
- **Golden-rules check:** before writing user-facing text, check whether the project uses i18n such as `t()`. Before adding data-fetching logic, check whether RLS or auth filters apply.
- **External-CLI gate:** before using an external subcommand that has not been verified in the current environment, inspect `<command> --help` (and subcommand help when available). Do not infer a command from another CLI or version.
- **Generated-output guard:** before running a build or generator that may touch tracked output, record the clean/dirty state and tracked generated paths. Prefer disposable output; otherwise verify and restore only task-created generated churn.

## 6. Communication and Language

- Use concise progress updates for multi-step work and report evidence from verification.
- Respond in the user’s language unless the user explicitly requests another language. English is the canonical language for repository rules, skills, and documentation.

## 7. Standard Input Contract and Task Scope

- All Catlazy skills accept a standardized input argument contract:
  ```text
  catlazy<N>-<skill> [report|fix-safe] [--scope ui|backend|api|docs|full]
                     [--base <commit-or-ref>] [--files <path,...>]
                     [--format normal|strict] [--language <code>]
  ```
- Resolve input values in strict precedence order: explicit command arguments > optional `.catlazy/task.json` manifest > user-named files > candidate changed files.
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

## 9. Standardized Skill Output Contract (Universal 3-Section Format)

All Catlazy skills, reviews, audits, and reports MUST output using the exact 3-section structure without conversational filler before the first heading:

### 1. `### 🔎 Inspection Summary`
- **Target / Scope:** resolved mode, scope, baseline, and files.
- **Standards Source:** state whether target repository (`docs/`) or bundled fallback standards were used.
- **Observation:** concise evidence and key findings summary.

### 2. `### 📋 Inspection Checklist`
- Report all items using standardized status badges: `[PASS]`, `[FAIL]`, or `[N/A]`. Every `[N/A]` must state the concrete reason.
- For any failure or finding, format details using the unified finding structure:
  - **Target:** `[file:line]` or `[component/layer]`
  - **Tag & Rule:** `[tag-name]` citing the violated guideline
  - **Evidence:** observed code or behavior evidence
  - **Smallest Fix:** smallest non-overengineered remediation

### 3. `### 🐈 Catlazy Finish Check`
- Report `[PASS]`, `[FAIL]`, or `[N/A]` for:
  - `Scope & Safety`
  - `Validation & Freshness`
  - `Diff & Side-effects`
- **Verdict:** concise one-line verdict statement.
- **Terminal Status:** conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.

## 10. DISMATH Reasoning Standard (Formal Logic Foundation)

`docs/logics/dismath/` is the formal reasoning foundation for all Catlazy skills, architecture, plans, and rules. See `docs/logics/dismath/11-catlazy-formal-methods.md` for complete chapter mappings.

- **Planning with Hoare triples (critical):** every implementation plan in `docs/plans/YYYY-MM-DD-*.md` MUST follow the Hoare triple structure $\{P\} S \{Q\}$ (DISMATH Ch. 08), specifying pre-condition $\{P\}$, statement/changes $S$, post-condition $\{Q\}$, and system invariants $\{I\}$.
- **Predicate architecture invariants:** layer rules are universal quantified predicates $\forall f \in \text{Layer}, \forall d \in \text{Imports}(f)$ (DISMATH Ch. 03–04). Findings (`[arch-leak]`, `[arch-bypass]`) are formal counterexamples.
- **Inference & Fallacy guard:** reasoning during review, audit, and decision-making MUST use valid rules of inference (Modus Ponens, Modus Tollens, Resolution) (DISMATH Ch. 05). Informal fallacies (affirming the consequent, denying the antecedent, circular reasoning) are strictly prohibited.
- **Proof of necessity (YAGNI):** justify new abstractions or dependencies via proof by contradiction (DISMATH Ch. 06): prove that omitting the abstraction leads to unacceptable failure.
- **Propositional consistency (SAT):** all agent rules and cross-platform configurations must be mutually satisfiable: $\varphi = R_1 \land R_2 \land \dots \land R_n \not\equiv \mathbf{F}$ (DISMATH Ch. 01–02, 10).
- **Inductive loop termination:** any repeating or looping skill (such as `/catlazy10-loop`) must define a strictly decreasing Loop Variant $V(i) > 0$ guaranteeing termination in finite steps (DISMATH Ch. 07).

