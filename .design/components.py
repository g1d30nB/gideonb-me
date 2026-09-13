# New components for the v2 page: plates (product frames), the Emotrix + PrepCall pairing,
# the ownership split, and the growing-people figure. Same tokens as diagrams.py.
from diagrams import dot, kicker, takeaway, figure, A, T, INK, AD, TD

# ---------------------------------------------------------------- plates
def plate(src, what, provenance, width="100%", dark=False, aspect=None, fit="cover", pos="top"):
    """A product frame. No device chrome, no radius: a hairline plate with a caption strip.
    aspect crops the image to a fixed ratio so a tall screenshot can sit in a short slot."""
    ink = "var(--night-ink)" if dark else "var(--ink)"
    mut = "var(--night-muted)" if dark else "var(--muted)"
    rule = "var(--night-rule)" if dark else "var(--rule-2)"
    img_style = f"display:block;width:100%;{'aspect-ratio:'+aspect+';object-fit:'+fit+';object-position:'+pos+';' if aspect else 'height:auto;'}"
    return (f'<figure style="margin:0;width:{width};">'
            f'<div style="border:1px solid {rule};background:{"var(--night-2)" if dark else "var(--paper-2)"};">'
            f'<img src="{src}" alt="" style="{img_style}"></div>'
            f'<figcaption style="display:flex;flex-direction:column;gap:5px;padding-top:10px;">'
            f'<span style="font-size:12.5px;line-height:1.5;color:{ink};font-weight:500;">{what}</span>'
            f'<span style="font-size:10.5px;letter-spacing:0.08em;text-transform:uppercase;color:{mut};line-height:1.5;">{provenance}</span>'
            f'</figcaption></figure>')

def phone_row(items, dark=False, cols=None):
    """App Store frames stepping across the width. items = [(src, what, provenance), ...]."""
    n = cols or len(items)
    cells = "".join(plate(s, w, p, dark=dark, aspect="9 / 19.5", fit="cover", pos="top") for s, w, p in items)
    return f'<div style="display:grid;grid-template-columns:repeat({n},minmax(0,1fr));gap:var(--s5);align-items:start;">{cells}</div>'

# ---------------------------------------------------------------- the pairing (case three centrepiece)
def pairing(emotrix_src, prepcall_src):
    # Two plates at one height: 7:5 columns, so the left aspect is 7/5 of the right one. Rounded, no hairline.
    def uni(src, what, prov, aspect, pos="center"):
        return (f'<figure style="margin:0;width:100%;">'
                f'<div style="border-radius:10px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,0.3),0 12px 32px rgba(0,0,0,0.35);">'
                f'<img src="{src}" alt="" style="display:block;width:100%;aspect-ratio:{aspect};object-fit:cover;object-position:{pos};"></div>'
                f'<figcaption style="display:flex;flex-direction:column;gap:5px;padding-top:10px;">'
                f'<span style="font-size:12.5px;line-height:1.5;color:var(--night-ink);font-weight:500;">{what}</span>'
                f'<span style="font-size:10.5px;letter-spacing:0.08em;text-transform:uppercase;color:var(--night-muted);line-height:1.5;">{prov}</span>'
                f'</figcaption></figure>')
    left = uni(emotrix_src, "The reading. Five constructs against the participant&rsquo;s own baseline, two interpreted lines above them, hatched where no reading is asserted.",
               "Emotrix, real interface, synthetic session", "1028/406", "center top")
    right = uni(prepcall_src, "What the product does with it. The listening half of a coaching report. What was said, how it sounded, and one thing to try.",
                "PrepCall, live product", "734/406", "center")
    return (f'<div style="display:grid;grid-template-columns:7fr 5fr;gap:var(--s7);align-items:start;">{left}{right}</div>'
            f'<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:var(--s7);margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid var(--night-rule);">'
            f'<p style="font-size:17px;line-height:1.7;font-weight:500;color:var(--night-ink);max-width:720px;margin:0;">On the left, Emotrix reads emotional markers from face and voice together and plots what they mean across a session, against the participant&rsquo;s own baseline. On the right, PrepCall reads the same kind of signal from voice alone and turns it into a coaching report. In both, the design work is the layer that turns a reading into something a person can act on.</p>'
            f'<p style="font-size:13px;line-height:1.6;color:var(--night-muted);max-width:300px;text-align:right;margin:0;">Both run on Hume&rsquo;s Empathic Voice Interface. Both built by me.</p></div>')

