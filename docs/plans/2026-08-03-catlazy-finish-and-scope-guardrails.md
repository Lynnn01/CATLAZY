# Catlazy Finish and Scope Guardrails

## Goal

Complete the lightweight Catlazy completion workflow: approved write scope, current validation evidence, a shared finish check, hollow implementation review, and optional ultra-only fault probes.

## Affected files and layers

- `.rules/AGENTS.md` — global scope and completion rules.
- `.catlazy/task.json.example` — minimal persistent task context.
- `skills/catlazy/SKILL.md` — consistent lite/full/ultra behavior.
- `skills/catlazy0-help/SKILL.md` — concise user-facing level and finish reference.
- `skills/catlazy1-design/SKILL.md` — approved write-scope protocol.
- `skills/catlazy2-review/SKILL.md` — scope verification, hollow checks, and finish verdict.
- `skills/catlazy3-architecture/SKILL.md` through `skills/catlazy9-compress/SKILL.md` — portable scope and finish rules for approved edits.
- `README.md` — portable workflow documentation.
- `docs/plans/2026-08-03-catlazy-finish-and-scope-guardrails.md` — this approved plan record.
- `C:/Users/jetsa/.codex/skills/CATLAZY/` — active host mirror of the changed rules, manifest example, README, and skills after repository validation.

No runtime, hook, scanner, cryptographic seal, marketplace entry, or new dependency will be added.

## Core snippets

```text
files = approved write scope
read outside scope = allowed
write outside scope = stop and request scope expansion
final diff = compare task changes with baseline and approved files
```

```text
CATLAZY_DONE
CATLAZY_BLOCKED: <reason>
CATLAZY_UNVERIFIED: <missing check>
```

```text
ultra = full + hollow review + negative-path validation
fault probe = optional, targeted, approved, and isolated from the live dirty worktree
```

## Verification status

- Repository rules, task manifest, README, mode skill, design skill, and review skill inspected in UTF-8.
- Existing active host copy and plugin shape inspected.
- User approved the complete roadmap in the current task, so implementation may continue without a second approval round.

## Decision trail

- **Observation:** Catlazy already resolves task files but does not treat them as the approved write boundary.
- **Decision:** Make `files` the protocol boundary while stating that host enforcement remains a soft guardrail.
- **Planned Action:** Align the global rules, core modes, design/review skills, manifest example, and README.
- **Verification:** Validate every changed skill, inspect the scoped diff, scan for hollow or borrowed terminology, sync the active copy, and compare SHA-256 hashes.
