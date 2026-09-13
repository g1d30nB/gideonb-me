# Mobile-only versions of the three figures whose desktop layout cannot collapse by CSS alone.
import diagrams as D
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"; AD="var(--amber-d)"; TD="var(--teal-d)"

def head(label,colour,kind):
    return (f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {colour};margin-bottom:var(--s3);">'
            f'{D.dot(colour,kind,9)}<p class="lbl" style="color:{colour};font-size:10.5px;">{label}</p></div>')
def fig(kick,colour,kind,title,sub,body,foot=""):
    f=f'<p style="font-size:13px;line-height:1.65;color:var(--ink);margin:var(--s4) 0 0;padding-top:var(--s3);border-top:1px solid var(--rule);font-weight:500;">{foot}</p>' if foot else ""
    return f'<div>{head(kick,colour,kind)}<p class="d3" style="margin-bottom:var(--s2);">{title}</p><p style="font-size:14px;line-height:1.65;color:var(--muted);margin:0 0 var(--s5);">{sub}</p>{body}{f}</div>'

def arc_m():
    rows=[]
    for i,(k,n,why,earn,_,_,_) in enumerate(D.ARC_STEPS):
        last=i==4; w=[20,38,56,76,100][i]
        if last: rows.append('<div style="display:flex;align-items:center;gap:10px;margin:var(--s5) 0;"><div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div><p class="lbl" style="color:var(--amber);font-size:9.5px;white-space:nowrap;">The question changed</p><div style="flex-grow:1;height:1px;background:repeating-linear-gradient(to right,oklch(0.575 0.075 62) 0 5px,transparent 5px 11px);"></div></div>')
        rows.append(f'<div class="arc-card" style="--i:{i};border-top:{"3px solid var(--amber)" if last else "2px solid var(--rule-2)"};padding-top:var(--s3);margin-bottom:var(--s5);"><p class="lbl" style="color:{A if last else "var(--faint)"};font-size:10px;margin-bottom:7px;">{k}</p><p class="d4" style="font-size:20px;margin-bottom:var(--s2);">{n}</p>'
          f'<p style="font-size:13.5px;line-height:1.6;color:var(--body);margin:0 0 10px;">{why}</p><div class="arc-bar" style="height:9px;background:oklch(0.93 0.030 68);width:{w}%;margin-bottom:7px;transform-origin:left;"></div><p style="font-size:12px;line-height:1.5;color:var(--muted);margin:0;"><span style="color:{A};font-weight:600;">Earned &rarr;</span> {earn}</p></div>')
    return '<div class="wk-arc wk-anim">'+fig("Case one &middot; the sequence",A,"fill","How the capability grew","Five capabilities in the order they were established. The bar under each is how much of the customer&rsquo;s experience design was allowed to own, from one screen to connected vehicle apps, in-vehicle multimedia and EV.","".join(rows),foot="Each capability earned the next. By the end the team sat inside quarterly planning, and its research and service design shaped where the business went next.")+'</div>'