# ---------------------------------------------------------------- ownership split (leading at a distance)
OWNED_ME=["The standard, the strategic context, the operating model",
          "The quality bar, held at review points",
          "The investment, the protection of time, the cover for hard calls",
          "Seeing the problems early, and putting the right people on them",
          "The client relationship at executive level, and the governance behind it",
          "New business across the Toyota ecosystem, and the design relationships in North America and Japan",
          "Financial performance, and resourcing across every engagement"]
OWNED_LEADS=["The daily design decisions",
             "The craft end to end, and the reviews and critiques behind it",
             "The customer-facing detail",
             "Resourcing inside the engagement",
             "The day-to-day client relationship, and the monthly report back",
             "New work inside the accounts they already ran",
             "Growing the people on their teams"]
HELD_TOGETHER=["Strategic planning, and the decisions that shaped the team",
               "Client satisfaction and the standard of what we delivered",
               "Team culture and career development",
               "Design quality and how the process improved"]

def ownership():
    """Two columns paired so each row reads across, a shared band beneath, then how each
    role was measured. DOM order stays grouped by column so mobile gives two labelled lists."""
    def head(label, colour, kind, col):
        return (f'<div class="wk-own-h" style="grid-column:{col};grid-row:1;">{dot(colour,kind,11)}'
                f'<p class="lbl" style="color:{colour};margin:0;">{label}</p></div>')
    def item(t, colour, kind, col, row):
        return (f'<div class="wk-own-i" style="grid-column:{col};grid-row:{row};">{dot(colour,kind,9)}'
                f'<p style="font-size:15.5px;line-height:1.6;color:var(--ink);margin:-3px 0 0;">{t}</p></div>')
    cells  = [head("I owned",A,"fill",1)]
    cells += [item(t,A,"fill",1,k+2) for k,t in enumerate(OWNED_ME)]
    cells += [head("My design managers and leads owned",T,"ring",2)]
    cells += [item(t,T,"ring",2,k+2) for k,t in enumerate(OWNED_LEADS)]
    grid = f'<div class="wk-own">{"".join(cells)}</div>'

    intro = ('<p style="font-size:15.5px;line-height:1.75;color:var(--body);max-width:780px;margin:0 0 var(--s6);">'
             'The organisation ran in three layers. I sat above two design managers, and the design leads sat '
             'inside each product team. I wrote this split down and agreed it with my design manager so we both '
             'knew where the line sat.</p>')

    lead_in = ('<p style="font-size:16.5px;line-height:1.6;font-weight:500;color:var(--ink);'
               'margin:var(--s7) 0 var(--s4);">We held some of it together.</p>')
    band_items = "".join('<p style="font-size:14.5px;line-height:1.55;color:var(--ink);margin:0;">'
                         f'{t}</p>' for t in HELD_TOGETHER)
    band = (f'<div class="wk-own-band">'
            f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s4);">'
            f'{dot("var(--ink)","fill",11)}<p class="lbl" style="color:var(--ink);margin:0;">Held together</p></div>'
            f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s5);">{band_items}</div></div>')

    escalation = ('<p style="font-size:15.5px;line-height:1.75;color:var(--body);max-width:780px;margin:var(--s6) 0 0;">'
                  'When delivery risk, a stakeholder conflict or a resourcing problem went past what a manager '
                  'could settle, it came to me.</p>')

    def measure(lead, rest, colour):
        return (f'<p style="font-size:14.5px;line-height:1.65;color:var(--body);margin:0;">'
                f'<span style="color:{colour};font-weight:600;">{lead}</span> {rest}</p>')
    measured = (f'<div class="wk-own-m">'
                f'<p class="lbl" style="color:var(--muted);margin:0 0 var(--s4);">How each role was measured</p>'
                f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s7);">'
                + measure("What I was measured on:",
                          "revenue growth and new business, budget and resourcing across all engagements, "
                          "talent retention, the maturity of the practice", A)
                + measure("What they were measured on:",
                          "project profitability and utilisation, client satisfaction and delivery, "
                          "team performance and individual growth, design quality", T)
                + '</div></div>')

    return figure(A,"Case one &middot; leading at a distance","fill",
      "What I owned, and what my design managers and leads owned",
      "This is how the split ran day to day.",
      intro + grid + lead_in + band + escalation + measured,
      takeaway("The app team in case two ran on the same split."))

