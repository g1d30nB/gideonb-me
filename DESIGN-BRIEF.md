# Design brief: the gideonb.me /work portfolio page

Version 2, 11 September 2026. Case three restructured the same day. Version 1 produced a design pass that did not land.
Point Claude Code at `/Users/gideon/Projects/My Website/gideonb-me`.

---

## Read first

- `work.md` at the repo root. The copy is considered and hard won. Treat the argument as settled and the layout as open.
- `.design/` in this repo. A previous /design session produced three directions, a canvas and a built page at `.design/gideonb-work-page.html`. Look at all of it before drawing anything.
- `.impeccable.md`. The design context and brand personality from that session, still accurate.
- `src/styles/global.css` and `homepage.md` for the live site.
- Invoke the `my-writing-style` skill for anything written in Gideon's voice.

`src/pages/work.astro` is the current implementation and it is disposable.

## Why this matters now

Four live applications assume this page exists. Miro runs a case presentation at stage three. Proton runs a portfolio review. CGI SPARCK will ask for work at second stage. Airwallex use a form with no cover letter field and no free-text questions at all, so the CV and this link carry the entire application on their own.

September has brought more postings and most of them ask for a portfolio. The page is the constraint on the whole search.

## What version 1 got wrong

Gideon's assessment, and it is the brief for this round.

**The page was too abstract.** Diagrams and typography carried everything and no product ever appeared. A portfolio for a design leader that shows no designed thing asks the reader to take the craft on trust. Version 1 treated imagery as an open question. It is now a requirement.

**Toyota came across as machinery.** Operating models, engagement models, career frameworks and a P&L. The leadership is in there and it reads as process. Two things need to surface much harder, described below.

## The three cases

The spine holds. Three cases at three distances from the work, and the design should express that.

**One. The organisation.** Toyota Connected Europe, 2018 to 2026. Every decision his. A design function from zero to 40+ across six disciplines, run as an internal consultancy with four engagement models and a P&L, with every engagement sold by him. The narrative spine is the capability arc, described in full in `work.md`.

**Two. What the organisation shipped.** MyToyota and Lexus Link+, 1.9 to 4.6 stars. He did not design it. A design manager led the team day to day and the design leads made the calls. His contribution was winning and expanding the engagement, staffing it, arguing UX research into a business that had never funded it, framing the two problems that mattered, holding the quality bar, and funding four rounds of testing against delivery pressure.

**Three. The craft, and the AI thesis.** PrepCall and Emotrix, 2026. Both built solo, so every decision is his. Rewritten on 11 September to carry both products under one idea, that signal is not meaning. See `work.md` for the full copy.

This case now does more work than the other two and should get the most visual weight. It carries the empathic voice interface work on Hume's EVI, the context growth failure and the bounded prompt fix, the Article 5 decision, and the Emotrix interpretation layer with its dashboards. It is also the only case where a reader sees Gideon's own hands on a shipped product, so the product imagery belongs here above all.

## Toyota leadership, told properly

Two things need to carry far more weight than version 1 gave them.

**Leading at a distance, deliberately.** He stepped out of daily craft to lead at scale and that was a choice. He owned the standard, the strategic context, the operating model, the quality bar at review points, the investment, the protection of time and the cover for hard calls. The leads owned the daily design decisions, the customer facing detail, the craft end to end and their own development inside a clear progression framework. When executives wanted to understand a change he brought the designer who made it. Design this so it reads as seniority.

**Growing people.** Currently a bullet, and it deserves a section. He hired every one of the 40+. He built two progression pathways, practitioner leadership and people leadership, converging at Lead, with written expectations at every level covering what they do, how they decide, how they engage clients and what the next level asks for. Leadership endorsed it as aligned to global talent strategy. The function held the highest permanent retention rate of any department in the company. He shifted it from roughly half contract to two thirds permanent without growing headcount. He ran an annual listening cycle that turned 185 pieces of feedback into ten themes and fourteen initiatives across three horizons with named owners. Several of the team describe it as the best team they have worked in, and the service design capability he created is still running without him.

This is the half of the job that takes years to learn and it should be visible from across the room.

## Imagery, now required

**PrepCall.** Screenshots of the real product. Assets in `/Users/gideon/Projects/PrepCall/images/` and the product is live at prepcall.me, so capture fresh frames if the stored ones are stale. Show the voice session and the generated coaching report, because the report architecture is the design work. Scrub any real user content.

**Emotrix.** Screenshots of the dashboards Gideon designed and built. Assets in `/Users/gideon/Projects/Emotrix/`. Dashboards only. No video of any kind goes on this page.

Read the dashboards before writing about them. The copy in `work.md` describes them at a level Gideon could state from memory, so correct it against what the interface actually shows and tell him what you changed.

**The AI and empathic voice work carries the case.** Show the emotional signal arriving and show what the product does with it. A dashboard frame beside a PrepCall report frame makes the whole argument in one view, so design that pairing deliberately.

