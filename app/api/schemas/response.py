from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class APIResponseModel(BaseModel, Generic[T]):
    """
    统一 API 响应体模型
    """

    data: T | None = Field(None, description="成功时返回的数据")
    message: str = Field("操作成功", description="接口操作结果的说明")
    error: str | None = Field(None, description="错误类型枚举值，仅在失败时返回")
    request_id: str = Field(..., description="请求的唯一标识符，用于链路追踪")
