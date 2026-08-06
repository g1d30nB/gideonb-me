// Shared capture logic for baseline and verification runs.
// Both sides MUST use identical normalisation or diffs are meaningless.

export const SLUGS = [
  'design-leadership-ai',
  'consulting-trap',
  'mvp-misunderstood',
  'toyota-continuous-development',
  'three-decades-new-media',
  'future-of-cities',
  'discovery-is-not-dead',
  'ask-better-questions',
  'easier-to-build-the-wrong-thing',
  'after-the-app-grid',
];

export const VIEWPORTS = [390, 768, 1440];

// Logical page names -> URL fragments for old (hash) and new (path) sites.
export function pageList() {
  return ['home', 'writing', ...SLUGS];
}

export function oldUrl(base, name) {
  if (name === 'home') return `${base}/`;
  if (name === 'writing') return `${base}/#writing`;
  return `${base}/#article/${name}`;
}

export function newUrl(base, name) {
  if (name === 'home') return `${base}/`;
  if (name === 'writing') return `${base}/writing/`;
  return `${base}/writing/${name}/`;
}

const FREEZE_CSS = `
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    caret-color: transparent !important;
  }
  .reveal { opacity: 1 !important; transform: none !important; }
  html { scroll-behavior: auto !important; }
`;

// Prepare a freshly-loaded page for deterministic capture.
export async function stabilise(page) {
  await page.addStyleTag({ content: FREEZE_CSS });
  await page.evaluate(async () => {
    document.querySelectorAll('img[loading="lazy"]').forEach((img) => {
      img.loading = 'eager';
    });
    await document.fonts.ready;
    const imgs = [...document.images];
    await Promise.all(
      imgs.map((img) =>
        img.complete
          ? Promise.resolve()
          : new Promise((res) => {
              img.addEventListener('load', res, { once: true });
              img.addEventListener('error', res, { once: true });
            })
      )
    );
    window.scrollTo(0, 0);
  });
  // Small settle for layout after font swap.
  await page.waitForTimeout(200);
}

export async function captureText(page) {
  const text = await page.evaluate(() => document.body.innerText);
  return normaliseText(text);
}

export function normaliseText(text) {
  return text
    .split('\n')
    .map((l) => l.replace(/\s+/g, ' ').trim())
    .filter((l) => l.length > 0)
    .join('\n');
}

// Capture screenshots at all widths plus text for one logical page.
// urlFn(name) -> full URL. Reloads per viewport for determinism.
export async function capturePage(browser, urlFn, name, outDir, textDir) {
  const fs = await import('node:fs');
  const path = await import('node:path');
  for (const width of VIEWPORTS) {
    const context = await browser.newContext({
      viewport: { width, height: 900 },
      deviceScaleFactor: 1,
      reducedMotion: 'reduce',
    });
    const page = await context.newPage();
    await page.goto(urlFn(name), { waitUntil: 'networkidle' });
    await stabilise(page);
    await page.screenshot({
      path: path.join(outDir, `${name}-${width}.png`),
      fullPage: true,
    });
    if (width === VIEWPORTS[0] && textDir) {
      const text = await captureText(page);
      fs.writeFileSync(path.join(textDir, `${name}.txt`), text + '\n');
    }
    await context.close();
  }
}