**MyToyota and Lexus Link+.** Current App Store and Play Store screenshots are public marketing assets and are safe to use.

Design the frames as part of the page rather than dropping in raw captures. Decide crops, device treatment and how a screenshot sits beside a diagram.

## Confidentiality, non-negotiable

This page is public and indexed.

**The client is never named, anywhere, in any form.** Not in copy, not in a caption, not in a file name, not in alt text, not in a commit message, and not visible inside any screenshot. The only public formulation is "a tier one automotive supplier". A mutual NDA signed 30 April is in force.

**Dashboards only.** No client video appears on this page under any circumstances. Check every frame for client names, logos, project codenames, vehicle programmes and real pilot data before it goes anywhere near the page. Where any doubt exists, use synthetic data and flag it to Gideon rather than deciding alone.

**No pilot results for Emotrix.** No legal entity, no funding, no outcomes. Early stage, no product in market.

**No revenue and no paying customers for PrepCall.** It is craft evidence.

**Nothing from the Sky decks marked confidential**, no unreleased V3 interface work, no Toyota service blueprints, no colleagues named.

Keep out entirely: the 22% margin contribution, revenue share by programme, the £2.25m design system savings projection, the build cost comparison, the 300+ properties figure, the DesignOps tooling saving, support call volumes, subscription non-renewal rates and screen counts.

Safe and public: 0 to 40+, £10m+ annual internal revenue, highest retention in the company, all App Store rating data, the PrepCall context growth figures, Article 5.

## Copy that must survive the layout pass

A design pass trims sentences that look like throat clearing. Three in `work.md` do load bearing work and must stay.

- Case two's role line naming that a design manager led the team and the design leads made the calls.
- "I did not design this app", and the paragraph after it.
- The line crediting the blueprints and patterns to the service designers he hired.

Change the layout to fit them.

## What I want from you

Start with a critique. Read `.design/gideonb-work-page.html` and the three directions, tell me what works, what fails and why, then propose where to go. Reuse anything worth keeping.

Then a design canvas covering the full page at desktop and mobile width, each case at component level, and every data and concept piece designed properly. Those are the capability arc, the team growth story, the TXD operating model, the EV before and after, the SUS rounds, the complaint timeline, the rating turnaround and the PrepCall context growth chart, plus the treatment for product screenshots.

Give me two directions before committing. The site today is warm off white (#f8f6f2), near black ink (#1e1a16), Inter, 740px measure, quiet and typographic. One direction should extend that faithfully. One should argue for more visual ambition, on the grounds that a design leader's portfolio that looks like a blog post makes an argument Gideon may not want to make. Say which you would pick and why.

Solve these rather than dodging them.

- The three cases have different authorship. Find a visual device that carries that without a paragraph of explanation each time.
- The capability arc covers seven years of widening scope, from a screen to the business behind it. It deserves the best diagram on the page.
- Service design has to be shown without showing a single Toyota blueprint.
- Product screenshots and abstract diagrams have to live together without the page feeling like two pages.
- Three cases at this depth make a long page. Someone should be able to take the whole argument from headings, numbers and images alone.
- The homepage carries shallow Toyota and Songkick snapshots and Songkick appears in none of the three cases. Say what should happen to it.

## Two candidates for a fourth case, your call

**The EV charging redesign.** Users set a charging schedule with a 92% completion rate and a below benchmark ease score, because the screen gave them a control and stayed silent about the outcome. It supplies the customer outcome the portfolio otherwise lacks. The research was run by Amy Mullin and Tatiana Papaioannou and belongs to his research team. His contribution was the function that ran it, the standard it was held to and the decisions taken from it.

**The n8n workflow.** Built and running on 4 September. A design leader who instruments a product's community to find first run friction, inside the product itself. Small, and it demonstrates agentic tooling on something other than PrepCall.

## Constraints

British English. Never use em dashes. Use commas, colons, semicolons or brackets. No emoji. Direct assertions throughout. Avoid antithesis and negative definition, so no "not X, but Y" or "X, not Y" constructions. No explanatory colons. Nothing should sound like a CV and nothing should sound like marketing.

## Implementation notes

- Page copy lives in `work.md` at the repo root, parsed at build time by `src/lib/page.mjs` using `::: section-name` markers, so it stays editable in Obsidian. Keep that pattern.
- Block labels are data. A case's `-meta` block sets `narrative-label` and `aside-label`, so new named sections need no template change.
- Read `CLAUDE.md` before touching anything else. The ten article slugs are frozen, `Gideons_Vault/` is not to be written to, and `.migration/baseline/` is not to be regenerated. Propose homepage changes rather than making them.
- `npm run build` works. `npm run verify` compares against a pre-migration baseline and will report expected homepage diffs.
- Nothing is committed. Work on a branch. Pushing to `main` deploys production on Vercel.
