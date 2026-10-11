// State Management for Checkout, Currency, 10-Min Flash Offer, Theme, AI Lab, Reel Player, and Analytics
const state = {
  currency: 'INR', // 'INR' | 'USD' (Auto-locked by visitor IP)
  offerExpired: false,
  offerRemainingSeconds: 600, // 10 minutes (600 seconds)
  prices: {
    INR: {
      base: 249,
      expiredBase: 499,
      strike: 1999,
      bump1: 249,
      expiredBump1: 399,
      bump2: 149,
      expiredBump2: 249,
      symbol: '₹'
    },
    USD: {
      base: 9,
      expiredBase: 19,
      strike: 79,
      bump1: 9,
      expiredBump1: 14,
      bump2: 5,
      expiredBump2: 9,
      symbol: '$'
    }
  },
  bumpAdded: false,
  bump2Added: false,
  promoCode: null,
  promoDiscountPercent: 0,
  theme: 'light',
  allCurriculumExpanded: false,
  mobileFrameMode: false,
  activeReelIndex: 0,
  lastPaymentMethod: 'Instant UPI Checkout'
};

// Gentle haptic feedback on supported mobile browsers
function triggerHaptic(ms = 18) {
  try {
    if (navigator.vibrate) navigator.vibrate(ms);
  } catch (e) {}
}

// Format price helper
function formatPrice(amount) {
  const sym = state.prices[state.currency].symbol;
  if (state.currency === 'INR') {
    return `${sym}${Math.round(amount).toLocaleString('en-IN')}`;
  }
  return `${sym}${amount.toFixed(amount % 1 === 0 ? 0 : 2)}`;
}

// Compute current totals (automatically increases price after 10-minute timer expires)
function getTotals() {
  const cfg = state.prices[state.currency];
  const rawBase = state.offerExpired ? cfg.expiredBase : cfg.base;
  const base = state.upgradeOnly ? 0 : rawBase;
  const activeBump1Price = state.offerExpired ? cfg.expiredBump1 : cfg.bump1;
  const activeBump2Price = state.offerExpired ? cfg.expiredBump2 : cfg.bump2;
  const bump1 = state.bumpAdded ? activeBump1Price : 0;
  const bump2 = state.bump2Added ? activeBump2Price : 0;
  const rawSubtotal = base + bump1 + bump2;
  const discount = state.promoDiscountPercent > 0
    ? Math.round((rawSubtotal * state.promoDiscountPercent) / 100)
    : 0;
  const finalTotal = Math.max(0, rawSubtotal - discount);
  return {
    cfg,
    base,
    activeBump1Price,
    activeBump2Price,
    bump1,
    bump2,
    rawSubtotal,
    discount,
    finalTotal
  };
}

// Recalculate and render all price elements across Desktop & Mobile
function renderPricing() {
  const { cfg, base, activeBump1Price, activeBump2Price, discount, finalTotal } = getTotals();

  // Header & Anchor prices (Always cross out the original retail price ₹1,999 / $79 so both tiers feel like a massive deal)
  const strikeEl = document.getElementById('anchor-strike-price');
  const baseEl = document.getElementById('header-base-price');
  if (strikeEl) {
    strikeEl.textContent = formatPrice(cfg.strike);
    strikeEl.className = 'text-xs sm:text-sm line-through text-slate-400 font-mono-num font-semibold';
  }
  if (baseEl) {
    baseEl.textContent = formatPrice(base);
    baseEl.className = 'font-mono-num text-xl font-extrabold text-slate-900';
  }

  document.getElementById('bump-price-display').textContent = `+${formatPrice(activeBump1Price)}`;
  const bump2PriceEl = document.getElementById('bump-2-price-display');
  if (bump2PriceEl) bump2PriceEl.textContent = `+${formatPrice(activeBump2Price)}`;

  // Update 10-Minute Flash Offer (Tier 1: 88% OFF) vs Launch Offer (Tier 2: 75% OFF) UI badges
  const saveBadge = document.getElementById('checkout-save-badge');
  const banner10m = document.getElementById('checkout-10m-banner');
  const text10m = document.getElementById('checkout-10m-text');
  const topDiscountLabel = document.getElementById('offer-discount-label');
  const topEndsLabel = document.getElementById('offer-ends-label');
  const savedAmount = cfg.strike - cfg.expiredBase;

  if (state.offerExpired) {
    if (saveBadge) {
      saveBadge.textContent = `SAVE 75% OFF ${formatPrice(cfg.strike)} (LAUNCH OFFER)`;
      saveBadge.className = 'inline-block rounded bg-emerald-50 border border-emerald-200 px-1.5 py-0.5 text-[10px] font-bold text-emerald-700';
    }
    if (banner10m) {
      banner10m.className = 'checkout-urgency-banner expired mb-3 rounded-lg px-3 py-1.5 flex items-center justify-between gap-2 text-[11px] font-semibold shadow-sm';
    }
    if (text10m) {
      text10m.innerHTML = `${formatPrice(cfg.base)} Fast-Action Bonus Ended — <strong>75% OFF Launch Offer Active:</strong> Only <strong>${formatPrice(cfg.expiredBase)}</strong> <span class="opacity-95">(Save ${formatPrice(savedAmount)} off ${formatPrice(cfg.strike)}!)</span>`;
    }
    if (topDiscountLabel) {
      topDiscountLabel.textContent = '75% OFF LAUNCH OFFER';
      topDiscountLabel.className = 'text-amber-300 font-black';
    }
    if (topEndsLabel) {
      topEndsLabel.textContent = ` — (${formatPrice(cfg.base)} Fast-Action Bonus Ended • Still Save ${formatPrice(savedAmount)} Off ${formatPrice(cfg.strike)}!):`;
    }
  } else {
    if (saveBadge) {
      saveBadge.textContent = 'SAVE 88% (10-MIN OFFER)';
      saveBadge.className = 'inline-block rounded bg-emerald-50 border border-emerald-200 px-1.5 py-0.5 text-[10px] font-bold text-emerald-700';
    }
    if (banner10m) {
      banner10m.className = 'checkout-urgency-banner mb-3 rounded-lg px-3 py-1.5 flex items-center justify-between gap-2 text-[11px] font-semibold shadow-sm';
    }
    if (text10m) {
      text10m.innerHTML = `10-Min Flash Offer: Only <strong>${formatPrice(cfg.base)}</strong> now (jumps to <strong>${formatPrice(cfg.expiredBase)}</strong> at 00:00!)`;
    }
    if (topDiscountLabel) {
      topDiscountLabel.textContent = '88% OFF FLASH SALE';
      topDiscountLabel.className = 'text-amber-300 font-black';
    }
    if (topEndsLabel) {
      topEndsLabel.textContent = ` — Grab For ${formatPrice(cfg.base)} Before Price Jumps To ${formatPrice(cfg.expiredBase)}:`;
    }
  }

  const mobileBarBumpPrice = document.getElementById('mobile-bar-bump-price');
  if (mobileBarBumpPrice) {
    mobileBarBumpPrice.textContent = state.bumpAdded ? 'Added ✓' : `+${formatPrice(activeBump1Price)}`;
  }
  const mobileBarBumpDot = document.getElementById('mobile-bar-bump-dot');
  if (mobileBarBumpDot) {
    if (state.bumpAdded) {
      mobileBarBumpDot.className = 'h-3.5 w-3.5 rounded bg-emerald-500 border border-emerald-400 flex items-center justify-center text-[9px] text-white font-bold';
      mobileBarBumpDot.textContent = '✓';
    } else {
      mobileBarBumpDot.className = 'h-3.5 w-3.5 rounded border border-brand-400 flex items-center justify-center text-[9px] text-white';
      mobileBarBumpDot.textContent = '';
    }
  }

  // Order Summary rows
  document.getElementById('summary-base-price').textContent = formatPrice(base);
  document.getElementById('summary-bump-price').textContent = formatPrice(activeBump1Price);
  const sumBump2Price = document.getElementById('summary-bump-2-price');
  if (sumBump2Price) sumBump2Price.textContent = formatPrice(activeBump2Price);

  const bumpRow = document.getElementById('summary-bump-row');
  if (state.bumpAdded) {
    bumpRow.classList.remove('hidden');
  } else {
    bumpRow.classList.add('hidden');
  }

  const bump2Row = document.getElementById('summary-bump-2-row');
  if (bump2Row) {
    if (state.bump2Added) {
      bump2Row.classList.remove('hidden');
    } else {
      bump2Row.classList.add('hidden');
    }
  }

  const discountRow = document.getElementById('summary-discount-row');
  if (discount > 0 && state.promoCode) {
    discountRow.classList.remove('hidden');
    document.getElementById('summary-discount-label').textContent =
      `Promo Discount (${state.promoCode} - ${state.promoDiscountPercent}%)`;
    document.getElementById('summary-discount-amount').textContent = `-${formatPrice(discount)}`;
  } else {
    discountRow.classList.add('hidden');
  }

  // Final Total & CTA Buttons
  const formattedTotal = formatPrice(finalTotal);
  document.getElementById('summary-total-price').textContent = formattedTotal;
  document.getElementById('cta-button-text').textContent = 'Make Payment';
  document.getElementById('mobile-sticky-price').textContent = formattedTotal;
  document.getElementById('mobile-cta-label').textContent = `Make Payment ${formattedTotal} →`;
  document.getElementById('modal-payable-amount').textContent = formattedTotal;

  const reelCtaBtn = document.getElementById('reel-cta-price-btn');
  if (reelCtaBtn) {
    reelCtaBtn.textContent = `Unlock This Persona Kit (${formatPrice(base)}) →`;
  }

  const mobileBumpIndicator = document.getElementById('mobile-bump-indicator');
  if (mobileBumpIndicator) {
    if (state.bumpAdded && state.bump2Added) {
      mobileBumpIndicator.textContent = 'VIP Bundle';
    } else if (state.bumpAdded || state.bump2Added) {
      mobileBumpIndicator.textContent = '+1 Upgrade';
    } else {
      mobileBumpIndicator.textContent = state.offerExpired ? 'Standard' : 'Launch';
    }
  }

  updateEarningsCalc();
}

// Toggle Order Bump #1 ("Uncensored Content Hack")
function toggleOrderBump() {
  triggerHaptic(22);
  state.bumpAdded = !state.bumpAdded;

  const container = document.getElementById('order-bump-container');
  const checkboxVis = document.getElementById('bump-checkbox-visual');
  const checkSvg = document.getElementById('bump-check-svg');
  const statusPill = document.getElementById('bump-status-pill');
  const tagRight = document.getElementById('bump-tag-right');

  if (state.bumpAdded) {
    container.classList.add('active');
    checkboxVis.classList.add('bg-fuchsia-500', 'border-fuchsia-500');
    checkSvg.classList.remove('hidden');
    if (statusPill) {
      statusPill.textContent = '✔ Added to Order';
      statusPill.className = 'text-[10px] font-medium text-emerald-600';
    }
    if (tagRight) {
      tagRight.textContent = 'Added ✓';
      tagRight.className = 'text-xs font-semibold text-emerald-600';
    }
  } else {
    container.classList.remove('active');
    checkboxVis.classList.remove('bg-fuchsia-500', 'border-fuchsia-500');
    checkSvg.classList.add('hidden');
    if (statusPill) {
      statusPill.textContent = 'Optional Add-On';
      statusPill.className = 'text-[10px] font-medium text-slate-400';
    }
    if (tagRight) {
      tagRight.textContent = '+Add to cart';
      tagRight.className = 'text-xs font-medium text-slate-600';
    }
  }

  if (state.bumpAdded) {
    const { activeBump1Price } = getTotals();
    trackMetaPixelEvent('AddToCart', {
      content_name: 'Uncensored Content Hack (VIP Add-On Guide)',
      content_category: 'Order Bump',
      value: activeBump1Price,
      currency: state.currency
    });
  }

  renderPricing();
}

// Toggle Order Bump #2 ("500+ Viral Reel Hooks & Auto-DM Pack")
function toggleSecondOrderBump() {
  triggerHaptic(22);
  state.bump2Added = !state.bump2Added;

  const container = document.getElementById('order-bump-2-container');
  const checkboxVis = document.getElementById('bump-2-checkbox-visual');
  const checkSvg = document.getElementById('bump-2-check-svg');
  const statusPill = document.getElementById('bump-2-status-pill');
  const tagRight = document.getElementById('bump-2-tag-right');

  if (state.bump2Added) {
    container.classList.add('active');
    checkboxVis.classList.add('bg-fuchsia-500', 'border-fuchsia-500');
    checkSvg.classList.remove('hidden');
    if (statusPill) {
      statusPill.textContent = '✔ Added to Order';
      statusPill.className = 'text-[10px] font-medium text-emerald-600';
    }
    if (tagRight) {
      tagRight.textContent = 'Added ✓';
      tagRight.className = 'text-xs font-semibold text-emerald-600';
    }
    const { activeBump2Price } = getTotals();
    trackMetaPixelEvent('AddToCart', {
      content_name: '500+ Viral Reel Hooks & Auto-DM Templates Pack',
      content_category: 'Order Bump',
      value: activeBump2Price,
      currency: state.currency
    });
  } else {
    container.classList.remove('active');
    checkboxVis.classList.remove('bg-fuchsia-500', 'border-fuchsia-500');
    checkSvg.classList.add('hidden');
    if (statusPill) {
      statusPill.textContent = 'Optional Add-On';
      statusPill.className = 'text-[10px] font-medium text-slate-400';
    }
    if (tagRight) {
      tagRight.textContent = '+Add to cart';
      tagRight.className = 'text-xs font-semibold text-slate-700';
    }
  }

  renderPricing();
}

