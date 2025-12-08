# Project Context

## Purpose
- FastAPI 项目
- 保持代码简洁、可演进，适合作为中小型后端或 API 服务的起点

## Tech Stack

### 核心框架
- **FastAPI**: 现代、快速的 Web 框架，用于构建高性能 API
- **Uvicorn**: ASGI 服务器，支持异步操作
- **Pydantic V2**: 数据验证和设置管理，使用 Python 类型提示

### 开发工具
- **UV**: 现代 Python 包管理工具
- **Ruff**: 代码检查和格式化工具

## Project Conventions

### Code Style
- 偏好函数式/声明式风格，避免不必要的类；函数签名必须完整类型标注
- Ruff 负责 lint/format
- 公共导出在 `__init__.py` 使用 `__all__`，减少未使用导出警告
- 路由与服务优先使用 `async def`，Pydantic 模型用于输入/输出校验

### Architecture Patterns

#### 项目结构
```
server/
├── core/              # 核心基础设施
│   ├── config.py      # 配置管理（Pydantic Settings）
│   ├── logger.py      # 日志配置
│   ├── handlers/      # 异常处理器
│   ├── middlewares/   # 中间件（request_id, logging 等）
│   ├── decorators/    # 装饰器（response_wrapper 等）
│   └── schemas/       # 共享的数据模型
├── modules/           # 业务模块
│   └── {module_name}/ # 每个模块包含 router, schema, service 等
└── main.py            # 应用入口
```

#### 设计原则
- **模块化**: 每个功能模块独立，便于维护和扩展
- **关注点分离**: 核心基础设施、业务逻辑等分层清晰
- **单例模式**: 配置和模型实例使用单例模式，延迟初始化

#### 错误处理
- 全局异常处理器统一处理 HTTP 异常和系统异常
- 使用 Pydantic 进行输入验证
- 所有操作都有相应的日志记录

### Testing Strategy
- 当前项目未附带自动化测试

### Git Workflow
- 提交信息尽量语义化（feat/fix/chore 等），与变更内容一致

## Domain Context
- 通用后端/API 启动器，内置示例项管理与健康检查路由，可快速扩展为业务 API

## Important Constraints
- 必须使用 uv 进行依赖与脚本管理；仅在有充分理由时新增依赖
- 全局异步路由；保持高性能与可观测性（健康检查、结构化日志）
- 代码应保持简洁与可读性，避免过度抽象

## External Dependencies
- 目前无外部服务集成；仅使用开源库（FastAPI、Pydantic、Uvicorn、Loguru）
- 如接入外部 API/DB/队列，请在此登记用途、认证方式和故障策略
