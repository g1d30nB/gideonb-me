# Direction E, the full desktop page. Emits per-section artboards for the canvas (the canvas caps a frame
# at 8000px) and one continuous HTML for a real full-page render.
import workmd as W, diagrams as D, components as C, os, sys
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"; AD="var(--amber-d)"; TD="var(--teal-d)"
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
c1,c2,c3,c4=W.C1,W.C2,W.C3,W.C4
def write(n,b): open(n,"w").write(HEAD+b+"\n"+TAIL)
def F(h,pt=0,pb=0): return f'<div style="padding:{pt}px 120px {pb}px;box-sizing:border-box;">{h}</div>'
def BAND(h,pt=72,pb=64): return f'<div style="background:var(--night);color:var(--night-body);padding:{pt}px 120px {pb}px;box-sizing:border-box;">{h}</div>'
def TEAM(h,pt=72,pb=72): return f'<div style="background:var(--paper-team);padding:{pt}px 120px {pb}px;box-sizing:border-box;">{h}</div>'
def P(items,size=17,colour="var(--body)",mb=18,lh=1.75):
    return "".join(f'<p style="font-size:{size}px;line-height:{lh};color:{colour};margin:0 0 {0 if i==len(items)-1 else mb}px;">{p}</p>' for i,p in enumerate(items))
def rail(label,colour,kind,body,sub=""):
    s=f'<p class="lbl" style="color:var(--faint);margin-top:10px;">{sub}</p>' if sub else ""
    return (f'<div style="display:grid;grid-template-columns:180px 1fr;gap:44px;align-items:start;">'
            f'<div><div style="display:flex;align-items:center;gap:10px;">{D.dot(colour,kind,10)}<p class="lbl" style="color:{colour};">{label}</p></div>{s}</div>'
            f'<div style="max-width:680px;">{body}</div></div>')
def quote(text,colour=A,cls="d3"):
    return f'<div style="margin:var(--s6) 0 0;"><div style="width:48px;height:3px;background:{colour};margin-bottom:var(--s4);"></div><p class="{cls}" style="max-width:660px;">{text}</p></div>'
def defgrid(items):
    cells="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s4);"><p class="d4" style="margin-bottom:var(--s2);">{a}</p>'
                  f'<p style="font-size:15.5px;line-height:1.75;color:var(--body);margin:0;">{b}</p></div>' for a,b in items)
    return f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:34px 44px;">{cells}</div>'
def statline(stats):
    out="".join(f'<div style="padding:0 var(--s6) 0 {"var(--s6)" if i else "0"};{"border-left:1px solid var(--night-rule);" if i else ""}">'
                f'<p class="stat" style="color:var(--night-ink);font-size:40px;margin-bottom:10px;">{v}</p>'
                f'<p style="font-size:13px;line-height:1.5;color:var(--night-muted);margin:0;max-width:200px;">{l}</p></div>' for i,(v,l) in enumerate(stats))
    return f'<div style="display:flex;align-items:flex-start;flex-wrap:wrap;row-gap:var(--s6);border-top:1px solid var(--night-rule);padding-top:var(--s6);">{out}</div>'
def opener(c,dcol,kind,extra=""):
    i=c["info"]
    return BAND(f'<div style="display:flex;align-items:center;gap:13px;margin-bottom:var(--s5);">{D.dot(dcol,kind,12)}<p class="lbl" style="color:{dcol};">{i["number"]}</p></div>'
        f'<p class="d2" style="color:var(--night-ink);max-width:1000px;margin-bottom:var(--s5);">{i["title"]}</p>'
        f'<p style="font-size:14px;color:var(--night-muted);margin:0 0 14px;">{i["company"]} &nbsp;&middot;&nbsp; {i["dates"]}</p>'
        f'<p style="font-size:18px;line-height:1.8;color:var(--night-body);max-width:760px;margin:0 0 var(--s8);">{i["role"]}</p>'
        f'{extra}{statline(c["stats"])}', pt=84, pb=76)