def gap_m():
    sl=[]
    for i,(n,o,mine) in enumerate(D.SLICES):
        if i>0: sl.append('<div style="display:flex;align-items:center;gap:9px;padding:7px 0 7px 5px;"><span style="width:10px;height:10px;border:1.5px dashed oklch(0.50 0.035 70);border-radius:50%;"></span><p style="font-size:11.5px;color:oklch(0.60 0.040 70);margin:0;">no owner</p></div>')
        sl.append(f'<div style="border:{"1.5px solid var(--amber-d)" if mine else "1px solid var(--night-rule)"};background:{"var(--night-2)" if mine else "transparent"};border-radius:3px;padding:var(--s3) 13px;"><p style="font-size:13.5px;font-weight:600;color:{"var(--night-ink)" if mine else "var(--night-body)"};margin:0 0 4px;">{n}</p><p style="font-size:11.5px;color:{AD if mine else "var(--night-muted)"};margin:0;">{o}</p></div>')
    after="".join(f'<div style="border:1px solid oklch(0.33 0.020 190);border-radius:3px;padding:9px 12px;margin-bottom:7px;"><p style="font-size:12.5px;color:var(--night-body);margin:0;">{n}</p></div>' for n,_,_ in D.SLICES)
    return (f'<div style="display:flex;align-items:center;gap:9px;padding-top:var(--s3);border-top:2px solid {AD};margin-bottom:var(--s3);">{D.dot(AD,"fill",9)}<p class="lbl" style="color:{AD};font-size:10.5px;">Case one &middot; what service design was for</p></div>'
     '<p class="d3" style="color:var(--night-ink);margin-bottom:var(--s3);">A disjointed experience is a faithful picture of a disjointed business</p><p style="font-size:14px;line-height:1.75;color:var(--night-muted);margin:0 0 var(--s6);">No Toyota blueprint is shown. This is the shape of the problem.</p>'
     '<p class="lbl" style="color:var(--night-muted);font-size:10px;margin-bottom:var(--s3);">Before &middot; one slice, the rest owned elsewhere</p>'+"".join(sl)+
     f'<p class="lbl" style="color:{TD};font-size:10px;margin:var(--s6) 0 var(--s3);">After &middot; one journey, owned together</p><div style="border:1.5px solid {TD};background:oklch(0.225 0.022 190);border-radius:3px;padding:13px;margin-bottom:10px;"><p style="font-size:13.5px;font-weight:600;color:var(--night-ink);margin:0 0 4px;">One end-to-end journey</p><p style="font-size:11.5px;color:{TD};margin:0;">Blueprinted front stage and back, reusable as service patterns</p></div>'+after+
     '<p style="font-size:15.5px;line-height:1.75;color:var(--night-ink);margin:var(--s5) 0 var(--s5);font-weight:500;">Business units that had never designed anything together started working on the same journey. They are still doing it, which is the part I am most confident about, because it outlasted me.</p>'
     f'<div style="border-top:1px solid var(--night-rule);padding-top:var(--s4);display:flex;gap:11px;align-items:flex-start;">{D.dot(TD,"ring",10)}<p style="font-size:14px;line-height:1.7;color:{TD};margin:-4px 0 0;">The blueprints, the reusable service patterns and the playbooks were built by the service designers who were hired to make them. What I did was make the case for it and hire into it.</p></div>')

def ev_m():
    bl="".join(f'<div style="display:grid;grid-template-columns:20px 1fr;gap:11px;align-items:center;margin-bottom:9px;"><p style="font-size:11px;color:var(--faint);margin:0;">0{i+1}</p><div style="border:1px solid var(--rule-2);border-radius:6px;background:var(--paper);padding:11px 13px;"><p style="font-size:13px;color:var(--body);margin:0;">{t}</p></div></div>' for i,t in enumerate(D.EV_BEFORE))
    aft="".join(f'<div style="border:1px solid oklch(0.86 0.022 195);border-radius:5px;background:oklch(0.995 0.002 195);padding:9px 11px;"><p style="font-size:12.5px;color:oklch(0.42 0.020 195);margin:0;">{t}</p></div>' for t in D.EV_AFTER)
    return fig("Case two &middot; what the team built",T,"ring","One EV domain in place of four","For an EV driver the questions are constant. Am I charged, can I leave, when will it be ready. The answers were scattered across the app.",
      f'<p class="lbl" style="font-size:10px;margin-bottom:var(--s3);">Before &middot; four places, one job</p>{bl}<div style="display:flex;justify-content:center;padding:var(--s4) 0;"><div style="width:1px;height:26px;background:{T};"></div></div><p class="lbl" style="color:{T};font-size:10px;margin-bottom:var(--s3);">After &middot; one place, at the point of use</p><div style="border:1.5px solid {T};border-radius:8px;background:oklch(0.985 0.008 195);padding:14px;"><p style="font-size:13px;font-weight:600;color:var(--ink);margin:0 0 10px;">EV domain</p><div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;">{aft}</div><p style="font-size:11.5px;line-height:1.5;color:{T};margin:12px 0 0;">Real-time status, mirroring what is happening at the car.</p></div>',
      foot="My call was that EV had to be solved as one experience rather than patched feature by feature.")
