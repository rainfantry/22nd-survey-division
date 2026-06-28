# 22nd Survey Division — Final Validation Checklist
## Automated + Manual Verification Protocol

### Automated Checks (Run Every Build)

#### 1. Link Validation
```bash
# Check all module links return 200
for mod in $(curl -s https://rainfantry.github.io/22nd-survey-division/index.html | grep -o 'modules/[^"]*\.html' | sort -u); do
    echo -n "Checking $mod... "
    curl -s -o /dev/null -w "%{http_code}" "https://rainfantry.github.io/22nd-survey-division/$mod"
    echo ""
done
```

#### 2. Image Validation
```bash
# Check all images load
for img in $(curl -s https://rainfantry.github.io/22nd-survey-division/index.html | grep -o 'https://[^"]*\.(jpg|png|gif|svg)' | sort -u); do
    echo -n "Checking $img... "
    curl -s -o /dev/null -w "%{http_code}" "$img"
    echo ""
done
```

#### 3. Mobile Responsiveness
```bash
# Use Google Mobile-Friendly Test API
curl -s "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key=API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://rainfantry.github.io/22nd-survey-division/", "requestScreenshot": true}'
```

#### 4. Performance (Lighthouse)
```bash
# Run Lighthouse CI
lighthouse https://rainfantry.github.io/22nd-survey-division/ \
  --output=json --output-path=./lighthouse-report.json \
  --chrome-flags="--headless" \
  --only-categories=performance,accessibility,best-practices,seo
```

### Manual Checks (Run Before Release)

#### 1. Layman Readability
- [ ] Open module in incognito window
- [ ] Read first 3 sections without technical knowledge
- [ ] Can you explain what the module teaches to a CEO?
- [ ] Are there more than 3 undefined technical terms per section?
- [ ] Do the "Why it works" boxes make sense?

#### 2. Copy-Paste Verification
- [ ] Open any module with code blocks
- [ ] Copy code block to clipboard
- [ ] Paste into terminal/IDE
- [ ] Does it run without modification?
- [ ] Are there any missing imports or dependencies?

#### 3. Screenshot Placement
- [ ] Every build output has a screenshot within 2 scrolls
- [ ] Every verification result has a screenshot
- [ ] Screenshots have timestamps visible
- [ ] Screenshots match the command output
- [ ] No placeholder images ("image coming soon")

#### 4. CEO Translation
- [ ] Open CEO_TRANSLATION.html
- [ ] Read any module summary
- [ ] Can you explain the dollar impact?
- [ ] Is the blame chain plausible?
- [ ] Would a non-technical executive take action?

#### 5. Glossary Functionality
- [ ] Open glossary.html
- [ ] Search for "AMSI" — does it appear?
- [ ] Click category filter "WINDOWS" — does it filter?
- [ ] Click module link — does it navigate?
- [ ] Is the definition understandable without reading the module?

#### 6. Navigation
- [ ] From index, click each module chip
- [ ] From module, click HOME
- [ ] From module, click previous/next
- [ ] From module, click glossary link
- [ ] All navigation works without 404

#### 7. Payment Flow
- [ ] Click BUY NOW
- [ ] Select Stripe payment
- [ ] Enter test card (4242 4242 4242 4242)
- [ ] Complete payment
- [ ] Receive confirmation email
- [ ] Download link works

#### 8. Tool Release Pipeline
- [ ] Run release_pipeline.sh
- [ ] Verify 7z files created
- [ ] Verify PASSWORD.txt generated
- [ ] Verify RELEASE_NOTES.txt exists
- [ ] Test decrypt: 7z x -p[password] file.7z
- [ ] Verify binaries run on clean VM

### Automated Scan Script
```bash
#!/bin/bash
# 22sd-validate.sh — Full site validation

SITE="https://rainfantry.github.io/22nd-survey-division"
ERRORS=0

echo "=== 22SD VALIDATION SCAN ==="
echo "Date: $(date)"
echo ""

# 1. Link check
echo "--- LINK CHECK ---"
for mod in $(curl -s $SITE/index.html | grep -o 'modules/[^"]*\.html' | sort -u); do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$SITE/$mod")
    if [ "$STATUS" != "200" ]; then
        echo "FAIL: $mod ($STATUS)"
        ERRORS=$((ERRORS+1))
    fi
done
echo "Link check complete. Errors: $ERRORS"

# 2. Image check
echo "--- IMAGE CHECK ---"
for img in $(curl -s $SITE/index.html | grep -o 'https://[^"]*\.(jpg|png|gif|svg)' | sort -u); do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$img")
    if [ "$STATUS" != "200" ]; then
        echo "FAIL: $img ($STATUS)"
        ERRORS=$((ERRORS+1))
    fi
done
echo "Image check complete. Errors: $ERRORS"

# 3. Keyword glossary check
echo "--- GLOSSARY CHECK ---"
if curl -s "$SITE/glossary.html" | grep -q "AMSI"; then
    echo "PASS: Glossary contains AMSI"
else
    echo "FAIL: Glossary missing AMSI"
    ERRORS=$((ERRORS+1))
fi

# 4. CEO translation check
echo "--- CEO CHECK ---"
if curl -s "$SITE/modules/CEO_TRANSLATION.html" | grep -q "dollar impact"; then
    echo "PASS: CEO translation has dollar impact"
else
    echo "FAIL: CEO translation missing dollar impact"
    ERRORS=$((ERRORS+1))
fi

# 5. Mobile meta check
echo "--- MOBILE CHECK ---"
if curl -s "$SITE/index.html" | grep -q "viewport"; then
    echo "PASS: Viewport meta tag present"
else
    echo "FAIL: Missing viewport meta tag"
    ERRORS=$((ERRORS+1))
fi

echo ""
echo "=== VALIDATION COMPLETE ==="
echo "Total errors: $ERRORS"
if [ $ERRORS -eq 0 ]; then
    echo "STATUS: PASS"
    exit 0
else
    echo "STATUS: FAIL"
    exit 1
fi
```

### Release Criteria
- [ ] All automated checks pass
- [ ] All manual checks pass
- [ ] Zero 404 errors
- [ ] All images load
- [ ] Mobile responsive (Lighthouse > 90)
- [ ] Accessibility compliant (Lighthouse > 90)
- [ ] Payment flow tested
- [ ] Tool pipeline tested
- [ ] CEO translation reviewed by non-technical person
- [ ] Glossary tested by student

### Post-Release Monitoring
- [ ] Google Analytics tracking
- [ ] Error tracking (Sentry)
- [ ] Uptime monitoring (UptimeRobot)
- [ ] Payment success rate (Stripe dashboard)
- [ ] Support ticket volume
- [ ] Student completion rate
- [ ] Tool download rate
- [ ] Refund rate (< 5%)
