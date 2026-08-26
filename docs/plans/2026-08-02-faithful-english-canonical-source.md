# Faithful English Canonical Source

## Goal

Translate the project’s canonical rules, skills, README, and reference documentation into English while preserving the original depth, structure, examples, checklists, and operational meaning.

## Source of truth

- Use the repository `HEAD` version as the reference for pre-existing Thai content.
- Preserve new, already-approved material added after `HEAD` where it is relevant.
- Keep historical plans untouched.

## Files

- `.rules/AGENTS.md`, `README.md`, `.env.example`, and `plugin.json` metadata.
- All source `SKILL.md` files under `skills/`.
- `docs/INDEX.md`, `docs/architecture/`, and `docs/design/`.

## Core constraints

- Translate; do not summarize or reduce requirements.
- Preserve file paths, command names, code identifiers, links, and examples unless a correction is needed.
- Retain the policy that the agent responds in the user’s language.
- Verify there is no Thai text in canonical source files, excluding historical plans, and verify the active review skill matches the repository source.