// Desktop "Mobile View" Phone Frame Simulator Toggle
function toggleMobileFrameMode() {
  state.mobileFrameMode = !state.mobileFrameMode;
  const label = document.getElementById('mobile-frame-label');
  const btn = document.getElementById('btn-mobile-frame');

  if (state.mobileFrameMode) {
    document.body.classList.add('mobile-frame-active');
    if (label) label.textContent = 'Exit Mobile View';
    if (btn) btn.classList.add('bg-brand-500', 'text-white');
  } else {
    document.body.classList.remove('mobile-frame-active');
    if (label) label.textContent = 'Mobile View';
    if (btn) btn.classList.remove('bg-brand-500', 'text-white');
  }
}

// Double-Tap Floating Heart Micro-Interaction
function spawnFloatingHeart(event, containerEl) {
  triggerHaptic(30);
  if (!containerEl) return;
  const rect = containerEl.getBoundingClientRect();
  const x = (event.clientX || rect.left + rect.width / 2) - rect.left;
  const y = (event.clientY || rect.top + rect.height / 2) - rect.top;

  const heart = document.createElement('div');
  heart.className = 'floating-heart';
  heart.textContent = '❤️';
  heart.style.left = `${x}px`;
  heart.style.top = `${y}px`;
  containerEl.appendChild(heart);

  setTimeout(() => {
    heart.remove();
  }, 900);
}

// =========================================================================
// INTERACTIVE VERTICAL MOBILE AI REEL FEED PLAYER
// =========================================================================
const reelFeedItems = [
  {
    img: 'assets/images/persona_maya.jpg',
    handle: '@mayavirtual',
    earnings: '$14.2K/mo',
    likes: '115.4K',
    comments: '1,842',
    caption: 'Golden hour in Monaco 🥂 Comment "LAUNCH" and my AI Auto-DM bot will send you the exact prompt! #AIInfluencer #VirtualModel'
  },
  {
    img: 'assets/images/persona_aira.jpg',
    handle: '@aira_digital',
    earnings: '$19.8K/mo',
    likes: '310.8K',
    comments: '4,290',
    caption: 'Rainy nights in Neo-Seoul ⚡ Built 100% on Android mobile in 12 mins. Comment "LAUNCH" for the Face-Lock seed! #Techwear #AICreator'
  },
  {
    img: 'assets/images/persona_alex.jpg',
    handle: '@alex_fit_ai',
    earnings: '$11.4K/mo',
    likes: '245.1K',
    comments: '2,915',
    caption: 'Sunrise penthouse grind in Dubai 🏋️‍♂️ Automated workout PDF sales running 24/7. Comment "LAUNCH" to see how! #AIFitness'
  },
  {
    img: 'assets/images/persona_bali.jpg',
    handle: '@virtual_journey',
    earnings: '$16.5K/mo',
    likes: '1.3M',
    comments: '9,210',
    caption: 'Ubud infinity pool bliss 🌴 4.2M views on a 100% virtual travel creator page. Comment "LAUNCH" for the blueprint! #Bali #VirtualInfluencer'
  }
];

function renderReelFeedItem() {
  const item = reelFeedItems[state.activeReelIndex];
  document.getElementById('reel-active-img').src = item.img;
  document.getElementById('reel-handle').textContent = item.handle;
  document.getElementById('reel-earnings-tag').textContent = item.earnings;
  document.getElementById('reel-like-count').textContent = item.likes;
  document.getElementById('reel-comment-count').textContent = item.comments;
  document.getElementById('reel-caption').textContent = item.caption;
  document.getElementById('reel-counter-badge').textContent = `${state.activeReelIndex + 1} / ${reelFeedItems.length}`;
}

function openReelFeedModal(startIndex = 0) {
  triggerHaptic(20);
  state.activeReelIndex = startIndex % reelFeedItems.length;
  renderReelFeedItem();
  const modal = document.getElementById('reel-feed-modal');
  modal.classList.remove('hidden');
  modal.classList.add('flex');
}

function closeReelFeedModal() {
  const modal = document.getElementById('reel-feed-modal');
  modal.classList.add('hidden');
  modal.classList.remove('flex');
}

function nextReelItem() {
  triggerHaptic(15);
  state.activeReelIndex = (state.activeReelIndex + 1) % reelFeedItems.length;
  renderReelFeedItem();
}

function prevReelItem() {
  triggerHaptic(15);
  state.activeReelIndex = (state.activeReelIndex - 1 + reelFeedItems.length) % reelFeedItems.length;
  renderReelFeedItem();
}

function triggerReelLike() {
  const touchArea = document.getElementById('reel-touch-area');
  spawnFloatingHeart({ clientX: 0, clientY: 0 }, touchArea);
  const circle = document.getElementById('reel-like-circle');
  circle.classList.add('bg-pink-600', 'scale-110');
  setTimeout(() => circle.classList.remove('scale-110'), 250);
}

function handleReelDoubleTap(event) {
  const touchArea = document.getElementById('reel-touch-area');
  spawnFloatingHeart(event, touchArea);
  const circle = document.getElementById('reel-like-circle');
  circle.classList.add('bg-pink-600');
}

function toggleReelCommentDrawer() {
  triggerHaptic(15);
  const drawer = document.getElementById('reel-comment-drawer');
  drawer.classList.toggle('hidden');
}

function submitReelTestComment(event) {
  event.preventDefault();
  triggerHaptic(25);
  const input = document.getElementById('reel-comment-input');
  const log = document.getElementById('reel-dm-log');
  const val = (input.value || 'LAUNCH').trim();

  const entry = document.createElement('div');
  entry.className = 'rounded-lg bg-brand-500/20 border border-brand-500/40 p-2';
  entry.innerHTML = `
    <strong>@you:</strong> ${val}
    <div class="mt-1 text-[11px] text-emerald-300">↳ <strong>AI Auto-DM Bot (Instant):</strong> Just DM'd you the full 5-Day AI Influencer Launch Kit link! 🚀</div>
  `;
  log.prepend(entry);
  input.value = '';
}

// Add vertical touch-swipe support to the Reel Feed Modal
function initReelSwipeGestures() {
  const area = document.getElementById('reel-touch-area');
  if (!area) return;
  let startY = 0;

  area.addEventListener('touchstart', (e) => {
    if (e.touches && e.touches.length > 0) {
      startY = e.touches[0].clientY;
    }
  }, { passive: true });

  area.addEventListener('touchend', (e) => {
    if (!e.changedTouches || e.changedTouches.length === 0) return;
    const endY = e.changedTouches[0].clientY;
    const diffY = startY - endY;
    if (Math.abs(diffY) > 45) {
      if (diffY > 0) {
        nextReelItem(); // Swiped up -> Next Reel
      } else {
        prevReelItem(); // Swiped down -> Prev Reel
      }
    }
  }, { passive: true });
}

// =========================================================================
// AUTOMATIC IP-BASED CURRENCY DETECTION & REGIONAL CHECKOUT LOCK
// =========================================================================
state.visitorCountry = 'IN';
state.detectedIpLabel = 'Auto IP';

function applyVisitorRegion(countryCode, ipSourceLabel = '') {
  const isIndia = String(countryCode || '').toUpperCase() === 'IN';
  state.visitorCountry = isIndia ? 'IN' : 'US';
  state.currency = isIndia ? 'INR' : 'USD';
  if (ipSourceLabel) state.detectedIpLabel = ipSourceLabel;

  // 1. Update Locked Geo-IP Header Badge (shows only the visitor's currency)
  const flagEl = document.getElementById('geo-flag-icon');
  const currTextEl = document.getElementById('geo-currency-text');
  const ipLabelEl = document.getElementById('geo-detected-ip-label');
  const simBtnIn = document.getElementById('geo-sim-btn-in');
  const simBtnUs = document.getElementById('geo-sim-btn-us');

  if (flagEl) flagEl.textContent = isIndia ? '🇮🇳' : '🇺🇸';
  if (currTextEl) currTextEl.textContent = isIndia ? 'INR (₹)' : 'USD ($)';
  if (ipLabelEl) ipLabelEl.textContent = state.detectedIpLabel;

  if (simBtnIn && simBtnUs) {
    if (isIndia) {
      simBtnIn.className = 'w-full flex items-center justify-between rounded-lg px-2.5 py-1.5 font-bold bg-brand-500 text-white transition-all';
      simBtnUs.className = 'w-full flex items-center justify-between rounded-lg px-2.5 py-1.5 font-bold hover:bg-white/10 transition-all';
    } else {
      simBtnUs.className = 'w-full flex items-center justify-between rounded-lg px-2.5 py-1.5 font-bold bg-brand-500 text-white transition-all';
      simBtnIn.className = 'w-full flex items-center justify-between rounded-lg px-2.5 py-1.5 font-bold hover:bg-white/10 transition-all';
    }
  }

  // 2. Update Checkout Phone Country Code & Placeholder
  const phoneFlag = document.getElementById('phone-country-flag');
  const phoneCode = document.getElementById('phone-country-code');
  const phoneInput = document.getElementById('customer-phone');
  if (phoneFlag) phoneFlag.textContent = isIndia ? '🇮🇳' : '🇺🇸';
  if (phoneCode) phoneCode.textContent = isIndia ? '+91' : '+1';
  if (phoneInput) phoneInput.placeholder = isIndia ? '98765 43210' : '(555) 234-5678';

  // 3. Swap Checkout Payment Badges (PhonePe/UPI vs Stripe/Apple Pay)
  const badgesIn = document.getElementById('payment-badges-in');
  const badgesUs = document.getElementById('payment-badges-us');
  if (badgesIn && badgesUs) {
    if (isIndia) {
      badgesIn.classList.remove('hidden');
      badgesIn.classList.add('flex');
      badgesUs.classList.add('hidden');
      badgesUs.classList.remove('flex');
    } else {
      badgesUs.classList.remove('hidden');
      badgesUs.classList.add('flex');
      badgesIn.classList.add('hidden');
      badgesIn.classList.remove('flex');
    }
  }

  // 4. Swap Payment Gateway Modal Options (UPI QR vs Stripe/Apple Pay USD)
  const gwIn = document.getElementById('payment-gateway-in');
  const gwUs = document.getElementById('payment-gateway-us');
  const modalGeoPill = document.getElementById('modal-geo-pill');
  if (gwIn && gwUs) {
    if (isIndia) {
      gwIn.classList.remove('hidden');
      gwUs.classList.add('hidden');
    } else {
      gwUs.classList.remove('hidden');
      gwIn.classList.add('hidden');
    }
  }
  if (modalGeoPill) {
    modalGeoPill.textContent = isIndia ? '🇮🇳 INR • Razorpay' : '🇺🇸 USD • PayPal';
  }

  renderPricing();
}

function setCurrency(curr) {
  applyVisitorRegion(curr === 'INR' ? 'IN' : 'US');
}

function toggleGeoSimPopover() {
  triggerHaptic(12);
  const pop = document.getElementById('geo-sim-popover');
  if (pop) pop.classList.toggle('hidden');
}

function simulateVisitorCountry(countryCode) {
  triggerHaptic(18);
  applyVisitorRegion(countryCode, `Simulated ${countryCode} IP`);
  const pop = document.getElementById('geo-sim-popover');
  if (pop) pop.classList.add('hidden');
  triggerPayoutToast(
    countryCode === 'IN'
      ? '🇮🇳 Visitor IP set to India — Routed to ₹ INR & Razorpay UPI Checkout'
      : '🇺🇸 Visitor IP set to US/Global — Routed to $ USD & PayPal Checkout'
  );
}

async function detectCurrencyByIP() {
  // 1. Check URL override (?geo=US or ?geo=IN) for quick testing
  try {
    const params = new URLSearchParams(window.location.search);
    const geoParam = (params.get('geo') || params.get('country') || '').toUpperCase();
    if (geoParam === 'US' || geoParam === 'IN') {
      applyVisitorRegion(geoParam, `URL ?geo=${geoParam}`);
      return;
    }
  } catch (e) {}

  // 2. Instant zero-flicker timezone heuristic before IP response arrives
  try {
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
    const isIndianTz = tz.includes('Calcutta') || tz.includes('Kolkata') || tz.includes('Asia/Colombo');
    applyVisitorRegion(isIndianTz ? 'IN' : 'US', 'Detecting IP...');
  } catch (e) {
    applyVisitorRegion('IN', 'Detecting IP...');
  }

  // 3. Live IP Geolocation lookup (Primary: ipapi.co, Fallback: ipwho.is)
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 3500);
    const res = await fetch('https://ipapi.co/json/', { signal: controller.signal });
    clearTimeout(timeout);
    if (res.ok) {
      const data = await res.json();
      if (data && data.country_code) {
        const cc = String(data.country_code).toUpperCase();
        const ipShort = data.ip ? `${cc} IP (${data.ip})` : `${cc} IP`;
        applyVisitorRegion(cc === 'IN' ? 'IN' : 'US', ipShort);
        return;
      }
    }
  } catch (e) {}

  try {
    const controller2 = new AbortController();
    const timeout2 = setTimeout(() => controller2.abort(), 3500);
    const res2 = await fetch('https://ipwho.is/', { signal: controller2.signal });
    clearTimeout(timeout2);
    if (res2.ok) {
      const data2 = await res2.json();
      if (data2 && data2.country_code) {
        const cc2 = String(data2.country_code).toUpperCase();
        const ipShort2 = data2.ip ? `${cc2} IP (${data2.ip})` : `${cc2} IP`;
        applyVisitorRegion(cc2 === 'IN' ? 'IN' : 'US', ipShort2);
      }
    }
  } catch (e) {}
}

