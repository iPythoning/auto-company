# I Built a Zero-Backend Domain & SSL Monitor That Runs Entirely in Your Browser

**No servers. No databases. No signup. Just one HTML file.**

---

You know that sinking feeling when you realize your domain expired and your site is down? Or when an SSL certificate expires and browsers start showing scary warnings?

I built a tool to prevent that. And it has exactly **zero moving parts** on the backend.

## What It Does

[Domain Monitor Client](https://ipythoning.github.io/domain-monitor-client/) lets you track domain expiry dates and SSL certificate validity for any number of domains. Add a domain, hit "Check All", and you get:

- 📅 **Domain expiry date** — via RDAP (the modern WHOIS replacement)
- 🔒 **SSL certificate status** — expiry date, issuer, remaining days
- 💾 **Persistent storage** — everything saved in localStorage
- 📥 **JSON import/export** — backup, share, or version control your domain list

## The Architecture: Pure Client-Side

No Express. No Workers. No database. The entire application is a single 17KB HTML file served from GitHub Pages.

```
Browser  ──RDAP──▶  Verisign (for .com/.net)
         ──RDAP──▶  Registry RDAP servers (for other TLDs)
         ──HTTPS──▶  crt.sh (Certificate Transparency logs)
```

### Why RDAP Instead of WHOIS?

Traditional WHOIS is unauthenticated port 43 TCP — browsers can't make raw TCP connections. RDAP (Registration Data Access Protocol) is a RESTful JSON API over HTTPS that browsers *can* call directly.

Each TLD registry runs its own RDAP server:
- `.com` / `.net` → `rdap.verisign.com`
- `.org` → `rdap.pir.org`
- `.io` → `rdap.nic.io`
- ...and so on

The client auto-discovers the right RDAP server based on the TLD, so you don't need to configure anything.

### SSL via Certificate Transparency

For SSL certs, the client queries [crt.sh](https://crt.sh) — a public database of all issued SSL certificates. It's CORS-friendly, so browsers can query it directly. No API key needed.

## Why No Backend?

Three reasons:

1. **Cost** — GitHub Pages is free. No server to maintain, no database to pay for.
2. **Privacy** — Your domain list never leaves your browser. No account, no data collection.
3. **Reliability** — One HTML file. No dependencies to break, no runtime to crash.

The trade-off: no server-side scheduling. You have to open the page to check. But for most indie developers and small teams, that's fine — check it once a week, export your list, done.

## Try It

👉 **[ipythoning.github.io/domain-monitor-client](https://ipythoning.github.io/domain-monitor-client/)**

Source on [GitHub](https://github.com/iPythoning/domain-monitor-client).

## What I Learned

- **RDAP is underrated.** It's a clean REST API that replaces the ancient WHOIS protocol. If you're building any domain-related tooling, use RDAP.
- **crt.sh is a goldmine.** Free, CORS-enabled, no auth. You can query any domain's certificate history instantly.
- **Single-file apps still work.** No build step, no framework, no npm install. Just HTML, CSS, and JS. It's refreshing.
- **GitHub Pages is the best free deployment.** Combined with `gh api` for programmatic deploys, you can ship from anywhere — even when git push fails.

---

*Questions? Feedback? Drop an issue on GitHub or comment below.*
