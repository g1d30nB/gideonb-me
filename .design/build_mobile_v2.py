# Direction E at 390px. Same copy, one column, figures redrawn for the width.
import workmd as W, diagrams as D, components as C, os, sys
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"; AD="var(--amber-d)"; TD="var(--teal-d)"; PAD=22
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
c1,c2,c3,c4=W.C1,W.C2,W.C3,W.C4
COMP=W.paras(W.SEC["case1-commercial"])[0]; COM=[COMP.split(". I ran",1)[0]+".", "I ran"+COMP.split(". I ran",1)[1]]
GOV=W.paras(W.SEC["governance"])
def F(h,pt=0,pb=0,bg=None): return f'<div style="{"background:"+bg+";" if bg else ""}padding:{pt}px {PAD}px {pb}px;box-sizing:border-box;">{h}</div>'
def B(h,pt=48,pb=44): return f'<div style="background:var(--night);color:var(--night-body);padding:{pt}px {PAD}px {pb}px;box-sizing:border-box;">{h}</div>'
def head(label,colour,kind):
    return (f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {colour};margin-bottom:var(--s3);">'
            f'{D.dot(colour,kind,9)}<p class="lbl" style="color:{colour};font-size:10.5px;">{label}</p></div>')
def P(items,size=16,colour="var(--body)",mb=16):
    return "".join(f'<p style="font-size:{size}px;line-height:1.75;color:{colour};margin:0 0 {0 if i==len(items)-1 else mb}px;">{p}</p>' for i,p in enumerate(items))
def blk(label,colour,kind,body,pt=40,bg=None): return F(head(label,colour,kind)+body,pt=pt,bg=bg)
def deflist(items):
    return "".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);margin-bottom:var(--s5);"><p class="d4" style="font-size:18px;margin-bottom:7px;">{a}</p>'
                   f'<p style="font-size:14.5px;line-height:1.75;color:var(--body);margin:0;">{b}</p></div>' for a,b in items)
def quote(t,colour=A,cls="d3"): return f'<div style="margin-top:var(--s6);"><div style="width:40px;height:3px;background:{colour};margin-bottom:var(--s3);"></div><p class="{cls}">{t}</p></div>'
def fig(kick,colour,kind,title,sub,body,foot=""):
    f=f'<p style="font-size:13px;line-height:1.65;color:var(--ink);margin:var(--s4) 0 0;padding-top:var(--s3);border-top:1px solid var(--rule);font-weight:500;">{foot}</p>' if foot else ""
    return f'<div>{head(kick,colour,kind)}<p class="d3" style="margin-bottom:var(--s2);">{title}</p><p style="font-size:14px;line-height:1.65;color:var(--muted);margin:0 0 var(--s5);">{sub}</p>{body}{f}</div>'
def statgrid(stats):
    return ('<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5) var(--s4);border-top:1px solid var(--night-rule);padding-top:var(--s5);">'
            + "".join(f'<div><p class="stat" style="color:var(--night-ink);font-size:28px;margin-bottom:6px;">{v}</p><p style="font-size:12px;line-height:1.45;color:var(--night-muted);margin:0;">{l}</p></div>' for v,l in stats)+'</div>')
def opener(c,dcol,kind,extra=""):
    i=c["info"]
    return B(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s4);">{D.dot(dcol,kind,11)}<p class="lbl" style="color:{dcol};font-size:10.5px;">{i["number"]}</p></div>'
      f'<p class="d2" style="color:var(--night-ink);margin-bottom:var(--s4);">{i["title"]}</p><p style="font-size:13px;color:var(--night-muted);margin:0 0 12px;">{i["company"]} &nbsp;&middot;&nbsp; {i["dates"]}</p>'
      f'<p style="font-size:16px;line-height:1.8;color:var(--night-body);margin:0 0 var(--s7);">{i["role"]}</p>{extra}{statgrid(c["stats"])}', pt=56, pb=52)
def plate(src,what,prov,dark=False,aspect=None):
    return C.plate(src,what,prov,dark=dark,aspect=aspect,fit="cover",pos="top")
SVGF='font-family="Schibsted Grotesk,Helvetica,sans-serif"'

