# Implementation Plan: Active Skill Sync and README Repair

## Goal

Ensure the review skill that the host actually loads has the same safe, evidence-based output contract as this repository, and remove broken or misleading Headroom guidance.

## Affected files

| File | Change |
|---|---|
| `R:\CATLAZY\README.md` | Remove the missing `docs/integrations.md` link; move Docker from mandatory prerequisites to the optional Headroom step; clarify that environment variables are only needed when using the proxy. |
| `R:\CATLAZY\plugin.json` | Bump patch version from `1.0.0` to `1.0.1` so the synchronized skill set is identifiable. |
| `C:\Users\jetsa\.codex\skills\CATLAZY\skills\catlazy2-review\SKILL.md` | Sync the active review skill with the repository's `skills/catlazy2-review/SKILL.md`, replacing private Chain-of-Thought requirements with `Inspection Summary` and adding the incremental repair-loop prompt. |

## Core changes

```diff
- ### 🧠 Analysis (Chain of Thought)
+ ### 🔎 Inspection Summary

- ดู [Integration Contract](docs/integrations.md) ...
- ติดตั้ง Docker
+ Docker จำเป็นเฉพาะเมื่อเลือกใช้ Headroom Proxy
```

The installed skill will be copied from the repository source after its contents are verified, not edited independently. This keeps `R:\CATLAZY` as the single source of truth.

## Verification

1. Compare the repository and installed `catlazy2-review/SKILL.md` byte-for-byte after sync.
2. Confirm no README link targets the missing integration document.
3. Confirm Docker is described only as an optional Headroom requirement.
4. Validate `plugin.json` parses as JSON and run `git diff --check`.

## Scope and safety

- The active skill path is outside the workspace, so the copy requires explicit elevated filesystem permission.
- No credentials, `.env`, Docker container, or network resource will be changed.
