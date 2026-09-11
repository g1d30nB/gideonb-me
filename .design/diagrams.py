# Diagram emitters for the /work page. Warm paper, one grotesque, no side stripes, no card grids.
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"
AD="var(--amber-d)"; TD="var(--teal-d)"

def dot(colour, kind="fill", s=11):
    if kind=="ring":
        return f'<span style="display:inline-block;width:{s}px;height:{s}px;border-radius:50%;border:2px solid {colour};box-sizing:border-box;flex-shrink:0;"></span>'
    return f'<span style="display:inline-block;width:{s}px;height:{s}px;border-radius:50%;background:{colour};flex-shrink:0;"></span>'

def kicker(text, colour, kind="fill", right=""):
    r = f'<p class="lbl" style="color:var(--faint);text-align:right;">{right}</p>' if right else "<span></span>"
    return (f'<div style="display:flex;align-items:center;justify-content:space-between;gap:32px;margin-bottom:var(--s4);">'
            f'<div style="display:flex;align-items:center;gap:10px;">{dot(colour,kind,10)}'
            f'<p class="lbl" style="color:{colour};">{text}</p></div>{r}</div>')

def takeaway(statement, note="", colour=INK):
    n = f'<p class="t3" style="max-width:300px;text-align:right;">{note}</p>' if note else ""
    return (f'<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:var(--s7);'
            f'margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid var(--rule);">'
            f'<p style="font-size:16.5px;line-height:1.6;font-weight:500;color:{colour};max-width:660px;margin:0;">{statement}</p>{n}</div>')

def figure(accent, kick, kind, title, sub, body, tk, right="", ground=None, pad=None):
    bg = f'background:{ground};' if ground else ""
    p  = pad or ("var(--s7) var(--s7)" if ground else "0")
    return (f'<div style="{bg}padding:{p};box-sizing:border-box;border-top:2px solid {accent};padding-top:var(--s5);">'
            f'{kicker(kick,accent,kind,right)}'
            f'<p class="d3" style="margin-bottom:var(--s3);">{title}</p>'
            f'<p class="t2" style="color:var(--muted);max-width:780px;margin-bottom:var(--s7);">{sub}</p>'
            f'{body}{tk}</div>')

# ---------------------------------------------------------------- capability arc
ARC_STEPS=[
 ("First","UX research","Nothing could be argued without evidence, so this came first.",
  "the right to frame the problem.",0,"var(--rule-2)",2),
 ("Second","UX and interface design","The screens the business already knew it wanted.",
  "credibility on delivery, and a place beside engineering.",56,"var(--rule-2)",2),
 ("Third","Product design","The team moved closer to the core business.",
  "a close enough view of the business to see what it could not see.",118,"var(--rule-2)",2),
 ("Fourth &middot; nobody asked","Service design","Did not exist anywhere in Toyota. I made the case for it and hired into it.",
  "the joins between business units that nobody owned.",196,A,3),
]

