from copy import *  # noqa
AMBER="#b07a3c"; TEAL="#3f7d7a"; INK="#1e1a16"; DA="#d9a55f"; DT="#6fb0ab"
W=390; PAD=22

def dot(c,k="fill",s=10):
    if k=="ring": return f'<div style="width:{s}px;height:{s}px;border-radius:50%;border:2px solid {c};box-sizing:border-box;flex-shrink:0;"></div>'
    return f'<div style="width:{s}px;height:{s}px;border-radius:50%;background:{c};flex-shrink:0;"></div>'

def F(h,pt=0,pb=0): return f'<div style="padding:{pt}px {PAD}px {pb}px; box-sizing:border-box;">{h}</div>'
def B(h,pt=44,pb=40): return f'<div style="background:#17130f;color:#c8c0b5;padding:{pt}px {PAD}px {pb}px;box-sizing:border-box;">{h}</div>'

def P(items,size=16,colour="#5c5347",mb=16):
    return "".join(f'<p style="font-size:{size}px;line-height:1.75;color:{colour};margin:0 0 {0 if i==len(items)-1 else mb}px;">{p}</p>' for i,p in enumerate(items))

def head(label,colour,kind):
    return (f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:14px;">{dot(colour,kind,9)}'
            f'<p class="lbl" style="color:{colour};font-size:10.5px;">{label}</p></div>')

def block(label,colour,kind,body,pt=40):
    return F(head(label,colour,kind)+body,pt=pt)

def deflist(items):
    return "".join(f'<div style="border-top:1px solid #e8e2da;padding-top:14px;margin-bottom:22px;">'
                   f'<p style="font-size:15px;font-weight:600;color:#1e1a16;margin:0 0 7px;line-height:1.45;">{a}</p>'
                   f'<p style="font-size:14px;line-height:1.7;color:#6b6057;margin:0;">{b}</p></div>' for a,b in items)