# ---------------------------------------------------------------- growing people
def people():
    # pathways converging at Lead
    path=('<svg viewBox="0 0 520 190" width="100%" height="190" preserveAspectRatio="none" style="display:block;" aria-label="Two progression pathways converging at Lead">'
          '<line x1="20" y1="50" x2="330" y2="50" stroke="#d5cabb" stroke-width="1.5"></line>'
          '<line x1="20" y1="140" x2="330" y2="140" stroke="#d5cabb" stroke-width="1.5"></line>'
          '<path d="M330,50 C400,50 400,95 470,95" fill="none" stroke="#9a6a34" stroke-width="2"></path>'
          '<path d="M330,140 C400,140 400,95 470,95" fill="none" stroke="#3f7d7a" stroke-width="2"></path>'
          + "".join(f'<circle cx="{x}" cy="50" r="4" fill="#9a6a34"></circle>' for x in [20,120,220,330])
          + "".join(f'<circle cx="{x}" cy="140" r="4" fill="#3f7d7a"></circle>' for x in [20,120,220,330])
          + '<circle cx="470" cy="95" r="7" fill="#1e1a16"></circle>'
          '<text x="20" y="30" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.3" fill="#9a6a34">PRACTITIONER LEADERSHIP</text>'
          '<text x="20" y="170" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.3" fill="#3f7d7a">PEOPLE LEADERSHIP</text>'
          '<text x="470" y="78" text-anchor="middle" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="12" font-weight="700" fill="#1e1a16">LEAD</text>'
          '</svg>')
    expect="".join(f'<div style="border-top:1px solid var(--rule);padding:10px 0;font-size:13.5px;line-height:1.5;color:var(--body);">{t}</div>'
                   for t in ["What they do","How they decide","How they engage clients","What the next level asks for"])
    # contract to permanent, same headcount
    def bar(label, perm, colour_perm):
        return (f'<div style="margin-bottom:var(--s4);"><p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:0 0 6px;">{label}</p>'
                f'<div style="display:flex;height:34px;">'
                f'<div style="width:{perm}%;background:{colour_perm};display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:oklch(0.97 0.008 80);font-weight:600;">Permanent {perm}%</span></div>'
                f'<div style="width:{100-perm}%;background:var(--paper-2);display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:var(--muted);">Contract</span></div></div></div>')
    loop="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);"><p class="stat" style="font-size:30px;margin-bottom:4px;">{v}</p>'
                 f'<p style="font-size:12px;line-height:1.45;color:var(--muted);margin:0;">{l}</p></div>'
                 for v,l in [("185","pieces of feedback"),("10","themes"),("14","initiatives, each with a named owner"),("3","horizons")])
    body=(f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:var(--s8);align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Two pathways, converging at Lead</p>{path}'
          f'<p class="lbl" style="margin:var(--s5) 0 var(--s2);color:var(--faint);">Written expectations at every level</p>{expect}</div>'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Contract to permanent, at the same headcount</p>'
          f'{bar("Roughly, when I started the shift",50,"oklch(0.55 0.075 62)")}{bar("At the end",67,"oklch(0.48 0.085 62)")}'
          f'<p class="lbl" style="margin:var(--s5) 0 var(--s3);color:var(--faint);">The listening cycle, every year</p>'
          f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s4);">{loop}</div></div></div>')
    return figure(A,"Case one &middot; growing people","fill","Hiring, progression and retention",
      "Progression before scale, a listening cycle that closed the loop, and a shift from contract to permanent at the same headcount.",
      body,
      takeaway("The highest permanent retention rate of any department in the company.",
               "Level codes and the framework document itself stay internal."))

