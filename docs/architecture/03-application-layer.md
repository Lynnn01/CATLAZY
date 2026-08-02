# 03 - Application Layer (Use Cases and Workflows)

## Role of the Application Layer

The Application layer coordinates a user-visible business outcome. It loads the required domain objects through ports, invokes domain behavior, persists the result, publishes events when appropriate, and returns an application result. It does not own the business invariants themselves.

## 1. CQRS (Command and Query Responsibility Segregation)

Commands change state and should express an intention, such as `PlaceOrder`. Queries read data and should not mutate state. They may use different models or storage paths when that simplifies the current requirement, but CQRS is not a reason to duplicate code without benefit.

## 2. Ports (Interfaces and Contracts)

Define ports in the inner layer for capabilities the use case needs: repositories, clocks, identity providers, payment gateways, or event publishers. Keep contracts small and business-oriented. Infrastructure implements them; the application depends only on the contract.

## 3. Pipeline Behaviors and Middleware

Cross-cutting application concerns such as authorization, validation, idempotency, transactions, logging, and metrics can run around use cases. Keep the pipeline explicit and ordered, and do not hide business rules inside generic middleware.

## Use-Case Shape

A use case should make its input, authorization context, output, and failure modes explicit. It should validate the request shape at the boundary, load only what it needs, invoke domain behavior, and commit one coherent outcome.

Avoid turning the Application layer into a second Domain layer. Business invariants belong to entities, value objects, aggregates, or explicit domain policies; the use case coordinates them.

## Transaction and Idempotency

Define the transaction boundary around the business outcome. Commands that may be retried should accept an idempotency key or use a domain-safe deduplication strategy. Queries should be observable and bounded, and they must not silently mutate state.