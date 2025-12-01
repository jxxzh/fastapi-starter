# AGENTS.md

## 项目概述

这是一个基于 FastAPI 的现代化 Python Web 应用，采用渐进式架构设计，使用 uv 作为包管理工具，Pydantic v2 进行数据验证。

## 设置命令

- **安装依赖**: `uv sync`
- **启动开发服务器**: `uv run dev` （自动热重载）
- **生产环境运行**: `uv run prod`

## 项目结构

```
fastapi-starter/
├── server/                     # 主应用目录
│   ├── core/                   # 核心基础设施（包括基础配置、日志、异常处理、中间件等等）
│   ├── routers/                # API 路由模块
│   ├── schemas/                # Pydantic 数据模型
│   └── main.py                 # 应用入口
├── logs/                       # 日志目录
├── agent-docs/                 # 提供给AI编码智能体的文档集合，按需阅读
├── .env(.env.dev,.env.prod)    # 环境变量
├── pyproject.toml              # 项目配置
└── README.md                   # 项目说明文档
```

## Vibe Coding指南

- 如果需要更详细的指南，优先按需参考 `/agent-docs` 目录下的相关文档
- 如果vibe coding过程中需要编写文档，默认输出到 `/agent-docs` 目录下

## Python 代码风格和原则

### 核心原则

- **函数式编程**: 优先使用函数和模块化设计，避免不必要的类
- **声明式编程**: 优先使用声明式而非命令式编程风格
- **类型提示**: 所有函数签名必须包含完整的类型提示
- **代码复用**: 通过迭代和模块化避免代码重复

## FastAPI 应用规则

### 应用结构 (main.py)

- **函数式组件**: 使用纯函数和 Pydantic 模型进行输入验证和响应模式
- **声明式路由**: 使用清晰的返回类型注解定义路由
- **异常处理**: 使用 `HTTPException` 处理预期错误，并将其建模为特定的 HTTP 响应