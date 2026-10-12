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
  'Google Drive Access Granted',
  'Automated Recovery Email Status',
  'Automated Add-On Upsell Status'
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
  } else if (sheet.getLastColumn() < HEADERS.length) {
    for (let c = sheet.getLastColumn() + 1; c <= HEADERS.length; c++) {
      sheet.getRange(1, c).setValue(HEADERS[c - 1]).setBackground('#4a044e').setFontColor('#ffffff').setFontWeight('bold');
    }
  }
  return sheet;
}

// Run this once inside Apps Script to auto-create headers & authorize DriveApp, GmailApp and Triggers!
function setupDatabaseSheet() {
  ensureSheetAndHeaders();
  if (CORE_FOLDER_ID) DriveApp.getFolderById(CORE_FOLDER_ID).getName();
  setupAutomatedEmailTriggers();
}

// =========================================================================
// 1. AUTOMATED 25-MIN ABANDONED CART RECOVERY (Safely skips anyone who buys within 25 mins)
// =========================================================================
function sendAbandonedCartRecoveryEmails() {
  const sheet = ensureSheetAndHeaders();
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return;

  const now = new Date();
  const MIN_DELAY_MINUTES = 25; // Waits 25 mins: Anyone who buys 5, 10, or 15 mins later is 100% skipped!

  // Build list of all customer emails that have successfully paid
  const paidEmails = new Set();
  for (let i = 1; i < data.length; i++) {
    const status = String(data[i][1] || '').trim().toUpperCase();
    const email = String(data[i][5] || '').trim().toLowerCase();
    if (status === 'PAID_SUCCESS' && email) {
      paidEmails.add(email);
    }
  }

  for (let i = 1; i < data.length; i++) {
    const rowNum = i + 1;
    const status = String(data[i][1] || '').trim().toUpperCase();
    const customerName = String(data[i][4] || 'Creator').trim();
    const buyerEmail = String(data[i][5] || '').trim().toLowerCase();
    const rowDateStr = String(data[i][0] || '');
    const emailStatus = String(data[i][20] || '').trim();

    if (status !== 'INITIATED_CHECKOUT') continue;
    if (!buyerEmail || !buyerEmail.includes('@')) continue;

    // If they bought later (even 15 mins later), skip them!
    if (paidEmails.has(buyerEmail)) {
      if (!emailStatus) sheet.getRange(rowNum, 21).setValue('SKIPPED (Purchased Course)');
      continue;
    }
    if (emailStatus && emailStatus.startsWith('SENT')) continue;

    // Check if at least 25 minutes have passed
    const rowTime = new Date(rowDateStr);
    const elapsedMinutes = !isNaN(rowTime.getTime()) ? (now.getTime() - rowTime.getTime()) / (1000 * 60) : 999;
    if (elapsedMinutes < MIN_DELAY_MINUTES) continue;

    try {
      const subject = `Your AI Influencer Launch Kit link (+ 88% Launch Discount Reserved)`;
      const htmlBody = `
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 580px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 16px; background-color: #ffffff; color: #1e293b;">
          <div style="text-align: center; margin-bottom: 20px;">
            <span style="background: linear-gradient(135deg, #e65ce4, #ec4899); color: #ffffff; padding: 6px 14px; border-radius: 9999px; font-weight: bold; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; display: inline-block;">PersonaLabs Academy</span>
            <h2 style="font-size: 20px; font-weight: 800; margin-top: 14px; color: #0f172a; margin-bottom: 6px;">Did your payment go through okay?</h2>
            <p style="font-size: 13px; color: #64748b; margin: 0;">We reserved your ₹249 Fast-Action Launch Offer</p>
          </div>
          <p style="font-size: 14px; line-height: 1.6;">Hi <strong>${customerName}</strong>,</p>
          <p style="font-size: 14px; line-height: 1.6;">We noticed you started setting up your access to the <strong>AI Influencer Accelerator (5-Day Launch Kit)</strong>, but your checkout was not completed.</p>
          <p style="font-size: 14px; line-height: 1.6;">Everything inside is waiting for you with zero waiting or subscription charges:</p>
          <ul style="font-size: 13px; line-height: 1.7; padding-left: 20px; color: #334155;">
            <li>✔ <strong>18 Step-by-Step HD Video Lessons</strong> (Runs 100% on Android & iOS mobile)</li>
            <li>✔ <strong>250+ Character DNA & Face-Lock Prompts</strong> (Consistent face across all reels)</li>
            <li>✔ <strong>Automated ManyChat Auto-DM Funnel Templates</strong></li>
            <li>✔ <strong>Instant Google Drive & Portal Access</strong></li>
          </ul>
          <div style="text-align: center; margin: 26px 0;">
            <a href="https://personalabs.store" style="background: linear-gradient(135deg, #e65ce4, #ec4899); color: #ffffff; padding: 14px 28px; border-radius: 12px; font-weight: 800; text-decoration: none; font-size: 14px; display: inline-block; box-shadow: 0 4px 14px rgba(230, 92, 228, 0.35);">
              Complete Enrollment for ₹249 →
            </a>
          </div>
          <p style="font-size: 12px; color: #64748b; line-height: 1.5; text-align: center; border-top: 1px solid #f1f5f9; padding-top: 16px; margin-top: 20px;">
            If your UPI payment already went through or you need direct support, simply reply to this email and our team will assist you immediately.
          </p>
        </div>
      `;

      GmailApp.sendEmail(buyerEmail, subject, `Hi ${customerName}, complete your enrollment at https://personalabs.store`, {
        name: 'PersonaLabs Academy',
        htmlBody: htmlBody
      });

      const sentTime = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
      sheet.getRange(rowNum, 21).setValue(`SENT (${sentTime})`).setBackground('#e0e7ff');
    } catch (err) {
      sheet.getRange(rowNum, 21).setValue(`ERR (${err.message})`);
    }
  }
}

