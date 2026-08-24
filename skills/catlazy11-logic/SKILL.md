---
name: catlazy11-logic
description: Extract and formalize codebase logic into discrete mathematical logic specifications (DISMATH) and core libraries architecture
---

# Catlazy 11: Discrete Logic & Libraries Extraction Engine (DISMATH)

Formalize and extract business-agnostic coding patterns, algorithms, predicates, state transitions, safety invariants, and core libraries from a codebase into standardized, mathematically rigorous specifications powered by **DISMATH** (`docs/logics/dismath/`).

---

## 🎯 Purpose

Bridge the gap between raw implementation code and formal theoretical logic using a **strictly unified documentation format**:
1. **Unified Schema:** Every generated chapter must strictly adhere to the exact same 6-section structure.
2. **Mathematical Formalization:** Translate source code into propositional calculus, predicates ($\forall, \exists$), truth tables, and Hoare triples ($\{P\} S \{Q\}$).
3. **Core Libraries Ecosystem:** Extract and document dependencies in a dedicated chapter.
4. **Business Sanitization:** Decouple proprietary domain details, producing reusable, generic architectural logic patterns.

---

## 📐 Canonical File Formats & Schemas

All profiles created by `/catlazy11-logic` must consist of three standardized file formats:

---

### Template A: `00-overview.md` (Master Table of Contents & Profile Hub)

Every overview file must follow this exact 5-section schema:

```markdown
# Developer Coding DNA & Mathematical Logic Overview (`[profile-name]`)

## 1. Executive Summary & Philosophy
- Summary of the developer's core philosophies and invariants.

## 2. Theoretical Framework (DISMATH Alignment)
- How the codebase logic maps to the 10 DISMATH mathematical pillars.

## 3. Master Table of Contents
| Chapter | Document | Core Formal Topics | Mathematical Category |

## 4. Notation & Symbol Reference
- Table of mathematical symbols and logical connectives used.

## 5. Ecosystem & Library Summary
- Brief summary and link to the dedicated dependencies document.
```

---

### Template B: Chapter Files (`01` to `NN-1`) (Standard Chapter Schema)

Every domain/pattern chapter must follow this exact 6-section schema:

```markdown
# [Chapter Number]. [Topic Title] ([Formal Category])

## 1. Overview & Problem Statement
- Context, motivation, and problem solved by this logic pattern.

## 2. DISMATH Theoretical Foundation
- Theoretical pillars referenced from DISMATH (e.g. Predicates, Equivalences, State Machines, Hoare Logic).

## 3. Formal Mathematical Specifications
- LaTeX formulas, quantified propositions ($\forall, \exists$), state transition matrices ($\delta$), or Hoare triples ($\{P\} S \{Q\}$).

## 4. Invariants & Mathematical Proofs
- Formal proof (Direct, Contraposition, Contradiction, or Induction) guaranteeing safety and correctness.

## 5. Sanitized Generic Implementation
- Clean, synthetic TypeScript/JavaScript code snippet (zero proprietary organization data).

## 6. Complexity & Algebraic Properties
- Time/Space complexity ($O(1)$, $O(N)$) and algebraic properties (monotonicity, idempotence, bijectivity).
```

---

### Template C: `NN-dependencies-and-libraries.md` (Dedicated Ecosystem Schema)

The final chapter must follow this exact 5-section schema:

```markdown
# [Chapter Number]. Core Dependencies & Library Ecosystem (Libraries & Runtime Engine)

## 1. Overview & Problem Statement
- Architectural motivation for leveraging third-party libraries (Ladder of Laziness).

## 2. DISMATH Theoretical Foundation
- Theoretical and functional roles provided by the libraries.

## 3. Ecosystem & Dependency Matrix
| Library / Tool | Category | Primary Architectural Purpose | Mathematical & Logic Role |

## 4. Deep Dive by Library
- Detailed analysis: Purpose, Mathematical Role, and Minimal Code Pattern per library.

## 5. Dependency Selection Philosophy & Trade-offs
- Ladder of Laziness evaluation and decision rationale.
```

---

## 🔄 Execution Workflow

1. **Scan Codebase:** Extract domain logic, invariants, AST rules, and dependencies from `package.json` and source files.
2. **Formalize into DISMATH Equations:** Map each pattern to the 10 DISMATH pillars.
3. **Apply Canonical Templates:** Write `00-overview.md` (Template A), `01` to `NN-1` (Template B), and `NN-dependencies-and-libraries.md` (Template C).
4. **Sanitize Code:** Ensure $100\%$ synthetic, generic domain naming.
5. **Verify Uniformity:** Check that every file strictly implements its template headers and section numbering.
