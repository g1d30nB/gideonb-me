from copy import *   # noqa
import diagrams as D
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"; AD="var(--amber-d)"; TD="var(--teal-d)"
PAD=22

def F(h,pt=0,pb=0,bg=None):
    b=f'background:{bg};' if bg else ""
    return f'<div style="{b}padding:{pt}px {PAD}px {pb}px;box-sizing:border-box;">{h}</div>'
def B(h,pt=48,pb=44): return F(h,pt,pb,bg="var(--night)").replace('box-sizing:border-box;','box-sizing:border-box;color:var(--night-body);')
def head(label,colour,kind):
    return (f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {colour};margin-bottom:var(--s3);">'
            f'{D.dot(colour,kind,9)}<p class="lbl" style="color:{colour};font-size:10.5px;">{label}</p></div>')
def P(items,size=16,colour="var(--body)",mb=16):
    return "".join(f'<p style="font-size:{size}px;line-height:1.75;color:{colour};margin:0 0 {0 if i==len(items)-1 else mb}px;">{p}</p>' for i,p in enumerate(items))
def blk(label,colour,kind,body,pt=40,bg=None): return F(head(label,colour,kind)+body,pt=pt,bg=bg)
def deflist(items):
    return "".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);margin-bottom:var(--s5);">'
                   f'<p class="d4" style="font-size:18px;margin-bottom:7px;">{a}</p>'
                   f'<p style="font-size:14.5px;line-height:1.75;color:var(--body);margin:0;">{b}</p></div>' for a,b in items)
def quote(t,colour=A,size="d3"):
    return (f'<div style="margin-top:var(--s6);"><div style="width:40px;height:3px;background:{colour};margin-bottom:var(--s3);"></div>'
            f'<p class="{size}">{t}</p></div>')
def fig(kick,colour,kind,title,sub,body,foot="",bg=None):
    b=f'background:{bg};padding:var(--s5) var(--s5);margin:0 calc(-1 * var(--s3));' if bg else ""
    f=(f'<p style="font-size:13px;line-height:1.65;color:var(--ink);margin:var(--s4) 0 0;padding-top:var(--s3);'
       f'border-top:1px solid var(--rule);font-weight:500;">{foot}</p>') if foot else ""
    return (f'<div style="{b}">{head(kick,colour,kind)}'
            f'<p class="d3" style="margin-bottom:var(--s2);">{title}</p>'
            f'<p style="font-size:14px;line-height:1.65;color:var(--muted);margin:0 0 var(--s5);">{sub}</p>{body}{f}</div>')

def statgrid(stats,dark=True):
    ink="var(--night-ink)" if dark else "var(--ink)"; lab="var(--night-muted)" if dark else "var(--muted)"
    rule="var(--night-rule)" if dark else "var(--rule)"
    return (f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s5) var(--s4);'
            f'border-top:1px solid {rule};padding-top:var(--s5);">'
            + "".join(f'<div><p class="stat" style="color:{ink};font-size:28px;margin-bottom:6px;">{v}</p>'
                      f'<p style="font-size:12px;line-height:1.45;color:{lab};margin:0;">{l}</p></div>' for v,l in stats) + '</div>')

def openband(c,dcol,kind):
    return B(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s4);">{D.dot(dcol,kind,11)}'
      f'<p class="lbl" style="color:{dcol};font-size:10.5px;">{c["num"]}</p></div>'
      f'<p class="d2" style="color:var(--night-ink);margin-bottom:var(--s4);">{c["title"]}</p>'
      f'<p style="font-size:13px;color:var(--night-muted);margin:0 0 12px;">{c["meta"]}</p>'
      f'<p style="font-size:16px;line-height:1.8;color:var(--night-body);margin:0 0 var(--s7);">{c["role"]}</p>'
      f'{statgrid(c["stats"])}', pt=56, pb=52)

