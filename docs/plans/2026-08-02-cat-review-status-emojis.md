# Catlazy Review Status Emoji Format

## Goal

Replace textual review statuses with a consistent cat-prefixed emoji format.

## Affected files

- `skills/catlazy2-review/SKILL.md`
- Active host copy of the same skill under `C:\Users\jetsa\.codex\skills\CATLAZY\skills\catlazy2-review\SKILL.md`

## Core change

```diff
- `[PASS]` / `[FAIL]` / `[N/A]`
+ `🐈 ✅` = pass, `🐈 ❌` = fail, `🐈 ⚪` = not applicable
```

## Verification

- Confirm no `PASS`, `FAIL`, or `N/A` status template remains in the review skill.
- Confirm the repository and active host copies have identical hashes.
