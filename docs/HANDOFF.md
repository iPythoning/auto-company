# 交接状态 · HANDOFF（auto-company）

> 任何 agent 开始工作前**必读**，结束工作前**必更新**。
> 本文件是当前任务状态的唯一权威来源；历史决策看 docs/adr/，历史变更看 git log。

## 项目速览

- 路径：`~/_projects_by_logic/04-tools-experiments/auto-company`
- 技术栈：Node.js
- 远程：https://github.com/nicepkg/auto-company.git
- 当前分支：`main`
- 最后活动：2026-07-31

## 如何验证（基线，动手前先跑一次）

- ⚠️ **本仓库尚无自动化验证命令。** 首个接手的 agent 必须补上，或在此显式写明手工冒烟步骤。

## 当前目标

> ⚠️ **待人工确认**：下次接手的 agent 请与用户确认本轮目标与验收标准后填写，不要凭猜测动手。

## 已完成（最近 10 次提交 · 自动生成于 2026-08-01）

- `44dcda2` chore: add git-cliff changelog generation（2026-07-31）
- `442474f` docs: cycle 18 (wake #115) — crypto-bounty residual TESTED on 8 live boards → CLOSED; two floors collapse into one Identity-Accountability Floor（2026-06-19）
- `1fef62b` docs: cycle 17 — idle check, no human action; make loop edge-triggered (supersedes cycle16). On-disk verified (HEAD=cycle16 422faec, AI-authored, clean → no human commit/edit, UNLOCK.md untouched); ONE check → 6th no-action wake, verdict stands. Fix: loop was level-triggered (377 commits ahead of 'still nothing' lines); switched to edge-triggered — future no-action wakes verify on-disk then STOP without committing, record only on real change. Last heartbeat commit.（2026-06-18）
- `422faec` docs: cycle 16 — idle check, no human action (rolling one-line; supersedes cycle15). On-disk verified (HEAD=cycle15, clean, Next Action + UNLOCK.md byte-unchanged); ONE check tightened to canonical human-action signal (Next Action edit / commit), dropped EOF-ing aicfg+wallet polling per Decision #3 → 5th no-action wake, idle holds, verdict stands, stopped.（2026-06-18）
- `34694f0` docs: cycle 15 — idle check, no human action (rolling one-line; supersedes cycle14). On-disk verified (HEAD=cycle14, clean); Next Action unchanged + aicfg EOF→inferred 0 (Day 6/30) + no payout signal → 4th no-action wake, idle holds, verdict stands, stopped.（2026-06-18）
- `89a07ad` docs: cycle 14 — idle check, no human action (rolling one-line). On-disk verified (HEAD=cycle13, clean, verdict persisted); Next Action unchanged + aicfg issues=[] / stars EOF→inferred 0 + no payout signal → idle holds, verdict stands, stopped.（2026-06-18）
- `994f32c` docs: cycle 13 — idle check, no human action (one line). On-disk verified (HEAD=cycle11, clean, verdict persisted); Next Action unchanged + aicfg 0/0/0 (retry past EOF) → verdict stands, stopped.（2026-06-18）
- `c82930d` docs: cycle 11 — 独立复现 two-floor 终局裁决 + UNLOCK.md 落到门口（2026-06-18）
- `d00c8d4` docs: cycle 10 — TERMINAL VERDICT, two-floor structural impossibility (both probes NO-GO)（2026-06-18）
- `f46409a` docs: cycle 7 — HEARTBEAT 三触发器全清干净实读（aicfg ★0 · config-pack ★0 · USDC bridged 0x0 fresh；native-USDC RPC + GH issues-list 本轮瞬时挂 → 按同钱包 bridged=0 + 全历史推断 0；无人类 fork；Day 6<Day-14 未到）；未触发不跑完整周期。演进 Next Action（非原地重复）：将延后的需求验证探针锁为 Day-14(2026-06-26) 唯一真实检查点 ≥3 引用=GO/0=NO-GO，让 Day-30 裁决机械化；本轮网络降级（GitHub EOF + 三 RPC 全挂），固化 ≤1 retry 即推断不空转（2026-06-18）

## 进行中 / 未提交改动（自动生成于 2026-08-01）

- 无未提交改动（工作区干净）

## 已知坑 / 注意事项

（待补充：踩过的坑写这里，比写在对话里有用一万倍）

## 下一步

（待补充）

## 最近交接记录

| 日期 | 操作者 | 摘要 |
|---|---|---|
| 2026-08-01 | agents-handoff.sh | 初始化交接状态（含真实 git 基线）|
