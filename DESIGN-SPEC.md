# Design spec: gideonb.me

Version 3, 18 September 2026. Supersedes the visual direction in `DESIGN-BRIEF.md` (v2) and the
aesthetic direction in `.impeccable.md`. The users, the confidentiality rules and the copy that must
survive a layout pass all still stand in those two files; read them for that, and ignore their
palette and typeface sections entirely.

The live reference is the design system artifact, which carries the tokens with usage notes and a
live preview of every component described here. `tokens.css` beside this file is the same thing as
CSS and is the thing to commit.

---

## The organising rule

**Everything is either very large or very small, with nothing in the middle.**

Type is 140px or 12px. Colour is a 40px mark or a full-bleed wash, never a mid-size flat panel.
Background geometry is a sharp hairline at 8 per cent or a soft blur at 4 per cent. The middle
register stays empty.

When a decision is not covered below, this rule decides it.

---

## Two registers

**Display.** Homepage hero, work hub header, case and project page headers, section openers. Type at
64px and up, bleeding off the right edge, grey or charcoal ground, construction geometry visible,
asymmetric placement.

**Document.** Case bodies, project bodies, articles. Prose at `--measure` (65 to 70 rendered
characters a line), 17px, paper ground,
the metadata rail, hairline rules, stat bands. No bleed, no background geometry, no type tricks.

They meet at section openers, where a display-scale heading introduces a document block. That
junction is what makes a two thousand word page feel composed. Build it as a component rather than
assembling it per page.

A diagram under an opener carries its own title only when that title names what the diagram shows.
If it restates the section's claim, it goes: the opener is the title. "What I owned, and what my
design managers and leads owned" names a diagram and stays; "Run as an internal consultancy" under
an opener that says the same thing does not. A subtitle left with no job goes with its title. The
small mono labels stay either way.

**A diagram title names what is plotted.** It never restates a stat or a sentence that appears within
one screen of it. The argument lives in the takeaway line or in the prose, once. 

**A diagram takeaway states what the picture shows or where the data came from.** It never states why
it matters. The opener does that, and does it better, because it sits at the top of the block rather
than under a chart. Same rule, one layer down: a takeaway that argues is repeating the opener, the
stat band or the prose, and in one case it contradicted them. Decided in 3a after the count: eight
placed takeaways, eight under an opener. The survivors are captions of fact.

---

## Colour

### Grounds

Five, cool, in a ladder. A long page reads as chapters because the ground changes underneath you.
Rotate rather than alternating two states. Two constraints: charcoal never follows charcoal, and
`ground-grey-deep` appears at most once per page.

A component inside a charcoal band sets `data-theme="dark"` on the band element and reads the same
token names. This is the pattern the existing `--night-*` tokens in `work.css` already follow; fold
those into the theme blocks rather than keeping a parallel set.

### One hue

The `fill-*` family sits on the same hue as the grounds and inks (250, chroma 0.004 to 0.006) and
lightness alone carries the difference. The site is neutral greys, the rating scale and the accent,
and nothing else. A warm lean for the fills was tried three times (hue 70, then 85 at two chromas)
and read as pink, then beige, then brown on the dark panels; it is withdrawn.

### Accessibility

Body text holds 4.5:1 against its ground. Diagram strokes carrying meaning hold 3:1. The ink ladder
has four steps: `ink` for headings and emphasis, `ink-muted` for body copy, `ink-label` for rail
labels and metadata at 12px and above, and `ink-faint`, which is **non-text only**: ticks, strokes,
hairlines and chart furniture. `ink-faint` never carries a glyph. One exception to the label step: a
label sitting on a `fill-100` panel takes `ink-muted`, because `ink-label` falls to 4.17:1 there. `fill-300` is a stroke colour,
never a text colour.

Measured, not estimated: `accent` on `ground-grey` is **2.84:1** and fails the 3:1 non-text minimum,
and `accent-text` on `ground-grey` is 4.41:1 and fails the 4.5:1 text minimum. So the two never
meet. No accent mark, focus-ring target or prose link sits on `ground-grey`, which means
`ground-grey` is not used behind a diagram that carries a mark or behind running prose with links.
On the other grounds the accent clears: 3.94 on paper, 3.46 on `rule-faint`, 3.21 on `fill-100`,
6.44 on charcoal. A per-case ground was tried for case two and withdrawn: it vanished the chart
furniture that shares its grey and pulled the label step under 4.5:1.

