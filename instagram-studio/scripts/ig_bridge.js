const http = require('http');
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

const ROOT = 'C:/Projects/ai-influencer-course-website/instagram-studio';

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Private-Network', 'true');
  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }
  const u = new URL(req.url, 'http://127.0.0.1:8766');
  const rel = u.searchParams.get('file') || '';
  const f = path.join(ROOT, rel);
  if (fs.existsSync(f) && fs.statSync(f).isFile()) {
    const b64 = fs.readFileSync(f).toString('base64');
    res.writeHead(200, { 'Content-Type': 'application/javascript' });
    res.end(`window.__fileData = window.__fileData || {}; window.__fileData[${JSON.stringify(rel)}] = ${JSON.stringify(b64)};`);
  } else {
    res.writeHead(404);
    res.end('Not found');
  }
});

server.on('upgrade', (req, socket) => {
  const key = req.headers['sec-websocket-key'];
  if (!key) {
    socket.destroy();
    return;
  }
  const accept = crypto
    .createHash('sha1')
    .update(key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11')
    .digest('base64');
  socket.write(
    'HTTP/1.1 101 Switching Protocols\r\n' +
    'Upgrade: websocket\r\n' +
    'Connection: Upgrade\r\n' +
    `Sec-WebSocket-Accept: ${accept}\r\n\r\n`
  );

  const u = new URL(req.url, 'http://localhost:8766');
  const rel = u.searchParams.get('file') || '';
  const f = path.join(ROOT, rel);
  let payload = Buffer.from('ERROR:NOT_FOUND');
  if (fs.existsSync(f) && fs.statSync(f).isFile()) {
    payload = fs.readFileSync(f); // raw binary frame
  }

  // Send binary WebSocket frame (opcode 0x82)
  const len = payload.length;
  let header;
  if (len < 126) {
    header = Buffer.alloc(2);
    header[0] = 0x82;
    header[1] = len;
  } else if (len < 65536) {
    header = Buffer.alloc(4);
    header[0] = 0x82;
    header[1] = 126;
    header.writeUInt16BE(len, 2);
  } else {
    header = Buffer.alloc(10);
    header[0] = 0x82;
    header[1] = 127;
    header.writeBigUInt64BE(BigInt(len), 2);
  }
  socket.write(Buffer.concat([header, payload]), () => {
    // Also send close frame after data flushed
    const closeFrame = Buffer.from([0x88, 0x00]);
    socket.end(closeFrame);
  });
});

server.listen(8766, '127.0.0.1', () => {
  console.log('WS + HTTP bridge listening on 127.0.0.1:8766');
});
