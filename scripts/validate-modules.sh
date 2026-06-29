#!/bin/bash
# 22ND SURVEY DIVISION — Module Validation Runner
# Usage: bash validate-modules.sh [MODULE_NAME] or bash validate-modules.sh all

REPO_DIR="/c/Users/gwu07/Desktop/repos/22nd-survey-division"
MODULES_DIR="$REPO_DIR/modules"
LOG_DIR="$REPO_DIR/scripts"
DATE=$(date -u +"%Y-%m-%d-%H%M")

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
AMBER='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}// MODULE VALIDATION RUNNER${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""

# Function to validate a single module
validate_module() {
    local module="$1"
    local module_path="$MODULES_DIR/${module}.html"
    
    if [ ! -f "$module_path" ]; then
        echo -e "${RED}✗ $module not found${NC}"
        return 1
    fi
    
    echo -e "${CYAN}// Validating $module...${NC}"
    
    # Check file size
    local size=$(wc -l < "$module_path")
    echo "  Lines: $size"
    
    # Check for navigation (multiple possible patterns)
    if grep -qE "class=\"nav\"|class='nav'|id=\"nav\"|id='nav'|href=\"MODULE_[0-9]+|href='MODULE_[0-9]+|← PREV|NEXT →|HOME" "$module_path" 2>/dev/null; then
        echo -e "  ${GREEN}✓ Navigation present${NC}"
    else
        echo -e "  ${AMBER}⚠ Navigation missing${NC}"
    fi
    
    # Check for evidence boxes
    local evidence_count=$(grep -c "evidence-box\|evidence-header" "$module_path" 2>/dev/null || echo "0")
    echo "  Evidence boxes: $evidence_count"
    # Check for mentor callouts (broader patterns)
    local mentor_count
    mentor_count=$(grep -icE "mentor|asi dev|lessons-from-teacher|mentor note|mentor says|mentor.*teaches|mentor.*words|mentor.*means" "$module_path" 2>/dev/null || echo "0")
    echo "  Mentor callouts: $mentor_count"
    
    # Check for cross-links
    local crosslink_count=$(grep -c "cross-link\|href=\"MODULE_" "$module_path" 2>/dev/null || echo "0")
    echo "  Cross-links: $crosslink_count"
    
    # Check for quizzes
    local quiz_count=$(grep -c "quiz\|question\|answer" "$module_path" 2>/dev/null || echo "0")
    echo "  Quiz elements: $quiz_count"
    
    # Check for copy buttons
    local copy_count=$(grep -c "copy-btn\|copyCode" "$module_path" 2>/dev/null || echo "0")
    echo "  Copy buttons: $copy_count"
    
    # Size assessment
    if [ "$size" -lt 500 ]; then
        echo -e "  ${RED}✗ TOO SHORT — needs expansion${NC}"
    elif [ "$size" -lt 1000 ]; then
        echo -e "  ${AMBER}⚠ Thin — consider expansion${NC}"
    else
        echo -e "  ${GREEN}✓ Good size${NC}"
    fi
    
    echo ""
}

# Main
if [ "$1" == "all" ] || [ -z "$1" ]; then
    echo "Validating all modules..."
    echo ""
    
    # Auto-discover all MODULE_*.html files
    for module_path in "$MODULES_DIR"/MODULE_*.html; do
        module=$(basename "$module_path" .html)
        validate_module "$module"
    done
    
    # Run full test suite
    echo -e "${CYAN}// Running full test suite...${NC}"
    cd "$REPO_DIR" && bash scripts/test-all.sh
    
elif [ "$1" == "list" ]; then
    echo "Available modules:"
    ls -1 "$MODULES_DIR"/MODULE_*.html | sed 's/.*\///' | sed 's/\.html$//' | sort
    
else
    validate_module "$1"
fi

echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}// Validation complete${NC}"
echo -e "${CYAN}========================================${NC}"
