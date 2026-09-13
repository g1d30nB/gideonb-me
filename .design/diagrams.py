# Diagram emitters for the /work page. Warm paper, one grotesque, no side stripes, no card grids.
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"
AD="var(--amber-d)"; TD="var(--teal-d)"

def dot(colour, kind="fill", s=11):
    if kind=="ring":
        return f'<span style="display:inline-block;width:{s}px;height:{s}px;border-radius:50%;border:2px solid {colour};box-sizing:border-box;flex-shrink:0;"></span>'
    return f'<span style="display:inline-block;width:{s}px;height:{s}px;border-radius:50%;background:{colour};flex-shrink:0;"></span>'

def kicker(text, colour, kind="fill", right=""):
    r = f'<p class="lbl" style="color:var(--amber);text-align:right;">{right}</p>' if right else "<span></span>"
    return (f'<div style="display:flex;align-items:center;justify-content:space-between;gap:32px;margin-bottom:var(--s4);">'
            f'<div style="display:flex;align-items:center;gap:10px;">{dot(colour,kind,10)}'
            f'<p class="lbl" style="color:{colour};">{text}</p></div>{r}</div>')

def takeaway(statement, note="", colour=INK):
    n = f'<p class="t3" style="max-width:300px;text-align:right;">{note}</p>' if note else ""
    return (f'<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:var(--s7);'
            f'margin-top:var(--s5);">'
            f'<p style="font-size:16.5px;line-height:1.6;font-weight:500;color:{colour};max-width:660px;margin:0;">{statement}</p>{n}</div>')

def figure(accent, kick, kind, title, sub, body, tk, right="", ground=None, pad=None, rule=True):
    bg = f'background:{ground};' if ground else ""
    p  = pad or ("var(--s7) var(--s7)" if ground else "0")
    top = f'border-top:2px solid {accent};padding-top:var(--s5);' if rule else ''
    return (f'<div style="{bg}padding:{p};box-sizing:border-box;{top}">'
            f'{kicker(kick,accent,kind,right) if kick else ""}'
            f'<p class="d3" style="margin-bottom:var(--s3);">{title}</p>'
            f'<p class="t2" style="color:var(--muted);max-width:780px;margin-bottom:var(--s7);">{sub}</p>'
            f'{body}{tk}</div>')

# ---------------------------------------------------------------- capability arc
ARC_STEPS=[
 ("First","UI design","Screens for flows that business analysts and product managers had already written, in support of Connected Technologies.",
  "a place inside the product teams.",0,"var(--rule-2)",2),
 ("Second","UX design","When the app passed into Connected Technologies&rsquo; ownership, the flows came with it.",
  "the flows themselves.",44,"var(--rule-2)",2),
 ("Third","UX research and analytics","The same people were wireframing without knowing what users did.",
  "evidence, and with it the right to frame the problem.",92,"var(--rule-2)",2),
 ("Fourth","Product design","The team moved closer to the core business.",
  "a close enough view of the business to see what it could not see.",144,"var(--rule-2)",2),
 ("Fifth","Service design","Connected Technologies owned the app in full and had to work with the rest of Toyota in Europe. Nothing like it existed anywhere in Toyota.",
  "the joins between business units that nobody owned.",216,A,3),
]