# ---------------------------------------------------------------- redrawn from the decks
def ladder():
    """Two pathways diverging upward from Senior Designer. Redrawn from the framework diagram; no level codes."""
    F='font-family="Schibsted Grotesk,Helvetica,sans-serif"'
    disc=["UX research","Product design","Service design","Design systems","Content"]
    xs=[150,200,250,300,350]
    s=[f'<svg viewBox="0 0 560 420" width="100%" height="420" preserveAspectRatio="xMidYMid meet" style="display:block;" aria-label="Career framework: practitioner and people pathways">']
    # trunk
    s.append('<line x1="250" y1="400" x2="250" y2="250" style="stroke:var(--ink)" stroke-width="2"></line>')
    for y,l in [(400,"Junior designer"),(340,"Mid designer"),(250,"Senior designer")]:
        s.append(f'<circle cx="250" cy="{y}" r="4.5" style="fill:var(--ink)"></circle><text x="238" y="{y+4}" text-anchor="end" {F} font-size="12.5" style="fill:var(--ink)">{l}</text>')
    # practitioner branches
    for x,d in zip(xs,disc):
        s.append(f'<path d="M250,250 C250,215 {x},215 {x},190 L{x},120" fill="none" style="stroke:var(--amber)" stroke-width="1.6"></path>')
        s.append(f'<circle cx="{x}" cy="190" r="3.5" style="fill:var(--amber)"></circle><circle cx="{x}" cy="120" r="3.5" style="fill:var(--amber)"></circle>')
        s.append(f'<text x="{x}" y="108" text-anchor="start" transform="rotate(-90 {x} 108)" {F} font-size="9.5" letter-spacing="0.6" style="fill:var(--muted)">{d.upper()}</text>')
    s.append(f'<text x="138" y="124" text-anchor="end" {F} font-size="12.5" style="fill:var(--amber)">Principal designer</text>')
    s.append(f'<text x="138" y="194" text-anchor="end" {F} font-size="12.5" style="fill:var(--amber)">Lead designer, practice</text>')
    # people track
    s.append('<path d="M250,250 C250,230 440,240 440,190 L440,60" fill="none" style="stroke:var(--teal)" stroke-width="1.6"></path>')
    for y,l in [(190,"Lead designer"),(120,"Design manager"),(60,"Head of design")]:
        s.append(f'<circle cx="440" cy="{y}" r="4" style="fill:var(--teal)"></circle><text x="456" y="{y+4}" {F} font-size="12.5" style="fill:var(--teal)">{l}</text>')
    # the crossover between tracks at Lead, dashed
    s.append('<line x1="350" y1="190" x2="440" y2="190" style="stroke:var(--teal)" stroke-width="1" stroke-dasharray="3 4"></line>')
    s.append(f'<text x="150" y="14" {F} font-size="11" font-weight="700" letter-spacing="1.3" style="fill:var(--amber)">PRACTITIONER LEADERSHIP</text>')
    s.append(f'<text x="440" y="14" text-anchor="middle" {F} font-size="11" font-weight="700" letter-spacing="1.3" style="fill:var(--teal)">PEOPLE LEADERSHIP</text>')
    s.append('</svg>')
    return "".join(s)

LISTEN=[("Career progression",55),("Role clarity",33),("Team goals",29),("Performance evaluation",28),("Organisational direction",26),("Resources",11)]
def listening():
    rows=[]
    for n,v in LISTEN:
        rows.append(f'<div style="display:grid;grid-template-columns:150px 1fr 32px;gap:10px;align-items:center;padding:5px 0;">'
                    f'<span style="font-size:12.5px;color:var(--body);">{n}</span>'
                    f'<span style="display:block;height:12px;width:{round(v/55*100)}%;background:oklch(0.575 0.075 62);"></span>'
                    f'<span class="stat" style="font-size:13px;text-align:right;">{v}</span></div>')
    return (f'<div style="display:flex;align-items:baseline;gap:12px;margin-bottom:6px;"><span class="stat" style="font-size:30px;">185</span>'
            f'<span style="font-size:12.5px;line-height:1.45;color:var(--muted);">pieces of feedback across six themes, one annual cycle</span></div>'
            + "".join(rows) +
            f'<p style="font-size:12.5px;line-height:1.55;color:var(--muted);margin:10px 0 0;">Fourteen initiatives across three horizons, each with a named owner and each traceable to the line that prompted it.</p>')