def arc(width=1120):
    cards=[]
    for i,(k,n,why,earn,mb,rule,rw) in enumerate(ARC_STEPS):
        last = i==3
        cards.append(
          f'<div style="margin-bottom:{mb}px;border-top:{rw}px solid {rule};padding-top:var(--s4);">'
          f'<p class="lbl" style="color:{A if last else "var(--faint)"};margin-bottom:var(--s3);">{k}</p>'
          f'<p class="d4" style="margin-bottom:var(--s3);">{n}</p>'
          f'<p style="font-size:14px;line-height:1.6;color:var(--body);margin:0 0 var(--s4);">{why}</p>'
          f'<p style="font-size:12.5px;line-height:1.55;color:var(--muted);margin:0;padding-top:var(--s3);border-top:1px solid var(--rule);">'
          f'<span style="color:{A};font-weight:600;">Earned &rarr;</span> {earn}</p></div>')
        if i==2:
            cards.append(
              '<div style="height:340px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:var(--s3);">'
              '<p style="writing-mode:vertical-rl;transform:rotate(180deg);font-size:11px;letter-spacing:0.13em;'
              'text-transform:uppercase;font-weight:600;color:var(--amber);margin:0;white-space:nowrap;">The question changed</p>'
              '<div style="width:1px;flex-grow:1;background:repeating-linear-gradient(to bottom,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div></div>')
    grid=(f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr 44px 1fr;gap:var(--s5);align-items:end;margin-bottom:var(--s7);">'
          f'{"".join(cards)}</div>')
    wedge=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:var(--s5);margin-bottom:10px;">'
           f'<p class="lbl" style="color:var(--muted);">Scope: one screen</p>'
           f'<p class="lbl" style="color:var(--ink);">Scope: the business behind it</p></div>'
           f'<svg viewBox="0 0 {width} 96" width="100%" height="96" preserveAspectRatio="none" style="display:block;" '
           f'aria-label="Scope widening from one screen to the whole business">'
           f'<polygon points="0,44 {width},4 {width},92 0,60" fill="#f0e3d0"></polygon>'
           f'<line x1="0" y1="44" x2="{width}" y2="4" stroke="#a97739" stroke-width="1.5"></line></svg>')
    return figure(A,"Case one &middot; the spine","fill","How the capability grew",
      "Four capabilities, in the order they were established. Each one earned the next. Only the last one was never asked for.",
      grid+wedge,
      takeaway("Each brief was wider than the last because the last one had worked. The widest one was the one nobody had asked for.",
               "Left to right is seven years. The band beneath is how much of the customer&rsquo;s experience design was allowed to own."),
      right="2018 &nbsp;&rarr;&nbsp; 2026")

# ---------------------------------------------------------------- service gap (dark)
SLICES=[("Choosing","Another business unit",0),("Buying","Another business unit",0),
        ("Connected services","Ours. The only slice we could see.",1),
        ("Living with it","Another business unit",0),("The next car","Another business unit",0)]

