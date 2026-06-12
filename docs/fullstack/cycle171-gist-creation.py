#!/usr/bin/env python3
"""Cycle 171: Create 5 Gists for new Telegraph articles + missing What is DNS"""

import subprocess

def create_gist(description, filename, content):
    result = subprocess.run(
        ['gh', 'gist', 'create', '--public', '-d', description, '-f', filename],
        input=content,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f'Gist creation failed: {result.stderr}')
    return result.stdout.strip()

# Gist 1: What is DNS (missing from cycle 170)
gist_what_is_dns = """# What is DNS — A Beginner's Guide to Domain Name System (2026)

DNS (Domain Name System) is the phonebook of the internet. When you type example.com into your browser, DNS translates that human-readable domain name into a machine-readable IP address like 93.184.216.34.

## How DNS Works (In 7 Steps)

1. **User types a URL** — You enter example.com in your browser
2. **DNS Resolver queries** — Your computer asks the DNS resolver (ISP or public resolver like 8.8.8.8)
3. **Root nameserver** — The resolver asks a root nameserver: "Who handles .com?"
4. **TLD nameserver** — The resolver asks the .com TLD server: "Who handles example.com?"
5. **Authoritative nameserver** — The resolver asks the authoritative nameserver: "What's the IP for example.com?"
6. **IP address returned** — The resolver caches the answer
7. **Browser connects** — Your browser uses the IP to load the website

## Common DNS Record Types

| Record | Purpose | Example |
|--------|---------|---------|
| **A** | Domain to IPv4 | example.com to 93.184.216.34 |
| **AAAA** | Domain to IPv6 | example.com to 2606:2800:... |
| **CNAME** | Domain alias | www to example.com |
| **MX** | Mail server | MX 10 mail.example.com |
| **TXT** | Text/SPF/DKIM | "v=spf1 include:_spf.google.com ~all" |
| **NS** | Nameservers | ns1.example.com |
| **SOA** | Zone admin | Primary NS, serial, TTL |
| **PTR** | Reverse DNS | IP to domain name |
| **CAA** | Cert Authority | Only specific CAs can issue certs |

## DNS Security

- **DNSSEC** — Cryptographic signatures prevent DNS spoofing/cache poisoning
- **DNS over HTTPS (DoH)** — Encrypted DNS queries over HTTPS (port 443)
- **DNS over TLS (DoT)** — Encrypted DNS queries on dedicated port 853

## Related Guides

- [DNS Record Types Explained](https://telegra.ph/DNS-Record-Types-Explained--A-Complete-Guide-2026-06-12)
- [How to Check DNS Records](https://telegra.ph/How-to-Check-DNS-Records--A-Complete-Guide-2026-06-12)
- [Complete DNS Guide](https://telegra.ph/The-Complete-DNS-Guide--Everything-You-Need-to-Know-About-Domain-Name-System-2026-06-12)
- [Free DNS Tools](https://ipythoning.github.io/dns-tools/)

---

*Part of the [DNS Tools](https://ipythoning.github.io/dns-tools/) collection — free DNS tools and guides.*
"""