def arc(width=1120):
    cards=[]
    n=len(ARC_STEPS)
    for i,(k,n_,why,earn,mb,rule,rw) in enumerate(ARC_STEPS):
        last = i==n-1
        cards.append(
          f'<div class="arc-card{" arc-last" if last else ""}" style="--i:{i};position:relative;border-top:1px solid var(--rule);padding-top:var(--s4);display:grid;grid-template-rows:subgrid;grid-row:span 4;align-content:start;">'
          f'<span class="arc-rule" style="position:absolute;left:0;right:0;top:-1px;height:{3 if last else 2}px;background:{A if last else "var(--ink)"};transform-origin:left;"></span>'
          f'<p class="lbl" style="color:{A if last else "var(--faint)"};margin-bottom:var(--s3);">{k}</p>'
          f'<p class="d4" style="margin-bottom:var(--s3);">{n_}</p>'
          f'<p style="font-size:14px;line-height:1.6;color:var(--body);margin:0 0 var(--s4);">{why}</p>'
          f'<p class="arc-earned" style="font-size:12.5px;line-height:1.55;color:var(--muted);margin:0;padding-top:var(--s3);border-top:1px solid var(--rule);align-self:start;">'
          f'<span style="color:{A};font-weight:600;">Earned &rarr;</span> {earn}</p></div>')
        if i==n-2:
            cards.append(
              '<div class="arc-hinge" style="display:flex;flex-direction:column;align-items:center;gap:var(--s3);align-self:stretch;grid-row:span 4;">'
              '<p class="arc-hinge-label" style="writing-mode:vertical-rl;transform:rotate(180deg);font-size:11px;letter-spacing:0.13em;'
              'text-transform:uppercase;font-weight:600;color:var(--amber);margin:0;white-space:nowrap;">The question changed</p>'
              '<div class="arc-hinge-line" style="width:1px;flex-grow:1;background:repeating-linear-gradient(to bottom,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);transform-origin:top;"></div></div>')
    grid=(f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr 40px 1fr;grid-template-rows:auto auto auto auto;gap:0 var(--s4);align-items:start;margin-bottom:var(--s7);">'
          f'{"".join(cards)}</div>')
    wedge=(f'<div style="display:flex;align-items:baseline;justify-content:space-between;gap:var(--s5);margin-bottom:10px;">'
           f'<p class="lbl" style="color:var(--muted);">Scope: one screen</p>'
           f'<p class="lbl arc-scope-r" style="color:var(--ink);">Scope: the business behind it</p></div>'
           f'<svg class="arc-band" viewBox="0 0 {width} 96" width="100%" height="96" preserveAspectRatio="none" style="display:block;" '
           f'aria-label="Scope widening from one screen to the whole business">'
           f'<polygon points="0,80 {width},4 {width},94 0,94" fill="#f0e3d0"></polygon>'
           f'<line x1="0" y1="80" x2="{width}" y2="4" stroke="#a97739" stroke-width="1.5"></line>'
           f'<line x1="0" y1="94" x2="{width}" y2="94" stroke="#d5cabb" stroke-width="1"></line></svg>')
    fig=figure(A,"Case one &middot; the sequence","fill","How the capability grew",
      "Five capabilities in the order they were established.",
      grid+wedge,
      takeaway("Each capability earned the next. By the end the team sat inside quarterly planning, and its research and service design shaped where the business went next.",
               "Left to right is seven years. The band beneath is how much of the customer&rsquo;s experience design was allowed to own, from one screen to connected vehicle apps, in-vehicle multimedia and EV."),
      right="2018 &nbsp;&rarr;&nbsp; 2026")
    return f'<div class="wk-arc wk-anim">{fig}</div>'

