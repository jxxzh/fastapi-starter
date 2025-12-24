# 🌿 FastAPI Starter

一个基于 FastAPI 的启动模板，采用简洁的架构设计，具备完整的错误处理、日志记录和监控能力。

## 开发
- 启动开发服务：`uv run dev`
- 代码检查/格式化：`uv run lint`

## 集成测试（真实 MySQL + 固定测试库）

### 1) 准备测试环境变量
本项目会按顺序尝试加载 `env.testing` / `.env.testing`（以及 `.env` 等基础文件）。

- 复制示例文件：
  - `cp env.testing.example env.testing`
- 修改 `env.testing` 中的 MySQL 连接信息，并确保：
  - `ENV=testing`（由 `uv run test` 自动设置，但建议文件中也写清楚）
  - `DB_NAME` **包含** `_test`（例如 `fastapi_starter_test`）

### 2) 运行测试
- `uv run test`

说明：
- 测试启动时会执行**防误连硬校验**：`ENV=testing` 且 `DB_NAME` 必须包含 `_test`，否则测试会直接失败。
- 表结构会通过 Alembic 执行 `upgrade head` 初始化到最新版本。

### 3) 覆盖率报告（coverage）
测试执行时会自动生成覆盖率报告（不设阈值，不会因覆盖率低而失败）：
- **终端**：`term-missing`（显示未覆盖行）
- **HTML**：生成在 `htmlcov/` 目录