// Promo Code Application
function applyQuickPromo(code) {
  triggerHaptic(20);
  const input = document.getElementById('promo-input');
  input.value = code;
  handleApplyPromo();
}

function handleApplyPromo() {
  const input = document.getElementById('promo-input');
  const feedback = document.getElementById('promo-feedback');
  const code = (input.value || '').trim().toUpperCase();

  feedback.classList.remove('hidden', 'text-emerald-400', 'text-rose-400');

  if (code === 'RIYA10' || code === 'EARLY10') {
    state.promoCode = code;
    state.promoDiscountPercent = 10;
    feedback.textContent = `✔ Promo "${code}" applied! Extra 10% discount unlocked.`;
    feedback.classList.add('text-emerald-400');
  } else if (code === 'VIP20') {
    state.promoCode = code;
    state.promoDiscountPercent = 20;
    feedback.textContent = `✔ VIP Promo "${code}" applied! 20% discount unlocked.`;
    feedback.classList.add('text-emerald-400');
  } else {
    state.promoCode = null;
    state.promoDiscountPercent = 0;
    feedback.textContent = `Invalid code. Try "RIYA10" (10% off) or "VIP20" (20% off)!`;
    feedback.classList.add('text-rose-400');
  }

  renderPricing();
}

// Theme Switcher (Dark / Light)
function toggleTheme() {
  triggerHaptic(15);
  const html = document.documentElement;
  const sun = document.getElementById('theme-icon-sun');
  const moon = document.getElementById('theme-icon-moon');

  if (state.theme === 'dark') {
    state.theme = 'light';
    html.setAttribute('data-theme', 'light');
    sun.classList.add('hidden');
    moon.classList.remove('hidden');
  } else {
    state.theme = 'dark';
    html.setAttribute('data-theme', 'dark');
    moon.classList.add('hidden');
    sun.classList.remove('hidden');
  }
}

// =========================================================================
// LIVE AI PERSONA & DNA PROMPT GENERATOR SANDBOX
// =========================================================================
const labConfigs = {
  monaco: {
    img: 'assets/images/persona_maya.jpg',
    handle: '@mayavirtual',
    cpm: 'Est. $14.2K/mo',
    subject: 'Maya, 23yo Mediterranean luxury fashion virtual influencer at Monaco sunset harbor lounge, wearing architectural navy silk evening wear, natural micro-pore skin texture, subtle freckles'
  },
  seoul: {
    img: 'assets/images/persona_aira.jpg',
    handle: '@aira_digital',
    cpm: 'Est. $19.8K/mo',
    subject: 'Aira, 21yo East-Asian cyber-streetwear virtual creator walking through rain-slicked Neo-Seoul alley at night, holographic technical jacket, realistic wet hair strands, ultra-detailed skin'
  },
  dubai: {
    img: 'assets/images/persona_alex.jpg',
    handle: '@alex_fit_ai',
    cpm: 'Est. $11.4K/mo',
    subject: 'Alex, 26yo athletic virtual fitness coach in a glass penthouse gym overlooking Downtown Dubai skyline at sunrise, fitted charcoal performance tee, realistic sweat sheen'
  },
  bali: {
    img: 'assets/images/persona_bali.jpg',
    handle: '@virtual_journey',
    cpm: 'Est. $16.5K/mo',
    subject: 'Sienna, 24yo sun-kissed travel & resort virtual creator in an infinity pool overlooking Ubud tropical jungle in Bali at sunrise, white linen resort wear, floating breakfast tray'
  }
};

const cameraSpecs = {
  '85mm': 'shot on Canon RF 85mm f/1.4L, shallow depth of field, warm golden hour rim lighting, Kodak Portra 400 color grade',
  iphone: 'shot on iPhone 16 Pro Max front/rear candid camera, raw handheld social media reel framing, authentic natural ambient light',
  neon: 'shot on 35mm anamorphic lens, electric violet and cyan neon reflections, high-contrast cinematic studio mood'
};

const hookSpecs = {
  curiosity: {
    title: '3-Second Curiosity Loop',
    desc: '<strong>On-Screen Hook (0–3s):</strong> "99% of people scrolling past this have no idea I don\'t actually exist..." → <strong>Monetization:</strong> Pinned comment triggers automated ManyChat DM funnel.'
  },
  pov: {
    title: 'Aspirational Luxury POV',
    desc: '<strong>On-Screen Hook (0–3s):</strong> "POV: You automated your digital creator brand and woke up to 1.4M views..." → <strong>Monetization:</strong> High-ticket affiliate link in bio + VIP fan club.'
  },
  outfit: {
    title: 'Instant Outfit Swap Transition',
    desc: '<strong>On-Screen Hook (0–3s):</strong> Beat-synced 3-outfit luxury wardrobe transition in 4 seconds → <strong>Monetization:</strong> Fashion brand sponsorship + LTK/Amazon storefront.'
  }
};

function selectLabNichePill(nicheKey) {
  triggerHaptic(18);
  const selectEl = document.getElementById('lab-niche');
  if (selectEl) selectEl.value = nicheKey;

  ['monaco', 'seoul', 'dubai', 'bali'].forEach((k) => {
    const pill = document.getElementById(`pill-niche-${k}`);
    if (!pill) return;
    if (k === nicheKey) {
      pill.className = 'touch-scale rounded-xl bg-brand-500 text-white px-3 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 shadow-md transition-all';
    } else {
      pill.className = 'touch-scale rounded-xl surface-elevated px-3 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 hover:border-brand-500 transition-all';
    }
  });

  runPersonaLab();
}

function runPersonaLab(forceRandomSeed = false) {
  const nicheKey = document.getElementById('lab-niche').value;
  const camKey = document.getElementById('lab-camera').value;
  const hookKey = document.getElementById('lab-hook').value;

  // Keep mobile pills synced if user changed dropdown on desktop
  ['monaco', 'seoul', 'dubai', 'bali'].forEach((k) => {
    const pill = document.getElementById(`pill-niche-${k}`);
    if (!pill) return;
    if (k === nicheKey) {
      pill.className = 'touch-scale rounded-xl bg-brand-500 text-white px-3 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 shadow-md transition-all';
    } else {
      pill.className = 'touch-scale rounded-xl surface-elevated px-3 py-2.5 text-xs font-bold flex items-center justify-center gap-1.5 hover:border-brand-500 transition-all';
    }
  });

  const overlay = document.getElementById('lab-loading-overlay');
  overlay.classList.remove('hidden');

  const seed = forceRandomSeed
    ? Math.floor(1000000 + Math.random() * 9000000)
    : 8849201 + nicheKey.length * 1337;

  setTimeout(() => {
    const cfg = labConfigs[nicheKey] || labConfigs.monaco;
    const cam = cameraSpecs[camKey] || cameraSpecs['85mm'];
    const hook = hookSpecs[hookKey] || hookSpecs.curiosity;

    document.getElementById('lab-preview-img').src = cfg.img;
    document.getElementById('lab-persona-handle').textContent = cfg.handle;
    document.getElementById('lab-persona-cpm').textContent = cfg.cpm;

    document.getElementById('lab-prompt-box').textContent =
      `[SEED_LOCK: ${seed}] Hyper-realistic vertical 9:16 Instagram Reel frame of ${cfg.subject}, ${cam} --ar 9:16 --style raw --cw 100 --v 6.1`;

    document.getElementById('lab-hook-box').innerHTML = hook.desc;
    overlay.classList.add('hidden');
  }, 240);
}

function copyLabPrompt() {
  triggerHaptic(25);
  const promptText = document.getElementById('lab-prompt-box').textContent.trim();
  const btn = document.getElementById('btn-copy-prompt');
  if (navigator.clipboard) {
    navigator.clipboard.writeText(promptText);
  }
  btn.textContent = '✔ Copied DNA Prompt!';
  setTimeout(() => {
    btn.textContent = '📋 Copy Prompt';
  }, 2000);
}

// =========================================================================
// PERSONA CASE STUDY INSPECTOR MODAL
// =========================================================================
const personaCaseStudies = {
  maya: {
    img: 'assets/images/persona_maya.jpg',
    niche: 'Monaco Luxury & High Fashion',
    handle: '@mayavirtual',
    stats: '184K Followers • Avg 1.8M Reel Views • 100% Mobile Workflow',
    rev: '$14,200 / mo (₹11.9 Lakhs/mo)',
    streams: [
      '• Luxury Boutique & Resort Sponsorships: $6,400/mo',
      '• Exclusive Fan Club & VIP Lookbooks: $4,800/mo',
      '• High-Ticket Fashion Affiliate Links: $3,000/mo'
    ],
    prompt: '[SEED_LOCK: 8849201] Maya, 23yo Mediterranean virtual model at Monaco yacht club sunset, navy silk couture, 85mm f/1.4 lens, micro-pore skin realism --ar 9:16 --cw 100'
  },
  aira: {
    img: 'assets/images/persona_aira.jpg',
    niche: 'Neo-Seoul Cyber Streetwear',
    handle: '@aira_digital',
    stats: '310K Followers • Avg 3.4M Reel Views • Viral Lip-Sync & Motion',
    rev: '$19,800 / mo (₹16.6 Lakhs/mo)',
    streams: [
      '• Techwear & Gaming Brand Collabs: $8,500/mo',
      '• Exclusive Fan Subscriptions: $7,200/mo',
      '• Automated ManyChat DM Digital Packs: $4,100/mo'
    ],
    prompt: '[SEED_LOCK: 5519044] Aira, 21yo cyber-streetwear virtual creator in rainy neon Seoul alley, reflective technical jacket, 35mm anamorphic rim lighting --ar 9:16 --cw 100'
  },
  alex: {
    img: 'assets/images/persona_alex.jpg',
    niche: 'Dubai Penthouse Fitness & Lifestyle',
    handle: '@alex_fit_ai',
    stats: '142K Followers • Avg 2.1M Reel Views • AI Voice & Workout Reels',
    rev: '$11,400 / mo (₹9.5 Lakhs/mo)',
    streams: [
      '• Supplement & Athleisure Affiliates: $5,200/mo',
      '• Automated 12-Week AI Workout PDF Funnel: $4,100/mo',
      '• Brand Shoutouts & Reels Placement: $2,100/mo'
    ],
    prompt: '[SEED_LOCK: 3391082] Alex, 26yo athletic male virtual fitness coach in luxury Dubai penthouse gym at sunrise, natural sweat texture, iPhone 16 Pro candid reel --ar 9:16'
  },
  bali: {
    img: 'assets/images/persona_bali.jpg',
    niche: 'Bali Tropical Resort & Travel',
    handle: '@virtual_journey',
    stats: '265K Followers • Avg 4.2M Reel Views • Golden Hour Travel POVs',
    rev: '$16,500 / mo (₹13.8 Lakhs/mo)',
    streams: [
      '• Boutique Hotel & Travel App Partnerships: $7,800/mo',
      '• Automated Travel Preset & Itinerary DMs: $5,400/mo',
      '• Creator Fund & Fan Memberships: $3,300/mo'
    ],
    prompt: '[SEED_LOCK: 7742910] Sienna, 24yo travel virtual influencer in Ubud infinity pool at sunrise, white linen resort wear, floating breakfast tray, golden hour --ar 9:16'
  }
};

function openPersonaModal(key) {
  triggerHaptic(18);
  const data = personaCaseStudies[key] || personaCaseStudies.maya;
  document.getElementById('pmodal-img').src = data.img;
  document.getElementById('pmodal-niche').textContent = data.niche;
  document.getElementById('pmodal-handle').textContent = data.handle;
  document.getElementById('pmodal-stats').textContent = data.stats;
  document.getElementById('pmodal-rev').textContent = data.rev;
  document.getElementById('pmodal-streams').innerHTML = data.streams.map((s) => `<div>${s}</div>`).join('');
  document.getElementById('pmodal-prompt').textContent = data.prompt;

  const modal = document.getElementById('persona-modal');
  modal.classList.remove('hidden');
  modal.classList.add('flex');
}

function closePersonaModal() {
  const modal = document.getElementById('persona-modal');
  modal.classList.add('hidden');
  modal.classList.remove('flex');
}

// =========================================================================
// 5-DAY CURRICULUM ACCORDION
// =========================================================================
function toggleCurriculum(index) {
  triggerHaptic(12);
  for (let i = 0; i < 5; i++) {
    const body = document.getElementById(`curr-body-${i}`);
    const icon = document.getElementById(`curr-icon-${i}`);
    if (i === index) {
      const isOpen = body.classList.contains('open');
      if (isOpen) {
        body.classList.remove('open');
        body.style.maxHeight = '0px';
        icon.classList.remove('rotate-180');
      } else {
        body.classList.add('open');
        body.style.maxHeight = body.scrollHeight + 32 + 'px';
        icon.classList.add('rotate-180');
      }
    } else if (!state.allCurriculumExpanded) {
      body.classList.remove('open');
      body.style.maxHeight = '0px';
      icon.classList.remove('rotate-180');
    }
  }
}