# ---------------------------------------------------------------- service gap (dark)
SLICES=[("Choosing","Another business unit",0),("Buying","Another business unit",0),
        ("Connected services","Connected Technologies, and the app.",1),
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
            f'What I did was make the case for it and hire into it.</p></div>')
    return (f'<div style="border-top:2px solid {AD};padding-top:var(--s5);">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:32px;margin-bottom:var(--s4);">'
            f'<div style="display:flex;align-items:center;gap:10px;">{dot(AD,"fill",10)}'
            f'<p class="lbl" style="color:{AD};">Case one &middot; what service design was for</p></div>'
            f'<p class="lbl" style="color:var(--night-muted);text-align:right;">No Toyota blueprint is shown. This is the shape of the problem.</p></div>'
            f'<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);max-width:1000px;">A disjointed experience is a faithful picture of a disjointed business</p>'
            f'<p style="font-size:15.5px;line-height:1.75;color:var(--night-muted);max-width:800px;margin:0 0 var(--s7);">'
            f'Once Connected Technologies owned the European app, the gaps between divisions became its problem too.</p>'
            f'<p class="lbl" style="color:var(--night-muted);margin-bottom:var(--s4);">Before &nbsp;&middot;&nbsp; one slice, the rest owned elsewhere</p>'
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

DISC6=[("Product design","UX and UI","Insight, user journey flows and the screens themselves."),
 ("Design system","Technical UI","iOS and Android components, tokens, and design governance."),
 ("UX research","Strategy and insight","Formative and evaluative customer insight."),
 ("Service design","Blueprints","Mapping front stage experiences and back stage operations."),
 ("Content and creative","Art direction and copy","Words, pictures and ideas for everyone, and everything in between."),
 ("Design leadership","Vision, planning and delivery","Team management, UX and creative direction, design strategy and delivery.")]
DMO=[("Process",["User-centred and lean research methods, innovation pathways","Research hub, consistent toolsets, the design system, standards and metrics","A community of practice, shared systems and methods"]),
 ("People",["Team design, org structure, role definition","Learning, individual career progression, goal setting","Talent and culture, rituals, people operations"]),
 ("Projects",["Business development, planning, resourcing, estimation","Project framing, impact evaluation, playbooks, defining good and done","Metrics for success, value creation, skills training"])]

def opmodel():
    cards="".join(
      f'<div style="border-top:2px solid {"var(--amber)" if n=="Service design" else "var(--rule-2)"};padding-top:var(--s4);">'
      f'<p class="d4" style="font-size:19px;margin-bottom:2px;">{n}</p>'
      f'<p class="lbl" style="color:{"var(--amber)" if n=="Service design" else "var(--faint)"};margin-bottom:var(--s3);">{sub}</p>'
      f'<p style="font-size:13.5px;line-height:1.6;color:var(--body);margin:0;">{d}</p></div>' for n,sub,d in DISC6)
    head="".join(f'<p class="lbl" style="color:var(--amber);padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);">{h}</p>' for h in ["Define","Equip","Support"])
    rows="".join(
      f'<p class="lbl" style="padding:var(--s4) 0 0;">{r}</p>'
      + "".join(f'<p style="font-size:13.5px;line-height:1.6;color:var(--body);margin:0;padding:var(--s4) 0 var(--s3);border-bottom:1px solid var(--rule);">{c}</p>' for c in cells)
      for r,cells in DMO)
    matrix=(f'<div style="display:grid;grid-template-columns:110px 1fr 1fr 1fr;gap:0 var(--s5);align-items:start;">'
            f'<span></span>{head}{rows}</div>')
    dmo=(f'<div style="display:grid;grid-template-columns:300px 1fr;gap:var(--s8);align-items:start;">'
         f'<div><p class="d4" style="margin-bottom:var(--s3);">Design Management Office</p>'
         f'<p style="font-size:14px;line-height:1.65;color:var(--body);margin:0 0 var(--s4);">The centre of the function. It defined how design engaged with product and engineering, equipped the embedded teams with shared standards and systems, and supported them as engagements matured.</p>'
         f'<p style="font-size:13px;line-height:1.6;color:var(--muted);margin:0;">Design systems &middot; design operations &middot; design leadership &middot; business development</p></div>{matrix}</div>')
    F='font-family="Schibsted Grotesk,Helvetica,sans-serif"'
    curve=('<svg viewBox="0 0 1120 220" width="100%" height="220" preserveAspectRatio="none" style="display:block;" aria-label="Evangelism gives way to operations as an embedded engagement matures">'
      '<path d="M0,20 C300,20 420,180 560,180 C700,180 820,190 1120,196 L1120,200 L0,200 Z" fill="#a97739" fill-opacity="0.35"></path>'
      '<path d="M0,196 C300,190 420,180 560,180 C700,180 820,20 1120,20 L1120,200 L0,200 Z" fill="#3f7d7a" fill-opacity="0.35"></path>'
      '<line x1="0" y1="200" x2="1120" y2="200" stroke="#d5cabb"></line>'
      f'<text x="120" y="86" {F} font-size="13" font-weight="700" letter-spacing="1.6" fill="#7a5327">EVANGELISM</text>'
      f'<text x="1000" y="86" text-anchor="end" {F} font-size="13" font-weight="700" letter-spacing="1.6" fill="#2f5f5c">OPERATIONS</text></svg>'
      '<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">'
      + "".join(f'<p class="lbl" style="color:var(--muted);{"text-align:right;" if i==3 else ("text-align:center;" if i in (1,2) else "")}">{t}</p>' for i,t in enumerate(["Awareness","Influence","Impact","Scale"])) + '</div>')
    foot=("".join(
      f'<div><p class="lbl" style="color:var(--faint);margin-bottom:var(--s2);">{h}</p>'
      f'<p style="font-size:14px;line-height:1.6;color:{c};margin:0;{w}">{t}</p></div>'
      for h,t,c,w in [
        ("Positioning","A published service catalogue and sales collateral. Partner teams bought the depth they needed.","var(--body)",""),
        ("Commercial","A P&amp;L. Every designer I hired was paid for by work I had won.","var(--body)",""),
        ("Effect","Design&rsquo;s commercial contribution became visible to senior leadership for the first time.","var(--ink)","font-weight:500;")]))
    body=(f'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s5);">Six disciplines, one team</p>'
          f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s5) var(--s6);">{cards}</div>'
          f'<p class="lbl" style="margin:var(--s8) 0 var(--s5);padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);">The office behind the embedded teams</p>{dmo}'
          f'<p class="lbl" style="margin:var(--s8) 0 var(--s4);padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);">How an embedded engagement changes over time</p>{curve}'
          f'<p style="font-size:13.5px;line-height:1.6;color:var(--muted);max-width:760px;margin:var(--s4) 0 0;">Early on the work is evangelism, making the case for design inside a client team. As the client sees the value, the work shifts to operations, scaling design into the team and its ways of working.</p>'
          f'<div style="margin-top:var(--s7);padding-top:var(--s5);border-top:1px solid var(--rule);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s6);">{foot}</div>')
    return figure(A,"Case one &middot; how it was run","fill","Run as an internal consultancy",
      "Six disciplines under one roof, a management office behind the embedded teams, and a service catalogue, explicit positioning and a P&amp;L.",
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
               "Everything shown here is the team&rsquo;s work.", colour=INK),
      right="The team&rsquo;s work")