def gap():
    cols="1fr 26px 1fr 26px 1fr 26px 1fr 26px 1fr"
    cells=[]
    for i,(n,o,mine) in enumerate(SLICES):
        if i>0:
            cells.append('<div style="display:flex;align-items:center;justify-content:center;">'
                         '<span style="width:11px;height:11px;border:1.5px dashed oklch(0.50 0.035 70);border-radius:50%;"></span></div>')
        cells.append(
          f'<div style="border:{"1.5px solid "+AD if mine else "1px solid var(--night-rule)"};'
          f'background:{"var(--night-2)" if mine else "transparent"};border-radius:3px;padding:var(--s4) 14px;min-height:98px;">'
          f'<p style="font-size:14px;font-weight:600;color:{"var(--night-ink)" if mine else "var(--night-body)"};margin:0 0 var(--s2);">{n}</p>'
          f'<p style="font-size:11.5px;line-height:1.5;color:{AD if mine else "var(--night-muted)"};margin:0;">{o}</p></div>')
    before=f'<div style="display:grid;grid-template-columns:{cols};align-items:stretch;margin-bottom:14px;">{"".join(cells)}</div>'
    joinnote=('<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s7);">'
              '<span style="width:11px;height:11px;border:1.5px dashed oklch(0.50 0.035 70);border-radius:50%;flex-shrink:0;"></span>'
              '<p style="font-size:13px;color:var(--night-muted);margin:0;">Four joins. Nobody accountable for any of them, and the customer crossing all four.</p></div>')
    stems="".join('<div style="height:26px;border-left:1px solid oklch(0.42 0.030 190);margin-left:50%;"></div><div></div>' for _ in range(4))+\
          '<div style="height:26px;border-left:1px solid oklch(0.42 0.030 190);margin-left:50%;"></div>'
    afterrow="".join(
      f'<div style="border:1px solid oklch(0.33 0.020 190);border-radius:3px;padding:var(--s3) 14px;">'
      f'<p style="font-size:13px;color:var(--night-body);margin:0;">{n}</p></div>' + ("<div></div>" if i<4 else "")
      for i,(n,_,_) in enumerate(SLICES))
    after=(f'<div style="border:1.5px solid {TD};background:oklch(0.225 0.022 190);border-radius:3px;padding:15px 18px;'
           f'display:flex;align-items:center;justify-content:space-between;gap:var(--s4);">'
           f'<p style="font-size:14px;font-weight:600;color:var(--night-ink);margin:0;">One end-to-end journey</p>'
           f'<p style="font-size:12px;color:{TD};margin:0;">Blueprinted front stage and back, reusable as service patterns</p></div>'
           f'<div style="display:grid;grid-template-columns:{cols};">{stems}</div>'
           f'<div style="display:grid;grid-template-columns:{cols};margin-bottom:var(--s5);">{afterrow}</div>')
    credit=(f'<div style="border-top:1px solid var(--night-rule);padding-top:var(--s5);display:flex;gap:14px;align-items:flex-start;">'
            f'{dot(TD,"ring",10)}'
            f'<p style="font-size:14.5px;line-height:1.7;color:{TD};margin:-4px 0 0;max-width:840px;">'
            f'The blueprints, the reusable service patterns and the playbooks were built by the service designers who were hired to make them. '
            f'What I did was make the case for a capability nobody had asked for, and hire into it.</p></div>')
    return (f'<div style="border-top:2px solid {AD};padding-top:var(--s5);">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:32px;margin-bottom:var(--s4);">'
            f'<div style="display:flex;align-items:center;gap:10px;">{dot(AD,"fill",10)}'
            f'<p class="lbl" style="color:{AD};">Case one &middot; what service design was for</p></div>'
            f'<p class="lbl" style="color:var(--night-muted);text-align:right;">No Toyota blueprint is shown. This is the shape of the problem.</p></div>'
            f'<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);max-width:1000px;">A disjointed experience is a faithful picture of a disjointed business</p>'
            f'<p style="font-size:15.5px;line-height:1.75;color:var(--night-muted);max-width:800px;margin:0 0 var(--s7);">'
            f'Once we were close enough to the Connected Technologies business to see how it operated, the gap was structural.</p>'
            f'<p class="lbl" style="color:var(--night-muted);margin-bottom:var(--s4);">Before &nbsp;&middot;&nbsp; one slice, behaving as though it owned all of them</p>'
            f'{before}{joinnote}'
            f'<p class="lbl" style="color:{TD};margin-bottom:var(--s4);">After &nbsp;&middot;&nbsp; one journey, owned together</p>'
            f'{after}'
            f'<p style="font-size:16.5px;line-height:1.7;color:var(--night-ink);max-width:840px;margin:0 0 var(--s6);font-weight:500;">'
            f'Business units that had never designed anything together started working on the same journey. They are still doing it, '
            f'which is the part I am most confident about, because it outlasted me.</p>{credit}</div>')

# ---------------------------------------------------------------- operating model
DISCIPLINES=[("Product design","Insight, journeys and the screens themselves",0),
 ("Design systems","Components, tokens and design governance",0),
 ("UX research","Formative and evaluative customer insight",0),
 ("Service design","Front stage experience and back stage operations",1),
 ("Content and creative","Words, tone of voice and art direction",0),
 ("Design leadership","Vision, planning and delivery",0)]
MODELS=[("Innovation sprints","Fast, exploratory, time-boxed",14,12,"left"),
 ("Team augmentation","Specialists into an existing team",41,42,"left"),
 ("Design studio","A dedicated team, scoped and delivered",70,20,"right"),
 ("Embedded partnership","Full design management and operations",86,82,"right")]

