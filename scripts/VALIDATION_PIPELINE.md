# 22ND SURVEY DIVISION — MODULE VALIDATION PIPELINE
# Operator: SERVITOR
# Purpose: Continuous research, lab testing, and evidence integration

## WORKFLOW OVERVIEW

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   RESEARCH  │───▶│  LAB TEST   │───▶│    WRITE    │───▶│   VALIDATE  │───▶│    PUSH     │
│  (Subagent) │    │  (Subagent) │    │  (Subagent) │    │  (Automated)│    │  (Automated)│
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## PHASE 1: RESEARCH

**Input:** Module HTML file, mentor documents, source repos
**Output:** `research_notes.md` with findings, citations, gaps

**Tasks:**
1. Read module content
2. Read relevant mentor docs (WHAT_I_HAVE.md, PRIVESC_LADDER.md, etc.)
3. Search source repos for real commands/code/findings
4. Check public references (Microsoft docs, MITRE, LOLBAS)
5. Identify outdated or incorrect information
6. List techniques needing lab verification

## PHASE 2: LAB TEST

**Targets:**
- `.42` — AMD sandbox, no Defender (malware/EDR testing)
- `.92` — Intel, Kaspersky active (real-world target)
- `.145` — RADON, authorized by Raed (limited access)

**Rules:**
- NEVER test on George's own machine (LAPTOP-R32M8MLI)
- Read-only recon first, then safe execution
- All tests logged with timestamp, target, command, output
- No destructive commands without explicit confirmation

**Output:** `lab_evidence.log` with commands and outputs

## PHASE 3: WRITE

**Input:** Research notes + Lab evidence + Current module HTML
**Output:** Updated module HTML with:
- Fixed incorrect facts
- Evidence boxes with real lab output
- Layman explanations
- Cross-links to related modules
- "Mentor Says" callouts
- Updated copy buttons and quizzes

## PHASE 4: VALIDATE

```bash
cd /c/Users/gwu07/Desktop/repos/22nd-survey-division
bash scripts/test-all.sh
```

Must pass all tests before pushing.

## PHASE 5: PUSH

```bash
git add -A
git commit -m "MODULE_XX: Validate with lab evidence [date]"
git push origin main
```

---

## MODULE PRIORITY QUEUE

| Priority | Module | Why | Research Sources | Lab Target |
|----------|--------|-----|------------------|------------|
| 1 | MODULE_17_SOCIAL_ENGINEERING | Mentor priority | lessons-from-teacher, public DNS | Public infra (safe) |
| 2 | MODULE_10_CODE_INJECTION | Foundational | vader-rootkit source, MSDN | .42 (safe exec) |
| 3 | MODULE_13_EDR_EVASION | High value | vader-rootkit, MSRC docs | .42 (no Defender) |
| 4 | MODULE_09_MALWARE | High value | vader-rootkit, cheyanne | .42 (no Defender) |
| 5 | MODULE_16_C2 | High value | cheyanne, starkiller | .42 (safe exec) |
| 6 | MODULE_08_PRIVESC | Foundational | lessons-from-teacher, WHAT_I_HAVE | .42 (safe exec) |
| 7 | MODULE_15_LATERAL | Advanced | lessons-from-teacher, PRIVESC_LADDER | .42 (safe exec) |
| 8 | MODULE_19_AD | Advanced | WHAT_I_HAVE, public docs | .42 (AD lab if available) |
| 9 | MODULE_20_KILL_CHAIN | Capstone glue | MITRE ATT&CK, mentor docs | N/A (theoretical) |
| 10 | MODULE_02_RECON | Foundation | lessons-from-teacher, winrecon | Public infra (safe) |
| 11 | MODULE_01_NETWORKING | Foundation | lessons-from-teacher | Public infra (safe) |
| 12 | MODULE_03_POWERSHELL | Foundation | lessons-from-teacher, MSDN | .92 (read-only) |
| 13 | MODULE_04_CODING_BASICS | Foundation | N/A (theoretical) | N/A (theoretical) |
| 14 | MODULE_05_SHELLCODE | Foundation | vader-rootkit, MSDN | .42 (safe exec) |
| 15 | MODULE_06_MEMORY | Foundation | vader-rootkit, MSDN | .42 (safe exec) |
| 16 | MODULE_07_REGISTRY | Foundation | lessons-from-teacher, MSDN | .42 (safe exec) |
| 17 | MODULE_11_ROOTKITS | Advanced | vader-rootkit, cheyanne | .42 (safe exec) |
| 18 | MODULE_12_DEFENSIVE_VERIFY | Advanced | vader-rootkit, MSRC | .42 (safe exec) |
| 19 | MODULE_14_CLOUD_FILES | Operations | Public docs, AWS/Azure | Public infra (safe) |
| 20 | MODULE_18_ANDROID | Advanced | starkiller, public docs | .42 (if Android VM) |
| 21 | MODULE_21_CAPSTONE | Capstone | All modules | N/A (scenario) |
| 22 | MODULE_00_READER | Meta | N/A | N/A |

---

## EVIDENCE BOX FORMAT

```html
<div class="evidence-box">
  <div class="evidence-header">// LIVE EVIDENCE — HOST [target]</div>
  <div class="evidence-meta">YYYY-MM-DD HH:MM UTC | [target desc] | [operator]</div>
  <p style="font-size: 0.85rem; color: var(--dim); margin-bottom: 1rem;">
    [Context: what was tested and why]
  </p>
  <div class="code-block">
    <button class="copy-btn" onclick="copyCode(this)">COPY</button>
[COMMAND]
[OUTPUT]
  </div>
  <p style="margin-top: 1rem;">
    <strong>What this proves:</strong> [Interpretation]
  </p>
  <p style="margin-top: 0.5rem;">
    <strong>Mentor says:</strong> "[Relevant quote]"
  </p>
</div>
```

---

## LOGGING FORMAT

```
[YYYY-MM-DD HH:MM UTC] TARGET: <ip/hostname> OPERATOR: SERVITOR
MODULE: <module_name>
PHASE: <research/lab/write/validate>
COMMAND: <exact command>
OUTPUT:
<output>
ASSESSMENT: <works/fails/partial/theory>
MENTOR_LINK: <which teaching this validates>
NEXT_ACTION: <what to do next>
```

---

## SUCCESS CRITERIA

- [ ] All commands in module tested or marked THEORY
- [ ] All lab evidence logged with target and timestamp
- [ ] All outdated information corrected
- [ ] All cross-links valid
- [ ] test-all.sh passes
- [ ] Module hooks back to at least one mentor teaching
- [ ] Evidence box added for every practical technique
- [ ] "Mentor Says" callout in every major section

---

## AUTOMATION

Run validation pipeline weekly:
```bash
# cronjob: every Sunday at 02:00 UTC
0 2 * * 0 cd /c/Users/gwu07/Desktop/repos/22nd-survey-division && bash scripts/validate-modules.sh
```

Or trigger manually:
```bash
bash scripts/validate-modules.sh MODULE_10_CODE_INJECTION
```

---

*VIDIMUS OMNIA — We see everything.*
