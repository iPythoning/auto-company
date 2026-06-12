# Reddit 推广内容

## r/webdev — "Showoff Saturday" or general post

**Title:** I built a zero-backend domain & SSL expiry monitor — single HTML file, free forever

**Body:**

Just shipped [domain-monitor-client](https://ipythoning.github.io/domain-monitor-client/) — a tool that tracks when your domains and SSL certs expire.

The twist: **zero backend.** It's a single 17KB HTML file. All queries go directly from your browser to RDAP (modern WHOIS) and crt.sh (Certificate Transparency). No server, no database, no signup.

Why I built it this way:
- I was tired of setting up cron jobs for domain monitoring
- Didn't want another SaaS subscription
- Wanted something I could share as a single file

Tech stack: HTML + CSS + vanilla JS. Deployed on GitHub Pages. Uses the RDAP protocol (RESTful WHOIS replacement) and crt.sh API — both CORS-friendly, no auth needed.

Try it: https://ipythoning.github.io/domain-monitor-client/
Source: https://github.com/iPythoning/domain-monitor-client

Would love feedback — especially on the RDAP integration (it handles 10+ TLDs with different registry servers).

---

## r/SideProject

**Title:** My weekend project: a domain/SSL monitor that costs $0 to run forever

**Body:**

Built a side project this weekend: a domain and SSL certificate expiry monitor.

What makes it different: there's literally no backend. It's one HTML file hosted on GitHub Pages. All the domain lookups happen client-side using RDAP (the JSON-based WHOIS replacement) and crt.sh (public certificate transparency logs).

Why? Because I wanted a tool that:
- Costs nothing to operate (no server bills)
- Never dies (no backend to maintain)
- Respects privacy (domain list stays in your browser's localStorage)

Check it out: https://ipythoning.github.io/domain-monitor-client/

For the technically curious: the RDAP auto-discovery (figuring out which registry server handles which TLD) was the trickiest part. Different registries have different RDAP endpoints, and some (looking at you, .io) have quirks.

---

## r/selfhosted

**Title:** Domain & SSL expiry monitor — self-hostable as a single HTML file

**Body:**

Sharing a tool I built: [Domain Monitor Client](https://ipythoning.github.io/domain-monitor-client/)

It tracks domain expiry and SSL certificate validity. But here's the self-hosting angle: it's a single HTML file. You can literally download index.html, open it in your browser, and it works. No Docker, no npm, no config.

Features:
- RDAP-based WHOIS lookups (no port 43 needed)
- SSL cert expiry via crt.sh
- localStorage persistence
- JSON import/export for backup
- Dark theme, responsive

Self-host options:
1. Download the HTML file and open it locally
2. Serve it from your NAS/home server
3. Fork the repo and use GitHub Pages (free)

Repo: https://github.com/iPythoning/domain-monitor-client
Live demo: https://ipythoning.github.io/domain-monitor-client/

The "backend" is literally your browser talking directly to RDAP servers and crt.sh. No server-side proxy needed because both APIs support CORS.