O=[f'<div style="border-bottom:1px solid var(--rule);padding:16px {PAD}px;display:flex;justify-content:space-between;align-items:center;"><p style="font-size:14px;font-weight:600;color:var(--ink);margin:0;">Gideon Bullock</p>'
   '<div style="display:flex;gap:16px;"><p class="lbl" style="font-size:10px;font-weight:500;">Home</p><p class="lbl" style="font-size:10px;font-weight:500;color:var(--ink);">Work</p><p class="lbl" style="font-size:10px;font-weight:500;">Writing</p></div></div>',
   F(f'<p class="lbl" style="margin-bottom:var(--s3);">Selected Work</p><p class="d1" style="margin-bottom:var(--s5);">{W.META.get("title","Three cases")}</p>'
     f'<p style="font-size:17.5px;line-height:1.7;color:var(--body);margin:0 0 var(--s4);">{W.INTRO[0]}</p><p style="font-size:15px;line-height:1.8;color:var(--muted);margin:0;">{W.INTRO[1]}</p>', pt=48)]
g=[]
for i,(lb,t,m,n,col,k) in enumerate([("Case one","The organisation",f'{c1["info"]["company"]} &middot; {c1["info"]["dates"]}',"Everything here is mine. Built from nothing, run for seven years, sold engagement by engagement.",A,"fill"),
    ("Case two","What the organisation shipped",f'{c2["info"]["company"]} &middot; {c2["info"]["dates"]}',"I won it, staffed it, framed it and held the bar. Other people designed it.",T,"ring"),
    ("Case three","One decision inside it, measured",f'{c3["info"]["company"]} &middot; {c3["info"]["dates"]}',"My research team ran the study. The standard and the decision were mine.",T,"ring"),
    ("Case four","The craft, and the thesis",f'{c4["info"]["company"]} &middot; {c4["info"]["dates"]}',"Built solo. There was nobody else.",INK,"fill")]):
    stem='<div style="width:1px;flex-grow:1;min-height:64px;background:var(--rule);"></div>' if i<3 else ""
    g.append(f'<div style="display:grid;grid-template-columns:22px 1fr;gap:14px;align-items:start;padding:var(--s5) 0;border-top:1px solid var(--rule);"><div style="display:flex;flex-direction:column;align-items:center;gap:6px;padding-top:3px;">{D.dot(col,k,12)}{stem}</div>'
      f'<div><p class="lbl" style="color:{col};font-size:10.5px;margin-bottom:6px;">{lb}</p><p class="d4" style="font-size:23px;margin-bottom:7px;">{t}</p><p style="font-size:12.5px;line-height:1.6;color:var(--muted);margin:0 0 9px;">{m}</p><p style="font-size:15px;line-height:1.7;color:var(--body);margin:0;">{n}</p></div></div>')
O.append(F('<p class="lbl" style="font-size:9.5px;margin-bottom:var(--s1);">The business behind the work</p>'+"".join(g)+
  f'<p class="lbl" style="font-size:9.5px;text-align:right;padding-top:var(--s4);border-top:1px solid var(--rule);">The drawing itself</p><p class="t3" style="margin-top:var(--s6);padding-top:var(--s4);border-top:1px solid var(--rule);">{W.INTRO[2]}</p>', pt=44, pb=56))
O.append("@@SPLIT@@")

# ---- case one ----
narr=c1["narrative"]
O.append(opener(c1,AD,"fill")); O.append(blk("The challenge",A,"fill",P(c1["challenge"]))); O.append(blk("My role",A,"fill",P(c1["role"]),pt=34)); O.append(blk("The commercial line",A,"fill",quote(COM[0],cls="d4")+'<div style="height:var(--s4);"></div>'+P([COM[1]]),pt=34))
O.append(blk(c1["info"]["narrative-label"],A,"fill",P(narr[:2])))
rows=[]
for i,(k,n,why,earn,_,_,_) in enumerate(D.ARC_STEPS):
    last=i==3; w=[26,46,70,100][i]
    if last: rows.append('<div style="display:flex;align-items:center;gap:10px;margin:var(--s5) 0;"><div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div><p class="lbl" style="color:var(--amber);font-size:9.5px;white-space:nowrap;">The question changed</p><div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div></div>')
    rows.append(f'<div style="border-top:{"3px solid var(--amber)" if last else "2px solid var(--rule-2)"};padding-top:var(--s3);margin-bottom:var(--s5);"><p class="lbl" style="color:{A if last else "var(--faint)"};font-size:10px;margin-bottom:7px;">{k}</p><p class="d4" style="font-size:20px;margin-bottom:var(--s2);">{n}</p>'
      f'<p style="font-size:13.5px;line-height:1.6;color:var(--body);margin:0 0 10px;">{why}</p><div style="height:9px;background:oklch(0.93 0.030 68);width:{w}%;margin-bottom:7px;"></div><p style="font-size:12px;line-height:1.5;color:var(--muted);margin:0;"><span style="color:{A};font-weight:600;">Earned &rarr;</span> {earn}</p></div>')
