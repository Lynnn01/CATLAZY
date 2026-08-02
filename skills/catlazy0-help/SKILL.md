---
name: catlazy0-help
description: Quick reference for Catlazy levels, skills, and commands
---

# Catlazy Quick Reference

Display the one-shot quick reference for `catlazy`.

**Important:** this command only prints information. It must not change the mode, create flag files, or persist any setting.

### 🎚️ Intensity Levels

- **`/catlazy [lite|full|ultra|off]`:** change the AI’s laziness level. See `/catlazy` or `skills/catlazy/SKILL.md` for the full rules.
- **Incremental Decision Trail:** complex work proceeds one issue at a time through Observe → Decide → Plan → Apply → Verify → Continue; small work uses Plan → Apply → Verify.

### 🛠️ Commands

- **`/catlazy0-help`:** display this guide.
- **`/catlazy1-design`:** brainstorm before writing code for any work, including UI, UX, and bug fixes.
- **`/catlazy2-review`:** review the latest changes for over-engineering and rule violations.
- **`/catlazy3-architecture`:** check the code against Clean Architecture guidance in `docs/architecture/`.
- **`/catlazy4-interface`:** check UI against the design-token rules in `docs/design/user_interface/`.
- **`/catlazy5-experience`:** check UX usability and clarity of feedback using `docs/design/user_experience/`.
- **`/catlazy6-audit`:** audit the repository for over-engineering, with emphasis on reducing unnecessary code.
- **`/catlazy7-debt`:** collect `catlazy:` comments into the debt ledger.
- **`/catlazy8-agent`:** review and update project rules into a simpler, consistent structure.
- **`/catlazy9-compress`:** compress large logs or JSON before processing when that is useful for token efficiency.

### ⚙️ Stop and Configure

- **Stop:** type `stop catlazy`, `normal mode`, or `/catlazy off`.
- **Enable again:** type `/catlazy` at any time.
- **Default:** the initial level is `full`.