# ---------------------------------------------------------------- SUS rounds
def sus(w=560):
    svg=(f'<svg viewBox="0 0 540 250" width="100%" height="250" preserveAspectRatio="none" style="display:block;" aria-label="SUS scores rising across rounds">'
     '<rect x="420" y="0" width="120" height="250" style="fill:var(--paper-2)"></rect>'
     '<line x1="0" y1="0" x2="540" y2="0" stroke="#e8e2da"></line><line x1="0" y1="125" x2="540" y2="125" stroke="#e8e2da"></line>'
     '<line x1="0" y1="249" x2="540" y2="249" stroke="#d5cabb"></line>'
     '<line x1="0" y1="33" x2="540" y2="33" style="stroke:var(--amber)" stroke-width="1.5" stroke-dasharray="5 5"></line>'
     '<line x1="0" y1="183" x2="540" y2="183" style="stroke:var(--amber)" stroke-dasharray="3 5"></line>'
     '<polyline points="70,142 210,92 350,83" fill="none" stroke="#3f7d7a" stroke-width="2.5"></polyline>'
     '<circle cx="70" cy="142" r="6" fill="#3f7d7a"></circle><circle cx="210" cy="92" r="6" fill="#3f7d7a"></circle><circle cx="350" cy="83" r="6" fill="#3f7d7a"></circle>'
     '<line x1="480" y1="70" x2="480" y2="249" stroke="#c5b9a8" stroke-dasharray="3 4"></line>'
     '<text x="70" y="128" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">73</text>'
     '<text x="210" y="78" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">79</text>'
     '<text x="350" y="69" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">80</text>'
     '<text x="536" y="27" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" style="fill:var(--amber)">TARGET 86</text>'
     '<text x="536" y="177" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" style="fill:var(--amber)">GLOBAL AVERAGE 68</text></svg>')
    axis=('<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">'
          + "".join(f'<p class="lbl" style="color:{c};text-align:center;">Round {i}</p>' for i,c in
                    [(1,"var(--muted)"),(2,"var(--muted)"),(3,"var(--muted)"),(4,"var(--faint)")]) + '</div>')
    ys=('<div style="width:34px;display:flex;flex-direction:column;justify-content:space-between;height:250px;padding-bottom:2px;">'
        + "".join(f'<p class="lbl" style="color:var(--faint);letter-spacing:0;">{v}</p>' for v in [90,75,60]) + '</div>')
    body=f'<div style="display:flex;gap:var(--s3);"><div style="flex-grow:1;">{svg}{axis}</div>{ys}</div>'
    return figure(T,None,"ring","Four rounds of user testing, the same tasks each round",
      "System Usability Scale scores from four rounds of moderated testing on one set of EV tasks.",
      body,
      takeaway("Four rounds on one task set, moderated, with a team of contract researchers.",
               "Three reported SUS scores. The fourth round was run to task-completion target."), rule=False)

