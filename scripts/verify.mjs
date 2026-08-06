// Migration check suite. Runs the 12 checks from the migration brief against
// a local build (default) or a deployed URL (--base https://...).
//
//   npm run verify                  build, serve dist/, check
//   npm run verify -- --base URL    check a deployed site (skips build/serve)
import { execSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import { chromium } from 'playwright';
import { PNG } from 'pngjs';
import pixelmatch from 'pixelmatch';
import {
  SLUGS,
  VIEWPORTS,
  pageList,
  newUrl,
  stabilise,
  captureText,
} from './lib/capture.mjs';

const argBase = (() => {
  const i = process.argv.indexOf('--base');
  return i >= 0 ? process.argv[i + 1].replace(/\/$/, '') : null;
})();

const BASELINE = '.migration/baseline';
const CURRENT = '.migration/current';
fs.mkdirSync(CURRENT, { recursive: true });

const results = [];
let server = null;
function record(id, name, pass, detail = '') {
  results.push({ id, name, pass, detail });
  const mark = pass === true ? 'PASS' : pass === 'skip' ? 'SKIP' : 'FAIL';
  console.log(`  [${mark}] ${id}. ${name}${detail ? ' — ' + detail : ''}`);
}

// ── Check 1: build ─────────────────────────────────────────────
let buildOut = '';
if (!argBase) {
  console.log('Building...');
  try {
    buildOut = execSync('npx astro build 2>&1', { encoding: 'utf8' });
    const warnings = buildOut
      .split('\n')
      .filter((l) => /\[WARN\]|warning/i.test(l) && !/deprecat/i.test(l));
    if (warnings.length) {
      record(1, 'Build', false, 'warnings: ' + warnings.slice(0, 3).join(' | '));
    } else {
      record(1, 'Build', true);
    }
  } catch (e) {
    record(1, 'Build', false, String(e.stdout || e.message).slice(-600));
    finish();
  }
} else {
  record(1, 'Build', 'skip', 'verifying deployed URL');
}

// ── Serve dist/ ────────────────────────────────────────────────
const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.mjs': 'text/javascript',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.xml': 'application/xml',
  '.txt': 'text/plain',
  '.skill': 'application/octet-stream',
};
let base = argBase;
if (!base) {
  server = http.createServer((req, res) => {
    let p = decodeURIComponent(new URL(req.url, 'http://x').pathname);
    let file = path.join('dist', p);
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) {
      file = path.join(file, 'index.html');
    }
    if (!fs.existsSync(file)) {
      const nf = path.join('dist', '404.html');
      res.writeHead(404, { 'content-type': 'text/html; charset=utf-8' });
      res.end(fs.existsSync(nf) ? fs.readFileSync(nf) : 'not found');
      return;
    }
    res.writeHead(200, {
      'content-type': MIME[path.extname(file)] || 'application/octet-stream',
    });
    res.end(fs.readFileSync(file));
  });
  await new Promise((res) => server.listen(4173, res));
  base = 'http://localhost:4173';
}

async function head(url) {
  try {
    const r = await fetch(url, { method: 'GET' });
    return { status: r.status, len: (await r.arrayBuffer()).byteLength };
  } catch (e) {
    return { status: 0, len: 0, err: String(e) };
  }
}

// ── Check 2: routes ────────────────────────────────────────────
{
  const bad = [];
  for (const name of pageList()) {
    const { status } = await head(newUrl(base, name));
    if (status !== 200) bad.push(`${name}:${status}`);
  }
  record(2, 'Routes', bad.length === 0, bad.join(', '));
}

