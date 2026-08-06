import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { satteri } from '@astrojs/markdown-satteri';

// Article markdown references images as "images/..." (relative), which worked
// when articles rendered at the site root. Pages now live at /writing/<slug>/,
// so root-prefix those srcs. External links open in a new tab, matching the
// behaviour of the previous hand-generated HTML.
function rehypeSiteLinks() {
  function walk(node) {
    if (node.type === 'element') {
      if (node.tagName === 'img' && typeof node.properties?.src === 'string') {
        const src = node.properties.src;
        if (!/^(https?:)?\//.test(src)) node.properties.src = '/' + src;
      }
      if (node.tagName === 'a' && typeof node.properties?.href === 'string') {
        if (/^https?:\/\//.test(node.properties.href)) {
          node.properties.target = '_blank';
          node.properties.rel = 'noopener';
        }
      }
    }
    (node.children || []).forEach(walk);
  }
  return (tree) => walk(tree);
}

export default defineConfig({
  site: 'https://gideonb.me',
  integrations: [sitemap()],
  markdown: {
    processor: satteri({
      hastPlugins: [rehypeSiteLinks],
      // The previous build kept the articles' punctuation exactly as typed;
      // smart-quote conversion would diverge from the published text.
      features: { smartPunctuation: false },
    }),
  },
});
