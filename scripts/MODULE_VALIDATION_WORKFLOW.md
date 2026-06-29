# Module Validation Workflow — 22nd Survey Division

## Purpose
Every module must be:
1. **Researched** against current sources (mentor docs, repos, recent techniques)
2. **Fact-checked** for accuracy of commands, APIs, offsets, and detection methods
3. **Lab-tested** against authorized lab machines (.42, .92, .145)
4. **Updated** with evidence widgets and layman explanations
5. **Validated** with `bash scripts/test-all.sh`

---

## Phase 1: Research (Subagent: `researcher`)

**Inputs:**
- Module HTML file
- Mentor documents in `lessons-from-teacher/`
- Source code repos: `vader-rootkit/`, `iron-sun/`, `cheyanne/`, `starkiller/`, etc.
- Public references: Microsoft docs, MITRE ATT&CK, LOLBAS, etc.

**Tasks:**
1. Read the current module content
2. Read relevant mentor documents
3. Search source code repos for real commands, code, and findings
4. Identify outdated or incorrect information
5. List techniques that need lab verification
6. Output: `research_notes.md` with findings and citations

---

## Phase 2: Lab Testing (Subagent: `tester`)

**Targets:**
- `.42` — AMD sandbox, no Defender, safe for malware/EDR testing
- `.92` — Intel machine, Kaspersky active, real-world target
- `.145` — RADON laptop, authorized by Raed, limited access

**Rules:**
- NEVER test on George's own machine (LAPTOP-R32M8MLI)
- All tests logged with timestamp, target, command, output
- No destructive commands without explicit confirmation
- Use read-only recon first, then safe execution

**Tasks:**
1. Run commands from the module on the appropriate target
2. Capture real output (sanitized if needed)
3. Verify techniques work as described
4. Note failures, errors, and detection events
5. Output: `lab_evidence.log` with commands and outputs

---

## Phase 3: Update Module (Subagent: `writer`)

**Inputs:**
- Research notes
- Lab evidence log
- Current module HTML

**Tasks:**
1. Fix incorrect facts
2. Add evidence widgets with real lab output
3. Add layman explanations for complex concepts
4. Add cross-links to related modules
5. Add "Mentor Says" callouts linking techniques to his teachings
6. Ensure copy buttons and quizzes still work
7. Output: Updated module HTML

---

## Phase 4: Validate (Automated)

```bash
cd /c/Users/gwu07/Desktop/repos/22nd-survey-division
bash scripts/test-all.sh
```

Must pass all tests before pushing.

---

## Evidence Widget Format

```html
<div class="evidence-box">
  <div class="evidence-header">// LIVE EVIDENCE — HOST .42</div>
  <div class="evidence-meta">2026-06-29 14:32 UTC | AMD sandbox | No Defender</div>
  <pre class="code-block">
C:\Users\lab> whoami
lab-pc\lab

C:\Users\lab> tasklist | findstr explorer
explorer.exe                  4520 Console                    1    125,432 K
  </pre>
  <p><strong>What this proves:</strong> Command execution works under standard user context.</p>
  <p><strong>Mentor says:</strong> "Real attacks are carried remotely — but you test locally first."</p>
</div>
```

---

## Module Priority Order

1. MODULE_17_SOCIAL_ENGINEERING (mentor priority)
2. MODULE_10_CODE_INJECTION (foundational)
3. MODULE_13_EDR_EVASION (high value)
4. MODULE_09_MALWARE (high value)
5. MODULE_16_C2 (high value)
6. MODULE_08_PRIVESC (foundational)
7. MODULE_15_LATERAL (advanced)
8. MODULE_19_AD (advanced)
9. MODULE_20_KILL_CHAIN (capstone glue)
10. Remaining modules

---

## Logging Format

```
[YYYY-MM-DD HH:MM UTC] TARGET: <ip/hostname> OPERATOR: SERVITOR
COMMAND: <exact command>
OUTPUT:
<output>
ASSESSMENT: <works/fails/partial>
MENTOR_LINK: <which teaching this validates>
```

---

## Success Criteria

- [ ] All commands in module tested or marked THEORY
- [ ] All lab evidence logged with target and timestamp
- [ ] All outdated information corrected
- [ ] All cross-links valid
- [ ] test-all.sh passes
- [ ] Module hooks back to at least one mentor teaching
