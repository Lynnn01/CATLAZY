# Operational Efficiency Guardrails

## Goal

Turn the latest Catlazy workflow review into concise, enforceable rules for verified external CLI usage, deterministic database cutovers, generated-output protection, review-mode integrity, bounded retries, simple secret-bearing commands, and explicit validation N/A reporting.

## Baseline and Approved Scope

- Baseline: `54a83bafe1cca87a62885f2368988bf0b4b2641a`
- Repository state before planning: clean
- Review mode after implementation: `report` (locked)
- Validation profile: documentation/skill validation
- Planned files:
  - `.rules/AGENTS.md`
  - `skills/catlazy/SKILL.md`
  - `skills/catlazy2-review/SKILL.md`
  - `skills/catlazy/references/database-cutover.md` (new)
  - `docs/plans/2026-08-03-operational-efficiency-guardrails.md`

Reading outside these paths is allowed for evidence. Writing outside them requires a scope update and new approval.

## Core Changes

### General operational guardrails

Add compact rules equivalent to:

```md
- Run `<command> --help` before using an external subcommand not already verified in the current environment.
- After a policy rejection, change mechanism immediately. After two equivalent operational failures, stop retrying that command pattern and simplify or replace it.
- Before a build, record tracked generated paths and verify or restore only task-created churn afterward.
- Report every expected validation as PASS, FAIL, or N/A; N/A requires a concrete reason.
- Keep secret retrieval, connection construction, ignored-env writing, migration/import, and verification as separate steps; never print secrets.
```

### Deterministic database cutover reference

Add a low-freedom recipe:

```text
destination-empty check
-> full backup + SHA-256 + rollback path
-> sanitize dump session settings such as empty search_path when required
-> import
-> schema-qualified verification
-> row/FK/sequence checks
-> deterministic digests with COLLATE "C" for ordered text
-> smoke tests
-> destructive cleanup only after all checks pass
```

The reference will require exact target/container/volume identity checks and keep credentials out of commands, logs, and committed files.

### Review-mode lock and finish evidence

Clarify that the resolved review mode is immutable for that review run. A `fix-safe` implementation pass must start a new final `report` review rather than relabel the earlier run. Require generated-output status and explicit validation N/A reasons in the finish check.

## Lazy Verification Status

- Repository search: passed; existing scope, review-mode, generated-file, validation, and finish-contract rules were located.
- Component/API inspection: N/A; no UI components or runtime API contracts are in scope.
- i18n check: N/A; repository rule and skill source remains English canonical.
- Design-document check: passed; this change affects operational agent guidance, not UI/UX behavior.
- Ladder of Laziness: reuse the existing AGENTS and skill structure; add one progressive-disclosure database reference instead of a new command, dependency, or helper script.

## Verification

After the last edit:

1. Run the skill validator against each changed skill folder.
2. Parse `plugin.json` and check Markdown/frontmatter structure with existing local tools.
3. Search for all new rule keywords and confirm the database reference is linked from the core skill.
4. Run `git diff --check`.
5. Compare the final changed paths with the approved scope.
6. Run `catlazy2-review report --scope full --base 54a83bafe1cca87a62885f2368988bf0b4b2641a --files <approved paths>` and keep the mode locked as `report`.

## Decision Trail

- Observation: Safety controls worked, but unverified CLI usage, nondeterministic database verification, late generated-file cleanup, mode relabeling, repeated blocked commands, and oversized PowerShell steps created avoidable rework.
- Decision: Put broadly applicable rules in `.rules/AGENTS.md`, execution behavior in the core skill, review evidence rules in `catlazy2-review`, and fragile database details in one directly linked reference.
- Planned Action: Edit only the five paths listed above after approval.
- Verification: Validate skill structure, inspect keywords and links, check the diff, then perform a locked read-only final review.

## Implementation Evidence

- `quick_validate.py skills/catlazy`: PASS after the last skill edit at `2026-08-03T23:18:14+07:00` with `PYTHONUTF8=1`.
- `quick_validate.py skills/catlazy2-review`: PASS after the last skill edit at `2026-08-03T23:18:14+07:00` with `PYTHONUTF8=1`.
- Initial validator attempt: FAIL/N/A as skill evidence because Windows Python selected `cp1252`; rerun with process-scoped UTF-8 passed without a source edit.
- `plugin.json` parse: PASS.
- Reference link and required-rule search: PASS after simplifying one failed PowerShell quoting attempt.
- Read-only forward-tests: PASS after adding write-quiescence/provider gates to the cutover recipe and clarifying docs validation, untracked candidates, generated-output N/A, and finish-status precedence in the review skill.
- Application build and lint: N/A — approved files are Markdown guidance; no runtime source is in scope, and unrelated project build/lint would not validate these skills.
- Active-host synchronization: N/A for this implementation scope — installed files are outside the approved paths and currently do not hash-match the repository changes.