O=['<div style="width:390px;box-sizing:border-box;background:var(--paper);">']
O.append(f'<div style="border-bottom:1px solid var(--rule);padding:16px {PAD}px;display:flex;justify-content:space-between;align-items:center;">'
 '<p style="font-size:14px;font-weight:600;color:var(--ink);margin:0;">Gideon Bullock</p>'
 '<div style="display:flex;gap:16px;"><p class="lbl" style="font-size:10px;font-weight:500;">Home</p>'
 '<p class="lbl" style="font-size:10px;font-weight:500;color:var(--ink);">Work</p>'
 '<p class="lbl" style="font-size:10px;font-weight:500;">Writing</p></div></div>')
O.append(F('<p class="lbl" style="margin-bottom:var(--s3);">Selected Work</p>'
 '<p class="d1" style="margin-bottom:var(--s5);">Three cases</p>'
 f'<p style="font-size:17.5px;line-height:1.7;color:var(--body);margin:0 0 var(--s4);">{INTRO[0]}</p>'
 f'<p style="font-size:15px;line-height:1.8;color:var(--muted);margin:0;">{INTRO[1]}</p>', pt=48))

g=[]
for i,(lb,t,m,n,e,k) in enumerate(GAUGE):
    c={"#b07a3c":A,"#3f7d7a":T,"#1e1a16":INK}[e]
    stem='<div style="width:1px;flex-grow:1;min-height:64px;background:var(--rule);"></div>' if i<2 else ""
    g.append(f'<div style="display:grid;grid-template-columns:22px 1fr;gap:14px;align-items:start;padding:var(--s5) 0;border-top:1px solid var(--rule);">'
      f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px;padding-top:3px;">{D.dot(c,k if k=="ring" else "fill",12)}{stem}</div>'
      f'<div><p class="lbl" style="color:{c};font-size:10.5px;margin-bottom:6px;">{lb}</p>'
      f'<p class="d4" style="font-size:23px;margin-bottom:7px;">{t}</p>'
      f'<p style="font-size:12.5px;line-height:1.6;color:var(--muted);margin:0 0 9px;">{m}</p>'
      f'<p style="font-size:15px;line-height:1.7;color:var(--body);margin:0;">{n}</p></div></div>')
O.append(F('<p class="lbl" style="font-size:9.5px;margin-bottom:var(--s1);">The business behind the work</p>'
 +"".join(g)+
 '<p class="lbl" style="font-size:9.5px;text-align:right;padding-top:var(--s4);border-top:1px solid var(--rule);">The drawing itself</p>'
 f'<p class="t3" style="margin-top:var(--s6);padding-top:var(--s4);border-top:1px solid var(--rule);">{CONFID}</p>', pt=44, pb=56))

# CASE ONE
O.append(openband(C1,AD,"fill"))
O.append(blk("The challenge",A,"fill",P(C1["challenge"])))
O.append(blk("My role",A,"fill",P(C1["myrole"]),pt=34))
O.append(blk("How the capability grew",A,"fill",P(C1["narr1"])))
rows=[]
for i,(k,n,why,earn,_,_,_) in enumerate(D.ARC_STEPS):
    last=i==3; w=[26,46,70,100][i]
    if last:
        rows.append('<div style="display:flex;align-items:center;gap:10px;margin:var(--s5) 0;">'
          '<div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div>'
          '<p class="lbl" style="color:var(--amber);font-size:9.5px;white-space:nowrap;">The question changed</p>'
          '<div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div></div>')
    rows.append(f'<div style="border-top:{"3px solid var(--amber)" if last else "2px solid var(--rule-2)"};padding-top:var(--s3);margin-bottom:var(--s5);">'
      f'<p class="lbl" style="color:{A if last else "var(--faint)"};font-size:10px;margin-bottom:7px;">{k}</p>'
      f'<p class="d4" style="font-size:20px;margin-bottom:var(--s2);">{n}</p>'
      f'<p style="font-size:13.5px;line-height:1.6;color:var(--body);margin:0 0 10px;">{why}</p>'
      f'<div style="height:9px;background:oklch(0.93 0.030 68);width:{w}%;margin-bottom:7px;"></div>'
      f'<p style="font-size:12px;line-height:1.5;color:var(--muted);margin:0;"><span style="color:{A};font-weight:600;">Earned &rarr;</span> {earn}</p></div>')
