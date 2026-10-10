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

      // OPTIONAL DRM: Auto-whitelist buyer's Gmail on your Restricted Google Drive folders!
      // Paste your 3 Google Drive Folder IDs below once uploaded from your Brand Gmail account:
      const CORE_FOLDER_ID = '';   // Folder 01: 01-Core-Course-Videos
      const NSFW_FOLDER_ID = '';   // Folder 02: 02-Uncensored-NSFW-Addon-Videos (Bump #1)
      const HOOKS_FOLDER_ID = '';  // Folder 03: 03-500-Viral-Hooks-And-Prompts-Pack (Bump #2)
      const buyerEmail = String(data.customerEmail || '').trim();

      if (buyerEmail && buyerEmail.includes('@')) {
        try {
          if (CORE_FOLDER_ID) DriveApp.getFolderById(CORE_FOLDER_ID).addViewer(buyerEmail);
          if (NSFW_FOLDER_ID && String(data.bump1_UncensoredHack || '').startsWith('YES')) {
            DriveApp.getFolderById(NSFW_FOLDER_ID).addViewer(buyerEmail);
          }
          if (HOOKS_FOLDER_ID && String(data.bump2_ViralHooksPack || '').startsWith('YES')) {
            DriveApp.getFolderById(HOOKS_FOLDER_ID).addViewer(buyerEmail);
          }
        } catch (driveErr) {}
      }
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

// Server-side verification endpoint called by course-vault/index.html (?action=verify&email=...)
function doGet(e) {
  try {
    const params = (e && e.parameter) || {};
    if (params.action === 'verify' && params.email) {
      const targetEmail = String(params.email).trim().toLowerCase();
      const sheet = ensureSheetAndHeaders();
      const rows = sheet.getDataRange().getValues();
      let bump1 = false;
      let bump2 = false;
      let verified = false;

      for (let i = 1; i < rows.length; i++) {
        const status = String(rows[i][1] || '');
        const rowEmail = String(rows[i][5] || '').trim().toLowerCase();
        if (status === 'PAID_SUCCESS' && rowEmail === targetEmail) {
          verified = true;
          if (String(rows[i][11] || '').toUpperCase().startsWith('YES')) bump1 = true;
          if (String(rows[i][12] || '').toUpperCase().startsWith('YES')) bump2 = true;
        }
      }

      return ContentService
        .createTextOutput(JSON.stringify({
          ok: verified,
          bump1: bump1,
          bump2: bump2,
          nsfwDriveUrl: bump1 ? 'https://drive.google.com/drive/folders/YOUR_NSFW_FOLDER_ID' : ''
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }
    return ContentService
      .createTextOutput(JSON.stringify({ ok: true, service: 'PersonaLabs Orders DB' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
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
