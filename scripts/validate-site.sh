#!/usr/bin/env bash
# 22nd Survey Division — Site Validation Script
# Run this after any major change to verify nothing is broken

set -e

SITE_URL="https://rainfantry.github.io/22nd-survey-division"
REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
ERRORS=0

echo "========================================"
echo "// 22ND SURVEY DIVISION — SITE VALIDATOR"
echo "========================================"
echo ""

# Test 1: All main pages load (HTTP 200)
echo "[TEST 1] Checking main pages..."
PAGES=("index.html" "crash-course.html" "practical-labs.html" "resources.html" "module-tree.html")
for page in "${PAGES[@]}"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "$SITE_URL/$page")
    if [ "$status" = "200" ]; then
        echo "  ✓ $page ($status)"
    else
        echo "  ✗ $page ($status) ← BROKEN"
        ((ERRORS++))
    fi
done
echo ""

# Test 2: All module pages load
echo "[TEST 2] Checking module pages..."
for module in "$REPO_DIR"/modules/MODULE_*.html; do
    name=$(basename "$module")
    status=$(curl -s -o /dev/null -w "%{http_code}" "$SITE_URL/modules/$name")
    if [ "$status" = "200" ]; then
        echo "  ✓ $name"
    else
        echo "  ✗ $name ($status) ← BROKEN"
        ((ERRORS++))
    fi
done
echo ""

# Test 3: Navigation links exist in modules
echo "[TEST 3] Checking module navigation..."
for module in "$REPO_DIR"/modules/MODULE_*.html; do
    name=$(basename "$module")
    if grep -q "MODULE_" "$module" 2>/dev/null; then
        echo "  ✓ $name has navigation"
    else
        echo "  ✗ $name missing navigation ← BROKEN"
        ((ERRORS++))
    fi
done
echo ""

# Test 4: No broken internal links
echo "[TEST 4] Checking internal links..."
# Extract all hrefs and verify they exist
python3 "$REPO_DIR/scripts/check_links.py" "$REPO_DIR" || ((ERRORS++))
echo ""

# Test 5: Copy buttons exist on practical-labs and resources
echo "[TEST 5] Checking copy buttons..."
for page in "practical-labs.html" "resources.html"; do
    if curl -s "$SITE_URL/$page" | grep -q "copy-btn"; then
        echo "  ✓ $page has copy buttons"
    else
        echo "  ✗ $page missing copy buttons"
        ((ERRORS++))
    fi
done
echo ""

# Test 6: Interactive quiz elements exist
echo "[TEST 6] Checking interactive quizzes..."
if curl -s "$SITE_URL/practical-labs.html" | grep -q "sim-option"; then
    count=$(curl -s "$SITE_URL/practical-labs.html" | grep -c "sim-option")
    echo "  ✓ practical-labs has $count quiz options"
else
    echo "  ✗ practical-labs missing quiz options"
    ((ERRORS++))
fi
echo ""

# Test 7: Module tree has all modules
echo "[TEST 7] Checking module tree completeness..."
MODULE_COUNT=$(curl -s "$SITE_URL/module-tree.html" | grep -c "module-item")
if [ "$MODULE_COUNT" -ge 22 ]; then
    echo "  ✓ module-tree has $MODULE_COUNT modules (expected 22+)"
else
    echo "  ✗ module-tree has only $MODULE_COUNT modules (expected 22+)"
    ((ERRORS++))
fi
echo ""

# Summary
echo "========================================"
if [ "$ERRORS" -eq 0 ]; then
    echo "✓ ALL TESTS PASSED — SITE IS HEALTHY"
    echo "========================================"
    exit 0
else
    echo "✗ $ERRORS TEST(S) FAILED — FIX BEFORE RELEASE"
    echo "========================================"
    exit 1
fi
