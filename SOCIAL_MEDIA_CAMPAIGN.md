# 22DIV — Social Media Campaign Ops
**OCCUPATION FORCE CALLSIGN GSW PTY. LTD. — George Wu**
Campaign: Course launch + proof of work

---

## POSTING SCHEDULE

| Day | Platform | Post | Hook |
|---|---|---|---|
| Day 1 (Tue 8am) | LinkedIn | POST-LI-01 | Launch announcement |
| Day 2 (Wed 12pm) | Instagram | POST-IG-01 | IRON-DOME screenshot |
| Day 3 (Thu 8am) | LinkedIn | POST-LI-02 | MSRC submission story |
| Day 4 (Fri 12pm) | Instagram | POST-IG-02 | StarKiller C2 |
| Day 7 (Mon 8am) | LinkedIn | POST-LI-03 | AV evasion doctrine |
| Day 8 (Tue 8pm) | Instagram | POST-IG-03 | ECLIPSE GPS |
| Day 10 (Thu 8am) | LinkedIn | POST-LI-04 | Windows Internals |
| Day 14 (Mon 8am) | LinkedIn | POST-LI-05 | Kill chain philosophy |
| Day 17 (Thu 12pm) | Instagram | POST-IG-04 | Kill chain 10/10 |
| Day 21 (Mon 8am) | LinkedIn | POST-LI-06 | Course offer post |

---

## LINKEDIN POSTS

### POST-LI-01 — LAUNCH
```
I built a complete offensive security course from scratch.

22 modules. Full kill chain. Everything I learned going from zero to:

→ Submitting a vulnerability to Microsoft (VULN-195458)
→ Building a rootkit that passed Windows Defender, Kaspersky Premium, and MalwareBytes simultaneously
→ Writing a C2 framework with GPS geolocation, VNC streaming, and Discord bridge
→ Building an Android RAT with GPS exfil, SMS intercept, and camera access

This isn't a certification prep course. There are no flashcards. No theory without implementation.

Every module ends with working code you built yourself.

The course is live: rainfantry.github.io/22nd-survey-division/
Access PIN available on the site.

22nd Survey Division — built in Sydney. No US company. No fluff.

#offensivesecurity #redteam #cybersecurity #malwaredevelopment #Sydney
```

### POST-LI-02 — MSRC STORY
```
I found a Tamper Protection bypass in Windows Defender.

Submitted it to Microsoft Security Response Center as VULN-195458.

The technique: Hardware Breakpoint (HWBP) injection into the Defender process. Set a breakpoint on the AMSI scan function. When the breakpoint fires, redirect execution to a NOP sled. AMSI returns "clean" on everything.

Microsoft acknowledged the submission. The embargo lapsed. I published the research.

The rootkit is called vader-rootkit. 26 clean binaries. Ring 0. Documented in Module 11 of the course.

This is what the course teaches — not how to use someone else's tools. How to build them, how to document the research, and how to submit it responsibly.

Link in bio.

#vulnerabilityresearch #windowssecurity #rootkit #AMSI #redteam #malwaredevelopment
```

### POST-LI-03 — AV EVASION DOCTRINE
```
Most AV evasion content online teaches you to run someone else's tool.

That's not evasion. That's using a signature that's already in a threat database.

Real evasion means understanding exactly what the scanner is looking for — and specifically engineering around it.

IRON-DOME v4.0.0 is what Module 12 builds:

Layer 1: XOR encoding with per-binary key
Layer 2: Dynamic API resolution (no import table)
Layer 3: Anti-sandbox (timing, CPU count, GPU check)
Layer 4: PE header stomping
Layer 5: ISUN gate (invalid instruction trap)
Layer 6: Jitter (randomised execution timing)
Layer 7: MinGW cross-compilation (removes MSVC patterns)
Layer 8: AMSI + ETW bypass (Module 11 vader-rootkit)

Result: 0 detections. Kaspersky Premium running active on the same machine.

The course: rainfantry.github.io/22nd-survey-division/

#AVevasion #redteam #malwaredevelopment #offensivesecurity #cybersecurity
```