### Accent budget

One wash per page, bleeding off an edge, fading out before it reaches type. One accent rule per page,
40px by 3px, at the entry point: it marks the thing to read first. The pull-quote bars that look like
it stay neutral `fill-500`; one is emphasis, the others are structure. Otherwise marks only.
Three accent appearances in a viewport is already too many. Links use `accent-text`, not `accent`.

### Authorship

**Amber and teal retire.** They carried authorship across the seventeen diagram components and never
satisfied contrast alone. Replace with three signals together:

- **Shape.** Filled square for his own decisions, open ring for the team's work, half rule for
  shared. Legible in greyscale and at small size.
- **Label.** A mono rail label naming it in words. This is the primary signal.
- **Weight.** `fill-500` for his own decisions against `fill-400` for the team's. `fill-300` at
  2.3:1 cannot carry a data line or a label.

### The one colour exception

The app rating diagrams keep `rating-low`, `rating-mid` and `rating-high`, because a rating scale is
what those colours mean. The value and the position carry the meaning alongside the colour, so colour
is never the only signal.

---

## Type

**Geist, with Geist Mono.** Self-host both, subset. Drop the Inter link in `Base.astro` and the
Schibsted Grotesk link in `work.astro`; `work.css` currently declares Inter in its body rule while
`work.astro` fetches Schibsted, so both go.

Display, document and technical registers as set out in `tokens.css`. Rail labels, section numerals,
stat figures and tags are mono. Stat figures are tabular so columns align.

**The two-tone heading.** A heading carries a breadcrumb inside itself: the first clause in
`ink-faint`, the clause that carries the argument in `ink`. It gives hierarchy without a second type
size and it is the most transferable device in the whole direction. Build it as a component.

---

## Layout

Frame at 1200px. The measure is specified in **rendered characters, 65 to 70 a line**, never in `ch`:
`ch` is the width of the zero glyph, not of an average character, and Geist's zero is wide (0.663em),
so `68ch` rendered 97 characters a line. In Geist at 17px the target is about 540px, which is what
`--measure: 48ch` resolves to; if the face or the prose size changes, re-measure rather than keeping
the number. The document register is two tracks and air: rail 170px, content at the measure, then
space on the right. The content is not recentred; the asymmetry is the point.

