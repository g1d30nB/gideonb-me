// Build-time parser for standalone content pages (work.md at the repo root),
// using the same `::: section-name` ... `:::` convention as homepage.md so the
// Obsidian editing workflow is identical.
import fs from 'node:fs';
import path from 'node:path';

export function loadPage(filename) {
  const file = path.resolve(process.cwd(), filename);
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

// Stat bullets are written as `- value | label`.
export function statPairs(text) {
  if (!text) return [];
  return text
    .split('\n')
    .filter((l) => l.trim().startsWith('- '))
    .map((l) => l.trim().slice(2))
    .map((l) => {
      const i = l.indexOf('|');
      if (i < 0) return { value: l.trim(), label: '' };
      return { value: l.slice(0, i).trim(), label: l.slice(i + 1).trim() };
    });
}
