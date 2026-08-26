# Implementation Plan: Incremental Decision Trail

## Goal

Add a concise, evidence-based workflow that lets an agent solve one problem at a time without requiring private chain-of-thought or making simple tasks unnecessarily heavy.

## Affected files

| File | Change |
|---|---|
| `.rules/AGENTS.md` | Add the global Incremental Decision Trail rule, its six stages, and when it may be shortened. |
| `skills/catlazy1-design/SKILL.md` | Make the plan artifact capture Observation, Decision, Planned Action, and Verification for complex or risky work. |
| `skills/catlazy2-review/SKILL.md` | Define the same four concise headings for review output so review results can become the next repair loop. |
| `skills/catlazy0-help/SKILL.md` | Add one-line guidance explaining when the incremental workflow applies. |
| `README.md` | Add a short workflow example so plugin users understand the behavior. |

## Core changes

```diff
+ **Incremental Decision Trail:** For complex, ambiguous, or multi-file work,
+ progress through one issue at a time: Observe → Decide → Plan → Apply → Verify → Continue.
+ Show concise evidence and the selected action, never private chain-of-thought.
+ For a small, clear change, use only Plan → Apply → Verify.
```

```md
### 🔎 Observation
- Evidence from the repository or user request

### 🎯 Decision
- One issue and the smallest safe action

### 🛠️ Planned Action
- Files and bounded change

### ✅ Verification
- The relevant search, test, or diff check
```

## Verification status

- Existing planning gate, inspection-summary headings, and review format were read.
- The change is documentation/skill behavior only; no runtime code, dependency, credential, or UI changes are involved.

## Verification after implementation

1. Search the changed rules and skills to ensure the four headings are identical.
2. Confirm the short-path exception appears in the rule and planning skill.
3. Run `git diff --check`.
