# 22nd Survey Division
## Offensive Security Training — Windows Internals, AV Evasion, C2 Frameworks
### Classification: PUBLIC COURSE SITE

---

## WHAT THIS IS

22nd Survey Division is an Australian offensive security training platform built from live research — not sanitized tutorial content. 22 modules covering Windows internals, malware development, rootkits, C2 frameworks, Android RATs, and social engineering. Every technique taught from first principles with real tools tested against live AV engines.

**Built by:** George Wu (VADER) — Windows security researcher, Sydney  
**Entity:** OCCUPATION FORCE CALLSIGN GSW PTY LTD (ACN 692 429 397)  
**Research:** MSRC VULN-195458 (Windows Defender Tamper Protection bypass, responsibly disclosed)

---

## COURSE OVERVIEW

| Module | Title | Tool Repo | Price |
|--------|-------|-----------|-------|
| 01 | Offensive Mindset | — | $29 |
| 02 | Recon & Footprinting | winrecon | $39 |
| 03 | Vulnerability Research | csec-research-authorization | $49 |
| 04 | Mitigations | — | $29 |
| 05 | Exploit Development | — | $49 |
| 06 | Windows Internals | — | $39 |
| 07 | Exploit Primitives | — | $49 |
| 08 | Privilege Escalation | winrecon | $69 |
| 09 | Malware Development | iron-sun + eclipse | $79 |
| 10 | Code Injection | iron-sun | $69 |
| 11 | Rootkits | vader-rootkit | $79 |
| 12 | Antivirus Evasion | iron-sun + eclipse + vader-rootkit | $79 |
| 13 | Memory Forensics | flagship | $59 |
| 14 | Reverse Engineering | — | $49 |
| 15 | Post-Exploitation | flagship | $79 |
| 16 | Command & Control | cheyanne | $79 |
| 17 | Network Warfare | winrecon | $59 |
| 18 | Cryptography Evasion | iron-sun + eclipse | $59 |
| 19 | Living Off the Land | — | $39 |
| 20 | Active Directory | winrecon | $69 |
| 21 | Mobile Security | starkiller | $79 |
| 22 | OSINT & Social Engineering | — | $39 |

**Full Bundle:** $497 AUD (all 22 modules + 5 private repos + lifetime access)  
**Monthly:** $21.99 AUD/mo (private repo access, cancel anytime)

---

## THE TOOLS (Included in Full Bundle)

### VADER-ROOTKIT
Hardware breakpoint bypass for AMSI + ETW. Zero memory writes. 26 Defender-clean binaries. MSRC VULN-195458 research.

**Wartime test:** Windows 11, Defender RTP + cloud + BehaviorMonitor — CLEAN. Kaspersky Premium — CLEAN. 0/72 VirusTotal projection.

### IRON-SUN
8-layer AV evasion stack. TCP reverse shell. XOR obfuscation, dynamic API resolution, anti-sandbox timing, PE header stomping, ISUN auth gate, beacon jitter, MinGW compile, HWBP bypass.

**Wartime test:** 10/10 POCs verified on live machine (192.168.1.92). Kaspersky Premium 21.25 — 0 detections. All layers active.

### CHEYANNE C2
Full C2 framework. Browser-based operator panel. GPS exfil, VNC shell, AES-256-CBC beacon, Discord bridge, service persistence.

**Wartime test:** 2 agents live. GPS polling 5s. SMS dump 47 messages. Play Protect bypassed. Built in Kotlin.

### GHOST-ENCODER
Zero-width Unicode steganography. Covert channel framework. 16-character invisible alphabet. PNG carrier implementation.

**Wartime test:** Payload hidden in Discord message. Entropy 0.12 (normal text range). 0/72 VirusTotal. Kaspersky CLEAN.

### WINRECON
Windows reconnaissance framework. Process enumeration, privilege escalation checks, network mapping, service enumeration.

**Wartime test:** 1229 lines of output. Standard user context. Defender OFF, Kaspersky ACTIVE. 2 writable SYSTEM services found.

---

## LIVE WIDGETS

15 interactive widgets demonstrating techniques in real-time:

| Widget | Demo |
|--------|------|
| VADER | HWBP bypass runtime — DR0/DR1 set, AMSI/ETW silenced |
| IRON-DOME | 8-layer compile + AV scan simulation + kill chain |
| Networking 101 | OSI model ↔ TCP/IP stack switching |
| Recon | WINRECON ↔ GHOST-SCRAPER tab switching |
| Terminal 101 | IPCONFIG ↔ PROCESSES live output |
| Privesc | TOKENS ↔ JUICYPOTATO privilege escalation |
| Kill Chain | All 7 phases: Recon → Weaponize → Deliver → Exploit → Install → C2 → Actions |
| Shellcode | Assembly BUILD with runtime compilation |
| WinRecon | IDENTITY ↔ PRIVILEGES enumeration |

---

## INFRASTRUCTURE

**Current:** GitHub Pages (free, fast, CDN)  
**Domain:** rainfantry.github.io/22nd-survey-division  
**Target:** Custom domain + cPanel when revenue justifies ($500+/mo)  
**Payment:** Stripe (cards) + Wise (bank transfer) + Invoice (corporate)  
**Delivery:** AES-256 encrypted 7z archive, PIN emailed within 24h

**Migration roadmap:** See [22sd-battle-plan](https://github.com/rainfantry/22sd-battle-plan) (private repo)

---

## HONESTY POLICY

This course teaches authorized security testing only. Every tool is tested on own hardware or authorized lab environments. MSRC responsible disclosure filed for all Microsoft-related findings.

**No false claims:**
- Every AV result is from live testing, not speculation
- Every screenshot is from real execution, not mockups
- Every module teaches why it works, not just how to copy it
- Every tool includes honest limitations and detection vectors

**What you won't learn here:**
- How to hack random people (illegal and immoral)
- How to evade law enforcement (impossible and stupid)
- How to get rich quick (this is a trade, not a lottery)

**What you will learn:**
- How Windows actually works under the hood
- How AV/EDR detects threats and how to engineer around it
- How to build tools from first principles
- How to think like an attacker so you can defend like one

---

## DEDICATION

This project is dedicated to my parents, who came from nothing and gave me everything. To Cheyanne — the fighter who never stops battling for her health, whose defiance against the odds inspired every bypass that beats Defender and KAV. And to [RADON Associates](https://radonassociates.com.au) — for their partnership and support throughout my years growing up, turning a kid with a laptop into someone who could build things that matter.

---

## LEGAL

**Entity:** OCCUPATION FORCE CALLSIGN GSW PTY LTD  
**ABN:** 50 692 429 397  
**ACN:** 692 429 397  
**MSRC:** VULN-195458 (responsible disclosure)  
**Location:** Sydney, NSW, Australia

---

## CONTACT

- **Email:** gwu0738@gmail.com
- **LinkedIn:** [linkedin.com/in/georgewu108](https://linkedin.com/in/georgewu108)
- **GitHub:** [github.com/rainfantry](https://github.com/rainfantry)
- **Discord:** The Coalition (invite via email)

---

*VIDIMUS OMNIA — We see everything.*
