# Implementation Plan: English Canonical Source

## Goal

Convert the plugin's maintained source documentation, rules, and skills to English so it can operate consistently across AI hosts and teams, while preserving localized user interaction by responding in the user's language unless a task explicitly requires another language.

## Scope

### Convert to English

- `.rules/AGENTS.md`
- `README.md`, `docs/INDEX.md`, every architecture/UI/UX guide, and document indexes
- All `skills/*/SKILL.md`
- `.env.example` comments and `run-headroom.bat` messages if any Thai remains

### Preserve

- File paths, skill names, command names, code blocks, URLs, JSON keys, and technical identifiers
- Existing `docs/plans/` artifacts as historical records; they are not canonical product documentation
- The active skill's source-of-truth relationship: `R:\CATLAZY\skills\catlazy2-review\SKILL.md` remains the file copied to the host-loaded path after verification

## Behavioral change

```diff
- You must output in Thai language.
+ Respond in the user's language unless the task explicitly requests a different language.

- อธิบายเหตุผลสั้นๆ เป็นภาษาไทยเสมอ
+ Explain the reason concisely in the user's language.
```

## Implementation groups

1. Translate rules, README, top-level docs, and architecture documents.
2. Translate design UI/UX documents and indexes.
3. Translate all skill instructions and replace Thai-only output constraints with the language policy.
4. Bump plugin version to `1.1.0`, sync the active review skill, then verify paths, Markdown links, JSON, and skill hashes.

## Verification

1. Search canonical source files for Thai Unicode; expected exceptions are paths/identifiers and intentionally retained historical plans only.
2. Confirm every skill contains the same language policy and no Thai-only output requirement.
3. Compare repository and active `catlazy2-review` SHA-256 hashes.
4. Run `git diff --check` and parse `plugin.json`.

## Safety

- No application runtime code, secrets, APIs, or external service configuration will change.
- Syncing the active skill path requires explicit elevated filesystem permission and occurs only after repository translation is verified.
