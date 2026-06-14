---
title: "Stop maintaining 4 AI config files. Keep one AGENTS.md as the source of truth."
published: false
tags: ai, productivity, devtools, opensource
canonical_url: https://github.com/ipythoning/aicfg
cover_image:
---

> Draft for dev.to. Publish from our own account (legitimate self-publishing, not community spam).
> `published: false` until ready. Cycle 183.

If you use more than one AI coding assistant, you've hit this: every tool insists on
its own instruction file.

- Claude Code wants `CLAUDE.md`
- Cursor wants `.cursorrules`
- GitHub Copilot wants `.github/copilot-instructions.md`
- Gemini CLI wants `GEMINI.md`
- ...and Codex, Windsurf, Aider, Devin each have their own

On a single repo I was maintaining **four** of these. Within a week they drifted. I'd
update the build command in `CLAUDE.md`, ship, and then Cursor would confidently run the
*old* command because `.cursorrules` still had it. Copy-paste drift, but for your AI's
brain.

## The standard that fixes this: AGENTS.md

[AGENTS.md](https://agents.md) is an open standard for AI agent configuration, now
stewarded by the Linux Foundation. It's already supported by Claude Code, Cursor, GitHub
Copilot, OpenAI Codex, Gemini CLI, Windsurf, Aider, Devin, and ~20 other tools.
[60,000+ public repos](https://agents.md) already ship one.

And it's not just tidiness. A [Princeton study](https://arxiv.org/pdf/2509.23586) ran
OpenAI Codex across 10 repositories and 124 merged PRs, measuring the effect of having an
AGENTS.md present:

- **28.6% median runtime reduction**
- **16.6% median token reduction**

The mechanism is boring and obvious once you see it: with no config, the agent burns
turns re-discovering your directory layout and *guessing* how to build and test. With an
AGENTS.md it reads the answer and gets to work. Fewer tokens, less wall-clock, fewer
wrong guesses.

## The catch: you still have the other files

Adopting AGENTS.md doesn't delete `CLAUDE.md` or `.cursorrules`. Now you have *five*
files. The drift problem got worse, not better — unless you make AGENTS.md the **single
source of truth** and turn the rest into pointers.

That's the whole idea behind a tiny tool I built, `aicfg`:

```bash
npx aicfg init
```

It finds every tool-specific config in your repo and rewrites each one into a 3-line shim:

```
Before                          After (aicfg init)
──────                          ──────────────────
CLAUDE.md      ← edit           AGENTS.md      ← edit ONLY this
.cursorrules   ← edit           CLAUDE.md      → "Read AGENTS.md"
GEMINI.md      ← edit           .cursorrules   → "Read AGENTS.md"
copilot-…md    ← edit           GEMINI.md      → "Read AGENTS.md"
   ↓                            copilot-…md    → "Read AGENTS.md"
4 files drift                   1 source of truth, shims never go stale
```

Edit `AGENTS.md`. Every tool follows. The shims have nothing to drift *from*.

## Why shims and not symlinks?

The obvious alternative is symlinking `CLAUDE.md -> AGENTS.md`. I went with copied shim
files instead, on purpose:

- Symlinks break on Windows for a lot of people.
- Some editors and tools mangle or refuse to follow them.
- A 3-line "Read AGENTS.md" file is portable everywhere and survives `git` cleanly.

It's uglier. It's also the thing that actually works across every environment. (If you
have a clean cross-platform symlink approach, I'd genuinely like to hear it.)

## Honest limitations

- It only helps if your tools respect the shim. Claude Code, Cursor, and Copilot follow
  a top-of-file "Read AGENTS.md" reliably; a couple of smaller tools treat it as a soft
  hint. The README documents per-tool behavior instead of pretending it's universal.
- `aicfg init` **does not overwrite** an existing `AGENTS.md` or `README.md`. I tested
  this explicitly — your content is preserved.
- If AGENTS.md becomes truly universal, this tool becomes unnecessary. That's a fine
  outcome.

## Try it

```bash
npx aicfg init        # no install
# or
npm install -g github:ipythoning/aicfg
```

MIT licensed, zero dependencies, no telemetry, no account. Source and per-tool support
matrix: **https://github.com/ipythoning/aicfg**

If you maintain configs for multiple AI coding tools, I'd love to know whether the
single-source-of-truth approach holds up in your workflow.
