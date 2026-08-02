# Implementation Plan: Review Follow-ups

## Goal

Resolve the review findings without adding new runtime behavior: remove the unused validator, make every changed audit skill use one output header, and align README's Headroom wording with the integration contract.

## Affected files

| File | Change |
|---|---|
| `scripts/validate-plugin.ps1` | Delete; it has no CI or release consumer. |
| `skills/catlazy2-review/SKILL.md` through `skills/catlazy7-debt/SKILL.md` | Replace remaining `### 🧠 Analysis` references in strict-format text with `### 🔎 Inspection Summary`. |
| `README.md` | Mark Headroom as optional and state that the proxy processes only LLM API traffic routed through it. |

## Core changes

```diff
- Do NOT output any conversational text before the `### 🧠 Analysis` header.
+ Do NOT output any conversational text before the `### 🔎 Inspection Summary` header.

- ### 2. รัน Headroom Proxy (Transparent Proxy)
- บีบอัด Token อัตโนมัติด้วยการรัน Headroom ทิ้งไว้:
+ ### 2. ใช้ Headroom Proxy (ไม่บังคับ)
+ Proxy จะบีบอัดเฉพาะ LLM API traffic ที่ถูกตั้งค่าให้วิ่งผ่านมันเท่านั้น
```

## Verification

1. Search `skills/` to confirm no stale `### 🧠 Analysis` output requirement remains.
2. Confirm `scripts/` is absent.
3. Confirm README and `docs/integrations.md` describe the same Headroom boundary.
4. Run `git diff --check`.
