# 01 - Unified Architecture Overview

## Introduction: Clean Architecture Meets Domain-Driven Design (DDD)

Unified Architecture combines Clean Architecture’s dependency boundaries with DDD’s business language and modeling tools. The goal is code that can change frameworks, storage, and interfaces without rewriting the business rules.

## Two Foundations

### 1. The Dependency Rule

Dependencies point from outer details toward inner policy. Domain code does not know about databases, HTTP frameworks, queues, or UI. Application code coordinates use cases through ports; infrastructure and presentation implement the outer details.

### 2. Ports and Adapters

A port is an interface owned by the inner layer that describes a capability it needs. An adapter implements that port for a database, external API, message broker, or user interface. This keeps replaceable technology at the boundary.

## Four Layers

1. **Domain:** entities, value objects, aggregates, domain events, and business invariants.
2. **Application:** use cases, commands, queries, orchestration, ports, and transaction boundaries.
3. **Infrastructure:** persistence, external clients, framework integrations, configuration, and concrete adapters.
4. **Presentation/Interface:** HTTP controllers, resolvers, DTOs, serialization, authentication entry points, and composition roots.

The allowed dependency direction is Presentation/Infrastructure → Application → Domain. Domain remains independent of all outer layers.

## Vertical Slicing and Modules

Organize code by business capability when that improves discovery and ownership. A feature may contain its application workflow, domain model, adapters, and tests while still respecting layer boundaries. Do not create empty layers or abstractions without a current reason.

## Proportional Architecture

Use the smallest architecture that protects a real boundary. A simple feature can use one use case and one adapter; a high-risk domain may need aggregates, events, policies, and stronger isolation. Complexity must be justified by a requirement, risk, or change seam—not by fashion.

## Practical Boundary Rules

- Domain imports must point inward only; a domain package should be testable without starting the web server or database.
- Application services may depend on domain types and ports, but not on concrete ORM, HTTP, or vendor SDK classes.
- Infrastructure and Presentation are replaceable outer details. Their code may depend on inner contracts, never the reverse.
- A boundary is useful only when it protects a real change, test seam, security boundary, or operational risk.

## Choosing a Slice

Start from a user or business capability, identify its use case, then place the invariant in the Domain and the technical integrations at the edge. Keep names in the business language used by the team. Add a new abstraction only when a second implementation, a test seam, or a clear policy boundary requires it.