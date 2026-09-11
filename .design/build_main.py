from copy import *  # noqa
import re, io
AMBER="#b07a3c"; TEAL="#3f7d7a"; INK="#1e1a16"; DA="#d9a55f"; DT="#6fb0ab"

def part(name):
    return open(name).read().strip()

def inner(name):
    s = part(name)
    s = s[s.index('>')+1:]
    s = s[:s.rindex('</div>')]
    return s

def dot(colour, kind="fill", size=11):
    if kind == "ring":
        return f'<div style="width:{size}px; height:{size}px; border-radius:50%; border:2px solid {colour}; box-sizing:border-box; flex-shrink:0;"></div>'
    return f'<div style="width:{size}px; height:{size}px; border-radius:50%; background:{colour}; flex-shrink:0;"></div>'

def frame(inner_html, pt=0, pb=0):
    return f'<div style="padding:{pt}px 120px {pb}px; box-sizing:border-box;">{inner_html}</div>'

def band(inner_html, pt=68, pb=60):
    return f'<div style="background:#17130f; color:#c8c0b5; padding:{pt}px 120px {pb}px; box-sizing:border-box;">{inner_html}</div>'

def rail(label, colour, kind, body, sub=""):
    subhtml = f'<p class="lbl" style="color:#b5a08a; margin-top:10px;">{sub}</p>' if sub else ""
    return (f'<div style="display:grid; grid-template-columns:180px 1fr; gap:44px; align-items:start;">'
            f'<div><div style="display:flex; align-items:center; gap:10px;">{dot(colour,kind,10)}'
            f'<p class="lbl" style="color:{colour};">{label}</p></div>{subhtml}</div>'
            f'<div style="max-width:680px;">{body}</div></div>')

def paras(items, size=17, colour="#5c5347", mb=18):
    out=[]
    for i,p in enumerate(items):
        m = 0 if i==len(items)-1 else mb
        out.append(f'<p style="font-size:{size}px; line-height:1.8; color:{colour}; margin:0 0 {m}px;">{p}</p>')
    return "".join(out)

def defgrid(items, colour=AMBER):
    cells=[]
    for lead, body in items:
        cells.append(f'<div style="border-top:1px solid #e8e2da; padding-top:16px;">'
                     f'<p style="font-size:16px; font-weight:600; color:#1e1a16; margin:0 0 8px; line-height:1.45;">{lead}</p>'
                     f'<p style="font-size:15px; line-height:1.75; color:#6b6057; margin:0;">{body}</p></div>')
    return f'<div style="display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:34px 44px;">{"".join(cells)}</div>'

def openband(c, colour, kind, marker_dark):
    stats="".join(
        f'<div><p class="disp num" style="font-size:44px; color:#f0ebe3; margin:0 0 8px;">{v}</p>'
        f'<p style="font-size:13px; line-height:1.5; color:#9a9086; margin:0;">{l}</p></div>' for v,l in c["stats"])
    return band(
        f'<div style="display:flex; align-items:center; gap:13px; margin-bottom:20px;">{dot(marker_dark,kind,12)}'
        f'<p class="lbl" style="color:{marker_dark};">{c["num"]}</p></div>'
        f'<p class="disp" style="font-size:58px; color:#f0ebe3; max-width:900px; margin:0 0 20px;">{c["title"]}</p>'
        f'<p style="font-size:14px; color:#9a9086; margin:0 0 14px;">{c["meta"]}</p>'
        f'<p style="font-size:18px; line-height:1.7; color:#c8c0b5; max-width:720px; margin:0 0 52px;">{c["role"]}</p>'
        f'<div style="display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:34px; border-top:1px solid #332c25; padding-top:32px;">{stats}</div>',
        pt=76, pb=68)

def figure(html, pt=56, pb=0):
    return f'<div style="padding:{pt}px 120px {pb}px; box-sizing:border-box;">{html}</div>'

def sectionrule():
    return '<div style="padding:0 120px;"><div style="height:1px; background:#e8e2da;"></div></div>'

O=[]
O.append('<div style="width:1440px; box-sizing:border-box; background:#f8f6f2;">')

