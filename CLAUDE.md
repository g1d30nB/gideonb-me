# gideonb.me — Personal Website

Static personal website for Gideon Bullock. Design leadership portfolio, case studies, and articles. Hosted on GitHub Pages.

## Tech Stack

- **Static:** HTML, CSS, vanilla JavaScript
- **Hosting:** GitHub Pages (repo: g1d30nB/gideonb-me)
- **Domain:** gideonb.me (DNS via IONOS)
- **CMS:** Markdown files in Obsidian vault (see below)

## How It Works

This is NOT a typical dev project. The website is managed through an Obsidian-based CMS workflow:

1. **Source of truth for content:** `Gideons_Vault/Personal Website/gideonb-me/Website build/`
2. **Homepage content:** `Website build/homepage.md` (sectioned with `::: section-name` markers)
3. **Articles:** Individual `.md` files in `Website build/posts/`
4. **Images:** `Website build/images/`

### Sync Workflow
1. Gideon edits markdown in Obsidian
2. Says "sync my site" in Cowork
3. Claude reads the markdown, rebuilds `articles.js` and `index.html`, copies everything to THIS directory
4. Gideon commits via GitHub Desktop and pushes to go live

### Key Files in This Repo
- `index.html` — The website (rebuilt by Claude during sync, don't hand-edit)
- `styles.css` — Styling (rebuilt by Claude)
- `app.js` — Site behaviour (rebuilt by Claude)
- `articles.js` — Article content as JS data (rebuilt from markdown during sync)
- `CNAME` — Custom domain config for GitHub Pages

## Commands

No build system. To preview locally, open `index.html` in a browser. Or use `Preview Site.command`.

## Important

- Never edit `index.html`, `styles.css`, `app.js`, or `articles.js` directly in this repo. They are generated from the Obsidian source.
- The full editing guide is at `Gideons_Vault/Personal Website/gideonb-me/GUIDE.md`
- Article template: `Website build/posts/_template.md`
- Only 2 articles should be `featured: true` at any time

## GitHub

- Username: g1d30nB
- Repo: github.com/g1d30nB/gideonb-me
- GitHub Desktop connected to this folder
