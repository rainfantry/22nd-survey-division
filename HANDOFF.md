# 22nd Survey Division — Handoff Log
**OCCUPATION FORCE CALLSIGN GSW PTY. LTD. — ABN 50 692 429 397 — ACN 692 429 397**
Last updated: 2026-06-27

---

## LIVE SITE — WORKING NOW

**URL:** https://rainfantry.github.io/22nd-survey-division/
**Access PIN:** `668340`

### Flow
1. Click START LEARNING / VIEW CURRICULUM / any CTA
2. PIN gate appears
3. Enter `668340`
4. Gate unlocks → reader opens at Module 1
5. All 22 modules accessible via `?b=<MODULE_ID>` in reader URL

### Reader
`https://rainfantry.github.io/books/reader.html?b=01_OFFENSIVE_MINDSET`

### Repos
| Repo | Use | Status |
|---|---|---|
| rainfantry/22nd-survey-division | Landing page | LIVE |
| rainfantry/rainfantry.github.io | Reader + showcase images | LIVE |
| 22div-backend/ (local) | PHP+MySQL auth backend | DEPLOY WHEN READY |

---

## AUTH — TWO OPTIONS

### Option A — Client-side (LIVE NOW, free)
`var CORRECT = '668340'` in index.html
- PIN visible in page source
- Works offline, no server needed
- Change PIN by editing index.html and pushing

### Option B — SQL Backend (ready to deploy, needs cPanel)
Files at: `C:\Users\gwu07\Desktop\repos\22div-backend\`
- Argon2id hashed PIN in MySQL
- Rate limiting (5 attempts / 15 min / IP)
- HMAC-SHA256 session tokens
- See `DEPLOY.md` for 7-step cPanel setup

**cPanel:** https://S06ee.syd5.hostingplatform.net.au:2083
Login: `divcom22` / (password in env)

---

## PAYMENT INTEGRATION (next step)

See `PAYMENT_INTEGRATION.md` in this repo.
Summary:
- **Stripe:** hosted checkout, webhook → email PIN to buyer
- **Square:** AU-friendly, same flow
- When paid, auto-email `668340` (or a per-customer PIN from DB)

---

## SOCIAL MEDIA / CAMPAIGN

See `SOCIAL_MEDIA_CAMPAIGN.md` in this repo.
- 12 LinkedIn posts (ready to copy-paste)
- 8 Instagram captions
- Hashtag sets
- Post schedule

---

## SEO — LIVE

- Lighthouse SEO: 100
- Schema.org: Organization + Course
- ABN/ACN in structured data
- og:image, Twitter cards, keywords, canonical

---

## PROOF SECTION — 13 REAL SCREENSHOTS

All AI screenshots replaced. Every proof card = real tool output.

| Card | Image |
|---|---|
| IRON-DOME v4.0.0 | iron_dome_build_complete_154613.jpg |
| KILL CHAIN 10/10 | iron_dome_v4_killchain.png |
| MODULE 12 AV EVASION | Defender_Quarantine_GaySun.png |
| MODULE 11 ROOTKITS | UnDefend_Engine_Unavailable.png |
| RESPONSIBLE DISCLOSURE | MSRC_VULN195458_Submission.png |
| VULNERABILITY RESEARCH | TOCTOU_Exploit_Live_Execution.png |
| MODULE 21 MOBILE | starkiller_agents_live.png |
| MODULE 9 MALWARE | eclipse_c2_browser_live.png |
| RECON/PRIVESC | winrecon_skywalker_findings.jpg |
| MODULE 16 C2 | iron_dome_v4_vnc_terminal.png |
| FLAGSHIP REVERSE SHELL | eclipse_c2_gps_live.png |
| FLAGSHIP VERDICT PASS | Defender_Quarantine_RoguePlanet.png |
| IRON-DOME SUITE | iron_dome_kill_chain_154619.jpg |

---

## COURSE — 22 MODULES

| # | ID | Topic |
|---|---|---|
| 01 | 01_OFFENSIVE_MINDSET | Attacker psychology, threat model |
| 02 | 02_RECON | winrecon, AD enum, footprinting |
| 03 | 03_VULNERABILITY_RESEARCH | TOCTOU, CVE, MSRC |
| 04 | 04_MITIGATIONS | ASLR, DEP, AMSI, ETW architecture |
| 05 | 05_EXPLOIT_DEVELOPMENT | Shellcode, stagers, primitives |
| 06 | 06_WINDOWS_INTERNALS | PEB, VAD, handles, kernel |
| 07 | 07_EXPLOIT_PRIMITIVES | UAF, heap spray, type confusion |
| 08 | 08_PRIVILEGE_ESCALATION | winrecon CWE scanner, token abuse |
| 09 | 09_MALWARE_DEVELOPMENT | iron-sun, eclipse, payload pipeline |
| 10 | 10_CODE_INJECTION | Hollowing, reflective DLL, APC |
| 11 | 11_ROOTKITS | vader-rootkit, HWBP, AMSI/ETW bypass |
| 12 | 12_AV_EVASION | IRON-DOME 8-layer stack |
| 13 | 13_MEMORY_FORENSICS | Volatility, artifacts, cleanup |
| 14 | 14_REVERSE_ENGINEERING | Ghidra, x64dbg, IDA |
| 15 | 15_POST_EXPLOITATION | Persistence, lateral movement |
| 16 | 16_COMMAND_AND_CONTROL | cheyanne C2, beacons, Discord bridge |
| 17 | 17_NETWORK_WARFARE | Covert channels, CDN exfil |
| 18 | 18_CRYPTOGRAPHY_EVASION | ghost-encoder, LSB steganography |
| 19 | 19_LIVING_OFF_THE_LAND | LOLBins, certutil, WMIC |
| 20 | 20_ACTIVE_DIRECTORY | Kerberoast, DCSync, BloodHound |
| 21 | 21_MOBILE_SECURITY | starkiller RAT, APK bypass |
| 22 | 22_OSINT | OSINT framework, social engineering |

---

## NEXT STEPS

1. ✅ Test now: go to site, enter 668340, click through modules
2. 💰 Get cPanel → run DEPLOY.md → SQL backend live → remove client-side PIN
3. 💳 Add Stripe/Square → auto-email PIN on purchase
4. 📣 Post LinkedIn campaign (see SOCIAL_MEDIA_CAMPAIGN.md)
5. 📸 Post Instagram with tool screenshots
6. 🔍 Submit sitemap to Google Search Console
7. 📦 Tag v1.0 release (done — see GitHub Releases)