// =========================================================================
// 2. AUTOMATED POST-PURCHASE ADD-ON UPGRADE (Emails buyers who missed the add-ons after 12h)
// =========================================================================
function sendPostPurchaseAddonUpsellEmails() {
  const sheet = ensureSheetAndHeaders();
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return;

  const now = new Date();
  const MIN_HOURS_AFTER_PURCHASE = 12; // Send 12 to 24 hours after they enroll in the core course

  // Track what each email owns across all purchase rows
  const ownedAddons = {};
  for (let i = 1; i < data.length; i++) {
    const status = String(data[i][1] || '').trim().toUpperCase();
    const email = String(data[i][5] || '').trim().toLowerCase();
    if (status === 'PAID_SUCCESS' && email) {
      if (!ownedAddons[email]) ownedAddons[email] = { bump1: false, bump2: false };
      if (String(data[i][11] || '').toUpperCase().startsWith('YES')) ownedAddons[email].bump1 = true;
      if (String(data[i][12] || '').toUpperCase().startsWith('YES')) ownedAddons[email].bump2 = true;
    }
  }

  for (let i = 1; i < data.length; i++) {
    const rowNum = i + 1;
    const status = String(data[i][1] || '').trim().toUpperCase();
    const customerName = String(data[i][4] || 'Creator').trim();
    const buyerEmail = String(data[i][5] || '').trim().toLowerCase();
    const rowDateStr = String(data[i][0] || '');
    const upsellStatus = String(data[i][21] || '').trim();

    if (status !== 'PAID_SUCCESS') continue;
    if (!buyerEmail || !buyerEmail.includes('@')) continue;
    if (upsellStatus && upsellStatus.startsWith('SENT')) continue;

    const userHas = ownedAddons[buyerEmail] || { bump1: false, bump2: false };
    // If they already bought BOTH add-ons, nothing to upsell!
    if (userHas.bump1 && userHas.bump2) {
      if (!upsellStatus) sheet.getRange(rowNum, 22).setValue('SKIPPED (Owns All Add-Ons)');
      continue;
    }

    // Wait at least 12 hours after initial course purchase
    const rowTime = new Date(rowDateStr);
    const elapsedHours = !isNaN(rowTime.getTime()) ? (now.getTime() - rowTime.getTime()) / (1000 * 60 * 60) : 999;
    if (elapsedHours < MIN_HOURS_AFTER_PURCHASE) continue;

    // Send 1-click upgrade email
    try {
      let upgradeHeadline = 'Exclusive Student VIP Upgrades for Your AI Influencer Kit';
      let upgradeCardsHtml = '';

      if (!userHas.bump1) {
        upgradeCardsHtml += `
          <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; margin-bottom: 12px; text-align: left;">
            <div style="font-weight: 800; font-size: 14px; color: #0f172a;">1. Uncensored Content Hack (+4 Exclusive NSFW Videos)</div>
            <p style="font-size: 12px; color: #475569; margin: 4px 0 10px 0;">How top creators structure high-curiosity content safely + 4 private NSFW video files on Google Drive.</p>
            <a href="https://personalabs.store/?upgrade=bump1" style="background-color: #0f172a; color: #ffffff; padding: 8px 16px; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 12px; display: inline-block;">
              Unlock VIP Hack for +₹249 →
            </a>
          </div>
        `;
      }

      if (!userHas.bump2) {
        upgradeCardsHtml += `
          <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 16px; margin-bottom: 12px; text-align: left;">
            <div style="font-weight: 800; font-size: 14px; color: #0f172a;">2. 500+ Viral Reel Hooks & ManyChat Auto-DM Pack</div>
            <p style="font-size: 12px; color: #475569; margin: 4px 0 10px 0;">500+ copy-paste high-retention reel hooks and comment-to-DM automation scripts that sell 24/7.</p>
            <a href="https://personalabs.store/?upgrade=bump2" style="background-color: #0f172a; color: #ffffff; padding: 8px 16px; border-radius: 8px; font-weight: bold; text-decoration: none; font-size: 12px; display: inline-block;">
              Unlock 500+ Hooks Pack for +₹149 →
            </a>
          </div>
        `;
      }

      const htmlBody = `
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 580px; margin: 0 auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 16px; background-color: #ffffff; color: #1e293b;">
          <div style="text-align: center; margin-bottom: 20px;">
            <span style="background: linear-gradient(135deg, #e65ce4, #ec4899); color: #ffffff; padding: 6px 14px; border-radius: 9999px; font-weight: bold; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; display: inline-block;">PersonaLabs Academy • Student Perks</span>
            <h2 style="font-size: 20px; font-weight: 800; margin-top: 14px; color: #0f172a; margin-bottom: 6px;">${upgradeHeadline}</h2>
            <p style="font-size: 13px; color: #64748b; margin: 0;">Special add-on access reserved for enrolled students</p>
          </div>
          <p style="font-size: 14px; line-height: 1.6;">Hi <strong>${customerName}</strong>,</p>
          <p style="font-size: 14px; line-height: 1.6;">Hope you are enjoying the AI Influencer Accelerator! We noticed you opted out of the optional add-ons during your enrollment.</p>
          <p style="font-size: 14px; line-height: 1.6;">As an enrolled student, you can add them to your portal and Google Drive anytime at your original student discount:</p>
          ${upgradeCardsHtml}
          <p style="font-size: 12px; color: #64748b; line-height: 1.5; text-align: center; border-top: 1px solid #f1f5f9; padding-top: 16px; margin-top: 20px;">
            These upgrade links automatically connect to your existing account so your Google Drive access is updated immediately upon payment.
          </p>
        </div>
      `;

      GmailApp.sendEmail(buyerEmail, `Student Upgrade: Complete Your AI Influencer Toolkit`, `Hi ${customerName}, upgrade your student toolkits at https://personalabs.store`, {
        name: 'PersonaLabs Academy',
        htmlBody: htmlBody
      });

      const sentTime = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
      sheet.getRange(rowNum, 22).setValue(`SENT (${sentTime})`).setBackground('#fef08a');
    } catch (err) {
      sheet.getRange(rowNum, 22).setValue(`ERR (${err.message})`);
    }
  }
}

// Creates the automatic recurring triggers in Apps Script (Cart Recovery every 15m + Addon Upsell every 2h)
function setupAutomatedEmailTriggers() {
  const triggers = ScriptApp.getProjectTriggers();
  let hasCartTrigger = false;
  let hasUpsellTrigger = false;

  for (let i = 0; i < triggers.length; i++) {
    const fn = triggers[i].getHandlerFunction();
    if (fn === 'sendAbandonedCartRecoveryEmails') hasCartTrigger = true;
    if (fn === 'sendPostPurchaseAddonUpsellEmails') hasUpsellTrigger = true;
  }

  if (!hasCartTrigger) {
    ScriptApp.newTrigger('sendAbandonedCartRecoveryEmails')
      .timeBased()
      .everyMinutes(15)
      .create();
  }

  if (!hasUpsellTrigger) {
    ScriptApp.newTrigger('sendPostPurchaseAddonUpsellEmails')
      .timeBased()
      .everyHours(2)
      .create();
  }
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