def opmodel():
    import components as C
    disc="".join(
      f'<div style="padding:11px 0;border-bottom:1px solid var(--rule);">'
      f'<p style="font-size:14.5px;font-weight:600;color:{A if m else "var(--ink)"};margin:0 0 2px;">{n}</p>'
      f'<p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{d}</p></div>' for n,d,m in DISCIPLINES)
    models="".join(
      f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);">'
      f'<div style="height:8px;background:oklch(0.93 0.030 68);width:{w}%;margin-bottom:8px;"></div>'
      f'<p style="font-size:14px;font-weight:600;color:var(--ink);margin:0 0 3px;">{n}</p>'
      f'<p style="font-size:12.5px;line-height:1.5;color:var(--muted);margin:0;">{d}</p></div>'
      for n,d,w in [("Innovation sprints","Fast, exploratory, time-boxed",28),("Team augmentation","Specialists into an existing team",52),
                    ("Design studio","A dedicated team, scoped and delivered",76),("Embedded partnership","Full design management and operations",100)])
    foot=("".join(
      f'<div><p class="lbl" style="color:var(--faint);margin-bottom:var(--s2);">{h}</p>'
      f'<p style="font-size:14px;line-height:1.6;color:{c};margin:0;{w}">{t}</p></div>'
      for h,t,c,w in [
        ("Positioning","A published service catalogue and sales collateral. Partner teams bought the depth they needed.","var(--body)",""),
        ("Commercial","A P&amp;L. Every designer I hired was paid for by work I had won.","var(--body)",""),
        ("Effect","Design&rsquo;s commercial contribution became visible to senior leadership for the first time.","var(--ink)","font-weight:500;")]))
    body=(f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:var(--s8);align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">One office, embedded pods, one community</p>{C.orgmodel()}</div>'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);">Six disciplines, one team</p>{disc}</div></div>'
          f'<p class="lbl" style="margin:var(--s7) 0 var(--s4);padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);">Four engagement models, shallow to deep</p>'
          f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s5);">{models}</div>'
          f'<div style="margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid var(--rule);'
          f'display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s6);">{foot}</div>')
    return figure(A,"Case one &middot; how it was run","fill","Run as an internal consultancy",
      "Six disciplines under one roof, four ways to buy them, and a management office at the centre of embedded teams. A service catalogue, explicit positioning, and a P&amp;L.",
      body, "", right="Toyota Experience Design")

# ---------------------------------------------------------------- EV domain
EV_BEFORE=["Home screen entry point, easy to miss","Battery status, tied to the default vehicle",
           "Home charging, stored somewhere else again","Charging schedule, split across three settings"]
EV_AFTER=["Charging status","Live session","Schedule","Home and public"]