O.append(F(fig("Case one &middot; the spine",A,"fill","How the capability grew","Four capabilities in the order they were established. Each earned the next. The bar under each is how much of the customer&rsquo;s experience design was allowed to own.","".join(rows),foot="Each brief was wider than the last because the last one had worked."),pt=40))
O.append(blk("The turn",A,"fill",P(narr[2:3])+quote("A disjointed end-to-end experience is usually a faithful reflection of a disjointed business, and this one was faithful.")))
O.append("@@SPLIT@@")
sl=[]
for i,(n,o,mine) in enumerate(D.SLICES):
    if i>0: sl.append('<div style="display:flex;align-items:center;gap:9px;padding:7px 0 7px 5px;"><span style="width:10px;height:10px;border:1.5px dashed oklch(0.50 0.035 70);border-radius:50%;"></span><p style="font-size:11.5px;color:oklch(0.60 0.040 70);margin:0;">no owner</p></div>')
    sl.append(f'<div style="border:{"1.5px solid var(--amber-d)" if mine else "1px solid var(--night-rule)"};background:{"var(--night-2)" if mine else "transparent"};border-radius:3px;padding:var(--s3) 13px;"><p style="font-size:13.5px;font-weight:600;color:{"var(--night-ink)" if mine else "var(--night-body)"};margin:0 0 4px;">{n}</p><p style="font-size:11.5px;color:{AD if mine else "var(--night-muted)"};margin:0;">{o}</p></div>')
after="".join(f'<div style="border:1px solid oklch(0.33 0.020 190);border-radius:3px;padding:9px 12px;margin-bottom:7px;"><p style="font-size:12.5px;color:var(--night-body);margin:0;">{n}</p></div>' for n,_,_ in D.SLICES)
O.append(B(f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {AD};margin-bottom:var(--s3);">{D.dot(AD,"fill",9)}<p class="lbl" style="color:{AD};font-size:10.5px;">Case one &middot; what service design was for</p></div>'
 '<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);">A disjointed experience is a faithful picture of a disjointed business</p><p style="font-size:14px;line-height:1.75;color:var(--night-muted);margin:0 0 var(--s6);">No Toyota blueprint is shown. This is the shape of the problem.</p>'
 '<p class="lbl" style="color:var(--night-muted);font-size:10px;margin-bottom:var(--s3);">Before &middot; one slice, behaving as though it owned all of them</p>'+"".join(sl)+
 f'<p class="lbl" style="color:{TD};font-size:10px;margin:var(--s6) 0 var(--s3);">After &middot; one journey, owned together</p><div style="border:1.5px solid {TD};background:oklch(0.225 0.022 190);border-radius:3px;padding:13px;margin-bottom:10px;"><p style="font-size:13.5px;font-weight:600;color:var(--night-ink);margin:0 0 4px;">One end-to-end journey</p><p style="font-size:11.5px;color:{TD};margin:0;">Blueprinted front stage and back, reusable as service patterns</p></div>'+after+
 '<p style="font-size:15.5px;line-height:1.75;color:var(--night-ink);margin:var(--s5) 0 var(--s5);font-weight:500;">Business units that had never designed anything together started working on the same journey. They are still doing it, which is the part I am most confident about, because it outlasted me.</p>'
 f'<div style="border-top:1px solid var(--night-rule);padding-top:var(--s4);display:flex;gap:11px;align-items:flex-start;">{D.dot(TD,"ring",10)}<p style="font-size:14px;line-height:1.7;color:{TD};margin:-4px 0 0;">The blueprints, the reusable service patterns and the playbooks were built by the service designers who were hired to make them. What I did was make the case for it and hire into it.</p></div>'))
O.append(blk("What it left behind",A,"fill",P([narr[3].split(" What they went on to build",1)[0]])+f'<div style="margin:var(--s5) 0;background:var(--paper-team);border:1px solid oklch(0.87 0.020 195);padding:var(--s4);"><div style="display:flex;align-items:center;gap:9px;margin-bottom:9px;">{D.dot(T,"ring",10)}<p class="lbl" style="color:{T};font-size:10px;">The team&rsquo;s work</p></div><p style="font-size:15.5px;line-height:1.75;color:oklch(0.38 0.022 195);margin:0;">What they went on to build, blueprints, reusable service patterns and playbooks, mattered less than what it did to the conversation. Business units that had never designed anything together started working on the same journey.</p></div>'+P(narr[4:6])))
# leading at a distance
def ownlist(label,colour,kind,items):
    return (f'<div style="margin-bottom:var(--s5);"><div style="display:flex;align-items:center;gap:9px;margin-bottom:var(--s3);">{D.dot(colour,kind,10)}<p class="lbl" style="color:{colour};font-size:10.5px;">{label}</p></div>'
            + "".join(f'<div style="display:flex;gap:10px;align-items:flex-start;padding:9px 0;border-top:1px solid var(--rule);">{D.dot(colour,kind,8)}<p style="font-size:14.5px;line-height:1.6;color:var(--ink);margin:-3px 0 0;">{t}</p></div>' for t in items)+'</div>')