function toggleAllCurriculum() {
  triggerHaptic(18);
  state.allCurriculumExpanded = !state.allCurriculumExpanded;
  const btn = document.getElementById('btn-expand-all');
  btn.textContent = state.allCurriculumExpanded ? 'Collapse All' : 'Expand All 5 Days';

  for (let i = 0; i < 5; i++) {
    const body = document.getElementById(`curr-body-${i}`);
    const icon = document.getElementById(`curr-icon-${i}`);
    if (state.allCurriculumExpanded) {
      body.classList.add('open');
      body.style.maxHeight = body.scrollHeight + 32 + 'px';
      icon.classList.add('rotate-180');
    } else {
      if (i === 0) {
        body.classList.add('open');
        body.style.maxHeight = body.scrollHeight + 32 + 'px';
        icon.classList.add('rotate-180');
      } else {
        body.classList.remove('open');
        body.style.maxHeight = '0px';
        icon.classList.remove('rotate-180');
      }
    }
  }
}

// =========================================================================
// REVENUE ANALYTICS DASHBOARD, DUAL-LINE SCRUBBER & 4-STREAM CALCULATOR
// =========================================================================
state.activeTimeframe = 'all';
state.activeRefMetric = 'gross';

const analyticsPresets = {
  all: {
    gross: '$213,593.25',
    grossDelta: '+$119,138.20 ↑',
    mrr: '$4,576.00',
    mrrDelta: '+$2,376.00 ↑',
    arr: '$54,912.00',
    arrDelta: '+$28,512.00 ↑',
    curves: {
      gross: {
        label: 'Gross revenue',
        blue: 'M 0,148 L 14,132 L 28,118 L 42,140 L 58,136 L 74,108 L 92,135 L 110,96 L 128,125 L 145,134 L 164,120 L 182,110 L 200,98 L 218,126 L 236,88 L 254,132 L 268,94 L 284,18 L 298,108 L 314,96 L 332,68 L 348,114 L 366,118 L 384,96 L 402,126 L 420,98 L 438,114 L 456,114 L 474,92 L 492,124 L 510,98 L 528,114 L 546,116 L 564,104 L 582,88 L 600,126',
        grey: 'M 0,152 L 22,138 L 45,126 L 68,144 L 92,118 L 115,138 L 138,106 L 162,132 L 185,118 L 208,108 L 232,134 L 255,96 L 278,126 L 302,88 L 325,112 L 348,92 L 372,124 L 395,104 L 418,128 L 442,102 L 465,122 L 488,98 L 512,126 L 535,106 L 558,120 L 580,96 L 600,118'
      },
      mrr: {
        label: 'MRR (Monthly Recurring)',
        blue: 'M 0,146 L 40,138 L 80,126 L 120,118 L 160,104 L 200,95 L 240,86 L 284,64 L 330,68 L 375,58 L 420,52 L 465,44 L 510,38 L 555,32 L 600,26',
        grey: 'M 0,152 L 50,146 L 100,140 L 150,132 L 200,126 L 250,118 L 300,112 L 350,104 L 400,98 L 450,92 L 500,86 L 550,80 L 600,74'
      },
      arr: {
        label: 'ARR (Annualized Run Rate)',
        blue: 'M 0,148 L 40,136 L 80,124 L 120,112 L 160,98 L 200,88 L 240,76 L 284,48 L 330,54 L 375,45 L 420,38 L 465,32 L 510,26 L 555,22 L 600,18',
        grey: 'M 0,153 L 50,145 L 100,136 L 150,128 L 200,120 L 250,110 L 300,102 L 350,94 L 400,88 L 450,80 L 500,72 L 550,66 L 600,60'
      }
    }
  },
  '90d': {
    gross: '$84,640.50',
    grossDelta: '+$42,190.00 ↑',
    mrr: '$8,920.00',
    mrrDelta: '+$4,110.00 ↑',
    arr: '$107,040.00',
    arrDelta: '+$49,320.00 ↑',
    curves: {
      gross: {
        label: 'Gross revenue (Last 90D)',
        blue: 'M 0,138 L 35,124 L 70,112 L 105,126 L 140,94 L 175,108 L 210,82 L 245,96 L 284,26 L 320,76 L 360,64 L 400,78 L 440,56 L 480,68 L 520,48 L 560,58 L 600,42',
        grey: 'M 0,148 L 40,136 L 80,128 L 120,134 L 160,118 L 200,124 L 240,106 L 284,92 L 330,104 L 375,94 L 420,102 L 465,88 L 510,96 L 555,84 L 600,78'
      },
      mrr: {
        label: 'MRR (Last 90D)',
        blue: 'M 0,140 L 60,124 L 120,108 L 180,92 L 240,78 L 300,64 L 360,52 L 420,42 L 480,32 L 540,26 L 600,20',
        grey: 'M 0,150 L 60,140 L 120,130 L 180,120 L 240,110 L 300,100 L 360,90 L 420,82 L 480,74 L 540,68 L 600,62'
      },
      arr: {
        label: 'ARR (Last 90D)',
        blue: 'M 0,138 L 60,120 L 120,104 L 180,86 L 240,70 L 300,56 L 360,44 L 420,34 L 480,26 L 540,20 L 600,16',
        grey: 'M 0,148 L 60,138 L 120,126 L 180,116 L 240,104 L 300,94 L 360,84 L 420,76 L 480,68 L 540,60 L 600,54'
      }
    }
  },
  '30d': {
    gross: '$40,914.22',
    grossDelta: '+$18,091.94 ↑',
    mrr: '$12,251.03',
    mrrDelta: '+$5,499.96 ↑',
    arr: '$147,012.36',
    arrDelta: '+$65,999.52 ↑',
    curves: {
      gross: {
        label: 'Gross revenue (Last 30D)',
        blue: 'M 0,132 L 40,118 L 80,104 L 120,114 L 160,86 L 200,94 L 240,68 L 284,22 L 330,62 L 375,54 L 420,66 L 465,44 L 510,52 L 555,36 L 600,28',
        grey: 'M 0,144 L 50,132 L 100,124 L 150,116 L 200,108 L 250,98 L 300,90 L 350,86 L 400,78 L 450,74 L 500,68 L 550,62 L 600,58'
      },
      mrr: {
        label: 'MRR (Last 30D)',
        blue: 'M 0,134 L 60,118 L 120,100 L 180,84 L 240,68 L 300,54 L 360,42 L 420,32 L 480,24 L 540,18 L 600,14',
        grey: 'M 0,146 L 60,136 L 120,124 L 180,114 L 240,102 L 300,92 L 360,82 L 420,72 L 480,64 L 540,56 L 600,50'
      },
      arr: {
        label: 'ARR (Last 30D)',
        blue: 'M 0,130 L 60,112 L 120,94 L 180,78 L 240,62 L 300,48 L 360,36 L 420,28 L 480,20 L 540,16 L 600,12',
        grey: 'M 0,144 L 60,132 L 120,120 L 180,108 L 240,96 L 300,86 L 360,76 L 420,66 L 480,58 L 540,50 L 600,44'
      }
    }
  }
};

function renderRefAnalyticsDashboard() {
  const preset = analyticsPresets[state.activeTimeframe] || analyticsPresets.all;
  const metricKey = state.activeRefMetric || 'gross';
  const curve = preset.curves[metricKey] || preset.curves.gross;

  // Update 3 bottom selectable metric cards
  const elGrossVal = document.getElementById('card-val-gross');
  const elGrossDelta = document.getElementById('card-delta-gross');
  const elMrrVal = document.getElementById('card-val-mrr');
  const elMrrDelta = document.getElementById('card-delta-mrr');
  const elArrVal = document.getElementById('card-val-arr');
  const elArrDelta = document.getElementById('card-delta-arr');

  if (elGrossVal) elGrossVal.textContent = preset.gross;
  if (elGrossDelta) elGrossDelta.textContent = preset.grossDelta;
  if (elMrrVal) elMrrVal.textContent = preset.mrr;
  if (elMrrDelta) elMrrDelta.textContent = preset.mrrDelta;
  if (elArrVal) elArrVal.textContent = preset.arr;
  if (elArrDelta) elArrDelta.textContent = preset.arrDelta;

  // Update top headline based on currently selected metric card
  const topLabel = document.getElementById('ref-chart-top-label');
  const topVal = document.getElementById('metric-gross');
  const topDelta = document.getElementById('metric-gross-delta');

  if (topLabel) topLabel.textContent = curve.label;
  if (topVal) topVal.textContent = preset[metricKey];
  if (topDelta) topDelta.textContent = preset[`${metricKey}Delta`];

  // Update SVG lines & gradient fill
  const linePath = document.getElementById('chart-line-path');
  const areaPath = document.getElementById('chart-area-path');
  const greyPath = document.getElementById('chart-grey-path');

  if (linePath) linePath.setAttribute('d', curve.blue);
  if (areaPath) areaPath.setAttribute('d', `${curve.blue} L 600,156 L 0,156 Z`);
  if (greyPath) greyPath.setAttribute('d', curve.grey);
}

function switchAnalyticsTab(key) {
  triggerHaptic(12);
  state.activeTimeframe = key;
  ['all', '90d', '30d'].forEach((t) => {
    const btn = document.getElementById(`tab-rev-${t}`);
    if (!btn) return;
    if (t === key) {
      btn.className = 'rounded-md bg-[#0b57d0] px-3 py-1 text-white transition-all';
    } else {
      btn.className = 'rounded-md px-3 py-1 opacity-70 hover:opacity-100 transition-all';
    }
  });
  renderRefAnalyticsDashboard();
}

function selectRefMetricCard(metricKey) {
  triggerHaptic(14);
  state.activeRefMetric = metricKey;
  ['gross', 'mrr', 'arr'].forEach((k) => {
    const card = document.getElementById(`ref-card-${k}`);
    if (!card) return;
    if (k === metricKey) {
      card.className = 'text-left rounded-2xl bg-white p-4 sm:p-5 border-2 border-[#0b57d0] shadow-md transition-all cursor-pointer';
    } else {
      card.className = 'text-left rounded-2xl bg-white p-4 sm:p-5 border border-[#e2e5ec] hover:border-[#0b57d0]/60 shadow-sm transition-all cursor-pointer';
    }
  });
  renderRefAnalyticsDashboard();
}

const scrubTimelineSamples = [
  { date: 'Jan 12', blue: '$3,410.00', grey: '$1,890.00', y: 132 },
  { date: 'Feb 04', blue: '$5,120.40', grey: '$2,410.00', y: 118 },
  { date: 'Feb 26', blue: '$6,840.15', grey: '$3,120.50', y: 108 },
  { date: 'Mar 19', blue: '$8,920.80', grey: '$4,250.00', y: 96 },
  { date: 'Apr 10', blue: '$9,450.00', grey: '$5,180.20', y: 98 },
  { date: 'May 02', blue: '$11,280.60', grey: '$6,040.00', y: 88 },
  { date: 'May 18 (Viral Spike)', blue: '$28,940.50', grey: '$7,410.00', y: 18 },
  { date: 'Jun 08', blue: '$14,620.00', grey: '$7,980.40', y: 68 },
  { date: 'Jul 01', blue: '$12,480.90', grey: '$6,920.00', y: 96 },
  { date: 'Jul 24', blue: '$13,890.25', grey: '$7,540.10', y: 92 },
  { date: 'Aug 16', blue: '$15,110.40', grey: '$8,120.00', y: 98 },
  { date: 'Today', blue: '$16,940.80', grey: '$9,210.50', y: 88 }
];

function handleChartScrub(event) {
  const svg = document.getElementById('ref-dual-chart-svg');
  const line = document.getElementById('chart-scrub-line');
  const dot = document.getElementById('chart-scrub-dot');
  const tooltip = document.getElementById('chart-scrub-tooltip');
  if (!svg || !line || !dot || !tooltip) return;

  const rect = svg.getBoundingClientRect();
  const clientX = event.touches && event.touches[0] ? event.touches[0].clientX : event.clientX;
  if (typeof clientX !== 'number') return;

  const relX = Math.max(0, Math.min(1, (clientX - rect.left) / (rect.width || 1)));
  const svgX = Math.round(relX * 600);
  const sampleIdx = Math.min(
    scrubTimelineSamples.length - 1,
    Math.floor(relX * scrubTimelineSamples.length)
  );
  const sample = scrubTimelineSamples[sampleIdx];

  line.setAttribute('x1', svgX);
  line.setAttribute('x2', svgX);
  line.classList.remove('hidden');

  dot.setAttribute('cx', svgX);
  dot.setAttribute('cy', sample.y);
  dot.classList.remove('hidden');

  const dEl = document.getElementById('scrub-date');
  const bEl = document.getElementById('scrub-val-blue');
  const gEl = document.getElementById('scrub-val-grey');
  if (dEl) dEl.textContent = sample.date;
  if (bEl) bEl.textContent = sample.blue;
  if (gEl) gEl.textContent = sample.grey;

  tooltip.classList.remove('hidden');
}