def ev():
    bars=['<div style="height:7px;border-radius:4px;background:var(--rule);"></div>',
          '<div style="height:26px;border-radius:5px;background:oklch(0.93 0.030 68);border:1px solid oklch(0.86 0.045 70);"></div>']
    screens=[]
    for i,t in enumerate(EV_BEFORE):
        fills="".join(f'<div style="height:7px;border-radius:4px;background:oklch(0.93 0.006 82);width:{w}%;"></div>' for w in [80,62,74][:2+(i%2)])
        screens.append(
          f'<div style="border:1px solid var(--rule-2);border-radius:9px;background:oklch(0.985 0.004 85);'
          f'padding:var(--s3) 11px;height:170px;display:flex;flex-direction:column;gap:7px;">'
          f'{bars[0]}{bars[1]}{fills}'
          f'<p style="font-size:12px;line-height:1.45;color:var(--muted);margin:auto 0 0;">{t}</p></div>')
    zig=('<svg viewBox="0 0 600 70" width="100%" height="70" preserveAspectRatio="none" style="display:block;margin-bottom:-1px;" '
         'aria-label="A single task crossing four separate locations">'
         '<path d="M66,66 L66,10 L378,10 L378,66" fill="none" stroke="#b09a80" stroke-width="1.5"></path>'
         '<path d="M222,66 L222,32 L534,32 L534,66" fill="none" stroke="#b09a80" stroke-width="1.5" stroke-dasharray="4 4"></path>'
         '<circle cx="66" cy="66" r="3.5" fill="#8a7d6e"></circle><circle cx="222" cy="66" r="3.5" fill="#8a7d6e"></circle>'
         '<circle cx="378" cy="66" r="3.5" fill="#8a7d6e"></circle><circle cx="534" cy="66" r="3.5" fill="#8a7d6e"></circle></svg>')
    after="".join(f'<div style="border:1px solid oklch(0.86 0.022 195);border-radius:5px;background:oklch(0.995 0.002 195);'
                  f'padding:var(--s2) 9px;"><p style="font-size:12px;color:oklch(0.42 0.020 195);margin:0;">{t}</p></div>' for t in EV_AFTER)
    body=(f'<div style="display:grid;grid-template-columns:600px 1fr;gap:56px;align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:20px;">Before &nbsp;&middot;&nbsp; four places, one job</p>'
          f'{zig}<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s5);">{"".join(screens)}</div>'
          f'<p class="t3" style="margin-top:18px;">Grown feature by feature and vehicle generation by vehicle generation. Public and home charging history lived in different places. Charger-only customers saw no range at all.</p></div>'
          f'<div><p class="lbl" style="color:{T};padding-bottom:var(--s3);border-bottom:1px solid oklch(0.84 0.025 195);margin-bottom:20px;">After &nbsp;&middot;&nbsp; one place, at the point of use</p>'
          f'<svg viewBox="0 0 460 70" width="100%" height="70" preserveAspectRatio="none" style="display:block;margin-bottom:-1px;" aria-label="One short path into a single domain">'
          f'<path d="M230,10 L230,66" fill="none" stroke="#3f7d7a" stroke-width="1.5"></path>'
          f'<circle cx="230" cy="66" r="4.5" fill="#3f7d7a"></circle></svg>'
          f'<div style="border:1.5px solid {T};border-radius:9px;background:oklch(0.975 0.010 195);padding:var(--s4) var(--s4) 14px;height:170px;box-sizing:border-box;display:flex;flex-direction:column;gap:9px;">'
          f'<p style="font-size:13px;font-weight:600;color:var(--ink);margin:0 0 2px;">EV domain</p>'
          f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;">{after}</div>'
          f'<p style="font-size:12px;line-height:1.45;color:{T};margin:auto 0 0;">Real-time status, mirroring what is happening at the car.</p></div>'
          f'<p class="t3" style="margin-top:18px;">The complexity of vehicle generations, home charger integrations and software constraints did not go away. The team moved it behind the experience rather than into the customer&rsquo;s hands.</p></div></div>')
    return figure(T,"Case two &middot; what the team built","ring","One EV domain in place of four",
      "For an EV driver the questions are constant. Am I charged, can I leave, when will it be ready. The answers were scattered across the app.",
      body,
      takeaway("My call was that EV had to be solved as one experience rather than patched feature by feature, and that it did not ship until task performance hit target.",
               "Everything drawn here is the team&rsquo;s work.", colour=INK),
      right="The team&rsquo;s work")

