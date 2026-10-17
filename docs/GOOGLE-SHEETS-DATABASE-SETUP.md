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
const SHEET_ID          = '1Sy8fyVC84tfgognGzGbJl0cSuIq5WFGgL8HoPzjGElc';
const LOGS_SHEET_NAME   = 'Logs';
const ORDERS_SHEET_NAME = 'Orders';

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

function ensureHeadersOnSheet(sheet) {
  if (!sheet) return;
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
}

/**
 * ONE-CLICK SETUP & BACKFILL FUNCTION
 * Run this once inside Apps Script to:
 * 1. Rename existing sheet to 'Logs'
 * 2. Create clean 'Orders' tab
 * 3. Backfill all 5 verified PAID_SUCCESS orders from Logs to Orders
 */
function setupAndBackfillOrders() {
  const ss = SpreadsheetApp.openById(SHEET_ID);

  // 1. Ensure Logs sheet exists (rename existing sheet if needed)
  let logsSheet = ss.getSheetByName(LOGS_SHEET_NAME);
  if (!logsSheet) {
    const existingOrders = ss.getSheetByName('Orders');
    if (existingOrders) {
      existingOrders.setName(LOGS_SHEET_NAME);
      logsSheet = existingOrders;
    } else {
      logsSheet = ss.getSheets()[0];
      logsSheet.setName(LOGS_SHEET_NAME);
    }
  }
  ensureHeadersOnSheet(logsSheet);

  // 2. Ensure Orders sheet exists
  let ordersSheet = ss.getSheetByName(ORDERS_SHEET_NAME);
  if (!ordersSheet) {
    ordersSheet = ss.insertSheet(ORDERS_SHEET_NAME);
  }
  ensureHeadersOnSheet(ordersSheet);

  // 3. Backfill all PAID_SUCCESS orders from Logs to Orders (preventing duplicates)
  const logsData = logsSheet.getDataRange().getValues();
  const existingOrdersData = ordersSheet.getDataRange().getValues();
  const existingTxIds = new Set();

  for (let j = 1; j < existingOrdersData.length; j++) {
    const tx = String(existingOrdersData[j][3] || existingOrdersData[j][2] || '').trim();
    if (tx) existingTxIds.add(tx);
  }

  let backfilledCount = 0;
  for (let i = 1; i < logsData.length; i++) {
    const row = logsData[i];
    const status = String(row[1] || '').trim().toUpperCase();
    const txId = String(row[3] || row[2] || '').trim();

    if (status === 'PAID_SUCCESS' && txId && !existingTxIds.has(txId)) {
      ordersSheet.appendRow(row);
      const newRowIdx = ordersSheet.getLastRow();
      ordersSheet.getRange(newRowIdx, 1, 1, HEADERS.length).setBackground('#dcfce7'); // Light green
      existingTxIds.add(txId);
      backfilledCount++;
    }
  }

  // Authorize Drive & Triggers
  if (CORE_FOLDER_ID) {
    try { DriveApp.getFolderById(CORE_FOLDER_ID).getName(); } catch (e) {}
  }
  setupAutomatedEmailTriggers();

  Logger.log(`Setup complete! Backfilled ${backfilledCount} orders into Orders sheet.`);
  return `Success! Logs and Orders sheets configured. Backfilled ${backfilledCount} paid orders into Orders tab.`;
}

// Legacy alias
function setupDatabaseSheet() {
  setupAndBackfillOrders();
}

