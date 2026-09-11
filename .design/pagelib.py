from copy import *   # noqa
import diagrams as D
# ---------- page helpers ----------
def F(h,pt=0,pb=0,pad=120): return f'<div style="padding:{pt}px {pad}px {pb}px;box-sizing:border-box;">{h}</div>'
def BAND(h,pt=72,pb=64):
    return f'<div style="background:var(--night);color:var(--night-body);padding:{pt}px 120px {pb}px;box-sizing:border-box;">{h}</div>'
def TEAM(h,pt=72,pb=72):
    return f'<div style="background:var(--paper-team);padding:{pt}px 120px {pb}px;box-sizing:border-box;">{h}</div>'

def rail(label,colour,kind,body,sub=""):
    s=f'<p class="lbl" style="color:var(--faint);margin-top:10px;">{sub}</p>' if sub else ""
    return (f'<div style="display:grid;grid-template-columns:180px 1fr;gap:44px;align-items:start;">'
            f'<div><div style="display:flex;align-items:center;gap:10px;">{D.dot(colour,kind,10)}'
            f'<p class="lbl" style="color:{colour};">{label}</p></div>{s}</div>'
            f'<div style="max-width:680px;">{body}</div></div>')

def P(items,size=17,colour="var(--body)",mb=18,lh=1.75):
    return "".join(f'<p style="font-size:{size}px;line-height:{lh};color:{colour};margin:0 0 {0 if i==len(items)-1 else mb}px;">{p}</p>'
                   for i,p in enumerate(items))

def quote(text,colour="var(--amber)",size="d3"):
    return (f'<div style="margin:var(--s6) 0 0;">'
            f'<div style="width:48px;height:3px;background:{colour};margin-bottom:var(--s4);"></div>'
            f'<p class="{size}" style="max-width:660px;">{text}</p></div>')

def defgrid(items):
    cells="".join(f'<div style="border-top:1px solid var(--rule);padding-top:var(--s4);">'
                  f'<p class="d4" style="margin-bottom:var(--s2);">{a}</p>'
                  f'<p style="font-size:15.5px;line-height:1.75;color:var(--body);margin:0;">{b}</p></div>' for a,b in items)
    return f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:34px 44px;">{cells}</div>'

def statline(stats, dark=True):
    ink   = "var(--night-ink)" if dark else "var(--ink)"
    lab   = "var(--night-muted)" if dark else "var(--muted)"
    rule  = "var(--night-rule)" if dark else "var(--rule)"
    out=[]
    for i,(v,l) in enumerate(stats):
        out.append(f'<div style="padding:0 var(--s6) 0 {"var(--s6)" if i else "0"};'
                   f'{"border-left:1px solid "+rule+";" if i else ""}">'
                   f'<p class="stat" style="color:{ink};font-size:40px;margin-bottom:10px;">{v}</p>'
                   f'<p style="font-size:13px;line-height:1.5;color:{lab};margin:0;max-width:200px;">{l}</p></div>')
    return (f'<div style="display:flex;align-items:flex-start;flex-wrap:wrap;row-gap:var(--s6);'
            f'border-top:1px solid {rule};padding-top:var(--s6);">{"".join(out)}</div>')

def openband(c,dcol,kind):
    return BAND(f'<div style="display:flex;align-items:center;gap:13px;margin-bottom:var(--s5);">{D.dot(dcol,kind,12)}'
        f'<p class="lbl" style="color:{dcol};">{c["num"]}</p></div>'
        f'<p class="d2" style="color:var(--night-ink);max-width:1000px;margin-bottom:var(--s5);">{c["title"]}</p>'
        f'<p style="font-size:14px;color:var(--night-muted);margin:0 0 14px;">{c["meta"]}</p>'
        f'<p style="font-size:18px;line-height:1.8;color:var(--night-body);max-width:760px;margin:0 0 var(--s8);">{c["role"]}</p>'
        f'{statline(c["stats"])}', pt=84, pb=76)


HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
def write(n,b): open(n,"w").write(HEAD+b+"\n"+TAIL)
def page(parts): return '<div style="width:1440px;box-sizing:border-box;background:var(--paper);">'+"\n".join(parts)+'</div>'
