# 22nd Survey Division
## Offensive Security Training — From Zero to Nation-State Tradecraft
### Classification: PUBLIC COURSE SITE

---

## WHAT THIS IS

22nd Survey Division is an Australian offensive security training platform built from **live research** — not sanitized tutorial content. 22 modules covering Windows internals, malware development, rootkits, C2 frameworks, Android RATs, and social engineering. Every technique taught from first principles with real tools tested against live AV engines.

**Built by:** George Wu (VADER) — Windows security researcher, Sydney  
**Entity:** OCCUPATION FORCE CALLSIGN GSW PTY LTD (ACN 692 429 397)  
**Research:** MSRC VULN-195458 (Windows Defender Tamper Protection bypass, responsibly disclosed)

**Mentor:** [HTB] — Israeli offensive security specialist, former anti-virus engineer, IDF soldier. Teaches: "Save every rung." "Privilege escalation is easy." "Real attacks are carried remotely."

---

## QUICK LINKS — START HERE

| Page | What It Is | Link |
|------|-----------|------|
| **Main Site** | Course overview, pricing, proof | [rainfantry.github.io/22nd-survey-division](https://rainfantry.github.io/22nd-survey-division/) |
| **Crash Course** | 22 modules + mentor teachings + 8-week plan | [→ Crash Course](https://rainfantry.github.io/22nd-survey-division/crash-course.html) |
| **Practical Labs** | Step-by-step exercises, SSH tests, defense bypasses | [→ Practical Labs](https://rainfantry.github.io/22nd-survey-division/practical-labs.html) |
| **Module Tree** | Complete archive — every module, every link | [→ Module Tree](https://rainfantry.github.io/22nd-survey-division/module-tree.html) |
| **Resources** | Cheat sheets, command reference, mentor documents | [→ Resources](https://rainfantry.github.io/22nd-survey-division/resources.html) |

---

## HOW TO USE THIS COURSE — LAYMAN PATH

### If You Know Nothing (Start Here)

1. **Read the Crash Course** → [crash-course.html](https://rainfantry.github.io/22nd-survey-division/crash-course.html)
   - 22 modules organized in 5 phases
   - Mentor teachings explained in plain English
   - 8-week study plan with deliverables

2. **Do the Practical Labs** → [practical-labs.html](https://rainfantry.github.io/22nd-survey-division/practical-labs.html)
   - Copy-paste commands
   - Expected outputs shown
   - "If this fails" troubleshooting for every step
   - Interactive quizzes with right/wrong feedback

3. **Check the Module Tree** → [module-tree.html](https://rainfantry.github.io/22nd-survey-division/module-tree.html)
   - See all modules at once
   - Click any module to jump to it
   - Status shows what's live vs pending

4. **Reference the Resources** → [resources.html](https://rainfantry.github.io/22nd-survey-division/resources.html)
   - Command cheat sheets (recon, privesc, persistence, defender, C2)
   - Mentor documents (WHAT_I_HAVE.md, PRIVESC_LADDER.md)
   - Tool downloads and build instructions

### Track A: Coders Learning Attack (12-Module Fast Path)

For people who already know Python, C, or PowerShell but want to learn offensive security.

| Order | Module | What You Learn |
|-------|--------|----------------|
| 1 | [Module 00: Reader](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_00_READER.html) | Course guide, lab setup, study methodology |
| 2 | [Module 01: Networking](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_01_NETWORKING.html) | OSI model, TCP/IP, ports, protocols, Wireshark |
| 3 | [Module 02: Recon](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_02_RECON.html) | Active/passive recon, OSINT, network mapping |
| 4 | [Module 04: Coding Basics](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_04_CODING_BASICS.html) | C, Python, Windows API for security |
| 5 | [Module 06: Memory](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_06_MEMORY.html) | Virtual memory, paging, heap vs stack, EPROCESS |
| 6 | [Module 10: Code Injection](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_10_CODE_INJECTION.html) | DLL injection, process hollowing, APC, reflective DLL |
| 7 | [Module 08: Privilege Escalation](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_08_PRIVESC.html) | Token abuse, service misconfig, unquoted paths, UAC bypass |
| 8 | [Module 09: Malware Development](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_09_MALWARE.html) | Shellcode, XOR encoding, API hashing, anti-sandbox |
| 9 | [Module 13: EDR Evasion](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_13_EDR_EVASION.html) | Direct syscalls, HWBP bypass, AMSI/ETW bypass, unhooking |
| 10 | [Module 16: C2](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_16_C2.html) | Beacon vs interactive, jitter, encryption, Discord bridge |
| 11 | [Module 20: Kill Chain](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_20_KILL_CHAIN.html) | MITRE ATT&CK, TTP mapping, purple teaming |
| 12 | [Module 21: Capstone](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_21_CAPSTONE.html) | GeoDefend scenario — full operation from recon to exfil |
| BONUS | [Module 22: Web Application Hacking](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_22_WEB_HACKING.html) | Recon, auth, SQLi, IDOR, API signature breaking |
| BONUS | [Module 23: Infostealers](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_23_INFOSTEALERS.html) | Builder, victim, C2, detection rules, incident response |

### Track B: Operators Learning Code (12-Module Fast Path)

For people who know pentest tools and the kill chain but want to build their own tooling.

| Order | Module | What You Learn |
|-------|--------|----------------|
| 1 | [Module 00: Reader](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_00_READER.html) | Course guide, lab setup, study methodology |
| 2 | [Module 01: Networking](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_01_NETWORKING.html) | Protocols, ports, packet analysis, tunneling |
| 3 | [Module 02: Recon](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_02_RECON.html) | Active/passive reconnaissance, OSINT targeting |
| 4 | [Module 03: PowerShell](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_03_POWERSHELL.html) | Cmdlets, remoting, WMI, AMSI bypass basics, LOLBAS |
| 5 | [Module 04: Coding Basics](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_04_CODING_BASICS.html) | C, Python, Windows API, compilation, debugging |
| 6 | [Module 05: Shellcode](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_05_SHELLCODE.html) | Assembly, registers, PIC, PEB walking, encoding |
| 7 | [Module 07: Registry](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_07_REGISTRY.html) | Hives, persistence, forensics, offline analysis |
| 8 | [Module 11: Rootkits](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_11_ROOTKITS.html) | Persistence mechanisms, DLL sideloading, API hooking |
| 9 | [Module 12: Defensive Verify](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_12_DEFENSIVE_VERIFY.html) | Memory scanning, behavioral analysis, EDR testing |
| 10 | [Module 15: Lateral Movement](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_15_LATERAL.html) | Pass-the-Hash, Kerberoasting, WMI, PSExec, DCOM |
| 11 | [Module 17: Social Engineering](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_17_SOCIAL_ENGINEERING.html) | Phishing, pretexting, OSINT targeting, payload delivery |
| 12 | [Module 21: Capstone](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_21_CAPSTONE.html) | Full operation — recon, exploit, persist, exfil |

### 🎯 Mentor Priority: Social Engineering

Your mentor's words: **"Real attacks are carried remotely. Physical access is niche. The inbox is the new building perimeter."**

Social engineering is the highest-ROI skill for independent operators. It requires no zero-days, no expensive tools, and no physical access. It requires understanding human psychology, building credible pretext, and delivering payloads through trust.

**Start here for social engineering:**
- [Module 17: Social Engineering](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_17_SOCIAL_ENGINEERING.html) — The full course on phishing, pretexting, OSINT targeting, and payload delivery
- [Module 02: Recon](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_02_RECON.html) — OSINT for building target profiles
- [Module 16: C2](https://rainfantry.github.io/22nd-survey-division/modules/MODULE_16_C2.html) — Payload delivery and command infrastructure

---

## 22 MODULES — FULL CURRICULUM
|------|-------|-------------|
| 1-2 | Socket programming + reverse shells | Working C reverse shell (Windows + Linux) |
| 3-4 | OpenSSH persistence + VNC | .42 with SSH + VNC, documented |
| 5-6 | PowerShell remoting + AMSI bypass | Lateral movement lab, obfuscated scripts |
| 7-8 | AD advanced (BloodHound, DCSync, tickets) | AD lab attack path report |
| 9-10 | Linux privilege escalation | 10 THM boxes completed |
| 11-12 | Cloud persistence (AWS, Azure) | Cloud-based C2 proof of concept |
| 13-14 | EDR deep-dive | Research paper: "EDR evasion beyond HWBP" |
| 15-16 | iOS + Flutter | Jailbreak persistence, Flutter RE report |

**Mentor's rule:** "Organized notes > memorization. Cheat sheets > textbooks."

---

## MENTOR TEACHINGS — THE CORE LESSONS

These are the lessons from [HTB] that shape every module:

| Lesson | What It Means | Where to Learn |
|--------|-------------|--------------|
| **"Reverse shell is basic"** | The foundation everything builds on | Module 16 (C2), Practical Labs Exercise 7 |
| **"Organized notes > memorize"** | Build cheat sheets, not memory | Resources page, Module 02 (Recon) |
| **"Privilege escalation is easy"** | Misconfigurations, not 0days | Module 08 (Privesc), Practical Labs Sim 2 |
| **"Save every rung"** | Persistence at every level | Module 11 (Persistence), Practical Labs Widget 3 |
| **"Real attacks are remote"** | Physical access is niche; remote is money | Module 17 (Social Engineering) |
| **"Defender management"** | Full spectrum from silent to nuclear | Practical Labs Exercise 3-6 |
| **"System settings"** | Attack surface lives in configuration | Module 03 (PowerShell), Resources Quick Ref |
| **"Eventually all comes to networking"** | Every technique needs a channel | Module 01 (Networking) |
| **"Linux terminal is way easier"** | Learn both, use both | Module 03 (PowerShell) |

---

## COURSE MODULES — 22 MODULES, 5 PHASES

### Phase 1: Foundation (Weeks 1-4)
| Module | Title | Status |
|--------|-------|--------|
| 00 | Reader Guide — How to Use This Course | ✅ Live |
| 01 | Networking Fundamentals | ✅ Live |
| 02 | Recon & OSINT | ✅ Live |
| 03 | PowerShell Warfare | ✅ Live |
| 04 | Coding Basics | ✅ Live |

### Phase 2: Weaponization (Weeks 5-8)
| Module | Title | Status |
|--------|-------|--------|
| 05 | Shellcode Development | ✅ Live |
| 06 | Memory Forensics | ✅ Live |
| 07 | Registry Analysis | ✅ Live |
| 08 | Privilege Escalation | ✅ Live |

### Phase 3: Evasion (Weeks 9-12)
| Module | Title | Status |
|--------|-------|--------|
| 09 | Malware Development | ✅ Live |
| 10 | Code Injection | ✅ Live |
| 11 | Rootkits & Persistence | ✅ Live |
| 12 | Defensive Verification | ✅ Live |
| 13 | EDR Evasion | ✅ Live |

### Phase 4: Operations (Weeks 13-16)
| Module | Title | Status |
|--------|-------|--------|
| 14 | Cloud Files & Exfil | ✅ Live |
| 15 | Lateral Movement | ✅ Live |
| 16 | C2 Frameworks | ✅ Live |
| 17 | Social Engineering | ✅ Live |

### Phase 5: Advanced (Weeks 17-22)
| Module | Title | Status |
|--------|-------|--------|
| 18 | Android RAT | ✅ Live |
| 19 | Active Directory | ✅ Live |
| 20 | Full Kill Chain | ✅ Live |
| 21 | Capstone: GeoDefend | ✅ Live |

**Bonus:** CEO Translation (board-ready risk language)

---

## THE TOOLS (Tested on Live Hardware)

### VADER-ROOTKIT
Hardware breakpoint bypass for AMSI + ETW. Zero memory writes. 26 Defender-clean binaries. MSRC VULN-195458 research.

**Test:** Windows 11, Defender RTP + cloud + BehaviorMonitor — CLEAN. Kaspersky Premium — CLEAN.

### IRON-SUN
8-layer AV evasion stack. TCP reverse shell. XOR obfuscation, dynamic API resolution, anti-sandbox timing, PE header stomping.

**Test:** 10/10 POCs verified on live machine (192.168.1.92). Kaspersky Premium 21.25 — 0 detections.

### CHEYANNE C2
Full C2 framework. Browser-based operator panel. GPS exfil, VNC shell, AES-256-CBC beacon, Discord bridge, service persistence.

**Test:** 2 agents live. GPS polling 5s. SMS dump 47 messages. Play Protect bypassed.

### GHOST-ENCODER
Zero-width Unicode steganography. Covert channel framework. 16-character invisible alphabet.

**Test:** Payload hidden in Discord message. Entropy 0.12. Kaspersky CLEAN.

### WINRECON
Windows reconnaissance framework. Process enumeration, privilege escalation checks, network mapping.

**Test:** 1229 lines of output. Standard user context. 2 writable SYSTEM services found.

---

## LIVE LAB EVIDENCE

| Lab | IP | Status | Key Finding |
|-----|-----|--------|-------------|
| **WUPC** | 192.168.1.42 | ✅ SSH_OK | SeImpersonatePrivilege + writable service |
| **HOST** | 192.168.1.92 | ✅ SSH_OK | Kaspersky active, real-world target |
| **RADON** | 192.168.1.145 | ⏳ Timeout | C2 beacon SYN_SENT |

**Verified 2026-06-29:** WUPC .42 — SSH_OK, Admin context, SeImpersonatePrivilege ENABLED. HealthSecurityHost service with Authenticated Users:(M) permissions → SYSTEM in one restart.

---

## TESTING & DEPLOYMENT

### Automated Testing

Every push is validated by the test suite:

```bash
# Run all tests
bash scripts/test-all.sh

# Check site health
bash scripts/validate-site.sh

# Check all links
python3 scripts/check_links.py .

# Performance audit (ad-hoc — quota limited)
bash scripts/perf-check.sh

# Create release
bash scripts/release.sh v2026.06.29
```

**Test Results (Latest):**
- ✅ 5/5 main pages: 200 OK
- ✅ 29/29 module pages: 200 OK
- ✅ 756/756 internal links: valid
- ✅ 27 quiz options: interactive
- ✅ 28 module tree items: complete
- ✅ All modules have mentor callouts and copy buttons
- ✅ Bonus modules: Web Application Hacking, Infostealers
### Deployment

| Target | Details |
|--------|---------|
| **Production** | GitHub Pages (auto-deploy from `main`) |
| **URL** | `https://rainfantry.github.io/22nd-survey-division/` |
| **Staging** | `http://192.168.1.92:18080/` (local server) |
| **Type** | Static HTML — no DB, no env, no backend |

### Rollback

```bash
# If release breaks something:
git revert HEAD && git push origin main
# GitHub Pages redeploys in ~2 minutes
```

### Migration

To move to a new host:
1. Copy all files from repo
2. Update `CNAME` if using custom domain
3. Run `bash scripts/test-all.sh`
4. Done — no database migration needed

See [DEPLOYMENT.md](DEPLOYMENT.md) for full details.

---

## SITREPS — DEVELOPMENT LOG

| Date | Commit | What Changed |
|------|--------|--------------|
| 2026-06-29 | `ded05d0` | Automated testing suite, DEPLOYMENT.md, perf-check.sh |
| 2026-06-29 | `36135c2` | Test scripts, link checker, release pipeline |
| 2026-06-29 | `e199d7b` | Interactive quizzes, module-tree.html, copy buttons |
| 2026-06-29 | `7d3641e` | Copy buttons on practical-labs + resources |
| 2026-06-29 | `88201d0` | Mentor redaction (asi dev → mentor), HTML comments cleaned |
| 2026-06-29 | `4051288` | Resources: Quick reference cheat sheets, KILL_CHAIN_LAB_EVIDENCE |
| 2026-06-29 | `47ef0eb` | Practical Labs: SSH tests, defense bypasses, simulations, widgets |
| 2026-06-29 | `69483d5` | Crash course expanded with detailed mentor explanations |

---

## HONESTY POLICY

This course teaches **authorized security testing only**. Every tool is tested on own hardware or authorized lab environments. MSRC responsible disclosure filed for all Microsoft-related findings.

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
