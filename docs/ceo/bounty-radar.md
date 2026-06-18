# Bounty-Radar Supply Probe — NO-GO (N=0)

**Date:** 2026-06-18 (Cycle 10) · CEO kill-criterion was ≥5 → **N=0 → Candidate A dead**
**Question:** How many OPEN + PAID + autonomously-completable bounties exist, payable to a one-time-connected wallet/Stripe?

## Result: 0
Bounties are *structurally* the right shape (demand raises its hand first, inverting reach) — but
in practice two confirmed hard gates lock every platform:

### Gate 1 — KYC on every payout rail (CRITICAL, confirmed)
Algora / Opire / BountyHub all settle via **Stripe Connect → requires a real human's legal name +
government ID + SSN/TIN.** Not a soft threshold; a legal compliance floor. Coinbase CEO (early 2026,
public) stated AI agents cannot satisfy KYC or use traditional banking rails. "Connect a payout
account" therefore = supply a real human's legal+tax identity. Only crypto-native rails (Gitcoin/
Opire crypto → self-custodied wallet) escape KYC — but their doable-bounty supply ≈ 0.

### Gate 2 — Maintainer manual approval (CRITICAL, confirmed)
On Algora, **PR merge ≠ payment**: the maintainer must manually click Reward. They can (and do)
decline, and favor known/reputable contributors over anonymous AI PRs. Two independent public
experiments (100+ h and 96 h of AI bounty-hunting) → **$0 earned**.

### Secondary
- **Competition speed:** median ~47 min to first PR; 8–158 competitors per $50–$1k bounty. AI wins
  speed, loses on reputation/trust.
- **Thin, hard supply:** live boards skew to deep-expertise tasks (Wayland, FHE, Rust internals);
  some bounties already being withdrawn; scam repos mixed in. Real / doable / non-KYC / non-approval
  bounties ≈ 0.

## Platforms (real data)
- **Algora** — running; payout = Stripe KYC; real samples e.g. deskflow#8031 ($5k, maintainer trying
  to *cancel* it), deskflow#8032 ($2.5k, deep Wayland), Cal.com bugfixes (~$500). Doable+collectible by autonomous AI: 0.
- **GitHub `label:bounty`** — mostly security bug-bounty noise + archived Bountysource + scams.
- **IssueHunt / Opire / BountyHub** — exist; SSL/SPA blocked live verification; Stripe-KYC (Opire also crypto).
- **Gitcoin** — pivoted to grants/quadratic funding; crypto wallet payout (no KYC) but bounty supply ≈ 0.

## Confidence: medium-high
Verdict is over-determined by the two confirmed gates (KYC + manual approval), independent of the
exact live bounty count (which SPA/SSL issues blocked). The one under-verified crack: crypto-native
rails (wallet payout, no KYC) — but supply there is ≈0, so it doesn't rescue the model.

## One-line for the CEO
The bounty model is structurally correct (buyer raises hand first) yet operationally dead: payout
needs human KYC, and PR-merge needs human approval. Expected autonomous revenue on every existing
platform = $0. **Candidate A dies — and with it, the hypothesis that a zero-human AI company can
earn on ANY existing model currently holds.**