def people():
    expect="".join(f'<div style="border-top:1px solid var(--rule);padding:9px 0;font-size:13.5px;line-height:1.5;color:var(--body);">{t}</div>'
                   for t in ["What they do","How they decide","How they engage clients","What the next level asks for"])
    def bar(label, perm, colour_perm):
        return (f'<div style="margin-bottom:var(--s3);"><p style="font-size:12.5px;font-weight:600;color:var(--ink);margin:0 0 6px;">{label}</p>'
                f'<div style="display:flex;height:30px;">'
                f'<div style="width:{perm}%;background:{colour_perm};display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:oklch(0.97 0.008 80);font-weight:600;">Permanent</span></div>'
                f'<div style="width:{100-perm}%;background:var(--paper-2);display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:var(--muted);">Contract</span></div></div></div>')
    body=(f'<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:var(--s8);align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Two pathways, one framework</p>{ladder()}'
          '</div>'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Listening that closed the loop</p>{listening()}'
          f'<p class="lbl" style="margin:var(--s6) 0 var(--s3);color:var(--faint);">Contract to permanent, at the same headcount</p>'
          f'{bar("Roughly half permanent, when the shift began",50,"oklch(0.55 0.075 62)")}{bar("Two thirds permanent, at the end",67,"oklch(0.48 0.085 62)")}</div></div>')
    return figure(A,"Case one &middot; growing people","fill","Hiring, progression and retention",
      "Progression before scale, a listening cycle that closed the loop, and a shift from contract to permanent at the same headcount.",
      body,
      takeaway("The highest permanent retention rate of any department in the company.",
               "Redrawn from the framework. Level codes and the document itself stay internal."))

def orgmodel():
    """Design Management Office at the centre, embedded pods in client teams, a community of practice around them."""
    F='font-family="Schibsted Grotesk,Helvetica,sans-serif"'
    def pod(cx,cy,label):
        dots=[(-16,-10,"#3f7d7a","D"),(14,-10,"#8a7d6e","P"),(0,14,"#8a7d6e","E"),(-14,10,"#3f7d7a","D"),(16,10,"#8a7d6e","E")]
        g=[f'<circle cx="{cx}" cy="{cy}" r="44" fill="none" stroke="#c5b9a8" stroke-width="1.2"></circle>']
        for dx,dy,c,t in dots:
            g.append(f'<circle cx="{cx+dx}" cy="{cy+dy}" r="8" fill="{c}"></circle><text x="{cx+dx}" y="{cy+dy+3.5}" text-anchor="middle" {F} font-size="9" font-weight="700" fill="#f8f6f2">{t}</text>')
        g.append(f'<text x="{cx}" y="{cy+66}" text-anchor="middle" {F} font-size="11.5" fill="#5c5347">{label}</text>')
        return "".join(g)
    s=[f'<svg viewBox="0 0 640 360" width="100%" height="360" preserveAspectRatio="xMidYMid meet" style="display:block;" aria-label="Operating model: a central office, embedded pods, a community of practice">',
       '<ellipse cx="320" cy="180" rx="300" ry="160" fill="none" stroke="#d5cabb" stroke-width="1" stroke-dasharray="4 5"></ellipse>',
       f'<text x="320" y="345" text-anchor="middle" {F} font-size="11" font-weight="700" letter-spacing="1.3" fill="#8a7d6e">COMMUNITY OF PRACTICE</text>',
       '<circle cx="320" cy="180" r="74" fill="oklch(0.575 0.075 62)"></circle>',
       f'<text x="320" y="166" text-anchor="middle" {F} font-size="12.5" font-weight="700" fill="#f8f6f2">Design Management</text>',
       f'<text x="320" y="182" text-anchor="middle" {F} font-size="12.5" font-weight="700" fill="#f8f6f2">Office</text>',
       f'<text x="320" y="204" text-anchor="middle" {F} font-size="10" fill="#f8f6f2" opacity="0.85">standards, systems, ops,</text>',
       f'<text x="320" y="217" text-anchor="middle" {F} font-size="10" fill="#f8f6f2" opacity="0.85">leadership, delivery</text>']
    for cx,cy,l in [(120,120,"Client team, Europe"),(520,120,"Client team, Japan"),(120,250,"Client team, North America"),(520,250,"Client team, in-vehicle")]:
        s.append(f'<line x1="320" y1="180" x2="{cx}" y2="{cy}" stroke="#d5cabb" stroke-width="1"></line>')
        s.append(pod(cx,cy,l))
    s.append('</svg>')
    key=("".join(f'<span style="display:inline-flex;align-items:center;gap:6px;margin-right:16px;"><span style="width:12px;height:12px;border-radius:50%;background:{c};display:inline-block;"></span>'
                 f'<span style="font-size:12px;color:var(--muted);">{t}</span></span>' for c,t in [("#3f7d7a","Designer, embedded"),("#8a7d6e","Product and engineering counterparts")]))
    return "".join(s)+f'<div style="margin-top:6px;">{key}</div>'

