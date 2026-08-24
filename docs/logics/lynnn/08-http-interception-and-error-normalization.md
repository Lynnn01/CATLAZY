# 08. HTTP Interception & Error Normalization (Monads & Idempotent Transformations)

## 1. Overview & Problem Statement
HTTP APIs often suffer from inconsistent envelope structures (e.g. inconsistent data wrapping) or catastrophic double-wrapping (`{ data: { data: ... } }`) when interceptors trigger on already-formatted responses. Furthermore, raw database and validation errors (arrays of strings) must be unwrapped into clean, normalized JSON responses without leaking internal stack traces for 4xx errors. This chapter formalizes idempotent response wrapping, Type-Guard projection, and global exception normalization.

## 2. DISMATH Theoretical Foundation
- **Idempotence & Monads (`02`):** Transformations where $f(f(x)) = f(x)$.
- **Custom Type-Guards as Invariant Indicators (`01`):** Deciding whether an arbitrary payload $x \in \mathcal{E}$.
- **String Projection Mappings (`03`):** Error unwrapping functions reducing arrays of validation messages into formatted comma-separated strings.

## 3. Formal Mathematical Specifications

### 3.1 Idempotent Response Envelope Monad ($\text{Wrap}$)
Let $\mathcal{U}$ be the arbitrary response payload universe and $\mathcal{E}$ be the standard envelope space:
$$\mathcal{E} = \{ \langle s, m, d \rangle \mid s \in \mathbb{N}, m \in \Sigma^*, d \in \mathcal{U} \}$$

We define the wrapping function $\text{Wrap}: \mathcal{U} \to \mathcal{E}$:
$$\text{Wrap}(x) = \begin{cases} x & \text{if } \text{IsStandardSuccess}(x) \\ \langle \text{statusCode}, \text{'Success'}, x \rangle & \text{otherwise} \end{cases}$$

- **Idempotence Property:**
  $$\forall x \in \mathcal{U}, \quad \text{Wrap}(\text{Wrap}(x)) = \text{Wrap}(x)$$

### 3.2 Error Normalization Projection ($\pi_{\text{err}}$)
Let $E$ be an arbitrary exception caught by the system. The normalization function $\pi_{\text{err}}(E)$ maps raw errors to a uniform envelope:
$$\pi_{\text{err}}(E) = \begin{cases} \langle 500, \text{'Internal Server Error'}, E.\text{message} \rangle & \text{if } E \notin \text{HttpException} \\ \langle E.\text{status}, \text{Join}(', ', E.\text{messages}), E.\text{error} \rangle & \text{if } E.\text{messages} \in \text{Array} \\ \langle E.\text{status}, E.\text{message}, E.\text{error} \rangle & \text{otherwise} \end{cases}$$

## 4. Invariants & Mathematical Proofs

### 4.1 No Double-Wrapping Invariant (Proof by Direct Deduction)
- **Theorem:** For any response payload $x$, applying the interceptor multiple times will never produce nested wrappers of the form $\{ \text{data}: \{ \text{data}: \dots \} \}$.
- **Proof:**
  1. Let $x_1 = \text{Wrap}(x_0)$.
  2. By definition of $\text{Wrap}$, $x_1$ has keys $\{\text{statusCode}: \text{number}, \text{message}: \text{string}, \text{data}: \text{any}\}$.
  3. The Type Guard $\text{IsStandardSuccess}(x_1)$ evaluates to $\text{True}$.
  4. In the second pass: $\text{Wrap}(x_1) = x_1$ because the guard branch directly returns $x_1$.
  5. By induction, $\text{Wrap}^k(x_0) = \text{Wrap}(x_0)$ for all $k \ge 1$. $\blacksquare$

## 5. Sanitized Generic Implementation

```typescript
import {
  ArgumentsHost,
  CallHandler,
  Catch,
  ExceptionFilter,
  ExecutionContext,
  HttpException,
  HttpStatus,
  Injectable,
  Logger,
  NestInterceptor,
} from '@nestjs/common';
import { Response } from 'express';
import { map, Observable } from 'rxjs';

export type StandardSuccessResponse = {
  statusCode: number;
  message: string;
  data: unknown;
};

/**
 * Type-Guard: Verifies if a response is already in standard format (Prevents nested wrapping)
 */
export function isStandardSuccess(value: unknown): value is StandardSuccessResponse {
  return (
    value !== null &&
    typeof value === 'object' &&
    'statusCode' in value &&
    typeof (value as StandardSuccessResponse).statusCode === 'number' &&
    'message' in value &&
    typeof (value as StandardSuccessResponse).message === 'string'
  );
}

@Injectable()
export class ResponsePatternInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<StandardSuccessResponse> {
    const response = context.switchToHttp().getResponse<Response | undefined>();

    return next.handle().pipe(
      map((body) => {
        // Idempotent Short-Circuit
        if (isStandardSuccess(body)) {
          return body;
        }

        const statusCode = response?.statusCode ?? HttpStatus.OK;
        return {
          statusCode,
          message: statusCode === HttpStatus.CREATED ? 'Created' : 'Success',
          data: body ?? null,
        };
      }),
    );
  }
}

@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
  private readonly logger = new Logger(GlobalExceptionFilter.name);

  catch(exception: Error | HttpException | object, host: ArgumentsHost) {
    const response = host.switchToHttp().getResponse<Response>();
    const body = this.buildErrorBody(exception);

    if (body.statusCode >= HttpStatus.INTERNAL_SERVER_ERROR) {
      this.logger.error(
        exception instanceof Error ? exception.message : 'Unknown server error',
        exception instanceof Error ? exception.stack : undefined,
      );
    }

    response.status(body.statusCode).json(body);
  }

  private buildErrorBody(exception: Error | HttpException | object) {
    if (!(exception instanceof HttpException)) {
      return {
        statusCode: HttpStatus.INTERNAL_SERVER_ERROR,
        message: 'Internal Server Error',
        error: exception instanceof Error ? exception.message : 'Unknown error',
      };
    }

    const status = exception.getStatus();
    const raw = exception.getResponse();

    if (typeof raw === 'string') {
      return { statusCode: status, message: raw, error: raw };
    }

    const record = raw as { message?: string | string[]; error?: string };
    const rawMessage = record.message;
    const message = Array.isArray(rawMessage)
      ? rawMessage.join(', ')
      : typeof rawMessage === 'string'
        ? rawMessage
        : 'An error occurred';

    return {
      statusCode: status,
      message,
      error: record.error ?? message,
    };
  }
}
```

## 6. Complexity & Algebraic Properties
- **Interception Overhead:** $O(1)$ evaluation time per HTTP request/response.
- **Idempotence Invariant:** Guarantees uniform API contract irrespective of controller return shape.
