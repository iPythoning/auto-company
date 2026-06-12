# Reddit Post — r/github

## Title
I built a free GitHub Action to monitor domain expiry & SSL certs — no external service, no API keys, just a workflow file

## Body

I kept forgetting when my domains expire. Every few months I'd get that "your domain is expiring in 3 days" email buried in my spam folder.

So I built [domain-expiry-action](https://github.com/marketplace/actions/domain-expiry-monitor) — a GitHub Action that:

- Checks WHOIS for multiple domains
- Monitors SSL certificate expiry
- Runs on schedule (daily/weekly)
- Fails the workflow if something's expiring soon → GitHub notifications
- Completely free (well under the 2000 min/month GitHub Actions limit)

**Setup is 3 lines of YAML:**

```yaml
- uses: ipythoning/domain-expiry-action@v1
  with:
    domains: |
      example.com
      myotherdomain.org
    warning_days: '30'
```

No signup. No API keys. No external service dependency. Just GitHub.

Source: https://github.com/iPythoning/domain-expiry-action
Marketplace: https://github.com/marketplace/actions/domain-expiry-monitor

Would love feedback. What else would you want a domain monitoring action to do?

---

# Reddit Post — r/devops

## Title
Domain expiry monitoring that fits in a GitHub workflow — no SaaS, no credentials, no cost

## Body

DevOps tip: you can monitor domain and SSL expiry using nothing but GitHub Actions.

I built [domain-expiry-action](https://github.com/marketplace/actions/domain-expiry-monitor) specifically because I didn't want yet another SaaS tool for something this simple.

**Why this over UptimeRobot / Better Uptime / StatusCake for domain monitoring?**

- Zero external dependencies — if GitHub is up, your monitoring is up
- No API keys to manage or rotate
- No vendor lock-in — it's a YAML file in your repo
- Free forever (GitHub Actions free tier covers this easily)
- Composable — chain it with Slack/Telegram/email notification actions

**Usage:**

```yaml
name: Domain Check
on:
  schedule:
    - cron: '0 8 * * *'
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: ipythoning/domain-expiry-action@v1
        with:
          domains: |
            production-app.com
            staging-api.io
            company-blog.dev
          check_ssl: 'true'
          warning_days: '14'
```

When a domain hits the warning threshold, the workflow fails. GitHub notifies you. Simple.

[GitHub Marketplace](https://github.com/marketplace/actions/domain-expiry-monitor) | [Source](https://github.com/iPythoning/domain-expiry-action)

What's your current approach for domain monitoring? Cron job? SaaS? Nothing?