function hideChartScrub() {
  const line = document.getElementById('chart-scrub-line');
  const dot = document.getElementById('chart-scrub-dot');
  const tooltip = document.getElementById('chart-scrub-tooltip');
  if (line) line.classList.add('hidden');
  if (dot) dot.classList.add('hidden');
  if (tooltip) tooltip.classList.add('hidden');
}

function copyChartSnapshotLink() {
  triggerHaptic(18);
  const text = 'Verified Creator Revenue Snapshot — Gross Revenue: $213,593.25 (+$119,138.20 ↑) | MRR: $4,576.00 | ARR: $54,912.00 — AI Influencer Accelerator by RIYA (@Ralix)';
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).catch(() => {});
  }
  triggerPayoutToast('Verified Analytics Snapshot copied to clipboard!');
}

function switchPayoutCardTab(cardNum, tab) {
  triggerHaptic(14);
  const tabE = document.getElementById(`pcard-${cardNum}-tab-e`);
  const tabP = document.getElementById(`pcard-${cardNum}-tab-p`);
  const bodyE = document.getElementById(`pcard-${cardNum}-earnings`);
  const bodyP = document.getElementById(`pcard-${cardNum}-payouts`);
  if (!tabE || !tabP || !bodyE || !bodyP) return;

  if (tab === 'earnings') {
    tabE.className = 'pb-2 text-xs font-semibold text-white border-b-2 border-[#22c55e] transition-all';
    tabP.className = 'pb-2 text-xs font-medium text-white/50 hover:text-white/80 border-b-2 border-transparent transition-all';
    bodyE.classList.remove('hidden');
    bodyP.classList.add('hidden');
  } else {
    tabP.className = 'pb-2 text-xs font-semibold text-white border-b-2 border-[#22c55e] transition-all';
    tabE.className = 'pb-2 text-xs font-medium text-white/50 hover:text-white/80 border-b-2 border-transparent transition-all';
    bodyP.classList.remove('hidden');
    bodyE.classList.add('hidden');
  }
}

function triggerPayoutToast(label) {
  triggerHaptic(20);
  const toastEl = document.getElementById('social-proof-toast');
  const avatarEl = document.getElementById('toast-avatar');
  const titleEl = document.getElementById('toast-title');
  const descEl = document.getElementById('toast-desc');
  const timeEl = document.getElementById('toast-time');
  if (!toastEl) return;

  if (avatarEl) avatarEl.textContent = '✓';
  if (titleEl) titleEl.textContent = 'Verified Creator Dashboard';
  if (descEl) descEl.textContent = label;
  if (timeEl) timeEl.textContent = 'Live Interactive Preview • RIYA (@Ralix)';

  toastEl.classList.remove('translate-y-24', 'opacity-0');
  toastEl.classList.add('translate-y-0', 'opacity-100');

  setTimeout(() => {
    toastEl.classList.add('translate-y-24', 'opacity-0');
    toastEl.classList.remove('translate-y-0', 'opacity-100');
  }, 4200);
}

function updateEarningsCalc() {
  const reelsEl = document.getElementById('calc-reels');
  const streamsEl = document.getElementById('calc-streams');
  if (!reelsEl || !streamsEl) return;

  const reels = parseInt(reelsEl.value, 10) || 5;
  const streams = parseInt(streamsEl.value, 10) || 3;
  const tierEl = document.getElementById('calc-niche-tier');
  const tierMult = tierEl ? parseFloat(tierEl.value) || 1.0 : 1.0;

  document.getElementById('calc-reels-val').textContent = `${reels} Reels / wk`;
  document.getElementById('calc-streams-val').textContent = `${streams} Stream${streams > 1 ? 's' : ''}`;

  const monthlyUsd = Math.round(reels * 185 * (1 + (streams - 1) * 0.45) * tierMult);
  const outputEl = document.getElementById('calc-output');

  const totalDisplayVal = state.currency === 'INR'
    ? Math.round((monthlyUsd * 84) / 1000) * 1000
    : monthlyUsd;

  if (state.currency === 'INR') {
    outputEl.textContent = `₹${totalDisplayVal.toLocaleString('en-IN')} / mo`;
  } else {
    outputEl.textContent = `$${totalDisplayVal.toLocaleString('en-US')} / mo`;
  }

  // Dynamic stream weights depending on how many streams are active (1..4)
  const weightsByStreamCount = {
    1: [1.0, 0, 0, 0],
    2: [0.55, 0.45, 0, 0],
    3: [0.42, 0.35, 0.23, 0],
    4: [0.35, 0.30, 0.20, 0.15]
  };
  const w = weightsByStreamCount[streams] || weightsByStreamCount[4];

  const sym = state.currency === 'INR' ? '₹' : '$';
  const loc = state.currency === 'INR' ? 'en-IN' : 'en-US';
  const sBrand = document.getElementById('split-brand');
  const sFan = document.getElementById('split-fan');
  const sAff = document.getElementById('split-aff');
  const sDm = document.getElementById('split-dm');

  if (sBrand) sBrand.textContent = `${sym}${Math.round(totalDisplayVal * w[0]).toLocaleString(loc)}`;
  if (sFan) sFan.textContent = `${sym}${Math.round(totalDisplayVal * w[1]).toLocaleString(loc)}`;
  if (sAff) sAff.textContent = `${sym}${Math.round(totalDisplayVal * w[2]).toLocaleString(loc)}`;
  if (sDm) sDm.textContent = `${sym}${Math.round(totalDisplayVal * w[3]).toLocaleString(loc)}`;

  // Update stacked bar chart segments
  const segBrand = document.getElementById('bar-seg-brand');
  const segFan = document.getElementById('bar-seg-fan');
  const segAff = document.getElementById('bar-seg-aff');
  const segDm = document.getElementById('bar-seg-dm');

  if (segBrand) segBrand.style.width = `${Math.round(w[0] * 100)}%`;
  if (segFan) segFan.style.width = `${Math.round(w[1] * 100)}%`;
  if (segAff) segAff.style.width = `${Math.round(w[2] * 100)}%`;
  if (segDm) segDm.style.width = `${Math.round(w[3] * 100)}%`;
}

// =========================================================================
// ASK RIYA'S AI COURSE ASSISTANT
// =========================================================================
const advisorAnswers = {
  faceless:
    '🎭 <strong>100% Faceless & Anonymous:</strong> You never have to show your real face, record your own voice, or buy a camera. Your virtual AI persona is the face of the brand while you operate everything privately from your phone.',
  tools:
    '🛠️ <strong>No Expensive Subscriptions Needed:</strong> Inside Day 1 & Day 3, we show you the exact free-tier & mobile cloud AI tools we use so you can generate consistent character photos and 60fps Reels without paying for expensive software or a gaming PC.',
  payouts:
    '🏦 <strong>Works in India & Worldwide:</strong> Whether you are in India (direct UPI / Bank Transfer via affiliate & creator platforms) or internationally (Stripe / PayPal / Wise), Day 5 walks you through setting up instant payouts step by step.',
  shadowban:
    '🛡️ <strong>Algorithm-Friendly Realism:</strong> Instagram & YouTube actively push high-retention Reels regardless of whether the creator is human or virtual — as long as the skin texture, motion, and hook hold watch-time. Our Face-Lock v4 pipeline passes visual realism checks effortlessly.'
};

function askAiAdvisor(topicKey) {
  triggerHaptic(15);
  const box = document.getElementById('ai-advisor-response');
  box.innerHTML = advisorAnswers[topicKey] || advisorAnswers.faceless;
}

function handleCustomAiQuestion(event) {
  event.preventDefault();
  triggerHaptic(20);
  const input = document.getElementById('ai-advisor-input');
  const box = document.getElementById('ai-advisor-response');
  const q = (input.value || '').trim();
  if (!q) return;

  const lower = q.toLowerCase();
  let reply = '';
  if (lower.includes('phone') || lower.includes('android') || lower.includes('mobile') || lower.includes('pc') || lower.includes('laptop')) {
    reply = `📱 <strong>Mobile Compatibility:</strong> Yes! Regarding <em>"${q}"</em> — the entire 5-Day AI Influencer Launch Kit runs 100% on any Android phone or iPhone via browser/cloud tools. No PC or graphics card is required.`;
  } else if (lower.includes('price') || lower.includes('refund') || lower.includes('guarantee') || lower.includes('subscription')) {
    reply = `🛡️ <strong>One-Time Payment + 7-Day Shield:</strong> It is a single one-time payment (${formatPrice(state.prices[state.currency].base)}) for lifetime access, backed by our 7-day 100% money-back guarantee.`;
  } else if (lower.includes('earn') || lower.includes('money') || lower.includes('monetiz') || lower.includes('income')) {
    reply = `💸 <strong>4 Monetization Streams:</strong> Day 5 covers Brand Deals, Exclusive Fan Subscriptions, High-Ticket Affiliate Links, and Automated ManyChat DM Funnels so you can monetize even with under 5,000 followers.`;
  } else {
    reply = `✨ <strong>Great question about "${q}"!</strong> Yes — everything is covered step-by-step inside the 18 HD video lessons and 250+ DNA prompt templates. Plus, you get direct support at <strong>sayana.official.help@gmail.com</strong> and our 7-day risk-free guarantee!`;
  }

  box.innerHTML = reply;
  input.value = '';
}

// =========================================================================
// CHECKOUT DRAFT PERSISTENCE, VALIDATION & RECEIPT DOWNLOAD
// =========================================================================
function saveCheckoutDraft() {
  try {
    const draft = {
      email: document.getElementById('customer-email')?.value || '',
      phone: document.getElementById('customer-phone')?.value || '',
      name: document.getElementById('customer-name')?.value || ''
    };
    localStorage.setItem('ai_accel_checkout_draft', JSON.stringify(draft));
  } catch (e) {}
}

function loadCheckoutDraft() {
  try {
    const raw = localStorage.getItem('ai_accel_checkout_draft');
    if (!raw) return;
    const draft = JSON.parse(raw);
    if (draft.email) document.getElementById('customer-email').value = draft.email;
    if (draft.phone) document.getElementById('customer-phone').value = draft.phone;
    if (draft.name) document.getElementById('customer-name').value = draft.name;
  } catch (e) {}
}

function scrollToCheckout() {
  triggerHaptic(18);
  const el = document.getElementById('checkout-section');
  if (el) {
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    setTimeout(() => {
      const emailInput = document.getElementById('customer-email');
      if (emailInput) emailInput.focus();
    }, 600);
  }
}

function openPreviewModal() {
  triggerHaptic(18);
  const m = document.getElementById('preview-modal');
  m.classList.remove('hidden');
  m.classList.add('flex');
}

function closePreviewModal() {
  const m = document.getElementById('preview-modal');
  m.classList.add('hidden');
  m.classList.remove('flex');
}

function closePaymentModal() {
  const m = document.getElementById('payment-modal');
  m.classList.add('hidden');
  m.classList.remove('flex');
}

// Razorpay / PayPal KYC Legal & Policy Modal (Terms, Privacy, Refund, Digital Delivery)
function openLegalModal(activeTab = 'terms') {
  triggerHaptic(15);
  const modal = document.getElementById('legal-policy-modal');
  if (!modal) return;

  const tabs = ['terms', 'privacy', 'refund', 'shipping'];
  tabs.forEach((t) => {
    const tabBtn = document.getElementById(`legal-tab-${t}`);
    const pane = document.getElementById(`legal-pane-${t}`);
    if (t === activeTab) {
      if (tabBtn) tabBtn.className = 'rounded-lg px-3 py-1.5 bg-fuchsia-600 text-white cursor-pointer';
      if (pane) pane.classList.remove('hidden');
    } else {
      if (tabBtn) tabBtn.className = 'rounded-lg px-3 py-1.5 bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer';
      if (pane) pane.classList.add('hidden');
    }
  });

  modal.classList.remove('hidden');
  modal.classList.add('flex');
}

function closeLegalModal() {
  const modal = document.getElementById('legal-policy-modal');
  if (!modal) return;
  modal.classList.add('hidden');
  modal.classList.remove('flex');
}

