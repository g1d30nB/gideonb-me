from copy import *   # noqa
import diagrams as D
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
def write(n,b): open(n,"w").write(HEAD+b+"\n"+TAIL)
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"

gauge=('<svg viewBox="0 0 800 62" width="100%" height="62" preserveAspectRatio="none" style="display:block;" aria-label="Three cases placed by distance from the drawing">'
 '<line x1="0" y1="30" x2="800" y2="30" stroke="#d5cabb" stroke-width="1.5"></line>'
 '<line x1="124" y1="30" x2="124" y2="62" stroke="#c5b9a8"></line><line x1="400" y1="30" x2="400" y2="62" stroke="#c5b9a8"></line>'
 '<line x1="676" y1="30" x2="676" y2="62" stroke="#c5b9a8"></line>'
 '<circle cx="124" cy="30" r="7" fill="#9a6a34"></circle>'
 '<circle cx="400" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle>'
 '<circle cx="676" cy="30" r="7" fill="#1e1a16"></circle>'
 '<text x="0" y="16" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE BUSINESS BEHIND THE WORK</text>'
 '<text x="800" y="16" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE DRAWING ITSELF</text></svg>')
gcards="".join(f'<div><p class="lbl" style="color:{c};margin-bottom:var(--s2);">{lb}</p>'
  f'<p class="d4" style="font-size:22px;margin-bottom:var(--s2);">{t}</p>'
  f'<p style="font-size:13px;line-height:1.6;color:var(--muted);margin:0;">{n}</p></div>'
  for lb,t,n,c in [(a,b,d,{"#b07a3c":A,"#3f7d7a":T,"#1e1a16":INK}[e]) for a,b,_,d,e,_ in GAUGE])

stats="".join(f'<div style="padding:0 var(--s5) 0 {"var(--s5)" if i else "0"};{"border-left:1px solid var(--night-rule);" if i else ""}">'
  f'<p class="stat" style="color:var(--night-ink);font-size:32px;margin-bottom:8px;">{v}</p>'
  f'<p style="font-size:12.5px;line-height:1.5;color:var(--night-muted);margin:0;max-width:150px;">{l}</p></div>'
  for i,(v,l) in enumerate(C1["stats"]))

c=(f'<div style="width:1000px;box-sizing:border-box;background:var(--paper);padding-bottom:var(--s7);">'
 f'<div style="background:var(--paper-2);padding:10px 40px;display:flex;justify-content:space-between;align-items:baseline;">'
 f'<p class="lbl" style="color:{A};">Direction C &nbsp;&middot;&nbsp; the revision</p>'
 f'<p class="lbl">One grotesque, no serif, dark bands kept</p></div>'

 f'<div style="border-bottom:1px solid var(--rule);padding:20px 100px;display:flex;justify-content:space-between;align-items:center;">'
 f'<p style="font-size:15px;font-weight:600;color:var(--ink);margin:0;">Gideon Bullock</p>'
 f'<div style="display:flex;gap:28px;"><p class="lbl" style="font-weight:500;">Home</p>'
 f'<p class="lbl" style="font-weight:500;color:var(--ink);">Work</p><p class="lbl" style="font-weight:500;">Writing</p></div></div>'

 f'<div style="padding:72px 100px 0;">'
 f'<p class="lbl" style="margin-bottom:var(--s4);">Selected Work</p>'
 f'<p class="d1" style="margin-bottom:var(--s6);">Three cases</p>'
 f'<p style="font-size:19px;line-height:1.65;color:var(--body);max-width:620px;margin:0 0 var(--s5);">{INTRO[0]}</p>'
 f'<p style="font-size:15.5px;line-height:1.8;color:var(--muted);max-width:620px;margin:0 0 var(--s7);">{INTRO[1]}</p></div>'

 f'<div style="padding:0 100px;">{gauge}'
 f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:36px;margin-top:var(--s1);">{gcards}</div></div>'

 f'<div style="background:var(--night);color:var(--night-body);padding:56px 100px 48px;margin-top:var(--s8);">'
 f'<div style="display:flex;align-items:center;gap:13px;margin-bottom:var(--s4);">{D.dot("var(--amber-d)","fill",12)}'
 f'<p class="lbl" style="color:var(--amber-d);">{C1["num"]}</p></div>'
 f'<p class="d2" style="color:var(--night-ink);max-width:740px;margin-bottom:var(--s4);">{C1["title"]}</p>'
 f'<p style="font-size:13.5px;color:var(--night-muted);margin:0 0 12px;">{C1["meta"]}</p>'
 f'<p style="font-size:17px;line-height:1.8;color:var(--night-body);max-width:640px;margin:0 0 var(--s7);">{C1["role"]}</p>'
 f'<div style="display:flex;align-items:flex-start;flex-wrap:wrap;row-gap:var(--s5);border-top:1px solid var(--night-rule);padding-top:var(--s5);">{stats}</div></div>'

 f'<div style="padding:56px 100px 0;display:grid;grid-template-columns:150px 1fr;gap:40px;align-items:start;">'
 f'<div><div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s2);">{D.dot(A,"fill",10)}'
 f'<p class="lbl" style="color:{A};">My call</p></div><p class="lbl" style="color:var(--faint);">The challenge</p></div>'
 f'<div style="max-width:600px;">'
 f'<p style="font-size:17px;line-height:1.8;color:var(--body);margin:0 0 18px;">{C1["challenge"][0]}</p>'
 f'<p class="d4" style="margin:0;">{C1["challenge"][1]}</p></div></div>'

 f'<div style="padding:56px 40px 0;">{D.arc()}</div>'

 f'<div style="margin:56px 100px 0;padding-top:var(--s5);border-top:1px solid var(--rule);display:grid;grid-template-columns:1fr 1fr;gap:40px;">'
 f'<div><p class="lbl" style="margin-bottom:var(--s2);">What changed from B</p>'
 f'<p style="font-size:14px;line-height:1.7;color:var(--body);margin:0;">The serif is gone. One family now does the whole site: Schibsted Grotesk, a Norwegian newspaper face '
 f'that carries a headline at 800 and disappears at 400. The dark bands stay, because they are what makes a three-case page scannable. '
 f'The side-stripe accents are gone too: authorship is carried by the ground a section sits on, a top rule, and a marker whose form differs, not by a coloured bar down the left edge.</p></div>'
 f'<div><p class="lbl" style="margin-bottom:var(--s2);">What it still costs</p>'
 f'<p style="font-size:14px;line-height:1.7;color:var(--body);margin:0;">A webfont swap across the site, and an eye over the ten articles to check nothing reflows badly. '
 f'The dark bands make /work look different from the homepage until the homepage catches up. '
 f'And the teal is still the only cool colour on a warm site, which is the point, and also the risk.</p></div></div></div>')
write("DirectionC.dc.html", c)
print("direction C ok")