O.append(F(fig("Case one &middot; the spine",A,"fill","How the capability grew",
  "Four capabilities, in the order they were established. Each one earned the next. The bar under each is how much of the customer&rsquo;s experience design was allowed to own.",
  "".join(rows), foot="The widest brief was the one nobody had asked for."), pt=40))
O.append(blk("The turn",A,"fill",P(C1["narr2"])+quote(C1["pull"])))

sl=[]
for i,(n,o,mine) in enumerate(D.SLICES):
    if i>0: sl.append('<div style="display:flex;align-items:center;gap:9px;padding:7px 0 7px 5px;">'
        '<span style="width:10px;height:10px;border:1.5px dashed oklch(0.50 0.035 70);border-radius:50%;"></span>'
        '<p style="font-size:11.5px;color:oklch(0.60 0.040 70);margin:0;">no owner</p></div>')
    sl.append(f'<div style="border:{"1.5px solid var(--amber-d)" if mine else "1px solid var(--night-rule)"};'
      f'background:{"var(--night-2)" if mine else "transparent"};border-radius:3px;padding:var(--s3) 13px;">'
      f'<p style="font-size:13.5px;font-weight:600;color:{"var(--night-ink)" if mine else "var(--night-body)"};margin:0 0 4px;">{n}</p>'
      f'<p style="font-size:11.5px;color:{AD if mine else "var(--night-muted)"};margin:0;">{o}</p></div>')
after="".join(f'<div style="border:1px solid oklch(0.33 0.020 190);border-radius:3px;padding:9px 12px;margin-bottom:7px;">'
              f'<p style="font-size:12.5px;color:var(--night-body);margin:0;">{n}</p></div>' for n,_,_ in D.SLICES)
O.append(B(f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {AD};margin-bottom:var(--s3);">'
 f'{D.dot(AD,"fill",9)}<p class="lbl" style="color:{AD};font-size:10.5px;">Case one &middot; what service design was for</p></div>'
 '<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);">A disjointed experience is a faithful picture of a disjointed business</p>'
 '<p style="font-size:14px;line-height:1.75;color:var(--night-muted);margin:0 0 var(--s6);">No Toyota blueprint is shown. This is the shape of the problem.</p>'
 '<p class="lbl" style="color:var(--night-muted);font-size:10px;margin-bottom:var(--s3);">Before &middot; one slice, behaving as though it owned all of them</p>'
 +"".join(sl)+
 f'<p class="lbl" style="color:{TD};font-size:10px;margin:var(--s6) 0 var(--s3);">After &middot; one journey, owned together</p>'
 f'<div style="border:1.5px solid {TD};background:oklch(0.225 0.022 190);border-radius:3px;padding:13px;margin-bottom:10px;">'
 f'<p style="font-size:13.5px;font-weight:600;color:var(--night-ink);margin:0 0 4px;">One end-to-end journey</p>'
 f'<p style="font-size:11.5px;color:{TD};margin:0;">Blueprinted front stage and back, reusable as service patterns</p></div>'
 +after+
 '<p style="font-size:15.5px;line-height:1.75;color:var(--night-ink);margin:var(--s5) 0 0;font-weight:500;">Business units that had never designed anything together started working on the same journey. They are still doing it, which is the part I am most confident about, because it outlasted me.</p>'))

O.append(blk("What it left behind",A,"fill",P(C1["narr3"])+
 f'<div style="margin:var(--s5) 0;background:var(--paper-team);border:1px solid oklch(0.87 0.020 195);padding:var(--s4);">'
 f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:9px;">{D.dot(T,"ring",10)}'
 f'<p class="lbl" style="color:{T};font-size:10px;">The team&rsquo;s work</p></div>'
 f'<p style="font-size:15.5px;line-height:1.75;color:oklch(0.38 0.022 195);margin:0;">{C1["credit"]}</p></div>'+P(C1["narr4"])))

dl="".join(f'<div style="padding:var(--s3) 0;border-bottom:1px solid var(--rule);">'
  f'<p style="font-size:14.5px;font-weight:600;color:{A if m else "var(--ink)"};margin:0 0 3px;">{n}</p>'
  f'<p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{d}</p></div>' for n,d,m in D.DISCIPLINES)