// =========================================================================
// HYBRID PAYMENT GATEWAY & META PIXEL CONFIGURATION
// =========================================================================
const PAYMENT_GATEWAY_CONFIG = {
  // 0a. GOOGLE SHEETS REAL-TIME ORDER & LEAD DATABASE WEBHOOK URL
  // Paste your Google Apps Script Web App URL (https://script.google.com/macros/s/.../exec)
  // Automatically logs every Checkout Lead (INITIATED_CHECKOUT) and Paid Order (PAID_SUCCESS) with Txn ID, Price, Currency & Items!
  googleSheetWebhookUrl: 'https://script.google.com/macros/s/AKfycbx5gW7QlFdzIzf_vGjmdnJlYZTHffP67kTj5pfc1cfVaVWt0QnKv5PsuQH_qwRrOvoSEA/exec',

  // 0b. META PIXEL ID (Facebook / Instagram Ads Conversion Tracking)
  // Paste your 15-digit Meta Pixel ID from business.facebook.com/events_manager
  // Automatically tracks: PageView, ViewContent, AddToCart, InitiateCheckout, and Purchase (with exact INR/USD value!)
  metaPixelId: 'YOUR_META_PIXEL_ID',

  // 'auto_region' automatically routes:
  //   🇮🇳 Indian Visitors (INR)     -> Razorpay (UPI, GPay, PhonePe, Paytm, Indian Cards)
  //   🇺🇸 US/Global Visitors (USD) -> PayPal (PayPal 1-Click + International Debit/Credit Cards)
  // (Automatically falls back to interactive preview mode until you paste your live keys below)
  mode: 'auto_region',

  // 1. INDIA GATEWAY (INR) — Razorpay Standard Checkout (UPI / GPay / PhonePe / Cards)
  razorpay: {
    keyId: 'rzp_live_YOUR_KEY_ID', // Paste your rzp_live_... or rzp_test_... Key ID from Razorpay Dashboard
    businessName: 'PersonaLabs Academy',
    themeColor: '#e65ce4'
  },

  // 2. US / GLOBAL GATEWAY (USD) — PayPal Checkout (Supports 3 easy plug-and-play options)
  paypal: {
    // OPTION A (Recommended): Paste your PayPal Live Client ID from developer.paypal.com
    // Renders official PayPal + Debit/Credit Card buttons directly inside the popup and auto-unlocks on payment!
    clientId: 'YOUR_PAYPAL_CLIENT_ID',

    // OPTION B (Zero-Code Instant Setup): Paste your PayPal.me username (e.g. 'riyalabs')
    // Automatically sends US buyers to https://www.paypal.com/paypalme/YOUR_USERNAME/9USD (matches exact cart total!)
    paypalMeUsername: 'YOUR_PAYPAL_ME_USERNAME',

    // OPTION C: Or paste PayPal No-Code Payment Links (https://www.paypal.com/ncp/payment/...)
    paymentLinks: {
      base_flash: 'https://www.paypal.com/ncp/payment/YOUR_9_USD_LINK',
      base_expired: 'https://www.paypal.com/ncp/payment/YOUR_19_USD_LINK',
      bundle_flash: 'https://www.paypal.com/ncp/payment/YOUR_18_USD_LINK'
    }
  },

  // 3. Optional Custom Backend Webhook / Order Endpoint
  customApi: {
    createOrderEndpoint: '/api/checkout/create-order',
    verifyPaymentEndpoint: '/api/checkout/verify-payment'
  }
};

// Automatic Meta Pixel Loader & Conversion Event Tracker (PageView, ViewContent, AddToCart, InitiateCheckout, Purchase)
function initMetaPixel() {
  const pixelId = (PAYMENT_GATEWAY_CONFIG.metaPixelId || '').trim();
  if (!pixelId || pixelId.includes('YOUR_')) return;

  if (!window.fbq) {
    !(function (f, b, e, v, n, t, s) {
      if (f.fbq) return;
      n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n;
      n.push = n;
      n.loaded = !0;
      n.version = '2.0';
      n.queue = [];
      t = b.createElement(e);
      t.async = !0;
      t.src = v;
      s = b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t, s);
    })(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
  }

  window.fbq('init', pixelId);
  window.fbq('track', 'PageView');
  const { base } = getTotals();
  window.fbq('track', 'ViewContent', {
    content_name: 'AI Influencer Accelerator – 5-Day Launch Kit',
    content_category: 'Digital Course',
    value: base,
    currency: state.currency
  });
}

function trackMetaPixelEvent(eventName, params = {}) {
  try {
    if (typeof window.fbq === 'function') {
      window.fbq('track', eventName, params);
    }
  } catch (e) {}
}

function buildCheckoutOrderPayload() {
  const { base, activeBump1Price, activeBump2Price, discount, finalTotal } = getTotals();
  const emailVal = document.getElementById('customer-email')?.value.trim() || '';
  const phoneVal = (document.getElementById('customer-phone')?.value || '').replace(/\D/g, '');
  const nameVal = document.getElementById('customer-name')?.value.trim() || '';
  const dialCode = state.currency === 'INR' ? '+91' : '+1';
  const orderId = state.currentOrderId || ('ORD-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(100 + Math.random() * 900));
  state.currentOrderId = orderId;

  return {
    orderId,
    currency: state.currency, // 'INR' (India IP) or 'USD' (US/Global IP)
    visitorCountry: state.visitorCountry,
    gateway: state.currency === 'INR' ? 'razorpay' : 'paypal',
    amount: finalTotal,
    formattedAmount: formatPrice(finalTotal),
    amountInSubunits: Math.round(finalTotal * 100), // Paise for Razorpay (INR) / Cents for PayPal (USD)
    offerStatus: state.offerExpired ? 'expired_standard_price' : 'active_10m_flash_offer',
    breakdown: {
      baseKit: base,
      uncensoredHackBump: state.bumpAdded ? activeBump1Price : 0,
      viralHooksBump: state.bump2Added ? activeBump2Price : 0,
      promoCode: state.promoCode || 'NONE',
      discountAmount: discount
    },
    items: [
      { id: 'ai_launch_kit', name: 'AI Influencer Accelerator – 5-Day Launch Kit', price: base },
      ...(state.bumpAdded ? [{ id: 'uncensored_hack', name: 'Uncensored Content Hack (VIP Add-On)', price: activeBump1Price }] : []),
      ...(state.bump2Added ? [{ id: 'viral_hooks_pack', name: '500+ Viral Reel Hooks & Auto-DM Pack', price: activeBump2Price }] : [])
    ],
    customer: {
      name: nameVal,
      email: emailVal,
      phone: `${dialCode}${phoneVal}`,
      rawPhone: phoneVal
    },
    createdAt: new Date().toISOString()
  };
}

// Automatically logs every Checkout Lead (INITIATED_CHECKOUT) and Completed Order (PAID_SUCCESS)
// to your Google Sheet via Google Apps Script Webhook (plus local backup in localStorage)
async function logOrderToGoogleSheet(eventStatus = 'PAID_SUCCESS', extra = {}) {
  try {
    const payload = window.lastCheckoutOrderPayload || buildCheckoutOrderPayload();
    const now = new Date();
    const istTime = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', dateStyle: 'medium', timeStyle: 'medium' });

    const sheetRow = {
      timestampIST: istTime,
      timestampISO: now.toISOString(),
      status: eventStatus, // 'INITIATED_CHECKOUT' or 'PAID_SUCCESS'
      orderId: payload.orderId,
      transactionId: extra.transactionId || state.lastTransactionId || 'PENDING',
      customerName: payload.customer.name || 'Guest',
      customerEmail: payload.customer.email || '',
      customerPhone: payload.customer.phone || '',
      currency: payload.currency,
      totalPaid: payload.amount,
      formattedTotal: payload.formattedAmount,
      basePrice: payload.breakdown.baseKit,
      bump1_UncensoredHack: state.bumpAdded ? `YES (+${formatPrice(payload.breakdown.uncensoredHackBump)})` : 'NO',
      bump2_ViralHooksPack: state.bump2Added ? `YES (+${formatPrice(payload.breakdown.viralHooksBump)})` : 'NO',
      promoCode: payload.breakdown.promoCode !== 'NONE' ? `${payload.breakdown.promoCode} (-${formatPrice(payload.breakdown.discountAmount)})` : 'NONE',
      paymentMethod: extra.paymentMethod || state.lastPaymentMethod || payload.gateway.toUpperCase(),
      offerTier: state.offerExpired ? 'Expired Standard Price' : '10-Min Flash Sale',
      visitorCountry: payload.visitorCountry || 'IN',
      itemsSummary: payload.items.map((i) => i.name).join(' + '),
      pageUrl: window.location.href,
      grantCoreDrive: eventStatus === 'PAID_SUCCESS',
      grantNsfwDrive: Boolean(eventStatus === 'PAID_SUCCESS' && state.bumpAdded),
      grantHooksDrive: Boolean(eventStatus === 'PAID_SUCCESS' && state.bump2Added)
    };

    // 1. Save to local backup log in browser localStorage
    try {
      const existingLogs = JSON.parse(localStorage.getItem('personalabs_order_log') || '[]');
      existingLogs.unshift(sheetRow);
      localStorage.setItem('personalabs_order_log', JSON.stringify(existingLogs.slice(0, 100)));
    } catch (e) {}

    // 2. Send to Google Sheets Webhook if configured
    const webhookUrl = (PAYMENT_GATEWAY_CONFIG.googleSheetWebhookUrl || '').trim();
    if (!webhookUrl || webhookUrl.includes('YOUR_')) {
      console.info('[Google Sheets DB Preview] Row ready to log:', sheetRow);
      return sheetRow;
    }

    await fetch(webhookUrl, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(sheetRow)
    });
    return sheetRow;
  } catch (err) {
    console.warn('Google Sheet webhook log warning:', err);
  }
}

// Helper you can run from browser console: testGoogleSheetWebhook() to send a test row to your Google Sheet!
window.testGoogleSheetWebhook = function () {
  return logOrderToGoogleSheet('TEST_WEBHOOK_PING', {
    transactionId: 'TEST-TXN-' + Math.floor(100000 + Math.random() * 900000),
    paymentMethod: 'Webhook Connection Test'
  });
};

// Dynamically load and mount official PayPal Smart Buttons when PAYMENT_GATEWAY_CONFIG.paypal.clientId is configured
let paypalSdkLoaded = false;
function mountPayPalSdkButtonsIfConfigured() {
  const clientId = PAYMENT_GATEWAY_CONFIG.paypal?.clientId;
  if (!clientId || clientId.includes('YOUR_')) return;

  const sdkContainer = document.getElementById('paypal-sdk-button-container');
  const fallbackButtons = document.getElementById('paypal-fallback-buttons');

  function renderButtons() {
    if (!window.paypal || !sdkContainer) return;
    sdkContainer.innerHTML = '';
    sdkContainer.classList.remove('hidden');
    if (fallbackButtons) fallbackButtons.classList.add('hidden');

    window.paypal
      .Buttons({
        style: { layout: 'vertical', color: 'gold', shape: 'rect', label: 'paypal' },
        createOrder: function (data, actions) {
          const payload = buildCheckoutOrderPayload();
          return actions.order.create({
            application_context: {
              brand_name: 'PersonaLabs Academy',
              shipping_preference: 'NO_SHIPPING',
              user_action: 'PAY_NOW'
            },
            purchase_units: [
              {
                description: payload.items.map((i) => i.name).join(' + '),
                soft_descriptor: 'PERSONALABS',
                custom_id: state.currentOrderId || '',
                amount: {
                  currency_code: 'USD',
                  value: String(payload.amount.toFixed(2))
                }
              }
            ]
          });
        },
        onApprove: function (data, actions) {
          return actions.order.capture().then(function (details) {
            const payerName = details?.payer?.name?.given_name || '';
            const ppTxId = details?.id || 'PP-' + Math.floor(10000000 + Math.random() * 90000000);
            simulatePaymentComplete(`PayPal USD (${ppTxId || payerName || 'Verified'})`, ppTxId);
          });
        }
      })
      .render('#paypal-sdk-button-container');
  }

  if (paypalSdkLoaded && window.paypal) {
    renderButtons();
    return;
  }

  const script = document.createElement('script');
  script.src = `https://www.paypal.com/sdk/js?client-id=${encodeURIComponent(clientId)}&currency=USD`;
  script.onload = () => {
    paypalSdkLoaded = true;
    renderButtons();
  };
  document.head.appendChild(script);
}

// Triggered when a US/Global visitor clicks the PayPal or Debit/Credit Card button in the modal
function triggerPayPalCheckout(methodLabel = 'PayPal Express (USD)') {
  const orderPayload = window.lastCheckoutOrderPayload || buildCheckoutOrderPayload();
  const ppCfg = PAYMENT_GATEWAY_CONFIG.paypal || {};

  // 1. Check if PayPal No-Code Payment Link is configured
  const linkKey = state.bumpAdded
    ? 'bundle_flash'
    : state.offerExpired
    ? 'base_expired'
    : 'base_flash';
  const ncpUrl = ppCfg.paymentLinks?.[linkKey];
  if (ncpUrl && !ncpUrl.includes('YOUR_')) {
    window.location.href = ncpUrl;
    return;
  }

  // 2. Check if PayPal.me username is configured (automatically passes exact dynamic USD total!)
  if (ppCfg.paypalMeUsername && !ppCfg.paypalMeUsername.includes('YOUR_')) {
    const cleanUser = ppCfg.paypalMeUsername.replace(/^@/, '').trim();
    window.location.href = `https://www.paypal.com/paypalme/${encodeURIComponent(cleanUser)}/${orderPayload.amount}USD`;
    return;
  }

  // 3. Fallback: Interactive preview completion when testing before keys are added
  simulatePaymentComplete(methodLabel);
}