// ── Check 3: slugs frozen ──────────────────────────────────────
{
  let built = [];
  if (!argBase) {
    built = fs
      .readdirSync('dist/writing', { withFileTypes: true })
      .filter((d) => d.isDirectory())
      .map((d) => d.name);
  } else {
    // Remote: collect /writing/<slug>/ links from the writing index.
    const html = await (await fetch(`${base}/writing/`)).text();
    built = [...new Set([...html.matchAll(/href="\/writing\/([\w-]+)\//g)].map((m) => m[1]))];
  }
  const extra = built.filter((s) => !SLUGS.includes(s));
  const missing = SLUGS.filter((s) => !built.includes(s));
  record(
    3,
    'Slugs',
    extra.length === 0 && missing.length === 0,
    [extra.length ? 'extra: ' + extra : '', missing.length ? 'missing: ' + missing : '']
      .filter(Boolean)
      .join('; ')
  );
}

// ── Browser-based checks ───────────────────────────────────────
const browser = await chromium.launch();
const consoleErrors = {}; // page -> [msgs]
const textFail = [];
const visualFail = [];
const linkTargets = new Set();
const imgTargets = new Set();
const metaByPage = {};

for (const name of pageList()) {
  consoleErrors[name] = [];
  for (const width of VIEWPORTS) {
    const context = await browser.newContext({
      viewport: { width, height: 900 },
      deviceScaleFactor: 1,
      reducedMotion: 'reduce',
    });
    const page = await context.newPage();
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors[name].push(msg.text());
    });
    page.on('pageerror', (err) => consoleErrors[name].push(String(err)));
    await page.goto(newUrl(base, name), { waitUntil: 'networkidle' });
    await stabilise(page);
    await page.screenshot({ path: path.join(CURRENT, `${name}-${width}.png`), fullPage: true });

    if (width === VIEWPORTS[0]) {
      // Text vs baseline
      const text = await captureText(page);
      const baseText = fs
        .readFileSync(path.join(BASELINE, 'text', `${name}.txt`), 'utf8')
        .trim();
      if (text.trim() !== baseText) {
        const a = baseText.split('\n');
        const b = text.trim().split('\n');
        let i = 0;
        while (i < a.length && i < b.length && a[i] === b[i]) i++;
        textFail.push(
          `${name}: first divergence at line ${i + 1}\n    baseline: ${JSON.stringify(a[i] ?? '<end>')}\n    current : ${JSON.stringify(b[i] ?? '<end>')}`
        );
      }
      // Collect links/images + metadata at one width only
      const collected = await page.evaluate(() => {
        const links = [...document.querySelectorAll('a[href]')].map((a) => a.href);
        const imgs = [...document.images].map((i) => i.src);
        const q = (sel, attr) => document.querySelector(sel)?.getAttribute(attr) ?? '';
        return {
          links,
          imgs,
          meta: {
            title: document.title,
            description: q('meta[name="description"]', 'content'),
            ogTitle: q('meta[property="og:title"]', 'content'),
            ogDescription: q('meta[property="og:description"]', 'content'),
            ogImage: q('meta[property="og:image"]', 'content'),
            ogUrl: q('meta[property="og:url"]', 'content'),
            twitterCard: q('meta[name="twitter:card"]', 'content'),
          },
        };
      });
      metaByPage[name] = collected.meta;
      const origin = new URL(base).origin;
      for (const l of collected.links) {
        if (l.startsWith(origin) && !l.includes('#')) linkTargets.add(l);
      }
      for (const s of collected.imgs) {
        if (s.startsWith(origin)) imgTargets.add(s);
      }
    }

    // Visual diff
    const basePath = path.join(BASELINE, `${name}-${width}.png`);
    const curPath = path.join(CURRENT, `${name}-${width}.png`);
    if (fs.existsSync(basePath)) {
      const img1 = PNG.sync.read(fs.readFileSync(basePath));
      const img2 = PNG.sync.read(fs.readFileSync(curPath));
      const W = Math.max(img1.width, img2.width);
      const H = Math.max(img1.height, img2.height);
      const pad = (img) => {
        if (img.width === W && img.height === H) return img;
        const out = new PNG({ width: W, height: H });
        // fill with site background so height deltas count as diffs
        for (let i = 0; i < out.data.length; i += 4) {
          out.data[i] = 0xf8; out.data[i + 1] = 0xf6; out.data[i + 2] = 0xf2; out.data[i + 3] = 255;
        }
        PNG.bitblt(img, out, 0, 0, img.width, img.height, 0, 0);
        return out;
      };
      const p1 = pad(img1);
      const p2 = pad(img2);
      const diff = new PNG({ width: W, height: H });
      const n = pixelmatch(p1.data, p2.data, diff.data, W, H, { threshold: 0.1 });
      const pct = (n / (W * H)) * 100;
      if (pct > 0.5) {
        fs.writeFileSync(path.join(CURRENT, `${name}-${width}-diff.png`), PNG.sync.write(diff));
        visualFail.push(`${name}@${width}: ${pct.toFixed(2)}% (h ${img1.height} vs ${img2.height})`);
      }
    }
  await context.close();
  }
}

// ── Check 4: console errors ────────────────────────────────────
{
  const bad = Object.entries(consoleErrors)
    .filter(([, v]) => v.length)
    .map(([k, v]) => `${k}: ${v[0]}`);
  record(4, 'Console', bad.length === 0, bad.slice(0, 3).join(' | '));
}

// ── Check 5: internal links + images ───────────────────────────
{
  const bad = [];
  for (const url of [...linkTargets, ...imgTargets]) {
    const { status } = await head(url);
    if (status === 404 || status === 0) bad.push(`${new URL(url).pathname}:${status}`);
  }
  record(5, 'Links', bad.length === 0, bad.slice(0, 5).join(', '));
}

// ── Check 6: skill asset ───────────────────────────────────────
{
  const { status, len } = await head(`${base}/files/verbalized-sampling.skill`);
  record(6, 'Asset', status === 200 && len > 0, `status ${status}, ${len} bytes`);
}

// ── Check 7: text vs baseline ──────────────────────────────────
record(7, 'Text', textFail.length === 0, textFail.length ? '\n  ' + textFail.join('\n  ') : '');

// ── Check 8: visual diff ───────────────────────────────────────
record(8, 'Visual', visualFail.length === 0, visualFail.join('; '));

// ── Check 9: article metadata ──────────────────────────────────
{
  const bad = [];
  for (const slug of SLUGS) {
    const m = metaByPage[slug];
    if (!m) { bad.push(`${slug}: no meta collected`); continue; }
    if (!m.title) bad.push(`${slug}: empty title`);
    if (!m.description) bad.push(`${slug}: empty description`);
    if (!m.ogTitle) bad.push(`${slug}: no og:title`);
    if (!m.ogDescription) bad.push(`${slug}: no og:description`);
    if (!m.ogImage?.startsWith('https://gideonb.me')) bad.push(`${slug}: og:image not absolute (${m.ogImage})`);
    if (!m.ogUrl?.startsWith('https://gideonb.me')) bad.push(`${slug}: og:url not absolute (${m.ogUrl})`);
    if (!m.twitterCard) bad.push(`${slug}: no twitter:card`);
  }
  record(9, 'Metadata', bad.length === 0, bad.slice(0, 4).join('; '));
}

// ── Check 10: uniqueness ───────────────────────────────────────
{
  const pages = pageList();
  const titles = pages.map((p) => metaByPage[p]?.title);
  const ogImages = pages.map((p) => metaByPage[p]?.ogImage);
  const dup = (arr) => arr.filter((v, i) => arr.indexOf(v) !== i);
  const dups = [...new Set([...dup(titles), ...dup(ogImages)])];
  record(10, 'Uniqueness', dups.length === 0, dups.join('; '));
}

// ── Check 11: sitemap ──────────────────────────────────────────
{
  let urls = [];
  let ok = false;
  for (const smPath of ['/sitemap-index.xml', '/sitemap.xml']) {
    const r = await fetch(base + smPath).catch(() => null);
    if (r?.status === 200) {
      const xml = await r.text();
      const locs = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
      for (const loc of locs) {
        if (loc.endsWith('.xml')) {
          const sub = await fetch(loc.replace('https://gideonb.me', base)).catch(() => null);
          if (sub?.status === 200) {
            urls.push(...[...(await sub.text()).matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]));
          }
        } else {
          urls.push(loc);
        }
      }
      ok = true;
      break;
    }
  }
  const paths = urls.map((u) => new URL(u).pathname);
  const expected = pageList().map((n) => new URL(newUrl('https://x', n)).pathname);
  const missing = expected.filter((p) => !paths.includes(p));
  record(11, 'Sitemap', ok && missing.length === 0, ok ? (missing.length ? 'missing: ' + missing.join(', ') : `${paths.length} urls`) : 'no sitemap found');
}

// ── Check 12: hash redirect shim ───────────────────────────────
{
  const bad = [];
  const context = await browser.newContext();
  for (const slug of SLUGS) {
    const page = await context.newPage();
    await page.goto(`${base}/#article/${slug}`, { waitUntil: 'load' });
    await page.waitForTimeout(400);
    const p = new URL(page.url()).pathname;
    if (p !== `/writing/${slug}/`) bad.push(`${slug} -> ${p}`);
    await page.close();
  }
  const page = await context.newPage();
  await page.goto(`${base}/#writing`, { waitUntil: 'load' });
  await page.waitForTimeout(400);
  if (new URL(page.url()).pathname !== '/writing/') bad.push(`#writing -> ${new URL(page.url()).pathname}`);
  await page.close();
  await context.close();
  record(12, 'Redirect shim', bad.length === 0, bad.slice(0, 3).join(', '));
}

await browser.close();
finish();

function finish() {
  if (server) server.close();
  console.log('\n──── Verification summary ────');
  for (const r of results) {
    const mark = r.pass === true ? '✔' : r.pass === 'skip' ? '−' : '✘';
    console.log(` ${mark} ${String(r.id).padStart(2)}. ${r.name}${r.pass !== true && r.detail ? ' — ' + r.detail : ''}`);
  }
  const failed = results.filter((r) => r.pass === false);
  console.log(failed.length ? `\n${failed.length} check(s) FAILED` : '\nAll checks passed');
  process.exit(failed.length ? 1 : 0);
}
