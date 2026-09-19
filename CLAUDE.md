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
| Pages | `src/pages/` (`index`, `writing/index`, `writing/[slug]`, `work/index`, `work/all`, `work/[slug]`, `404`) |
| Work copy | `work.md` (repo root, `::: section` markers), read by `src/lib/work.mjs` |
| Work sections | `src/components/work/sections/` (`Opening`, `CaseOne` to `CaseFour`, `Closing`, `Contact`), composed by every /work page |
| Work diagrams | `src/components/work/*.html`, hand-maintained (see below) |
| Collection schema | `src/content.config.ts` |
| Images / files | `public/images/`, `public/files/` |
| Client JS (reveals, header, portrait) | `public/site.js` |
| Verification harness | `scripts/verify.mjs`, baselines in `.migration/baseline/` |

## /work routes

| Route | What | Source |
|---|---|---|
| `/work/` | Hub: four case cards on the authorship gauge, three project cards | `work/index.astro` |
| `/work/all/` | Every section on one page; the print path | `work/all.astro` |
| `/work/design-organisation/` | Case one | `work/[slug].astro`, `CaseOne` with `extended` |
| `/work/mytoyota-lexus/` | Case two. On the paper ground like the rest; `.wk-case2` is a bare hook with no styles | `CaseTwo` with `extended` |
| `/work/songkick-dopay/` | Case three | `CaseThree` |
| `/work/ai-products/` | Case four and governance | `CaseFour` with `extended` |
| `/work/prepcall/`, `/work/emotrix/`, `/work/nudge/` | Project stubs from `homepage.md` `project-*` sections | `work/[slug].astro` |

Slugs live in `CASES` and `PROJECTS` in `src/lib/work.mjs` and are public URLs. `extended` adds the diagrams the single-scroll view does not carry (`gap`, `ev`, `ctx`); `/work/all/` stays as the old `/work` was. Anchors into the old single page (`/work/#case-two` and the like) are redirected client-side by the shim in `Base.astro`.

## Work diagrams are hand-maintained

The 17 files in `src/components/work/*.html` were generated once by `.design/export_fragments.py` and are now edited by hand. Their colours resolve through the `--dg-*` role tokens and their type through the `.dg-*` size classes, both in `src/styles/work.css`. The generator is retired as `.design/RETIRED_export_fragments.py` and exits immediately; running it would have overwritten the token work. No other `.design/` script writes into `src/` (`build_pages_v2.py` and `build_all.py` write `.dc.html` files inside `.design/`). `opmodel.html`, `evmeasure.html` and `evmeasure_m.html` are unplaced pending a copy decision; do not delete them.

Five mobile rules in `work.css` key on literal inline strings (`[style*="grid-template-columns"]`, `[style*="display:flex"]`, `[style*="max-width:190px"]`, `[style*="translateX(-100%)"]`, `[style*='border-top']`). Moving an inline value into a class can silently switch one off. A diagram moves whole or not at all.

## DEFECTS

Known and left alone on purpose; fix in a pass of their own.

- `evmeasure_m.html`: both charts use `preserveAspectRatio="none"`, so at 390px the text inside them is squashed to about two thirds width.
- `evmeasure.html` labels itself "Case three" (it was built for the standalone EV case) and reports 3 rounds and a SUS of 76; `sus.html`, live in case two, shows four rounds at 73, 79 and 80. Placing both without a copy decision puts two contradicting charts in one case.
- Two of the five `[style*=]` mobile rules match nothing today (`translateX(-100%)`, `border-top`) and switch on silently if a matching inline value is ever written.
- Every /work page still loads Schibsted Grotesk from Google Fonts; nothing uses it since `25b39c6`.
- `npm run verify` fails checks 4, 7 and 8 on `main` (console 404s, text and visual drift on home and writing against the pre-migration baseline). Not caused by the /work work.
- `.design/*.py` carry absolute paths to this machine (`workmd.py`, the retired exporter).

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