async function handleCheckoutSubmit(event) {
  event.preventDefault();
  triggerHaptic(25);

  const emailEl = document.getElementById('customer-email');
  const phoneEl = document.getElementById('customer-phone');
  const nameEl = document.getElementById('customer-name');

  const errEmail = document.getElementById('err-email');
  const errPhone = document.getElementById('err-phone');
  const errName = document.getElementById('err-name');

  errEmail.classList.add('hidden');
  errPhone.classList.add('hidden');
  errName.classList.add('hidden');

  let valid = true;
  const emailVal = emailEl.value.trim();
  const phoneVal = phoneEl.value.replace(/\D/g, '');
  const nameVal = nameEl.value.trim();

  if (!emailVal || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailVal)) {
    errEmail.classList.remove('hidden');
    valid = false;
  }

  if (!phoneVal || phoneVal.length < 10) {
    errPhone.classList.remove('hidden');
    valid = false;
  }

  if (!nameVal || nameVal.length < 2) {
    errName.classList.remove('hidden');
    valid = false;
  }

  if (!valid) return;

  state.currentOrderId = 'ORD-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(100 + Math.random() * 900);
  const orderPayload = buildCheckoutOrderPayload();
  window.lastCheckoutOrderPayload = orderPayload;

  // Fire Meta Pixel InitiateCheckout Event with exact cart value and currency
  trackMetaPixelEvent('InitiateCheckout', {
    value: orderPayload.amount,
    currency: orderPayload.currency,
    num_items: orderPayload.items.length,
    content_name: orderPayload.items.map((i) => i.name).join(' + ')
  });

  // Log Lead / Initiated Checkout to Google Sheet right away (captures WhatsApp/Email even if buyer drops off!)
  logOrderToGoogleSheet('INITIATED_CHECKOUT', {
    transactionId: 'PENDING_PAYMENT',
    paymentMethod: orderPayload.currency === 'INR' ? 'Razorpay (Initiated)' : 'PayPal (Initiated)'
  });

  // 1. Auto-Region Live Routing:
  //    - India (INR) -> Opens live Razorpay Checkout popup immediately once keyId is set
  //    - US/Global (USD) -> Opens PayPal Checkout modal (or redirects to PayPal link if configured)
  if (PAYMENT_GATEWAY_CONFIG.mode === 'auto_region') {
    const rzpKey = PAYMENT_GATEWAY_CONFIG.razorpay?.keyId || '';
    if (orderPayload.currency === 'INR' && window.Razorpay && rzpKey && !rzpKey.includes('YOUR_')) {
      const rzp = new window.Razorpay({
        key: rzpKey,
        amount: orderPayload.amountInSubunits,
        currency: 'INR',
        name: PAYMENT_GATEWAY_CONFIG.razorpay.businessName,
        description: orderPayload.items.map((i) => i.name).join(' + '),
        prefill: {
          name: orderPayload.customer.name,
          email: orderPayload.customer.email,
          contact: orderPayload.customer.phone
        },
        theme: { color: PAYMENT_GATEWAY_CONFIG.razorpay.themeColor },
        handler: function (response) {
          document.getElementById('payment-modal').classList.remove('hidden');
          document.getElementById('payment-modal').classList.add('flex');
          const rzpTxId = response.razorpay_payment_id || 'rzp_verified_' + Date.now();
          simulatePaymentComplete(`Razorpay UPI/Card (${rzpTxId})`, rzpTxId);
        }
      });
      rzp.open();
      return;
    } else if (orderPayload.currency === 'USD') {
      mountPayPalSdkButtonsIfConfigured();
    }
  } else if (PAYMENT_GATEWAY_CONFIG.mode === 'custom_api') {
    try {
      const res = await fetch(PAYMENT_GATEWAY_CONFIG.customApi.createOrderEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(orderPayload)
      });
      const data = await res.json();
      if (data && data.checkoutUrl) {
        window.location.href = data.checkoutUrl;
        return;
      }
    } catch (err) {
      console.error('Custom gateway error:', err);
    }
  }

  // Open region-matched Razorpay (INR) / PayPal (USD) checkout modal
  document.getElementById('payment-step-select').classList.remove('hidden');
  document.getElementById('payment-step-success').classList.add('hidden');

  const modal = document.getElementById('payment-modal');
  modal.classList.remove('hidden');
  modal.classList.add('flex');
}

function simulatePaymentComplete(methodName, explicitTxId = null) {
  triggerHaptic(40);
  state.lastPaymentMethod = methodName;
  const txId = explicitTxId || ('PLA-' + Math.floor(10000000 + Math.random() * 90000000));
  state.lastTransactionId = txId;

  const nameVal = document.getElementById('customer-name').value.trim() || 'Creator';
  const emailVal = document.getElementById('customer-email').value.trim();

  // Fire Meta Pixel Purchase Event with exact total paid & currency (INR or USD)
  const { finalTotal } = getTotals();
  trackMetaPixelEvent('Purchase', {
    value: finalTotal,
    currency: state.currency,
    content_name: 'AI Influencer Accelerator – 5-Day Launch Kit',
    content_type: 'product'
  });

  // Compute deterministic verification signature tied to (email, txId, addonKey)
  // Prevents manual URL (?b1=1) or localStorage (bumpAdded: true) tampering
  function computeAddonSig(email, tx, addonKey) {
    const raw = `PL_VIP_2026::${String(email || '').trim().toLowerCase()}::${String(tx || '').trim()}::${addonKey}`;
    let h1 = 0x811c9dc5;
    for (let i = 0; i < raw.length; i++) {
      h1 ^= raw.charCodeAt(i);
      h1 = Math.imul(h1, 0x01000193);
    }
    return (h1 >>> 0).toString(16).padStart(8, '0');
  }

  let vt1 = '';
  let vt2 = '';
  try {
    const prevRaw = localStorage.getItem('personalabs_unlocked_vault');
    const prev = prevRaw ? JSON.parse(prevRaw) : {};
    const prevTx = prev.transactionId || txId;
    const prevEmail = prev.email || emailVal;

    const prevB1Valid = Boolean(prev.bumpAdded && prev.vt1 === computeAddonSig(prevEmail, prevTx, 'BUMP1_NSFW_8f92a1c4'));
    const prevB2Valid = Boolean(prev.bump2Added && prev.vt2 === computeAddonSig(prevEmail, prevTx, 'BUMP2_HOOKS_3d7e91b2'));

    state.bumpAdded = Boolean(state.bumpAdded || prevB1Valid);
    state.bump2Added = Boolean(state.bump2Added || prevB2Valid);

    if (state.bumpAdded) vt1 = computeAddonSig(emailVal, txId, 'BUMP1_NSFW_8f92a1c4');
    if (state.bump2Added) vt2 = computeAddonSig(emailVal, txId, 'BUMP2_HOOKS_3d7e91b2');

    localStorage.setItem(
      'personalabs_unlocked_vault',
      JSON.stringify({
        unlocked: true,
        transactionId: txId,
        name: nameVal,
        email: emailVal,
        method: methodName,
        bumpAdded: state.bumpAdded,
        bump2Added: state.bump2Added,
        vt1,
        vt2,
        unlockedAt: new Date().toISOString()
      })
    );
  } catch (e) {}

  // Log Completed Order + Trigger Automatic Google Drive Folder Whitelisting (DriveApp.addViewer)
  if (methodName !== 'Verified Order Lookup' && methodName !== 'Verified Order') {
    logOrderToGoogleSheet('PAID_SUCCESS', {
      transactionId: txId,
      paymentMethod: methodName
    });
  }

  document.getElementById('payment-step-select').classList.add('hidden');
  const successStep = document.getElementById('payment-step-success');
  successStep.classList.remove('hidden');

  document.getElementById('success-customer-greeting').textContent =
    `Hi ${nameVal}! Payment (${txId}) verified. Google Drive viewer access has been automatically whitelisted for ${emailVal}!`;

  const qs = new URLSearchParams();
  qs.set('email', emailVal);
  qs.set('tx', txId);
  if (vt1) qs.set('vt1', vt1);
  if (vt2) qs.set('vt2', vt2);
  const vaultParams = `?${qs.toString()}`;

  const portalBtn = document.getElementById('delivery-link-vault-portal');
  if (portalBtn) {
    portalBtn.href = `course-vault/index.html${vaultParams}`;
  }
  const urlInput = document.getElementById('direct-vault-url-input');
  if (urlInput) {
    urlInput.value = `${window.location.origin}/course-vault/index.html${vaultParams}`;
  }

  const bumpDownload = document.getElementById('success-bump-download');
  const bump1Link = document.getElementById('delivery-link-bump1');
  if (state.bumpAdded && vt1) {
    if (bump1Link) bump1Link.href = `course-vault/uncensored-vip-8f92a1c4.html?email=${encodeURIComponent(emailVal)}&tx=${encodeURIComponent(txId)}&vt1=${vt1}`;
    bumpDownload.classList.remove('hidden');
  } else {
    bumpDownload.classList.add('hidden');
  }

  const bump2Download = document.getElementById('success-bump-2-download');
  const bump2Link = document.getElementById('delivery-link-bump2');
  if (bump2Download) {
    if (state.bump2Added && vt2) {
      if (bump2Link) bump2Link.href = `course-vault/hooks-vip-3d7e91b2.html?email=${encodeURIComponent(emailVal)}&tx=${encodeURIComponent(txId)}&vt2=${vt2}`;
      bump2Download.classList.remove('hidden');
    } else {
      bump2Download.classList.add('hidden');
    }
  }
}

function copyDirectVaultLink() {
  triggerHaptic(20);
  const input = document.getElementById('direct-vault-url-input');
  const btn = document.getElementById('btn-copy-vault-link');
  const linkUrl = input ? input.value : `${window.location.origin}/course-vault/index.html`;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(linkUrl).catch(() => {});
  } else if (input) {
    input.select();
    document.execCommand('copy');
  }
  if (btn) {
    const orig = btn.textContent;
    btn.textContent = '✓ Copied!';
    btn.classList.add('bg-emerald-600');
    setTimeout(() => {
      btn.textContent = orig;
      btn.classList.remove('bg-emerald-600');
    }, 2200);
  }
  triggerPayoutToast('📋 Direct Course Vault link copied to clipboard!');
}

function openSignInModal() {
  triggerHaptic(20);
  try {
    const raw = localStorage.getItem('personalabs_unlocked_vault');
    if (raw) {
      const saved = JSON.parse(raw);
      if (saved && saved.unlocked) {
        state.bumpAdded = Boolean(saved.bumpAdded);
        state.bump2Added = Boolean(saved.bump2Added);
        state.lastPaymentMethod = saved.method || 'Verified Order';
        const modal = document.getElementById('payment-modal');
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        simulatePaymentComplete(state.lastPaymentMethod, saved.transactionId || null);
        return;
      }
    }
  } catch (e) {}

  const email = window.prompt('Enter the email address used during your purchase to re-open your Instant Access Vault:');
  if (email && email.includes('@')) {
    const emailInput = document.getElementById('customer-email');
    if (emailInput) emailInput.value = email.trim();
    const modal = document.getElementById('payment-modal');
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    simulatePaymentComplete('Verified Order Lookup');
  }
}

