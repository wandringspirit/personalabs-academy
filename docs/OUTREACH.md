# 💬 Outreach, Comment-to-DM Scripts & Recovery Templates (`OUTREACH.md`)

Last Updated: **November 9, 2026 (`v2.9.5`)**

> **Operating Mode (`9 Nov 2026`):** Because initial comment volume on the 11-Day Organic Master Reels queue is still low, DM fulfillment runs **Manually via Instagram Saved Replies / Direct Messages** (zero monthly ManyChat cost until daily comments pass `10–15/day`). Abandoned cart recovery and 12-hour add-on upsells run **100% automatically via Google Apps Script (`Version 3`) `GmailApp` triggers**!

---

## 1. Instagram Reel Comment-to-DM Workflow (`@personalabsacademy`)

### Active 11-Reel Trigger Keywords (`9 Nov – 19 Nov 2026`)
All keywords point to `https://personalabs.store` (`₹199 / $9` Flash Offer):  
`PROMPT` · `MODEL` · `GLITCH` · `TRAVEL` · `DANCE` · `TWIRL` · `CREATOR` · `VACATION` · `SKIN` · `LAUNCH` · `VIP` *(plus universal `AI` / `LINK`)*

### A. Public Comment Replies (Rotate Variations to Look Natural)
1. *"Just sent the full 5-day blueprint straight to your DMs! Check your inbox or Message Requests 🚀✨"*
2. *"Check your DMs! Just dropped the exact mobile workflow & prompt vault for you 🔥📩"*
3. *"Sent! Look inside your DMs right now before the ₹199 launch flash timer expires ⏱️👇"*

### B. Phase 1 — Manual Instagram Saved Reply DM *(Active Right Now)*
Pin these as **Instagram Saved Replies** in `@personalabsacademy` Settings → Saved Replies for 1-tap manual sending whenever someone comments or replies to a Story:

> **Saved Reply 1 (`kit` — Main Blueprint Link):**
> Hey! 👋 Here is instant access to the **PersonaLabs Academy 5-Day AI Influencer Launch Kit & 250+ Character DNA Prompt Vault** you asked for:
>
> 👉 **https://personalabs.store**
>
> Right now our **90% OFF Launch Flash Offer (₹199 India / $9 Global)** is live for the next 10 minutes on your link!
>
> Inside, you'll unlock immediately:
> ✅ **23 HD English-Captioned Videos** (19 Core + 100% mobile/cloud tools)
> ✅ **250+ Character DNA & Face-Lock Prompts** (100% consistent face across every scene)
> ✅ **Instant Member Vault + Google Drive Access** right after checkout
>
> 💡 *Tip: Tick the **Uncensored Content Hack** & **500+ Viral Reel Hooks** add-ons at checkout if you want the full VIP toolkit!*
>
> Reply here anytime if you want help choosing your virtual creator's niche! 🙌

> **Saved Reply 2 (`followup` — 4-Hour Gentle Check-In if No Reply):**
> Hey! Quick heads-up ⚡ Our **₹199 / $9** launch offer stays locked via your direct link here: **https://personalabs.store** *(you can also apply promo code **`RIYA10`** at checkout for an extra 10% off!)*. Let me know if you have any questions!

### C. Phase 2 — ManyChat Automation Blueprint *(Enable When Comments > 10–15/day)*
- Wire **Comment Contains** trigger on all reels for: `PROMPT, MODEL, GLITCH, TRAVEL, DANCE, TWIRL, CREATOR, VACATION, SKIN, LAUNCH, VIP, AI`.
- **Step 1 (5s Delay Quick-Reply Opener):**  
  `Hey {{first_name}}! 👋 You asked for the 5-Day AI Influencer Blueprint & 250+ DNA Prompt Vault! Tap below so Instagram keeps our chat open and I'll drop your link right here 👇` → Button: `Send Me The Blueprint 🚀`
- **Step 2 (On Button Tap):** Deliver Saved Reply 1 copy with `https://personalabs.store`.

---

## 2. Automated Email Recovery (`Apps Script Version 3` — Active 24/7) + Optional Manual WhatsApp

### A. Primary Engine (Zero Manual Effort):
`sendAbandonedCartRecoveryEmails` automatically emails `INITIATED_CHECKOUT` leads from **`PersonaLabs Academy <personalabsacademy@gmail.com>`** 25 minutes after drop-off (skipping buyers who completed payment).

### B. Optional Personal WhatsApp Follow-Up (For High-Intent Carts `₹448+` in `Logs` Tab):
> *"Hey [Name]! 👋 Noticed you were unlocking the **AI Influencer Accelerator** on PersonaLabs Academy (`personalabs.store`) earlier in case the UPI/payment page timed out.*
>
> *Your ₹199 launch spot is still reserved! You can complete your instant access here:*
> 👉 *https://personalabs.store*
>
> *Use promo code **RIYA10** (10% OFF) at checkout — reply here if you need any help!* 🙌"

---

## 3. Post-Purchase Add-On Upsell Templates (`?upgrade=bump1` / `?upgrade=bump2`)
**Automated Trigger (`12h` post-purchase):** `sendPostPurchaseAddonUpsellEmails` automatically sends 1-click student upgrade links where Base Kit = `₹0 / $0`.

**Manual DM / WhatsApp Version (If Following Up With VIP Candidates):**
> *"Hey [Name]! Hope you're loving the AI Influencer Accelerator videos! 🔥*
>
> *Since you're already enrolled, you can unlock our two add-on toolkits without paying for the base course again:*
>
> 1️⃣ **Uncensored Content Hack (4 Exclusive FaceFusion NSFW Videos + VIP Guide):**
> 👉 *https://personalabs.store/?upgrade=bump1* (`+₹249` / `+$9`)
>
> 2️⃣ **500+ Viral Reel Hooks & Auto-DM Pack:**
> 👉 *https://personalabs.store/?upgrade=bump2* (`+₹149` / `+$5`)
>
> *Once unlocked, they open immediately inside your Course Vault & Google Drive!*"