# Gist 2: WHOIS Lookup
gist_whois = """# Free WHOIS Lookup — How to Check Domain Ownership and Registration Details (2026)

WHOIS is the internet's domain phonebook. It tells you who registered a domain, when, and when it expires. This guide covers both traditional WHOIS and the modern RDAP protocol.

## What WHOIS Tells You
- **Registrar** — Which company manages the domain (GoDaddy, Namecheap, Cloudflare, etc.)
- **Registration & Expiration Dates** — Domain creation and expiry
- **Nameservers** — Where the domain's DNS is hosted
- **Domain Status** — Active, pending delete, locked, etc.
- **Registrant Info** — Often redacted for GDPR privacy

## RDAP vs WHOIS
RDAP (Registration Data Access Protocol) is the modern JSON-based replacement:
- **Structured JSON output** — Much easier for tools to parse
- **Standardized fields** — Consistent across all registrars
- **HTTPS security** — Better than plain-text WHOIS
- **Differentiated access** — Public vs authenticated queries

## How to Check WHOIS

### Command Line
```bash
whois example.com
```
Most OSes include this. Use `brew install whois` on macOS if missing.

### RDAP via curl
```bash
curl -s https://rdap.verisign.com/com/v1/domain/example.com
```

### Online WHOIS Tools
Use a free WHOIS lookup tool for instant, structured results via RDAP.

## WHOIS Status Codes
- **clientTransferProhibited** — Transfer locked
- **ok** — Domain active, no restrictions
- **pendingDelete** — About to be released to public
- **redemptionPeriod** — Expired but can be restored (significant fee)
- **clientDeleteProhibited** — Deletion locked
- **clientUpdateProhibited** — Settings modification locked

## GDPR and Domain Privacy
Since GDPR (2018), personal data is redacted for EU residents. Most registrars now offer WHOIS privacy by default, showing "REDACTED FOR PRIVACY" or the registrar's proxy info instead of real owner details.

## Free DNS Tools
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — RDAP-powered domain lookup
- [Domain Expiry Calculator](https://ipythoning.github.io/dns-tools/expiry-calculator.html) — Track domain expiration
- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query DNS records
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All tools

## Related Telegraph Guides
- [WHOIS Lookup Complete Guide](https://telegra.ph/Free-WHOIS-Lookup--How-to-Check-Domain-Ownership-and-Registration-Details-2026-06-12)
- [DNS Record Types Explained](https://telegra.ph/DNS-Record-Types-Explained--A-Complete-Guide-2026-06-12)
- [Complete DNS Guide](https://telegra.ph/The-Complete-DNS-Guide--Everything-You-Need-to-Know-About-Domain-Name-System-2026-06-12)

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*
"""

# Gist 3: DNS Record Lookup
gist_dns_lookup = """# DNS Record Lookup — How to Query A, AAAA, MX, TXT, CNAME, NS Records (2026)

DNS record lookup lets you query what records exist for any domain. Essential for troubleshooting, verifying DNS changes, and investigating domain configurations.

## Common DNS Record Types

| Record | Purpose | Example |
|--------|---------|---------|
| **A** | Domain to IPv4 | example.com to 93.184.216.34 |
| **AAAA** | Domain to IPv6 | example.com to 2606:2800:... |
| **CNAME** | Domain alias | www to example.com |
| **MX** | Mail server | MX 10 mail.example.com |
| **TXT** | Text/SPF/DKIM | "v=spf1 include:_spf.google.com ~all" |
| **NS** | Nameserver | ns1.example.com |
| **SOA** | Zone admin | Primary NS, serial, TTL |
| **PTR** | Reverse DNS | IP to domain name |
| **SRV** | Service location | _sip._tcp.example.com |
| **CAA** | Cert Authority | Only Let's Encrypt |

## How to Query DNS Records

### dig (Linux/macOS)
```bash
dig example.com A        # A record (IPv4 address)
dig example.com MX       # Mail servers
dig example.com ANY      # All records
dig @8.8.8.8 example.com # Query specific resolver
```

### nslookup (All platforms, including Windows)
```bash
nslookup example.com
nslookup -type=mx example.com
```

### Online DNS Lookup Tools
Use a free DNS record lookup tool to query A, AAAA, MX, TXT, CNAME, NS, and SOA records in one click using DNS-over-HTTPS.

## Troubleshooting Common Issues
- **NXDOMAIN** — Domain doesn't exist (check spelling)
- **SERVFAIL** — Server error, try a different resolver like 1.1.1.1
- **No records returned** — That record type may not exist for the domain
- **Inconsistent results** — DNS propagation may still be in progress
- **DoH blocked** — Some networks block DNS-over-HTTPS; fall back to standard DNS

## Free DNS Tools
- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query A, AAAA, MX, TXT, CNAME, NS, SOA
- [DNS Record Types Reference](https://ipythoning.github.io/dns-tools/dns-record-types.html) — Complete guide to all record types
- [Check DNS Propagation](https://ipythoning.github.io/dns-tools/check-dns-propagation.html) — Global DNS propagation checker
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All tools

## Related Telegraph Guides
- [DNS Record Lookup Complete Guide](https://telegra.ph/DNS-Record-Lookup--How-to-Query-A-AAAA-MX-TXT-CNAME-NS-Records-2026-06-12)
- [DNS Record Types Explained](https://telegra.ph/DNS-Record-Types-Explained--A-Complete-Guide-2026-06-12)
- [What is DNS — Beginner's Guide](https://telegra.ph/What-is-DNS--A-Beginners-Guide-2026-06-12)

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*
"""

