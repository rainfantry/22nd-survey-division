#!/usr/bin/env bash
# 22nd Survey Division — Master Test Runner
# Run all tests with one command: bash scripts/test-all.sh

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPTS_DIR="$REPO_DIR/scripts"

echo "========================================"
echo "// MASTER TEST RUNNER — 22ND SURVEY DIVISION"
echo "========================================"
echo ""

PASS=0
FAIL=0

run_test() {
    local name="$1"
    local cmd="$2"
    
    echo "[TEST] $name..."
    if eval "$cmd"; then
        echo "  ✓ PASS"
        ((PASS++))
    else
        echo "  ✗ FAIL"
        ((FAIL++))
    fi
    echo ""
}

# Test 1: Site validation
run_test "Site Validation" "bash $SCRIPTS_DIR/validate-site.sh"

# Test 2: Link checker
run_test "Link Checker" "python3 $SCRIPTS_DIR/check_links.py $REPO_DIR"

# Test 3: Lighthouse — SKIPPED in regular CI (quota issues)
# Run ad-hoc: bash scripts/perf-check.sh
echo "  ⚠ Lighthouse skipped in regular CI — run 'bash scripts/perf-check.sh' for performance audit"

# Test 4: Module count
run_test "Module Count" "test $(ls $REPO_DIR/modules/MODULE_*.html | wc -l) -ge 22"

# Test 5: Navigation completeness
run_test "Navigation Check" "test $(grep -l 'MODULE_' $REPO_DIR/modules/MODULE_*.html | wc -l) -ge 22"

# Summary
echo "========================================"
echo "RESULTS: $PASS passed, $FAIL failed"
echo "========================================"

if [ "$FAIL" -eq 0 ]; then
    echo "✓ ALL TESTS PASSED — READY FOR RELEASE"
    exit 0
else
    echo "✗ $FAIL TEST(S) FAILED — FIX BEFORE RELEASE"
    exit 1
fi
