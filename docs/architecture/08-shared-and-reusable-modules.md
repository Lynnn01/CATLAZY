# 08 - Shared and Reusable Modules

## 1. The Reusable-First Principle

When developing a new feature or creating a new file, identify any utility, calculation, formatter, validator, or common workflow that has foreseeable utility outside the current module.

**Core Rule:** Extract reusable functions immediately into dedicated central shared locations rather than inlining them inside feature-specific files.

## 2. Central Shared Hierarchy & Layer Alignment

Place reusable code in central shared folders aligned with Clean Architecture layers:

```text
src/ (or lib/)
├── shared/ (or core/)
│   ├── utils/          # Pure functions, math/date helpers, formatters (Zero dependencies)
│   ├── domain/         # Shared Kernel: Value Objects, Base Entities, Domain Events
│   ├── application/    # Shared DTOs, Use-Case helpers, Common Ports & Interfaces
│   ├── ui/             # Reusable UI Primitives, Design Tokens, Shared Layouts
│   └── infra/          # Generic HTTP clients, Storage wrappers, Cache adapters
└── features/           # Vertical slices / domain-specific feature modules
```

### Layer Classification Guide

1. **`shared/utils/` (Pure Utilities):**
   - Pure functions, string manipulation, date math, number formatters, cryptographic helpers.
   - Must have zero framework or domain dependencies and no side effects.
2. **`shared/domain/` (Shared Kernel):**
   - Shared Value Objects (e.g. `Money`, `Email`, `UUID`), common domain events, base entities, universal business invariants.
3. **`shared/application/` (Shared Use-Case Logic):**
   - Cross-feature application ports, common orchestration helpers, pagination/sorting contracts, shared DTOs.
4. **`shared/ui/` or `components/ui/` (Shared Presentation):**
   - Atomic UI primitives (Buttons, Inputs, Dialogs), design tokens, shared layout wrappers.
5. **`shared/infra/` (Shared Infrastructure):**
   - Base HTTP client instances, caching adapters, metric emitters, database connection pools.

## 3. Strict Boundary & Decoupling Rules

- **Zero Inward Leakage:** Code inside any `shared/` directory MUST NEVER import code from a feature-specific or local module (`shared/` → `features/` is strictly forbidden).
- **Single Source of Truth:** Never copy-paste duplicate helper functions across feature files.
- **Tree-Shakeable Exports:** Export functions explicitly to allow bundlers to prune unused helpers. Avoid giant monolithic barrel files (`index.ts`) that pull in unnecessary dependencies.
- **Language Agnostic:** This structure applies across languages (TypeScript, Python, Go, Rust, C#).

## 4. Temporary Inline Deferrals (Catlazy Debt)

If an inline helper cannot be immediately extracted due to tight constraints, mark it explicitly with a technical debt comment:

```typescript
// catlazy: inline helper | ceiling: 1 caller | upgrade: extract to shared/utils on 2nd caller
```

Catlazy skills (such as `/catlazy7-debt` and `/catlazy3-architecture`) will track this debt and enforce extraction when a second caller is introduced.
