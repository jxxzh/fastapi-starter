from fastapi import Request
from fastapi.responses import JSONResponse

from app.api.schemas.error import APIError
from app.api.schemas.response import APIResponseModel
from app.core.logger import logger


async def api_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    全局 API 异常处理器
    """
    if not isinstance(exc, APIError):
        raise exc
    request_id = getattr(request.state, "request_id", "N/A")
    logger.error(
        f"API Exception: {exc.error_type.value} - {exc.message}",
        extra={"request_id": request_id},
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponseModel[None](
            data=None,
            message=exc.message,
            error=exc.error_type.value,  # 使用枚举值
            request_id=request_id,
        ).model_dump(),
    )
