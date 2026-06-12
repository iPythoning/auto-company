# 如何用 MCP Server 自动监控域名过期和 SSL 证书 — 零 API Key 方案

> 目标平台：dev.to  
> 标签：`mcp`, `devops`, `ssl`, `domain`, `tutorial`  
> 状态：草稿，待 dev.to 账号认证后发布

---

你有没有遇到过这种情况：

- SSL 证书过期，用户看到 "Your connection is not private" 的红色警告页面
- 域名忘记续费，网站直接消失
- 监控工具配置了但没人看 dashboard

我最近也在处理这个问题，于是做了一个 MCP server 来解决它。核心思路很简单：**让 AI 助手帮你盯着域名健康，而不是多一个要记得查看的 dashboard。**

## 为什么是 MCP？

如果你在用 Claude Desktop、Claude Code、Cursor、Windsurf 这些 AI 工具，MCP（Model Context Protocol）让 AI 能直接调用外部工具。这意味着你可以在和 AI 对话时直接问："检查一下我们所有域名的 SSL 证书有没有快过期的"，AI 会调用 MCP 工具去查，然后告诉你结果。

不需要：
- 注册任何服务
- 申请任何 API key
- 配置任何 webhook

## 怎么用

### 1. 安装（2 分钟）

在 Claude Code 中：

```bash
claude mcp add domain-monitor -- npx domain-monitor-mcp-server
```

或在 Claude Desktop 的 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "domain-monitor": {
      "command": "npx",
      "args": ["domain-monitor-mcp-server"]
    }
  }
}
```

### 2. 使用

然后你就可以直接问 AI：

> "帮我看一下 example.com 的域名什么时候过期"

AI 会调用 `domain_check` 工具，返回：
- WHOIS 注册过期日期
- SSL 证书过期日期
- 各项剩余天数
- 严重程度判断

或者批量检查：

> "检查这些域名的 SSL 证书状态：example.com, github.com, anthropic.com"

AI 会用 `domain_check_batch` 并行检查，返回每个域名的状态（ok/warning/critical/expired）。

### 3. 技术细节

底层用了两个免费数据源：

| 数据源 | 协议 | 用途 |
|--------|------|------|
| rdap.org | RDAP（WHOIS 的现代替代） | 域名注册过期查询 |
| crt.sh | Certificate Transparency 日志 | SSL 证书过期查询 |

两个都**不需要 API key**，零注册，零配置。RDAP 是 IANA 标准协议，比传统 WHOIS 更结构化、更可靠。

### 4. 一个实际案例

假设你管理 5 个域名的 SaaS 产品。传统做法是：
1. 在 monitoring dashboard 里配置 5 个 check
2. 设置 alert threshold
3. 配置通知渠道（email/Slack）
4. 等着在真正出问题的时候收到告警

用 MCP 的方式：
1. 安装 domain-monitor MCP server
2. 在 Claude Code 里问 "检查我们的 5 个域名有没有快过期的"
3. 看到结果，如果有需要处理的，立即去续费

**核心区别：dashboard 是被动的（等你去看），MCP 是主动的（等你来问）。前者是又一个要记得检查的系统，后者是你日常工作流的一部分。**

## 为什么选这个方案

市面上已经有很多监控工具（UptimeRobot, Better Uptime, Datadog Synthetics），它们都很强。但我的场景是：

1. **不想多一个 dashboard 要维护** — 已经在用 Claude Code 写代码，域名监控跟着 AI 助手走更自然
2. **不想注册新服务** — 零 API key 意味着零注册、零费用、零隐私顾虑
3. **批量检查场景** — 经常需要一次性检查几十个域名，传统工具要么不支持批量，要么要一个个配置

## 限制和未来方向

当前版本的限制：
- stdio transport only — 不支持远程 HTTP 调用（所以 Smithery 暂不支持）
- 依赖 rdap.org 和 crt.sh 的外部服务可用性
- npm 包发布等待 2FA 审批

下一步计划：
- 添加 HTTP transport 以支持 Smithery 和远程部署
- 添加 email/webhook 通知（当 domain_check 发现即将过期时主动告警）
- 支持自定义 RDAP bootstrap（企业内部 DNS 场景）

## 代码

GitHub: [ipythoning/domain-monitor-mcp-server](https://github.com/iPythoning/domain-monitor-mcp-server)

欢迎 star / issue / PR。特别是如果你有其他数据源的建议（DNS 记录检查？HTTP response 监控？），开 issue 讨论。

---

*这个 server 是「用 AI 替代 dashboard」的实验。如果你也在想"能不能让我的 AI 助手干这个事"，希望这个案例对你有启发。*