O.append(blk(c1["info"]["leading-label"],A,"fill",P(W.paras(W.SEC["case1-leading"]))))
O.append(F(fig("Case one &middot; leading at a distance",A,"fill","What I owned, and what the leads owned","The split, as it ran day to day.",
  ownlist("I owned",A,"fill",C.OWNED_ME)+ownlist("The leads owned",T,"ring",C.OWNED_LEADS),foot="When executives wanted to understand a specific change, I brought the designer who had made it."),pt=40))
O.append("@@SPLIT@@")
# growing people
O.append(blk(c1["info"]["people-label"],A,"fill",P(W.paras(W.SEC["case1-people"]))))
def bar(label,perm,col):
    return (f'<div style="margin-bottom:var(--s3);"><p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:0 0 6px;">{label}</p><div style="display:flex;height:30px;"><div style="width:{perm}%;background:{col};display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:oklch(0.97 0.008 80);font-weight:600;">Permanent</span></div><div style="width:{100-perm}%;background:oklch(0.90 0.014 80);display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:var(--muted);">Contract</span></div></div></div>')
O.append(F(fig("Case one &middot; growing people",A,"fill","Hiring, progression and retention","Progression before scale, a listening cycle that closed the loop, and a shift from contract to permanent at the same headcount.",
  f'<p class="lbl" style="font-size:10px;margin-bottom:var(--s3);">Two pathways, one framework</p>{C.ladder()}'
  f'<p class="lbl" style="font-size:10px;margin:var(--s5) 0 var(--s3);">Listening that closed the loop</p>{C.listening()}'
  f'<p class="lbl" style="font-size:10px;margin:var(--s5) 0 var(--s3);">Contract to permanent, at the same headcount</p>{bar("Roughly half permanent, when the shift began",50,"oklch(0.55 0.075 62)")}{bar("Two thirds permanent, at the end",67,"oklch(0.48 0.085 62)")}',
  foot="The highest permanent retention rate of any department in the company."),pt=40))
# operating model
disc="".join(f'<div style="padding:var(--s3) 0;border-bottom:1px solid var(--rule);"><p style="font-size:14.5px;font-weight:600;color:{A if m else "var(--ink)"};margin:0 0 3px;">{n}</p><p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{d}</p></div>' for n,d,m in D.DISCIPLINES)
models="".join(f'<div style="padding:var(--s3) 0;border-bottom:1px solid var(--rule);"><p style="font-size:14.5px;font-weight:600;color:var(--ink);margin:0 0 7px;">{n}</p><div style="height:8px;background:oklch(0.93 0.030 68);width:{w}%;margin-bottom:6px;"></div><p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{d}</p></div>' for n,d,w,_,_ in D.MODELS)
O.append(F(fig("Case one &middot; how it was run",A,"fill","Run as an internal consultancy","Six disciplines under one roof, four ways to buy them, and a management office at the centre of embedded teams.",
  f'<p class="lbl" style="font-size:10px;margin-bottom:var(--s3);">One office, embedded pods, one community</p>{C.orgmodel()}<p class="lbl" style="font-size:10px;margin:var(--s5) 0 0;padding-bottom:9px;border-bottom:1px solid var(--rule-2);">Six disciplines, one team</p>{disc}<p class="lbl" style="font-size:10px;margin:var(--s5) 0 0;padding-bottom:9px;border-bottom:1px solid var(--rule-2);">Four engagement models, shallow to deep</p>{models}',
  foot="Design&rsquo;s commercial contribution became visible to senior leadership for the first time."),pt=40))
O.append(blk("How it was run",A,"fill",deflist(c1["approach"]))); O.append(blk("The hardest part",A,"fill",P(c1["hard"]))); O.append(blk("What changed",A,"fill",P(c1["impact"],size=17,colour="var(--ink)"),pt=34))
O.append('<div style="height:56px;"></div>'); O.append("@@SPLIT@@")

