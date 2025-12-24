# Change: 集成测试能力（pytest + httpx）

## Why
当前项目未附带自动化测试，API 与数据库相关改动缺少回归保障，导致：
- 迭代时难以及时发现登录鉴权、依赖注入、错误响应格式等关键路径的回归
- 新同学/CI 环境缺少“一条命令可验证”的质量门槛

本变更目标是提供**最小、可重复、默认使用真实 MySQL + 固定独立测试库（同一开发环境）** 的集成测试能力，用于验证 API 的真实请求/响应行为，并尽量贴近生产数据库特性。

## What Changes
- 新增测试依赖与运行入口：提供 `uv run test` 一键运行集成测试。
- 新增集成测试脚手架：在进程内启动 FastAPI ASGI 应用，通过 `httpx` 发起真实 HTTP 请求（ASGITransport）。
- 提供测试数据库隔离：复用本地/开发环境 MySQL Server，但使用**固定独立测试库**（例如 `*_test`），并通过 FastAPI dependency override 将 `get_db` 指向测试专用 `Session`，避免污染开发库。
- 提供防误连保护：测试启动时对配置进行硬校验（例如 `ENV=testing` 且 `DB_NAME` 必须包含 `_test`），不满足则直接失败。
- 集成覆盖率报告：运行测试时输出覆盖率报告（终端 + HTML），不强制阈值、不因覆盖率低失败。
- 新增首批集成测试用例：
  - `/api/v1/auth/access-token`：成功获取 token、错误密码返回标准错误响应
  - `/api/v1/user/me`：未携带 token 的拒绝访问、携带 token 正常返回当前用户
- 补充文档：README 中增加如何运行测试、如何配置 testing 环境。

## Impact
- Affected specs:
  - 新增 capability：`integration-tests`
- Affected code (implementation stage):
  - `pyproject.toml`（新增测试依赖组与 pytest 配置）
  - `scripts/commands.py`（新增 test 命令入口）
  - `app/api/deps.py`（测试阶段会通过 dependency override 替换 `get_db`）
  - `app/core/config.py`（可能需要明确/补充 testing 环境的最小配置策略）
  - 新增 `tests/` 目录与用例文件
  - 覆盖率配置（`pytest-cov`/`tool.coverage.*`）

## Non-Goals
- 不在本次变更中引入容器化 MySQL（例如 Testcontainers）作为默认路径（可作为后续增强/CI 方案）。
- 不在本次变更中覆盖全部路由与所有错误分支，只提供关键路径的基线用例。

## Open Questions
- （暂无）


