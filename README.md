# 22nd Survey Division — Course Site

**Live URL:** https://rainfantry.github.io/22nd-survey-division/
**Repo:** rainfantry/22nd-survey-division (this repo)
**Reader:** https://rainfantry.github.io/books/reader.html (lives in rainfantry/rainfantry.github.io)

Offensive security training. 22 modules, 8 interactive labs. $497 AUD full course.

---

## How the site works (for when you're learning to code)

The site is a single HTML file (`index.html`) — no framework, no build step, no npm. Everything is plain HTML, CSS, and vanilla JavaScript written inline. GitHub Pages serves it directly. Push to `main` → live in ~60 seconds.

### The PIN gate

The site has a gate that blocks access to course content until a PIN is entered. Here's how it works technically:

**On page load:**
```javascript
// Top of <head>, runs before the page renders
if (sessionStorage.getItem('22div_gate_auth') !== '1') {
  document.documentElement.classList.add('course-locked');
}
```
`sessionStorage` is a browser API that stores key-value pairs for the lifetime of a tab. When the tab closes, `sessionStorage` clears. This means every new tab or browser session re-challenges with the PIN.

`document.documentElement` is the `<html>` element. Adding `course-locked` to it triggers CSS rules like:
```css
html.course-locked .mod-card { pointer-events: none; opacity: 0.3; }
html.course-locked #curriculum { filter: blur(4px); }
```
So the content is visible but non-interactive and blurred until auth.

**The PIN modal (`#pin-gate`):**
A `<div>` with `position: fixed; inset: 0` — covers the entire viewport at z-index 99999. It's invisible (`display: none`) until `showGate()` is called.

On page load, the gate IIFE calls `showGate()` automatically if not authenticated:
```javascript
if (!isAuthed()) { showGate(); }
```

**When PIN is entered correctly:**
```javascript
function unlock() {
  sessionStorage.setItem('22div_gate_auth', '1');  // mark auth for this session
  gate.style.opacity = '0';
  setTimeout(() => gate.style.display = 'none', 350);  // fade out
  document.documentElement.classList.remove('course-locked');  // reveal content
}
```

**The PIN verification has two paths:**
1. **API path** — POST to `https://22div.com.au/api/auth.php` with `{pin: val}`. If the server responds `{ok: true}`, unlock. If API is down, fall through.
2. **Fallback** — `if (val === CORRECT)` where `CORRECT = '668340'` is hardcoded in the JS. This is visible in page source — a determined person can read it. It's a temporary measure until the backend is live.

**Rate limiting:** 5 wrong attempts (tracked in `sessionStorage`) locks the input and shows a contact message. Resets on tab close.

### Module progression

The 22 module cards (`#mod-01` through `#mod-22`) have classes `mod-locked`, `mod-unlocked`, or `mod-done`. Progress is tracked in `localStorage` as JSON (`22div_progress`). Completing Module 1's MCQ unlocks Module 2, etc. The cards link to reader.html with a `?b=MODULE_ID` query param.

### Ghost Scraper (`ghost-scraper.html`)

Separate page with its own PIN gate. Already uses `sessionStorage` properly. No backend dependency — the OSINT tool runs in-browser.

---

## Repo structure

```
index.html              — landing page + PIN gate + all 22 module cards
ghost-scraper.html      — OSINT tool with own PIN gate
ads.html                — advertising/campaign page
HANDOFF.md              — operational handoff (auth, reader, deployment)
PAYMENT_INTEGRATION.md  — Stripe/Square webhook setup
SOCIAL_MEDIA_CAMPAIGN.md — 12 LinkedIn + 8 Instagram posts ready to copy
campaign/               — ad creative assets
widgets/                — embeddable widget components
```

---

## Session Log

### 2026-06-27 — PIN Gate Hardened (5 changes to index.html)

**Problem:** The PIN gate was using `document.cookie` for auth state. Browser cookies persist across sessions by default. Once a visitor entered the PIN, the cookie stayed set and they never saw the gate again on return visits. The gate was also dismissible by clicking the dark backdrop outside the PIN box.

