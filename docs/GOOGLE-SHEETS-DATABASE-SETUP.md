# 📊 Google Sheets Real-Time Order & Customer Database Setup (`personalabsacademy@gmail.com`)

Your website ([`app.js`](../app.js)) has a built-in **Real-Time Google Sheets Order & Lead Logger** (`logOrderToGoogleSheet`) + **Automatic Private Google Drive Whitelisting** (`DriveApp.addViewer`).

Every time someone interacts with your checkout, it automatically logs a row into your Google Sheet under **`personalabsacademy@gmail.com`** with **20 columns** and automatically grants **Google Drive Viewer access** to the buyer's Gmail for the exact folders they purchased!

---

## ⚡ 60-Second Setup Under `personalabsacademy@gmail.com`

### Step 1: Create a Blank Google Sheet in `personalabsacademy@gmail.com`
1. Make sure you are signed into Chrome as **`personalabsacademy@gmail.com`**.
2. Go to **[sheets.new](https://sheets.new)**.
3. Name the spreadsheet: **`PersonaLabs Academy — Orders DB`**.

### Step 2: Paste the Pre-Configured Apps Script (All 3 Folder IDs Already Filled In!)
1. Inside your new Google Sheet top menu, click **Extensions → Apps Script**.
2. Delete any default `function myFunction() {}` code in `Code.gs` and paste the complete script below:

```javascript
const SHEET_ID   = '1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc';
const SHEET_NAME = 'Orders';

// Pre-configured with your 3 Google Drive Folder IDs under personalabsacademy@gmail.com:
const CORE_FOLDER_ID  = '1QaLzvcaA2QyJI9uqO1AoRqhKz6uTLHwm'; // 01-Core-Course-Videos
const NSFW_FOLDER_ID  = '10HGXWcRMR898lbQnTX41G--fPLKoBOvW'; // 02-Uncensored-NSFW-Addon-Videos (Bump #1)
const HOOKS_FOLDER_ID = '1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN'; // 03-500-Viral-Hooks-And-Prompts-Pack (Bump #2)

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
  'Source Page URL',
  'Google Drive Access Granted'
];

function ensureSheetAndHeaders() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.getSheets()[0];
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

// Run this once inside Apps Script to auto-create the styled headers & authorize DriveApp!
function setupDatabaseSheet() {
  ensureSheetAndHeaders();
  if (CORE_FOLDER_ID) DriveApp.getFolderById(CORE_FOLDER_ID).getName();
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    const sheet = ensureSheetAndHeaders();
    const data = JSON.parse(e.postData.contents || '{}');

    let driveGrantedList = [];
    const buyerEmail = String(data.customerEmail || '').trim();
    const isPaid = data.status === 'PAID_SUCCESS';

    if (isPaid && buyerEmail && buyerEmail.includes('@')) {
      const wantCore  = data.grantCoreDrive !== false;
      const wantNsfw  = Boolean(data.grantNsfwDrive) || String(data.bump1_UncensoredHack || '').toUpperCase().startsWith('YES');
      const wantHooks = Boolean(data.grantHooksDrive) || String(data.bump2_ViralHooksPack || '').toUpperCase().startsWith('YES');

      if (wantCore && CORE_FOLDER_ID) {
        try {
          DriveApp.getFolderById(CORE_FOLDER_ID).addViewer(buyerEmail);
          driveGrantedList.push('01-Core');
        } catch (err) {
          driveGrantedList.push('01-Core-ERR');
        }
      }
      if (wantNsfw && NSFW_FOLDER_ID) {
        try {
          DriveApp.getFolderById(NSFW_FOLDER_ID).addViewer(buyerEmail);
          driveGrantedList.push('02-NSFW');
        } catch (err) {
          driveGrantedList.push('02-NSFW-ERR');
        }
      }
      if (wantHooks && HOOKS_FOLDER_ID) {
        try {
          DriveApp.getFolderById(HOOKS_FOLDER_ID).addViewer(buyerEmail);
          driveGrantedList.push('03-Hooks');
        } catch (err) {
          driveGrantedList.push('03-Hooks-ERR');
        }
      }
    }

    const row = [
      data.timestampIST || new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' }),
      data.status || 'PAID_SUCCESS',
      data.orderId || '',
      data.transactionId || '',
      data.customerName || '',
      buyerEmail,
      "'" + (data.customerPhone || ''),
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
      data.pageUrl || '',
      isPaid ? (driveGrantedList.join(', ') || 'None') : 'PENDING'
    ];

    sheet.appendRow(row);
    const lastRow = sheet.getLastRow();
    const rowRange = sheet.getRange(lastRow, 1, 1, HEADERS.length);

    if (isPaid) {
      rowRange.setBackground('#dcfce7'); // Green for verified paid orders
    } else if (data.status === 'INITIATED_CHECKOUT') {
      rowRange.setBackground('#fef9c3'); // Yellow for initiated checkout leads
    }

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true, row: lastRow, driveGranted: driveGrantedList }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// Server-side verification endpoint called by course-vault/index.html (?action=verify) & Sign-In modal (?action=lookupOrder)
function doGet(e) {
  try {
    const params = (e && e.parameter) || {};
    const action = params.action || '';
    const targetEmail = String(params.email || '').trim().toLowerCase();

    if ((action === 'verify' || action === 'lookupOrder') && targetEmail) {
      const sheet = ensureSheetAndHeaders();
      const rows = sheet.getDataRange().getValues();
      let bump1 = false;
      let bump2 = false;
      let verified = false;
      let lastTxId = '';

      for (let i = 1; i < rows.length; i++) {
        const status = String(rows[i][1] || '');
        const txId   = String(rows[i][3] || '').trim();
        const rowEmail = String(rows[i][5] || '').trim().toLowerCase();
        if (status === 'PAID_SUCCESS' && rowEmail === targetEmail && txId && !txId.startsWith('PLA-')) {
          verified = true;
          lastTxId = txId;
          if (String(rows[i][11] || '').toUpperCase().startsWith('YES')) bump1 = true;
          if (String(rows[i][12] || '').toUpperCase().startsWith('YES')) bump2 = true;
        }
      }

      return ContentService
        .createTextOutput(JSON.stringify({
          ok: verified,
          found: verified,
          transactionId: lastTxId,
          bump1: bump1,
          bump2: bump2,
          nsfwDriveUrl: bump1 ? 'https://drive.google.com/drive/folders/10HGXWcRMR898lbQnTX41G--fPLKoBOvW?usp=sharing' : '',
          hooksDriveUrl: bump2 ? 'https://drive.google.com/drive/folders/1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN?usp=sharing' : ''
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }
    return ContentService
      .createTextOutput(JSON.stringify({ ok: true, service: 'PersonaLabs Orders DB (personalabsacademy@gmail.com)' }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
```

### Step 3: Run `setupDatabaseSheet` & Deploy as Web App
1. At the top of Apps Script, select **`setupDatabaseSheet`** from the dropdown next to **Run**, and click **Run** once.
2. When Google prompts for permission, click **Review permissions → Choose `personalabsacademy@gmail.com` → Advanced → Go to Untitled project (unsafe) → Allow** *(this authorizes both Google Sheets and Google Drive `addViewer`!)*.
3. Click the blue **Deploy** button (top right) → **New deployment**:
   - Click the gear icon ⚙️ next to *Select type* → choose **Web app**.
   - **Execute as:** `Me (personalabsacademy@gmail.com)`
   - **Who has access:** **`Anyone`**
4. Click **Deploy**, copy the **`Web app URL`** (`https://script.google.com/macros/s/.../exec`), and paste it in chat so we update `googleSheetWebhookUrl` in [`app.js`](../app.js) and [`course-vault/index.html`](../course-vault/index.html)!
