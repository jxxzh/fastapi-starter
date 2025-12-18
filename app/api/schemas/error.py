from enum import Enum
from http import HTTPStatus


class APIErrorType(Enum):
    """
    错误类型枚举
    用于规范化和标准化错误类型
    """

    # 客户端错误 (4xx)
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    CONFLICT = "CONFLICT"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    # 服务器错误 (5xx)
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    DATABASE_ERROR = "DATABASE_ERROR"
    # 业务错误
    ITEM_NOT_FOUND = "ITEM_NOT_FOUND"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    INVALID_INPUT = "INVALID_INPUT"
    DUPLICATE_ENTRY = "DUPLICATE_ENTRY"


class APIError(Exception):
    """
    API 异常基类
    所有自定义的业务异常都应继承自此类
    """

    status_code: int
    message: str
    error_type: APIErrorType

    def __init__(
        self,
        message: str = HTTPStatus.INTERNAL_SERVER_ERROR.description,
        status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR.value,
        error_type: APIErrorType = APIErrorType.INTERNAL_SERVER_ERROR,
    ):
        self.message = message
        self.status_code = status_code
        self.error_type = error_type
        super().__init__(message)
