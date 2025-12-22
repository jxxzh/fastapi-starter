from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.handlers import api_exception_handler, general_exception_handler
from app.api.main import api_router
from app.api.middlewares import LoggingMiddleware, RequestIDMiddleware
from app.api.schemas.error import APIError
from app.core.config import settings
from app.core.logger import setup_logger

# 初始化日志配置
setup_logger()


app = FastAPI()

# 添加中间件 - 注意顺序很重要！
# cors中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Request-ID"],
)

# 注意：FastAPI/Starlette 中间件是“后添加先执行”（最后 add 的在最外层）。
# 因此要让 RequestIDMiddleware 先执行并写入 request.state.request_id，
# 需要先添加 LoggingMiddleware，再添加 RequestIDMiddleware。
app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIDMiddleware)


# 添加异常处理器
app.add_exception_handler(APIError, api_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)


# 添加路由
app.include_router(api_router, prefix=settings.API_V1_STR)
