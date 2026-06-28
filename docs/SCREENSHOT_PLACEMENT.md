# Screenshot Placement Guide — 22nd Survey Division Course
## Where to Place GitHub Repository Images in Course Content

### Philosophy
Every screenshot must serve the student's understanding. Not decoration. Not proof-of-work for the instructor. The student sees the screenshot and thinks: "I can do that. That output looks like what I should see."

### Screenshot Categories

#### 1. BUILD OUTPUT SCREENS (Critical)
**When to use:** After every compilation, build, or tool execution
**Where to place:** Immediately after the command block, before the explanation
**What it shows:** Terminal output with success indicators, file sizes, timestamps
**Example:**
```
[Command block: gcc -o phantom_rpc.exe phantom_rpc.c]
[BUILD OUTPUT SCREENSHOT]
[Explanation: "You should see 0 errors, 0 warnings. The file size is 153KB..."]
```
**Repos:** vader-rootkit, iron-sun, phantom_rpc, cheyanne-phantom

#### 2. VERIFICATION SCREENS (Critical)
**When to use:** After every test, scan, or validation step
**Where to place:** After the build output, before the "Why it works" section
**What it shows:** KAV scan results, Defender status, process listing, registry query
**Example:**
```
[Command block: avp.exe SCAN phantom_rpc.exe]
[VERIFICATION SCREENSHOT: "Total detected: 0"]
[Why it works: "KAV uses signature matching. Our tool has no signatures..."]
```
**Repos:** All tool repos, winrecon, defender-quarantine

#### 3. BEFORE/AFTER COMPARISON SCREENS (High Value)
**When to use:** When demonstrating evasion, bypass, or state change
**Where to place:** Side-by-side or stacked, with clear labels
**What it shows:** Left = before bypass (Defender active, AMSI blocking), Right = after bypass (Defender quiet, AMSI disabled)
**Example:**
```
[BEFORE SCREENSHOT: Windows Security showing "Threats found"]
[AFTER SCREENSHOT: Windows Security showing "No actions needed"]
[Explanation: "The HWBP bypass intercepts AMSI before it can flag our payload..."]
```
**Repos:** vader-rootkit, defender-quarantine, 22sd-research-findings

#### 4. ERROR SCREENS (Teaching Moments)
**When to use:** When something fails and the student needs to understand why
**Where to place:** In the "Common Errors" or "Troubleshooting" section
**What it shows:** The actual error message, not a mockup
**Example:**
```
[ERROR SCREENSHOT: "0x80070057 — ERROR_INVALID_PARAMETER"]
[Explanation: "This means your struct size is wrong. The API expects 32 bytes, you passed 16..."]
```
**Repos:** All repos, especially cloud-files, cve-submissions

#### 5. LIVE EVIDENCE SCREENS (Trust Building)
**When to use:** In the "Evidence" or "Verification Status" table
**Where to place:** Embedded in the table cell or immediately below
**What it shows:** Real machine output with timestamps, hostnames, IP addresses
**Example:**
```
[EVIDENCE TABLE]
| Test | Result | Screenshot |
| KAV Scan | 0 detections | [SCREENSHOT] |
| Process List | SYSTEM achieved | [SCREENSHOT] |
```
**Repos:** All modules, especially Module 12 (Defensive Verify), Module 20 (Kill Chain)

### Screenshot Technical Specs
- **Format:** PNG (lossless, no compression artifacts)
- **Resolution:** 1920x1080 minimum (scales down, not up)
- **Annotation:** Red boxes around critical output lines, not full-screen highlights
- **Timestamp:** Visible in screenshot (proves live execution)
- **Hostname:** Visible (proves which machine: .92, .42, .145)
- **No cropping:** Show full terminal window, not just the output line

### Automation: Where Our Tools Generate Screenshots

| Tool | Screenshot Trigger | Output Location | Course Placement |
|------|-------------------|-----------------|------------------|
| winrecon | After every scan | `recon/RECON_<hostname>_<timestamp>.log` | Module 01, 03, 06, 07 |
| vader-rootkit | After build + scan | `build/` directory | Module 11, 12, 13 |
| iron-sun | After C2 connection | `logs/` directory | Module 16, 20 |
| phantom_rpc | After privesc test | `test/` directory | Module 08, 15, 20 |
| cheyanne-phantom | After full kill chain | `reports/` directory | Module 20, 21 |
| cfapi_brute_force | After each test | `logs/` directory | Module 14 |

### Automated Pipeline
```
1. Tool execution → generates output
2. Screenshot capture (automated via phantom_rpc --screenshot)
3. Upload to GitHub repo (showcase/ directory)
4. Embed in course module (Markdown: ![desc](showcase/image.png))
5. Verify image loads in browser (automated check)
```

### Manual Placement Checklist
- [ ] Screenshot appears within 2 scrolls of the command block
- [ ] Screenshot has alt text describing what the student should see
- [ ] Screenshot is referenced in the text ("As shown in the screenshot above...")
- [ ] Screenshot matches the command output (not a different run)
- [ ] Screenshot timestamp is recent (not older than 30 days for live modules)
- [ ] Screenshot hostname matches the module's target machine

### Example: Module 09 — Malware Development
```
[Section: Live Compile]
[Command: gcc -o phantom_rpc.exe phantom_rpc.c -lws2_32]
[BUILD SCREENSHOT: 0 errors, 153KB output]
[Explanation: "153KB is the expected size. If you get 2KB, you forgot -lws2_32."]

[Section: KAV Verification]
[Command: avp.exe SCAN phantom_rpc.exe /i0]
[VERIFICATION SCREENSHOT: Total detected: 0, Total OK: 2]
[Explanation: "iChecker and iSwift are enabled. The file was fully scanned, not cached."]

[Section: Behavioral Test]
[Command: phantom_rpc.exe --spooler]
[EVIDENCE SCREENSHOT: whoami output showing NT AUTHORITY\SYSTEM]
[Explanation: "The spooler exploit worked. You now have SYSTEM privileges."]
```

### Example: Module 20 — Full Kill Chain
```
[Section: Step 3 — Execution]
[Command: phantom_rpc.exe --spooler]
[BEFORE/AFTER: Left = standard user prompt, Right = SYSTEM prompt]
[Explanation: "Notice the prompt change. Before: C:\Users\swu. After: C:\Windows\System32."]

[Section: Verification Status]
[Table with 10 rows, each row has a screenshot column]
[Row 1: Recon screenshot showing nmap output]
[Row 2: Initial access screenshot showing SSH login]
[...]
[Row 10: Exfiltration screenshot showing C2 server receipt]
```