# ---------------------------------------------------------------- SUS rounds
def sus(w=560):
    svg=(f'<svg viewBox="0 0 540 250" width="100%" height="250" preserveAspectRatio="none" style="display:block;" aria-label="SUS scores rising across rounds">'
     '<rect x="420" y="0" width="120" height="250" fill="#efe9e1"></rect>'
     '<line x1="0" y1="0" x2="540" y2="0" stroke="#e8e2da"></line><line x1="0" y1="125" x2="540" y2="125" stroke="#e8e2da"></line>'
     '<line x1="0" y1="249" x2="540" y2="249" stroke="#d5cabb"></line>'
     '<line x1="0" y1="33" x2="540" y2="33" stroke="#a97739" stroke-width="1.5" stroke-dasharray="5 5"></line>'
     '<line x1="0" y1="183" x2="540" y2="183" stroke="#b09a80" stroke-dasharray="3 5"></line>'
     '<polyline points="70,142 210,92 350,83" fill="none" stroke="#3f7d7a" stroke-width="2.5"></polyline>'
     '<circle cx="70" cy="142" r="6" fill="#3f7d7a"></circle><circle cx="210" cy="92" r="6" fill="#3f7d7a"></circle><circle cx="350" cy="83" r="6" fill="#3f7d7a"></circle>'
     '<line x1="480" y1="70" x2="480" y2="249" stroke="#c5b9a8" stroke-dasharray="3 4"></line>'
     '<text x="70" y="128" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">73</text>'
     '<text x="210" y="78" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">79</text>'
     '<text x="350" y="69" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">80</text>'
     '<text x="536" y="27" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" fill="#a97739">TARGET 86</text>'
     '<text x="536" y="177" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" fill="#9c8a72">GLOBAL AVERAGE 68</text></svg>')
    axis=('<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">'
          + "".join(f'<p class="lbl" style="color:{c};text-align:center;">Round {i}</p>' for i,c in
                    [(1,"var(--muted)"),(2,"var(--muted)"),(3,"var(--muted)"),(4,"var(--faint)")]) + '</div>')
    ys=('<div style="width:34px;display:flex;flex-direction:column;justify-content:space-between;height:250px;padding-bottom:2px;">'
        + "".join(f'<p class="lbl" style="color:var(--faint);letter-spacing:0;">{v}</p>' for v in [90,75,60]) + '</div>')
    body=f'<div style="display:flex;gap:var(--s3);"><div style="flex-grow:1;">{svg}{axis}</div>{ys}</div>'
    return figure(T,"Case two &middot; what the team built","ring","Four rounds, against the same task set",
      "System Usability Scale, measured round by round on a fixed set of EV tasks.",
      body,
      takeaway("My part was funding four rounds against a delivery schedule and holding the ship gate until performance hit target.",
               "Three reported SUS scores. The fourth round was run to task-completion target."))

# ---------------------------------------------------------------- rating turnaround
def rating():
    def bar(label, one, mid, five, strong):
        onelab=f'<p style="font-size:13px;color:var(--muted);margin:0;">1&#9733; &nbsp;{one}%</p>' if one>20 else ""
        fivelab=f'<p style="font-size:13px;color:oklch(0.96 0.010 80);margin:0;">5&#9733; &nbsp;{five}%</p>' if five>40 else ""
        midlab=f'<p style="font-size:13px;color:oklch(0.38 0.030 72);margin:0;">{mid}%</p>'
        return (f'<div style="margin-bottom:var(--s5);">'
                f'<p style="font-size:13px;font-weight:600;color:{"var(--ink)" if strong else "var(--muted)"};margin:0 0 7px;">{label}</p>'
                f'<div style="display:flex;height:46px;border-radius:3px;overflow:hidden;">'
                f'<div style="width:{one}%;background:oklch(0.955 0.011 80);border:1px solid oklch(0.875 0.014 80);box-sizing:border-box;display:flex;align-items:center;padding-left:10px;">{onelab}</div>'
                f'<div style="width:{mid}%;background:oklch(0.835 0.055 72);display:flex;align-items:center;padding-left:10px;">{midlab}</div>'
                f'<div style="width:{five}%;background:oklch(0.475 0.085 62);display:flex;align-items:center;padding-left:12px;">{fivelab}</div></div></div>')
    head=(f'<div style="display:flex;align-items:flex-end;gap:var(--s5);margin-bottom:var(--s7);">'
          f'<div><p class="lbl" style="color:var(--faint);margin-bottom:var(--s1);">At launch</p>'
          f'<p class="stat" style="color:var(--muted);font-size:54px;">1.9&#9733;</p></div>'
          f'<p style="font-size:32px;color:var(--rule-2);padding-bottom:8px;margin:0;">&rarr;</p>'
          f'<div><p class="lbl" style="color:{A};margin-bottom:var(--s1);">August 2025</p>'
          f'<p class="stat" style="font-size:54px;">4.6&#9733;</p></div>'
          f'<p class="t3" style="margin:0 0 10px auto;max-width:190px;text-align:right;">Rating more than doubled over thirteen months.</p></div>')
    key="".join(f'<div style="display:flex;align-items:center;gap:7px;"><span style="width:11px;height:11px;background:{c};'
                f'{b}display:inline-block;"></span><p class="t3" style="font-size:12px;">{n}</p></div>'
                for n,c,b in [("One star","oklch(0.955 0.011 80)","border:1px solid oklch(0.875 0.014 80);"),
                              ("Two to four","oklch(0.835 0.055 72)",""),("Five stars","oklch(0.475 0.085 62)","")])
    body=(head+'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:20px;">Share of reviews, by star rating</p>'
          +bar("Before",67,19,14,False)+bar("After",4,16,80,True)
          +f'<div style="display:flex;gap:20px;align-items:center;padding-top:var(--s4);border-top:1px solid var(--rule);">{key}'
          f'<p style="font-size:13px;font-weight:600;color:var(--ink);margin:0 0 0 auto;">One star: 2 in 3 &rarr; 1 in 25</p></div>')
    return figure(A,"Case two &middot; the public proof","fill","The public rating data",
      "The rating, and the share of reviews behind it.", body,
      takeaway("Five-star reviews grew nearly six-fold, and one-star reviews fell from two thirds of all reviews to four per cent.",
               "Public App Store and Play Store data. Lexus Link+; MyToyota shows the same pattern."))

