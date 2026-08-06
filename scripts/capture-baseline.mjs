// Capture ground-truth baselines from the live site before migration.
// Usage: node scripts/capture-baseline.mjs [baseUrl]
import { chromium } from 'playwright';
import { pageList, oldUrl, capturePage } from './lib/capture.mjs';
import fs from 'node:fs';

const base = (process.argv[2] || 'https://gideonb.me').replace(/\/$/, '');
const outDir = '.migration/baseline';
const textDir = '.migration/baseline/text';
fs.mkdirSync(textDir, { recursive: true });

const browser = await chromium.launch();
for (const name of pageList()) {
  process.stdout.write(`capturing ${name} ... `);
  await capturePage(browser, (n) => oldUrl(base, n), name, outDir, textDir);
  console.log('done');
}
await browser.close();
console.log('Baseline captured to', outDir);