# header
O.append('<div style="border-bottom:1px solid #e8e2da; padding:22px 120px; display:flex; justify-content:space-between; align-items:center; background:rgba(248,246,242,0.94);">'
         '<p style="font-size:15px; font-weight:600; color:#1e1a16; margin:0; letter-spacing:0.02em;">Gideon Bullock</p>'
         '<div style="display:flex; gap:30px;">'
         '<p class="lbl" style="font-weight:500; color:#8a7d6e;">Home</p>'
         '<p class="lbl" style="font-weight:500; color:#1e1a16;">Work</p>'
         '<p class="lbl" style="font-weight:500; color:#8a7d6e;">Writing</p></div></div>')

# hero
O.append(frame(
  '<p class="lbl" style="margin-bottom:16px;">Selected Work</p>'
  '<p class="disp" style="font-size:92px; margin:0 0 30px;">Three cases</p>'
  f'<p style="font-size:20px; line-height:1.65; color:#5c5347; max-width:700px; margin:0 0 20px;">{INTRO[0]}</p>'
  f'<p style="font-size:16px; line-height:1.75; color:#7a6f63; max-width:700px; margin:0;">{INTRO[1]}</p>', pt=96, pb=0))

# gauge
cards=[]
for lbl, title, meta, note, colour, kind in GAUGE:
    cards.append(f'<div><p class="lbl" style="color:{colour}; margin-bottom:8px;">{lbl}</p>'
                 f'<p class="disp" style="font-size:29px; margin-bottom:9px;">{title}</p>'
                 f'<p style="font-size:13px; line-height:1.6; color:#8a7d6e; margin:0 0 11px;">{meta}</p>'
                 f'<p style="font-size:15px; line-height:1.7; color:#6b6057; margin:0;">{note}</p></div>')
gauge_svg=('<svg viewBox="0 0 1200 66" width="1200" height="66" style="display:block;" aria-label="Three cases placed by distance from the drawing">'
  '<line x1="0" y1="30" x2="1200" y2="30" stroke="#d8cec0" stroke-width="1.5"></line>'
  '<line x1="186" y1="30" x2="186" y2="66" stroke="#c9bfb2" stroke-width="1"></line>'
  '<line x1="600" y1="30" x2="600" y2="66" stroke="#c9bfb2" stroke-width="1"></line>'
  '<line x1="1014" y1="30" x2="1014" y2="66" stroke="#c9bfb2" stroke-width="1"></line>'
  '<circle cx="186" cy="30" r="7" fill="#b07a3c"></circle>'
  '<circle cx="600" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle>'
  '<circle cx="1014" cy="30" r="7" fill="#1e1a16"></circle>'
  '<text x="0" y="16" font-family="Inter, sans-serif" font-size="11" font-weight="600" letter-spacing="1.4" fill="#8a7d6e">THE BUSINESS BEHIND THE WORK</text>'
  '<text x="1200" y="16" text-anchor="end" font-family="Inter, sans-serif" font-size="11" font-weight="600" letter-spacing="1.4" fill="#8a7d6e">THE DRAWING ITSELF</text></svg>')
O.append(frame(gauge_svg + f'<div style="display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:42px; margin-top:6px;">{"".join(cards)}</div>'
  f'<div style="margin-top:52px; padding-top:22px; border-top:1px solid #e8e2da; display:flex; gap:14px; align-items:flex-start; max-width:840px;">'
  f'<svg width="10" height="10" viewBox="0 0 10 10" style="flex-shrink:0; margin-top:7px;"><polygon points="5,0 10,5 5,10 0,5" fill="#b5a08a"></polygon></svg>'
  f'<p class="cap" style="font-size:14px;">{CONFID}</p></div>', pt=64, pb=0))

# ---------------- CASE ONE ----------------
O.append(f'<div style="height:88px;"></div>')
O.append(openband(C1, AMBER, "fill", DA))
O.append(frame(rail("The challenge", AMBER, "fill", paras(C1["challenge"])), pt=72))
O.append(frame(rail("My role", AMBER, "fill", paras(C1["myrole"])), pt=48))
O.append(frame(rail("How the capability grew", AMBER, "fill", paras(C1["narr1"]), sub="Narrative"), pt=64))
O.append(figure(part("b_arc.part"), pt=52))
O.append(frame(rail("The turn", AMBER, "fill",
    paras(C1["narr2"]) +
    f'<p class="disp" style="font-size:34px; margin:34px 0 0; padding-left:24px; border-left:3px solid {AMBER};">{C1["pull"]}</p>'), pt=64))
