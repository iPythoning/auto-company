#!/usr/bin/env python3
"""Cycle 171: 创建 4 篇新 Telegraph 文章 + 所有对应 Gists"""

import json
import os
import urllib.request
import urllib.parse
import subprocess
import sys

TOKEN = os.environ.get("TELEGRAPH_ACCESS_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAPH_ACCESS_TOKEN environment variable not set")
AUTHOR = "DNS Tools Team"
DNS_TOOLS_URL = "https://ipythoning.github.io/dns-tools/"

def create_telegraph_page(title, content_nodes):
    """Create a Telegraph page and return the URL"""
    url = "https://api.telegra.ph/createPage"
    data = urllib.parse.urlencode({
        "access_token": TOKEN,
        "title": title,
        "author_name": AUTHOR,
        "content": json.dumps(content_nodes),
        "return_content": "false"
    }).encode()

    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())

    if not result.get("ok"):
        raise Exception(f"Telegraph API error: {result}")

    return result["result"]["url"]


def create_gist(description, filename, content):
    """Create a public GitHub Gist and return the URL"""
    result = subprocess.run(
        ["gh", "gist", "create", "--public", "-d", description, "-f", filename],
        input=content.encode(),
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Gist creation failed: {result.stderr}")
    return result.stdout.strip()


def p(text):
    return {"tag": "p", "children": [text]}

def h3(text):
    return {"tag": "h3", "children": [text]}

def h4(text):
    return {"tag": "h4", "children": [text]}

def ul(items):
    return {"tag": "ul", "children": [{"tag": "li", "children": [item]} for item in items]}

def ol(items):
    return {"tag": "ol", "children": [{"tag": "li", "children": [item]} for item in items]}

def link(text, href):
    return {"tag": "a", "attrs": {"href": href}, "children": [text]}


# ============ ARTICLE DEFINITIONS ============

articles = []

# --- Article 7: WHOIS Lookup Guide ---
articles.append({
    "title": "Free WHOIS Lookup — How to Check Domain Ownership and Registration Details (2026)",
    "slug": "Free-WHOIS-Lookup--How-to-Check-Domain-Ownership-and-Registration-Details-2026",
    "nodes": [
        p("Looking up WHOIS information is one of the first steps when investigating a domain — whether you're checking if a domain is available, verifying ownership, or troubleshooting a website. This guide covers everything you need to know about WHOIS lookups in 2026."),

        h3("What is WHOIS?"),
        p("WHOIS is a protocol used to query databases that store registered domain information. When someone registers a domain, their registrar collects contact details (or privacy-protected versions of them) and makes them available through WHOIS servers. Think of it as the phonebook of the internet — it tells you who owns a domain name, when it was registered, and when it expires."),
        p("Key information available through WHOIS includes:"),
        ul([
            "Registrar name (e.g., GoDaddy, Namecheap, Cloudflare)",
            "Registration and expiration dates",
            "Nameservers (where the domain's DNS is managed)",
            "Registrant contact information (often redacted for privacy)",
            "Domain status (active, pending delete, etc.)"
        ]),

        h3("RDAP vs WHOIS: What's the Difference?"),
        p("The Registration Data Access Protocol (RDAP) is the modern replacement for the traditional WHOIS protocol. While WHOIS returns plain text, RDAP returns structured JSON data — making it much easier for tools and applications to parse. ICANN has mandated RDAP support for all gTLD registries and registrars since 2019."),
        p("Advantages of RDAP over traditional WHOIS:"),
        ul([
            "Structured JSON responses instead of free-form text",
            "Standardized field names across registrars",
            "Built-in support for internationalized domain names",
            "HTTPS-based access with better security",
            "Differentiated access levels (public vs. authenticated)"
        ]),

        h3("How to Perform a WHOIS Lookup"),
        p("Method 1: Command Line — Most operating systems come with a built-in whois command:"),
        p("whois example.com"),
        p("For RDAP queries, you can use curl:"),
        p("curl -s https://rdap.verisign.com/com/v1/domain/example.com"),
        p("Method 2: Online WHOIS Tools — Use a free WHOIS lookup tool for instant results. Our WHOIS lookup tool uses RDAP for accurate, structured results. You just enter a domain name and instantly get registration details, expiry status, and nameserver information."),
        p("Method 3: Registrar Websites — Every ICANN-accredited registrar provides WHOIS lookup on their website, though the interface varies by provider."),

        h3("Understanding WHOIS Privacy and GDPR"),
        p("In 2018, GDPR changed WHOIS dramatically. Before GDPR, anyone could see the full contact details of domain owners. Now, most personal information is redacted for domains owned by individuals in the EU. Many registrars now offer WHOIS privacy protection by default, displaying 'REDACTED FOR PRIVACY' or the registrar's proxy information instead of the actual owner's details."),

        h3("Common WHOIS Status Codes"),
        ul([
            "clientTransferProhibited — Domain cannot be transferred to another registrar",
            "serverTransferProhibited — Registry-level transfer lock",
            "clientUpdateProhibited — Domain settings cannot be modified",
            "clientDeleteProhibited — Domain cannot be deleted",
            "ok — The domain is active with no restrictions",
            "pendingDelete — Domain is in the redemption period (about to be released)",
            "redemptionPeriod — Domain expired but can be restored (usually with a fee)"
        ]),

        h3("When to Check WHOIS"),
        ul([
            "Before buying a domain — verify it's not stolen or involved in disputes",
            "Checking expiration dates — avoid accidentally letting domains expire",
            "Troubleshooting DNS — verify nameservers are correctly configured",
            "Security investigation — identify potentially malicious domains",
            "Competitive research — understand when competitors registered their domains"
        ]),

        h3("Try Our Free WHOIS Lookup Tool"),
        p("Use our free online WHOIS lookup tool to instantly check any domain. It supports RDAP queries for modern, structured results."),
        p(link("DNS Tools — Free WHOIS Lookup", f"{DNS_TOOLS_URL}free-whois-lookup.html")),
        p(link("DNS Tools Homepage", DNS_TOOLS_URL)),

        h3("Related Guides"),
        ul([
            link("DNS Record Types Explained", f"{DNS_TOOLS_URL}dns-record-types.html"),
            link("How to Check DNS Records", f"{DNS_TOOLS_URL}how-to-check-dns-records.html"),
            link("What is DNS — Beginner's Guide", f"{DNS_TOOLS_URL}what-is-dns.html"),
            link("How to Check DNS Propagation", f"{DNS_TOOLS_URL}check-dns-propagation.html"),
        ]),
    ]
})

# --- Article 8: DNS Lookup Guide ---
articles.append({
    "title": "DNS Record Lookup — How to Query A, AAAA, MX, TXT, CNAME, NS Records (2026)",
    "slug": "DNS-Record-Lookup--How-to-Query-A-AAAA-MX-TXT-CNAME-NS-Records-2026",
    "nodes": [
        p("DNS record lookup is a fundamental tool for anyone managing websites or diagnosing DNS issues. Whether you're verifying your DNS changes propagated correctly or investigating a domain's email configuration, knowing how to query DNS records is essential. This guide covers all major record types and lookup methods."),

        h3("What is a DNS Record Lookup?"),
        p("A DNS record lookup queries DNS servers for specific record types associated with a domain. Think of it as asking the internet's phonebook: 'What's the IP address for example.com?' or 'Which servers handle email for example.com?' Each query type returns different information about the domain."),

        h3("Common DNS Record Types You Can Look Up"),

        h4("A Record (Address Record)"),
        p("Maps a domain name to an IPv4 address. This is the most fundamental DNS record — it tells browsers and applications which server IP to connect to. Example: example.com → 93.184.216.34"),

        h4("AAAA Record (IPv6 Address Record)"),
        p("Same as A records, but for IPv6 addresses. As the internet transitions to IPv6, these records are becoming increasingly important. Example: example.com → 2606:2800:220:1:248:1893:25c8:1946"),

        h4("CNAME Record (Canonical Name)"),
        p("Creates an alias from one domain to another. Instead of pointing to an IP, it points to another domain name. Commonly used for www subdomains. Example: www.example.com → example.com"),

        h4("MX Record (Mail Exchange)"),
        p("Specifies which mail servers handle email for the domain. Includes a priority number — lower numbers are tried first. Essential for email delivery. Example: example.com MX 10 mail.example.com"),

        h4("TXT Record (Text Record)"),
        p("Stores arbitrary text data. Most commonly used for SPF records (email authentication), DKIM keys, and domain verification tokens. Example: 'v=spf1 include:_spf.google.com ~all'"),

        h4("NS Record (Nameserver)"),
        p("Specifies which nameservers are authoritative for the domain. These are the servers that answer DNS queries for the domain. Example: example.com NS ns1.example.com"),

        h4("SOA Record (Start of Authority)"),
        p("Contains administrative information about the DNS zone, including the primary nameserver, admin email, serial number (for tracking changes), and timing parameters for caching and retries."),

        h3("How to Perform a DNS Record Lookup"),

        h4("Command Line: dig (Domain Information Groper)"),
        p("dig is the most powerful DNS lookup tool available on Linux, macOS, and WSL:"),
        p("dig example.com A        # Look up A record"),
        p("dig example.com MX       # Look up MX records"),
        p("dig example.com ANY      # Look up all records"),
        p("dig @8.8.8.8 example.com # Query specific DNS server"),

        h4("Command Line: nslookup"),
        p("nslookup is available on all platforms (including Windows) and is simpler than dig:"),
        p("nslookup example.com"),
        p("nslookup -type=mx example.com"),

        h4("Online DNS Lookup Tools"),
        p("For a quick, no-installation approach, use a free online DNS lookup tool:"),
        p("Our DNS record lookup tool queries Google's DNS-over-HTTPS service and returns A, AAAA, MX, TXT, CNAME, NS, and SOA records in one click. It's fast, free, and requires no technical knowledge."),

        h3("Troubleshooting Common DNS Lookup Issues"),
        ul([
            "NXDOMAIN — The domain doesn't exist. Double-check the spelling.",
            "SERVFAIL — The DNS server encountered an error. Try a different resolver.",
            "No records returned — The record type might not exist for that domain (e.g., no MX records if the domain doesn't handle email).",
            "Different results from different servers — DNS changes may still be propagating.",
            "DNS-over-HTTPS (DoH) vs traditional DNS — DoH encrypts your queries; some network configurations may block it."
        ]),

        h3("Try Our Free DNS Record Lookup Tool"),
        p("We built a free DNS record lookup tool that checks A, AAAA, MX, TXT, CNAME, NS, and SOA records in one query using Google's DNS-over-HTTPS service. No registration required."),
        p(link("DNS Tools — Free DNS Record Lookup", f"{DNS_TOOLS_URL}dns-lookup.html")),
        p(link("DNS Tools Homepage", DNS_TOOLS_URL)),

        h3("Related Guides"),
        ul([
            link("DNS Record Types Explained — Complete Guide", f"{DNS_TOOLS_URL}dns-record-types.html"),
            link("How to Check DNS Propagation", f"{DNS_TOOLS_URL}check-dns-propagation.html"),
            link("How to Clear DNS Cache", f"{DNS_TOOLS_URL}clear-dns-cache.html"),
            link("What is DNS — Beginner's Guide", f"{DNS_TOOLS_URL}what-is-dns.html"),
        ]),
    ]
})

# --- Article 9: SSL Certificate Checker Guide ---
articles.append({
    "title": "SSL Certificate Checker — How to Verify SSL/TLS Certificates and Avoid Expiry (2026)",
    "slug": "SSL-Certificate-Checker--How-to-Verify-SSL-TLS-Certificates-and-Avoid-Expiry-2026",
    "nodes": [
        p("SSL/TLS certificates are the foundation of web security. An expired or misconfigured certificate means browsers will show scary warnings to your visitors — costing you trust and traffic. This guide explains how to check SSL certificates, understand common issues, and never let a certificate expire again."),

        h3("What is an SSL/TLS Certificate?"),
        p("An SSL (Secure Sockets Layer) or TLS (Transport Layer Security) certificate is a digital certificate that authenticates a website's identity and enables an encrypted connection. When you see the padlock icon in your browser's address bar, that's SSL/TLS at work."),
        p("SSL/TLS certificates serve three purposes:"),
        ol([
            "Encryption — All data between browser and server is encrypted, protecting passwords, credit card numbers, and personal information.",
            "Authentication — The certificate verifies that you're connected to the real website, not an imposter.",
            "Trust — Certificate Authorities (CAs) validate domain ownership before issuing certificates."
        ]),

        h3("Types of SSL Certificates"),
        ul([
            "Domain Validated (DV) — Basic validation. CA only verifies you control the domain. Issued in minutes. Suitable for blogs and personal sites.",
            "Organization Validated (OV) — CA verifies the organization's identity. Shows company name in certificate details. Suitable for business websites.",
            "Extended Validation (EV) — Most rigorous validation. Shows company name in the browser address bar. Used by banks and large enterprises.",
            "Wildcard — Covers a domain AND all its subdomains (e.g., *.example.com).",
            "Multi-Domain (SAN) — Covers multiple different domains in a single certificate."
        ]),

        h3("How to Check an SSL Certificate"),

        h4("Browser Method"),
        p("Click the padlock icon in your browser's address bar → 'Connection is secure' → 'Certificate is valid'. This shows you the issuer, validity period, and certificate details."),

        h4("Command Line: openssl"),
        p("openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>/dev/null | openssl x509 -noout -dates -subject -issuer"),
        p("This returns the certificate's validity dates, subject (who it was issued to), and issuer (who issued it)."),

        h4("Online SSL Checker Tools"),
        p("Use a free SSL certificate checker for instant results including:"),
        ul([
            "Certificate validity period (issued and expiry dates)",
            "Issuer (Certificate Authority like Let's Encrypt, DigiCert, etc.)",
            "Subject Alternative Names (SANs) — all domains the certificate covers",
            "Certificate chain validation — is the full chain of trust intact?",
            "Days remaining until expiry"
        ]),

        h3("Common SSL Certificate Issues"),
        ul([
            "Certificate Expired — The most common issue. Certificates have a maximum validity of 398 days (since 2020). Set up auto-renewal!",
            "Certificate Name Mismatch — The domain in the URL doesn't match the name on the certificate. Common with www vs non-www redirects.",
            "Self-Signed Certificate — Not trusted by browsers. Only use for testing/development.",
            "Incomplete Certificate Chain — The server doesn't send intermediate certificates, breaking the chain of trust.",
            "Mixed Content — HTTPS page loads HTTP resources (images, scripts). The padlock disappears or shows a warning.",
            "Obsolete Protocol/Cipher — Using old TLS versions (1.0, 1.1) or weak ciphers that modern browsers reject."
        ]),

        h3("Preventing Certificate Expiry"),
        p("Let's Encrypt provides free SSL certificates with 90-day validity. Their Certbot tool can automatically renew certificates — set up a cron job and forget about manual renewals. Most hosting platforms (Cloudflare, Netlify, Vercel) provide free auto-renewing SSL certificates out of the box."),

        h3("Try Our Free SSL Certificate Checker"),
        p("Check any website's SSL certificate instantly — issuer, expiry date, days remaining, and certificate chain validation."),
        p(link("DNS Tools — Free SSL Certificate Checker", f"{DNS_TOOLS_URL}ssl-checker.html")),
        p(link("DNS Tools Homepage", DNS_TOOLS_URL)),

        h3("Related Guides"),
        ul([
            link("DNS Record Types Explained", f"{DNS_TOOLS_URL}dns-record-types.html"),
            link("Free WHOIS Lookup Guide", f"{DNS_TOOLS_URL}free-whois-lookup.html"),
            link("What is DNS — Beginner's Guide", f"{DNS_TOOLS_URL}what-is-dns.html"),
        ]),
    ]
})

# --- Article 10: Domain Expiry Calculator Guide ---
articles.append({
    "title": "Domain Expiry Calculator — How to Track Domain Expiration and Avoid Losing Your Domain (2026)",
    "slug": "Domain-Expiry-Calculator--How-to-Track-Domain-Expiration-and-Avoid-Losing-Your-Domain-2026",
    "nodes": [
        p("Forgetting to renew a domain can be catastrophic — you could lose your website, email, and brand. Google famously forgot to renew google.com in 2015 (a former employee bought it for $12 before Google got it back). This guide explains how to track domain expiration dates, understand the domain lifecycle, and never miss a renewal."),

        h3("Why Domain Expiry Matters"),
        p("When a domain expires, it doesn't immediately disappear. Instead, it goes through a lifecycle with several stages — each giving you a chance to renew. Understanding this lifecycle can save you from permanently losing a valuable domain."),

        h3("The Domain Expiration Lifecycle"),

        h4("Stage 1: Active (Registration Period)"),
        p("Your domain is active and working normally. You registered it for 1-10 years. During this period, you can transfer to another registrar, update DNS settings, or renew to extend the registration."),

        h4("Stage 2: Expired (Grace Period — 0-45 days)"),
        p("The domain has expired but you can still renew it at the regular price. Your website and email stop working. The registrar may show a parking page. Most registrars offer a grace period of 30-45 days."),

        h4("Stage 3: Redemption Period (30 days)"),
        p("After the grace period, the domain enters redemption. You can still get it back, but there's usually a significant restoration fee ($80-$300+). The domain is still in your name but not functional."),

        h4("Stage 4: Pending Delete (5 days)"),
        p("The final stage before the domain is released back to the public. You cannot recover the domain at this point. After 5 days, it becomes available for anyone to register."),

        h3("How to Check Domain Expiration"),
        ul([
            "WHOIS Lookup — The most reliable method. WHOIS always shows the exact expiration date.",
            "Registrar Dashboard — Log in to your domain registrar and check the expiration column.",
            "Domain Expiry Calculator — Use our free tool to calculate days remaining and get the exact expiry date from a WHOIS lookup.",
            "ICANN Lookup — The official ICANN WHOIS at lookup.icann.org shows registration and expiration dates for all gTLDs."
        ]),

        h3("Auto-Renewal Best Practices"),
        ol([
            "Enable auto-renewal on all domains — it's the simplest way to prevent accidental expiration.",
            "Keep your payment method up to date — auto-renewal fails if your credit card is expired.",
            "Use a dedicated email address — make sure your registrar can reach you if auto-renewal fails.",
            "Set calendar reminders — even with auto-renewal, set reminders 30 and 7 days before expiry.",
            "Renew for multiple years — domain registration can be extended up to 10 years. Lock in your rate and reduce renewal anxiety."
        ]),

        h3("Calculating Domain Age"),
        p("Domain age is a factor some people consider for SEO and credibility. The formula is simple:"),
        p("Domain Age = Today's Date - Registration Date"),
        p("Older domains are sometimes perceived as more trustworthy, though Google has stated that domain age is not a direct ranking factor. However, older domains may have accumulated more backlinks and authority over time."),

        h3("Try Our Free Domain Expiry Calculator"),
        p("Enter any domain to instantly see registration date, expiration date, days remaining, and domain age. Uses RDAP for accurate, real-time data."),
        p(link("DNS Tools — Free Domain Expiry Calculator", f"{DNS_TOOLS_URL}expiry-calculator.html")),
        p(link("DNS Tools Homepage", DNS_TOOLS_URL)),

        h3("Related Guides"),
        ul([
            link("Free WHOIS Lookup — Complete Guide", f"{DNS_TOOLS_URL}free-whois-lookup.html"),
            link("DNS Record Types Explained", f"{DNS_TOOLS_URL}dns-record-types.html"),
            link("How to Check DNS Records", f"{DNS_TOOLS_URL}how-to-check-dns-records.html"),
            link("What is DNS — Beginner's Guide", f"{DNS_TOOLS_URL}what-is-dns.html"),
        ]),
    ]
})

# ============ ALSO: Gist for "What is DNS" (missing Gist #6) ============

what_is_dns_gist_content = """# What is DNS — A Beginner's Guide to Domain Name System (2026)

DNS (Domain Name System) is the phonebook of the internet. When you type `example.com` into your browser, DNS translates that human-readable domain name into a machine-readable IP address like `93.184.216.34`.

## How DNS Works (In 7 Steps)

1. **User types a URL** — You enter `example.com` in your browser
2. **DNS Resolver queries** — Your computer asks the DNS resolver (usually your ISP or a public resolver like 8.8.8.8)
3. **Root nameserver** — The resolver asks a root nameserver: "Who handles .com?"
4. **TLD nameserver** — The resolver asks the .com TLD server: "Who handles example.com?"
5. **Authoritative nameserver** — The resolver asks the authoritative nameserver: "What's the IP for example.com?"
6. **IP address returned** — The resolver gets the answer and caches it
7. **Browser connects** — Your browser uses the IP address to load the website

## Key DNS Concepts

### DNS Resolver
Also called a recursive resolver. This is the server your computer talks to first. It does all the work of traversing the DNS hierarchy to find your answer. Popular public resolvers include Google (8.8.8.8) and Cloudflare (1.1.1.1).

### DNS Caching
To speed up the internet, DNS results are cached at multiple levels: browser cache, OS cache, router cache, and resolver cache. Each cache has a TTL (Time To Live) that determines how long entries are kept before being refreshed.

### DNS Propagation
When you change DNS records (like pointing your domain to a new server), the changes don't take effect instantly everywhere. This delay is called DNS propagation, and it can take anywhere from a few minutes to 48 hours.

## Common DNS Record Types

| Record Type | Purpose | Example |
|------------|---------|---------|
| **A** | Maps domain to IPv4 address | example.com → 93.184.216.34 |
| **AAAA** | Maps domain to IPv6 address | example.com → 2606:2800:... |
| **CNAME** | Alias from one domain to another | www.example.com → example.com |
| **MX** | Mail server for email delivery | example.com MX 10 mail.example.com |
| **TXT** | Text data (SPF, DKIM, verification) | "v=spf1 include:_spf.google.com ~all" |
| **NS** | Authoritative nameservers | example.com NS ns1.example.com |
| **PTR** | Reverse DNS (IP → domain name) | 93.184.216.34 → example.com |
| **SOA** | Zone administrative information | Primary NS, admin email, serial number |
| **CAA** | Certificate Authority Authorization | Only Let's Encrypt can issue certs |

## DNS Security

- **DNSSEC** — Adds cryptographic signatures to DNS records to prevent DNS spoofing/cache poisoning
- **DNS over HTTPS (DoH)** — Encrypts DNS queries using HTTPS (port 443), hiding them in regular web traffic
- **DNS over TLS (DoT)** — Encrypts DNS queries using TLS on a dedicated port (853)

## Free Online DNS Tools

- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query A, AAAA, MX, TXT, CNAME, NS, SOA records
- [DNS Record Types Reference](https://ipythoning.github.io/dns-tools/dns-record-types.html) — Complete guide to all DNS record types
- [Check DNS Propagation](https://ipythoning.github.io/dns-tools/check-dns-propagation.html) — Check if DNS changes propagated globally
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — Check domain registration details
- [Clear DNS Cache](https://ipythoning.github.io/dns-tools/clear-dns-cache.html) — Guide for all platforms

---

*Part of the [DNS Tools](https://ipythoning.github.io/dns-tools/) collection — free DNS tools and guides.*
"""

# ============ EXECUTION ============

results = []

print("=== Cycle 171: Creating Telegraph Articles & Gists ===\n")

# Phase 1: Create 4 new Telegraph articles
for i, article in enumerate(articles):
    print(f"[Telegraph] Creating article {i+7}: {article['title'][:80]}...")
    try:
        url = create_telegraph_page(article["title"], article["nodes"])
        print(f"  ✅ {url}")
        results.append({"type": "telegraph", "index": i+7, "title": article["title"], "url": url})
    except Exception as e:
        print(f"  ❌ Failed: {e}")

# Phase 2: Create "What is DNS" Gist (missing from cycle 170)
print(f"\n[Gist] Creating 'What is DNS' (missing Gist #6)...")
try:
    url = create_gist(
        "What is DNS — A Beginner's Guide to Domain Name System (2026)",
        "what-is-dns-beginners-guide.md",
        what_is_dns_gist_content
    )
    print(f"  ✅ {url}")
    results.append({"type": "gist", "topic": "What is DNS", "url": url})
except Exception as e:
    print(f"  ❌ Failed: {e}")

# Phase 3: Create Gists for new Telegraph articles
gist_topics = [
    ("Free WHOIS Lookup Guide", "free-whois-lookup-guide.md", """# Free WHOIS Lookup — How to Check Domain Ownership and Registration Details (2026)

WHOIS is the internet's domain phonebook. It tells you who registered a domain, when, and when it expires. This guide covers both traditional WHOIS and the modern RDAP protocol.

## What WHOIS Tells You
- **Registrar** — Which company manages the domain (GoDaddy, Namecheap, Cloudflare, etc.)
- **Registration & Expiration Dates** — When the domain was created and when it expires
- **Nameservers** — Where the domain's DNS is hosted
- **Domain Status** — Active, pending delete, locked, etc.
- **Registrant Info** — Often redacted for privacy (GDPR)

## RDAP vs WHOIS
RDAP (Registration Data Access Protocol) is the modern replacement for WHOIS. Key advantages:
- **JSON output** — Easy for tools to parse
- **Standardized fields** — Consistent across all registrars
- **HTTPS** — Better security than plain-text WHOIS
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

### Online Tools
Use a free WHOIS lookup tool for instant, structured results.

## WHOIS Status Codes
- **clientTransferProhibited** — Transfer locked
- **ok** — Domain active, no restrictions
- **pendingDelete** — About to be released to public
- **redemptionPeriod** — Expired but can be restored (fee applies)

## GDPR and Privacy
Since 2018, GDPR requires redaction of personal data for EU residents. Most registrars now offer WHOIS privacy by default.

## Free Tools
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — Check any domain's registration details
- [Domain Expiry Calculator](https://ipythoning.github.io/dns-tools/expiry-calculator.html) — Track domain expiration
- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query DNS records
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All tools

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*"""),

    ("DNS Record Lookup Guide", "dns-record-lookup-guide.md", """# DNS Record Lookup — How to Query A, AAAA, MX, TXT, CNAME, NS Records (2026)

DNS record lookup lets you query what records exist for any domain. Essential for troubleshooting, verifying DNS changes, and investigating domain configurations.

## Common DNS Record Types

| Record | Purpose | Example |
|--------|---------|---------|
| **A** | Domain → IPv4 | example.com → 93.184.216.34 |
| **AAAA** | Domain → IPv6 | example.com → 2606:2800:... |
| **CNAME** | Domain alias | www → example.com |
| **MX** | Mail server | example.com MX 10 mail.example.com |
| **TXT** | Text data (SPF/DKIM) | "v=spf1 include:_spf.google.com ~all" |
| **NS** | Nameserver | example.com NS ns1.example.com |
| **SOA** | Zone admin info | Primary NS, serial, TTL |
| **PTR** | Reverse DNS | IP → domain name |
| **SRV** | Service location | _sip._tcp.example.com |
| **CAA** | Cert Authority restriction | Only Let's Encrypt |

## How to Query DNS Records

### dig (Linux/macOS)
```bash
dig example.com A        # Look up A record
dig example.com MX       # Mail servers
dig example.com ANY      # All records
dig @8.8.8.8 example.com # Query specific resolver
```

### nslookup (All platforms)
```bash
nslookup example.com
nslookup -type=mx example.com
```

### Online Tools
Use a free DNS lookup tool for instant results across multiple record types.

## Troubleshooting
- **NXDOMAIN** — Domain doesn't exist
- **SERVFAIL** — DNS server error, try different resolver
- **No records** — Record type may not exist for that domain
- **Inconsistent results** — DNS propagation still in progress

## Free DNS Tools
- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query all record types
- [DNS Record Types](https://ipythoning.github.io/dns-tools/dns-record-types.html) — Complete reference
- [Check DNS Propagation](https://ipythoning.github.io/dns-tools/check-dns-propagation.html) — Global propagation checker
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All free tools

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*"""),

    ("SSL Certificate Checker Guide", "ssl-certificate-checker-guide.md", """# SSL Certificate Checker — How to Verify SSL/TLS Certificates (2026)

SSL/TLS certificates secure websites with encryption. An expired or misconfigured certificate means browsers show warnings to visitors — bad for trust and SEO.

## What SSL/TLS Certificates Do
1. **Encryption** — All data between browser and server is encrypted
2. **Authentication** — Verifies you're connected to the real website
3. **Trust** — Certificate Authorities validate domain ownership

## Certificate Types
- **Domain Validated (DV)** — Basic, issued in minutes
- **Organization Validated (OV)** — Company identity verified
- **Extended Validation (EV)** — Maximum validation, shows company name
- **Wildcard** — Covers all subdomains (*.example.com)
- **Multi-Domain (SAN)** — Multiple domains in one cert

## How to Check SSL Certificates

### Browser
Click the padlock → "Connection is secure" → "Certificate is valid"

### Command Line (openssl)
```bash
openssl s_client -connect example.com:443 -servername example.com < /dev/null 2>/dev/null | openssl x509 -noout -dates -subject -issuer
```

### Online SSL Checker
Get instant results: validity dates, issuer, SANs, chain validation, days until expiry.

## Common Issues
- **Certificate expired** — Most common problem, set up auto-renewal
- **Name mismatch** — www vs non-www misconfiguration
- **Self-signed** — Not trusted by browsers
- **Incomplete chain** — Missing intermediate certificates
- **Mixed content** — HTTPS page loading HTTP resources

## Let's Encrypt
Free SSL certificates with 90-day validity. Use Certbot for auto-renewal:
```bash
certbot --nginx -d example.com
```

## Free Tools
- [SSL Certificate Checker](https://ipythoning.github.io/dns-tools/ssl-checker.html) — Check any website's SSL
- [DNS Record Lookup](https://ipythoning.github.io/dns-tools/dns-lookup.html) — Query DNS records
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — Domain registration details
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All tools

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*"""),

    ("Domain Expiry Calculator Guide", "domain-expiry-calculator-guide.md", """# Domain Expiry Calculator — Track Domain Expiration and Never Lose a Domain (2026)

Forgetting to renew a domain can be catastrophic. Google famously forgot to renew google.com in 2015. This guide explains the domain lifecycle and how to never miss a renewal.

## Domain Lifecycle Stages

| Stage | Duration | Can Renew? | Cost |
|-------|----------|------------|------|
| **Active** | 1-10 years | ✅ | Regular price |
| **Grace Period** | 0-45 days | ✅ | Regular price |
| **Redemption** | 30 days | ✅ | $80-$300+ |
| **Pending Delete** | 5 days | ❌ | Cannot recover |

**After pending delete → domain becomes available to anyone.**

## How to Check Expiration

### WHOIS Lookup
Most reliable method. Always shows exact expiration date.
```bash
whois example.com | grep "Expiry Date"
```

### Online Expiry Calculator
Enter a domain to see: registration date, expiration date, days remaining, domain age.

### Registrar Dashboard
Log in to your registrar (GoDaddy, Namecheap, Cloudflare, etc.) and check the domains list.

## Prevention Checklist
- [ ] **Enable auto-renewal** on all domains
- [ ] **Keep payment method current**
- [ ] **Use dedicated email** for WHOIS/admin contact
- [ ] **Set calendar reminders** at 30 and 7 days before expiry
- [ ] **Renew for multiple years** (up to 10 years maximum)
- [ ] **Track all domains** in a spreadsheet or domain monitor

## Domain Age Calculation
Domain Age = Today - Registration Date

While Google says domain age isn't a direct ranking factor, older domains often have more backlinks and authority.

## Free Tools
- [Domain Expiry Calculator](https://ipythoning.github.io/dns-tools/expiry-calculator.html) — Check any domain's expiry and age
- [WHOIS Lookup](https://ipythoning.github.io/dns-tools/free-whois-lookup.html) — Full domain registration details
- [SSL Certificate Checker](https://ipythoning.github.io/dns-tools/ssl-checker.html) — Check SSL expiry
- [DNS Tools Homepage](https://ipythoning.github.io/dns-tools/) — All free tools

---

*Part of [DNS Tools](https://ipythoning.github.io/dns-tools/) — free DNS tools and guides.*"""),
]

print("\n[Gists] Creating Gists for new Telegraph articles...")
for i, (desc, filename, content) in enumerate(gist_topics):
    print(f"  [{i+1}] {desc}...")
    try:
        url = create_gist(desc, filename, content)
        print(f"    ✅ {url}")
        results.append({"type": "gist", "topic": desc, "url": url})
    except Exception as e:
        print(f"    ❌ Failed: {e}")

print("\n=== Summary ===")
for r in results:
    print(f"  [{r['type']}] {r.get('index', '')} {r.get('title', r.get('topic', ''))}: {r['url']}")

print(f"\nTotal: {len(results)} assets created")