def openband(c,dcol,kind):
    stats="".join(f'<div><p class="disp num" style="font-size:30px;color:#f0ebe3;margin:0 0 6px;">{v}</p>'
                  f'<p style="font-size:12px;line-height:1.45;color:#9a9086;margin:0;">{l}</p></div>' for v,l in c["stats"])
    return B(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;">{dot(dcol,kind,11)}'
             f'<p class="lbl" style="color:{dcol};font-size:10.5px;">{c["num"]}</p></div>'
             f'<p class="disp" style="font-size:36px;color:#f0ebe3;margin:0 0 16px;">{c["title"]}</p>'
             f'<p style="font-size:13px;color:#9a9086;margin:0 0 12px;">{c["meta"]}</p>'
             f'<p style="font-size:16px;line-height:1.7;color:#c8c0b5;margin:0 0 34px;">{c["role"]}</p>'
             f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;border-top:1px solid #332c25;padding-top:24px;">{stats}</div>',pt=52,pb=48)

def fig(title,kicker,sub,body,colour=AMBER,bg="#fdfcfa",border="#e8e2da",foot=""):
    return (f'<div style="border:1px solid {border};background:{bg};border-radius:4px;padding:22px 20px;">'
            f'<p class="lbl" style="color:{colour};font-size:10.5px;margin-bottom:7px;">{kicker}</p>'
            f'<p class="disp" style="font-size:24px;margin:0 0 8px;">{title}</p>'
            f'<p style="font-size:14px;line-height:1.65;color:#6b6057;margin:0 0 22px;">{sub}</p>{body}{foot}</div>')

O=[f'<div style="width:{W}px;box-sizing:border-box;background:#f8f6f2;">']

O.append(f'<div style="border-bottom:1px solid #e8e2da;padding:16px {PAD}px;display:flex;justify-content:space-between;align-items:center;">'
         '<p style="font-size:14px;font-weight:600;color:#1e1a16;margin:0;">Gideon Bullock</p>'
         '<div style="display:flex;gap:16px;"><p class="lbl" style="font-size:10px;font-weight:500;color:#8a7d6e;">Home</p>'
         '<p class="lbl" style="font-size:10px;font-weight:500;color:#1e1a16;">Work</p>'
         '<p class="lbl" style="font-size:10px;font-weight:500;color:#8a7d6e;">Writing</p></div></div>')

O.append(F('<p class="lbl" style="margin-bottom:12px;">Selected Work</p>'
   '<p class="disp" style="font-size:52px;margin:0 0 22px;">Three cases</p>'
   f'<p style="font-size:17px;line-height:1.7;color:#5c5347;margin:0 0 16px;">{INTRO[0]}</p>'
   f'<p style="font-size:15px;line-height:1.75;color:#7a6f63;margin:0;">{INTRO[1]}</p>',pt=48))

# gauge, vertical on mobile
g=[]
for i,(lbl,title,meta,note,colour,kind) in enumerate(GAUGE):
    g.append(f'<div style="display:grid;grid-template-columns:22px 1fr;gap:14px;align-items:start;padding:18px 0;border-top:1px solid #e8e2da;">'
             f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px;padding-top:3px;">{dot(colour,kind,12)}'
             f'{"<div style=\"width:1px;flex-grow:1;min-height:60px;background:#e8e2da;\"></div>" if i<2 else ""}</div>'
             f'<div><p class="lbl" style="color:{colour};font-size:10.5px;margin-bottom:6px;">{lbl}</p>'
             f'<p class="disp" style="font-size:25px;margin-bottom:7px;">{title}</p>'
             f'<p style="font-size:12.5px;line-height:1.6;color:#8a7d6e;margin:0 0 9px;">{meta}</p>'
             f'<p style="font-size:14.5px;line-height:1.7;color:#6b6057;margin:0;">{note}</p></div></div>')
O.append(F('<div style="display:flex;justify-content:space-between;margin-bottom:6px;">'
   '<p class="lbl" style="font-size:9.5px;color:#8a7d6e;">The business behind the work</p></div>'
   +"".join(g)+
   '<p class="lbl" style="font-size:9.5px;color:#8a7d6e;text-align:right;padding-top:14px;border-top:1px solid #e8e2da;">The drawing itself</p>'
   f'<div style="margin-top:30px;padding-top:18px;border-top:1px solid #e8e2da;display:flex;gap:11px;align-items:flex-start;">'
   f'<svg width="9" height="9" viewBox="0 0 10 10" style="flex-shrink:0;margin-top:6px;"><polygon points="5,0 10,5 5,10 0,5" fill="#b5a08a"></polygon></svg>'
   f'<p class="cap" style="font-size:13px;">{CONFID}</p></div>',pt=44,pb=56))

# ---- CASE ONE ----
O.append(openband(C1,DA,"fill"))
O.append(block("The challenge",AMBER,"fill",P(C1["challenge"])))
O.append(block("My role",AMBER,"fill",P(C1["myrole"]),pt=34))
O.append(block("How the capability grew",AMBER,"fill",P(C1["narr1"])))

arc_steps=[("First","UX research","Nothing could be argued without evidence, so this came first.","the right to frame the problem, not just answer it.",26,"#d8cec0"),
           ("Second","UX and interface design","The screens the business already knew it wanted.","credibility on delivery, and a place beside engineering.",46,"#d8cec0"),
           ("Third","Product design","The team moved closer to the core business.","a close enough view of the business to see what it could not see.",70,"#d8cec0"),
           ("Fourth &middot; nobody asked","Service design","Did not exist anywhere in Toyota. I made the case for it and hired into it.","the joins between business units that nobody owned.",100,AMBER)]
rows=[]
for i,(k,n,why,earn,w,rule) in enumerate(arc_steps):
    if i==3:
        rows.append('<div style="display:flex;align-items:center;gap:10px;margin:22px 0;">'
                    '<div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,#b07a3c 0 5px,transparent 5px 11px);"></div>'
                    '<p class="lbl" style="color:#b07a3c;font-size:9.5px;white-space:nowrap;">The question changed</p>'
                    '<div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,#b07a3c 0 5px,transparent 5px 11px);"></div></div>')
    rows.append(f'<div style="border-top:{"3px" if i==3 else "2px"} solid {rule};padding-top:13px;margin-bottom:20px;">'
                f'<p class="lbl" style="color:{AMBER if i==3 else "#b5a08a"};font-size:10px;margin-bottom:7px;">{k}</p>'
                f'<p class="disp" style="font-size:22px;margin-bottom:8px;">{n}</p>'
                f'<p style="font-size:13.5px;line-height:1.6;color:#6b6057;margin:0 0 10px;">{why}</p>'
                f'<div style="height:9px;background:#efe2cf;border-left:2px solid {AMBER};width:{w}%;margin-bottom:7px;"></div>'
                f'<p style="font-size:12px;line-height:1.5;color:#8a7d6e;margin:0;"><span style="color:{AMBER};">Earned &rarr;</span> {earn}</p></div>')
O.append(F(fig("How the capability grew","Case one &middot; the spine",
   "Four capabilities, in the order they were established. Each one earned the next. The bar under each is how much of the customer&rsquo;s experience design was allowed to own.",
   "".join(rows),
   foot='<p style="font-size:13px;line-height:1.6;color:#1e1a16;margin:6px 0 0;padding-top:14px;border-top:1px solid #e8e2da;font-weight:500;">The widest brief was the one nobody had asked for.</p>'),pt=40))

O.append(block("The turn",AMBER,"fill",P(C1["narr2"])+
   f'<p class="disp" style="font-size:26px;margin:26px 0 0;padding-left:18px;border-left:3px solid {AMBER};">{C1["pull"]}</p>'))

slices=[("Choosing","Another business unit",0),("Buying","Another business unit",0),
        ("Connected services","Ours. The only slice we could see.",1),("Living with it","Another business unit",0),("The next car","Another business unit",0)]
sl=[]
for i,(n,o,mine) in enumerate(slices):
    if i>0:
        sl.append('<div style="display:flex;align-items:center;gap:9px;padding:7px 0 7px 5px;">'
                  '<div style="width:10px;height:10px;border:1.5px dashed #7a6a52;border-radius:50%;"></div>'
                  '<p style="font-size:11.5px;color:#8a7a5e;margin:0;">no owner</p></div>')
    sl.append(f'<div style="border:{"1.5px solid #d9a55f" if mine else "1px solid #332c25"};background:{"#241d14" if mine else "transparent"};border-radius:3px;padding:12px 13px;">'
              f'<p style="font-size:13.5px;font-weight:600;color:{"#f0ebe3" if mine else "#c8c0b5"};margin:0 0 4px;">{n}</p>'
              f'<p style="font-size:11.5px;color:{"#d9a55f" if mine else "#6b6157"};margin:0;">{o}</p></div>')
after="".join(f'<div style="border:1px solid #2b3a38;border-radius:3px;padding:9px 12px;margin-bottom:7px;"><p style="font-size:12.5px;color:#c8c0b5;margin:0;">{n}</p></div>' for n,_,_ in slices)
O.append(B(f'<p class="lbl" style="color:{DA};font-size:10.5px;margin-bottom:8px;">Case one &middot; what service design was for</p>'
   '<p class="disp" style="font-size:30px;color:#f0ebe3;margin:0 0 12px;">A disjointed experience is a faithful picture of a disjointed business</p>'
   '<p style="font-size:14px;line-height:1.7;color:#9a9086;margin:0 0 28px;">No Toyota blueprint is shown. This is the shape of the problem.</p>'
   '<p class="lbl" style="color:#9a9086;font-size:10px;margin-bottom:12px;">Before &middot; one slice, behaving as though it owned all of them</p>'
   +"".join(sl)+
   '<p class="lbl" style="color:#6fb0ab;font-size:10px;margin:32px 0 12px;">After &middot; one journey, owned together</p>'
   '<div style="border:1.5px solid #6fb0ab;background:#12211f;border-radius:3px;padding:13px;margin-bottom:10px;">'
   '<p style="font-size:13.5px;font-weight:600;color:#f0ebe3;margin:0 0 4px;">One end-to-end journey</p>'
   '<p style="font-size:11.5px;color:#6fb0ab;margin:0;">Blueprinted front stage and back, reusable as service patterns</p></div>'
   +after+
   '<p style="font-size:15px;line-height:1.7;color:#f0ebe3;margin:24px 0 0;">Business units that had never designed anything together started working on the same journey. They are still doing it, which is the part I am most confident about, because it outlasted me.</p>',pt=48,pb=44))

O.append(block("What it left behind",AMBER,"fill",P(C1["narr3"])+
   f'<div style="margin:22px 0;padding:16px 18px;border-left:3px solid {TEAL};background:#f3f7f6;">'
   f'<div style="display:flex;align-items:center;gap:9px;margin-bottom:9px;">{dot(TEAL,"ring",10)}'
   f'<p class="lbl" style="color:{TEAL};font-size:10px;">The team&rsquo;s work</p></div>'
   f'<p style="font-size:15.5px;line-height:1.75;color:#3d4c4b;margin:0;">{C1["credit"]}</p></div>'+P(C1["narr4"])))

models=[("Innovation sprints","Fast, exploratory, time-boxed",26),("Team augmentation","Specialists into an existing team",52),
        ("Design studio","A dedicated team, scoped and delivered",76),("Embedded partnership","Full design management and operations",100)]
disc=[("Product design","Insight, journeys and the screens themselves",0),("Design systems","Components, tokens and design governance",0),
      ("UX research","Formative and evaluative customer insight",0),("Service design","Front stage experience and back stage operations",1),
      ("Content and creative","Words, tone of voice and art direction",0),("Design leadership","Vision, planning and delivery",0)]
dl="".join(f'<div style="padding:11px 0;border-bottom:1px solid #e8e2da;">'
           f'<p style="font-size:14.5px;font-weight:600;color:{AMBER if m else "#1e1a16"};margin:0 0 3px;">{n}</p>'
           f'<p style="font-size:12.5px;line-height:1.5;color:#8a7d6e;margin:0;">{d}</p></div>' for n,d,m in disc)
ml="".join(f'<div style="padding:12px 0;border-bottom:1px solid #e8e2da;">'
           f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:7px;">'
           f'<p style="font-size:14.5px;font-weight:600;color:#1e1a16;margin:0;">{n}</p></div>'
           f'<div style="height:8px;background:#efe2cf;width:{w}%;margin-bottom:6px;"></div>'
           f'<p style="font-size:12.5px;line-height:1.5;color:#8a7d6e;margin:0;">{d}</p></div>' for n,d,w in models)
O.append(F(fig("An internal consultancy, not a service desk","Case one &middot; how it was run",
   "Six disciplines under one roof, and four ways to buy them. A service catalogue, explicit positioning, and a P&amp;L.",
   f'<p class="lbl" style="color:#8a7d6e;font-size:10px;padding-bottom:9px;border-bottom:1px solid #d8cec0;margin-bottom:0;">Six disciplines, one team</p>{dl}'
   f'<p class="lbl" style="color:#8a7d6e;font-size:10px;padding-bottom:9px;border-bottom:1px solid #d8cec0;margin:26px 0 0;">Four engagement models, shallow to deep</p>{ml}',
   foot='<p style="font-size:13px;line-height:1.6;color:#1e1a16;margin:16px 0 0;font-weight:500;">Design&rsquo;s commercial contribution became visible to senior leadership for the first time.</p>'),pt=40))

O.append(block("How it was run",AMBER,"fill",deflist(C1["approach"])))
O.append(block("The hardest part",AMBER,"fill",P(C1["hard"])))
O.append(block("What changed",AMBER,"fill",P(C1["impact"],size=17,colour="#1e1a16"),pt=34))
O.append('<div style="height:56px;"></div>')

# ---- CASE TWO ----
O.append(openband(C2,DT,"ring"))
O.append(block("The challenge",AMBER,"fill",P(C2["challenge"])))
O.append(F(head("Authorship",TEAL,"ring")+
   f'<div style="border-top:2px solid {TEAL};border-bottom:1px solid #e8e2da;padding:26px 0 24px;">'
   f'<p class="disp" style="font-size:38px;margin:0 0 16px;">{C2["disclaim"]}</p>'
   f'<p style="font-size:16px;line-height:1.75;color:#5c5347;margin:0;">{C2["disclaim2"]}</p></div>',pt=36))
O.append(block("What I did instead",AMBER,"fill",P(C2["myrole"]),pt=34))
O.append(block("How",AMBER,"fill",deflist(C2["approach"])))

res="".join(f'<div style="border-top:1px solid #e8e2da;padding-top:11px;">'
            f'<p class="disp num" style="font-size:26px;margin:0 0 4px;">{v}</p>'
            f'<p style="font-size:11.5px;line-height:1.45;color:#8a7d6e;margin:0;">{l}</p></div>' for v,l in C2["research"])
O.append(F(fig("Before a single screen was redrawn","Case two &middot; what the research bought",
   "UX research was not part of Toyota&rsquo;s playbook. I pitched its value and funded a dedicated research team inside the app organisation.",
   f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;">{res}</div>'),pt=40))

O.append(F(f'<div style="border-left:3px solid {TEAL};padding:4px 0 4px 20px;">'
   f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">{dot(TEAL,"ring",11)}'
   f'<p class="lbl" style="color:{TEAL};font-size:10.5px;">What the team built</p></div>'
   f'<p class="disp" style="font-size:32px;margin:0 0 14px;">Everything from here to the credit line is theirs</p>'
   f'<p style="font-size:15.5px;line-height:1.75;color:#5c5347;margin:0;">The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p></div>',pt=52))

before_ev=["Home screen entry point, easy to miss","Battery status, tied to the default vehicle","Home charging, stored somewhere else again","Charging schedule, split across three settings"]
bl="".join(f'<div style="display:grid;grid-template-columns:20px 1fr;gap:11px;align-items:center;margin-bottom:9px;">'
           f'<p class="num" style="font-size:11px;color:#b5a08a;margin:0;">0{i+1}</p>'
           f'<div style="border:1px solid #d8cec0;border-radius:6px;background:#fdfcfa;padding:11px 13px;">'
           f'<p style="font-size:13px;color:#6b6057;margin:0;">{t}</p></div></div>' for i,t in enumerate(before_ev))
after_ev="".join(f'<div style="border:1px solid #bcd2d0;border-radius:5px;background:#ffffff;padding:9px 11px;"><p style="font-size:12.5px;color:#48504f;margin:0;">{t}</p></div>' for t in ["Charging status","Live session","Schedule","Home and public"])
O.append(F(fig("One EV domain in place of four","Case two &middot; what the team built",
   "For an EV driver the questions are constant: am I charged, can I leave, when will it be ready. The answers were scattered across the app.",
   f'<p class="lbl" style="color:#8a7d6e;font-size:10px;margin-bottom:12px;">Before &middot; four places, one job</p>{bl}'
   f'<div style="display:flex;justify-content:center;padding:14px 0;"><div style="width:1px;height:26px;background:#3f7d7a;"></div></div>'
   f'<p class="lbl" style="color:{TEAL};font-size:10px;margin-bottom:12px;">After &middot; one place, at the point of use</p>'
   f'<div style="border:1.5px solid {TEAL};border-radius:8px;background:#f2f7f6;padding:14px;">'
   f'<p style="font-size:13px;font-weight:600;color:#1e1a16;margin:0 0 10px;">EV domain</p>'
   f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;">{after_ev}</div>'
   f'<p style="font-size:11.5px;line-height:1.5;color:{TEAL};margin:12px 0 0;">Real-time status, mirroring what is happening at the car.</p></div>',
   colour=TEAL,foot=f'<p style="font-size:13px;line-height:1.6;color:{TEAL};margin:16px 0 0;padding-top:14px;border-top:1px solid #e8e2da;">My call was that EV had to be solved as one experience rather than patched feature by feature.</p>'),pt=36))

O.append(F(fig("Four rounds, against the same task set","Case two &middot; what the team built",
   "System Usability Scale, measured round by round on a fixed set of EV tasks.",
   '<svg viewBox="0 0 300 190" width="100%" height="190" style="display:block;" aria-label="SUS scores rising across rounds">'
   '<rect x="228" y="0" width="72" height="190" fill="#efe9e1"></rect>'
   '<line x1="0" y1="1" x2="300" y2="1" stroke="#e8e2da"></line><line x1="0" y1="95" x2="300" y2="95" stroke="#e8e2da"></line>'
   '<line x1="0" y1="189" x2="300" y2="189" stroke="#d8cec0"></line>'
   '<line x1="0" y1="25" x2="300" y2="25" stroke="#b07a3c" stroke-width="1.5" stroke-dasharray="5 5"></line>'
   '<line x1="0" y1="139" x2="300" y2="139" stroke="#b5a08a" stroke-dasharray="3 5"></line>'
   '<polyline points="40,108 116,70 192,63" fill="none" stroke="#3f7d7a" stroke-width="2.5"></polyline>'
   '<circle cx="40" cy="108" r="5" fill="#3f7d7a"></circle><circle cx="116" cy="70" r="5" fill="#3f7d7a"></circle><circle cx="192" cy="63" r="5" fill="#3f7d7a"></circle>'
   '<text x="40" y="98" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#1e1a16">73</text>'
   '<text x="116" y="60" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#1e1a16">79</text>'
   '<text x="192" y="53" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" font-weight="600" fill="#1e1a16">80</text>'
   '<text x="297" y="20" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#b07a3c">TARGET 86</text>'
   '<text x="297" y="134" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#b5a08a">GLOBAL AVERAGE 68</text></svg>'
   '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:7px;">'
   '<p class="lbl" style="font-size:9.5px;color:#8a7d6e;text-align:center;">R1</p><p class="lbl" style="font-size:9.5px;color:#8a7d6e;text-align:center;">R2</p>'
   '<p class="lbl" style="font-size:9.5px;color:#8a7d6e;text-align:center;">R3</p><p class="lbl" style="font-size:9.5px;color:#b5a08a;text-align:center;">R4</p></div>',
   colour=TEAL,foot='<p style="font-size:12.5px;line-height:1.6;color:#8a7d6e;margin:16px 0 0;padding-top:14px;border-top:1px solid #e8e2da;">Three reported SUS scores. The fourth round was run to task-completion target. Mine: funding four rounds against a delivery schedule, and holding the ship gate.</p>'),pt=28))

O.append(block("And the rest of it",TEAL,"ring",P(C2["hard2"])+
   f'<div style="margin-top:22px;padding-top:16px;border-top:1px solid #e8e2da;display:flex;gap:11px;align-items:flex-start;">'
   f'{dot(TEAL,"ring",10)}<p style="font-size:14.5px;line-height:1.7;color:{TEAL};margin:-4px 0 0;">{C2["credit"]}</p></div>'))

beats=[("2024","Design dominates the complaints","The deprecated US app lands in Europe at 1.9 stars. Navigation customers cannot learn, information displays they cannot read, no dark mode, driving analytics nobody understands.",DA),
       ("Spring 2025","The language shifts","&ldquo;Intuitive&rdquo;, &ldquo;simple and effective&rdquo;, &ldquo;very well thought out&rdquo; start appearing in customer feedback where the complaints used to be.",DA),
       ("June 2025","Design credited by name","An internal customer-experience report attributes reduced complaint volume directly to intuitive design. The first time on record that design was the cause rather than the problem.",DA),
       ("August 2025","Out of the top five","Displaced by backend and connectivity issues outside design&rsquo;s ownership. The 4.6 star rating stabilises.",DT)]
bt=[]
for i,(d,h,t,c) in enumerate(beats):
    bt.append(f'<div style="display:grid;grid-template-columns:18px 1fr;gap:14px;align-items:start;padding-bottom:26px;">'
              f'<div style="display:flex;flex-direction:column;align-items:center;gap:5px;padding-top:4px;">'
              f'<div style="width:9px;height:9px;border-radius:50%;{"background:"+c if i<3 else "border:2px solid "+c+";box-sizing:border-box"};"></div>'
              f'{"<div style=\"width:1px;flex-grow:1;min-height:74px;background:#332c25;\"></div>" if i<3 else ""}</div>'
              f'<div><p class="lbl" style="color:{c};font-size:10px;margin-bottom:8px;">{d}</p>'
              f'<p style="font-size:16px;font-weight:600;color:#f0ebe3;margin:0 0 8px;line-height:1.35;">{h}</p>'
              f'<p style="font-size:13px;line-height:1.65;color:#9a9086;margin:0;">{t}</p></div></div>')
O.append(B(f'<p class="lbl" style="color:{DA};font-size:10.5px;margin-bottom:8px;">Case two &middot; the outcome</p>'
   '<p class="disp" style="font-size:30px;color:#f0ebe3;margin:0 0 12px;">Thirteen months from complaint driver to differentiator</p>'
   '<p style="font-size:14px;line-height:1.7;color:#9a9086;margin:0 0 30px;">Design dominated the complaint list when the repurposed app landed. Then it left the list altogether.</p>'
   +"".join(bt),pt=48,pb=32))

O.append(F(fig("What customers actually left behind","Case two &middot; the public proof",
   "The rating is the headline. The composition underneath it is the story.",
   '<div style="display:flex;align-items:flex-end;gap:14px;margin-bottom:26px;">'
   '<div><p class="lbl" style="color:#b5a08a;font-size:10px;margin-bottom:2px;">At launch</p><p class="disp num" style="font-size:40px;color:#8a7d6e;">1.9&#9733;</p></div>'
   '<p class="disp" style="font-size:24px;color:#c9bfb2;padding-bottom:6px;">&rarr;</p>'
   '<div><p class="lbl" style="color:#b07a3c;font-size:10px;margin-bottom:2px;">August 2025</p><p class="disp num" style="font-size:40px;color:#1e1a16;">4.6&#9733;</p></div></div>'
   '<p class="lbl" style="color:#8a7d6e;font-size:10px;padding-bottom:9px;border-bottom:1px solid #d8cec0;margin-bottom:16px;">Share of reviews, by star rating</p>'
   '<p style="font-size:12.5px;font-weight:600;color:#8a7d6e;margin:0 0 6px;">Before</p>'
   '<div style="display:flex;height:38px;border-radius:3px;overflow:hidden;margin-bottom:16px;">'
   '<div style="width:67%;background:#f2ebe0;border:1px solid #ddd3c5;box-sizing:border-box;display:flex;align-items:center;padding-left:8px;"><p class="num" style="font-size:12px;color:#8a7d6e;margin:0;">1&#9733; 67%</p></div>'
   '<div style="width:19%;background:#dcc39c;"></div><div style="width:14%;background:#8f5f28;"></div></div>'
   '<p style="font-size:12.5px;font-weight:600;color:#1e1a16;margin:0 0 6px;">After</p>'
   '<div style="display:flex;height:38px;border-radius:3px;overflow:hidden;">'
   '<div style="width:4%;background:#f2ebe0;border:1px solid #ddd3c5;box-sizing:border-box;"></div>'
   '<div style="width:16%;background:#dcc39c;"></div>'
   '<div style="width:80%;background:#8f5f28;display:flex;align-items:center;padding-left:10px;"><p class="num" style="font-size:12px;color:#f5efe6;margin:0;">5&#9733; 80%</p></div></div>'
   '<p class="num" style="font-size:12.5px;color:#1e1a16;margin:14px 0 0;">One star: 2 in 3 &rarr; 1 in 25</p>',
   foot='<p class="cap" style="font-size:12px;margin-top:14px;">Public App Store and Play Store data. Lexus Link+; MyToyota shows the same pattern.</p>'),pt=40))

O.append(block("What changed",AMBER,"fill",P(C2["impact"])+
   f'<p class="disp" style="font-size:24px;margin:24px 0 0;padding-left:18px;border-left:3px solid {AMBER};">{C2["impact2"]}</p>'))
O.append('<div style="height:56px;"></div>')

# ---- CASE THREE ----
O.append(openband(C3,"#f0ebe3","fill"))
O.append(block("The challenge",INK,"fill",P(C3["challenge"])))
O.append(block("My role",INK,"fill",P(C3["myrole"]),pt=34))
O.append(F(fig("Nothing was broken. The prompt had grown six times.","Case three &middot; the failure that taught me the most",
   "Quality started degrading around the fourth session per user. Context had simply accumulated until the model was drowning in its own history.",
   '<svg viewBox="0 0 300 200" width="100%" height="200" style="display:block;" aria-label="System prompt characters growing session one to four">'
   '<line x1="0" y1="1" x2="300" y2="1" stroke="#e8e2da"></line><line x1="0" y1="100" x2="300" y2="100" stroke="#e8e2da"></line>'
   '<line x1="0" y1="199" x2="300" y2="199" stroke="#d8cec0"></line>'
   '<polygon points="70,168 230,20 230,199 70,199" fill="#efe9e1"></polygon>'
   '<rect x="24" y="168" width="46" height="31" fill="#c9bfb2"></rect><rect x="230" y="12" width="46" height="187" fill="#1e1a16"></rect>'
   '<line x1="0" y1="154" x2="300" y2="154" stroke="#b07a3c" stroke-width="2" stroke-dasharray="6 5"></line>'
   '<text x="297" y="149" text-anchor="end" font-family="Inter,sans-serif" font-size="9.5" font-weight="600" fill="#b07a3c">BOUNDED PROMPT: HARD BUDGET</text>'
   '<text x="47" y="160" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#1e1a16">5,600</text>'
   '<text x="253" y="6" text-anchor="middle" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#1e1a16">34,000+</text></svg>'
   '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:7px;">'
   '<p class="lbl" style="font-size:9.5px;color:#8a7d6e;text-align:center;">S1</p><p class="lbl" style="font-size:9.5px;color:#b5a08a;text-align:center;">2</p>'
   '<p class="lbl" style="font-size:9.5px;color:#b5a08a;text-align:center;">3</p><p class="lbl" style="font-size:9.5px;color:#8a7d6e;text-align:center;">S4</p></div>',
   foot='<p style="font-size:13px;line-height:1.6;color:#1e1a16;margin:16px 0 0;padding-top:14px;border-top:1px solid #e8e2da;">The fix was architectural, not cosmetic: hard character budgets, enforced regardless of how many sessions a user has had.</p>'),pt=40))
O.append(block("What I learned building it",INK,"fill",deflist(C3["approach"])))
O.append(block("Where it stands",INK,"fill",P(C3["impact"],size=17,colour="#1e1a16")))
O.append('<div style="height:64px;"></div>')

O.append(B(f'<p class="lbl" style="color:{DA};font-size:10.5px;margin-bottom:16px;">The pattern</p>'
   f'<p style="font-size:17px;line-height:1.75;color:#c8c0b5;margin:0 0 30px;">{CLOSING[0]}</p>'
   f'<p style="font-size:15px;line-height:1.75;color:#9a9086;margin:0 0 20px;">{CLOSING_LEAD}</p>'
   f'<p class="disp" style="font-size:42px;color:#f0ebe3;margin:0;">{CLOSING_BIG}</p>',pt=56,pb=56))

O.append(F('<p class="lbl" style="margin-bottom:14px;">Contact</p>'
   f'<p style="font-size:18px;line-height:1.7;color:#1e1a16;font-weight:500;margin:0 0 16px;">{CONTACT[0]}</p>'
   f'<p style="font-size:16px;line-height:1.8;color:#5c5347;margin:0;">{CONTACT[1]}</p>',pt=56,pb=48))
O.append(f'<div style="padding:20px {PAD}px 40px;border-top:1px solid #e8e2da;display:flex;justify-content:space-between;">'
   '<p style="font-size:12.5px;color:#b5a08a;margin:0;">&copy; 2026 Gideon Bullock</p>'
   '<p style="font-size:12.5px;color:#b5a08a;margin:0;">gideonb.me</p></div>')
O.append('</div>')
open("b_mobile.part","w").write("\n".join(O))
print("built")
