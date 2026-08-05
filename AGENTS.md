# AGENTS.md — Node.js + Express API

Project conventions for AI coding agents. These rules **override** default agent behavior. Follow them exactly; when a rule has a *Why*, honor the reasoning, don't just pattern-match the letter.

## Stack assumptions

- Node.js (LTS) · Express · TypeScript (strict) · package manager: npm
- Adjust the commands below if your project differs.

```bash
npm run dev      # dev server (tsx/nodemon, auto-reload)
npm run build    # tsc — production build (must pass before any commit)
npm run lint     # ESLint
npm run test     # test suite (supertest for HTTP integration)
```

## Scope discipline (read first)

- **Change only what the task requires.** Do not refactor, rename, or reformat code outside the requested change. *Why: unrequested edits bury the real diff and break unrelated work.*
- **Ask before introducing a new dependency, pattern, or abstraction.** Prefer what the codebase already uses. *Why: a second HTTP client, ORM, or validation library is a tax forever.*
- **No speculative generality.** Build for the requirement in front of you (YAGNI).

## TypeScript

- **`strict` is on. Never use `any` — use `unknown` and narrow.** *Why: `any` silently disables the type system exactly where bugs hide.*
- Type request/response bodies; never trust `req.body`, `req.params`, or `req.query` as-is — they are `unknown` until validated.
- Derive types from your validation schema (`z.infer`) instead of hand-maintaining a parallel `interface`.

## Architecture

- **Keep route handlers thin. Push business logic into a service layer; keep data access in a repository/model layer.** *Why: logic buried in a route handler can only be tested by spinning up HTTP — services are unit-testable in isolation.*
- Layering: `routes → controllers → services → repositories`. A layer talks only to the one below it.
- One concern per module; group by feature (`features/orders/{orders.routes.ts, orders.service.ts, orders.repo.ts}`), not by type.

## Async & error handling (the #1 Express failure mode)

- **Every async route/middleware must forward errors to `next(err)`.** Wrap async handlers (`asyncHandler(fn)` or `express-async-errors`) so a rejected promise never escapes. *Why: an unhandled promise rejection in a raw `async` handler hangs the request and can crash the process — Express does not catch it for you.*
- **Use one centralized error-handling middleware** (the 4-arg `(err, req, res, next)`) registered last. Map known errors to status codes there; never `try/catch` and `res.json` an error in every handler.
- **Never swallow an error with an empty `catch {}`.** *Why: a silent catch turns a clear failure into a mystery bug three layers away.*
- **Never leak internals to the client.** Log the full error + stack server-side; return a safe message and a stable error code to the caller. *Why: stack traces and DB errors in responses are an information-disclosure vulnerability.*

## Validation

- **Validate every external input at the edge with a schema (zod/valibot) before it reaches a service.** Reject with `400` on failure. *Why: trusting unvalidated request data is the root of most crashes and injection bugs.*
- Validate config too: load env into a schema at startup and fail fast if a required var is missing or malformed.

## Configuration & secrets

- All config comes from environment variables, parsed once into a typed, validated config object. **Never read `process.env` scattered through the code.**
- **Never hardcode secrets.** No keys, tokens, or connection strings in source. *Why: committed secrets leak permanently — even after deletion they live in git history.*

## Security

- Use `helmet` for security headers and an explicit CORS allowlist — never `cors()` wide open in production.
- **Rate-limit public and auth endpoints.** *Why: unthrottled login/signup routes are brute-force and abuse targets.*
- Parameterize every database query; never string-concatenate SQL or build queries from user input.
- Enforce a request body size limit (`express.json({ limit })`).

## Observability

- Use a structured logger (pino/winston) with levels. **No `console.log` in committed code.** *Why: `console.log` has no levels, no structure, and floods production logs.*
- Log request id / correlation id so a single request can be traced across layers.

## API responses

- Use one consistent response shape across the API (e.g. `{ data }` on success, `{ error: { code, message } }` on failure). *Why: a predictable envelope lets every client handle success and error the same way.*
- Use correct HTTP status codes — `201` for create, `204` for empty success, `4xx` for client errors, `5xx` only for genuine server faults.

## Lifecycle

