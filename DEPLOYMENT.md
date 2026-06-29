# DEPLOYMENT.md — 22nd Survey Division

## Deployment Target

**Primary:** GitHub Pages (auto-deploy from `main` branch)
- URL: `https://rainfantry.github.io/22nd-survey-division/`
- No build step required — static HTML
- Deploys within ~2 minutes of push

**Staging:** Local python http.server
- URL: `http://192.168.1.92:18080/`
- Command: `python3 -m http.server 18080 --bind 192.168.1.92`
- Test locally before pushing

**Custom Domain:** Update `CNAME` file in repo root

## Environment

- **No database** — all static HTML/CSS/JS
- **No env vars** — everything self-contained
- **No backend** — client-side only
- **No secrets** — nothing to leak

## Release Workflow

```bash
# 1. Test locally
bash scripts/test-all.sh

# 2. Stage locally (optional)
cd /c/Users/gwu07 && python3 -m http.server 18080 --bind 192.168.1.92
# Browse to http://192.168.1.92:18080/22nd-survey-division/

# 3. Create release
bash scripts/release.sh v2026.06.29

# 4. GitHub Pages auto-deploys from main
# Wait ~2 minutes, verify at https://rainfantry.github.io/22nd-survey-division/
```

## Rollback Plan

If a release breaks something:

```bash
# Option 1: Revert the release commit
git revert HEAD
git push origin main

# Option 2: Reset to previous tag
git reset --hard <PREVIOUS_TAG>
git push --force origin main

# Option 3: Emergency hotfix
# Edit files directly, commit, push
```

## Testing

| Test | Command | When |
|------|---------|------|
| Full suite | `bash scripts/test-all.sh` | Every commit |
| Site validation | `bash scripts/validate-site.sh` | Before release |
| Link checker | `python3 scripts/check_links.py .` | Before release |
| Performance | `bash scripts/perf-check.sh` | Ad-hoc (quota limited) |

## Migration

To move to a new host:

1. Copy all files from repo to new hosting
2. Update `CNAME` if using custom domain
3. Run `bash scripts/test-all.sh` to verify
4. Done — no database migration needed

## Files That Matter

| File | Purpose |
|------|---------|
| `index.html` | Main site |
| `crash-course.html` | Course overview |
| `practical-labs.html` | Hands-on exercises |
| `resources.html` | Links + cheat sheets |
| `module-tree.html` | Complete archive |
| `modules/*.html` | 22 course modules |
| `scripts/*.sh` | Testing + release |
| `CNAME` | Custom domain (if used) |
