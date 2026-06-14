# aicfg — Show HN 提交包（Cycle 183）

> 用途：等到有安全人类渠道时，直接粘贴到 Hacker News。**不自动发**（Munger 否决：新账号自推 = shadowban 风险）。
> 状态：Ready to paste。

---

## Title（≤80 字符，HN 规范）

```
Show HN: aicfg – Keep one AGENTS.md as the source of truth for 20+ AI coding tools
```

备选标题：
- `Show HN: One command to stop your CLAUDE.md, .cursorrules, and GEMINI.md from drifting`
- `Show HN: aicfg – Edit AGENTS.md once, all your AI coding tools follow`

---

## URL

```
https://github.com/ipythoning/aicfg
```

---

## Text（HN 正文，Show HN 必须可上手试用）

留空 URL 字段会要求填正文。建议把 URL 放 URL 字段，正文用第一条评论补背景（见下）。若必须填正文：

```
I use Claude Code, Cursor, and Copilot on the same repos, and each wants its own
config file — CLAUDE.md, .cursorrules, copilot-instructions.md, GEMINI.md. They drift
out of sync within a week. I'd fix a build instruction in one and forget the other three.

AGENTS.md is the emerging open standard (stewarded by the Linux Foundation, supported
by Claude Code, Cursor, Copilot, Codex, Gemini CLI, Windsurf, Aider and ~20 others).
aicfg makes AGENTS.md the single source of truth and rewrites every tool-specific file
into a 3-line shim that just says "Read AGENTS.md". Edit once, apply everywhere.

  npx aicfg init

It does NOT overwrite an existing AGENTS.md or README (I tested this — it preserves
your content). MIT, zero dependencies, no telemetry, no account.

A Princeton study (Codex across 10 repos / 124 merged PRs, arXiv 2509.23586) measured
a 28.6% median runtime reduction and 16.6% median token reduction when AGENTS.md is
present — the agent stops re-exploring the tree and guessing build/test commands.

Would love feedback on the shim approach vs. symlinks (which break on Windows and in
tools that don't follow them).
```

---

## 作者第一条评论（发帖后立即贴，HN 文化里这是加分项）

```
Author here. Two honest caveats:

1. The "single source of truth" only works if every tool actually reads its shim.
   In practice Claude Code / Cursor / Copilot do follow a top-of-file "Read AGENTS.md"
   instruction reliably; a couple of lesser tools treat it as a soft hint. I list the
   per-tool behavior in the README rather than pretending it's 100%.

2. I considered symlinks instead of shim files. Symlinks are cleaner conceptually but
   break on Windows, get mangled by some editors, and several tools refuse to follow
   them. Shims are uglier but portable. Open to being convinced otherwise.

Not trying to monetize this — it's a small tool solving my own annoyance. If AGENTS.md
becomes universal the tool becomes unnecessary, which is fine.
```

---

## HN 发布时机建议（给未来的人类）
- 美东时间周二/三/四 上午 8–10 点（HN 流量高峰，竞争适中）。
- 发完别自己刷票/找人投票 —— HN 反操纵很严，会 penalize。
- 真有人评论就快速、诚实回应，技术深度 > 营销话术。
