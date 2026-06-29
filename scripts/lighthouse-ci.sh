#!/usr/bin/env bash
# 22nd Survey Division — Lighthouse CI Script
# Runs PageSpeed Insights on key pages and saves results
# Requires: curl, python3 (for json parsing)

set -e

SITE_URL="https://rainfantry.github.io/22nd-survey-division"
OUTPUT_DIR="lighthouse-reports"
API_KEY="${LIGHTHOUSE_API_KEY:-}"  # Optional: set for higher quota

echo "========================================"
echo "// LIGHTHOUSE CI — 22ND SURVEY DIVISION"
echo "========================================"
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
    
    # Call PageSpeed Insights API
    if [ -n "$API_KEY" ]; then
        api_url="https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$url&category=PERFORMANCE&category=ACCESSIBILITY&category=BEST_PRACTICES&category=SEO&strategy=DESKTOP&key=$API_KEY"
    else
        api_url="https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$url&category=PERFORMANCE&category=ACCESSIBILITY&category=BEST_PRACTICES&category=SEO&strategy=DESKTOP"
    fi
    
    response=$(curl -s "$api_url" || true)
    
    # Check if response is valid JSON
    if echo "$response" | python3 -c "import sys,json; json.load(sys.stdin)" 2>/dev/null; then
        # Save raw response
        echo "$response" > "$output_file"
        
        # Extract scores
        perf=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['performance']['score']*100))" 2>/dev/null || echo "N/A")
        a11y=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['accessibility']['score']*100))" 2>/dev/null || echo "N/A")
        best=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['best-practices']['score']*100))" 2>/dev/null || echo "N/A")
        seo=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(round(d['lighthouseResult']['categories']['seo']['score']*100))" 2>/dev/null || echo "N/A")
        
        echo "  ✓ Performance: $perf | Accessibility: $a11y | Best Practices: $best | SEO: $seo"
        
        # Flag low scores
        if [ "$perf" != "N/A" ] && [ "$perf" -lt 70 ]; then
            echo "  ⚠ Performance below 70 — needs optimization"
        fi
        if [ "$a11y" != "N/A" ] && [ "$a11y" -lt 70 ]; then
            echo "  ⚠ Accessibility below 70 — needs ARIA labels"
        fi
    else
        echo "  ✗ API error (quota exceeded or network issue)"
        echo "  Response: $(echo "$response" | head -c 200)"
        ((ERRORS++))
    fi
    
    sleep 2  # Rate limiting
done

echo ""
echo "========================================"
if [ "$ERRORS" -eq 0 ]; then
    echo "✓ LIGHTHOUSE COMPLETE — Reports in $OUTPUT_DIR/"
    echo "========================================"
    exit 0
else
    echo "✗ $ERRORS LIGHTHOUSE TEST(S) FAILED"
    echo "========================================"
    exit 1
fi
