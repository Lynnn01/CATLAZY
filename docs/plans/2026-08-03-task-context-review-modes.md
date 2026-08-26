# Task Context and Review Modes

## Goal

Make Catlazy reviews deterministic in a dirty worktree by establishing an explicit task scope, a selectable baseline, and an explicit report-versus-safe-fix mode.

## Affected files

- `skills/catlazy2-review/SKILL.md`
- `skills/catlazy3-architecture/SKILL.md`
- `skills/catlazy4-interface/SKILL.md`
- `skills/catlazy5-experience/SKILL.md`
- `skills/catlazy1-design/SKILL.md`
- `README.md`
- `.rules/AGENTS.md`
- Optional task manifest template: `.catlazy/task.json.example`

## Task Context Contract

```text
catlazy review [report|fix-safe] [--scope ui|backend|api|full]
                [--base <commit-or-ref>] [--files <path,...>]
                [--format normal|strict] [--language <code>]
```

Resolution order:

1. Explicit command arguments.
2. Optional `.catlazy/task.json` manifest.
3. The current task's explicitly named files.
4. A safe default: show the candidate changed files and ask for confirmation; never silently review all unrelated dirty changes.

## Core behavior

```diff
- Review all `git diff` changes.
+ Resolve and print the task scope before review.
+ `report`: inspect only; do not edit.
+ `fix-safe`: repair only approved, local, low-risk findings in scope,
+ then re-run the same review and validation profile.
```

```json
{
  "base": "origin/main",
  "scope": "ui",
  "files": ["src/features/screener"],
  "format": "normal",
  "validationProfile": "ui"
}
```

## Safe-fix boundaries

- Allowed: local duplication, unused imports, spelling/documentation corrections, or a token/style reuse that does not change behavior.
- Never automatic: data mutations, authentication/authorization, public API contracts, dependency changes, migrations, generated files, or edits outside resolved scope.
- If a fix needs a judgment call, report it and wait for approval.

## Verification

- Skills document the same scope-resolution order and report/fix-safe distinction.
- The manifest is optional and ignored unless explicitly present.
- Candidate files are shown before review.
- No formatting command may run outside resolved files.
- Repository and active-host skill copies have matching hashes.