### POST-LI-04 — WINDOWS INTERNALS
```
You can't evade what you don't understand.

Module 6 — Windows Internals — is the foundation everything else in the course sits on.

Before you bypass AMSI, you need to understand what AMSI is at the API level.
Before you hollow a process, you need to understand what a process IS in the kernel.
Before you write a rootkit, you need to understand the handle table, the PEB, and where the seams are.

Most offensive security courses skip this. They give you a Metasploit command and call it a technique.

We go to the source. PEB/TEB, VAD trees, kernel object lifecycle, handle inheritance, the difference between a process and a job. All of it. Because when you understand the internals, the bypasses write themselves.

22nd Survey Division — 22 modules, full kill chain, built in Sydney.
rainfantry.github.io/22nd-survey-division/

#windowsinternals #offensivesecurity #redteam #malwaredevelopment #kernelexploitation
```

### POST-LI-05 — PHILOSOPHY
```
The kill chain is a mindset, not a checklist.

Recon → Weaponise → Deliver → Exploit → Install → C2 → Exfil

Most people learn one of these phases in isolation. They become recon specialists, or they learn a payload builder, and they think that's the whole picture.

The 22nd Survey Division course is built around the full chain. Every module connects to the one before and after it.

You don't just learn to bypass AMSI. You learn WHY AMSI exists (Module 4 — Mitigations), HOW to bypass it (Module 11 — Rootkits), and how that bypass feeds into your payload delivery (Module 12 — AV Evasion) which feeds into your C2 callback (Module 16 — C2).

That's how attackers think. One continuous operation, not a collection of disconnected techniques.

22nd Survey Division — Sydney, Australia.
Link in bio.

#offensivesecurity #killchain #redteam #cybersecurity #MITRE
```

### POST-LI-06 — OFFER
```
22nd Survey Division — offensive security course — is open.

$497 AUD. One time. No subscription.

What you get:
→ 22 modules, full kill chain (MITRE ATT&CK aligned)
→ 8 private tool repos — C2 framework, rootkit, Android RAT, payload pipeline
→ Real proof: MSRC submission, Kaspersky bypass, 2 Android agents live, GPS tracking

What this is NOT:
→ Not CEH, OSCP, or any certification course
→ Not theory-only. Every module = working code
→ Not recorded lectures. Field manual format — read, build, prove.

This is what I built working as a survey technician in Sydney while teaching myself offensive security from scratch. Every technique documented, every tool functional, every result real.

rainfantry.github.io/22nd-survey-division/

#offensivesecurity #cybersecurity #redteam #malwaredevelopment #Sydney #Australia
```

---

## INSTAGRAM POSTS

### POST-IG-01 — IRON-DOME SCREENSHOT
**Image:** iron_dome_build_complete_154613.jpg
```
IRON-DOME v4.0.0
8 layers. 0 detections.
Kaspersky Premium running on the same machine.

XOR + dynamic API + anti-sandbox + PE header stomp + ISUN gate + jitter + MinGW + AMSI bypass.

Built from scratch. Module 12.

22nd Survey Division → link in bio

#offensivesecurity #redteam #malwaredevelopment #AVevasion #cybersecurity #hacking #infosec
```

### POST-IG-02 — STARKILLER
**Image:** starkiller_agents_live.png
```
2 Android agents. Live.

GPS location. SMS intercept. Camera access. Contacts. File system. Play Protect bypassed.

This is StarKiller — Android RAT built in Module 21.

ADB logcat running. Device comms flowing. Real hardware.

22nd Survey Division → link in bio

#android #RAT #mobileattack #offensivesecurity #redteam #malwaredevelopment #cybersecurity
```

### POST-IG-03 — ECLIPSE GPS
**Image:** eclipse_c2_gps_live.png
```
ECLIPSE C2.
GPS tracking. Reverse shell. Browser-based operator interface.

Sydney, NSW. Target acquired.

Module 9 → Module 16 → connected.

22nd Survey Division → link in bio

#C2 #commandandcontrol #offensivesecurity #redteam #cybersecurity #GPS #malwaredevelopment
```

