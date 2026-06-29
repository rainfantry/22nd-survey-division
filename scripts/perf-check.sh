#!/usr/bin/env bash
# 22nd Survey Division — Performance Check (Ad-hoc)
# Run this manually when you want Lighthouse scores
# NOT part of regular CI — quota limited

set -e

SITE_URL="https://rainfantry.github.io/22nd-survey-division"
OUTPUT_DIR="lighthouse-reports"

echo "========================================"
echo "// PERFORMANCE CHECK — AD-HOC"
echo "========================================"
echo ""
echo "This script runs PageSpeed Insights on key pages."
echo "Quota: ~100 queries/day per IP. Don't run this in CI."
echo ""

mkdir -p "$OUTPUT_DIR"

PAGES=(
    "index.html:Home"
    "crash-course.html:Crash-Course"
    "practical-labs.html:Practical-Labs"
    "resources.html:Resources"
    "module-tree.html:Module-Tree"
)

ERRORS=0

for entry in "${PAGES[@]}"; do
    page="${entry%%:*}"
    name="${entry##*:}"
    
    echo "[TEST] $name ($page)..."
    
    url="$SITE_URL/$page"
    output_file="$OUTPUT_DIR/${name}-desktop.json"
    
    api_url="https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$url&category=PERFORMANCE&category=ACCESSIBILITY&category=BEST_PRACTICES&category=SEO&strategy=DESKTOP"
    
    response=$(curl -s "$api_url" || true)
    
    if echo "$response" | python3 -c "import sys,json; json.load(sys.stdin)" 2>/dev/null; then
        echo "$response" > "$output_file"
        
        perf=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['performance']['score']*100))" 2>/dev/null || echo "N/A")
        a11y=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['accessibility']['score']*100))" 2>/dev/null || echo "N/A")
        best=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['best-practices']['score']*100))" 2>/dev/null || echo "N/A")
        seo=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['seo']['score']*100))" 2>/dev/null || echo "N/A")
        
        echo "  ✓ Performance: $perf | Accessibility: $a11y | Best Practices: $best | SEO: $seo"
        
        if [ "$perf" != "N/A" ] && [ "$perf" -lt 70 ]; then echo "  ⚠ Performance below 70"; fi
        if [ "$a11y" != "N/A" ] && [ "$a11y" -lt 70 ]; then echo "  ⚠ Accessibility below 70"; fi
    else
        echo "  ✗ API error — check quota or network"
        echo "  Response: $(echo "$response" | head -c 200)"
        ((ERRORS++))
    fi
    
    sleep 2
done

echo ""
echo "========================================"
if [ "$ERRORS" -eq 0 ]; then
    echo "✓ PERFORMANCE CHECK COMPLETE"
    echo "Reports: $OUTPUT_DIR/"
    echo "========================================"
    exit 0
else
    echo "✗ $ERRORS CHECK(S) FAILED"
    echo "========================================"
    exit 1
fi