# ---- case two ----
role2=c2["role"]; hard2=c2["hard"]
O.append(opener(c2,TD,"ring")); O.append(blk("The challenge",A,"fill",P(c2["challenge"])))
O.append(F(f'<div style="border-top:2px solid {T};border-bottom:1px solid var(--rule);padding:var(--s5) 0;"><div style="display:flex;align-items:center;gap:9px;margin-bottom:var(--s4);">{D.dot(T,"ring",10)}<p class="lbl" style="color:{T};font-size:10.5px;">Authorship</p></div><p class="d2" style="margin-bottom:var(--s4);">I did not design this app.</p><p style="font-size:16px;line-height:1.8;color:var(--body);margin:0;">{role2[0].split("I did not design this app. ",1)[-1]}</p></div>',pt=36))
O.append(blk("What I did",A,"fill",P(role2[1:]),pt=34)); O.append(blk("How",A,"fill",deflist(c2["approach"])))

O.append("@@SPLIT@@")
PH=[("mytoyota-01-home.jpg","MyToyota, home","Public App Store listing"),("lexus-01-dashboard.jpg","Lexus Link+, home","Public App Store listing"),("mytoyota-03-car-status.jpg","MyToyota, vehicle status","Public App Store listing"),("lexus-03-vehicle-status.jpg","Lexus Link+, vehicle status","Public App Store listing")]
phones=f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s4);">'+"".join(plate(s,w,p,aspect="9 / 16") for s,w,p in PH)+'</div>'
bl="".join(f'<div style="display:grid;grid-template-columns:20px 1fr;gap:11px;align-items:center;margin-bottom:9px;"><p style="font-size:11px;color:var(--faint);margin:0;">0{i+1}</p><div style="border:1px solid var(--rule-2);border-radius:6px;background:var(--paper);padding:11px 13px;"><p style="font-size:13px;color:var(--body);margin:0;">{t}</p></div></div>' for i,t in enumerate(D.EV_BEFORE))
aft="".join(f'<div style="border:1px solid oklch(0.86 0.022 195);border-radius:5px;background:oklch(0.995 0.002 195);padding:9px 11px;"><p style="font-size:12.5px;color:oklch(0.42 0.020 195);margin:0;">{t}</p></div>' for t in D.EV_AFTER)
TEAMBODY=[f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s3);">{D.dot(T,"ring",11)}<p class="lbl" style="color:{T};font-size:10.5px;">{c2["info"]["aside-label"]}</p></div><p class="d2" style="margin-bottom:var(--s4);">Everything on this ground is theirs</p><p style="font-size:15.5px;line-height:1.8;color:oklch(0.40 0.020 195);margin:0 0 var(--s6);">The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p>',
  phones,'<div style="height:44px;"></div>',
  fig("Case two &middot; what the team built",T,"ring","One EV domain in place of four","For an EV driver the questions are constant. Am I charged, can I leave, when will it be ready. The answers were scattered across the app.",
    f'<p class="lbl" style="font-size:10px;margin-bottom:var(--s3);">Before &middot; four places, one job</p>{bl}<div style="display:flex;justify-content:center;padding:var(--s4) 0;"><div style="width:1px;height:26px;background:{T};"></div></div><p class="lbl" style="color:{T};font-size:10px;margin-bottom:var(--s3);">After &middot; one place, at the point of use</p><div style="border:1.5px solid {T};border-radius:8px;background:oklch(0.985 0.008 195);padding:14px;"><p style="font-size:13px;font-weight:600;color:var(--ink);margin:0 0 10px;">EV domain</p><div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;">{aft}</div><p style="font-size:11.5px;line-height:1.5;color:{T};margin:12px 0 0;">Real-time status, mirroring what is happening at the car.</p></div>',
    foot="My call was that EV had to be solved as one experience rather than patched feature by feature."),
  '<div style="height:40px;"></div>',
  fig("Case two &middot; what the team built",T,"ring","Four rounds, against the same task set","System Usability Scale, measured round by round on a fixed set of EV tasks.",
    '<svg viewBox="0 0 300 190" width="100%" height="190" preserveAspectRatio="none" style="display:block;" aria-label="SUS scores rising across rounds"><rect x="228" y="0" width="72" height="190" fill="#e6ebea"></rect><line x1="0" y1="1" x2="300" y2="1" stroke="#d9e2e1"></line><line x1="0" y1="95" x2="300" y2="95" stroke="#d9e2e1"></line><line x1="0" y1="189" x2="300" y2="189" stroke="#c3d0ce"></line><line x1="0" y1="25" x2="300" y2="25" stroke="#a97739" stroke-width="1.5" stroke-dasharray="5 5"></line><line x1="0" y1="139" x2="300" y2="139" stroke="#9fb0ae" stroke-dasharray="3 5"></line><polyline points="40,108 116,70 192,63" fill="none" stroke="#3f7d7a" stroke-width="2.5"></polyline><circle cx="40" cy="108" r="5" fill="#3f7d7a"></circle><circle cx="116" cy="70" r="5" fill="#3f7d7a"></circle><circle cx="192" cy="63" r="5" fill="#3f7d7a"></circle>'
    f'<text x="40" y="98" text-anchor="middle" {SVGF} font-size="14" font-weight="700" fill="#1e1a16">73</text><text x="116" y="60" text-anchor="middle" {SVGF} font-size="14" font-weight="700" fill="#1e1a16">79</text><text x="192" y="53" text-anchor="middle" {SVGF} font-size="14" font-weight="700" fill="#1e1a16">80</text><text x="297" y="20" text-anchor="end" {SVGF} font-size="9.5" font-weight="700" fill="#a97739">TARGET 86</text><text x="297" y="134" text-anchor="end" {SVGF} font-size="9.5" font-weight="700" fill="#7d8c8a">GLOBAL AVERAGE 68</text></svg>'
    '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:7px;">'+"".join(f'<p class="lbl" style="font-size:9.5px;text-align:center;">R{i}</p>' for i in [1,2,3,4])+'</div>',
    foot="Three reported SUS scores. The fourth round was run to task-completion target. My part was funding the four rounds against a delivery schedule."),
  f'<div style="margin-top:var(--s6);">{head("And the rest of it",T,"ring")}{P(hard2[1:2],colour="oklch(0.40 0.020 195)")}<div style="margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid oklch(0.87 0.020 195);display:flex;gap:11px;align-items:flex-start;">{D.dot(T,"ring",10)}<p style="font-size:14.5px;line-height:1.75;color:{T};margin:-4px 0 0;">{hard2[2]}</p></div></div>']
