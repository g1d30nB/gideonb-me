# gideonb.me — Personal Website

Personal site for Gideon Bullock: design leadership portfolio, case studies, and articles. Built with Astro (static output, no client-side framework), deployed by Vercel on push. Every article has its own real URL with full social metadata.

**The old single-page architecture is gone.** There is no `articles.js`, no `app.js` SPA router, no hand-regenerated HTML. Content flows from markdown through `npm run build`. Never recreate those files.

## Tech Stack

- **Framework:** Astro 7, static output, zero client-side JS framework
- **Styling:** `src/styles/global.css` (the original hand-written stylesheet, unchanged)
- **Hosting:** Vercel, builds the site on every push (framework preset: Astro)
- **Domain:** gideonb.me (DNS at IONOS)
- **Repo:** github.com/g1d30nB/gideonb-me

## Commands

```
npm run dev       # local dev server
npm run build     # production build to dist/
npm run verify    # migration check suite: build + 12 checks vs live-site baseline
npm run verify -- --base https://<url>   # run checks against a deployed URL
```

## Structure

| What | Where |
|---|---|
| Articles (source of truth) | `src/content/writing/<slug>.md` |
| Article template | `src/content/writing/_template.md` |
| Homepage copy | `homepage.md` (repo root, `::: section` markers) |
| Layouts | `src/layouts/` (`Base.astro` = head/header/shim, `Footer`, `ArticleRow`) |
| Pages | `src/pages/` (`index`, `writing/index`, `writing/[slug]`, `404`) |
| Collection schema | `src/content.config.ts` |
| Images / files | `public/images/`, `public/files/` |
| Client JS (reveals, header, portrait) | `public/site.js` |
| Verification harness | `scripts/verify.mjs`, baselines in `.migration/baseline/` |

## Content rules

- **Slugs are frozen for the existing ten articles.** The filename is the slug is the URL. Renaming a file breaks its public URL.
- **Frontmatter:** `title` (required), `subtitle` (may be empty), `category` (string or array; arrays display joined with " & "), `readTime`, `image`, `featured` (default false), `order` (display position; highest = latest, shown on homepage).
- **Only two articles should be `featured: true` at a time.** (Currently five are, inherited from the old site — tidy when convenient.)
- Body images use root paths: `![...](/images/...)`.
- Old hash URLs (`/#article/<slug>`, `/#writing`) are redirected by an inline script in `Base.astro`. Keep it.

## Editing workflow (Obsidian CMS)

Gideon edits markdown in `Gideons_Vault/Personal Website/gideonb-me/Website build/` and says "sync my site". Syncing now means: copy changed article markdown into `src/content/writing/` (renamed to slug, images root-prefixed) and `homepage.md` to the repo root, run `npm run verify`, commit, push. Vercel deploys automatically. **Note:** the vault copy still reflects the pre-Astro layout; treat vault markdown as copy source only, never sync repo → vault without asking.

## Deploy model

Push to `main` → Vercel builds and deploys production. Preview deployments per branch. GitHub Pages is retired (see MIGRATION-REPORT.md for the cutover steps if not yet completed).

## Safety

- Never edit files in `Gideons_Vault/` without asking (Obsidian Sync).
- Run `npm run verify` before declaring changes done.
- `.migration/baseline/` is the captured ground truth of the pre-migration live site; don't regenerate it against the new site unless intentionally re-baselining.
