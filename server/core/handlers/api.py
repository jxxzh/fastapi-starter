from fastapi import Request
from fastapi.responses import JSONResponse
from server.core.logger import logger
from server.schemas.api import APIError


async def api_exception_handler(request: Request, exc: APIError) -> JSONResponse:
    """
    全局 API 异常处理器
    """
    request_id = getattr(request.state, "request_id", "N/A")
    logger.error(
        f"API Exception: {exc.error_type.value} - {exc.message}",
        extra={"request_id": request_id},
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "data": None,
            "message": exc.message,
            "error": exc.error_type.value,  # 使用枚举值
            "request_id": request_id,
        },
    )
