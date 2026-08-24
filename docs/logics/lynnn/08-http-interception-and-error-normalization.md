# 08. การห่อหุ้ม Response และจัดการ Error ให้เป็นมาตรฐาน (HTTP Interception & Error Normalization)

หัวข้อนี้อธิบายถึงตรรกะการแปลง Response ให้มีโครงสร้าง Envelope ที่สม่ำเสมอ (`ResponsePatternInterceptor`), การป้องกันการห่อหุ้มซ้ำซ้อน (Idempotent Wrapping Guard), และการแปลง Error Messages ที่ซับซ้อนให้เข้าใจง่าย (`GlobalExceptionFilter`)

---

## 1. Idempotent Response Wrapping (`isPatternSuccess` Type Guard)

### แนวคิดและปัญหาที่แก้
เมื่อสร้าง Response Interceptor เพื่อห่อหุ้ม Payload ให้อยู่ในรูป `{ statusCode, message, data }` ปัญหาที่มักพบคือเมื่อ Controller คืนค่าโครงสร้างที่ถูกจัดรูปแบบมาแล้ว หรือเกิดการเรียก Interceptor ซ้ำ อาจทำให้เกิดการห่อหุ้มซ้อนกันหลายชั้น (เช่น `{ data: { data: ... } }`)

ผู้พัฒนาแก้ปัญหานี้ด้วย **Type Guard `isPatternSuccess`**:

```typescript
import {
  CallHandler,
  ExecutionContext,
  HttpStatus,
  Injectable,
  NestInterceptor,
} from '@nestjs/common';
import { Response } from 'express';
import { map, Observable } from 'rxjs';

export type ResponseBody = Record<string, unknown>;

type StandardSuccessResponse = {
  statusCode: number;
  message: string;
  data: unknown;
};

/**
 * Type Guard ตรวจสอบว่า Response ถูกจัด Format สำเร็จรูปแล้วหรือไม่ เพื่อป้องกันการ wrap ซ้ำ
 */
function isStandardSuccess(value: unknown): value is StandardSuccessResponse {
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
        // หากข้อมูลถูกจัดรูปแบบเป็น StandardSuccessResponse อยู่แล้ว ให้ส่งผ่านทันที (Idempotent)
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
```

---

## 2. Global Error Normalization & Message Unwrapping

### แนวคิดและปัญหาที่แก้
ข้อผิดพลาดที่เกิดขึ้นในระบบอาจมาจากหลายแหล่ง:
1. `HttpException` ทั่วไป (`NotFoundException`, `ForbiddenException`)
2. Validation Errors ซึ่งส่ง `message` ออกมาเป็น `string[]` (Array ของข้อความเตือน)
3. Unhandled Runtime Error ซึ่งไม่ใช่ `HttpException`

ผู้พัฒนาจึงสร้าง **Error Normalization Logic** ใน ExceptionFilter เพื่อแปลงข้อความทุกรูปแบบให้เป็น Format ที่สม่ำเสมอ:

```typescript
import {
  ArgumentsHost,
  Catch,
  ExceptionFilter,
  HttpException,
  HttpStatus,
  Logger,
} from '@nestjs/common';
import { Response } from 'express';

type StandardErrorBody = {
  statusCode: number;
  message: string;
  error: string | string[];
};

@Catch()
export class GlobalExceptionFilter implements ExceptionFilter {
  private readonly logger = new Logger(GlobalExceptionFilter.name);

  catch(exception: Error | HttpException | object, host: ArgumentsHost) {
    const response = host.switchToHttp().getResponse<Response>();
    const body = this.buildErrorBody(exception);

    // บันทึก Log เฉพาะข้อผิดพลาดระดับ Server Error (>= 500) เพื่อไม่ให้ Log บวม
    if (body.statusCode >= HttpStatus.INTERNAL_SERVER_ERROR) {
      this.logger.error(
        exception instanceof Error ? exception.message : 'Unknown server error',
        exception instanceof Error ? exception.stack : undefined,
      );
    }

    response.status(body.statusCode).json(body);
  }

  private buildErrorBody(exception: Error | HttpException | object): StandardErrorBody {
    // 1. จัดการ Unhandled Exception ทั่วไป
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

    // 2. Unpack Message: รวม Array ของ Validation Error ให้กลายเป็น Comma-Separated String
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
