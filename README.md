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
fastapi-starter/
├── server/                    # 主应用目录
│   ├── core/                 # 核心组件
│   │   ├── config.py        # 配置管理
│   │   └── logger.py        # 日志配置
│   ├── routers/             # API路由模块
│   │   ├── items.py         # 项目相关路由
│   │   └── health.py        # 健康检查路由
│   ├── schemas/             # Pydantic 数据模型
│   │   └── item.py         # 项目数据模型
│   └── main.py             # FastAPI 应用入口
├── logs/                    # 日志目录
├── .cursor/                 # Cursor 配置
│   └── rules/              # 代码规则
├── pyproject.toml          # 项目元数据和依赖
├── uv.lock                 # 锁定的依赖版本
└── README.md               # 项目说明文档
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

### 3. 运行应用

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
uv run uvicorn server.main:app --host 0.0.0.0 --port 8000
```

### Docker 部署
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen

COPY . .

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📚 开发指南

### 添加新的API端点
1. 在 `server/schemas/` 中定义数据模型
2. 在 `server/routers/` 中创建路由和业务逻辑
3. 在 `server/main.py` 中注册路由
4. 在路由函数中直接处理所有逻辑

### 何时考虑架构升级
- 单个路由函数超过50行
- 出现大量重复代码
- 需要复杂的数据验证
- 团队成员增加
- 业务逻辑变得复杂

### 代码规范
- 遵循 Python PEP 8 规范
- 使用类型提示
- 实现完整的错误处理
- 编写清晰的文档字符串
- 保持函数简洁明了

---

🌿 **FastAPI Starter** - 基于渐进式架构的现代化FastAPI启动模板