# ---------------------------------------------------------------- rating turnaround
def rating():
    def bar(label, one, mid, five, strong):
        onelab=f'<p style="font-size:13px;color:oklch(0.99 0 0);margin:0;">1&#9733; &nbsp;{one}%</p>' if one>20 else ""
        fivelab=f'<p style="font-size:13px;color:oklch(0.99 0 0);margin:0;">5&#9733; &nbsp;{five}%</p>' if five>40 else ""
        midlab=f'<p style="font-size:13px;color:oklch(0.35 0.06 80);margin:0;">{mid}%</p>'
        return (f'<div style="margin-bottom:var(--s5);">'
                f'<p style="font-size:13px;font-weight:600;color:{"var(--ink)" if strong else "var(--muted)"};margin:0 0 7px;">{label}</p>'
                f'<div style="display:flex;height:46px;border-radius:3px;overflow:hidden;">'
                f'<div style="width:{one}%;background:#ec7b72;display:flex;align-items:center;padding-left:10px;">{onelab}</div>'
                f'<div style="width:{mid}%;background:#f6d56b;display:flex;align-items:center;padding-left:10px;">{midlab}</div>'
                f'<div style="width:{five}%;background:#7bbf84;display:flex;align-items:center;padding-left:12px;">{fivelab}</div></div></div>')
    head=(f'<div style="display:flex;align-items:flex-end;gap:var(--s5);margin-bottom:var(--s7);">'
          f'<div><p class="lbl" style="color:var(--faint);margin-bottom:var(--s1);">At launch</p>'
          f'<p class="stat" style="color:var(--muted);font-size:54px;">1.9<span style="font-size:0.5em;color:#f2b632;vertical-align:0.35em;margin-left:0.06em;">&#9733;</span></p></div>'
          f'<p style="font-size:32px;color:var(--rule-2);padding-bottom:8px;margin:0;">&rarr;</p>'
          f'<div><p class="lbl" style="color:{A};margin-bottom:var(--s1);">August 2025</p>'
          f'<p class="stat" style="font-size:54px;">4.6<span style="font-size:0.5em;color:#f2b632;vertical-align:0.35em;margin-left:0.06em;">&#9733;</span></p></div>'
          f'<p class="t3" style="margin:0 0 10px auto;max-width:190px;text-align:right;">Rating more than doubled over thirteen months.</p></div>')
    key="".join(f'<div style="display:flex;align-items:center;gap:7px;"><span style="width:11px;height:11px;background:{c};'
                f'{b}display:inline-block;"></span><p class="t3" style="font-size:12px;">{n}</p></div>'
                for n,c,b in [("One star","#ec7b72",""),
                              ("Two to four","#f6d56b",""),("Five stars","#7bbf84","")])
    body=(head+'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:20px;">Share of reviews, by star rating</p>'
          +bar("Before",67,19,14,False)+bar("After",5,17,78,True)
          +f'<div style="display:flex;gap:20px;align-items:center;padding-top:var(--s4);border-top:1px solid var(--rule);">{key}'
          f'<p style="font-size:13px;font-weight:600;color:var(--ink);margin:0 0 0 auto;">One star: 2 in 3 &rarr; 1 in 20</p></div>')
    return figure(A,"Case two &middot; the rating data","fill","The public rating data",
      "The rating, and the share of reviews behind it.", body,
      takeaway("Five-star reviews grew nearly six-fold, and one-star reviews fell from two thirds of all reviews to five per cent.",
               "Public App Store and Play Store data, about 43,600 reviews. Lexus Link+; MyToyota shows the same pattern."), rule=False)

