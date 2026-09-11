import workmd as W
import diagrams as D
import components as C
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"; AD="var(--amber-d)"; TD="var(--teal-d)"
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
def write(n,b): open(n,"w").write(HEAD+b+"\n"+TAIL)
def P(items,size=16.5,colour="var(--body)",mb=16,lh=1.75):
    return "".join(f'<p style="font-size:{size}px;line-height:{lh};color:{colour};margin:0 0 {0 if i==len(items)-1 else mb}px;">{p}</p>' for i,p in enumerate(items))
def strip(text, right):
    return (f'<div style="background:var(--paper-2);padding:9px 40px;display:flex;justify-content:space-between;align-items:baseline;">'
            f'<p class="lbl" style="color:{A};">{text}</p><p class="lbl">{right}</p></div>')
def header(pad):
    return (f'<div style="border-bottom:1px solid var(--rule);padding:20px {pad}px;display:flex;justify-content:space-between;align-items:center;">'
            f'<p style="font-size:15px;font-weight:600;color:var(--ink);margin:0;">Gideon Bullock</p>'
            f'<div style="display:flex;gap:28px;"><p class="lbl" style="font-weight:500;">Home</p><p class="lbl" style="font-weight:500;color:var(--ink);">Work</p><p class="lbl" style="font-weight:500;">Writing</p></div></div>')
def argue(what, cost, pad):
    return (f'<div style="margin:64px {pad}px 0;padding-top:var(--s5);border-top:1px solid var(--rule);display:grid;grid-template-columns:1fr 1fr;gap:40px;">'
            f'<div><p class="lbl" style="margin-bottom:var(--s2);">What this direction argues</p><p style="font-size:14px;line-height:1.7;color:var(--body);margin:0;">{what}</p></div>'
            f'<div><p class="lbl" style="margin-bottom:var(--s2);">What it costs</p><p style="font-size:14px;line-height:1.7;color:var(--body);margin:0;">{cost}</p></div></div>')

PHONES=[("mytoyota-01-home.jpg","MyToyota, home","Public App Store listing"),
        ("lexus-01-dashboard.jpg","Lexus Link+, home","Public App Store listing"),
        ("mytoyota-03-car-status.jpg","MyToyota, vehicle status","Public App Store listing")]
c1,c2,c3=W.C1,W.C2,W.C3

# ============================================================ D · the document, with evidence
M=130  # margins give a 740 measure inside 1000
def dplate(src,what,prov): return C.plate(src,what,prov)
d=[f'<div style="width:1000px;box-sizing:border-box;background:var(--paper);padding-bottom:56px;">',
   strip("Direction D","The document, with evidence &nbsp;&middot;&nbsp; one measure, plates inline"),
   header(M),
   f'<div style="padding:72px {M}px 0;"><p class="lbl" style="margin-bottom:var(--s4);">Selected Work</p>'
   f'<p class="d1" style="font-size:56px;margin-bottom:var(--s5);">Three cases</p>{P(W.INTRO[:2],size=17)}</div>',
   # case three, the centrepiece, inline
   f'<div style="padding:72px {M}px 0;"><div style="height:1px;background:var(--rule);margin-bottom:56px;"></div>'
   f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s3);">{D.dot(INK,"fill",10)}<p class="lbl" style="color:var(--ink);">{c3["info"]["number"]} &middot; the craft</p></div>'
   f'<p class="d2" style="font-size:36px;margin-bottom:var(--s3);">{c3["info"]["title"]}</p>'
   f'<p style="font-size:14px;color:var(--muted);margin:0 0 var(--s5);">{c3["info"]["company"]} &nbsp;&middot;&nbsp; {c3["info"]["dates"]}</p>'
   f'{P(c3["narrative"][:1])}'
   f'<div style="margin:40px 0 12px;">{dplate("emotrix-timeline.jpg","Emotrix session review. Five constructs against the participant&rsquo;s own baseline; two interpreted lines above; hatched where no reading is asserted.","Real interface, synthetic session")}</div>'
   f'<div style="margin:32px 0 0;">{dplate("prepcall-report-listening.jpg","PrepCall coaching report, the listening half. What was said, then how it sounded.","Illustrative report; real frame to follow")}</div>'
   f'<p style="font-size:16.5px;line-height:1.75;color:var(--ink);font-weight:500;margin:36px 0 0;">Signal above, meaning below. The design work is the layer between them, and it is the same layer in both products.</p></div>',
   # case one leadership, inline
   f'<div style="padding:72px {M}px 0;"><div style="height:1px;background:var(--rule);margin-bottom:56px;"></div>'
   f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s3);">{D.dot(A,"fill",10)}<p class="lbl" style="color:{A};">{c1["info"]["leading-label"]}</p></div>'
   f'{P(W.paras(W.SEC["case1-leading"])[:1])}'
   f'<div style="margin-top:40px;">{C.ownership()}</div>'
   f'<div style="display:flex;align-items:center;gap:10px;margin:64px 0 var(--s3);">{D.dot(A,"fill",10)}<p class="lbl" style="color:{A};">{c1["info"]["people-label"]}</p></div>'
   f'{P(W.paras(W.SEC["case1-people"])[:1])}'
   f'<div style="margin-top:40px;">{C.people()}</div></div>',
   # case two frames inline
   f'<div style="padding:72px {M}px 0;"><div style="height:1px;background:var(--rule);margin-bottom:56px;"></div>'
   f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:var(--s3);">{D.dot(T,"ring",10)}<p class="lbl" style="color:{T};">{c2["info"]["aside-label"]}</p></div>'
   f'<p class="d3" style="margin-bottom:var(--s5);">The app as it stands in public</p>{C.phone_row(PHONES)}</div>',
   argue("That the site&rsquo;s quietness is the position, and that evidence can be added without changing the register. One measure, plates set inline like figures in a monograph, captions doing the attribution. Continuous with the homepage to the pixel.",
         "At this length it still reads at one pitch: no landmarks, so the ninety-second scroll sees a long article with pictures. The centrepiece pairing stacks vertically and loses the side-by-side argument. Phones at 220px wide are illustrations rather than evidence.", M),
   '</div>']