### POST-IG-04 — KILL CHAIN
**Image:** iron_dome_v4_killchain.png
```
Kill chain: 10/10.

Recon → Weaponise → Deliver → Exploit → Install → C2 → Exfil

Every phase. Every module. Built, not borrowed.

22nd Survey Division → link in bio

#killchain #MITRE #offensivesecurity #redteam #cybersecurity #penetrationtesting
```

### POST-IG-05 — ROOTKIT / MSRC
**Image:** MSRC_VULN195458_Submission.png
```
VULN-195458.

Tamper Protection bypass submitted to Microsoft Security Response Center.

Hardware breakpoint injection. AMSI patched. Defender blind.

This is what Module 11 builds.

22nd Survey Division → link in bio

#MSRC #vulnerabilityresearch #rootkit #windowssecurity #AMSI #offensivesecurity
```

### POST-IG-06 — VERDICT
**Image:** Defender_Quarantine_GaySun.png + Defender_Quarantine_RoguePlanet.png
```
Before evasion. After evasion.

Same payload. Different engineering.

Module 12 shows you exactly what changed and why.

22nd Survey Division → link in bio

#AVevasion #malwaredevelopment #offensivesecurity #redteam #cybersecurity #WindowsDefender
```

---

## HASHTAG SETS

### LinkedIn (primary)
```
#offensivesecurity #redteam #malwaredevelopment #cybersecurity #windowsinternals #AVevasion #MITRE #penetrationtesting #infosec #Sydney
```

### Instagram (volume)
```
#offensivesecurity #redteam #cybersecurity #hacking #ethicalhacking #malwaredevelopment #infosec #pentesting #kalilinux #cybersec #hackers #informationsecurity #networksecurity #darkweb #cybercrime #security #hack #python #c2 #rat #rootkit #AMSI #windowssecurity #malware #reverseengineering
```

### Twitter/X (punchy)
```
#offensivesecurity #redteam #malwaredevelopment #rootkit #AMSI #cybersecurity
```

---

## VIRAL MECHANICS

### What works on LinkedIn for security content:
1. **Story arc** — "from zero to MSRC submission" — personal journey performs 3-5x better than pure technical
2. **Specific numbers** — "8 layers", "26 clean binaries", "0 detections" — beat vague claims
3. **Controversy lite** — "This isn't OSCP" positions against established brands
4. **First comment** — post a link to the site in the first comment, not in the body (LinkedIn penalizes external links in post body)

### What works on Instagram for security content:
1. **Terminal screenshots** — dark background, green text, real output — high engagement
2. **Before/after** — GaySun caught vs IRON-DOME 0 detections
3. **Live proof** — StarKiller with 2 agents, GPS map on screen
4. **Captions under 150 chars** for the preview — long captions work but hook must fit in preview

### Viral prep — what to have ready before posting:
- [ ] Profile link → site URL
- [ ] Bio: "Security researcher. Built: rootkit, C2, Android RAT. 22DIV course link ↓"
- [ ] Story highlights: Proof / Tools / Course
- [ ] 3-5 posts queued so profile looks active when people check

---

## GOOGLE + META ADS COPY (when budget allows)

### Google Search Ad
**Headline 1:** Offensive Security Course — Sydney
**Headline 2:** Full Kill Chain. 22 Modules. $497 AUD
**Headline 3:** MSRC Research. Real Tools. Real Proof.
**Description:** Built by a security researcher who submitted to MSRC. C2, rootkit, Android RAT. Not a cert prep course. Learn to build, not just use.
**URL:** rainfantry.github.io/22nd-survey-division/

### LinkedIn Sponsored Post
Use POST-LI-06 body. CTA button: "Learn More". Budget: $20-50/day. Target: Security Engineers, Penetration Testers, Software Developers in AU/NZ/US.

### Instagram/Facebook Ad
**Image:** iron_dome_kill_chain_154619.jpg (Kaspersky active, IRON-DOME running)
**Caption:** "0 detections. Kaspersky Premium active. Module 12."
**CTA:** Learn More → site URL
**Audience:** Interests: Cybersecurity, Ethical Hacking, Kali Linux. Age 22-45.
