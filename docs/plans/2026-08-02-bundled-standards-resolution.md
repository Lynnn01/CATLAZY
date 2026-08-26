# Bundled Standards Resolution for Audit Skills

## Goal

Ensure Catlazy audit skills can always read their canonical architecture and design standards when the target repository does not include a `docs/` folder.

## Affected files

- `skills/catlazy2-review/SKILL.md`
- `skills/catlazy3-architecture/SKILL.md`
- `skills/catlazy4-interface/SKILL.md`
- `skills/catlazy5-experience/SKILL.md`
- Matching active host copies under `C:\Users\jetsa\.codex\skills\CATLAZY\skills\`

## Core change

```diff
- Read only docs/... in the target repository.
+ Resolve standards in this order:
+ 1. Target repository docs/... when present.
+ 2. The bundled Catlazy docs/ directory beside the installed skills.
+ Do not replace the audit with generic principles when bundled standards exist.
```

## Verification

- Check each skill has the same resolution order.
- Confirm the repository and active host copies match.
- Confirm no generic fallback text remains for missing target-repository docs.