# ---------------------------------------------------------------- context growth
def ctx():
    svg=('<svg viewBox="0 0 520 270" width="100%" height="270" preserveAspectRatio="none" style="display:block;" aria-label="System prompt characters growing from session one to session four">'
     '<line x1="0" y1="1" x2="520" y2="1" stroke="#e8e2da"></line><line x1="0" y1="135" x2="520" y2="135" stroke="#e8e2da"></line>'
     '<line x1="0" y1="269" x2="520" y2="269" stroke="#d5cabb"></line>'
     '<polygon points="120,228 400,24 400,269 120,269" fill="#efe9e1"></polygon>'
     '<rect x="40" y="228" width="80" height="41" fill="#c5b9a8"></rect><rect x="400" y="14" width="80" height="255" fill="#1e1a16"></rect>'
     '<line x1="0" y1="209" x2="520" y2="209" stroke="#a97739" stroke-width="2" stroke-dasharray="6 5"></line>'
     '<text x="516" y="203" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" fill="#a97739">BOUNDED PROMPT: HARD BUDGET</text>'
     '<text x="80" y="218" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">5,600</text>'
     '<text x="440" y="6" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">34,000+</text>'
     '<text x="260" y="130" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="12.5" fill="#8a7d6e">accumulated, session on session</text></svg>')
    axis=('<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">'
          '<p class="lbl" style="color:var(--muted);text-align:center;">Session 1</p>'
          '<p class="lbl" style="color:var(--faint);text-align:center;">2</p>'
          '<p class="lbl" style="color:var(--faint);text-align:center;">3</p>'
          '<p class="lbl" style="color:var(--muted);text-align:center;">Session 4</p></div>')
    ys=('<div style="width:44px;display:flex;flex-direction:column;justify-content:space-between;height:270px;padding-bottom:2px;">'
        + "".join(f'<p class="lbl" style="color:var(--faint);letter-spacing:0;">{v}</p>' for v in ["36k","18k","0"]) + '</div>')
    body=f'<div style="display:flex;gap:var(--s3);"><div style="flex-grow:1;">{svg}{axis}</div>{ys}</div>'
    return figure(A,"Case three &middot; the failure that taught me the most","fill","Nothing was broken. The prompt had grown six times.",
      "Quality started degrading around the fourth session per user. Context had simply accumulated until the model was drowning in its own history.",
      body,
      takeaway("The fix was architectural. A bounded prompt with hard character budgets, enforced however many sessions a user has had.",
               "Sessions two and three are shown as accumulation rather than measured points. The two figures are the ones I recorded."))

