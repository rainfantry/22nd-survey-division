# LINKEDIN AD COPY — 22ND SURVEY DIVISION
## 5 posts. Drop your screenshot where marked. Post 1 per day.

---

## POST 1 — IRON-DOME (AV Evasion)

📸 [DROP SCREENSHOT: iron_dome_build_complete or vader_widget screenshot showing 0 detections]

---

**Caption:**

I built a payload that bypassed Kaspersky Premium, Windows Defender, and MalwareBytes at the same time. On the same machine.

0 detections. 8 layers deep.

Here's what the stack looks like:

🔴 Layer 1 — XOR encoder (breaks static signatures)
🔴 Layer 2 — Dynamic API resolution (no import table entries)
🔴 Layer 3 — Anti-sandbox checks (timing, CPU count, GPU presence)
🔴 Layer 4 — PE header stomp (kills forensic recovery)
🔴 Layer 5 — ISUN gate (emulator divergence trap)
🔴 Layer 6 — Execution jitter (defeats ML timing profiles)
🔴 Layer 7 — AMSI bypass via hardware breakpoint
🔴 Layer 8 — ETW silenced (no event logs)

This is what Module 12 of the 22nd Survey Division course teaches you to build from source.

Not theory. Working code. Compile it yourself.

22 modules. Full kill chain. $497 AUD.
🔗 rainfantry.github.io/22nd-survey-division

#CyberSecurity #MalwareDevelopment #RedTeam #OffensiveSecurity #WindowsSecurity #PenetrationTesting

---

## POST 2 — VADER ROOTKIT (HWBP / MSRC)

📸 [DROP SCREENSHOT: vader_widget.html showing debug registers DR0-DR7 + AMSI bypass log]

---

**Caption:**

I submitted a Windows security finding to Microsoft.

Reference number: VULN-195458.

The technique: Hardware Breakpoint AMSI bypass.

No memory patching. No code injection. No signatures to detect.

You set DR0 = AmsiScanBuffer address. You enable it in DR7. You install a Vectored Exception Handler. When PowerShell calls AMSI to scan your script, the CPU hits the hardware breakpoint, your VEH fires, you overwrite RCX with AMSI_RESULT_CLEAN, and return.

Windows Defender doesn't see it. Kaspersky doesn't see it. MalwareBytes doesn't see it.

Tamper Protection monitors memory integrity. It doesn't watch debug registers.

Microsoft rejected it as "expected behavior." I published it anyway.

Module 11 of the 22nd Survey Division course walks every line of this code.

22 modules. Full kill chain. $497 AUD.
🔗 rainfantry.github.io/22nd-survey-division

#CyberSecurity #WindowsInternals #RootKit #AMSI #RedTeam #SecurityResearch #MSRC

---

## POST 3 — STARKILLER (Android RAT)

📸 [DROP SCREENSHOT: starkiller_agents_live.png OR starkiller_widget showing 2 agents + GPS coords]

---

**Caption:**

Two Android phones. Both compromised. GPS coordinates live.

This is StarKiller — an Android RAT I built from scratch in Module 21.

What it does:
📍 GPS location polling via Windows Location API → exfiltrated every 5 seconds
💬 SMS interception — full message thread dump
📷 Camera access — rear and front
📁 File system browsing
📞 Contacts dump
🖥️ Reverse shell

Play Protect triggered on install. We killed the Play Protect process and reinstated persistence.

Both agents are live. Both are phones I own, on a network I control.

This is what offensive Android security looks like when you understand the internals.

Module 21. 22nd Survey Division.

22 modules. Full kill chain. $497 AUD.
🔗 rainfantry.github.io/22nd-survey-division

#AndroidSecurity #MobileSecurity #PenetrationTesting #RedTeam #CyberSecurity #OffensiveSecurity

---

## POST 4 — ECLIPSE C2 (GPS Tracker)

📸 [DROP SCREENSHOT: eclipse_c2_gps_live.png OR eclipse_widget showing GPS trail + shell]

---

**Caption:**

GPS coordinates. Live. Updating every 5 seconds.

This is ECLIPSE — a C2 framework with real-time geographic targeting.

The agent is running as SYSTEM inside svchost.exe. It has:

📡 GPS polling → Sydney coords exfiltrated to operator
🔐 AES-256-CBC encrypted beacon channel
🔄 Service persistence — survives reboot
💻 Full reverse shell with PowerShell execution
🛡️ SeDebugPrivilege confirmed — process injection ready
🚫 Windows Defender: disabled

The operator panel shows a live GPS trail. Every movement logged.

This is Module 16 of the 22nd Survey Division course.

You build the beacon in C. You build the Python operator listener. You build the Discord bridge. Then you put them together.

22 modules. Full kill chain. $497 AUD.
🔗 rainfantry.github.io/22nd-survey-division

#C2Framework #RedTeam #CyberSecurity #OffensiveSecurity #PenetrationTesting #WindowsSecurity

---

## POST 5 — KILL CHAIN (Full Course Pitch)

📸 [DROP SCREENSHOT: killchain_widget.html OR showcase page showing all 5 widgets]

---

**Caption:**

7 phases. Full kill chain. Everything working.

🔵 Phase 01 — Recon: winrecon.py pulls WMI data, AD enumeration, CWE scan
🟣 Phase 02 — Weaponise: ghost-encoder + XOR + IRON-DOME 8-layer stack → 0/72 VT detections
🔴 Phase 03 — Deliver: LNK spoof + APK sideload (StarKiller)
🟠 Phase 04 — Exploit: vader-rootkit HWBP → AMSI blind → ETW silent (MSRC VULN-195458)
🟡 Phase 05 — Install: SCM service, HKLM autorun, reflective DLL inject → survives reboot
🟡 Phase 06 — C2: CHEYANNE + ECLIPSE GPS + Discord bridge + VNC callback
🟢 Phase 07 — Exfil: ghost-encoder zero-width Unicode steg + AES-256 + covert DNS

Every tool in this chain was built from source.
Every module teaches you how.
Every lesson ends with working code.

This is the 22nd Survey Division course.

Not CEH. Not OSCP prep. Not a certification.

22 modules. $497 AUD.
🔗 rainfantry.github.io/22nd-survey-division

#CyberSecurity #RedTeam #KillChain #MITREAttack #OffensiveSecurity #MalwareDevelopment #PenetrationTesting #SecurityResearch
