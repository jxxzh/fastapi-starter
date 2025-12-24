## 1. 测试依赖与命令入口
- [x] 1.1 在 `pyproject.toml` 新增 `dependency-groups.test`：`pytest`、`pytest-asyncio`、`httpx`（以及必要的 ASGI 测试依赖）
- [x] 1.2 在 `scripts/commands.py` 新增 `test()` 命令，提供 `uv run test` 入口（并在 `pyproject.toml` 注册脚本）
- [x] 1.3 增加 pytest 配置（例如 `pyproject.toml` 的 `tool.pytest.ini_options`），确保 asyncio 测试可用（例如 `asyncio_mode=auto`）
- [x] 1.4 集成覆盖率报告（pytest-cov）：默认输出终端报告与 HTML（不设置阈值）

## 2. testing 环境与数据库隔离
- [x] 2.1 明确 `ENV=testing` 的最小配置策略（优先：新增 `.env.testing`；备选：调整 `Settings` 在 testing 下的默认值/校验策略）
- [x] 2.2 新增 `tests/conftest.py`：
  - 创建测试专用 MySQL engine（复用同一 MySQL Server，但 `DB_NAME` 指向固定测试库，例如 `*_test`）
  - 测试启动前做防误连硬校验（例如 `ENV=testing` 且 `DB_NAME` 必须包含 `_test`）
  - 初始化表结构（实现阶段二选一）：
    - 方案 A（更快）：`SQLModel.metadata.create_all(...)`
    - 方案 B（更贴近生产）：通过 Alembic 迁移到 head
  - 使用 FastAPI dependency override 覆盖 `app.api.deps.get_db`
  - 提供 `client` fixture（`httpx.AsyncClient`）

## 3. 首批集成测试用例（可验证）
- [x] 3.1 `POST /api/v1/auth/access-token`：正确账号密码返回 `access_token`
- [x] 3.2 `POST /api/v1/auth/access-token`：错误密码返回 `400` 且响应体符合 `APIResponseModel` 错误结构
- [x] 3.3 `GET /api/v1/user/me`：无 token 返回 `401`（或对应框架行为）且响应体为标准错误结构
- [x] 3.4 `GET /api/v1/user/me`：携带 token 返回当前用户（至少包含 `email/is_active/is_superuser/id` 等字段）
- [x] 3.5 断言 `X-Request-ID` 响应头存在（验证中间件链路）

## 4. 文档与验证
- [x] 4.1 `README.md` 增加“如何运行集成测试”“如何配置 testing 环境”
- [x] 4.2 更新 `openspec/project.md` 的 Testing Strategy（从“未附带”更新为“已提供集成测试基线”）
- [x] 4.3 本地验证：`uv run test` 通过；并在本地 MySQL 可用（同一开发环境）情况下可运行