O.append(f'<div style="height:64px;"></div>')
O.append(band(inner("b_gap.part"), pt=68, pb=60))
O.append(frame(rail("What it left behind", AMBER, "fill",
    paras(C1["narr3"]) +
    f'<div style="margin:26px 0; padding:20px 24px; border-left:3px solid {TEAL}; background:#f3f7f6;">'
    f'<div style="display:flex; align-items:center; gap:11px; margin-bottom:11px;">{dot(TEAL,"ring",11)}'
    f'<p class="lbl" style="color:{TEAL};">The team&rsquo;s work</p></div>'
    f'<p style="font-size:17px; line-height:1.8; color:#3d4c4b; margin:0;">{C1["credit"]}</p></div>' +
    paras(C1["narr4"])), pt=72))
O.append(figure(part("b_opmodel.part"), pt=64))
O.append(frame(rail("How it was run", AMBER, "fill", defgrid(C1["approach"])), pt=64))
O.append(frame(rail("The hardest part", AMBER, "fill", paras(C1["hard"])), pt=64))
O.append(frame(rail("What changed", AMBER, "fill", paras(C1["impact"], size=18, colour="#1e1a16")), pt=56, pb=88))

# ---------------- CASE TWO ----------------
O.append(openband(C2, TEAL, "ring", DT))
O.append(frame(rail("The challenge", AMBER, "fill", paras(C2["challenge"])), pt=72))
O.append(frame(
  f'<div style="display:grid; grid-template-columns:180px 1fr; gap:44px; align-items:start;">'
  f'<div><div style="display:flex; align-items:center; gap:10px;">{dot(TEAL,"ring",10)}'
  f'<p class="lbl" style="color:{TEAL};">Authorship</p></div></div>'
  f'<div style="max-width:820px; border-top:2px solid {TEAL}; border-bottom:1px solid #e8e2da; padding:34px 0 30px;">'
  f'<p class="disp" style="font-size:52px; margin:0 0 22px;">{C2["disclaim"]}</p>'
  f'<p style="font-size:18px; line-height:1.75; color:#5c5347; max-width:680px; margin:0;">{C2["disclaim2"]}</p></div></div>', pt=56))
O.append(frame(rail("What I did instead", AMBER, "fill", paras(C2["myrole"])), pt=48))
O.append(frame(rail("How", AMBER, "fill", defgrid(C2["approach"])), pt=56))

res="".join(f'<div style="border-top:1px solid #e8e2da; padding-top:14px;">'
            f'<p class="disp num" style="font-size:34px; margin:0 0 5px;">{v}</p>'
            f'<p style="font-size:12.5px; line-height:1.5; color:#8a7d6e; margin:0;">{l}</p></div>' for v,l in C2["research"])
O.append(figure(
  f'<div style="border:1px solid #e8e2da; background:#fdfcfa; border-radius:4px; padding:32px 34px;">'
  f'<p class="lbl" style="color:{AMBER}; margin-bottom:8px;">Case two &middot; what the research bought</p>'
  f'<p class="disp" style="font-size:28px; margin:0 0 8px;">Before a single screen was redrawn</p>'
  f'<p style="font-size:15px; line-height:1.7; color:#6b6057; max-width:760px; margin:0 0 30px;">UX research was not part of Toyota&rsquo;s playbook. I pitched its value and funded a dedicated research team inside the app organisation. This is what that bought.</p>'
  f'<div style="display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:24px;">{res}</div></div>', pt=56))

O.append(frame(
  f'<div style="border-left:3px solid {TEAL}; padding:6px 0 6px 26px; max-width:900px;">'
  f'<div style="display:flex; align-items:center; gap:11px; margin-bottom:14px;">{dot(TEAL,"ring",12)}'
  f'<p class="lbl" style="color:{TEAL};">What the team built</p></div>'
  f'<p class="disp" style="font-size:44px; margin:0 0 16px;">Everything from here to the credit line is theirs</p>'
  f'<p style="font-size:17px; line-height:1.8; color:#5c5347; max-width:680px; margin:0;">The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p></div>', pt=80))

