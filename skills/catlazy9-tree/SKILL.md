---
name: catlazy9-tree
description: Scan project directory structure and report an annotated folder tree with purpose descriptions
---
# Catlazy Directory Tree & Purpose Explainer

When invoked with `/catlazy9-tree`, recursively inspect the project directory structure, construct an annotated ASCII tree, and report the architectural role and purpose description of each folder.

### ⚙️ Core Rules

1. **Read-only discovery:** this skill only inspects directories and files; it does not modify project code.
2. **Standard exclusions:** automatically ignore version control, build caches, and package dependencies (`.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`, `.coverage`, `.turbo`, `.next`).
3. **Architectural layer alignment:** classify directories into standard Clean Architecture / DDD layers according to `docs/architecture/` (Domain, Application, Infrastructure, Presentation, Shared, Config, Docs, Tools, Tests).
4. **Concrete descriptions:** summarize the exact responsibility of each directory based on its contents, exported modules, and naming conventions. Avoid vague generic descriptions.
5. **Structural health check:** detect anti-patterns using standard finding tags:
   - `[tree-empty-dir]`: empty folder containing no tracked files or code.
   - `[tree-deep-nesting]`: folder nesting depth exceeds 5 levels.
   - `[tree-layer-leakage]`: folder naming or placement violates Clean Architecture layer boundaries.
   - `[tree-unshared]`: duplicate local utility folders that should be consolidated into central `shared/`.

### Standards Resolution

Resolve `docs/architecture/` in this order before mapping:

1. Use the target repository’s `docs/architecture/` when it exists.
2. Otherwise, use the canonical `docs/architecture/` directory in the installed Catlazy bundle, beside its `skills/` directory.
3. State whether target repository or bundled fallback standards were used in the Inspection Summary.

### Task Context and Arguments

Accept standardized input arguments:
```text
catlazy9-tree [report] [--scope <path>] [--depth <N>]
              [--base <commit-or-ref>] [--files <path,...>]
              [--format normal|strict] [--language <code>]
```

Resolve values in strict precedence order: explicit arguments, optional `.catlazy/task.json`, then user-named files.
- `--scope <path>`: restrict directory scan to a specific subtree (default: project root).
- `--depth <N>`: limit recursive depth (default: 4 levels).
- `--format normal|strict`: `normal` displays the annotated tree and summary table; `strict` adds comprehensive file counts, layer invariant checks, and structural health metrics.

### 🚨 STRICT OUTPUT FORMAT (CRITICAL)

Follow this exact structure. Do not output conversational text before the `### 🔎 Inspection Summary` heading. Respond in the user's language unless another language is requested.

### 🔎 Inspection Summary

- **Target / Scope:** root path, scan depth, and resolved folder count.
- **Standards Source:** state whether target repository (`docs/architecture/`) or bundled fallback standards were used.
- **Observation:** concise executive summary of project layout, architectural style (Clean Architecture, DDD, NestJS, Monorepo, etc.), and modularity.

### 📋 Inspection Checklist

- `[PASS]` / `[FAIL]` / `[N/A]` `[tree-structure]` (Directory hierarchy analysis)
- `[PASS]` / `[FAIL]` / `[N/A]` `[layer-classification]` (Architectural layer tagging)
- `[PASS]` / `[FAIL]` / `[N/A]` `[structural-health]` (Empty dirs, deep nesting, naming consistency)

#### 1. 🌳 Directory Tree

```text
<project-root>/
├── <dir-1>/             # [Layer] Short description
│   ├── <sub-dir-1>/     # [Layer] Short description
│   └── <sub-dir-2>/     # [Layer] Short description
└── <dir-2>/             # [Layer] Short description
```

#### 2. 📂 Directory Purpose & Architecture Matrix

| Directory Path | Architectural Layer | Primary Responsibility & Contents |
| :--- | :--- | :--- |
| `src/domain/` | Domain | Core business entities, value objects, and domain invariants |
| `src/application/` | Application | Use cases, command/query handlers, and port interfaces |
| `src/infrastructure/` | Infrastructure | Persistence adapters, external API clients, database drivers |
| `src/presentation/` | Presentation | HTTP controllers, UI components, resolvers, DTOs |
| `src/shared/` | Shared Kernel | Reusable pure utilities, cross-cutting helpers, design tokens |

#### 3. 🏥 Structural Findings & Health Analysis

If any directory anomalies are found:
- **Target:** `[directory/path]`
- **Tag & Rule:** `[tree-*]` (citing the violated structural guideline)
- **Evidence:** observed issue (e.g. empty directory with no tracked files, nesting depth > 5)
- **Smallest Fix:** recommended action (delete unused folder, consolidate shared utilities)

### 🐈 Catlazy Finish Check

- **Scope & Safety:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Validation & Freshness:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Diff & Side-effects:** `[PASS]` / `[FAIL]` / `[N/A]`
- **Verdict:** Output **“Directory tree mapped and documented successfully.”**
- **Status:** Conclude with exactly one status: `CATLAZY_DONE`, `CATLAZY_BLOCKED: <reason>`, or `CATLAZY_UNVERIFIED: <missing check>`.
