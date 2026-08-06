// Shared helpers over the writing collection.
import { getCollection } from 'astro:content';

export async function allArticles() {
  const entries = await getCollection('writing');
  return entries.sort((a, b) => a.data.order - b.data.order);
}

export function categoryLabel(category) {
  return category.join(' & ');
}

export function imagePath(image) {
  return image.startsWith('/') ? image : '/' + image;
}

// Homepage shows the first three articles plus the latest (highest order),
// skipping the latest if it is already among the first three — the exact
// logic of the old app.js.
export function homepageArticles(articles) {
  const first3 = articles.slice(0, 3);
  const latest = articles[articles.length - 1];
  if (first3.find((a) => a.id === latest.id)) return first3;
  return [...first3, latest];
}

// Meta description: subtitle if present, else the opening of the body with
// markdown syntax stripped, cut at a word boundary around 155 characters.
export function description(entry) {
  if (entry.data.subtitle) return entry.data.subtitle;
  const text = entry.body
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/^#+ .*$/gm, '')
    .replace(/^> ?/gm, '')
    .replace(/[*_`]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
  if (text.length <= 155) return text;
  const cut = text.slice(0, 155);
  return cut.slice(0, cut.lastIndexOf(' ')) + '…';
}
