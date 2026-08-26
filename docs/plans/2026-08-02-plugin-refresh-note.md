# Implementation Plan: Plugin Refresh Note

## Goal

Document the one required maintenance step after updating this repository: reload or reinstall the plugin in the AI host so its active skills match the repository version.

## Affected file

| File | Change |
|---|---|
| `README.md` | Add one concise note below the project structure stating that the host must reload/reinstall the plugin after an update, following that host's own procedure. |

## Core change

```diff
+ > หลังอัปเดต plugin ให้ reload หรือ reinstall plugin ตามวิธีของ AI host
+ > เพื่อให้ skills ที่ host โหลดอยู่ตรงกับเวอร์ชันใน repository
```

## Verification

1. Confirm the note does not claim a vendor-specific command.
2. Confirm the README remains valid Markdown.
3. Run `git diff --check`.
