# 如何用 GitHub Actions 免费监控域名过期

> 零成本、零外部依赖、5 分钟设置的域名和 SSL 证书监控方案

---

你的域名什么时候过期？SSL 证书呢？

说实话——大部分人不知道。你注册域名的时候填了邮箱，然后从未看过它。证书是 Let's Encrypt 自动续的，但万一自动续期失败呢？

我最近建了一个免费的 GitHub Action 来解决这个问题。不需要注册新服务，不需要信用卡，不需要 API key。只需要一个 GitHub 仓库和 5 分钟。

## 它能做什么

`domain-expiry-action` 是一个 GitHub Action，可以：

- **批量监控域名过期时间** — 支持同时检查多个域名
- **SSL 证书过期监控** — 不只是域名，证书也一起查
- **按 schedule 自动运行** — 每天/每周自动检查，完全零人工
- **失败时 workflow 变红** — GitHub 自带的 CI/CD 通知机制，action 失败你就能看到
- **完全免费** — GitHub Actions 每月 2000 分钟免费额度，每天跑一次只用 ~30 分钟/月

## 5 分钟设置

### 1. 在任意仓库创建 workflow 文件

```yaml
# .github/workflows/domain-check.yml
name: Domain Expiry Check

on:
  schedule:
    - cron: '0 8 * * *'  # 每天早上 8 点跑
  workflow_dispatch:      # 也可以手动触发

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: ipythoning/domain-expiry-action@v1
        with:
          domains: |
            yourdomain.com
            another-domain.org
          check_ssl: 'true'
          warning_days: '30'
```

### 2. Push 到 GitHub

就这样。GitHub Actions 会自动按 schedule 运行。如果有域名在 `warning_days` 天内过期，workflow 会失败（变红），你会在 GitHub 通知里看到。

## 为什么用 GitHub Action 而不是 SaaS 工具

市面上的域名监控工具通常：

- **免费版限制 1-2 个域名**，然后就要付费
- **需要注册账号**，又一个要记密码的服务
- **邮件通知可能被拦截**，你根本不知道域名快过期了

GitHub Action 方案：

- **无限域名** — 你已经在用 GitHub 了，只是多一个 workflow 文件
- **零额外账号** — 不需要注册任何新服务
- **通知走 GitHub** — 你已经在看 GitHub notifications，不用检查另一个收件箱
- **可定制** — 想要 Slack/Telegram 通知？加一个 notification action 在后面就行
- **自有数据** — 你的域名列表在你自己的 repo 里，不给第三方

## 适用场景

- **独立开发者**：管理多个 side project 域名
- **小团队**：没有专门的 DevOps，但有 GitHub
- **代理/顾问**：帮客户管理域名，一个 repo 一份 client list
- **任何人**：不想在域名过期这件事上靠记忆

## 安装

从 GitHub Marketplace 一键添加：

👉 [github.com/marketplace/actions/domain-expiry-monitor](https://github.com/marketplace/actions/domain-expiry-monitor)

或者直接在你的 workflow 文件里引用：

```yaml
uses: ipythoning/domain-expiry-action@v1
```

源码在 [github.com/iPythoning/domain-expiry-action](https://github.com/iPythoning/domain-expiry-action)。

---

**免费。开源。不需要注册任何东西。**

如果你有域名，花 5 分钟设一下。未来某天你会感谢现在的自己。