# ---------------------------------------------------------------- context growth
def ctx():
    svg=('<svg viewBox="0 0 520 270" width="100%" height="270" preserveAspectRatio="none" style="display:block;" aria-label="System prompt characters growing from session one to session four">'
     '<line x1="0" y1="1" x2="520" y2="1" stroke="#e8e2da"></line><line x1="0" y1="135" x2="520" y2="135" stroke="#e8e2da"></line>'
     '<line x1="0" y1="269" x2="520" y2="269" stroke="#d5cabb"></line>'
     '<polygon points="120,228 400,24 400,269 120,269" fill="#efe9e1"></polygon>'
     '<rect x="40" y="228" width="80" height="41" fill="#c5b9a8"></rect><rect x="400" y="28" width="80" height="241" fill="#1e1a16"></rect>'
     '<line x1="0" y1="209" x2="520" y2="209" stroke="#a97739" stroke-width="2" stroke-dasharray="6 5"></line>'
     '<text x="516" y="203" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.2" fill="#a97739">BOUNDED PROMPT: HARD BUDGET</text>'
     '<text x="80" y="218" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">5,600</text>'
     '<text x="440" y="20" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="16" font-weight="700" fill="#1e1a16">34,000+</text>'
     '<text x="260" y="130" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="12.5" fill="#8a7d6e">accumulated, session on session</text></svg>')
    axis=('<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:var(--s2);">'
          '<p class="lbl" style="color:var(--muted);text-align:center;">Session 1</p>'
          '<p class="lbl" style="color:var(--faint);text-align:center;">2</p>'
          '<p class="lbl" style="color:var(--faint);text-align:center;">3</p>'
          '<p class="lbl" style="color:var(--muted);text-align:center;">Session 4</p></div>')
    ys=('<div style="width:44px;display:flex;flex-direction:column;justify-content:space-between;height:270px;padding-bottom:2px;">'
        + "".join(f'<p class="lbl" style="color:var(--faint);letter-spacing:0;">{v}</p>' for v in ["36k","18k","0"]) + '</div>')
    body=f'<div style="display:flex;gap:var(--s3);"><div style="flex-grow:1;">{svg}{axis}</div>{ys}</div>'
    return figure(A,"Case four &middot; the failure","fill","Everything was working. The prompt had grown six times.",
      "Quality started degrading around the fourth session per user. Context had simply accumulated until the model was drowning in its own history.",
      body,
      takeaway("The fix was architectural. A bounded prompt with hard character budgets, enforced however many sessions a user has had.",
               "Sessions two and three are shown as accumulation rather than measured points. The two figures are the ones I recorded."))