ml="".join(f'<div style="padding:var(--s3) 0;border-bottom:1px solid var(--rule);">'
  f'<p style="font-size:14.5px;font-weight:600;color:var(--ink);margin:0 0 7px;">{n}</p>'
  f'<div style="height:8px;background:oklch(0.93 0.030 68);width:{w}%;margin-bottom:6px;"></div>'
  f'<p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{d}</p></div>' for n,d,w,_,_ in D.MODELS)
O.append(F(fig("Case one &middot; how it was run",A,"fill","An internal consultancy, not a service desk",
 "Six disciplines under one roof, and four ways to buy them. A service catalogue, explicit positioning, and a P&amp;L.",
 f'<p class="lbl" style="font-size:10px;padding-bottom:9px;border-bottom:1px solid var(--rule-2);">Six disciplines, one team</p>{dl}'
 f'<p class="lbl" style="font-size:10px;padding-bottom:9px;border-bottom:1px solid var(--rule-2);margin-top:var(--s5);">Four engagement models, shallow to deep</p>{ml}',
 foot="Design&rsquo;s commercial contribution became visible to senior leadership for the first time."), pt=40))
O.append(blk("How it was run",A,"fill",deflist(C1["approach"])))
O.append(blk("The hardest part",A,"fill",P(C1["hard"])))
O.append(blk("What changed",A,"fill",P(C1["impact"],size=17,colour="var(--ink)"),pt=34))
O.append('<div style="height:56px;"></div>')

# CASE TWO
O.append(openband(C2,TD,"ring"))
O.append(blk("The challenge",A,"fill",P(C2["challenge"])))
O.append(F(f'<div style="border-top:2px solid {T};border-bottom:1px solid var(--rule);padding:var(--s5) 0;">'
 f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:var(--s4);">{D.dot(T,"ring",10)}'
 f'<p class="lbl" style="color:{T};font-size:10.5px;">Authorship</p></div>'
 f'<p class="d2" style="margin-bottom:var(--s4);">{C2["disclaim"]}</p>'
 f'<p style="font-size:16px;line-height:1.8;color:var(--body);margin:0;">{C2["disclaim2"]}</p></div>', pt=36))
O.append(blk("What I did instead",A,"fill",P(C2["myrole"]),pt=34))
O.append(blk("How",A,"fill",deflist(C2["approach"])))
res="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);">'
  f'<p class="stat" style="font-size:26px;margin-bottom:4px;">{v}</p>'
  f'<p style="font-size:11.5px;line-height:1.45;color:var(--muted);margin:0;">{l}</p></div>' for v,l in C2["research"])
