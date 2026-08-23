# 06 - Best Practices (Unified Rules)

## Rules for Unified Architecture

### 1. Prefer Vertical Slices

Organize related code by business capability so a change is discoverable in one place. Keep the internal layer boundaries inside the slice; vertical slicing does not permit bypassing the Domain or Application rules.

### 2. Avoid an Anemic Domain Model

Put behavior and invariant protection near the data they govern. Do not turn entities into bags of setters while moving every rule into controllers or services.

### 3. Use Value Objects to Protect Invariants

Represent concepts such as money, email, identifiers, and ranges with validated types. Make illegal states unrepresentable and avoid repeating primitive validation at every call site.

### 4. Test Behavior

Prefer tests that describe observable business behavior over tests coupled to implementation details. Test domain invariants directly, application workflows through ports, and adapters with focused integration tests.

### 5. Do Not Share Module Data Directly

Modules communicate through explicit contracts, commands, queries, or events. Do not reach into another module’s tables or internal entities because it is convenient.

### 6. Enforce the Architecture

Use package boundaries, dependency checks, lint rules, code review, and focused tests to prevent forbidden imports and layer bypasses. Enforcement should be proportional to the project’s risk.

### 7. Test Coverage by Risk

Prioritize high-risk business rules, authorization, money movement, data loss, and critical workflows. Coverage percentage is a signal, not a substitute for testing the failure modes that matter.

### 8. Extract Reusable Logic Early (Reusable-First)

When introducing a new file or feature, proactively identify utilities, pure calculations, formatters, and common invariants. Place them in central shared folders (`shared/utils/`, `shared/domain/`, etc.) to prevent duplicate logic across modules while respecting layer boundaries.

## Review Questions

- Can a developer find the complete business capability without searching unrelated folders?
- Can the Domain be tested without a framework, network, or database?
- Are reusable functions extracted into central shared folders instead of duplicated across local feature folders?
- Does every cross-module interaction have an explicit contract?
- Is the chosen abstraction protecting a real boundary, or only anticipating a hypothetical feature?
- Are failures, authorization, and data-loss scenarios tested at the layer that owns them?

A passing architecture review is not a count of folders. It is evidence that dependencies point in the intended direction and that the most important rules have a clear owner.