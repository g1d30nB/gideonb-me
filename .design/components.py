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
def pairing(emotrix_src, prepcall_src, prepcall_pending=True):
    pc_prov = "PrepCall, live product" if not prepcall_pending else "PrepCall, illustrative report (real frame to follow)"
    left = plate(emotrix_src, "The reading arrives. Five constructs against the participant&rsquo;s own baseline, two interpreted lines above them, hatched where no reading is asserted.",
                 "Emotrix, real interface, synthetic session", dark=True)
    right = plate(prepcall_src, "What the product does with it. The listening half of a coaching report: what was said, then how it sounded, then one thing to try.",
                  pc_prov, dark=True)
    return (f'<div style="display:grid;grid-template-columns:7fr 5fr;gap:var(--s7);align-items:start;">{left}{right}</div>'
            f'<div style="display:flex;align-items:flex-start;justify-content:space-between;gap:var(--s7);margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid var(--night-rule);">'
            f'<p style="font-size:17px;line-height:1.7;font-weight:500;color:var(--night-ink);max-width:720px;margin:0;">Signal on the left, meaning on the right. The design work is the layer between them, and it is the same layer in both products.</p>'
            f'<p style="font-size:13px;line-height:1.6;color:var(--night-muted);max-width:300px;text-align:right;margin:0;">Both run on Hume&rsquo;s Empathic Voice Interface. Both built solo.</p></div>')

# ---------------------------------------------------------------- ownership split (leading at a distance)
OWNED_ME=["The standard, the strategic context, the operating model",
          "The quality bar, held at review points",
          "The investment, the protection of time, the cover for hard calls",
          "Framing the problems so the team had a sharp target"]
OWNED_LEADS=["The daily design decisions",
             "The customer-facing detail",
             "The craft, end to end",
             "Their own development, inside a written progression framework"]

def ownership():
    def col(label, colour, kind, items):
        rows="".join(f'<div style="display:flex;gap:12px;align-items:flex-start;padding:var(--s3) 0;border-top:1px solid var(--rule);">'
                     f'{dot(colour,kind,9)}<p style="font-size:15.5px;line-height:1.6;color:var(--ink);margin:-3px 0 0;">{t}</p></div>' for t in items)
        return (f'<div><div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s4);">{dot(colour,kind,11)}'
                f'<p class="lbl" style="color:{colour};">{label}</p></div>{rows}</div>')
    body=(f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s8);">'
          f'{col("I owned",A,"fill",OWNED_ME)}{col("The leads owned",T,"ring",OWNED_LEADS)}</div>')
    return figure(A,"Case one &middot; leading at a distance","fill","Two columns, and the line between them was the job",
      "Stepping out of the daily craft was a choice. The split below is what it meant in practice.",
      body,
      takeaway("When executives wanted to understand a specific change, I brought the designer who had made it.",
               "The same split, at the same level, ran the app in case two."))

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
                f'<div style="width:{100-perm}%;background:oklch(0.90 0.014 80);display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:var(--muted);">Contract</span></div></div></div>')
    loop="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s3);"><p class="stat" style="font-size:30px;margin-bottom:4px;">{v}</p>'
                 f'<p style="font-size:12px;line-height:1.45;color:var(--muted);margin:0;">{l}</p></div>'
                 for v,l in [("185","pieces of feedback"),("10","themes"),("14","initiatives, each with a named owner"),("3","horizons")])
    body=(f'<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:var(--s8);align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Two pathways, converging at Lead</p>{path}'
          f'<p class="lbl" style="margin:var(--s5) 0 var(--s2);color:var(--faint);">Written expectations at every level</p>{expect}</div>'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Same headcount, a different team</p>'
          f'{bar("Roughly, when I started the shift",50,"oklch(0.55 0.075 62)")}{bar("At the end",67,"oklch(0.48 0.085 62)")}'
          f'<p class="lbl" style="margin:var(--s5) 0 var(--s3);color:var(--faint);">The listening cycle, every year</p>'
          f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s4);">{loop}</div></div></div>')
    return figure(A,"Case one &middot; growing people","fill","Every one of the 40+ hired by me, and most of them stayed",
      "The half of the job that takes years to learn. Progression before scale, listening that closed the loop, and a workforce shaped for the long term.",
      body,
      takeaway("The highest permanent retention rate of any department in the company, and a service design capability still running without me.",
               "Level codes and the framework document itself stay internal."))

