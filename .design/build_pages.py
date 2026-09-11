from pagelib import *   # noqa
import diagrams as D
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"

HEADER=('<div style="border-bottom:1px solid var(--rule);padding:22px 120px;display:flex;justify-content:space-between;align-items:center;">'
  '<p style="font-size:15px;font-weight:600;color:var(--ink);margin:0;letter-spacing:-0.005em;">Gideon Bullock</p>'
  '<div style="display:flex;gap:30px;"><p class="lbl" style="font-weight:500;color:var(--muted);">Home</p>'
  '<p class="lbl" style="font-weight:500;color:var(--ink);">Work</p>'
  '<p class="lbl" style="font-weight:500;color:var(--muted);">Writing</p></div></div>')

def marker(txt):
    return (f'<div style="background:var(--paper-2);padding:9px 120px;display:flex;justify-content:space-between;align-items:baseline;">'
            f'<p class="lbl" style="color:var(--faint);">{txt}</p>'
            f'<p class="lbl" style="color:var(--faint);">One scrolling page &nbsp;&middot;&nbsp; split here only so the canvas can show it</p></div>')

# ---- 1. opening ----
cards="".join(f'<div><p class="lbl" style="color:{c};margin-bottom:var(--s2);">{lb}</p>'
  f'<p class="d4" style="font-size:26px;margin-bottom:10px;">{t}</p>'
  f'<p style="font-size:13px;line-height:1.6;color:var(--muted);margin:0 0 11px;">{m}</p>'
  f'<p style="font-size:15.5px;line-height:1.7;color:var(--body);margin:0;">{n}</p></div>'
  for lb,t,m,n,c in [(a,b,cc,d,{"#b07a3c":A,"#3f7d7a":T,"#1e1a16":INK}[e]) for a,b,cc,d,e,_ in GAUGE])
gauge=('<svg viewBox="0 0 1200 66" width="100%" height="66" preserveAspectRatio="none" style="display:block;" aria-label="Three cases placed by distance from the drawing">'
 '<line x1="0" y1="30" x2="1200" y2="30" stroke="#d5cabb" stroke-width="1.5"></line>'
 '<line x1="186" y1="30" x2="186" y2="66" stroke="#c5b9a8"></line><line x1="600" y1="30" x2="600" y2="66" stroke="#c5b9a8"></line>'
 '<line x1="1014" y1="30" x2="1014" y2="66" stroke="#c5b9a8"></line>'
 '<circle cx="186" cy="30" r="7" fill="#9a6a34"></circle>'
 '<circle cx="600" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle>'
 '<circle cx="1014" cy="30" r="7" fill="#1e1a16"></circle>'
 '<text x="0" y="16" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE BUSINESS BEHIND THE WORK</text>'
 '<text x="1200" y="16" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE DRAWING ITSELF</text></svg>')
write("Main.dc.html", page([HEADER,
  F('<p class="lbl" style="margin-bottom:var(--s4);">Selected Work</p>'
    '<p class="d1" style="margin-bottom:var(--s6);">Three cases</p>'
    f'<p style="font-size:21px;line-height:1.65;color:var(--body);max-width:720px;margin:0 0 var(--s5);">{INTRO[0]}</p>'
    f'<p style="font-size:16px;line-height:1.8;color:var(--muted);max-width:720px;margin:0;">{INTRO[1]}</p>', pt=96),
  F(gauge+f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:42px;margin-top:var(--s2);">{cards}</div>'
    f'<div style="margin-top:var(--s7);padding-top:var(--s5);border-top:1px solid var(--rule);max-width:840px;">'
    f'<p class="t3" style="font-size:14px;">{CONFID}</p></div>', pt=64, pb=96)]))

# ---- 2. case one, first half ----
write("DeskCaseOneA.dc.html", page([marker("Continues from the opening"),
  openband(C1,"var(--amber-d)","fill"),
  F(rail("The challenge",A,"fill",P(C1["challenge"])), pt=76),
  F(rail("My role",A,"fill",P(C1["myrole"])), pt=48),
  F(rail("How the capability grew",A,"fill",P(C1["narr1"]),sub="Narrative"), pt=64),
  F(D.arc(), pt=56),
  F(rail("The turn",A,"fill",P(C1["narr2"])+quote(C1["pull"])), pt=64, pb=88)]))

# ---- 3. case one, second half ----
write("DeskCaseOneB.dc.html", page([marker("Case one continues"),
  BAND(D.gap()),
  F(rail("What it left behind",A,"fill",
    P(C1["narr3"])+
    f'<div style="margin:var(--s6) 0;background:var(--paper-team);border:1px solid oklch(0.87 0.020 195);padding:var(--s5);">'
    f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:var(--s3);">{D.dot(T,"ring",11)}'
    f'<p class="lbl" style="color:{T};">The team&rsquo;s work</p></div>'
    f'<p style="font-size:17px;line-height:1.8;color:oklch(0.36 0.022 195);margin:0;">{C1["credit"]}</p></div>'+
    P(C1["narr4"])), pt=76),
  F(D.opmodel(), pt=64),
  F(rail("How it was run",A,"fill",defgrid(C1["approach"])), pt=72),
  F(rail("The hardest part",A,"fill",P(C1["hard"])), pt=64),
  F(rail("What changed",A,"fill",P(C1["impact"],size=18,colour="var(--ink)")), pt=56, pb=96)]))

# ---- 4. case two, first half ----
res="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s4);">'
  f'<p class="stat" style="font-size:34px;margin-bottom:6px;">{v}</p>'
  f'<p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{l}</p></div>' for v,l in C2["research"])
