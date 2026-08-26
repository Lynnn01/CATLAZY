# Documentation Index

Welcome to the development guidance hub. Documentation is organized into three main areas: **Architecture**, **Design**, and **Logics**.

## 🏗️ 1. Software Architecture

Folder: `architecture/`

These guides combine Clean Architecture and Domain-Driven Design (DDD) to keep code resilient to change and maintainable.

| File | Main coverage |
|---|---|
| [01-architecture-overview.md](./architecture/01-architecture-overview.md) | Clean Architecture & DDD foundations, Dependency Rule, 4 layers |
| [02-domain-layer.md](./architecture/02-domain-layer.md) | Entities, Value Objects, Aggregates, Domain Events, Invariants |
| [03-application-layer.md](./architecture/03-application-layer.md) | Use cases, Commands, Queries, Ports, Transaction Boundaries |
| [04-infrastructure-layer.md](./architecture/04-infrastructure-layer.md) | Persistence, Adapters, External APIs, Concrete Clients |
| [05-presentation-interface-layer.md](./architecture/05-presentation-interface-layer.md) | HTTP Controllers, Resolvers, DTOs, Serialization |
| [06-best-practices.md](./architecture/06-best-practices.md) | Dependency Injection, Composition Roots, Testing Strategies |
| [07-cross-cutting-concerns.md](./architecture/07-cross-cutting-concerns.md) | Security, Reliability, Observability, Cross-layer Concerns |
| [08-shared-and-reusable-modules.md](./architecture/08-shared-and-reusable-modules.md) | Reusable-First, Central Shared Folders, Layer Hierarchy, Decoupling |

## 🎨 2. Design

Folder: `design/`

Design is split into two complementary disciplines:

- [User Interface](./design/user_interface/INDEX.md): visual tokens, layout, components, and interaction states.
- [User Experience](./design/user_experience/INDEX.md): information architecture, feedback, performance, accessibility, and validation.

## 🧠 3. Developer Logics & Patterns

Folder: `logics/`

Documentation of coding DNA, domain algorithms, mathematical modeling, defensive invariants, and developer-specific reasoning patterns:

| Profile | Main coverage |
|---|---|
| [dismath/](./logics/dismath/00-overview.md) | Discrete Mathematics logic curriculum (Kenneth Rosen): Propositional logic, Equivalences, Predicates, Quantifiers, Rules of Inference, Proof Methods, Mathematical Induction, and Hoare Logic Program Correctness |