// =========================================================================
// 1. AUTOMATED 25-MIN ABANDONED CART RECOVERY (Safely skips anyone who buys within 25 mins)
// =========================================================================
function sendAbandonedCartRecoveryEmails() {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  const logsSheet = ss.getSheetByName(LOGS_SHEET_NAME) || ss.getSheets()[0];
  const ordersSheet = ss.getSheetByName(ORDERS_SHEET_NAME);
  const data = logsSheet.getDataRange().getValues();
  if (data.length <= 1) return;

  const now = new Date();
  const MIN_DELAY_MINUTES = 25; // Waits 25 mins

  // Build list of all customer emails that have successfully paid (from both sheets)
  const paidEmails = new Set();
  const collectPaid = (sheetObj) => {
    if (!sheetObj) return;
    const rows = sheetObj.getDataRange().getValues();
    for (let i = 1; i < rows.length; i++) {
      const status = String(rows[i][1] || '').trim().toUpperCase();
      const email = String(rows[i][5] || '').trim().toLowerCase();
      if (status === 'PAID_SUCCESS' && email) paidEmails.add(email);
    }
  };
  collectPaid(ordersSheet);
  collectPaid(logsSheet);

  for (let i = 1; i < data.length; i++) {
    const rowNum = i + 1;
    const status = String(data[i][1] || '').trim().toUpperCase();
    const customerName = String(data[i][4] || 'there').trim();
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
      const subject = `Regarding your PersonaLabs enrollment (${customerName})`;
      const plainText = `Hi ${customerName},\n\nWe noticed you started setting up your access to the AI Influencer Accelerator (5-Day Launch Kit), but your checkout wasn't completed.\n\nYour enrollment details are reserved for you at: https://personalabs.store\n\nIncluded:\n- 18 Step-by-Step HD Video Lessons (Runs 100% on Android & iOS)\n- 250+ Character DNA & Face-Lock Prompts\n- ManyChat Auto-DM Funnel Templates\n- Instant Google Drive & Portal Access\n\nComplete enrollment here: https://personalabs.store\n\nIf you experienced any issues during checkout or have questions, simply reply to this email.\n\nPersonaLabs Academy\nRegistered MSME: UDYAM-UP-43-0208040\nUttar Pradesh, India\nTo manage email preferences, reply with "unsubscribe".`;

      const htmlBody = `
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 560px; margin: 0 auto; padding: 24px; color: #1e293b; background: #ffffff;">
          <p style="font-size: 15px; line-height: 1.6;">Hi ${customerName},</p>
          <p style="font-size: 15px; line-height: 1.6;">We noticed you started setting up your access to the <strong>AI Influencer Accelerator (5-Day Launch Kit)</strong>, but your checkout wasn't completed.</p>
          <p style="font-size: 15px; line-height: 1.6;">Your reserved fast-action enrollment details are ready:</p>
          <ul style="font-size: 14px; line-height: 1.7; color: #334155;">
            <li><strong>18 Step-by-Step HD Video Lessons</strong> (Runs 100% on Android & iOS)</li>
            <li><strong>250+ Character DNA & Face-Lock Prompts</strong></li>
            <li><strong>ManyChat Auto-DM Funnel Templates</strong></li>
            <li><strong>Instant Google Drive & Portal Access</strong></li>
          </ul>
          <p style="margin: 24px 0;">
            <a href="https://personalabs.store" style="background: #0f172a; color: #ffffff; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 14px; display: inline-block;">
              Complete Enrollment →
            </a>
          </p>
          <p style="font-size: 13px; color: #64748b; line-height: 1.6;">If your UPI payment already completed or you experienced any issues during checkout, simply reply directly to this email and we'll assist you immediately.</p>
          <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 28px 0 16px 0;" />
          <p style="font-size: 11px; color: #94a3b8; line-height: 1.5; margin: 0;">
            PersonaLabs Academy • MSME Registration: UDYAM-UP-43-0208040<br/>
            Sector 62, Noida, Uttar Pradesh, India • You received this because an order was initiated on personalabs.store.<br/>
            To unsubscribe or manage email preferences, reply with "unsubscribe".
          </p>
        </div>
      `;

      GmailApp.sendEmail(buyerEmail, subject, plainText, {
        name: 'PersonaLabs Academy',
        htmlBody: htmlBody,
        replyTo: 'personalabsacademy@gmail.com'
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
    const customerName = String(data[i][4] || 'there').trim();
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
      let subject = `[Student Resource] AI Influencer Toolkit Upgrades (${customerName})`;
      let plainText = `Hi ${customerName},\n\nHope you're enjoying the AI Influencer Accelerator!\n\nAs an enrolled student, your original student discount for the add-on toolkits is still active for your account.\n\n`;
      let upgradeCardsHtml = '';

      if (!userHas.bump1) {
        plainText += `- Uncensored Content Hack (+4 Private NSFW Videos): https://personalabs.store/?upgrade=bump1\n`;
        upgradeCardsHtml += `
          <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; text-align: left;">
            <div style="font-weight: 700; font-size: 14px; color: #0f172a;">1. Uncensored Content Hack (+4 Exclusive NSFW Videos)</div>
            <p style="font-size: 13px; color: #475569; margin: 4px 0 12px 0;">Viral curiosity framing and multi-platform monetization + 4 exclusive NSFW video masterclasses.</p>
            <a href="https://personalabs.store/?upgrade=bump1" style="background-color: #0f172a; color: #ffffff; padding: 8px 16px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 13px; display: inline-block;">
              Unlock VIP Hack (+₹249) →
            </a>
          </div>
        `;
      }

      if (!userHas.bump2) {
        plainText += `- 500+ Viral Reel Hooks & Auto-DM Pack: https://personalabs.store/?upgrade=bump2\n`;
        upgradeCardsHtml += `
          <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin-bottom: 12px; text-align: left;">
            <div style="font-weight: 700; font-size: 14px; color: #0f172a;">2. 500+ Viral Reel Hooks & ManyChat Auto-DM Pack</div>
            <p style="font-size: 13px; color: #475569; margin: 4px 0 12px 0;">500+ copy-paste hooks and comment-to-DM automation scripts to monetize followers 24/7.</p>
            <a href="https://personalabs.store/?upgrade=bump2" style="background-color: #0f172a; color: #ffffff; padding: 8px 16px; border-radius: 6px; font-weight: bold; text-decoration: none; font-size: 13px; display: inline-block;">
              Unlock 500+ Hooks Pack (+₹149) →
            </a>
          </div>
        `;
      }

      plainText += `\nIf you have any questions or need student support, reply to this email.\n\nPersonaLabs Academy\nRegistered MSME: UDYAM-UP-43-0208040\nUttar Pradesh, India\nTo manage email preferences, reply with "unsubscribe".`;

      const htmlBody = `
        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; max-width: 560px; margin: 0 auto; padding: 24px; color: #1e293b; background: #ffffff;">
          <p style="font-size: 15px; line-height: 1.6;">Hi ${customerName},</p>
          <p style="font-size: 15px; line-height: 1.6;">Hope you are enjoying the AI Influencer Accelerator! We noticed you opted out of the optional add-ons during your enrollment.</p>
          <p style="font-size: 15px; line-height: 1.6;">As an enrolled student, your original student discount remains reserved for your account:</p>
          ${upgradeCardsHtml}
          <p style="font-size: 13px; color: #64748b; line-height: 1.6;">Upgrading automatically syncs with your registered email and unlocks the folders in your Google Drive immediately.</p>
          <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 28px 0 16px 0;" />
          <p style="font-size: 11px; color: #94a3b8; line-height: 1.5; margin: 0;">
            PersonaLabs Academy • MSME Registration: UDYAM-UP-43-0208040<br/>
            Sector 62, Noida, Uttar Pradesh, India • You received this because you are an enrolled student at personalabs.store.<br/>
            To unsubscribe or manage email preferences, reply with "unsubscribe".
          </p>
        </div>
      `;

      GmailApp.sendEmail(buyerEmail, subject, plainText, {
        name: 'PersonaLabs Academy',
        htmlBody: htmlBody,
        replyTo: 'personalabsacademy@gmail.com'
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
    const ss = SpreadsheetApp.openById(SHEET_ID);
    let logsSheet = ss.getSheetByName(LOGS_SHEET_NAME) || ss.getSheetByName('Sheet1') || ss.getSheets()[0];
    let ordersSheet = ss.getSheetByName(ORDERS_SHEET_NAME);

    ensureHeadersOnSheet(logsSheet);
    if (ordersSheet) ensureHeadersOnSheet(ordersSheet);

    const data = JSON.parse(e.postData.contents || '{}');
    const isPaid = data.status === 'PAID_SUCCESS';
    const buyerEmail = String(data.customerEmail || '').trim();

    let driveGrantedList = [];
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

    // 1. Always append to Logs (Audit trail for CTA clicks, leads, abandoned checkouts)
    logsSheet.appendRow(row);
    const logsLastRow = logsSheet.getLastRow();
    const logsRowRange = logsSheet.getRange(logsLastRow, 1, 1, HEADERS.length);

    if (isPaid) {
      logsRowRange.setBackground('#dcfce7'); // Green for verified paid orders
    } else if (data.status === 'INITIATED_CHECKOUT') {
      logsRowRange.setBackground('#fef9c3'); // Yellow for initiated checkout leads
    }

    // 2. If PAID_SUCCESS, ALSO append to the clean Orders sheet!
    let ordersLastRow = null;
    if (isPaid) {
      if (!ordersSheet) {
        ordersSheet = ss.insertSheet(ORDERS_SHEET_NAME);
        ensureHeadersOnSheet(ordersSheet);
      }
      ordersSheet.appendRow(row);
      ordersLastRow = ordersSheet.getLastRow();
      ordersSheet.getRange(ordersLastRow, 1, 1, HEADERS.length).setBackground('#dcfce7');
    }

    return ContentService
      .createTextOutput(JSON.stringify({
        ok: true,
        logsRow: logsLastRow,
        ordersRow: ordersLastRow,
        driveGranted: driveGrantedList
      }))
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
      const ss = SpreadsheetApp.openById(SHEET_ID);
      // Check Orders sheet first (fastest & cleanest!), fallback to Logs
      const ordersSheet = ss.getSheetByName(ORDERS_SHEET_NAME);
      const logsSheet   = ss.getSheetByName(LOGS_SHEET_NAME) || ss.getSheets()[0];

      let foundRow = null;

      const searchSheet = (sheetObj) => {
        if (!sheetObj) return null;
        const rows = sheetObj.getDataRange().getValues();
        for (let i = rows.length - 1; i >= 1; i--) { // search newest first
          const status = String(rows[i][1] || '').trim().toUpperCase();
          const txId   = String(rows[i][3] || '').trim();
          const rowEmail = String(rows[i][5] || '').trim().toLowerCase();
          if (status === 'PAID_SUCCESS' && rowEmail === targetEmail && txId && !txId.startsWith('PLA-')) {
            return rows[i];
          }
        }
        return null;
      };

      foundRow = searchSheet(ordersSheet) || searchSheet(logsSheet);

      if (foundRow) {
        const bump1 = String(foundRow[11] || '').toUpperCase().startsWith('YES');
        const bump2 = String(foundRow[12] || '').toUpperCase().startsWith('YES');
        return ContentService
          .createTextOutput(JSON.stringify({
            ok: true,
            found: true,
            transactionId: String(foundRow[3] || '').trim(),
            bump1: bump1,
            bump2: bump2,
            nsfwDriveUrl: bump1 ? 'https://drive.google.com/drive/folders/10HGXWcRMR898lbQnTX41G--fPLKoBOvW?usp=sharing' : '',
            hooksDriveUrl: bump2 ? 'https://drive.google.com/drive/folders/1IId4demuyfYX8g1jYVZpngoo6m-Sf1oN?usp=sharing' : ''
          }))
          .setMimeType(ContentService.MimeType.JSON);
      } else {
        return ContentService
          .createTextOutput(JSON.stringify({ ok: false, found: false, error: 'No active paid enrollment found for this email' }))
          .setMimeType(ContentService.MimeType.JSON);
      }
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