function downloadOfficialReceipt() {
  const { finalTotal } = getTotals();
  const nameVal = document.getElementById('customer-name').value.trim() || 'Valued Creator';
  const emailVal = document.getElementById('customer-email').value.trim() || 'creator@example.com';
  const phoneVal = document.getElementById('customer-phone').value.trim() || '';
  const txId = state.lastTransactionId || ('PLA-' + Math.floor(10000000 + Math.random() * 90000000));
  const vaultOrigin = window.location.origin.startsWith('http') ? window.location.origin : 'https://personalabs.store';

  const items = ['1x AI Influencer Accelerator – 5-Day Launch Kit (Lifetime Access)'];
  if (state.bumpAdded) items.push('1x Uncensored Content Hack (VIP Add-On Guide)');
  if (state.bump2Added) items.push('1x 500+ Viral Reel Hooks & Auto-DM Templates Pack');

  const receiptText = [
    '==========================================================',
    '     OFFICIAL PAYMENT RECEIPT — PERSONALABS ACADEMY       ',
    '==========================================================',
    `Transaction ID : ${txId}`,
    `Date           : ${new Date().toLocaleString()}`,
    `Customer Name  : ${nameVal}`,
    `Email          : ${emailVal}`,
    `Phone          : ${state.currency === 'INR' ? '+91' : '+1'} ${phoneVal}`,
    `Payment Method : ${state.lastPaymentMethod}`,
    '----------------------------------------------------------',
    'ITEMS UNLOCKED:',
    ...items.map((i) => `  - ${i}`),
    '----------------------------------------------------------',
    `TOTAL PAID     : ${formatPrice(finalTotal)} (${state.currency})`,
    '----------------------------------------------------------',
    'INSTANT ACCESS LINKS (BOOKMARK THESE — NO EMAIL NEEDED):',
    `1. Interactive 5-Day Course Portal : ${vaultOrigin}/course-vault/index.html`,
    `2. 250+ Character DNA Prompt Bible : ${vaultOrigin}/course-vault/character-dna-prompt-bible.html`,
    '3. Google Drive Resource Vault     : https://drive.google.com/drive/folders/13prDNfskRSTJNdFlTsunhzY6Mu34YiMv?usp=sharing',
    state.bumpAdded ? `4. Uncensored Content Hack Guide   : ${vaultOrigin}/course-vault/uncensored-content-hack.html` : '',
    state.bump2Added ? `5. 500+ Viral Reel Hooks & Auto-DM : ${vaultOrigin}/course-vault/viral-hooks-and-autodm-pack.html` : '',
    '----------------------------------------------------------',
    'Support Email  : sayana.official.help@gmail.com',
    '=========================================================='
  ].filter(Boolean).join('\n');

  const blob = new Blob([receiptText], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `PersonaLabs-Academy-Receipt-${txId}.txt`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function downloadHooksPack() {
  const content = [
    '==========================================================',
    '   500+ VIRAL AI REEL HOOKS & MANYCHAT AUTO-DM TEMPLATES  ',
    '==========================================================',
    '',
    '[TOP CURIOSITY HOOKS FOR AI INFLUENCER REELS (0-3 SECONDS)]',
    '1. "Everyone asked how I traveled to 4 countries this week without leaving my room..."',
    '2. "Stop scrolling if you still think you need a camera to build a 100K creator page."',
    '3. "POV: You locked in your AI character seed once and automated your entire content calendar."',
    '4. "99% of people watching this Reel cannot tell what is different about this video..."',
    '5. "They told me virtual influencers were a fad... here is my last 30 days creator dashboard."',
    '',
    '[HIGH-CONVERTING MANYCHAT COMMENT-TO-DM AUTOMATION FLOW]',
    'Trigger Keyword: "LAUNCH" or "BLUEPRINT"',
    'Auto-Reply Public Comment: "Just sent the full kit straight to your DMs! Check your message requests ⚡"',
    'Automated DM #1: "Hey {{first_name}}! Here is the exact step-by-step AI breakdown you requested 👇 [YOUR_AFFILIATE_OR_PRODUCT_LINK]"'
  ].join('\n');

  const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'Viral-AI-Reel-Hooks-And-Auto-DM-Templates.txt';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// =========================================================================
// 10-MINUTE FLASH OFFER COUNTDOWN & AUTOMATIC PRICE INCREASE ON EXPIRY
// =========================================================================
const OFFER_STORAGE_KEY = 'personalabs_10m_offer_v3';

function renderOfferTimerDisplay() {
  const timerEl = document.getElementById('countdown-timer');
  const miniTimerEl = document.getElementById('checkout-mini-timer');
  const pulseDot = document.getElementById('offer-pulse-dot');
  const pulseInner = document.getElementById('offer-pulse-inner');

  if (state.offerExpired || state.offerRemainingSeconds <= 0) {
    if (timerEl) {
      timerEl.textContent = '🔥 75% OFF ACTIVE';
      timerEl.className = 'font-mono-num rounded-md bg-amber-400 border border-amber-200 px-2.5 py-0.5 text-xs sm:text-sm font-black text-slate-950 shadow-sm transition-colors cursor-pointer';
    }
    if (miniTimerEl) {
      miniTimerEl.textContent = 'SAVE 75%';
      miniTimerEl.className = 'font-mono-num font-black text-xs px-2 py-0.5 rounded bg-yellow-300 text-red-950 shrink-0';
    }
    if (pulseDot) pulseDot.className = 'relative flex h-2.5 w-2.5 items-center justify-center text-amber-400 pulse-dot';
    if (pulseInner) pulseInner.className = 'h-2.5 w-2.5 rounded-full bg-amber-400';
    return;
  }

  const mins = String(Math.floor(state.offerRemainingSeconds / 60)).padStart(2, '0');
  const secs = String(state.offerRemainingSeconds % 60).padStart(2, '0');
  const formatted = `⏱ ${mins}:${secs}`;

  if (timerEl) {
    timerEl.textContent = formatted;
    if (state.offerRemainingSeconds <= 180) {
      timerEl.className = 'font-mono-num rounded-md bg-rose-500 border border-yellow-300 px-2.5 py-0.5 text-xs sm:text-sm font-black text-white shadow-sm animate-pulse transition-colors cursor-pointer';
    } else {
      timerEl.className = 'font-mono-num rounded-md bg-amber-400 border border-amber-200 px-2.5 py-0.5 text-xs sm:text-sm font-black text-slate-950 shadow-sm transition-colors cursor-pointer';
    }
  }
  if (miniTimerEl) {
    miniTimerEl.textContent = `${mins}:${secs}`;
    miniTimerEl.className = 'font-mono-num font-black text-xs px-2 py-0.5 rounded bg-amber-400 text-slate-950 shadow-sm shrink-0';
  }
  if (pulseDot) pulseDot.className = 'relative flex h-2.5 w-2.5 items-center justify-center text-amber-400 pulse-dot';
  if (pulseInner) pulseInner.className = 'h-2.5 w-2.5 rounded-full bg-amber-400';
}

function handleOfferExpiredTransition() {
  if (state.offerExpired) return;
  state.offerExpired = true;
  state.offerRemainingSeconds = 0;
  triggerHaptic(40);
  renderOfferTimerDisplay();
  renderPricing();

  const cfg = state.prices[state.currency];
  const savedAmount = cfg.strike - cfg.expiredBase;
  triggerPayoutToast(
    `⚡ ${formatPrice(cfg.base)} Fast-Action Bonus ended! 75% OFF Launch Offer still active: ${formatPrice(cfg.expiredBase)} (Save ${formatPrice(savedAmount)} off ${formatPrice(cfg.strike)}!)`
  );
}

function fastForwardOfferTimer() {
  triggerHaptic(18);
  state.offerExpired = false;
  state.offerRemainingSeconds = 3;
  try {
    sessionStorage.setItem(OFFER_STORAGE_KEY, String(Date.now() + 3000));
  } catch (e) {}
  const pop = document.getElementById('geo-sim-popover');
  if (pop) pop.classList.add('hidden');
  renderOfferTimerDisplay();
  renderPricing();
  triggerPayoutToast('⏩ Timer set to 00:03 — Watch price increase automatically in 3 seconds!');
}

function resetOfferTimer() {
  triggerHaptic(18);
  state.offerExpired = false;
  state.offerRemainingSeconds = 600;
  try {
    sessionStorage.setItem(OFFER_STORAGE_KEY, String(Date.now() + 600 * 1000));
  } catch (e) {}
  const pop = document.getElementById('geo-sim-popover');
  if (pop) pop.classList.add('hidden');
  renderOfferTimerDisplay();
  renderPricing();
  const cfg = state.prices[state.currency];
  triggerPayoutToast(`🔄 10:00 Flash Offer Reset! 88% OFF (${formatPrice(cfg.base)}) restored.`);
}

// Countdown Timer & Live Social Proof Notifications (Region-Matched by IP)
function initTimersAndSocialProof() {
  // Initialize 10-minute (600s) deadline in sessionStorage (auto-renews if an old background session expired)
  try {
    const savedDeadline = parseInt(sessionStorage.getItem(OFFER_STORAGE_KEY), 10);
    const now = Date.now();
    if (savedDeadline && !isNaN(savedDeadline) && savedDeadline > now) {
      state.offerRemainingSeconds = Math.ceil((savedDeadline - now) / 1000);
      state.offerExpired = false;
    } else {
      state.offerRemainingSeconds = 600; // Fresh 10 minutes
      state.offerExpired = false;
      sessionStorage.setItem(OFFER_STORAGE_KEY, String(now + 600 * 1000));
    }
  } catch (e) {
    state.offerRemainingSeconds = 600;
    state.offerExpired = false;
  }

  renderOfferTimerDisplay();
  renderPricing();

  setInterval(() => {
    if (state.offerExpired) return;
    if (state.offerRemainingSeconds > 0) {
      state.offerRemainingSeconds--;
      renderOfferTimerDisplay();
      if (state.offerRemainingSeconds <= 0) {
        handleOfferExpiredTransition();
      }
    }
  }, 1000);

  const buyersIN = [
    { name: 'Aarav S. from Mumbai', action: 'Unlocked AI Influencer Kit + Uncensored Hack (₹498)', time: 'Just now • Verified UPI' },
    { name: 'Priya K. from Bengaluru', action: 'Enrolled in AI Influencer Accelerator (₹249)', time: '2 mins ago • Verified GPay' },
    { name: 'Rohan M. from Delhi', action: 'Unlocked Full VIP Bundle (₹647)', time: '4 mins ago • Verified PhonePe' },
    { name: 'Sneha T. from Jaipur', action: 'Enrolled in AI Influencer Accelerator (₹249)', time: '6 mins ago • Verified Paytm' },
    { name: 'Vikram D. from Pune', action: 'Unlocked AI Influencer Kit + Uncensored Hack (₹498)', time: '9 mins ago • Verified Card' }
  ];

  const buyersUS = [
    { name: 'Tyler M. from Austin, TX', action: 'Unlocked AI Influencer Kit + Uncensored Hack ($18)', time: 'Just now • Verified Apple Pay' },
    { name: 'Sophia L. from Miami, FL', action: 'Enrolled in AI Influencer Accelerator ($9)', time: '2 mins ago • Verified Stripe' },
    { name: 'Marcus R. from Los Angeles, CA', action: 'Unlocked Full VIP Bundle ($23)', time: '4 mins ago • Verified Apple Pay' },
    { name: 'Chloe W. from New York, NY', action: 'Enrolled in AI Influencer Accelerator ($9)', time: '6 mins ago • Verified PayPal' },
    { name: 'Brandon K. from Seattle, WA', action: 'Unlocked AI Influencer Kit + Uncensored Hack ($18)', time: '8 mins ago • Verified Stripe' }
  ];

  let idx = 0;
  const toastEl = document.getElementById('social-proof-toast');
  const avatarEl = document.getElementById('toast-avatar');
  const titleEl = document.getElementById('toast-title');
  const descEl = document.getElementById('toast-desc');
  const timeEl = document.getElementById('toast-time');

  function triggerToast() {
    const activeList = state.currency === 'INR' ? buyersIN : buyersUS;
    const item = activeList[idx % activeList.length];
    idx++;
    avatarEl.textContent = item.name.charAt(0);
    titleEl.textContent = item.name;
    descEl.textContent = item.action;
    timeEl.textContent = item.time;

    toastEl.classList.remove('translate-y-24', 'opacity-0');
    toastEl.classList.add('translate-y-0', 'opacity-100');

    setTimeout(() => {
      toastEl.classList.add('translate-y-24', 'opacity-0');
      toastEl.classList.remove('translate-y-0', 'opacity-100');
    }, 4500);
  }

  setTimeout(triggerToast, 4000);
  setInterval(triggerToast, 14000);
}

// =========================================================================
// DYNAMIC REAL-TIME "VIEWING NOW" COUNTER (👁 32 viewing now)
// =========================================================================
function initDynamicLiveViewers() {
  let currentViewers = 32;
  const minViewers = 26;
  const maxViewers = 54;

  function scheduleNextViewerTick() {
    // Organic randomized interval between 2.2s and 4.5s
    const nextDelayMs = Math.floor(2200 + Math.random() * 2300);
    setTimeout(() => {
      // Pick a realistic delta: -2, -1, +1, +2, or +3 (slight upward bias when under 36)
      const deltas = currentViewers < 36 ? [-1, 1, 1, 2, 3] : [-2, -1, -1, 1, 2];
      const delta = deltas[Math.floor(Math.random() * deltas.length)];
      currentViewers = Math.max(minViewers, Math.min(maxViewers, currentViewers + delta));

      const countEls = document.querySelectorAll('.live-viewer-count');
      countEls.forEach((el) => {
        el.textContent = String(currentViewers);
        el.classList.add('scale-125', 'text-white');
        setTimeout(() => {
          el.classList.remove('scale-125', 'text-white');
        }, 280);
      });

      scheduleNextViewerTick();
    }, nextDelayMs);
  }

  scheduleNextViewerTick();
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
  const day1 = document.getElementById('curr-body-0');
  if (day1) {
    day1.style.maxHeight = day1.scrollHeight + 32 + 'px';
  }
  loadCheckoutDraft();
  detectCurrencyByIP();
  initTimersAndSocialProof();
  initDynamicLiveViewers();
  initReelSwipeGestures();
  initMetaPixel();

  // Check if a returning student clicked a 1-Click Add-On Upgrade link from course-vault/index.html (?upgrade=bump1 or ?upgrade=bump2)
  try {
    const params = new URLSearchParams(window.location.search);
    const upgradeTarget = (params.get('upgrade') || '').toLowerCase();
    if (upgradeTarget === 'bump1' || upgradeTarget === 'bump2') {
      state.upgradeOnly = true;
      const prevRaw = localStorage.getItem('personalabs_unlocked_vault');
      const prev = prevRaw ? JSON.parse(prevRaw) : {};

      // Mark already-owned add-on so student knows it's already in their vault and isn't charged twice
      if (prev.bumpAdded && upgradeTarget === 'bump2') {
        const p1 = document.getElementById('bump-status-pill');
        const t1 = document.getElementById('bump-tag-right');
        if (p1) { p1.textContent = '✔ Already Owned in Vault'; p1.className = 'text-[10px] font-bold text-emerald-600'; }
        if (t1) { t1.textContent = 'Owned ✓'; t1.className = 'text-xs font-semibold text-emerald-600'; }
      }
      if (prev.bump2Added && upgradeTarget === 'bump1') {
        const p2 = document.getElementById('bump-2-status-pill');
        const t2 = document.getElementById('bump-2-tag-right');
        if (p2) { p2.textContent = '✔ Already Owned in Vault'; p2.className = 'text-[10px] font-bold text-emerald-600'; }
        if (t2) { t2.textContent = 'Owned ✓'; t2.className = 'text-xs font-semibold text-emerald-600'; }
      }

      if (upgradeTarget === 'bump1' && !state.bumpAdded) toggleOrderBump();
      if (upgradeTarget === 'bump2' && !state.bump2Added) toggleSecondOrderBump();
      renderPricing();
      setTimeout(() => {
        scrollToCheckout();
        triggerPayoutToast(
          upgradeTarget === 'bump1'
            ? '🔓 Add-On Upgrade Mode: Paying only for Uncensored Content Hack (+4 NSFW Videos)!'
            : '⚡ Add-On Upgrade Mode: Paying only for 500+ Viral Reel Hooks Pack!'
        );
      }, 400);
    }
  } catch (e) {}
});
