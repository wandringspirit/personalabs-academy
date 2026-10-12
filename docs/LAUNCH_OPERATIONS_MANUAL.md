# 📖 PersonaLabs Academy — Complete Launch & Operations Manual

Last Updated: **October 12, 2026**  
Status: **Campaign #1 Live & Active (`Preparing` / `In Review`) • Storefront v2.8.2 Live on Vercel CDN**

---

## 🎯 1. Executive Summary & Live Assets

| Asset / Component | Live Identifier / URL | Current Status | Notes |
| :--- | :--- | :--- | :--- |
| **Official Website** | [https://personalabs.store](https://personalabs.store) & [https://www.personalabs.store](https://www.personalabs.store) | 🟢 **100% Live** | Hosted on Vercel Global Edge CDN (`216.198.79.1`). Zero server costs. |
| **Secret Testing Route** | [https://www.personalabs.store/kjboavhpoieabpraegnaln](https://www.personalabs.store/kjboavhpoieabpraegnaln) | 🟢 **Active for Testing** | ₹5 INR (Razorpay) / $1 USD (PayPal) per item with 1-click currency toggle. Can be disabled anytime in `app.js`. |
| **Member Vault Portal** | `https://personalabs.store/course-vault/` | 🟢 **100% Live** | 18 HD lessons, 250+ prompts, and authenticated add-on downloads. |
| **Meta Ad Campaign #1** | `IN - Sales - AI Influencer Launch Kit (INR)` | 🟡 **Preparing / In Review** | Budget: **₹300.00/day**. Target: India 18–36, IG Reels & Stories. |
| **Meta Ad Account** | `PersonaLabs Academy Ads` (`2218391099056783`) | 🟢 **Active** | Currency: INR (`₹`). Timezone: Asia/Kolkata. |
| **Meta Dataset / Pixel** | `PersonaLabs Academy Pixel` (`1661173205598260`) | 🟢 **Tracking Live** | Events: `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`. |
| **Instagram Creator Identity** | `@personalabsacademy` | 🟢 **Active** | 8K Exact-Face Saree Profile Picture. |
| **Facebook Page Identity** | `PersonaLabs Academy` (`ID: 61595148306909`) | 🟢 **Connected** | Linked to Ad Account and Campaign Identity. |
| **India Payment Gateway** | Razorpay Live (`rzp_live_TmX62nNGuBaTUc`) | 🟢 **Live** | Instant UPI (GPay, PhonePe, Paytm, QR) + RuPay/Visa Cards. |
| **Global Payment Gateway** | PayPal Live (`BAARfEN6...`) | 🟢 **Live** | PayPal 1-Click + International Cards in USD ($). |
| **Google Sheets Orders DB** | `PersonaLabs Academy — Orders DB` (`1Sy8fy...`) | 🟢 **Connected** | Real-time logging of leads (`INITIATED_CHECKOUT`) and paid orders (`PAID_SUCCESS`). |
| **Google Drive Auto-Access** | Webhook App (`DriveApp.addViewer`) | 🟢 **Connected** | Automatically whitelists customer's Gmail for purchased Drive folders. |

---

## ⚡ 2. Campaign #1 Setup & Budget Architecture

### A. How Your ₹300 Daily Budget Is Split Across Ads
You have **Advantage Campaign Budget (CBO)** enabled on the Campaign level:
* **Total Daily Budget:** **₹300.00 / day** (plus standard 18% GST).
* **Budget Distribution:** Meta's machine learning algorithm does **NOT** divide ₹300 equally into ₹100 / ₹100 / ₹100. Instead, it dynamically tests all 3 creatives and feeds the majority of the budget to whichever ad earns the **highest Watch-Time, highest Outbound CTR, and lowest Cost per Click**:
  * **`Ad 01 - Curiosity Reveal (INR)`:** High scroll-stopping hook (*"Wait… she doesn't actually exist"*).
  * **`Ad 02 - Proof & Monetization`:** Revenue & consistency proof (*"Stop paying ₹15,000 for product shoots"*).
  * **`Ad 03 - No Laptop 5Day System`:** Low-friction mobile objection handler (*"Think you need an expensive gaming PC?"*).
* **Why this is ideal:** If `Ad 01` gets 2x more clicks at a lower cost than `Ad 03`, Meta automatically routes ~₹200 to `Ad 01` and ~₹50 to `Ad 02` and `Ad 03`. You never waste money on a creative that isn't pulling its weight.

---

### B. Ad Scheduling: Can You Specify What Hours Ads Run?

#### 1. How Scheduling Works in Meta Ads:
* **Under Daily Budget (Current Setup — ₹300/day):**  
  Meta runs ads **24 hours a day** continuously. The AI algorithm paces the ₹300 spend across the day, naturally spending less when audiences are asleep and concentrating delivery during peak engagement hours. Meta **disables** the hourly time-of-day scheduler when using a Daily Budget.
* **Under Lifetime Budget:**  
  If you switch the budget type to a **Lifetime Budget** (e.g. ₹2,100 for 7 days), Meta enables the **Ad Scheduling** grid where you can highlight specific hours (e.g., only 10:00 AM – 11:30 PM).

#### 2. Recommendation: Keep It Running 24/7 on Daily Budget!
* **Peak Indian Impulse Buying Hours:** For digital products and creator education in India, **10:00 PM to 2:00 AM** and **7:00 AM to 9:30 AM** produce some of the cheapest conversions. People scroll Instagram Reels in bed and make quick ₹249 impulse purchases via UPI.
* Restricting hours artificially prevents Meta's auction from bidding when competition is low and ad space is cheapest. Let Meta run 24/7.

---

## 🛠️ 3. Secret Testing Route (`/kjboavhpoieabpraegnaln`)

* **URL:** `https://www.personalabs.store/kjboavhpoieabpraegnaln`
* **Test Pricing:**
  * **Rupees (`INR`):** Base Kit = **₹5**, Order Bump #1 = **+₹5**, Order Bump #2 = **+₹5**
  * **Dollars (`USD`):** Base Kit = **$1**, Order Bump #1 = **+$1**, Order Bump #2 = **+$1**
* **Features:**
  * Dedicated on-screen toggle to switch between **Rupees (Razorpay)** and **Dollars (PayPal)**.
  * Real payment execution: testing verifies Razorpay / PayPal receipt, Google Sheets logging, and Google Drive auto-whitelisting.
* **How to Enable / Disable:**
  * In `app.js` (around line 1810):
    ```javascript
    testSandboxPage: {
      slug: 'kjboavhpoieabpraegnaln',
      enabled: false // Change to false to disable and redirect all visits to '/'
    }
    ```

---

## 📊 4. The 24-to-48 Hour Ad Monitoring Playbook

Once the campaign changes from **`Preparing`** → **`In Review`** → **`Active` (Green Dot)**:

### Rule 1: Do Not Touch the Campaign for the First 24 Hours
* Meta enters the **Learning Phase**. Every time you edit the ad set, budget, or targeting, the learning resets. Let it spend the first ₹300 untouched.

### Rule 2: Key Metrics to Track in Ads Manager

| Metric | Target Benchmark | What It Means | Action to Take |
| :--- | :--- | :--- | :--- |
| **Outbound CTR** | **`> 1.2%`** | Strong hook, viewers are clicking through to the site. | Creative is a winner. Keep running. |
| **Cost Per Link Click (CPC)** | **`< ₹5.00`** | Cheap, targeted Indian creator traffic. | Healthy ad auction performance. |
| **Cost Per Initiate Checkout** | **`< ₹40 – ₹60`** | Visitors are entering name/email/phone on checkout. | Strong intent; check Orders DB for leads. |
| **Cost Per Purchase (CPA)** | **`< ₹120 – ₹150`** | Profitable customer acquisition against ₹249+ cart. | Scale daily budget by **+25%**. |

---

### Rule 3: Recovering Initiated Checkouts (Free Immediate Revenue)
1. Open your Google Sheet: **`PersonaLabs Academy — Orders DB`**.
2. Look for any rows highlighted in **Yellow** (`INITIATED_CHECKOUT`).
3. These are real people who clicked your ad, typed their Name, Phone, and Email, but dropped off before paying UPI.
4. Send them a polite WhatsApp message within 2–4 hours:
   > *"Hey [Name]! Saw you were checking out the AI Influencer Launch Kit on PersonaLabs Academy. Did your UPI payment go through okay? Here’s the direct access link if you'd like to complete it before the 88% launch discount ends: https://personalabs.store"*
5. **Conversion Rate:** 20–30% of abandoned checkouts in India convert immediately via a single WhatsApp message.

---

### Rule 4: Budget Scaling Strategy
* If your campaign achieves **2 or more purchases** in the first 48 hours at a Cost Per Purchase under ₹150:
  * Increase the daily budget by **+25%** (e.g. from `₹300` to `₹375` or `₹450`).
  * Never double the budget overnight (e.g. ₹300 to ₹1,000) as this resets Meta's learning phase and spikes CPMs.