# ---------------------------------------------------------------- case three: one decision, measured
def ev_measure(mobile=False):
    F='font-family="Schibsted Grotesk,Helvetica,sans-serif"'
    # ease against benchmark on a 1 to 7 scale
    ease=('<svg viewBox="0 0 520 90" width="100%" height="90" preserveAspectRatio="none" style="display:block;" aria-label="Ease score 5.15 against a benchmark of 5.5">'
      '<line x1="20" y1="46" x2="500" y2="46" stroke="#d5cabb" stroke-width="2"></line>'
      + "".join(f'<line x1="{20+i*80}" y1="41" x2="{20+i*80}" y2="51" stroke="#c5b9a8"></line><text x="{20+i*80}" y="70" text-anchor="middle" {F} font-size="10" fill="#b5a08a">{i+1}</text>' for i in range(7))
      + f'<line x1="380" y1="24" x2="380" y2="46" stroke="#1e1a16" stroke-width="1.5" stroke-dasharray="3 3"></line><text x="380" y="16" text-anchor="middle" {F} font-size="10.5" font-weight="700" letter-spacing="1" fill="#1e1a16">BENCHMARK 5.5</text>'
      + f'<circle cx="352" cy="46" r="7" fill="#3f7d7a"></circle><text x="352" y="86" text-anchor="middle" {F} font-size="12" font-weight="700" fill="#3f7d7a">5.15</text></svg>')
    # domain completion across three rounds, endpoints published
    comp=('<svg viewBox="0 0 520 210" width="100%" height="210" preserveAspectRatio="none" style="display:block;" aria-label="Task completion across the EV domain, 78 to 87 per cent over three rounds">'
      '<line x1="0" y1="190" x2="520" y2="190" stroke="#d5cabb"></line>'
      '<rect x="60" y="82" width="90" height="108" fill="#c5b9a8"></rect>'
      '<rect x="215" y="60" width="90" height="130" fill="none" stroke="#c5b9a8" stroke-dasharray="4 4"></rect>'
      '<rect x="370" y="36" width="90" height="154" fill="#3f7d7a"></rect>'
      f'<text x="105" y="72" text-anchor="middle" {F} font-size="16" font-weight="700" fill="#1e1a16">78%</text>'
      f'<text x="260" y="110" text-anchor="middle" {F} font-size="10" fill="#8a7d6e">round two</text><text x="260" y="124" text-anchor="middle" {F} font-size="10" fill="#8a7d6e">figure not published here</text>'
      f'<text x="415" y="26" text-anchor="middle" {F} font-size="16" font-weight="700" fill="#1e1a16">87%</text>'
      f'<text x="105" y="206" text-anchor="middle" {F} font-size="10" font-weight="700" letter-spacing="1" fill="#8a7d6e">ROUND 1</text><text x="260" y="206" text-anchor="middle" {F} font-size="10" font-weight="700" letter-spacing="1" fill="#b5a08a">ROUND 2</text><text x="415" y="206" text-anchor="middle" {F} font-size="10" font-weight="700" letter-spacing="1" fill="#8a7d6e">ROUND 3</text></svg>')
    standard="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);"><p class="stat" style="font-size:26px;margin-bottom:4px;">{v}</p><p style="font-size:12px;line-height:1.45;color:var(--muted);margin:0;">{l}</p></div>'
                     for v,l in [("3","rounds, May to July 2025"),("25","participants"),("4","countries: UK, Germany, Norway, Sweden"),("76","SUS, against an industry average of 68")])
    cols="1fr" if mobile else "5fr 7fr"
    body=(f'<div style="display:grid;grid-template-columns:{cols};gap:var(--s7);align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">The finding</p>'
          f'<div style="display:flex;align-items:baseline;gap:12px;margin-bottom:var(--s3);"><span class="stat" style="font-size:40px;">92%</span><span style="font-size:13px;line-height:1.45;color:var(--muted);">completed the schedule task</span></div>{ease}'
          f'<p style="font-size:13.5px;line-height:1.6;color:var(--body);margin:var(--s3) 0 0;">Completed, and rated below the benchmark for ease. The control worked and said nothing about its result.</p></div>'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">The change, measured across the EV domain</p>{comp}</div></div>'
          f'<p class="lbl" style="margin:var(--s6) 0 var(--s3);color:var(--faint);">The standard it was held to</p>'
          f'<div style="display:grid;grid-template-columns:repeat({2 if mobile else 4},minmax(0,1fr));gap:var(--s4);">{standard}</div>')
    return figure(T,"Case three &middot; what the research found","ring","The schedule control, measured",
      "A charging schedule people set and completed without trusting it. One change, stating the outcome on the screen, served new users and advanced users alike.",
      body,
      takeaway("The research was the team&rsquo;s. The standard and the decision were mine.",
               "Round two&rsquo;s domain figure is not published here; the two endpoints are the ones in the source deck."),
      right="Run by my research team")

