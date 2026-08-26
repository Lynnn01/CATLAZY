# 2026-08-23: Reusable-First Architecture & Shared Module Standards

## Goal
Establish a canonical standard for creating reusable modules, utilities, and components in `docs/architecture/08-shared-and-reusable-modules.md`, and update all Catlazy skills, agent rules, and host configuration entrypoints to enforce "Reusable-First" across new feature development.

## Affected Files & Layers
- `docs/plans/2026-08-23-reusable-first-architecture-standards.md` [NEW]
- `docs/architecture/08-shared-and-reusable-modules.md` [NEW]
- `docs/INDEX.md` [MODIFY]
- `docs/architecture/01-architecture-overview.md` [MODIFY]
- `docs/architecture/06-best-practices.md` [MODIFY]
- `.rules/AGENTS.md` [MODIFY]
- `README.md` [MODIFY]
- `CLAUDE.md` [MODIFY]
- `.cursorrules` [MODIFY]
- `.windsurfrules` [MODIFY]
- `.github/copilot-instructions.md` [MODIFY]
- `.cursor/rules/catlazy.mdc` [MODIFY]
- `skills/catlazy0-help/SKILL.md` [MODIFY]
- `skills/catlazy1-design/SKILL.md` [MODIFY]
- `skills/catlazy2-review/SKILL.md` [MODIFY]
- `skills/catlazy3-architecture/SKILL.md` [MODIFY]
- `skills/catlazy6-audit/SKILL.md` [MODIFY]
- `skills/catlazy7-debt/SKILL.md` [MODIFY]

## Core Concepts
1. **Reusable-First on New Features:** When developing a new feature or creating a new file, identify any utility, calculation, formatter, validator, or common workflow that has foreseeable utility outside the current module, and extract it immediately into dedicated central shared locations.
2. **Layer-Aligned Shared Hierarchy:**
   - `shared/utils/` (Pure Utilities)
   - `shared/domain/` (Shared Kernel / Common Invariants)
   - `shared/application/` (Shared Use-Case Logic & Ports)
   - `shared/ui/` or `components/ui/` (Shared Presentation & Tokens)
   - `shared/infra/` (Shared Infrastructure & Client Instances)
3. **Decoupling and Zero Inward Leakage:** Code inside any `shared/` directory MUST NEVER import code from a feature-specific module.

## Decision Trail
- **Observe:** Redundant code and duplicated helper functions degrade maintainability and violate the Ladder of Laziness (Step 2: Reuse). Explicit architectural standards for shared central modules ensure agents and developers proactively place reusable logic in the right layer.
- **Decide:** Add `08-shared-and-reusable-modules.md` and propagate the Reusable-First policy across the entire Catlazy ecosystem.
- **Plan & Apply:** Author the architecture document, update rules, update all affected skills, sync multi-agent config files, and verify with `/catlazy3-architecture`.
