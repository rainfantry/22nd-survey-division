# Release v1.1.0 — 22nd Survey Division

## Deployment
- **Target:** GitHub Pages (auto-deploy from main branch)
- **URL:** https://rainfantry.github.io/22nd-survey-division/
- **Staging:** http://192.168.1.92:18080/ (local python http.server)
- **Type:** Static HTML — no database, no env vars, no backend

## Rollback Plan
If this release breaks something:
[main 0e82a44] Revert "Fix validate-modules.sh: fix mentor_count display glitch (double 0 output from subshell fallback)."
 Date: Tue Jun 30 01:14:47 2026 +1000
 1 file changed, 1 insertion(+), 2 deletions(-)
HEAD is now at 0e82a44 Revert "Fix validate-modules.sh: fix mentor_count display glitch (double 0 output from subshell fallback)."
GitHub Pages deploys within ~2 minutes of push.

## Test Results
2026-06-29 15:14 UTC
- All modules: 27 HTML files
- Navigation: Complete (all modules linked)
- Interactive quizzes: 27 options
- Copy buttons: Enabled on practical-labs + resources

## What's Included
- Complete 22-module course (Modules 00-21 + Capstone)
- Crash course with mentor teachings
- Practical labs with step-by-step exercises
- Interactive quizzes with right/wrong feedback
- Module tree (complete archive)
- Resources page with command cheat sheets
- Live lab evidence from WUPC .42 and HOST .92

## Migration Notes
To migrate to a new domain:
1. Copy all files from this repo to the new hosting
2. Update CNAME if using GitHub Pages custom domain
3. No database required — all static HTML
4. No env vars — everything is self-contained
5. Test with: bash scripts/test-all.sh

