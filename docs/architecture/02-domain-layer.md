# 02 - Domain Layer (Core Business Rules)

## Role of the Domain Layer

The Domain layer is the system’s most stable core. It owns business rules, invariants, and language that should remain valid regardless of UI, database, transport, or framework.

It must not import web frameworks, ORM entities, HTTP types, infrastructure services, or configuration details.

## DDD Building Blocks

### 1. Entities

An Entity has a stable identity and behavior that can change over time. Keep invariants inside the entity or a domain policy rather than scattering checks across controllers.

### 2. Aggregates and Aggregate Roots

An Aggregate is a consistency boundary. External code modifies it through the Aggregate Root, which protects invariants and controls access to child entities. Keep aggregates small enough to transact reliably.

### 3. Value Objects

A Value Object is defined by its values rather than identity. Make invalid states unrepresentable: validate at construction, keep the object immutable where practical, and expose behavior instead of raw primitive fields. Examples include `Money`, `EmailAddress`, and `DateRange`.

### 4. Domain Events

A Domain Event records a meaningful business fact that already happened, such as `OrderPlaced`. Events allow other workflows to react without coupling the core rule to a specific transport. Define stable names and payloads and publish only after the relevant transaction succeeds.

### 5. Domain Errors

Use domain-specific errors for violated invariants and expected business failures. They should be meaningful to the application layer without exposing persistence or HTTP concerns.

## Invariant Ownership

- Constructors and factories establish valid initial state.
- Methods that change state enforce the invariant before returning.
- Aggregate roots expose intentional operations instead of public mutable collections.
- Domain services are for rules that genuinely span multiple entities; do not create a service merely to move code out of an entity.

## Domain Independence Checklist

- No ORM annotations or persistence IDs that change business meaning.
- No HTTP status codes, request objects, framework decorators, or environment lookups.
- No direct network, file-system, clock, or random-number access without an application-provided port.
- Tests can exercise the rule with plain in-memory values and deterministic inputs.