write("DeskCaseTwoA.dc.html", page([marker("Continues from case one"),
  openband(C2,"var(--teal-d)","ring"),
  F(rail("The challenge",A,"fill",P(C2["challenge"])), pt=76),
  F(f'<div style="display:grid;grid-template-columns:180px 1fr;gap:44px;align-items:start;">'
    f'<div><div style="display:flex;align-items:center;gap:10px;">{D.dot(T,"ring",10)}'
    f'<p class="lbl" style="color:{T};">Authorship</p></div></div>'
    f'<div style="max-width:840px;border-top:2px solid {T};border-bottom:1px solid var(--rule);padding:var(--s6) 0;">'
    f'<p class="d2" style="margin-bottom:var(--s5);">{C2["disclaim"]}</p>'
    f'<p style="font-size:18px;line-height:1.8;color:var(--body);max-width:700px;margin:0;">{C2["disclaim2"]}</p></div></div>', pt=60),
  F(rail("What I did instead",A,"fill",P(C2["myrole"])), pt=52),
  F(rail("How",A,"fill",defgrid(C2["approach"])), pt=60),
  F(D.figure(A,"Case two &middot; what the research bought","fill","Before a single screen was redrawn",
    "UX research was not part of Toyota&rsquo;s playbook. I pitched its value and funded a dedicated research team inside the app organisation. This is what that bought.",
    f'<div style="display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:var(--s5);">{res}</div>',""), pt=60, pb=88)]))

# ---- 5. case two, second half ----
write("DeskCaseTwoB.dc.html", page([marker("Case two continues"),
  TEAM(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:var(--s4);">{D.dot(T,"ring",12)}'
    f'<p class="lbl" style="color:{T};">What the team built</p></div>'
    f'<p class="d2" style="max-width:900px;margin-bottom:var(--s5);">Everything on this ground is theirs</p>'
    f'<p style="font-size:17px;line-height:1.8;color:oklch(0.40 0.020 195);max-width:700px;margin:0 0 var(--s8);">'
    f'The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p>'
    f'{D.ev()}<div style="height:64px;"></div>'
    f'<div style="display:grid;grid-template-columns:700px 1fr;gap:56px;align-items:start;">{D.sus()}'
    f'<div><p class="lbl" style="color:{T};margin-bottom:var(--s4);">And the rest of it</p>'
    f'{P(C2["hard2"],size=16,colour="oklch(0.40 0.020 195)")}'
    f'<div style="margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid oklch(0.87 0.020 195);display:flex;gap:13px;align-items:flex-start;">'
    f'{D.dot(T,"ring",11)}<p style="font-size:15.5px;line-height:1.75;color:{T};margin:-4px 0 0;">{C2["credit"]}</p></div></div></div>', pt=88, pb=88),
  BAND(D.timeline()),
  F(f'<div style="display:grid;grid-template-columns:700px 1fr;gap:56px;align-items:start;">{D.rating()}'
    f'<div><p class="lbl" style="color:{A};margin-bottom:var(--s4);">What changed</p>'
    f'{P(C2["impact"],size=16)}{quote(C2["impact2"],size="d4")}</div></div>', pt=72, pb=104)]))

# ---- 6. case three, closing, contact ----
write("DeskCaseThree.dc.html", page([marker("Continues from case two"),
  openband(C3,"var(--night-ink)","fill"),
  F(rail("The challenge",INK,"fill",P(C3["challenge"])), pt=76),
  F(rail("My role",INK,"fill",P(C3["myrole"])), pt=48),
  F(f'<div style="display:grid;grid-template-columns:700px 1fr;gap:56px;align-items:start;">{D.ctx()}'
    f'<div><p class="lbl" style="color:{A};margin-bottom:var(--s4);">Why it matters</p>'
    f'<p style="font-size:17px;line-height:1.8;color:var(--body);margin:0 0 18px;">That is what designing for a probabilistic system actually involves. The interface is the easy part.</p>'
    f'<p class="d4" style="margin:0;">The hard part is designing for a product that behaves differently on Tuesday than it did on Monday, and building the constraints that keep it trustworthy anyway.</p></div></div>', pt=60),
  F(rail("What I learned building it",INK,"fill",defgrid(C3["approach"])), pt=72),
  F(rail("Where it stands",INK,"fill",P(C3["impact"],size=18,colour="var(--ink)")), pt=60, pb=112),
  BAND(f'<p class="lbl" style="color:var(--amber-d);margin-bottom:var(--s5);">The pattern</p>'
    f'<p style="font-size:20px;line-height:1.8;color:var(--night-body);max-width:840px;margin:0 0 var(--s7);">{CLOSING[0]}</p>'
    f'<p style="font-size:17px;line-height:1.8;color:var(--night-muted);max-width:840px;margin:0 0 var(--s6);">{CLOSING_LEAD}</p>'
    f'<p class="d2" style="color:var(--night-ink);max-width:1080px;margin:0;">{CLOSING_BIG}</p>', pt=96, pb=96),
  F(f'<p class="lbl" style="margin-bottom:var(--s4);">Contact</p>'
    f'<p class="d4" style="font-size:24px;max-width:760px;margin-bottom:var(--s5);">{CONTACT[0]}</p>'
    f'<p style="font-size:17px;line-height:1.8;color:var(--body);max-width:760px;margin:0;">{CONTACT[1]}</p>', pt=96, pb=76),
  '<div style="padding:26px 120px 48px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;align-items:center;">'
  '<p class="t3" style="color:var(--faint);">&copy; 2026 Gideon Bullock</p>'
  '<p class="t3" style="color:var(--faint);">gideonb.me</p></div>']))
print("desktop pages ok")