# ---------------------------------------------------------------- redrawn from the decks
def ladder():
    """Two pathways diverging upward from Senior Designer. Redrawn from the framework diagram; no level codes."""
    F='font-family="Schibsted Grotesk,Helvetica,sans-serif"'
    disc=["UX research","Product design","Service design","Design systems","Content"]
    xs=[150,200,250,300,350]
    s=[f'<svg viewBox="0 0 560 420" width="100%" height="420" preserveAspectRatio="xMidYMid meet" style="display:block;" aria-label="Career framework: practitioner and people pathways">']
    # trunk
    s.append('<line x1="250" y1="400" x2="250" y2="250" stroke="#1e1a16" stroke-width="2"></line>')
    for y,l in [(400,"Junior designer"),(340,"Mid designer"),(250,"Senior designer")]:
        s.append(f'<circle cx="250" cy="{y}" r="4.5" fill="#1e1a16"></circle><text x="238" y="{y+4}" text-anchor="end" {F} font-size="12.5" fill="#1e1a16">{l}</text>')
    # practitioner branches
    for x,d in zip(xs,disc):
        s.append(f'<path d="M250,250 C250,215 {x},215 {x},190 L{x},120" fill="none" stroke="#9a6a34" stroke-width="1.6"></path>')
        s.append(f'<circle cx="{x}" cy="190" r="3.5" fill="#9a6a34"></circle><circle cx="{x}" cy="120" r="3.5" fill="#9a6a34"></circle>')
        s.append(f'<text x="{x}" y="108" text-anchor="start" transform="rotate(-90 {x} 108)" {F} font-size="9.5" letter-spacing="0.6" fill="#8a7d6e">{d.upper()}</text>')
    s.append(f'<text x="138" y="124" text-anchor="end" {F} font-size="12.5" fill="#9a6a34">Principal designer</text>')
    s.append(f'<text x="138" y="194" text-anchor="end" {F} font-size="12.5" fill="#9a6a34">Lead designer, practice</text>')
    # people track
    s.append('<path d="M250,250 C250,230 440,240 440,190 L440,60" fill="none" stroke="#3f7d7a" stroke-width="1.6"></path>')
    for y,l in [(190,"Lead designer"),(120,"Design manager"),(60,"Head of design")]:
        s.append(f'<circle cx="440" cy="{y}" r="4" fill="#3f7d7a"></circle><text x="456" y="{y+4}" {F} font-size="12.5" fill="#3f7d7a">{l}</text>')
    # the crossover between tracks at Lead, dashed
    s.append('<line x1="350" y1="190" x2="440" y2="190" stroke="#3f7d7a" stroke-width="1" stroke-dasharray="3 4"></line>')
    s.append(f'<text x="150" y="14" {F} font-size="11" font-weight="700" letter-spacing="1.3" fill="#9a6a34">PRACTITIONER LEADERSHIP</text>')
    s.append(f'<text x="440" y="14" text-anchor="middle" {F} font-size="11" font-weight="700" letter-spacing="1.3" fill="#3f7d7a">PEOPLE LEADERSHIP</text>')
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
                f'<div style="width:{100-perm}%;background:oklch(0.90 0.014 80);display:flex;align-items:center;padding-left:10px;"><span style="font-size:12px;color:var(--muted);">Contract</span></div></div></div>')
    body=(f'<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:var(--s8);align-items:start;">'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Two pathways, one framework</p>{ladder()}'
          f'<p class="lbl" style="margin:var(--s4) 0 var(--s2);color:var(--faint);">Written expectations at every level</p>{expect}</div>'
          f'<div><p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s4);">Listening that closed the loop</p>{listening()}'
          f'<p class="lbl" style="margin:var(--s6) 0 var(--s3);color:var(--faint);">Same headcount, a different team</p>'
          f'{bar("Roughly half permanent, when the shift began",50,"oklch(0.55 0.075 62)")}{bar("Two thirds permanent, at the end",67,"oklch(0.48 0.085 62)")}</div></div>')
    return figure(A,"Case one &middot; growing people","fill","Every one of the 40+ hired by me, and most of them stayed",
      "The half of the job that takes years to learn. Progression before scale, listening that closed the loop, and a workforce shaped for the long term.",
      body,
      takeaway("The highest permanent retention rate of any department in the company, and a service design capability still running without me.",
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