def marker(txt):
    return (f'<div style="background:var(--paper-2);padding:9px 120px;display:flex;justify-content:space-between;align-items:baseline;">'
            f'<p class="lbl" style="color:var(--faint);">{txt}</p><p class="lbl" style="color:var(--faint);">One scrolling page, cut here only so the canvas can show it</p></div>')
def page(parts): return '<div style="width:1440px;box-sizing:border-box;background:var(--paper);">'+"\n".join(parts)+'</div>'

HEADER=('<div style="border-bottom:1px solid var(--rule);padding:22px 120px;display:flex;justify-content:space-between;align-items:center;">'
  '<p style="font-size:15px;font-weight:600;color:var(--ink);margin:0;letter-spacing:-0.005em;">Gideon Bullock</p>'
  '<div style="display:flex;gap:30px;"><p class="lbl" style="font-weight:500;color:var(--muted);">Home</p><p class="lbl" style="font-weight:500;color:var(--ink);">Work</p><p class="lbl" style="font-weight:500;color:var(--muted);">Writing</p></div></div>')
GAUGE=[("Case one","The organisation",f'{c1["info"]["company"]} &nbsp;&middot;&nbsp; {c1["info"]["dates"]}',"Everything here is mine. Built from nothing, run for seven years, sold engagement by engagement.",A,"fill"),
       ("Case two","What the organisation shipped",f'{c2["info"]["company"]} &nbsp;&middot;&nbsp; {c2["info"]["dates"]}',"I won it, staffed it, framed it and held the bar. Other people designed it.",T,"ring"),
       ("Case three","One decision inside it, measured",f'{c3["info"]["company"]} &nbsp;&middot;&nbsp; {c3["info"]["dates"]}',"My research team ran the study. The standard and the decision were mine.",T,"ring"),
       ("Case four","The craft, and the thesis",f'{c4["info"]["company"]} &nbsp;&middot;&nbsp; {c4["info"]["dates"]}',"Built solo. There was nobody else.",INK,"fill")]
cards="".join(f'<div><p class="lbl" style="color:{c};margin-bottom:var(--s2);">{lb}</p><p class="d4" style="font-size:26px;margin-bottom:10px;">{t}</p>'
  f'<p style="font-size:13px;line-height:1.6;color:var(--muted);margin:0 0 11px;">{m}</p><p style="font-size:15.5px;line-height:1.7;color:var(--body);margin:0;">{n}</p></div>' for lb,t,m,n,c,k in GAUGE)
gauge=('<svg viewBox="0 0 1200 66" width="100%" height="66" preserveAspectRatio="none" style="display:block;" aria-label="Three cases placed by distance from the drawing">'
 '<line x1="0" y1="30" x2="1200" y2="30" stroke="#d5cabb" stroke-width="1.5"></line><line x1="0" y1="30" x2="0" y2="66" stroke="#c5b9a8"></line>'
 '<line x1="308.5" y1="30" x2="308.5" y2="66" stroke="#c5b9a8"></line><line x1="617" y1="30" x2="617" y2="66" stroke="#c5b9a8"></line><line x1="925.5" y1="30" x2="925.5" y2="66" stroke="#c5b9a8"></line>'
 '<circle cx="0" cy="30" r="7" fill="#9a6a34"></circle><circle cx="308.5" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle><circle cx="617" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle><circle cx="925.5" cy="30" r="7" fill="#1e1a16"></circle>'
 '<text x="0" y="16" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE BUSINESS BEHIND THE WORK</text>'
 '<text x="1200" y="16" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE WORK</text></svg>')

