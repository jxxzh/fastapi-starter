# Project Context

## Purpose
- FastAPI + SQLModel 项目
- 保持代码简洁、可演进，适合作为中小型后端或 API 服务的起点

## Tech Stack

### 核心框架
- **FastAPI**: 现代、快速的 Web 框架，用于构建高性能 API
- **Pydantic V2**: 数据验证和设置管理，使用 Python 类型提示
- **SQLModel**: 数据库 ORM，使用 Python 类型提示
- **Alembic**: 数据库迁移工具

### 开发工具
- **UV**: 现代 Python 包管理工具
- **Ruff**: 代码检查和格式化工具
- **Mypy**: 静态类型检查工具
- **Loguru**: 日志记录工具
- **Pytest**: 单元测试框架

## Project Conventions

### Code Style
- 偏好函数式/声明式风格，避免不必要的类
- 函数签名必须完整类型标注
- 路由与服务优先使用 `async def`，Pydantic 模型用于输入/输出校验

### Architecture Patterns

#### 项目结构
```
├── app/                       # 主应用目录
│   ├── core/                  # 核心基础设施
│   │   ├── config.py          # 配置管理（Pydantic Settings）
│   │   ├── logger.py          # 日志配置 (Loguru)
│   │   ├── db.py              # 数据库配置 (SQLModel)
│   │   └── models.py          # SQLModel 模型注册入口（用于 Alembic autogenerate）
│   ├── api/                   # API 路由
│   │   ├── routes/            # 路由（按功能组织，每个模块包含 router, schema, service 等）
│   │   └── main.py            # API 路由入口
│   └── main.py                # 主应用入口
├── scripts/                   # 脚本目录
├── alembic/                   # Alembic 迁移目录
├── pyproject.toml             # 项目元数据和依赖
├── .env(.development,.production,.testing)           # 环境变量
├── AGENTS.md                  # AI 编码代理指南
└── README.md                  # 项目说明文档
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
- 已提供集成测试基线：使用 `uv run test` 运行，默认复用真实 MySQL 并连接固定独立测试库（`DB_NAME` 包含 `_test`），表结构通过 Alembic 迁移到 head 初始化。

### Git Workflow
- 提交信息尽量语义化（feat/fix/chore 等），与变更内容一致

## Domain Context
- 通用后端/API 启动器，内置示例项管理与健康检查路由，可快速扩展为业务 API

## Important Constraints
- 必须使用 uv 进行依赖与脚本管理；仅在有充分理由时新增依赖
- 全局异步路由；保持高性能与可观测性
- 代码应保持简洁与可读性，避免过度抽象

## External Dependencies
- Database: SQLModel + Alembic + MySQL
- Testing: pytest + httpx + pytest-asyncio + pytest-cov
