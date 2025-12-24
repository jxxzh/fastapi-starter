## Context
项目当前没有自动化测试与测试入口；同时应用配置与数据库引擎在 import 时初始化（`app/core/config.py`、`app/core/db.py`），会导致测试环境需要明确的配置与 DB 隔离策略。

现有 API 关键路径主要集中在：
- `/api/v1/auth/access-token`：用户名/密码校验与 JWT 生成
- `/api/v1/user/me`：OAuth2 Bearer token 解析、用户查询与权限校验
- 全局异常处理：`APIExceptionResponse` 将错误统一包装为 `APIResponseModel`

## Goals / Non-Goals
- Goals:
  - 提供一条命令可运行的集成测试入口（本地与 CI 都可用）
  - 复用同一开发环境的真实 MySQL Server，通过独立测试库验证 FastAPI 路由的真实请求/响应行为
  - DB 相关逻辑可在测试中可控、可隔离
- Non-Goals:
  - 默认不引入真实 MySQL 容器；不把“迁移脚本正确性”作为本次验收项

## Decisions
### Decision: 使用 pytest + httpx（ASGITransport）进行 in-process 集成测试
- **Why**：不需要启动独立服务进程，速度快；能覆盖 FastAPI 依赖注入、中间件、异常处理等真实链路。
- **How**：使用 `httpx.AsyncClient(transport=ASGITransport(app=...))` 对 `app` 发起请求。

### Decision: 使用 FastAPI dependency override 替换 `get_db`，绑定测试专用 Session/Engine
- **Why**：`SessionDep = Depends(get_db)` 已是项目的 DB 注入入口；override 侵入小且与业务代码解耦。
- **How**：
  - 在 `tests/conftest.py` 创建指向 **固定独立测试库** 的 MySQL engine（例如 `DB_NAME=fastapi_starter_test`）
  - 通过 `SQLModel.metadata.create_all(test_engine)` 或 Alembic 迁移初始化表结构（实现阶段二选一，优先贴近生产可选用 Alembic）
  - 覆盖 `app.api.deps.get_db` 返回测试 Session

### Decision: 测试数据使用服务层创建（create_user/authenticate），避免直接写 SQL
- **Why**：测试更贴近业务规则（如密码哈希），减少重复实现与漂移风险。

## Risks / Trade-offs
- **配置耦合风险**：应用在 import 时读取 settings，若缺少测试环境变量会导致测试启动失败。
  - Mitigation：在测试运行前明确设置 `ENV=testing`，并提供 `.env.testing`（或在实现阶段调整 settings 的 testing 默认值策略）。
- **误连开发库风险**：复用同一 MySQL Server 时，若配置错误可能写入开发库。
  - Mitigation：测试启动时做硬校验（例如 `ENV=testing` 且 `DB_NAME` 必须包含 `_test`），不满足直接 fail；建议使用测试专用账号并限制其仅能访问测试库。

## Migration Plan（实现阶段）
- 为测试新增 `ENV=testing` 的最小可运行配置（推荐 `.env.testing`），并将 `DB_NAME` 指向固定测试库（例如 `*_test`）。
- 增加 `uv run test` 与 `tests/` 目录，逐步扩展用例覆盖。

## Open Questions
- 是否需要在 CI 中固定跑 MySQL 集成测试？若需要，可使用 CI service/container，并复用同样的“固定测试库”策略。