O.append(figure(part("b_ev.part"), pt=44))
O.append(figure(
  f'<div style="display:grid; grid-template-columns:640px 1fr; gap:40px; align-items:start;">'
  f'{part("b_sus.part")}'
  f'<div style="padding-top:6px;">'
  f'<p class="lbl" style="color:{TEAL}; margin-bottom:14px;">And the rest of it</p>'
  f'{paras(C2["hard2"], size=16)}'
  f'<div style="margin-top:26px; padding-top:20px; border-top:1px solid #e8e2da; display:flex; gap:13px; align-items:flex-start;">'
  f'{dot(TEAL,"ring",11)}<p style="font-size:15px; line-height:1.7; color:{TEAL}; margin:-3px 0 0;">{C2["credit"]}</p></div>'
  f'</div></div>', pt=44))

O.append(f'<div style="height:80px;"></div>')
O.append(band(inner("b_timeline.part"), pt=68, pb=60))
O.append(figure(
  f'<div style="display:grid; grid-template-columns:640px 1fr; gap:40px; align-items:start;">'
  f'{part("b_rating.part")}'
  f'<div style="padding-top:6px;">'
  f'<p class="lbl" style="color:{AMBER}; margin-bottom:14px;">What changed</p>'
  f'{paras(C2["impact"], size=16)}'
  f'<p class="disp" style="font-size:30px; margin:28px 0 0; padding-left:22px; border-left:3px solid {AMBER};">{C2["impact2"]}</p>'
  f'</div></div>', pt=64, pb=96))

# ---------------- CASE THREE ----------------
O.append(openband(C3, INK, "fill", "#f0ebe3"))
O.append(frame(rail("The challenge", INK, "fill", paras(C3["challenge"])), pt=72))
O.append(frame(rail("My role", INK, "fill", paras(C3["myrole"])), pt=48))
O.append(figure(
  f'<div style="display:grid; grid-template-columns:640px 1fr; gap:40px; align-items:start;">'
  f'{part("b_ctx.part")}'
  f'<div style="padding-top:6px;">'
  f'<p class="lbl" style="color:{AMBER}; margin-bottom:14px;">Why it matters</p>'
  f'<p style="font-size:17px; line-height:1.8; color:#5c5347; margin:0 0 18px;">That is what designing for a probabilistic system actually involves. The interface is the easy part.</p>'
  f'<p style="font-size:17px; line-height:1.8; color:#1e1a16; margin:0; font-weight:500;">The hard part is designing for a product that behaves differently on Tuesday than it did on Monday, and building the constraints that keep it trustworthy anyway.</p>'
  f'</div></div>', pt=56))
O.append(frame(rail("What I learned building it", INK, "fill", defgrid(C3["approach"])), pt=64))
O.append(frame(rail("Where it stands", INK, "fill", paras(C3["impact"], size=18, colour="#1e1a16")), pt=56, pb=104))

# ---------------- CLOSING ----------------
O.append(band(
  f'<p class="lbl" style="color:{DA}; margin-bottom:20px;">The pattern</p>'
  f'<p style="font-size:20px; line-height:1.75; color:#c8c0b5; max-width:820px; margin:0 0 40px;">{CLOSING[0]}</p>'
  f'<p style="font-size:17px; line-height:1.75; color:#9a9086; max-width:820px; margin:0 0 26px;">{CLOSING_LEAD}</p>'
  f'<p class="disp" style="font-size:64px; color:#f0ebe3; max-width:1000px; margin:0;">{CLOSING_BIG}</p>', pt=88, pb=88))

O.append(frame(
  f'<p class="lbl" style="margin-bottom:16px;">Contact</p>'
  f'<p style="font-size:21px; line-height:1.7; color:#1e1a16; font-weight:500; max-width:720px; margin:0 0 18px;">{CONTACT[0]}</p>'
  f'<p style="font-size:17px; line-height:1.8; color:#5c5347; max-width:720px; margin:0;">{CONTACT[1]}</p>', pt=88, pb=72))

O.append('<div style="padding:26px 120px 48px; border-top:1px solid #e8e2da; display:flex; justify-content:space-between; align-items:center;">'
         '<p style="font-size:13px; color:#b5a08a; margin:0;">&copy; 2026 Gideon Bullock</p>'
         '<p style="font-size:13px; color:#b5a08a; margin:0;">gideonb.me</p></div>')

O.append('</div>')
open("b_main.part","w").write("\n".join(O))
print("built")
