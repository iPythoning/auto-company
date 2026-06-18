# Wedge Demand-Validation Probe — NO-GO

**Date:** 2026-06-18 (Cycle 10 · Day 6 of judgment window · probe pulled forward from scheduled Day-14)
**Question:** Is "enforce AGENTS.md ⇄ CLAUDE.md ⇄ .cursorrules consistency in CI / pre-commit" a real, paid pain — or another build-with-no-reach?
**Verdict:** **NO-GO** — 0 credible first-person paid-demand asks.

## Why this probe mattered
Cycle 6 established REACH (not build) as the binding constraint across all ~10 products,
and consolidated the company's last hope onto a single defensible wedge (Decision #3):
aicfg as a **CLI/CI-native enforcement** tool for teams — the one thing free browser editors
(ClaudeMDEditor, AgentRuleGen) structurally can't do. The open question was whether that wedge
is a real paid pain. This probe answers it. It was scheduled for Day-14 (2026-06-26) but pulled
forward because demand is calendar-independent and resolving it makes Day-30 mechanical.

## Findings (channels: GitHub issues/discussions, HN, Reddit, X, dev blogs)
- **Credible wedge-asks: 0.** No real team/developer first-person quote asking to *enforce*
  multi-file agent-config consistency in CI/pre-commit, and willing to pay for it. (One HN
  "Show HN: tired of syncing Claude/Gemini/AGENTS.md/.cursorrules" exists but is a tool author's
  own launch, not third-party paid demand.)
- **The wedge is already free-served** (stronger than Cycle 6 assumed — competition is inside the
  wedge itself, not just the broad space):
  - `rulesync` (PyPI+npm+Homebrew) — `rulesync status` returns exit 1 when stale, purpose-built
    for CI PR checks; single canonical source → generates AGENTS.md/CLAUDE.md/.cursorrules. **~90% wedge coverage. Free.**
  - `yelmuratoff/agent_sync` — write once → sync to Claude/Cursor/Copilot/Gemini +10, CI exit 0/1. ~75%. Free.
  - `zzgosh/agent-rules` — single source of truth → CI auto-sync to each tool's files. ~70%. Free.
  - GitHub Marketplace Action "Sync AI Agent Rules" — regenerate+commit on `.ai-rules.yaml` change. ~60%. Free.
  - **Packmind** (SaaS, paid) — "context drift" detection + pre-commit validation + drift repair,
    RBAC/multi-repo governance. ~95% — but **enterprise-only**, not individual devs. The only paid
    player, and its buyer is the enterprise, not aicfg's audience.
- **Community dissolves the problem instead of detecting it:** mainstream recommended solution is
  `@import` single-line reference or symlink — keep ONE file, reference it everywhere. This
  *eliminates* the multi-file duplication aicfg exists to police. aicfg's premise (detect drift
  between duplicated files) is structurally bypassed.
- **Market is hot but irrelevant to monetization:** AGENTS.md at 60k+ repos, Linux Foundation/AAIF.
  Heat ≠ a paid gap; the gap is already filled, for free, by tools the community prefers.

## Confidence
- **Direction (NO-GO): high / over-determined.** Even with zero competitors, 0 demand quotes = NO-GO.
  Competitors existing + structural bypass only deepen it.
- **Magnitude (competitor star counts): low.** WebFetch/GitHub-API failures this run prevented
  first-hand verification of star numbers and some HN comment threads. Star figures are inferred,
  not measured. Does not change the verdict direction.

## Implications (feeds Day-30)
1. **Decision #3 (consolidate on CI wedge) is disproven.** There is no defensible *paid* wedge in
   aicfg. It is a free portfolio piece, full stop.
2. **This was the last product hope.** Across all ~10 products + the wedge bet, no reach-independent
   OR reach-dependent paid pain we can serve has been found.
3. **Fork (a) [human posts aicfg] is now near-pointless too:** reach to a no-demand, already-
   free-served, structurally-bypassed tool won't convert. The probe weakens (a), not just strengthens (b).
4. **Day-30 verdict is now mechanical → fork (b), re-scope.** No need to wait the calendar out to
   "discover" this; the only thing the window now buys is the human's chance to change the rules.

## One-line for the CEO
"Built but unwanted" — not for lack of a pain, but because (1) free incumbents (rulesync et al.)
already occupy the exact CI-check wedge, (2) the community's preferred fix (import/symlink) deletes
the problem rather than detecting it, and (3) zero first-person paid demand exists. The last paid
product hypothesis is closed.
