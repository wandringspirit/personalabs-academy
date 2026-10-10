# 📊 Google Sheets Real-Time Order & Customer Database Setup

Your website ([`app.js`](file:///C:/Projects/ai-influencer-course-website/app.js)) now has a built-in **Real-Time Google Sheets Order & Lead Logger** (`logOrderToGoogleSheet`).

Every time someone interacts with your checkout, it automatically logs a row into your Google Sheet with **16 columns**:
1. **Timestamp (IST)** (`11 Oct 2026, 01:05:12 AM`)
2. **Order Status** (`PAID_SUCCESS` in **Green** or `INITIATED_CHECKOUT` in **Yellow** so you also capture abandoned cart WhatsApp numbers!)
3. **Order ID** (`ORD-...`)
4. **Transaction ID** (`pay_...` from Razorpay, `PP-...` from PayPal, or `PLA-...`)
5. **Customer Name**
6. **Customer Email**
7. **Customer Phone / WhatsApp** (`+91...` or `+1...`)
8. **Currency** (`INR` or `USD`)
9. **Total Amount Paid** (`249`, `498`, `647`, `9`, `18`, etc.)
10. **Formatted Total** (`₹249`, `$9`, etc.)
11. **Base Course Price** (`249` / `9`)
12. **Bump #1: Uncensored Content Hack** (`YES (+₹249)` or `NO`)
13. **Bump #2: 500+ Viral Reel Hooks** (`YES (+₹149)` or `NO`)
14. **Promo Code Used** (`NONE`, `RIYA10 (-₹25)`, etc.)
15. **Payment Method / Gateway** (`Razorpay UPI/Card (pay_...)`, `PayPal USD (...)`)
16. **Country & Items Summary** (`IN` / `US` + Full list of unlocked items)

---

## ⚡ 2-Minute Setup Instructions (100% Free Forever)

### Step 1: Create a Blank Google Sheet
1. Go to **[sheets.new](https://sheets.new)** (logged into your Google account).
2. Name the spreadsheet: **`PersonaLabs Academy — Orders & Customers DB`**.

### Step 2: Paste the Auto-Formatting Webhook Script
1. Inside your Google Sheet top menu, click **Extensions → Apps Script**.
2. Delete any default `function myFunction() {}` code in `Code.gs` and paste the complete script below:

```javascript
const SHEET_NAME = 'Orders';

const HEADERS = [
  'Timestamp (IST)',
  'Order Status',
  'Order ID',
  'Transaction ID',
  'Customer Name',
  'Customer Email',
  'Customer Phone (WhatsApp)',
  'Currency',
  'Total Paid (Numeric)',
  'Formatted Total',
  'Base Kit Price',
  'Bump #1 (Uncensored Hack)',
  'Bump #2 (500+ Viral Hooks)',
  'Promo Code',
  'Payment Method / Gateway',
  'Offer Tier',
  'Country',
  'Items Purchased',
  'Source Page URL'
];

function ensureSheetAndHeaders() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.getActiveSheet();
    sheet.setName(SHEET_NAME);
  }

  if (sheet.getLastRow() === 0) {
    sheet.appendRow(HEADERS);
    const headerRange = sheet.getRange(1, 1, 1, HEADERS.length);
    headerRange.setBackground('#4a044e');
    headerRange.setFontColor('#ffffff');
    headerRange.setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  return sheet;
}

// Run this once inside Apps Script to auto-create the styled headers!
function setupDatabaseSheet() {
  ensureSheetAndHeaders();
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    const sheet = ensureSheetAndHeaders();
    const data = JSON.parse(e.postData.contents || '{}');

    const row = [
      data.timestampIST || new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }),
      data.status || 'PAID_SUCCESS',
      data.orderId || '',
      data.transactionId || '',
      data.customerName || '',
      data.customerEmail || '',
      "'" + (data.customerPhone || ''), // Prefix with ' so Google Sheets doesn't treat +91 as a math formula
      data.currency || 'INR',
      Number(data.totalPaid || 0),
      data.formattedTotal || '',
      Number(data.basePrice || 0),
      data.bump1_UncensoredHack || 'NO',
      data.bump2_ViralHooksPack || 'NO',
      data.promoCode || 'NONE',
      data.paymentMethod || '',
      data.offerTier || '',
      data.visitorCountry || '',
      data.itemsSummary || '',
      data.pageUrl || ''
    ];

    sheet.appendRow(row);
    const lastRow = sheet.getLastRow();
    const rowRange = sheet.getRange(lastRow, 1, 1, HEADERS.length);

    // Auto color-code row: Green for PAID_SUCCESS, Soft Yellow for INITIATED_CHECKOUT (Lead)
    if (data.status === 'PAID_SUCCESS') {
      rowRange.setBackground('#dcfce7');
    } else if (data.status === 'INITIATED_CHECKOUT') {
      rowRange.setBackground('#fef9c3');
    }

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true, row: lastRow }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}
```

### Step 3: Deploy as Web App & Copy the URL
1. At the top of Apps Script, select `setupDatabaseSheet` from the function dropdown next to **Run**, and click **Run** once (grant permission when prompted — click *Advanced → Go to Untitled project (unsafe) → Allow*). Your Google Sheet will immediately get its purple header row!
2. Click the blue **Deploy** button (top right) → **New deployment**.
3. Click the gear icon ⚙️ next to "Select type" → choose **Web app**.
4. Set:
   - **Description:** `PersonaLabs Orders Webhook`
   - **Execute as:** `Me`
   - **Who has access:** **`Anyone`** *(Important so customers' browsers can send order rows without logging into your Google account)*
5. Click **Deploy**, copy the **Web app URL** (`https://script.google.com/macros/s/.../exec`), and share it with me here (or paste it into `googleSheetWebhookUrl` on line 1411 of [`app.js`](file:///C:/Projects/ai-influencer-course-website/app.js))!
