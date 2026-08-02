---
name: catlazy6-audit
description: Audit the repository for over-engineering and deletion candidates
---
# Catlazy Repository Audit

Inspect the entire repository for dead code, duplication, unnecessary dependencies, stale configuration, and abstractions that do not protect a real boundary.

### ⚙️ Core Rules

1. Read repository rules and the relevant architecture/design docs first.
2. Search all references before recommending deletion or renaming.
3. Do not edit immediately; present findings and wait for approval.
4. Never recommend deleting security, accessibility, data-loss handling, tests, or required architecture layers merely to reduce line count.
5. Classify findings as deletion, consolidation, reuse, dependency removal, or intentional complexity.

### 🚨 STRICT OUTPUT FORMAT

Start with `### 🔎 Inspection Summary`, then show `### 📋 Audit Checklist` with `[PASS]`, `[FAIL]`, or `[N/A]` for dead code, duplication, dependencies, configuration, architecture, and risk. For every failure include file, evidence, impact, and the smallest safe action. Always show both sections and respond in the user’s language.