There is no meta column. One was built and withdrawn on evidence: held to the rule that it carries
only facts that qualify the block beside it, and never repeats a number already in a stat band, a
diagram or the prose on the same screen, it produced one real entry across four cases. Where a
block has a qualifying fact that appears nowhere else (case three's dates), it sits in the rail as a
second mono line under the label.

One breakpoint:

- Below 808px the rail label moves above the prose as a single line (rail 170 + gap 48 + measure 541
  + padding 48 = 807, so the prose never gives way to the rail). The content is still capped at the
  measure: the measure holds at every viewport, and only narrows where the screen is narrower than
  it. The rail never becomes a narrow column of wrapped text on a phone.
- Display sizes step down with the clamps in `tokens.css`.

Side gutter 16px minimum on phones. No horizontal page scroll at any width.

---

## Motion

The permitted list. **Nothing outside it ships.** If an effect is not named here, it does not exist.

**Background.** Continuous loops, 30 to 120 seconds, opacity capped at 8 per cent, transform only.
Parallax confined to the blurred shapes at plus or minus 0.3 to 0.5.

**Interface.** 220ms on state change, on `--ease`. The chip travelling across a pill. Icon weight
animating 100 to 300 on hover.

**Entrance.** One staggered reveal per section, 520ms with a 60ms stagger, fires once. The existing
IntersectionObserver in `work.astro` already does this; extend it rather than adding a library.

**Performance.** Transform and opacity only. No filter, width, position or box-shadow animation.
At most three moving layers in the viewport, with layers outside it paused via IntersectionObserver.
The target machine is a meeting room laptop nobody chose.

**Reduced motion.** Ambient loops are removed entirely rather than shortened. Entrance reveals become
an opacity fade. Everything stays usable with no motion at all.

**Explicitly rejected.** Smooth-scroll libraries. The page must scroll natively, because find-in-page,
anchors and trackpad momentum all matter more than the effect, and the metadata rail depends on real
sticky positioning.

---

## Iconography

Material Symbols Outlined, variable, subset to the ten glyphs in use: `design_services`,
`arrow_forward`, `arrow_outward`, `arrow_downward`, `arrow_back`, `download`, `mail`, `insights`,
`graphic_eq`, `schema`.

- **Weight steps with size.** 100 at 32px and above, 200 at 24px, 300 at 20px. Weight 100 below 32px
  fails the 3:1 non-text minimum.
- **Grade flips with ground.** 0 on light, -25 on charcoal. That axis exists to compensate for the
  bloom that makes light strokes on dark grounds look heavier.
- **Optical size tracks the rendered size.** `font-optical-sizing: auto`, or set `opsz` per step.

The variable font is loaded rather than exporting SVGs, so weight can animate on hover.
`design_services` is the recurring mark and is never enlarged as a watermark.

---

## Background geometry

**Construction geometry.** Circles, rectangles, full-height column rules and node dots at 1px,
`geo-line`, oversized beyond the viewport so what shows is a fragment of something larger. Static or
drifting on a 90 to 120 second loop. Inline SVG.

**Soft blurred shapes.** `geo-blur`, heavily blurred, the only layer permitted to parallax.

**The rule that keeps decoration apart from evidence.** Background geometry never exceeds 8 per cent
and never carries the accent. Diagrams sit at full contrast, use the same hairline weight, and own
the accent entirely.

Display register only. Never behind a case body, where it competes with the diagrams carrying the
argument.

---

## Imagery

Every image is framed and composed. No bare screenshots in the flow.

Decided crops, consistent device treatment, screenshots sitting inside a well on a warm grey or
charcoal fill. Scenes and environments are not invented: faked mockup photography reads worse than an
honest crop.

Assets for PrepCall, Emotrix, the Toyota apps and Nudge are still to come.

---

## What this touches in the repo

| Area | Work |
|---|---|
| `src/styles/global.css` | Replace the warm palette with `tokens.css`. Retire the 740px `.container` in favour of the frame and the three-track grid. |
| `src/styles/work.css` | Fold `--night-*` into the `[data-theme="dark"]` block. Remove the Inter declaration. |
| `src/layouts/Base.astro` | Drop the Inter link, add the self-hosted Geist faces and the subset Material Symbols. |
| `src/pages/work.astro` | Drop the Schibsted link. Extend the reveal observer to the motion spec. |
| `src/components/work/*.html` | Seventeen components. Amber and teal to the authorship device, warm greys, new grounds. This is a token swap only if the normalisation pass landed first. |
| `src/pages/index.astro` | The largest job. Rebuild in the two registers: display hero, three-track document body, stat bands, section openers. All prose is kept; the layout does the work. |
| New case and project pages | Apply the case template once the IA restructure has landed. |

---

## Order

1. Land the diagram normalisation and the IA restructure. Both are in flight.
2. Commit `tokens.css`. Swap `global.css` and `work.css` onto it. Nothing else changes yet.
3. Fonts: self-host Geist and Geist Mono, subset Material Symbols, remove Inter and Schibsted.
4. Build the shared pieces: section opener, two-tone heading, three-track layout, stat band, pill and
   chip button, rail label, tag, image well, construction geometry layer.
5. Apply to the case template, then the project template, then the work hub, then the homepage, then
   writing.
6. Verify: `npm run build`, `npm run verify`, contrast check, `prefers-reduced-motion`, keyboard
   focus, and Playwright screenshots at 1440 and 390.

---

## Carried forward, unchanged

British English. Never em dashes; commas, colons, semicolons or brackets. No emoji. Direct
assertions. Nothing should sound like a CV and nothing should sound like marketing.

The confidentiality rules in `DESIGN-BRIEF.md` are unchanged and absolute. The client is never named
in copy, captions, file names, alt text or commit messages. The only public formulation is "a tier
one automotive supplier".

The three load-bearing sentences named in `DESIGN-BRIEF.md` survive every layout pass. Change the
layout to fit them.

Astro, static output, no client framework. Ten article slugs frozen. `Gideons_Vault/` is never
written to. Work on a branch; pushing to `main` deploys production.
