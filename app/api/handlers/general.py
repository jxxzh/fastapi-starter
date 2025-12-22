from http import HTTPStatus

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.schemas.error import APIErrorType, APIException, APIExceptionResponse
from app.core.logger import logger


async def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    全局通用异常处理器
    """
    request_id = getattr(request.state, "request_id", "N/A")

    if isinstance(exc, RequestValidationError):
        # 格式化 Pydantic 校验错误信息
        error_details = []
        for error in exc.errors():
            loc = " -> ".join(str(i) for i in error["loc"])
            msg = error["msg"]
            error_details.append(f"{loc}: {msg}")
        detail = "参数校验失败: " + "; ".join(error_details)

        return APIExceptionResponse(
            exc=APIException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail=detail,
                error_type=APIErrorType.VALIDATION_ERROR,
            ),
            request_id=request_id,
        )

    if isinstance(exc, APIException):
        return APIExceptionResponse(
            exc=exc,
            request_id=request_id,
        )

    if isinstance(exc, HTTPException):
        return APIExceptionResponse(
            exc=APIException.from_http_exception(exc),
            request_id=request_id,
        )

    # 对于未捕获的未知异常，如果是调试模式，则抛出异常，让 FastAPI 显示详细的堆栈信息页面
    if request.app.debug:
        raise exc

    # 生产模式下，记录日志并返回统一的 500 错误响应
    logger.exception("Unhandled exception occurred", extra={"request_id": request_id})
    return APIExceptionResponse(
        exc=APIException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR),
        request_id=request_id,
    )
