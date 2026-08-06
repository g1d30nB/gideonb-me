# Migration Report: gideonb.me → Astro on Vercel

*Written 6 August 2026, on branch `astro-migration`. `main` is untouched and the live site is unaffected.*

## 1. What was done

The site has been rebuilt as an Astro project: every article now has its own real page at `gideonb.me/writing/<slug>/` instead of a hash URL that search engines and LinkedIn could never see. Before touching anything, I captured screenshots and text of every page of the live site at three screen widths, then built a 12-point automated check suite that compares the new site against those captures. The new site passes all twelve checks and is pixel-identical to the live one (0.00% visual difference on every page tested). The hand-maintained `articles.js` file is gone; articles are plain markdown files and `npm run build` does the rest. The branch is deployed on Vercel and verified working at **https://gideonb-me.vercel.app** — it just needs your domain pointed at it (steps below).

## 2. Check suite results

Run locally and again against the deployed Vercel URL. All checks passed in both runs.

| # | Check | Result |
|---|-------|--------|
| 1 | Build completes cleanly | ✔ |
| 2 | All 12 pages return 200 | ✔ |
| 3 | The ten article slugs match the frozen list exactly | ✔ |
| 4 | Zero browser console errors on every page | ✔ |
| 5 | Every internal link and image resolves (no 404s) | ✔ |
| 6 | The Verbalised Sampling `.skill` download works | ✔ |
| 7 | Text of every page matches the live site word-for-word | ✔ |
| 8 | Pixel comparison vs live site under 0.5% at 390/768/1440px | ✔ (0.00%) |
| 9 | Every article has title, description, OG and Twitter tags with absolute URLs | ✔ |
| 10 | No two pages share a title or social image | ✔ |
| 11 | Sitemap exists and lists all twelve pages | ✔ |
| 12 | Old `/#article/...` links redirect to the new URLs | ✔ |

Re-run any time with `npm run verify` (or `npm run verify -- --base <url>` against a deployed copy).

## 3. Things that didn't pass / needed a judgement call

Nothing failed. Six judgement calls to be aware of:

1. **Article order and featured flags.** The old generated file had drifted from `posts/manifest.json`: the live site showed articles in a different order, with **five** featured articles, not the two your old notes said. I preserved exactly what the live site shows (that's what the pixel checks demand). Order now lives in each article's `order` field; tidy the featured flags whenever you like.
2. **A homepage sentence you never published.** The repo's `homepage.md` contained "The tools change faster than the thinking." at the end of the writing intro, but the live site doesn't show it — it was edited but never synced. I removed it from the repo copy so the site matches what's live. Your Obsidian vault still has it; it will publish the next time you sync.
3. **"Back to Writing" now goes to Writing.** On the old site that link said "Back to Writing" but actually went to the homepage. The new one goes where the label says.
4. **One typo-level markdown fix** in *Three Decades of New Media*: a stray `****` in the Ericsson quote that the new renderer displayed literally. Visible text is unchanged.
5. **The `.skill` file isn't actually linked from any article.** The Verbalised Sampling article tells readers to download the file but never links it. It's still served at `/files/verbalized-sampling.skill` — you may want to add the link some day.
6. **Social images for the two index pages.** Articles use their own images; the homepage and writing index needed one each, so they use your two portrait frames. Swap if you'd prefer something else.

## 4. Remaining manual steps (in order)

Vercel is already building this branch automatically: project **gideonb-me** in the **HUBIQ** team, framework detected as Astro. One nuance: because this was a brand-new Vercel project, its current "production" deployment is built from the `astro-migration` branch — the new site. That's fine, but it means **the switch to the new site happens at step 2 (DNS), not at the merge**. In order:

1. **Attach the domain in Vercel.** Dashboard → HUBIQ team → gideonb-me project → Settings → Domains → add `gideonb.me` (and `www.gideonb.me` if you want it). Nothing changes yet; the world's DNS still points at GitHub Pages. Vercel will show the exact DNS records it wants — use those. They will almost certainly be:
   - `gideonb.me` (apex): **A record → 76.76.21.21**
   - `www.gideonb.me`: **CNAME → cname.vercel-dns.com**
2. **Repoint DNS at IONOS.** Replace the current GitHub Pages records (four A records starting 185.199...) with the records from step 1. **This is the go-live moment** — as it propagates (minutes to a few hours), gideonb.me starts serving the new site.
3. **Disable GitHub Pages.** GitHub → g1d30nB/gideonb-me → Settings → Pages → set Source to "None".
4. **Merge the branch.** Merge `astro-migration` into `main` (GitHub Desktop or a pull request). Vercel will rebuild from `main` and future pushes to `main` deploy automatically. The `CNAME` file in the repo root is a GitHub Pages leftover; it can be deleted after this step.

## 5. Rolling back

- **Before step 2:** nothing has changed; do nothing.
- **After step 2, before step 3:** put the old GitHub Pages A records back at IONOS (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153). The old site is still there and comes back as DNS propagates.
- **After step 3:** re-enable GitHub Pages from `main` in repo settings, then restore the DNS records as above.
- **After step 4:** rollback is a git revert of the merge on `main` — but note that reverting restores the *old site's files*, which Vercel can't build (no `package.json` build on the Astro preset). Realistically, after step 4 you fix forward: tell Claude Code what's wrong and push a fix; Vercel redeploys in under a minute.

## 6. How you edit the site from now on

Nothing about your writing habit changes; only what Claude does behind the scenes changed.

- **New article:** write it in Obsidian as before (`Website build/posts/`), then tell Claude Code "add this article to my site". Claude copies it to `src/content/writing/<slug>.md` (the filename becomes the URL), gives it the next `order` number, runs `npm run verify`, commits and pushes. Vercel publishes it automatically — no more rebuilding `articles.js`.
- **Homepage copy:** edit `Website build/homepage.md` in Obsidian, then "sync my site". Claude copies it to the repo's `homepage.md`, verifies, commits, pushes.
- **The old "sync my site" instructions in the vault's GUIDE.md describe the dead workflow** — worth updating or deleting when convenient.
- Committing/pushing via GitHub Desktop still works exactly as before if you prefer doing that part yourself.

## 7. The vault copy

`Gideons_Vault/Personal Website/gideonb-me/Website build/` is now a **stale archive** of the old architecture (it still contains `articles.js`, `app.js`, `index.html`). I have not touched it. The markdown in it (posts + homepage.md) is still your writing source and still current; the generated files in it are dead. Decide at leisure what to prune — but remember note 2 above: its `homepage.md` has one unpublished sentence that will go live on your next sync.