COMP=W.paras(W.SEC["case1-commercial"])[0]; COM=[COMP.split(". I ran",1)[0]+".", "I ran"+COMP.split(". I ran",1)[1]]
GOV=W.paras(W.SEC["governance"])
S={}
S["Main"]=[HEADER,
  F(f'<p class="lbl" style="margin-bottom:var(--s4);">Selected Work</p><p class="d1" style="margin-bottom:var(--s6);">{W.META.get("title","Three cases")}</p>'
    f'<p style="font-size:21px;line-height:1.65;color:var(--body);max-width:720px;margin:0 0 var(--s5);">{W.INTRO[0]}</p>'
    f'<p style="font-size:16px;line-height:1.8;color:var(--muted);max-width:720px;margin:0;">{W.INTRO[1]}</p>', pt=96),
  F(gauge+f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:34px;margin-top:var(--s2);">{cards}</div>'
    f'<div style="margin-top:var(--s7);padding-top:var(--s5);border-top:1px solid var(--rule);max-width:840px;"><p class="t3" style="font-size:14px;">{W.INTRO[2]}</p></div>', pt=64, pb=96)]

narr=c1["narrative"]
S["DeskOneA"]=[marker("Continues from the opening"), opener(c1,AD,"fill"),
  F(rail("The challenge",A,"fill",P(c1["challenge"])), pt=76), F(rail("My role",A,"fill",P(c1["role"])), pt=48),
  F(rail("The commercial line",A,"fill",quote(COM[0],cls="d4")+'<div style="height:var(--s5);"></div>'+P([COM[1]])), pt=56),
  F(rail(c1["info"]["narrative-label"],A,"fill",P(narr[:2]),sub="Narrative"), pt=64), F(D.arc(), pt=56),
  F(rail("The turn",A,"fill",P(narr[2:3])+quote("A disjointed end-to-end experience is usually a faithful reflection of a disjointed business, and this one was faithful.")), pt=64, pb=88)]
S["DeskOneB"]=[marker("Case one continues"), BAND(D.gap()),
  F(rail("What it left behind",A,"fill",P([narr[3].split(" What they went on to build",1)[0]])+
    f'<div style="margin:var(--s6) 0;background:var(--paper-team);border:1px solid oklch(0.87 0.020 195);padding:var(--s5);">'
    f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:var(--s3);">{D.dot(T,"ring",11)}<p class="lbl" style="color:{T};">The team&rsquo;s work</p></div>'
    f'<p style="font-size:17px;line-height:1.8;color:oklch(0.36 0.022 195);margin:0;">What they went on to build{narr[3].split(" What they went on to build",1)[1]}</p></div>'+
    P(narr[4:6])), pt=76),
  F(rail(c1["info"]["leading-label"],A,"fill",P(W.paras(W.SEC["case1-leading"]))), pt=88), F(C.ownership(), pt=48),
  F(rail(c1["info"]["people-label"],A,"fill",P(W.paras(W.SEC["case1-people"]))), pt=88), F(C.people(), pt=48, pb=88)]
S["DeskOneC"]=[marker("Case one continues"), F(D.opmodel(), pt=72),
  F(rail("How it was run",A,"fill",defgrid(c1["approach"])), pt=72),
  F(rail("The hardest part",A,"fill",P(c1["hard"])), pt=64),
  F(rail("What changed",A,"fill",P(c1["impact"],size=18,colour="var(--ink)")), pt=56, pb=96)]

res=[("2,321","users surveyed"),("266","app store reviews analysed"),("19","customer interviews"),("20 hrs","contextual research"),("4","nationwide dealership visits"),("12","competitor teardowns")]
resh="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s4);"><p class="stat" style="font-size:34px;margin-bottom:6px;">{v}</p><p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{l}</p></div>' for v,l in res)
role2=c2["role"]
S["DeskTwoA"]=[marker("Continues from case one"), opener(c2,TD,"ring"),
  F(rail("The challenge",A,"fill",P(c2["challenge"])), pt=76),
  F(f'<div style="display:grid;grid-template-columns:180px 1fr;gap:44px;align-items:start;"><div><div style="display:flex;align-items:center;gap:10px;">{D.dot(T,"ring",10)}<p class="lbl" style="color:{T};">Authorship</p></div></div>'
    f'<div style="max-width:840px;border-top:2px solid {T};border-bottom:1px solid var(--rule);padding:var(--s6) 0;"><p class="d2" style="margin-bottom:var(--s5);">I did not design this app.</p>'
    f'<p style="font-size:18px;line-height:1.8;color:var(--body);max-width:700px;margin:0;">{role2[0].split("I did not design this app. ",1)[-1]}</p></div></div>', pt=60),
  F(rail("What I did",A,"fill",P(role2[1:])), pt=52), F(rail("How",A,"fill",defgrid(c2["approach"])), pt=60, pb=88)]
