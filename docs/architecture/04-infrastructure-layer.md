# 04 - Infrastructure Layer (Concrete Implementations)

## Role of the Infrastructure Layer

Infrastructure contains replaceable technical details: databases, message brokers, external services, file systems, framework integrations, and configuration. It implements ports owned by the Application or Domain boundary and translates between external data and internal models.

## 1. Adapters

An adapter converts a port’s contract to a concrete technology. Keep retries, timeouts, serialization, connection handling, and vendor-specific errors at this boundary. Do not leak SDK types into the Domain.

## 2. Repositories and Data Models

Repositories load and save aggregates through an application-facing contract. Persistence models may differ from domain models; map deliberately and preserve domain invariants. Keep query-specific read models separate when that is simpler than forcing every query through an aggregate.

## 3. External API Clients and Services

Wrap external clients behind narrow ports. Set explicit timeouts, validate responses, handle rate limits and transient failures, and record enough context to diagnose an outage without logging secrets.

## 4. Domain-Event Dispatching

Dispatch domain events at a reliable transaction boundary. If delivery is asynchronous, use an outbox or equivalent durable handoff where the failure risk justifies it. Make handlers idempotent and keep transport concerns out of the Domain layer.

## Failure Handling

- Set timeouts for every network call and classify errors as transient, permanent, or unknown.
- Retry only idempotent operations and use bounded backoff; do not multiply load during an outage.
- Validate external payloads before mapping them to trusted internal values.
- Keep secrets out of logs, error messages, and persisted telemetry.

## Persistence Discipline

The infrastructure adapter owns migrations, connection details, and vendor-specific query behavior. The application owns the meaning of a repository operation. Avoid leaking lazy ORM entities, query builders, or transaction objects beyond the adapter boundary.