write("DirectionD.dc.html","\n".join(d))

# ============================================================ E · the exhibition
PAD=72
def rail(label,colour,kind,body):
    return (f'<div style="display:grid;grid-template-columns:150px 1fr;gap:36px;align-items:start;">'
            f'<div style="display:flex;align-items:center;gap:10px;">{D.dot(colour,kind,10)}<p class="lbl" style="color:{colour};">{label}</p></div>'
            f'<div style="max-width:640px;">{body}</div></div>')
stats3="".join(f'<div style="padding:0 var(--s5) 0 {"var(--s5)" if i else "0"};{"border-left:1px solid var(--night-rule);" if i else ""}">'
   f'<p class="stat" style="color:var(--night-ink);font-size:30px;margin-bottom:8px;">{v}</p><p style="font-size:12.5px;line-height:1.5;color:var(--night-muted);margin:0;max-width:150px;">{l}</p></div>'
   for i,(v,l) in enumerate(c3["stats"]))
phones_e="".join(f'<div style="margin-top:{[0,40,16,56][i]}px;">{C.plate(s,w,p,aspect="9 / 16",fit="cover",pos="top")}</div>'
                 for i,(s,w,p) in enumerate(PHONES+[("lexus-03-vehicle-status.jpg","Lexus Link+, vehicle status","Public App Store listing")]))
e=[f'<div style="width:1000px;box-sizing:border-box;background:var(--paper);padding-bottom:56px;">',
   strip("Direction E &nbsp;&middot;&nbsp; recommended","The exhibition &nbsp;&middot;&nbsp; imagery leads, diagrams annotate"),
   header(PAD),
   f'<div style="padding:72px {PAD}px 0;"><p class="lbl" style="margin-bottom:var(--s4);">Selected Work</p>'
   f'<p class="d1" style="margin-bottom:var(--s6);">Three cases</p>'
   f'<p style="font-size:19px;line-height:1.65;color:var(--body);max-width:640px;margin:0 0 var(--s5);">{W.INTRO[0]}</p>'
   f'<p style="font-size:15px;line-height:1.8;color:var(--muted);max-width:640px;margin:0;">{W.INTRO[1]}</p></div>',
   # case three opener band with the pairing
   f'<div style="background:var(--night);color:var(--night-body);padding:56px {PAD}px 52px;margin-top:64px;">'
   f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:var(--s4);">{D.dot("var(--night-ink)","fill",11)}<p class="lbl" style="color:var(--night-ink);">{c3["info"]["number"]} &middot; the craft</p></div>'
   f'<p class="d2" style="color:var(--night-ink);max-width:760px;margin-bottom:var(--s4);">{c3["info"]["title"]}</p>'
   f'<p style="font-size:13.5px;color:var(--night-muted);margin:0 0 12px;">{c3["info"]["company"]} &nbsp;&middot;&nbsp; {c3["info"]["dates"]}</p>'
   f'<p style="font-size:16.5px;line-height:1.8;color:var(--night-body);max-width:640px;margin:0 0 var(--s7);">{c3["info"]["role"]}</p>'
   f'{C.pairing("emotrix-timeline.jpg","prepcall-report-listening.jpg")}'
   f'<div style="display:flex;flex-wrap:wrap;row-gap:var(--s5);border-top:1px solid var(--night-rule);padding-top:var(--s5);margin-top:var(--s7);">{stats3}</div></div>',
   # case one: leadership as a wide figure, people as a wide figure
   f'<div style="padding:64px {PAD}px 0;">{rail(c1["info"]["leading-label"],A,"fill",P(W.paras(W.SEC["case1-leading"]),size=16))}</div>'
   f'<div style="padding:40px {PAD}px 0;">{C.ownership()}</div>'
   f'<div style="padding:64px {PAD}px 0;">{rail(c1["info"]["people-label"],A,"fill",P(W.paras(W.SEC["case1-people"])[:1],size=16))}</div>'
   f'<div style="padding:40px {PAD}px 0;">{C.people()}</div>',
   # case two: team ground with phones stepping across
   f'<div style="background:var(--paper-team);padding:56px {PAD}px 56px;margin-top:72px;">'
   f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:var(--s3);">{D.dot(T,"ring",11)}<p class="lbl" style="color:{T};">{c2["info"]["aside-label"]}</p></div>'
   f'<p class="d2" style="font-size:34px;max-width:700px;margin-bottom:var(--s3);">Everything on this ground is theirs</p>'
   f'<p style="font-size:15.5px;line-height:1.75;color:oklch(0.40 0.020 195);max-width:600px;margin:0 0 var(--s7);">The EV domain, the home screen redesign and the design system are the team&rsquo;s work, and are presented as such.</p>'
   f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--s5);align-items:start;">{phones_e}</div></div>',
   argue("That a design leader&rsquo;s portfolio should be an exhibition of evidence. The imagery leads each section and the diagrams annotate it. Six landmarks (three dark openers, the pairing, the timeline, the close) so the ninety-second scroll gets the argument from the pictures and numbers alone. Case three carries the most weight because it is where the hands are on the work.",
         "More to build: an image pipeline, frames at two densities, and captions that have to stay true. The dark bands make /work visibly different from the homepage until the homepage follows. And it asks more of the copy: every frame needs a caption that says whose work it is.", PAD),
   '</div>']
write("DirectionE.dc.html","\n".join(e))
print("directions written")