O.append(F("".join(TEAMBODY),pt=56,pb=56,bg="var(--paper-team)"))
bt=[]
for i,(d,h,t,last) in enumerate(D.BEATS):
    stem='<div style="width:1px;flex-grow:1;min-height:80px;background:var(--night-rule);"></div>' if i<3 else ""
    mark=f'<span style="width:9px;height:9px;border-radius:50%;{"border:2px solid "+TD+";box-sizing:border-box;" if last else "background:"+AD+";"}display:inline-block;"></span>'
    bt.append(f'<div style="display:grid;grid-template-columns:18px 1fr;gap:14px;align-items:start;padding-bottom:var(--s6);"><div style="display:flex;flex-direction:column;align-items:center;gap:5px;padding-top:4px;">{mark}{stem}</div><div><p class="lbl" style="color:{TD if last else AD};font-size:10px;margin-bottom:var(--s2);">{d}</p><p style="font-size:16.5px;font-weight:600;color:var(--night-ink);margin:0 0 var(--s2);line-height:1.35;letter-spacing:-0.012em;">{h}</p><p style="font-size:13px;line-height:1.7;color:var(--night-muted);margin:0;">{t}</p></div></div>')
O.append(B(f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {AD};margin-bottom:var(--s3);">{D.dot(AD,"fill",9)}<p class="lbl" style="color:{AD};font-size:10.5px;">Case two &middot; the outcome</p></div><p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);">Thirteen months from complaint driver to differentiator</p><p style="font-size:14px;line-height:1.75;color:var(--night-muted);margin:0 0 var(--s6);">Design dominated the complaint list when the repurposed app landed. Then it left the list altogether.</p>'+"".join(bt),pt=48,pb=32))
O.append(F(fig("Case two &middot; the public proof",A,"fill","The public rating data","The rating, and the share of reviews behind it.",
  '<div style="display:flex;align-items:flex-end;gap:14px;margin-bottom:var(--s6);"><div><p class="lbl" style="color:var(--faint);font-size:10px;margin-bottom:2px;">At launch</p><p class="stat" style="font-size:40px;color:var(--muted);">1.9<span style="font-size:0.5em;color:#f2b632;vertical-align:0.35em;margin-left:0.06em;">&#9733;</span></p></div><p style="font-size:24px;color:var(--rule-2);padding-bottom:6px;margin:0;">&rarr;</p>'
  f'<div><p class="lbl" style="color:{A};font-size:10px;margin-bottom:2px;">August 2025</p><p class="stat" style="font-size:40px;">4.6<span style="font-size:0.5em;color:#f2b632;vertical-align:0.35em;margin-left:0.06em;">&#9733;</span></p></div></div>'
  '<p class="lbl" style="font-size:10px;padding-bottom:9px;border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Share of reviews, by star rating</p><p style="font-size:12.5px;font-weight:600;color:var(--muted);margin:0 0 6px;">Before</p><div style="display:flex;height:38px;border-radius:3px;overflow:hidden;margin-bottom:var(--s4);"><div style="width:67%;background:#ec7b72;display:flex;align-items:center;padding-left:8px;"><p style="font-size:12px;color:#fff;margin:0;">1&#9733; 67%</p></div><div style="width:19%;background:#f6d56b;"></div><div style="width:14%;background:#7bbf84;"></div></div>'
  '<p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:0 0 6px;">After</p><div style="display:flex;height:38px;border-radius:3px;overflow:hidden;"><div style="width:5%;background:#ec7b72;"></div><div style="width:17%;background:#f6d56b;"></div><div style="width:78%;background:#7bbf84;display:flex;align-items:center;padding-left:10px;"><p style="font-size:12px;color:#fff;margin:0;">5&#9733; 78%</p></div></div><p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:var(--s4) 0 0;">One star: 2 in 3 &rarr; 1 in 20</p>',
  foot="Public App Store and Play Store data. Lexus Link+; MyToyota shows the same pattern."),pt=40))
O.append(blk("What changed",A,"fill",P(c2["impact"][:1])+quote(c2["impact"][1],cls="d4"))); O.append('<div style="height:56px;"></div>'); O.append("@@SPLIT@@")

# ---- case three, EV ----
O.append(opener(c3,TD,"ring")); O.append(blk("The challenge",A,"fill",P(c3["challenge"]))); O.append(blk("Whose work",T,"ring",P(c3["role"]),pt=34))
O.append(F(C.ev_measure(mobile=True),pt=40))
O.append(blk("What was found, and what was decided",A,"fill",deflist(c3["approach"]))); O.append(blk("What changed",A,"fill",P(c3["impact"],size=17,colour="var(--ink)"),pt=34))
O.append('<div style="height:56px;"></div>'); O.append("@@SPLIT@@")

# ---- case four ----
pair=(f'<div style="margin-bottom:var(--s5);">{plate("emotrix-timeline.jpg","The reading. Five constructs against the participant&rsquo;s own baseline, two interpreted lines above them, hatched where no reading is asserted.","Emotrix, real interface, synthetic session",dark=True)}</div>'
      f'<div style="margin-bottom:var(--s5);">{plate("prepcall-report-listening.jpg","What the product does with it. The listening half of a coaching report.","PrepCall, illustrative report (real frame to follow)",dark=True)}</div>'
      f'<p style="font-size:15.5px;line-height:1.7;font-weight:500;color:var(--night-ink);margin:0 0 var(--s6);">Signal above, meaning below. The design work is the layer between them, in both products.</p>')
O.append(opener(c4,"var(--night-ink)","fill",extra=pair)); O.append(blk("The challenge",INK,"fill",P(c4["challenge"]))); O.append(blk("My role",INK,"fill",P(c4["role"]),pt=34))
O.append(blk(c4["info"]["narrative-label"],INK,"fill",P(c4["narrative"])))
O.append(F(f'<div style="margin-bottom:var(--s5);">{plate("emotrix-stage.jpg","Emotrix session review. The video pane is withheld; the readings, the moments and the channel quality sit beside it.","Real interface, synthetic session")}</div>{plate("emotrix-cloud-hero.jpg","emotrix.cloud. The thesis, stated in public.","Live site, September 2026")}',pt=40))
O.append(blk("What I learned building it",INK,"fill",deflist(c4["approach"])))
O.append(F(fig("Case three &middot; the failure that taught me most",A,"fill","Everything was working. The prompt had grown six times.","Quality started degrading around the fourth session per user. Context had simply accumulated until the model was drowning in its own history.",
  '<svg viewBox="0 0 300 200" width="100%" height="200" preserveAspectRatio="none" style="display:block;" aria-label="System prompt characters growing session one to four"><line x1="0" y1="1" x2="300" y2="1" stroke="#e8e2da"></line><line x1="0" y1="100" x2="300" y2="100" stroke="#e8e2da"></line><line x1="0" y1="199" x2="300" y2="199" stroke="#d5cabb"></line><polygon points="70,168 230,20 230,199 70,199" fill="#efe9e1"></polygon><rect x="24" y="168" width="46" height="31" fill="#c5b9a8"></rect><rect x="230" y="12" width="46" height="187" fill="#1e1a16"></rect><line x1="0" y1="154" x2="300" y2="154" stroke="#a97739" stroke-width="2" stroke-dasharray="6 5"></line>'
  f'<text x="297" y="149" text-anchor="end" {SVGF} font-size="9.5" font-weight="700" fill="#a97739">BOUNDED PROMPT: HARD BUDGET</text><text x="47" y="160" text-anchor="middle" {SVGF} font-size="13" font-weight="700" fill="#1e1a16">5,600</text><text x="253" y="6" text-anchor="middle" {SVGF} font-size="13" font-weight="700" fill="#1e1a16">34,000+</text></svg>'
  '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:7px;"><p class="lbl" style="font-size:9.5px;text-align:center;">S1</p><p class="lbl" style="font-size:9.5px;text-align:center;color:var(--faint);">2</p><p class="lbl" style="font-size:9.5px;text-align:center;color:var(--faint);">3</p><p class="lbl" style="font-size:9.5px;text-align:center;">S4</p></div>',
  foot="The fix was architectural. A bounded prompt with hard character budgets, enforced however many sessions a user has had."),pt=40))
O.append(blk(c4["info"]["aside-label"],INK,"fill",f'<div style="border:1px solid var(--rule-2);padding:var(--s4);">{P(c4["hard"],size=15)}</div>'))
O.append(blk("Where it stands",INK,"fill",P(c4["impact"],size=17,colour="var(--ink)")))
O.append(blk("Governance",INK,"fill",P(GOV,size=15.5)+'<div style="margin-top:var(--s5);">'+"".join(
  f'<div style="border-top:1px solid var(--rule);padding:var(--s3) 0;"><p style="font-size:14px;font-weight:600;color:var(--ink);margin:0 0 3px;">{a}</p><p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{b}</p></div>'
  for a,b in [("EU AI Act, Article 5","Classification and the data protection impact assessment, on a shipped product"),("European Accessibility Act","Governance across a whole design function, turned into a four-tier service"),("Regulated automotive delivery","Every programme in the first three cases")])+'</div>'))
O.append('<div style="height:64px;"></div>')
O.append(B(f'<p class="lbl" style="color:{AD};font-size:10.5px;margin-bottom:var(--s4);">The pattern</p><p style="font-size:17px;line-height:1.8;color:var(--night-body);margin:0 0 var(--s6);">{W.CLOSING[0]}</p><p style="font-size:15px;line-height:1.8;color:var(--night-muted);margin:0 0 var(--s5);">The last part is the one people underestimate.</p><p class="d2" style="color:var(--night-ink);margin:0;">Most of what I am proudest of was drawn by somebody else.</p>',pt=64,pb=64))
O.append(F(f'<p class="lbl" style="margin-bottom:var(--s3);">Contact</p><p class="d4" style="font-size:20px;margin-bottom:var(--s4);">{W.CONTACT[0]}</p><p style="font-size:16px;line-height:1.8;color:var(--body);margin:0;">{W.CONTACT[1]}</p>',pt=56,pb=48))
O.append(f'<div style="padding:20px {PAD}px 40px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;"><p class="t3" style="color:var(--faint);">&copy; 2026 Gideon Bullock</p><p class="t3" style="color:var(--faint);">gideonb.me</p></div>')

NAMES=["Mobile","MobOneA","MobOneB","MobOneC","MobTwoA","MobTwoB","MobEV","MobThree"]
LABELS=["","Continues from the opening","Case one continues","Case one continues","Continues from case one","Case two continues","Continues from case two","Continues from case three"]
segs=[[]]
for item in O:
    if item=="@@SPLIT@@": segs.append([])
    else: segs[-1].append(item)
assert len(segs)==len(NAMES), (len(segs),len(NAMES))
for name,label,seg in zip(NAMES,LABELS,segs):
    cont=f'<div style="background:var(--paper-2);padding:8px 22px;"><p class="lbl" style="color:var(--faint);font-size:9.5px;">{label}</p></div>' if label else ""
    open(f"{name}.dc.html","w").write(HEAD+'<div style="width:390px;box-sizing:border-box;background:var(--paper);">'+cont+"\n".join(seg)+'</div>\n'+TAIL)
out=sys.argv[1] if len(sys.argv)>1 else "."
open(os.path.join(out,"full-mobile.dc.html"),"w").write(HEAD+'<div style="width:390px;box-sizing:border-box;background:var(--paper);">'+"\n".join(i for i in O if i!="@@SPLIT@@")+'</div>\n'+TAIL)
print("mobile sections:", ", ".join(NAMES))
