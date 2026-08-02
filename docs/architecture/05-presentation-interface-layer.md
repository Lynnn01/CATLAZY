# 05 - Presentation / Interface Layer (The Gateway)

## Role of the Presentation Layer

Presentation translates external input into an application request and translates the result into a protocol response. It owns transport concerns, not business policy.

## 1. Controllers, Resolvers, and Endpoints

Keep endpoints thin: authenticate the request, validate its shape, map it to a command or query, invoke the application service, and map the result to a response. Do not call repositories or domain internals directly from a controller.

## 2. DTOs (Data Transfer Objects)

Use explicit request and response DTOs at the boundary. Validate untrusted input, avoid exposing persistence models, and version or deprecate contracts deliberately. DTO mapping should not silently change domain meaning.

## 3. Global Exception Handling

Map known domain and application errors to stable client-safe responses. Hide stack traces and infrastructure details from users, while logging diagnostic context with correlation IDs. Unknown failures should produce a safe generic error and an observable server-side record.

## 4. Composition Root

The composition root is the one place where concrete adapters, configuration, dependency injection, and application services are assembled. Keep wiring explicit and keep framework setup at the outer boundary.

## Boundary Checklist

- Validate syntax, size, authentication, and authorization before invoking a use case.
- Map only allowed fields into a command or query; never pass an untrusted request object through blindly.
- Return stable status codes and response shapes for known failures.
- Add correlation or request IDs so an external error can be connected to server-side diagnostics.

Presentation should not contain pricing rules, aggregate invariants, repository queries, or vendor-specific retry logic. Those concerns belong in the inner policy or the infrastructure adapter.