PH=[("mytoyota-01-home.jpg","MyToyota, home","Public App Store listing"),("lexus-01-dashboard.jpg","Lexus Link+, home","Public App Store listing"),
    ("mytoyota-03-car-status.jpg","MyToyota, vehicle status","Public App Store listing"),("lexus-03-vehicle-status.jpg","Lexus Link+, vehicle status","Public App Store listing")]
phones="".join(f'<div style="margin-top:{[0,40,16,56][i]}px;">{C.plate(s,w,p,aspect="9 / 16",fit="cover",pos="top")}</div>' for i,(s,w,p) in enumerate(PH))
hard2=c2["hard"]
S["DeskTwoB"]=[marker("Case two continues"),
  TEAM(f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:var(--s4);">{D.dot(T,"ring",12)}<p class="lbl" style="color:{T};">{c2["info"]["aside-label"]}</p></div>'
    f'<p class="d2" style="max-width:900px;margin-bottom:var(--s5);">Everything on this ground is theirs</p>'
    f'<p style="font-size:17px;line-height:1.8;color:oklch(0.40 0.020 195);max-width:700px;margin:0 0 var(--s8);">The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p>'
    f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s5);align-items:start;">{phones}</div>'
    f'<div style="height:72px;"></div>{D.ev()}<div style="height:64px;"></div>'
    f'<div style="display:grid;grid-template-columns:700px 1fr;gap:56px;align-items:start;">{D.sus()}'
    f'<div><p class="lbl" style="color:{T};margin-bottom:var(--s4);">And the rest of it</p>{P(hard2[1:2],size=16,colour="oklch(0.40 0.020 195)")}'
    f'<div style="margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid oklch(0.87 0.020 195);display:flex;gap:13px;align-items:flex-start;">{D.dot(T,"ring",11)}'
    f'<p style="font-size:15.5px;line-height:1.75;color:{T};margin:-4px 0 0;">{hard2[2]}</p></div></div></div>', pt=88, pb=88),
  BAND(D.timeline()),
  F(f'<div style="display:grid;grid-template-columns:700px 1fr;gap:56px;align-items:start;">{D.rating()}<div><p class="lbl" style="color:{A};margin-bottom:var(--s4);">What changed</p>{P(c2["impact"][:1],size=16)}{quote(c2["impact"][1],cls="d4")}</div></div>', pt=72, pb=104)]

S["DeskEV"]=[marker("Continues from case two"), opener(c3,TD,"ring"),
  F(rail("The challenge",A,"fill",P(c3["challenge"])), pt=76), F(rail("Whose work",T,"ring",P(c3["role"])), pt=48),
  F(C.ev_measure(), pt=64),
  F(rail("What was found, and what was decided",A,"fill",defgrid(c3["approach"])), pt=72),
  F(rail("What changed",A,"fill",P(c3["impact"],size=18,colour="var(--ink)")), pt=56, pb=96)]

