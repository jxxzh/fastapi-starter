# integration-tests Specification

## Purpose
TBD - created by archiving change add-integration-tests. Update Purpose after archive.
## Requirements
### Requirement: 集成测试运行入口
系统 MUST 提供可重复执行的集成测试运行入口，用于在本地与 CI 环境验证 API 行为。

#### Scenario: 通过单一命令运行测试
- **WHEN** 开发者运行 `uv run test`
- **THEN** 测试套件被执行并以退出码表示通过/失败

### Requirement: 集成测试覆盖率报告
系统 MUST 在运行测试时生成覆盖率报告，用于帮助开发者识别未覆盖代码路径；该报告 MUST 不作为默认的失败门槛（不强制阈值）。

#### Scenario: 生成覆盖率报告但不强制阈值
- **WHEN** 开发者运行 `uv run test`
- **THEN** 系统生成覆盖率报告（终端输出与 HTML 报告）
- **AND** 覆盖率不足不会导致测试额外失败（失败仅由测试断言决定）

### Requirement: 集成测试默认使用真实 MySQL 的固定独立测试库
系统 MUST 支持使用真实 MySQL 运行集成测试，并通过**固定独立测试库**保证测试数据与运行环境隔离、可重复，避免污染开发/生产数据库。

#### Scenario: 使用固定测试库与依赖覆盖
- **WHEN** 测试启动应用并覆盖 `get_db` 依赖为指向固定测试库的 `Session`
- **THEN** 测试对数据库的读写不影响开发/生产数据库

#### Scenario: 防误连保护
- **WHEN** 测试环境配置不满足约束（例如 `ENV!=testing` 或 `DB_NAME` 不包含 `_test`）
- **THEN** 测试套件 MUST 立即失败以避免误写入非测试库

### Requirement: 基线鉴权链路集成测试
系统 MUST 提供覆盖鉴权关键路径的集成测试基线，用于验证 token 获取与受保护接口访问的端到端行为。

#### Scenario: 登录成功并访问受保护接口
- **WHEN** 使用有效账号密码请求 `/api/v1/auth/access-token`
- **THEN** 响应包含可用于后续请求的 `access_token`
- **WHEN** 携带该 token 请求 `/api/v1/user/me`
- **THEN** 响应返回当前用户信息且 HTTP 状态码为 `200`

#### Scenario: 登录失败返回标准错误结构
- **WHEN** 使用无效账号或密码请求 `/api/v1/auth/access-token`
- **THEN** 响应返回 `4xx` 且响应体符合统一错误结构（`APIResponseModel`）