- Handle `SIGTERM`/`SIGINT`: stop accepting connections, finish in-flight requests, close the DB pool, then exit. *Why: killing mid-request drops user data and corrupts connections.*

## Code style

- Immutability by default: return new objects, don't mutate inputs. *Why: hidden mutation is the hardest class of bug to trace.*
- Early returns over deep nesting (max ~3 levels). Named constants over magic numbers.
- Functions under ~50 lines; files under ~400 (hard cap 800) — extract when they grow.
- No commented-out code or context-free TODOs in committed code.

## Testing

- Integration-test routes with `supertest`; unit-test services directly. Use Arrange–Act–Assert.
- Cover the error paths, not just the happy path — bad input, missing auth, downstream failure. *Why: the error paths are exactly where Express apps break in production.*
- Descriptive names: `returns 400 when email is missing`.
- Run `npm run test` and `npm run build` before declaring work done.

## Definition of done

- [ ] Build passes (`npm run build`)
- [ ] Lint clean (`npm run lint`)
- [ ] Tests pass for changed logic (happy + error paths)
- [ ] Every async handler forwards errors; no empty catches
- [ ] No `any`, no hardcoded secrets, no stray `console.log`, no internal errors leaked to clients
- [ ] Diff contains only what the task required


---

# 跨 agent 交接协议（通用，勿删）

## 开始工作前：接续三步（必做）

1. 按固定顺序阅读：`README* → AGENTS.md → docs/HANDOFF.md → docs/adr/ → git log -10 --oneline`
2. 先跑一次下方验证命令，确认基线是绿的。**基线红 → 先修基线，绝不在红基线上叠改动。**
3. 用自己的话复述当前任务与验收标准，确认与 HANDOFF 一致后再动手。

## 结束工作前：收尾三件套（必做）

1. 跑完整验证命令，确认全绿。
2. 更新 `docs/HANDOFF.md`：当前目标 / 已完成 / 进行中（含文件与位置）/ 已知坑 / 下一步 / 验证方式。
3. 提交 git：**不留未提交的半成品**；commit message 用 Conventional Commits 并写清"为什么"。

## 验证命令（共同基线）

- ⚠️ **本仓库尚无自动化验证命令。** 首个接手的 agent 必须补上，或在此显式写明手工冒烟步骤。

如命令变更，必须同步更新本节——这是所有 agent 的共同基线。

## 决策记录（ADR）

- 任何"为什么这么改"的架构 / 方案决策，写入 `docs/adr/`，格式见 `docs/adr/0000-template.md`。
- 对话里想通但没落盘的决策，等于没发生过。

## Git 纪律

- **禁止 `git add -A`**：只用 `git add -u` 或逐文件 `git add <path>`；新文件必须显式 add。
- commit 前 `git diff --stat` 确认无意外的 Dockerfile / nginx.conf / docker-compose.yml 变更；基础设施文件单独 commit。
- 小步提交，一个 commit 只做一件事；一个任务一个分支。

## 反模式（禁止）

- ❌ 把关键上下文写进 `.claude/`、`.cursor/` 等厂商私有目录
- ❌ 依赖对话摘要 / 上下文压缩传递状态
- ❌ 在测试红的状态下继续叠新功能
- ❌ 一次性做超出"半天能讲完"粒度的任务再交接


## 工程原则

- 不保留向后兼容：删除过时路径，而不是加兼容层、回退或迁移代码。
- 选择能完全满足当前需求的最简实现；避免投机性的抽象、配置与间接层。
- 分层演进：从端到端能跑通的最小版本开始，在"已经能用"的基础上叠加新能力；绝不用半成品复杂度替换能用的产品。
- 保持组件模块化，关注点清晰分离。
- 优先采用成熟且维护良好的库（能降低整体复杂度或提升可靠性时）；无明确理由不重复实现常见功能。
- 先用项目里已有的依赖，再考虑自己实现或新增包；在查文档和类型定义之前，不要假设某个库缺少某能力。
- 架构决策面向长期；不接受"只能应付现在、注定以后替换"的临时方案。

冲突裁决：架构边界按长期设计，边界之内的实现按当前最简。

安全红线：绝不提交密钥、证书、证件与客户隐私数据；发现仓库中已存在此类文件时，先报告，不静默处理。