n3=c4["narrative"]
S["DeskThree"]=[marker("Continues from case three"),
  opener(c4,"var(--night-ink)","fill", extra=C.pairing("emotrix-timeline.jpg","prepcall-report-listening.jpg")+'<div style="height:56px;"></div>'),
  F(rail("The challenge",INK,"fill",P(c4["challenge"])), pt=76), F(rail("My role",INK,"fill",P(c4["role"])), pt=48),
  F(rail(c4["info"]["narrative-label"],INK,"fill",P(n3)), pt=64),
  F(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:start;">'
    f'{C.plate("emotrix-stage.jpg","Emotrix session review. The video pane is withheld; the readings, the moments and the channel quality sit beside it.","Real interface, synthetic session")}'
    f'{C.plate("emotrix-cloud-hero.jpg","emotrix.cloud. The thesis, stated in public.","Live site, September 2026")}</div>', pt=64),
  F(rail("What I learned building it",INK,"fill",defgrid(c4["approach"])), pt=72),
  F(f'<div style="display:grid;grid-template-columns:700px 1fr;gap:56px;align-items:start;">{D.ctx()}<div><p class="lbl" style="color:{A};margin-bottom:var(--s4);">Why it matters</p>'
    f'<p style="font-size:17px;line-height:1.8;color:var(--body);margin:0 0 18px;">Designing for a probabilistic system is largely this work, deciding what the model is allowed to carry. The interface is the easy part.</p>'
    f'<p class="d4" style="margin:0;">The hard part is a product that behaves differently on Tuesday than it did on Monday, and the constraints that keep it trustworthy anyway.</p></div></div>', pt=64),
  F(rail(c4["info"]["aside-label"],INK,"fill",f'<div style="border:1px solid var(--rule-2);padding:var(--s5);">{P(c4["hard"],size=16)}</div>'), pt=72),
  F(rail("Where it stands",INK,"fill",P(c4["impact"],size=18,colour="var(--ink)")), pt=60, pb=96),
  F(rail("Governance",INK,"fill",P(GOV,size=17)+
    '<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s5);margin-top:var(--s6);">'+"".join(
      f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);"><p style="font-size:14px;font-weight:600;color:var(--ink);margin:0 0 4px;">{a}</p><p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{b}</p></div>'
      for a,b in [("EU AI Act, Article 5","Classification and the data protection impact assessment, on a shipped product"),("European Accessibility Act","Governance across a whole design function, turned into a four-tier service"),("Regulated automotive delivery","Every programme in the first three cases")])+'</div>'), pt=72, pb=112),
  BAND(f'<p class="lbl" style="color:{AD};margin-bottom:var(--s5);">The pattern</p><p style="font-size:20px;line-height:1.8;color:var(--night-body);max-width:840px;margin:0 0 var(--s7);">{W.CLOSING[0]}</p>'
    f'<p style="font-size:17px;line-height:1.8;color:var(--night-muted);max-width:840px;margin:0 0 var(--s6);">The last part is the one people underestimate.</p>'
    f'<p class="d2" style="color:var(--night-ink);max-width:1080px;margin:0;">Most of what I am proudest of was drawn by somebody else.</p>', pt=96, pb=96),
  F(f'<p class="lbl" style="margin-bottom:var(--s4);">Contact</p><p class="d4" style="font-size:24px;max-width:760px;margin-bottom:var(--s5);">{W.CONTACT[0]}</p>'
    f'<p style="font-size:17px;line-height:1.8;color:var(--body);max-width:760px;margin:0;">{W.CONTACT[1]}</p>', pt=96, pb=76),
  '<div style="padding:26px 120px 48px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;align-items:center;"><p class="t3" style="color:var(--faint);">&copy; 2026 Gideon Bullock</p><p class="t3" style="color:var(--faint);">gideonb.me</p></div>']

for name,parts in S.items(): write(f"{name}.dc.html", page(parts))
# one continuous page for the real render (markers stripped)
full="".join(p for name in ["Main","DeskOneA","DeskOneB","DeskOneC","DeskTwoA","DeskTwoB","DeskEV","DeskThree"] for p in S[name] if not p.startswith('<div style="background:var(--paper-2);padding:9px 120px'))
out=sys.argv[1] if len(sys.argv)>1 else "."
open(os.path.join(out,"full-desktop.dc.html"),"w").write(HEAD+page([full])+"\n"+TAIL)
print("desktop sections:", ", ".join(S.keys()))
