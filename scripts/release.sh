#!/usr/bin/env bash
# 22nd Survey Division — Release Script
# Creates a GitHub release with version tag and release notes

set -e

REPO="rainfantry/22nd-survey-division"
VERSION="${1:-v$(date +%Y.%m.%d-%H%M)}"
NOTES_FILE="${2:-RELEASE_NOTES.md}"

echo "========================================"
echo "// RELEASE SCRIPT — 22ND SURVEY DIVISION"
echo "========================================"
echo "Version: $VERSION"
echo ""

# Run validation first
echo "[1/4] Running site validation..."
if bash "$(dirname "$0")/validate-site.sh"; then
    echo "✓ Validation passed"
else
    echo "✗ Validation failed — aborting release"
    exit 1
fi

echo ""

# Run Lighthouse
echo "[2/4] Running Lighthouse CI..."
if bash "$(dirname "$0")/lighthouse-ci.sh"; then
    echo "✓ Lighthouse passed"
else
    echo "⚠ Lighthouse failed (non-blocking — check reports manually)"
fi

echo ""

# Generate release notes
echo "[3/4] Generating release notes..."
cat > "$NOTES_FILE" << EOF
# Release $VERSION — 22nd Survey Division

## Site Status
- $(date -u +"%Y-%m-%d %H:%M UTC")
- All modules: $(ls modules/MODULE_*.html | wc -l) HTML files
- Navigation: Complete (all modules linked)
- Interactive quizzes: $(grep -c 'sim-option' practical-labs.html 2>/dev/null || echo 0) options
- Copy buttons: Enabled on practical-labs + resources

## Test Results
$(cat lighthouse-reports/*.json 2>/dev/null | python3 -c "
import sys, json, glob
for f in glob.glob('lighthouse-reports/*-desktop.json'):
    try:
        d = json.load(open(f))
        name = f.split('/')[-1].replace('-desktop.json', '')
        perf = round(d['lighthouseResult']['categories']['performance']['score']*100)
        a11y = round(d['lighthouseResult']['categories']['accessibility']['score']*100)
        best = round(d['lighthouseResult']['categories']['best-practices']['score']*100)
        seo = round(d['lighthouseResult']['categories']['seo']['score']*100)
        print(f'- {name}: Performance {perf} | Accessibility {a11y} | Best Practices {best} | SEO {seo}')
    except:
        pass
" 2>/dev/null || echo "- Lighthouse reports pending")

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
4. Test with: bash scripts/validate-site.sh

EOF

echo "✓ Release notes written to $NOTES_FILE"

echo ""

# Create Git tag and release
echo "[4/4] Creating GitHub release..."
git add -A
git commit -m "Release $VERSION — $(date +%Y-%m-%d)" || true
git tag -a "$VERSION" -m "Release $VERSION" || {
    echo "⚠ Tag $VERSION already exists — updating"
    git tag -d "$VERSION" || true
    git tag -a "$VERSION" -m "Release $VERSION"
}
git push origin main

# Check if gh CLI is available for release creation
if command -v gh &> /dev/null; then
    gh release create "$VERSION" \
        --title "22nd Survey Division $VERSION" \
        --notes-file "$NOTES_FILE" \
        --repo "$REPO" || {
        echo "⚠ gh release failed — create manually at https://github.com/$REPO/releases/new"
    }
else
    echo "⚠ gh CLI not installed — create release manually at:"
    echo "  https://github.com/$REPO/releases/new?tag=$VERSION"
fi

echo ""
echo "========================================"
echo "✓ RELEASE $VERSION COMPLETE"
echo "========================================"
