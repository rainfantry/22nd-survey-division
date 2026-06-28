# Payment Gateway Integration — 22nd Survey Division

**Current state:** PIN gate `668340` (placeholder).  
**Replace with:** Payment provider checkout redirect.  
**ACN:** 692 429 397 — OCCUPATION FORCE CALLSIGN GSW PTY. LTD. t/a 22ND SURVEY DIVISION  
**Currency:** AUD  

---

## How the swap works

The PIN gate lives in two places in `index.html`:

1. **`<div id="pin-gate">`** — the overlay HTML (keep as loading indicator or remove)
2. **Bottom `<script>` block** — the `interceptCourseLink` function that intercepts clicks

**To integrate payment**, replace the `interceptCourseLink` logic so that instead of showing the PIN box, it redirects to your payment provider's checkout. On successful payment, the provider redirects back to your site with a session token — you store that in `localStorage` the same way the PIN gate does (`22div_gate_auth = '1'`).

---

## Option A — Stripe (Recommended for AU)

Stripe is the easiest option with full AUD support, Afterpay, and AU bank transfer.

### Setup
1. Register at [stripe.com/au](https://stripe.com/au) with your ACN 692 429 397
2. Create a **Payment Link** (no server needed for static sites):
   - Dashboard → Payment Links → Create
   - Product: "22DIV Course Access" — set price in AUD
   - Success URL: `https://rainfantry.github.io/22nd-survey-division/?access=stripe_success`
3. Copy the Payment Link URL (format: `https://buy.stripe.com/XXXX`)

### index.html swap

Replace the `showGate` call in `interceptCourseLink` with:

```javascript
// Replace the IIFE at the bottom of index.html with this:
(function() {
  var AUTH_KEY = '22div_gate_auth';

  function isAuthed() {
    return localStorage.getItem(AUTH_KEY) === '1';
  }

  // Check for Stripe success redirect
  var params = new URLSearchParams(location.search);
  if (params.get('access') === 'stripe_success') {
    localStorage.setItem(AUTH_KEY, '1');
    // Clean URL
    history.replaceState(null, '', location.pathname);
  }

  function interceptCourseLink(el, action) {
    el.addEventListener('click', function(e) {
      if (isAuthed()) return;
      e.preventDefault();
      e.stopPropagation();
      // Redirect to Stripe checkout
      window.location.href = 'https://buy.stripe.com/YOUR_PAYMENT_LINK_ID';
    }, true);
  }

  // Wire up all course access points (same selectors as PIN gate)
  document.querySelectorAll('a[href="#curriculum"], .nav-cta').forEach(function(a) {
    interceptCourseLink(a, function() {
      var el = document.getElementById('curriculum');
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    });
  });

  document.querySelectorAll('[id^="mod-"]').forEach(function(el) {
    if (el.tagName === 'A') {
      var href = el.getAttribute('href');
      interceptCourseLink(el, function() { if (href) window.location.href = href; });
    }
  });

  document.querySelectorAll('a[href*="evasion-lab"], a[href*="reader.html"], a[href*="books/"]').forEach(function(a) {
    var href = a.getAttribute('href');
    interceptCourseLink(a, function() { window.location.href = href; });
  });

  window.requireAuth = function(href) {
    if (isAuthed()) { window.location.href = href; return; }
    window.location.href = 'https://buy.stripe.com/YOUR_PAYMENT_LINK_ID';
  };
})();
```

### Afterpay (via Stripe)
Afterpay is automatically available in Stripe AU for amounts AUD $1–$2,000.  
Enable: Stripe Dashboard → Settings → Payment Methods → Afterpay/Clearpay → Enable.  
No code changes required — it appears as a payment option in the Stripe-hosted checkout.

---

## Option B — Square

Square AU supports EFTPOS, credit/debit, and Afterpay via their online checkout.

### Setup
1. Register at [squareup.com/au](https://squareup.com/au) — use ACN 692 429 397
2. Create a **Payment Link**:
   - Square Dashboard → Online → Payment Links → Create
   - Add item: "22DIV Course Access" — AUD price
   - Copy the generated URL (format: `https://square.link/u/XXXX`)

### Success URL
Square Payment Links support a redirect after payment.  
Set redirect to: `https://rainfantry.github.io/22nd-survey-division/?access=square_success`

Update the check in `interceptCourseLink`:
```javascript
if (params.get('access') === 'square_success') {
  localStorage.setItem(AUTH_KEY, '1');
  history.replaceState(null, '', location.pathname);
}
```

---

## Option C — Pin Payments (AU-native, no US entity)

Pin Payments is an Australian-owned gateway — no Stripe US parent company.  
ABN/ACN accepted directly. Lower fees for AUD transactions.

- Register: [pinpayments.com](https://pinpayments.com)
- Supports: Visa, Mastercard, AMEX, EFTPOS
- No Afterpay native (use Zip instead)
- Hosted checkout URL pattern: `https://checkout.pinpayments.com/XXXX`

Integration approach is identical to Stripe — replace the redirect URL.

---

## Option D — Zip (AU buy-now-pay-later)

For students who need payment plans:
- Register at [zip.co/au/business](https://zip.co/au/business)
- Zip Pay (up to $1,000) and Zip Money (up to $50,000) available
- Hosted checkout with redirect on success

---

## Security notes

- **Never validate access server-side** on a static site — this is client-side only.  
  `localStorage.getItem('22div_gate_auth') === '1'` is a UX gate, not a DRM system.
- When you move to a real domain + backend: replace localStorage with a JWT cookie validated server-side on every book fetch.
- **`BLACKOPS`**: Remove the PIN gate `<div id="pin-gate">` block entirely once payment is live — it's a placeholder, not required.

---

## Next steps when domain is ready

1. Register domain (recommend: `22div.com.au` — matches your 22div.com.au hosting)
2. Point CNAME to `rainfantry.github.io` OR migrate off GitHub Pages to a VPS
3. Add HTTPS (GitHub Pages: automatic; VPS: Let's Encrypt via certbot)
4. Update payment success URLs from `rainfantry.github.io/...` to `22div.com.au/...`
5. Update ACN footer links and contact email

---

## GST

Your ABN (50 692 429 397) shows GST not registered.  
You do **not** charge GST until you hit $75,000 AUD annual turnover.  
At that threshold: register for GST with ATO, add 10% to course price, lodge BAS quarterly.  
All major gateways support GST-inclusive pricing with automatic BAS reporting.
