# dns-tools 目标关键词清单

**日期**: 2026-06-12 (Cycle 161)  
**目标**: 识别高搜索量、低竞争的长尾 DNS 关键词，指导 SEO 内容页优先级

## 方法论

基于以下维度评估每个关键词：
- **预估 MSV**（月搜索量）：基于 SEMrush/Ahrefs 公开数据范围的推断
- **难度**: 1-10（1=极低竞争，10=高度竞争）
- **意图匹配**: 是否能用我们现有工具或一篇指南页满足
- **商业价值**: 是否能自然引导到工具使用

## Top 20 关键词清单

### Tier 1 — 已覆盖（2 篇已上线）

| # | 关键词 | 预估 MSV | 难度 | 状态 |
|---|--------|----------|------|------|
| 1 | what is dns | 60,000–90,000 | 7 | ✅ `what-is-dns.html` |
| 2 | how to check dns records | 8,000–15,000 | 4 | ✅ `how-to-check-dns-records.html` |

### Tier 2 — 高优先级（下一篇应做）

| # | 关键词 | 预估 MSV | 难度 | 内容主题 | 工具连接 |
|---|--------|----------|------|----------|----------|
| 3 | dns record types explained | 5,000–10,000 | 3 | 每种记录类型详解（A/AAAA/CNAME/MX/TXT/NS/SOA/PTR）+ 使用场景 | → DNS Lookup |
| 4 | check dns propagation | 4,000–8,000 | 4 | DNS 传播原理、TTL、如何验证变更已生效 | → DNS Lookup |
| 5 | how to clear dns cache | 12,000–25,000 | 3 | 各平台清除 DNS 缓存教程（macOS/Windows/Linux/Chrome）| → DNS Lookup |
| 6 | free whois lookup | 6,000–12,000 | 5 | WHOIS vs RDAP 对比、如何查域名注册信息 | → WHOIS |
| 7 | what is a dns a record | 3,000–6,000 | 2 | A 记录深度解析、IPv4 地址映射原理 | → DNS Lookup |
| 8 | how to check ssl certificate | 5,000–10,000 | 5 | SSL/TLS 证书验证方法（浏览器/命令行/在线）| → SSL Checker |

### Tier 3 — 中优先级（内容飞轮）

| # | 关键词 | 预估 MSV | 难度 | 内容主题 | 工具连接 |
|---|--------|----------|------|----------|----------|
| 9 | dns mx record check | 2,000–5,000 | 2 | MX 记录详解 + 邮件服务器配置排查 | → DNS Lookup |
| 10 | check domain expiry date | 3,000–6,000 | 3 | 域名过期风险检查、自动续费设置 | → Expiry Calculator + WHOIS |
| 11 | dns txt record lookup | 1,500–3,000 | 2 | TXT 记录用途（SPF/DKIM/DMARC/验证）| → DNS Lookup |
| 12 | free ssl checker online | 4,000–8,000 | 6 | 在线 SSL 检测工具的对比和使用 | → SSL Checker |
| 13 | reverse dns lookup | 4,000–7,000 | 3 | PTR 记录、反向 DNS 原理和排查 | → DNS Lookup |
| 14 | dns cname vs a record | 1,500–3,000 | 2 | CNAME 和 A 记录的区别和使用场景 | → DNS Lookup |
| 15 | what is dnssec | 2,000–4,000 | 3 | DNSSEC 安全扩展原理解析 | 引导到 DNS 工具生态 |

### Tier 4 — 长尾（低竞争快速排名）

| # | 关键词 | 预估 MSV | 难度 | 内容主题 |
|---|--------|----------|------|----------|
| 16 | how dns works step by step | 2,000–5,000 | 2 | DNS 解析的 8 步流程图解 |
| 17 | dns lookup command line | 1,500–3,000 | 2 | dig/nslookup/host 命令大全 |
| 18 | check dns records for domain | 2,000–4,000 | 3 | 如何为任意域名检查 DNS（与 #2 互补）|
| 19 | what is dns spoofing | 1,500–3,000 | 2 | DNS 欺骗/缓存投毒攻击原理 |
| 20 | free domain health check | 1,000–2,500 | 2 | 域名健康检查清单（DNS+SSL+WHOIS+过期）|

## 策略建议

### 内容优先级

```
Phase 1（本周）: #3 dns record types explained  ← 下一篇
Phase 2（下周）: #4 check dns propagation + #5 how to clear dns cache
Phase 3:        #6 free whois lookup + #8 how to check ssl certificate
Phase 4+:        Tier 3-4 按搜索量递减逐个覆盖
```

### 为什么选 #3 作为下一篇

1. **搜索量大、竞争低**: 5K-10K MSV，难度仅 3/10
2. **完美承接现有内容**: 用户在 "What is DNS?" 了解基础后，自然想了解 "record types"
3. **长尾覆盖**: 每种记录类型（A record, MX record, TXT record）本身都是独立的长尾关键词
4. **工具连接强**: 每种记录类型都能链接到 DNS Lookup 工具的实际使用
5. **内容可复用**: 可与 `what-is-dns.html` 互链，形成内容集群

### 内容集群架构

```
            what-is-dns.html (总览)
                 /        \
dns-record-types.html   how-to-check-dns-records.html
    /    |    \              /        |         \
A记录  MX记录  TXT记录   dig教程  nslookup  在线工具
   \    |    /              \        |         /
        DNS Lookup 工具 ← 所有路径汇聚到工具
```

### 长期 SEO 目标

- **6 个月目标**: 20 篇内容页 + 月度 500-1000 自然访客
- **12 个月目标**: 50 篇内容页 + 月度 3000-5000 自然访客
- **关键指标**: 从 informational query → 工具使用 → 分享/外链的转化漏斗

## 竞争分析摘要

- **主要竞争者**: whatsmydns.net (DA 50+), dnschecker.org (DA 60+), mxtoolbox.com (DA 70+)
- **差异化空间**: 无广告 + 极简 + 开源 + GitHub Pages 部署（技术受众偏好）
- **我们的优势**: 页面加载速度极快（GitHub Pages CDN）、无跟踪、JSON-LD 结构化数据覆盖
- **我们的劣势**: 域名权威低（新站）、内容量少（2篇 vs 竞品几百篇）
- **突破路径**: 长尾关键词优先（难度 2-4），避开竞品主攻的 head terms（难度 7+）