# ---------------------------------------------------------------- complaint timeline (dark)
BEATS=[("2024","Design dominates the complaints","The deprecated US app lands in Europe at 1.9 stars. Navigation customers cannot learn, information displays they cannot read, no dark mode, driving analytics nobody understands.",False),
 ("Spring 2025","The language shifts","&ldquo;Intuitive&rdquo;, &ldquo;simple and effective&rdquo;, &ldquo;very well thought out&rdquo; start appearing in customer feedback where the complaints used to be.",False),
 ("June 2025","Design credited by name","An internal customer-experience report attributes reduced complaint volume directly to intuitive design. The first time on record that design was named as the cause of an improvement.",False),
 ("August 2025","Out of the top five","Displaced by backend and connectivity issues outside design&rsquo;s ownership. The 4.6 star rating stabilises.",True)]

def timeline():
    F='font-family="Schibsted Grotesk,Helvetica,sans-serif"'
    xs=[6,288.5,577,865.5]
    stems="".join(f'<line class="tl-stem" style="--i:{k}" x1="{x}" y1="{50 if k<3 else 116}" x2="{x}" y2="150" stroke="#d5cabb" stroke-width="1" stroke-dasharray="2 4"></line>' for k,x in enumerate(xs))
    dots="".join(f'<circle class="tl-dot" style="--i:{k}" cx="{x}" cy="50" r="6" style="fill:var(--amber)"></circle>' for k,x in enumerate(xs[:3]))
    track=('<svg class="tl-svg" viewBox="0 0 1120 150" width="100%" height="150" preserveAspectRatio="none" style="display:block;overflow:visible;" '
     'aria-label="Design inside the top five complaint categories, then out of them">'
     '<rect class="tl-band" x="0" y="18" width="1120" height="70" rx="3" style="fill:var(--amber-wash)"></rect>'
     '<line class="tl-band" x1="0" y1="88" x2="1120" y2="88" stroke="#d5cabb" stroke-width="1"></line>'
     f'{stems}'
     f'<path class="tl-path" pathLength="1" d="M{xs[0]},50 L{xs[2]},50 C{xs[2]+110},50 {xs[2]+160},116 {xs[3]},116" fill="none" style="stroke:var(--amber)" stroke-width="2.5" stroke-linecap="round"></path>'
     f'{dots}'
     f'<circle class="tl-dot tl-exit" style="--i:3" cx="{xs[3]}" cy="116" r="7" fill="#f8f6f2" stroke="#3f7d7a" stroke-width="2.5"></circle>'
     f'<text class="tl-band" x="1106" y="39" text-anchor="end" {F} font-size="11" font-weight="700" letter-spacing="1.4" style="fill:var(--amber)">INSIDE THE TOP FIVE COMPLAINT CATEGORIES</text>'
     f'<text class="tl-exit-label" x="{xs[3]-6}" y="144" text-anchor="start" {F} font-size="11" font-weight="700" letter-spacing="1.4" fill="#3f7d7a">OUT OF THE TOP FIVE</text></svg>')
    cols="".join(
      f'<div class="tl-beat" style="--i:{k};border-top:1px solid {T if last else "var(--rule)"};padding-top:18px;">'
      f'<p class="lbl" style="color:{T if last else A};margin-bottom:10px;">{d}</p>'
      f'<p style="font-size:17.5px;font-weight:600;color:var(--ink);margin:0 0 10px;line-height:1.35;letter-spacing:-0.012em;">{h}</p>'
      f'<p style="font-size:13px;line-height:1.7;color:var(--muted);margin:0;">{t}</p></div>' for k,(d,h,t,last) in enumerate(BEATS))
    fig=figure(A,"Case two &middot; the outcome","fill","Thirteen months from complaint driver to differentiator",
      "Design dominated the complaint list when the repurposed app landed. Then it left the list altogether.",
      track+f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:34px;padding-top:12px;">{cols}</div>', "",
      right="Internal customer-experience reporting, Jul 2024 to Aug 2025")
    return f'<div class="wk-tl wk-anim">{fig}</div>'

