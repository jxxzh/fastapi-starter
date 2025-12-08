# 🌿 FastAPI Starter

一个基于 FastAPI 的启动模板，采用简洁的架构设计，具备完整的错误处理、日志记录和监控能力。

## ✨ 项目特性

- 🚀 **高性能**：基于 FastAPI 和异步编程
- 🛡️ **完整错误处理**：全局异常处理器和输入验证
- 📝 **完整文档**：自动生成的 OpenAPI 文档
- 🏗️ **渐进式架构**：从简单开始，随项目复杂度逐步演进
- 🔍 **监控能力**：健康检查端点和结构化日志
- 📊 **开发友好**：热重载、详细日志、清晰的项目结构

## 📁 项目结构

```
├── server/                    # 主应用目录
│   ├── core/                  # 核心基础设施
│   │   ├── config.py          # 配置管理
│   │   ├── logger.py          # 日志配置
│   │   ├── exceptions/        # 统一异常体系（含 __init__.py, base.py 等）
│   │   ├── middlewares/       # 中间件（如 request_id, logging 等）
│   │   ├── handlers/          # 异常处理器（如 general_exception_handler 等）
│   │   ├── schemas/           # 基础 schema（如 APIResponseModel, APIError 等）
│   │   └── decorators/        # 装饰器（如 response_wrapper 等）
│   ├── modules/               # 功能模块（每个模块根据需要内含 router,schema,service等）
│   └── main.py                # 应用入口
├── logs/                      # 日志目录
├── pyproject.toml             # 项目元数据和依赖
├── uv.lock                    # 锁定的依赖版本
├── .env                       # 环境变量
├── .env.dev                   # 开发环境变量
├── .env.prod                  # 生产环境变量
├── AGENTS.md                  # AI 编码代理指南
└── README.md                  # 项目说明文档
```

### 目录化的异常、中间件和装饰器
- 每个功能点单独一个文件，便于维护和扩展
- 通过 `__init__.py` 统一导出常用内容，外部可直接 `from server.core.schemas import APIError`
- 推荐在 `__init__.py` 中使用 `__all__`，既规范导出又避免 Ruff F401 报错

```python
# 例如 server/core/decorators/__init__.py
from .response_wrapper import response_wrapper
__all__ = ["response_wrapper"]
```

## 🛠️ 安装和运行

本项目使用 [uv](https://github.com/astral-sh/uv) 进行依赖管理。

### 1. 安装依赖

```bash
uv sync
```

### 2. 环境配置（可选）

在项目根目录创建 `.env` 文件：

```env
# .env
APP_NAME="FastAPI Starter"
ADMIN_EMAIL="admin@example.com"
LOG_LEVEL="INFO"
LOG_FORMAT_JSON=true
```

### 3. 本地开发

```bash
uv run dev
```

服务器将在代码更改时自动重新启动。

### 4. 访问API

服务器运行后，可以通过以下地址访问：

- **应用首页**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📖 API 端点

### 根端点
- `GET /` - 应用欢迎页面

### 项目管理
- `GET /items/` - 获取所有项目列表
- `GET /items/{item_id}` - 根据ID获取单个项目
- `POST /items/` - 创建新项目

### 健康检查
- `GET /health/` - 健康检查端点

### 请求示例

#### 创建项目
```bash
curl -X POST "http://127.0.0.1:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "人参",
    "price": 88.5,
    "is_offer": true
  }'
```

#### 获取项目列表
```bash
curl "http://127.0.0.1:8000/items/"
```

#### 获取单个项目
```bash
curl "http://127.0.0.1:8000/items/1"
```

## 🏗️ 当前架构设计

### 错误处理
- **全局异常处理器**：统一处理HTTP异常和系统异常
- **输入验证**：使用Pydantic进行数据验证
- **详细日志记录**：所有操作都有相应的日志记录

### 数据处理
- **Pydantic模型**：确保数据类型安全
- **异步操作**：所有路由使用async/await

## 🔧 技术栈

- **FastAPI**: 现代、快速的 Web 框架
- **Pydantic**: 数据验证和序列化
- **Uvicorn**: ASGI 服务器
- **Loguru**: 结构化日志记录
- **UV**: 现代Python包管理工具

## 🚀 部署

### 生产环境运行
```bash
uv run start
```

### Docker 部署
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

COPY . .

EXPOSE 8000
CMD ["uv", "run", "start"]
```