# Gist 4: SSL Certificate Checker
gist_ssl = """# SSL Certificate Checker — How to Verify SSL/TLS Certificates and Avoid Expiry (2026)

SSL/TLS certificates secure websites with encryption. An expired or misconfigured certificate means browsers show scary warnings to visitors — costing you trust, traffic, and SEO ranking.

## What SSL/TLS Certificates Do
1. **Encryption** — All data between browser and server is encrypted
2. **Authentication** — Verifies you are connected to the real website
3. **Trust** — Certificate Authorities (CAs) validate domain ownership

## Certificate Types
- **Domain Validated (DV)** — Basic validation, issued in minutes. For blogs and personal sites.
- **Organization Validated (OV)** — Company identity verified. Shows org name in certificate.
- **Extended Validation (EV)** — Maximum validation. Company name in browser address bar.
- **Wildcard** — Covers all subdomains (*.example.com)
- **Multi-Domain (SAN)** — Multiple domains in a single certificate

## How to Check SSL Certificates

### Browser Method
Click the padlock icon in the address bar -> "Connection is secure" -> "Certificate is valid"

### Command Line (openssl)
```bash
openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>/dev/null | openssl x509 -noout -dates -subject -issuer
```
This returns validity dates, subject, and issuer.

### Online SSL Checker
Get instant results: validity dates, issuer, Subject Alternative Names (SANs), chain validation, days until expiry.

## Common SSL Issues
- **Certificate Expired** — Most common problem. Set up auto-renewal!
- **Name Mismatch** — www vs non-www misconfiguration
- **Self-Signed Certificate** — Not trusted by browsers
- **Incomplete Certificate Chain** — Missing intermediate certificates
- **Mixed Content** — HTTPS page loading HTTP resources
- **Obsolete Protocol** — Using old TLS 1.0/1.1 or weak ciphers

## Let's Encrypt — Free SSL
Free SSL certificates with 90-day validity. Auto-renewal via Certbot:
```bash
certbot --nginx -d example.com -d www.example.com
```
Most platforms (Cloudflare, Netlify, Vercel) provide free auto-renewing SSL.

## Free Tools
- [SSL Certificate Checker](https://ipythoning.github.io/dns-tools/ssl-checker.html) — Instant SSL check
- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query DNS records
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — Domain registration
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All tools

## Related Telegraph Guides
- [SSL Certificate Checker Complete Guide](https://telegra.ph/SSL-Certificate-Checker--How-to-Verify-SSLTLS-Certificates-and-Avoid-Expiry-2026-06-12)
- [WHOIS Lookup Guide](https://telegra.ph/Free-WHOIS-Lookup--How-to-Check-Domain-Ownership-and-Registration-Details-2026-06-12)
- [Complete DNS Guide](https://telegra.ph/The-Complete-DNS-Guide--Everything-You-Need-to-Know-About-Domain-Name-System-2026-06-12)

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*
"""