# ---------------------------------------------------------------- the service catalogue, fully formed
CATALOGUE=[
 ("Business design",[("Insights",["Research and insights","Concept research","Prototyping","Usability research","UX and UI audit"]),
                     ("Experience strategy",["Futures design and innovation","Workshops and co-creation","Design leadership and strategy","Service design and journey mapping"])]),
 ("Product design",[("Experience standards",["Design at scale, systems and governance","Accessibility and inclusivity","Privacy"]),
                    ("Production and growth design",["UX and UI design","Design strategy and workshops","Growth-focused design"])]),
 ("Brand marketing design",[("Creative",["Brand, visual and tone","Marketing campaigns","Ideation and co-creation","Rapid concept, prototyping and idea generation"]),
                            ("Content and localisation",["Content creation","Animation, video and iconography","CMS and content strategy","Translation and localisation"])]),
]
STAGES=["Opportunity identification and problem framing","Validate, productionise, standardise","Iterate, validate and market fit","Scaling, adoption and market success"]

def catalogue():
    cols=[]
    for title,groups in CATALOGUE:
        g="".join(f'<p class="lbl" style="color:{A};margin:var(--s4) 0 var(--s2);">{h}</p>'
                  + "".join(f'<p style="font-size:13.5px;line-height:1.55;color:var(--body);margin:0 0 5px;padding-left:12px;text-indent:-12px;">&middot;&nbsp; {i}</p>' for i in items)
                  for h,items in groups)
        cols.append(f'<div style="border-top:2px solid var(--rule-2);padding-top:var(--s4);"><p class="d4" style="font-size:19px;">{title}</p>{g}</div>')
    stages="".join(
      f'<div style="display:flex;align-items:center;gap:var(--s4);">'
      f'<p style="font-size:14px;line-height:1.5;color:var(--ink);font-weight:500;margin:0;">{t}</p>'
      + ('<svg width="28" height="12" viewBox="0 0 28 12" style="flex-shrink:0;"><path d="M0,6 H24 M19,1 L25,6 L19,11" fill="none" stroke="#a97739" stroke-width="1.5"></path></svg>' if i<3 else '')
      + '</div>' for i,t in enumerate(STAGES))
    body=(f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s7);align-items:start;">{"".join(cols)}</div>'
          f'<p class="lbl" style="margin:var(--s7) 0 var(--s3);color:var(--faint);">From concept to market</p>'
          f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s5);border-top:1px solid var(--rule);padding-top:var(--s4);">{stages}</div>')
    return figure(A,"Case one &middot; the catalogue","fill","What the team offered, once it was fully formed",
      "The published service catalogue. Three practices, each bought by partner teams from concept through to market.",
      body, "", right="Toyota Experience Design")
