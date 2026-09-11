import workmd as W, diagrams as D, components as C, json, os
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
def write(n,b): open(n,"w").write(HEAD+b+"\n"+TAIL)
def wrap(w,body,bg="var(--paper)",pad="var(--s7)"): return f'<div style="width:{w}px;box-sizing:border-box;padding:{pad};background:{bg};">{body}</div>'
write("Ownership.dc.html", wrap(1200, C.ownership()))
write("People.dc.html", wrap(1200, C.people()))
write("Pairing.dc.html", wrap(1300, C.pairing("emotrix-timeline.jpg","prepcall-report-listening.jpg"), bg="var(--night)"))
# the frame sheet: every plate with its provenance, and the treatment rules
frames=[("emotrix-timeline.jpg","Emotrix, session review timeline","Real interface, synthetic session"),
        ("emotrix-stage.jpg","Emotrix, video pane withheld, live readings and moments","Real interface, synthetic session"),
        ("emotrix-review-full.jpg","Emotrix, the whole review interface","Real interface, synthetic session"),
        ("emotrix-cloud-hero.jpg","emotrix.cloud, public site","Live, September 2026"),
        ("prepcall-report-listening.jpg","PrepCall report, the listening half","Illustrative report from prepcall.me; real frame to follow"),
        ("prepcall-report-said.jpg","PrepCall report, what you said and how it sounded","Illustrative report from prepcall.me; real frame to follow")]
phones=[("mytoyota-01-home.jpg","MyToyota, home","Public App Store listing"),("mytoyota-03-car-status.jpg","MyToyota, vehicle status","Public App Store listing"),
        ("mytoyota-02-hybrid-coaching.jpg","MyToyota, hybrid coaching","Public App Store listing"),("lexus-01-dashboard.jpg","Lexus Link+, home","Public App Store listing"),
        ("lexus-03-vehicle-status.jpg","Lexus Link+, vehicle status","Public App Store listing"),("lexus-02-trip.jpg","Lexus Link+, trip","Public App Store listing")]
rules=("".join(f'<div style="border-top:1px solid var(--rule);padding:var(--s3) 0;font-size:14px;line-height:1.6;color:var(--body);">{t}</div>' for t in [
 "No device chrome and no radius. A hairline plate on the page&rsquo;s own ground, so a screenshot and a diagram obey the same rules.",
 "Every plate carries two lines under it. Left, what it is and whose work it is. Right, provenance in small caps.",
 "Phones are cropped to a fixed ratio from the top, so a row of them lines up whatever the source height.",
 "Dark ground for the two things built solo (Emotrix, PrepCall). Team ground for the app the team built. Paper for everything else.",
 "Nothing from the pilot: the Emotrix frames are the real interface driven by a synthetic session, and say so in the caption."]))
sheet=(f'<p class="lbl" style="color:var(--amber);margin-bottom:var(--s2);">Frames</p><p class="d2" style="margin-bottom:var(--s3);">Product imagery, and the treatment</p>'
       f'<p class="t2" style="max-width:820px;margin-bottom:var(--s7);">Screenshots and diagrams have to live on one page without it feeling like two. The plate is the shared grammar.</p>'
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--s7);margin-bottom:var(--s8);"><div>{rules}</div>'
       f'<div style="background:var(--night);padding:var(--s5);">{C.plate("emotrix-stage.jpg","Example on the dark ground","Real interface, synthetic session",dark=True)}</div></div>'
       f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:var(--s7);margin-bottom:var(--s8);">'+"".join(C.plate(s,w,p) for s,w,p in frames)+'</div>'
       f'<div style="background:var(--paper-team);padding:var(--s6);">{C.phone_row(phones)}</div>')
write("Frames.dc.html", wrap(1440, sheet))
# existing diagram artboards, unchanged emitters
import subprocess; subprocess.run(["python3","build_all.py"],check=True)
canvas={"pages":[{"id":"page-1","name":"Directions v2"},{"id":"page-2","name":"Frames and components"},{"id":"page-3","name":"Diagrams"}],
 "artboards":[
  {"file":"DirectionD.dc.html","x":0,"y":0,"w":1000,"h":5400,"page":"page-1","title":"Direction D — The document, with evidence"},
  {"file":"DirectionE.dc.html","x":1120,"y":0,"w":1000,"h":5400,"page":"page-1","title":"Direction E — The exhibition (recommended)"},
  {"file":"Main.dc.html","x":2240,"y":0,"w":1000,"h":2380,"page":"page-1","title":"Previous attempt, kept for the record"},
  {"file":"Frames.dc.html","x":0,"y":0,"w":1440,"h":3200,"page":"page-2","title":"Frames and the plate treatment"},
  {"file":"Pairing.dc.html","x":1560,"y":0,"w":1300,"h":900,"page":"page-2","title":"The pairing, case three"},
  {"file":"Ownership.dc.html","x":1560,"y":1020,"w":1200,"h":760,"page":"page-2","title":"Leading at a distance"},
  {"file":"People.dc.html","x":1560,"y":1900,"w":1200,"h":900,"page":"page-2","title":"Growing people"},
  {"file":"CapabilityArc.dc.html","x":0,"y":0,"w":1200,"h":1020,"page":"page-3"},
  {"file":"ServiceGap.dc.html","x":1320,"y":0,"w":1200,"h":1400,"page":"page-3"},
  {"file":"OperatingModel.dc.html","x":2640,"y":0,"w":1200,"h":1000,"page":"page-3"},
  {"file":"EVDomain.dc.html","x":0,"y":1540,"w":1200,"h":820,"page":"page-3"},
  {"file":"ComplaintTimeline.dc.html","x":1320,"y":1540,"w":1200,"h":720,"page":"page-3"},
  {"file":"SUSRounds.dc.html","x":0,"y":2480,"w":700,"h":790,"page":"page-3"},
  {"file":"RatingTurnaround.dc.html","x":820,"y":2480,"w":700,"h":820,"page":"page-3"},
  {"file":"ContextGrowth.dc.html","x":1640,"y":2480,"w":700,"h":810,"page":"page-3"}],
 "annotations":[
  {"id":"v2-note","x":3360,"y":0,"w":340,"page":"page-1","text":"Version 2. Both directions share the agreed system (Schibsted Grotesk, warm paper, amber for my call and teal for the team's work). What differs is composition.\n\nD keeps one measure and sets the frames inline, like plates in a monograph.\n\nE lets the imagery lead: the Emotrix and PrepCall pairing opens case three on a dark ground, the ownership split and the people figure run wide, and the App Store frames step across the team ground.\n\nI'd build E. The brief's own diagnosis of version one (abstract, no product, leadership buried) is a composition problem, and D fixes the imagery without fixing the pitch."},
  {"id":"pc-note","x":3360,"y":560,"w":340,"page":"page-1","text":"PrepCall frames are stand-ins from the public illustrative report on prepcall.me until your screenshots arrive (session ready screen, mid-session, one real report). The slots are sized for them.\n\nThe App Store frames both show a My Garage button on the home screen; case two says the team removed it. Tell me which build these are before they are captioned as the team's work."},
  {"id":"gap-note","x":1560,"y":2920,"w":340,"page":"page-2","text":"Growing people: the pathway diagram deliberately shows no level codes and no framework pages. Contract to permanent is drawn as roughly half to two thirds at the same headcount, which is the claim in work.md; there is no year-by-year series and none is implied."}],
 "launch":{"view":"canvas","page":"page-1"}}
json.dump(canvas,open("canvas.json","w"),indent=2,ensure_ascii=False)
print("artboards:",len(canvas["artboards"]))