**What was changed and why:**

**1. Initial lock check (top of `<head>`, line ~12):**
```javascript
// BEFORE
if (document.cookie.indexOf('22div_gate_auth=1') === -1) {

// AFTER
if (sessionStorage.getItem('22div_gate_auth') !== '1') {
```
`sessionStorage` clears when the browser tab closes. Cookies persist until expiry or manual clear. Using `sessionStorage` means every new browser session requires PIN re-entry.

**2. `unlock()` function — removed cookie and localStorage writes:**
```javascript
// BEFORE
document.cookie = AUTH_KEY + '=1; path=/; SameSite=Strict';
try { localStorage.setItem(AUTH_KEY, '1'); } catch(e) {}

// AFTER
try { sessionStorage.setItem(AUTH_KEY, '1'); } catch(e) {}
```
`localStorage` also persists until manually cleared. Removed both. Only `sessionStorage` now.

**3. `isAuthed()` — now reads sessionStorage:**
```javascript
// BEFORE
return document.cookie.indexOf(AUTH_KEY + '=1') > -1;

// AFTER
try { return sessionStorage.getItem(AUTH_KEY) === '1'; } catch(e) { return false; }
```
The `try/catch` is because `sessionStorage` can throw in some browser privacy modes.

**4. Token storage (API auth path) — removed cookie write:**
```javascript
// BEFORE
if (data.token) document.cookie = '22div_token=' + encodeURIComponent(data.token) + '...';

// AFTER
if (data.token) try { sessionStorage.setItem('22div_token', data.token); } catch(e) {}
```
When `22div.com.au/api/auth.php` is live, it returns a HMAC token. Now stored in sessionStorage instead of a persistent cookie.

**5. Backdrop-click dismiss — removed:**
```javascript
// BEFORE (deleted entirely)
gate.addEventListener('click', function(e) {
  if (e.target === gate) {
    gate.style.display = 'none';  // closed gate without PIN — bypass
  }
});
```
This was a bypass. Clicking outside the PIN box hid the gate without any auth. Content was still CSS-locked (the `course-locked` class was still on `<html>`) so the content wasn't readable, but the overlay was gone and it was confusing. Removed. Gate is now inescapable — you either enter the PIN or close the tab.

**6. Auto-show gate on page load (added):**
```javascript
// NEW — at end of gate IIFE
if (!isAuthed()) { showGate(); }
```
Previously the gate only appeared when you clicked a CTA (like "START LEARNING"). A visitor could scroll the entire landing page — hero, pricing, curriculum — without ever seeing the PIN prompt. Now it shows immediately on load if not authed in this session. Still allows scrolling the landing page because clicking the backdrop no longer closes it — but it's clearly there.

**Current state:** Commit `a5547fe`, pushed to `main`. GitHub Pages: live.

**What to do next:**

1. **Payment gateway (the real fix):**
   - Set up Stripe Checkout or Square. When payment succeeds, Stripe sends a webhook to `22div.com.au/api/purchase.php`.
   - The backend generates a customer-specific PIN (or re-uses `668340` for now) and emails it to the buyer.
   - See `PAYMENT_INTEGRATION.md` for the full Stripe webhook flow.

2. **Remove the hardcoded PIN:**
   - Once the backend (`22div.com.au/api/auth.php`) is live and PIN validation goes server-side, remove `var CORRECT = '668340'` from `index.html`.
   - The fallback client-side check is a security hole — it's visible in page source.

3. **SQL backend (ready to deploy):**
   - Files at `C:\Users\gwu07\Desktop\repos\22div-backend\` — PHP + MySQL.
   - Argon2id hashed PINs, rate limiting per IP, HMAC session tokens.
   - cPanel: `https://S06ee.syd5.hostingplatform.net.au:2083` — login: `divcom22`.
   - See `HANDOFF.md` → Option B for 7-step cPanel deployment.