O.append(F(fig("Case two &middot; what the research bought",A,"fill","Before a single screen was redrawn",
 "UX research was not part of Toyota&rsquo;s playbook. I pitched its value and funded a dedicated research team inside the app organisation.",
 f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s4);">{res}</div>'), pt=40))

# team ground begins
TEAMBODY=[]
TEAMBODY.append(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s3);">{D.dot(T,"ring",11)}'
 f'<p class="lbl" style="color:{T};font-size:10.5px;">What the team built</p></div>'
 f'<p class="d2" style="margin-bottom:var(--s4);">Everything on this ground is theirs</p>'
 f'<p style="font-size:15.5px;line-height:1.8;color:oklch(0.40 0.020 195);margin:0 0 var(--s7);">The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p>')
bl="".join(f'<div style="display:grid;grid-template-columns:20px 1fr;gap:11px;align-items:center;margin-bottom:9px;">'
  f'<p style="font-size:11px;color:var(--faint);margin:0;">0{i+1}</p>'
  f'<div style="border:1px solid var(--rule-2);border-radius:6px;background:var(--paper);padding:11px 13px;">'
  f'<p style="font-size:13px;color:var(--body);margin:0;">{t}</p></div></div>' for i,t in enumerate(D.EV_BEFORE))
aft="".join(f'<div style="border:1px solid oklch(0.86 0.022 195);border-radius:5px;background:oklch(0.995 0.002 195);padding:9px 11px;">'
  f'<p style="font-size:12.5px;color:oklch(0.42 0.020 195);margin:0;">{t}</p></div>' for t in D.EV_AFTER)
TEAMBODY.append(fig("Case two &middot; what the team built",T,"ring","One EV domain in place of four",
 "For an EV driver the questions are constant: am I charged, can I leave, when will it be ready. The answers were scattered across the app.",
 f'<p class="lbl" style="font-size:10px;margin-bottom:var(--s3);">Before &middot; four places, one job</p>{bl}'
 f'<div style="display:flex;justify-content:center;padding:var(--s4) 0;"><div style="width:1px;height:26px;background:{T};"></div></div>'
 f'<p class="lbl" style="color:{T};font-size:10px;margin-bottom:var(--s3);">After &middot; one place, at the point of use</p>'
 f'<div style="border:1.5px solid {T};border-radius:8px;background:oklch(0.985 0.008 195);padding:14px;">'
 f'<p style="font-size:13px;font-weight:600;color:var(--ink);margin:0 0 10px;">EV domain</p>'
 f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;">{aft}</div>'
 f'<p style="font-size:11.5px;line-height:1.5;color:{T};margin:12px 0 0;">Real-time status, mirroring what is happening at the car.</p></div>',
 foot="My call was that EV had to be solved as one experience rather than patched feature by feature."))
TEAMBODY.append('<div style="height:40px;"></div>')
TEAMBODY.append(fig("Case two &middot; what the team built",T,"ring","Four rounds, against the same task set",
 "System Usability Scale, measured round by round on a fixed set of EV tasks.",
 '<svg viewBox="0 0 300 190" width="100%" height="190" preserveAspectRatio="none" style="display:block;" aria-label="SUS scores rising across rounds">'
 '<rect x="228" y="0" width="72" height="190" fill="#e6ebea"></rect>'
 '<line x1="0" y1="1" x2="300" y2="1" stroke="#d9e2e1"></line><line x1="0" y1="95" x2="300" y2="95" stroke="#d9e2e1"></line>'
 '<line x1="0" y1="189" x2="300" y2="189" stroke="#c3d0ce"></line>'
 '<line x1="0" y1="25" x2="300" y2="25" stroke="#a97739" stroke-width="1.5" stroke-dasharray="5 5"></line>'
 '<line x1="0" y1="139" x2="300" y2="139" stroke="#9fb0ae" stroke-dasharray="3 5"></line>'
 '<polyline points="40,108 116,70 192,63" fill="none" stroke="#3f7d7a" stroke-width="2.5"></polyline>'
 '<circle cx="40" cy="108" r="5" fill="#3f7d7a"></circle><circle cx="116" cy="70" r="5" fill="#3f7d7a"></circle><circle cx="192" cy="63" r="5" fill="#3f7d7a"></circle>'
 '<text x="40" y="98" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="14" font-weight="700" fill="#1e1a16">73</text>'
 '<text x="116" y="60" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="14" font-weight="700" fill="#1e1a16">79</text>'
 '<text x="192" y="53" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="14" font-weight="700" fill="#1e1a16">80</text>'
 '<text x="297" y="20" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="9.5" font-weight="700" fill="#a97739">TARGET 86</text>'
 '<text x="297" y="134" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="9.5" font-weight="700" fill="#7d8c8a">GLOBAL AVERAGE 68</text></svg>'
 '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:7px;">'
 +"".join(f'<p class="lbl" style="font-size:9.5px;text-align:center;">R{i}</p>' for i in [1,2,3,4])+'</div>',
 foot="Three reported SUS scores. The fourth round was run to task-completion target. Mine: funding four rounds against a delivery schedule."))
TEAMBODY.append(f'<div style="margin-top:var(--s6);">{head("And the rest of it",T,"ring")}'
 +P(C2["hard2"],colour="oklch(0.40 0.020 195)")+
 f'<div style="margin-top:var(--s5);padding-top:var(--s4);border-top:1px solid oklch(0.87 0.020 195);display:flex;gap:11px;align-items:flex-start;">'
 f'{D.dot(T,"ring",10)}<p style="font-size:14.5px;line-height:1.75;color:{T};margin:-4px 0 0;">{C2["credit"]}</p></div></div>')
O.append(F("".join(TEAMBODY), pt=56, pb=56, bg="var(--paper-team)"))

bt=[]
for i,(d,h,t,last) in enumerate(D.BEATS):
    stem='<div style="width:1px;flex-grow:1;min-height:80px;background:var(--night-rule);"></div>' if i<3 else ""
    mark=f'<span style="width:9px;height:9px;border-radius:50%;{"border:2px solid "+TD+";box-sizing:border-box;" if last else "background:"+AD+";"}display:inline-block;"></span>'
    bt.append(f'<div style="display:grid;grid-template-columns:18px 1fr;gap:14px;align-items:start;padding-bottom:var(--s6);">'
      f'<div style="display:flex;flex-direction:column;align-items:center;gap:5px;padding-top:4px;">{mark}{stem}</div>'
      f'<div><p class="lbl" style="color:{TD if last else AD};font-size:10px;margin-bottom:var(--s2);">{d}</p>'
      f'<p style="font-size:16.5px;font-weight:600;color:var(--night-ink);margin:0 0 var(--s2);line-height:1.35;letter-spacing:-0.012em;">{h}</p>'
      f'<p style="font-size:13px;line-height:1.7;color:var(--night-muted);margin:0;">{t}</p></div></div>')
O.append(B(f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {AD};margin-bottom:var(--s3);">'
 f'{D.dot(AD,"fill",9)}<p class="lbl" style="color:{AD};font-size:10.5px;">Case two &middot; the outcome</p></div>'
 '<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);">Thirteen months from complaint driver to differentiator</p>'
 '<p style="font-size:14px;line-height:1.75;color:var(--night-muted);margin:0 0 var(--s6);">Design dominated the complaint list when the repurposed app landed. Then it left the list altogether.</p>'
 +"".join(bt), pt=48, pb=32))

O.append(F(fig("Case two &middot; the public proof",A,"fill","What customers actually left behind",
 "The rating is the headline. The composition underneath it is the story.",
 '<div style="display:flex;align-items:flex-end;gap:14px;margin-bottom:var(--s6);">'
 '<div><p class="lbl" style="color:var(--faint);font-size:10px;margin-bottom:2px;">At launch</p>'
 '<p class="stat" style="font-size:40px;color:var(--muted);">1.9&#9733;</p></div>'
 '<p style="font-size:24px;color:var(--rule-2);padding-bottom:6px;margin:0;">&rarr;</p>'
 f'<div><p class="lbl" style="color:{A};font-size:10px;margin-bottom:2px;">August 2025</p>'
 '<p class="stat" style="font-size:40px;">4.6&#9733;</p></div></div>'
 '<p class="lbl" style="font-size:10px;padding-bottom:9px;border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Share of reviews, by star rating</p>'
 '<p style="font-size:12.5px;font-weight:600;color:var(--muted);margin:0 0 6px;">Before</p>'
 '<div style="display:flex;height:38px;border-radius:3px;overflow:hidden;margin-bottom:var(--s4);">'
 '<div style="width:67%;background:oklch(0.955 0.011 80);border:1px solid oklch(0.875 0.014 80);box-sizing:border-box;display:flex;align-items:center;padding-left:8px;">'
 '<p style="font-size:12px;color:var(--muted);margin:0;">1&#9733; 67%</p></div>'
 '<div style="width:19%;background:oklch(0.835 0.055 72);"></div><div style="width:14%;background:oklch(0.475 0.085 62);"></div></div>'
 '<p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:0 0 6px;">After</p>'
 '<div style="display:flex;height:38px;border-radius:3px;overflow:hidden;">'
 '<div style="width:4%;background:oklch(0.955 0.011 80);border:1px solid oklch(0.875 0.014 80);box-sizing:border-box;"></div>'
 '<div style="width:16%;background:oklch(0.835 0.055 72);"></div>'
 '<div style="width:80%;background:oklch(0.475 0.085 62);display:flex;align-items:center;padding-left:10px;">'
 '<p style="font-size:12px;color:oklch(0.96 0.010 80);margin:0;">5&#9733; 80%</p></div></div>'
 '<p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:var(--s4) 0 0;">One star: 2 in 3 &rarr; 1 in 25</p>',
 foot="Public App Store and Play Store data. Lexus Link+; MyToyota shows the same pattern."), pt=40))
O.append(blk("What changed",A,"fill",P(C2["impact"])+quote(C2["impact2"],size="d4")))
O.append('<div style="height:56px;"></div>')

# CASE THREE
O.append(openband(C3,"var(--night-ink)","fill"))
O.append(blk("The challenge",INK,"fill",P(C3["challenge"])))
O.append(blk("My role",INK,"fill",P(C3["myrole"]),pt=34))
O.append(F(fig("Case three &middot; the failure that taught me the most",A,"fill","Nothing was broken. The prompt had grown six times.",
 "Quality started degrading around the fourth session per user. Context had simply accumulated until the model was drowning in its own history.",
 '<svg viewBox="0 0 300 200" width="100%" height="200" preserveAspectRatio="none" style="display:block;" aria-label="System prompt characters growing session one to four">'
 '<line x1="0" y1="1" x2="300" y2="1" stroke="#e8e2da"></line><line x1="0" y1="100" x2="300" y2="100" stroke="#e8e2da"></line>'
 '<line x1="0" y1="199" x2="300" y2="199" stroke="#d5cabb"></line>'
 '<polygon points="70,168 230,20 230,199 70,199" fill="#efe9e1"></polygon>'
 '<rect x="24" y="168" width="46" height="31" fill="#c5b9a8"></rect><rect x="230" y="12" width="46" height="187" fill="#1e1a16"></rect>'
 '<line x1="0" y1="154" x2="300" y2="154" stroke="#a97739" stroke-width="2" stroke-dasharray="6 5"></line>'
 '<text x="297" y="149" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="9.5" font-weight="700" fill="#a97739">BOUNDED PROMPT: HARD BUDGET</text>'
 '<text x="47" y="160" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="13" font-weight="700" fill="#1e1a16">5,600</text>'
 '<text x="253" y="6" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="13" font-weight="700" fill="#1e1a16">34,000+</text></svg>'
 '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:7px;">'
 '<p class="lbl" style="font-size:9.5px;text-align:center;">S1</p><p class="lbl" style="font-size:9.5px;text-align:center;color:var(--faint);">2</p>'
 '<p class="lbl" style="font-size:9.5px;text-align:center;color:var(--faint);">3</p><p class="lbl" style="font-size:9.5px;text-align:center;">S4</p></div>',
 foot="The fix was architectural, not cosmetic: hard character budgets, enforced regardless of how many sessions a user has had."), pt=40))
O.append(blk("What I learned building it",INK,"fill",deflist(C3["approach"])))
O.append(blk("Where it stands",INK,"fill",P(C3["impact"],size=17,colour="var(--ink)")))
O.append('<div style="height:64px;"></div>')

O.append(B(f'<p class="lbl" style="color:{AD};font-size:10.5px;margin-bottom:var(--s4);">The pattern</p>'
 f'<p style="font-size:17px;line-height:1.8;color:var(--night-body);margin:0 0 var(--s6);">{CLOSING[0]}</p>'
 f'<p style="font-size:15px;line-height:1.8;color:var(--night-muted);margin:0 0 var(--s5);">{CLOSING_LEAD}</p>'
 f'<p class="d2" style="color:var(--night-ink);margin:0;">{CLOSING_BIG}</p>', pt=64, pb=64))
O.append(F('<p class="lbl" style="margin-bottom:var(--s3);">Contact</p>'
 f'<p class="d4" style="font-size:20px;margin-bottom:var(--s4);">{CONTACT[0]}</p>'
 f'<p style="font-size:16px;line-height:1.8;color:var(--body);margin:0;">{CONTACT[1]}</p>', pt=56, pb=48))
O.append(f'<div style="padding:20px {PAD}px 40px;border-top:1px solid var(--rule);display:flex;justify-content:space-between;">'
 '<p class="t3" style="color:var(--faint);">&copy; 2026 Gideon Bullock</p>'
 '<p class="t3" style="color:var(--faint);">gideonb.me</p></div>')
O.append('</div>')
open("Mobile.dc.html","w").write(HEAD+"\n".join(O)+"\n"+TAIL)
print("mobile ok")