# ---------------------------------------------------------------- complaint timeline (dark)
BEATS=[("2024","Design dominates the complaints","The deprecated US app lands in Europe at 1.9 stars. Navigation customers cannot learn, information displays they cannot read, no dark mode, driving analytics nobody understands.",False),
 ("Spring 2025","The language shifts","&ldquo;Intuitive&rdquo;, &ldquo;simple and effective&rdquo;, &ldquo;very well thought out&rdquo; start appearing in customer feedback where the complaints used to be.",False),
 ("June 2025","Design credited by name","An internal customer-experience report attributes reduced complaint volume directly to intuitive design. The first time on record that design was the cause rather than the problem.",False),
 ("August 2025","Out of the top five","Displaced by backend and connectivity issues outside design&rsquo;s ownership. The 4.6 star rating stabilises.",True)]

def timeline():
    track=('<svg viewBox="0 0 1120 96" width="100%" height="96" preserveAspectRatio="none" style="display:block;margin-bottom:6px;" '
     'aria-label="Design inside then outside the top five complaint categories">'
     '<polygon points="0,18 700,18 880,64 880,78 700,50 0,50" fill="#3a2c1a"></polygon>'
     '<line x1="0" y1="18" x2="700" y2="18" stroke="#d9a55f" stroke-width="1.5"></line>'
     '<line x1="700" y1="18" x2="880" y2="64" stroke="#d9a55f" stroke-width="1.5"></line>'
     '<line x1="880" y1="64" x2="1120" y2="88" stroke="#d9a55f" stroke-width="1.5" stroke-dasharray="5 5"></line>'
     '<line x1="0" y1="86" x2="1120" y2="86" stroke="#332c25"></line>'
     '<circle cx="60" cy="18" r="5" fill="#d9a55f"></circle><circle cx="380" cy="18" r="5" fill="#d9a55f"></circle>'
     '<circle cx="700" cy="18" r="5" fill="#d9a55f"></circle>'
     '<circle cx="1050" cy="86" r="5.5" fill="none" stroke="#6fb0ab" stroke-width="2"></circle>'
     '<text x="10" y="40" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#96835f">INSIDE THE TOP FIVE COMPLAINT CATEGORIES</text>'
     '<text x="1110" y="78" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#6fb0ab">OUT ENTIRELY</text></svg>')
    cols="".join(
      f'<div style="border-top:1px solid {TD if last else "var(--night-rule)"};padding-top:18px;">'
      f'<p class="lbl" style="color:{TD if last else AD};margin-bottom:10px;">{d}</p>'
      f'<p style="font-size:17.5px;font-weight:600;color:var(--night-ink);margin:0 0 10px;line-height:1.35;letter-spacing:-0.012em;">{h}</p>'
      f'<p style="font-size:13px;line-height:1.7;color:var(--night-muted);margin:0;">{t}</p></div>' for d,h,t,last in BEATS)
    return (f'<div style="border-top:2px solid {AD};padding-top:var(--s5);">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:32px;margin-bottom:var(--s4);">'
            f'<div style="display:flex;align-items:center;gap:10px;">{dot(AD,"fill",10)}'
            f'<p class="lbl" style="color:{AD};">Case two &middot; the outcome</p></div>'
            f'<p class="lbl" style="color:var(--night-muted);text-align:right;">Internal customer-experience reporting, Jul 2024 to Aug 2025</p></div>'
            f'<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);">Thirteen months from complaint driver to differentiator</p>'
            f'<p style="font-size:15.5px;line-height:1.75;color:var(--night-muted);max-width:820px;margin:0 0 var(--s7);">'
            f'Design dominated the complaint list when the repurposed app landed. Then it left the list altogether.</p>'
            f'{track}<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:34px;padding-top:22px;">{cols}</div></div>')