# Gist 5: Domain Expiry Calculator
gist_expiry = """# Domain Expiry Calculator — How to Track Domain Expiration and Avoid Losing Your Domain (2026)

Forgetting to renew a domain can be catastrophic — you could lose your website, email, and brand. Google famously forgot to renew google.com in 2015 (a former employee bought it for $12 before Google got it back). This guide explains how to never miss a domain renewal.

## Domain Expiration Lifecycle

| Stage | Duration | Can Renew? | Cost |
|-------|----------|------------|------|
| **Active** | 1-10 years | Yes | Regular price |
| **Grace Period** | 0-45 days | Yes | Regular price |
| **Redemption** | 30 days | Yes | $80-$300+ restoration fee |
| **Pending Delete** | 5 days | No | Cannot recover |

After pending delete, the domain becomes available for anyone to register.

## How to Check Domain Expiration

### WHOIS Lookup (Most Reliable)
```bash
whois example.com | grep -i "expir"
```
WHOIS always shows the exact expiration date.

### Domain Expiry Calculator
Enter any domain to instantly see: registration date, expiration date, days remaining, and domain age. Uses RDAP for accurate, real-time data.

### Registrar Dashboard
Log in to your domain registrar (GoDaddy, Namecheap, Cloudflare) and check the domains list.

## Prevention Checklist
- [ ] **Enable auto-renewal** on all domains
- [ ] **Keep payment method up to date** — auto-renewal fails if credit card is expired
- [ ] **Use dedicated email** for WHOIS/admin contact
- [ ] **Set calendar reminders** at 30 and 7 days before expiry
- [ ] **Renew for multiple years** — up to 10 years maximum, lock in your rate
- [ ] **Track all domains** in a spreadsheet or domain monitoring tool

## Domain Age Calculation
Domain Age = Today's Date - Registration Date

While Google states domain age is not a direct ranking factor, older domains often have accumulated more backlinks and authority over time.

## Free Tools
- [Domain Expiry Calculator](https://ipythoning.github.io/dns-tools/expiry-calculator.html) — Check expiry and age
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — Full registration details
- [SSL Certificate Checker](https://ipythoning.github.io/dns-tools/ssl-checker.html) — Check SSL certificate expiry
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All tools

## Related Telegraph Guides
- [Domain Expiry Calculator Complete Guide](https://telegra.ph/Domain-Expiry-Calculator--How-to-Track-Domain-Expiration-and-Avoid-Losing-Your-Domain-2026-06-12)
- [WHOIS Lookup Guide](https://telegra.ph/Free-WHOIS-Lookup--How-to-Check-Domain-Ownership-and-Registration-Details-2026-06-12)
- [How to Clear DNS Cache](https://telegra.ph/How-to-Clear-DNS-Cache--Complete-Guide-for-All-Platforms-2026-06-12)

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*
"""

gists = [
    ("What is DNS — A Beginner's Guide to Domain Name System (2026)", "what-is-dns-beginners-guide.md", gist_what_is_dns),
    ("Free WHOIS Lookup — How to Check Domain Ownership and Registration (2026)", "free-whois-lookup-guide.md", gist_whois),
    ("DNS Record Lookup — How to Query A, AAAA, MX, TXT, CNAME, NS Records (2026)", "dns-record-lookup-guide.md", gist_dns_lookup),
    ("SSL Certificate Checker — How to Verify SSL/TLS Certificates (2026)", "ssl-certificate-checker-guide.md", gist_ssl),
    ("Domain Expiry Calculator — Track Domain Expiration and Never Lose a Domain (2026)", "domain-expiry-calculator-guide.md", gist_expiry),
]

results = []
for desc, filename, content in gists:
    try:
        url = create_gist(desc, filename, content)
        print(f"✅ {desc}")
        print(f"   {url}")
        results.append({"description": desc, "url": url})
    except Exception as e:
        print(f"❌ {desc}: {e}")

print(f"\n=== Created {len(results)}/{len(gists)} Gists ===")
