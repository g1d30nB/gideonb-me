// Build-time parser for homepage.md (repo root), which Gideon edits as the
// homepage CMS. Sections are delimited by `::: section-name` ... `:::`.
import fs from 'node:fs';
import path from 'node:path';

export function loadHomepage() {
  const file = path.resolve(process.cwd(), 'homepage.md');
  const raw = fs.readFileSync(file, 'utf8');

  const meta = {};
  const fm = raw.match(/^---\n([\s\S]*?)\n---/);
  if (fm) {
    for (const line of fm[1].split('\n')) {
      const i = line.indexOf(':');
      if (i > 0) meta[line.slice(0, i).trim()] = line.slice(i + 1).trim();
    }
  }

  const sections = {};
  const re = /^::: ([\w-]+)\r?\n([\s\S]*?)\r?\n:::[ \t]*$/gm;
  let m;
  while ((m = re.exec(raw))) sections[m[1]] = m[2].trim();

  return { meta, sections };
}

// key: value lines (case studies, project cards)
export function parseKV(text) {
  const out = {};
  for (const line of text.split('\n')) {
    const i = line.indexOf(':');
    if (i > 0) out[line.slice(0, i).trim()] = line.slice(i + 1).trim();
  }
  return out;
}

export function paragraphs(text) {
  return text
    .split('\n')
    .filter((l) => !l.trim().startsWith('- '))
    .join('\n')
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean);
}

export function bullets(text) {
  return text
    .split('\n')
    .filter((l) => l.trim().startsWith('- '))
    .map((l) => l.trim().slice(2).trim());
}

function escapeHtml(s) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

// Minimal inline markdown: **bold** only (what homepage.md actually uses).
export function inlineMd(text) {
  return escapeHtml(text).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
}

// The contact section is plain prose in homepage.md; the rendered page links
// the email address and the word LinkedIn, as the previous build did.
export function linkifyContact(text) {
  return inlineMd(text)
    .replace(
      /gideonb@me\.com/,
      '<a href="mailto:gideonb@me.com">gideonb@me.com</a>'
    )
    .replace(
      /LinkedIn/,
      '<a href="https://www.linkedin.com/in/gideonbullock/" target="_blank" rel="noopener">LinkedIn</a>'
    )
    .replace(
      /download my CV/,
      '<a href="/files/Gideon-Bullock-CV.pdf" download>download my CV</a>'
    );
}

// Project card links: old hash routes become real paths.
export function projectHref(link) {
  const m = link.match(/^#article\/([\w-]+)/);
  if (m) return `/writing/${m[1]}/`;
  return link;
}
