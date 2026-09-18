# RETIRED on 2026-09-18. Do not run, do not revive.
# This script regenerated all 17 files in src/components/work/ from diagrams.py, components.py
# and mobile_figures.py. Those files are now hand-maintained: their colours resolve through the
# --dg-* tokens and their type through the .dg-* classes in src/styles/work.css. Running this
# would overwrite that work, and it was already stale (it still emitted Schibsted Grotesk,
# replaced by hand in 25b39c6). Edit src/components/work/*.html directly. See CLAUDE.md.
import sys
sys.exit("RETIRED: src/components/work/ is hand-maintained. This script would overwrite it. See CLAUDE.md.")

# Writes every diagram as a static HTML fragment for the Astro page. Copy blocks stay in work.md;
# these are the drawn pieces, regenerated from here when a figure changes.
import re, os, diagrams as D, components as C, mobile_figures as M
OUT="/Users/gideon/Projects/My Website/gideonb-me/src/components/work"
os.makedirs(OUT,exist_ok=True)
def img(s):
    s=re.sub(r'src="([\w\-]+\.jpg)"', r'src="/images/work/\1"', s)
    # rows that keep their columns at phone width: chart axes, the EV chips, the rating key
    s=s.replace('<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">','<div class="keep" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">')
    s=s.replace('<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;">','<div class="keep" style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;">')
    s=s.replace('<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;">','<div class="keep" style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;">')
    return s
gauge=('<svg viewBox="0 0 1200 66" width="100%" height="66" preserveAspectRatio="none" style="display:block;overflow:visible;" aria-label="Four cases placed by distance from the drawing">'
 '<line x1="0" y1="30" x2="1200" y2="30" stroke="#d5cabb" stroke-width="1.5"></line><line x1="0" y1="30" x2="0" y2="66" stroke="#c5b9a8"></line>'
 '<line x1="308.5" y1="30" x2="308.5" y2="66" stroke="#c5b9a8"></line><line x1="617" y1="30" x2="617" y2="66" stroke="#c5b9a8"></line><line x1="925.5" y1="30" x2="925.5" y2="66" stroke="#c5b9a8"></line>'
 '<circle cx="0" cy="30" r="7" fill="#9a6a34"></circle><circle cx="308.5" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle><circle cx="617" cy="30" r="7" fill="#9a6a34"></circle><circle cx="925.5" cy="30" r="7" fill="#1e1a16"></circle>'
 '<text x="0" y="16" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE BUSINESS BEHIND THE WORK</text>'
 '<text x="1200" y="16" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE WORK</text></svg>')
frags={"gauge":gauge,"arc":D.arc(),"arc_m":M.arc_m(),"gap":D.gap(),"gap_m":M.gap_m(),"opmodel":D.opmodel(),"ownership":C.ownership(),"people":C.people(),
       "ev":D.ev(),"ev_m":M.ev_m(),"sus":D.sus(),"rating":D.rating(),"ctx":D.ctx(),"timeline":D.timeline(),"evmeasure":C.ev_measure(),"evmeasure_m":C.ev_measure(True),
       "pairing":C.pairing("emotrix-timeline.jpg","prepcall-report.jpg")}
for k,v in frags.items(): open(f"{OUT}/{k}.html","w").write(img(v))
print("fragments:",", ".join(frags))
