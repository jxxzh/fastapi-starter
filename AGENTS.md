<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# AGENTS instructions

## Project Knowledge

### Development Environment
- Use `uv` as the package manager.
  - dev server: `uv run fastapi dev`
  - prod server: `uv run fastapi start`
- Use `ruff` as the linter and formatter.
  - lint: `uv run ruff check --fix`
  - format: `uv run ruff format`

### Core Stack
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.14+
- Pydantic V2: Data validation and settings management using Python type hints

### Project Architecture

Organize code by functionality instead of file types, keeping code highly cohesive.

```
├── app/                       # 主应用目录
│   ├── core/                  # 核心基础设施
│   ├── routes/                # 路由模块（每个模块根据需要内含 router,schema,service等）
│   └── main.py                # 应用入口
├── logs/                      # 日志目录
├── pyproject.toml             # 项目元数据和依赖
├── uv.lock                    # 锁定的依赖版本
├── .env(.dev,.prod)           # 环境变量
├── AGENTS.md                  # AI 编码代理指南
└── README.md                  # 项目说明文档
```

### Code Style
- **Functional Programming**: Prefer functional programming over object-oriented programming
- **Declarative Programming**: Prefer declarative programming over imperative programming
- **Type Hints**: All function signatures must include complete type hints
- **Code Reusability**: Avoid code duplication through iteration and modularization
