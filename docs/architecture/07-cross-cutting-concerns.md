# 07 - Cross-Cutting Concerns

## 1. Trust Boundaries and Security

- Validate every request at its trust boundary. Client-side validation improves UX but never authorizes access or protects data.
- Authenticate the caller, authorize the use case, and enforce tenant or ownership filters before accessing data.
- Keep secrets out of source code and logs. Classify PII and redact it from diagnostics by default.
- Define a small error taxonomy: validation, authentication, authorization, not-found, conflict, transient dependency, and unexpected failure. Presentation maps these to safe user-facing responses.

## 2. Reliable External Work

- Every network call needs a timeout. Retry only transient failures and only when the operation is safe or idempotent.
- Give commands an idempotency key when duplicate delivery could create money movement, orders, or other irreversible effects.
- Do not publish an integration event directly from a database transaction. Use an outbox or equivalent atomic handoff, then deliver asynchronously.
- Treat public APIs and events as contracts: document owner, schema, version, compatibility policy, and failure/retry behavior.

## 3. Observability and Operations

- Emit structured logs with a correlation ID that flows through presentation, application, adapters, and events.
- Record metrics for request rate, failures, latency, queue/backlog, and dependency failures; add traces for cross-service paths when the system has them.
- Expose health/readiness checks without leaking secrets. Define a small production checklist: backups, migrations, alerts, access review, and rollback path.

## 4. Architectural Proportionality

The dependency rule applies at every size, but the amount of ceremony must match the problem. A small CRUD application may have few modules and thin domain behavior; a complex domain benefits from explicit value objects, ports, events, and module boundaries. Add a boundary only when it protects a real change, risk, or ownership boundary.

## References

- [Microsoft Learn: domain analysis for microservices](https://learn.microsoft.com/en-nz/azure/architecture/microservices/model/domain-analysis)
