from copy import *      # noqa
import diagrams as D
HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
def write(n,b): open(n,"w").write(HEAD+b+"\n"+TAIL)
A="var(--amber)"; T="var(--teal)"; INK="var(--ink)"

# ============================================================ AUTHORSHIP
def labelrow(text,colour,kind):
    return (f'<div style="display:flex;align-items:center;gap:11px;margin-bottom:var(--s3);">{D.dot(colour,kind,11)}'
            f'<p class="lbl" style="color:{colour};">{text}</p></div>')

gauge=('<svg viewBox="0 0 1120 66" width="100%" height="66" preserveAspectRatio="none" style="display:block;margin-top:26px;" aria-label="Three cases placed by distance from the drawing">'
 '<line x1="0" y1="30" x2="1120" y2="30" stroke="#d5cabb" stroke-width="1.5"></line>'
 '<line x1="173" y1="30" x2="173" y2="66" stroke="#c5b9a8"></line><line x1="560" y1="30" x2="560" y2="66" stroke="#c5b9a8"></line>'
 '<line x1="947" y1="30" x2="947" y2="66" stroke="#c5b9a8"></line>'
 '<circle cx="173" cy="30" r="7" fill="#9a6a34"></circle>'
 '<circle cx="560" cy="30" r="7" fill="none" stroke="#3f7d7a" stroke-width="2.5"></circle>'
 '<circle cx="947" cy="30" r="7" fill="#1e1a16"></circle>'
 '<text x="0" y="16" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE BUSINESS BEHIND THE WORK</text>'
 '<text x="1120" y="16" text-anchor="end" font-family="Schibsted Grotesk,Helvetica,sans-serif" font-size="11" font-weight="700" letter-spacing="1.4" fill="#8a7d6e">THE DRAWING ITSELF</text></svg>')
gcards="".join(f'<div><p class="lbl" style="color:{c};margin-bottom:var(--s2);">{lb}</p>'
  f'<p class="d4" style="font-size:25px;margin-bottom:var(--s2);">{t}</p>'
  f'<p style="font-size:13px;line-height:1.6;color:var(--muted);margin:0 0 10px;">{m}</p>'
  f'<p style="font-size:15px;line-height:1.7;color:var(--body);margin:0;">{n}</p></div>'
  for lb,t,m,n,c in [(a,b,cc,d,{"#b07a3c":A,"#3f7d7a":T,"#1e1a16":INK}[e]) for a,b,cc,d,e,_ in GAUGE])

auth=(f'<div style="width:1200px;box-sizing:border-box;padding:var(--s7);background:var(--paper);">'
 f'<p class="lbl" style="color:{A};margin-bottom:var(--s2);">The device</p>'
 f'<p class="d2" style="margin-bottom:var(--s3);max-width:940px;">Carrying authorship without a paragraph of explanation</p>'
 f'<p style="font-size:16px;line-height:1.75;color:var(--body);max-width:840px;margin:0 0 var(--s7);">'
 f'Three carriers, in order of how far they can be read from. The ground a section sits on. The marker and label at the top of each block. '
 f'And the words themselves, which never leave the job to the other two.</p>'

 f'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);">One &nbsp;&middot;&nbsp; the distance gauge, once, at the top of the page</p>'
 f'{gauge}<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:42px;margin-bottom:var(--s8);">{gcards}</div>'

 f'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s6);">Two &nbsp;&middot;&nbsp; the ground, for a section at a time</p>'
 f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s7);margin-bottom:var(--s8);">'
 f'<div style="background:var(--paper);border:1px solid var(--rule);padding:var(--s6);">'
 f'{labelrow("My call","var(--amber)","fill")}'
 f'<p style="font-size:15.5px;line-height:1.75;margin:0;">Warm paper, the site&rsquo;s own ground. The decision was mine and the accountability sits with me. '
 f'The whole of case one, the whole of case three, and the framing, funding and gatekeeping in case two.</p></div>'
 f'<div style="background:var(--paper-team);padding:var(--s6);">'
 f'{labelrow("The team&rsquo;s work","var(--teal)","ring")}'
 f'<p style="font-size:15.5px;line-height:1.75;color:oklch(0.40 0.020 195);margin:0;">The ground turns very slightly cool and stays that way until the credit line. '
 f'Case two&rsquo;s craft section runs on it end to end. You know whose work you are looking at before you read a word.</p></div></div>'

 f'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s6);">Three &nbsp;&middot;&nbsp; the marker, on every block</p>'
 f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s7);margin-bottom:var(--s8);">'
 f'<div style="border-top:2px solid var(--amber);padding-top:var(--s4);">{labelrow("My call","var(--amber)","fill")}'
 f'<p style="font-size:15px;line-height:1.75;margin:0;">Filled disc, amber rule. Solid ink weight in the copy.</p></div>'
 f'<div style="border-top:2px solid var(--teal);padding-top:var(--s4);">{labelrow("The team&rsquo;s work","var(--teal)","ring")}'
 f'<p style="font-size:15px;line-height:1.75;margin:0;">Hollow ring, teal rule. The ring is the point: the form differs, so this survives greyscale and colour blindness.</p></div>'
 f'<div style="border-top:2px solid var(--ink);padding-top:var(--s4);">{labelrow("Solo","var(--ink)","fill")}'
 f'<p style="font-size:15px;line-height:1.75;margin:0;">Ink rule, no accent. Case three only, where there was nobody else in the room.</p></div></div>'

 f'<p class="lbl" style="padding-bottom:var(--s3);border-bottom:1px solid var(--rule-2);margin-bottom:var(--s6);">Four &nbsp;&middot;&nbsp; how it reads in the page</p>'
 f'<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--s7);align-items:start;">'
 f'<div style="border-top:2px solid var(--amber);padding-top:var(--s4);">{labelrow("My call &nbsp;&middot;&nbsp; case two","var(--amber)","fill")}'
 f'<p style="font-size:16.5px;line-height:1.8;margin:0;">The work did not ship until task performance hit target, and getting there took four rounds of moderated usability testing. '
 f'Backing that, against a delivery schedule, is most of what a design leader is actually for.</p></div>'
 f'<div style="background:var(--paper-team);padding:var(--s5) var(--s5) var(--s5);margin:-1px -1px 0;">'
 f'{labelrow("What the team built &nbsp;&middot;&nbsp; case two","var(--teal)","ring")}'
 f'<p style="font-size:16.5px;line-height:1.8;color:oklch(0.40 0.020 195);margin:0;">The team built one EV domain in place of four scattered locations: a single place for charging status and scheduling, '
 f'real-time updates, and a live session view mirroring what was happening at the car.</p></div></div>'

 f'<p class="t3" style="margin-top:var(--s7);padding-top:var(--s5);border-top:1px solid var(--rule);max-width:860px;">'
 f'Block labels are set from each case&rsquo;s <span style="color:var(--ink);">-meta</span> block in work.md, so a new named section needs no template change. '
 f'Case one uses &ldquo;How the capability grew&rdquo;, case two uses &ldquo;What the team built&rdquo;.</p></div>')
write("Authorship.dc.html", auth)

# ============================================================ CASE ANATOMY
def slot(key,label,note,colour,locked=False,diagram=False):
    lock=('<div style="display:flex;align-items:center;gap:7px;margin-top:10px;">'
          '<svg width="9" height="9" viewBox="0 0 10 10" style="flex-shrink:0;"><polygon points="5,0 10,5 5,10 0,5" fill="#9a6a34"></polygon></svg>'
          '<p style="font-size:10px;letter-spacing:0.11em;text-transform:uppercase;font-weight:700;color:var(--amber);margin:0;">Load-bearing copy, must survive</p></div>') if locked else ""
    k=f'<p style="font-size:11px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--faint);margin:0 0 5px;">::: {key}</p>' if key else \
      '<p style="font-size:10px;letter-spacing:0.11em;text-transform:uppercase;font-weight:700;color:var(--muted);margin:0 0 5px;">Diagram</p>'
    bg='background:oklch(0.945 0.013 82);padding:var(--s4) var(--s4) var(--s4);margin:0 calc(-1 * var(--s4));' if diagram else ""
    return (f'<div style="border-top:{"2px" if locked else "1px"} solid {colour if locked else "var(--rule)"};padding-top:var(--s3);margin-bottom:var(--s5);">'
            f'<div style="{bg}">{k}<p style="font-size:15px;font-weight:600;color:var(--ink);margin:0 0 5px;line-height:1.4;">{label}</p>'
            f'<p style="font-size:12.5px;line-height:1.6;color:var(--muted);margin:0;">{note}</p>{lock}</div></div>')

c1=[slot("case1-meta","Opener band, reversed out","Number, title, company and dates, role line. Full-bleed dark. The first of six landmarks.",A),
 slot("case1-stats","Four numbers, in the band","0 to 40+, &pound;10m+, 1 of 3, #1. Rule-separated, unequal widths, no boxes.",A),
 slot("case1-challenge","The challenge","Two paragraphs. Rail label plus a 680px measure.",A),
 slot("case1-role","My role","Sold every engagement, hired every person.",A),
 slot("case1-narrative","How the capability grew &nbsp;<span style='color:var(--faint)'>&larr; label from -meta</span>","Service design did not exist; it was not the first thing built.",A),
 slot("","The capability arc","Four steps on a rising baseline, a hinge before the fourth, a widening scope wedge beneath.",A,diagram=True),
 slot("case1-narrative","The turn, plus the pull-quote","&ldquo;A disjointed end-to-end experience is usually a faithful reflection of a disjointed business.&rdquo; Set large, under a short rule.",A),
 slot("","The joins nobody owned","Dark band. Journey slices, owners, four unowned joins. Service design shown without a blueprint.",A,diagram=True),
 slot("case1-narrative","Making the case, and what outlasted it","Carries the service designers&rsquo; credit for the blueprints and patterns, on the team ground.",T,locked=True),
 slot("","The operating model","Six disciplines, four engagement models plotted on breadth against duration.",A,diagram=True),
 slot("case1-approach","How it was run","Seven items, two-column definition grid.",A),
 slot("case1-hard","The hardest part","Distributed cohesion, then the programme that closed overnight.",A),
 slot("case1-impact","What changed","Displaced the agencies, retention, half contract to two thirds permanent.",A)]

c2=[slot("case2-meta","Opener band, reversed out","The role line naming the design manager and the design leads sits inside the band, not below it.",T,locked=True),
 slot("case2-stats","Four numbers, in the band","2,321, 4 rounds, 1st, 13 months. Three of the four are things I funded, not things I drew.",T),
 slot("case2-challenge","The challenge","1.9 stars. Ends on the line that this case tests whether case one was worth building.",A),
 slot("case2-role","&ldquo;I did not design this app&rdquo;","Set at display size with a rule above and below, and its own band of white space.",T,locked=True),
 slot("case2-approach","What I did instead","Six items. Won it, staffed it, argued research in, framed two problems, held the bar, backed the system.",A),
 slot("","The research that bought the right to redraw","2,321 surveyed, 266 reviews, 19 interviews, 20 hours contextual, 4 dealership visits, 12 teardowns.",A,diagram=True),
 slot("case2-hard","What the team built &nbsp;<span style='color:var(--faint)'>&larr; label from -meta</span>","The ground turns cool here and stays that way to the credit line.",T),
 slot("","One EV domain in place of four","Before and after information architecture, drawn as blocks. No screenshots.",T,diagram=True),
 slot("","Four rounds against the same task set","SUS 73, 79, 80, with the target and global average marked.",T,diagram=True),
 slot("case2-hard","My Garage, the switcher, the system","Removal of My Garage, the vehicle switcher, unified climate, and the first design system in any Toyota app.",T),
 slot("case2-hard","The credit line","Named on request, and among the references I would offer. Closes the team ground.",T,locked=True),
 slot("","Thirteen months","Dark band. Four beats, design leaving the top five complaint categories.",A,diagram=True),
 slot("","The rating turnaround","1.9 to 4.6, and the composition of reviews before and after. Public data.",A,diagram=True),
 slot("case2-impact","What changed, and what it proves","Ends on: the organisation produced a commercial outcome without me touching the work.",A)]

c3=[slot("case3-meta","Opener band, reversed out","Solo. Every decision mine, including the bad ones.",INK),
 slot("case3-stats","Four numbers, in the band","5.6k to 34k+, 20 min, Article 5, 1 person.",INK),
 slot("case3-challenge","The challenge","A question that stopped being answerable from the sidelines.",INK),
 slot("","Context growth","5,600 characters at session one to over 34,000 by session four, and the ceiling that fixed it.",A,diagram=True),
 slot("case3-approach","What I learned building it","The failure, the architectural fix, Article 5 as a design input, signal is not meaning.",INK),
 slot("case3-impact","Where it stands","Live, no revenue, no paying customers. Craft evidence rather than a business.",INK)]

def col(title,sub,colour,items):
    return (f'<div><div style="padding-bottom:var(--s3);border-bottom:2px solid {colour};margin-bottom:var(--s5);">'
            f'<p class="lbl" style="color:{colour};margin-bottom:var(--s2);">{sub}</p>'
            f'<p class="d4" style="font-size:26px;">{title}</p></div>{"".join(items)}</div>')

key="".join(f'<div style="display:flex;align-items:center;gap:8px;">{g}<p class="t3" style="font-size:12px;">{n}</p></div>' for g,n in [
 (D.dot(A,"fill",11),"My call"),(D.dot(T,"ring",11),"The team&rsquo;s work"),(D.dot(INK,"fill",11),"Solo, nobody else in the room"),
 ('<svg width="10" height="10" viewBox="0 0 10 10"><polygon points="5,0 10,5 5,10 0,5" fill="#9a6a34"></polygon></svg>',"Copy that must survive the layout pass"),
 ('<span style="width:14px;height:11px;background:oklch(0.945 0.013 82);display:inline-block;"></span>',"Diagram, not prose")])

anat=(f'<div style="width:1440px;box-sizing:border-box;padding:var(--s7);background:var(--paper);">'
 f'<p class="lbl" style="color:{A};margin-bottom:var(--s2);">Structure</p>'
 f'<p class="d2" style="margin-bottom:var(--s3);">The three cases, pulled apart</p>'
 f'<p style="font-size:16px;line-height:1.75;color:var(--body);max-width:920px;margin:0 0 var(--s5);">'
 f'Every block maps to a <span style="font-family:ui-monospace,Menlo,monospace;font-size:15px;color:var(--ink);">::: section</span> marker in work.md, '
 f'so the copy stays editable in Obsidian. Block labels come from each case&rsquo;s '
 f'<span style="font-family:ui-monospace,Menlo,monospace;font-size:15px;color:var(--ink);">-meta</span> block, so a new named section needs no template change.</p>'
 f'<div style="display:flex;gap:26px;align-items:center;padding:var(--s3) 0 var(--s6);border-bottom:1px solid var(--rule);margin-bottom:var(--s6);">{key}</div>'
 f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--s7);align-items:start;">'
 f'{col("The organisation","Case one &middot; Toyota Connected Europe",A,c1)}'
 f'{col("What the organisation shipped","Case two &middot; MyToyota and Lexus Link+",T,c2)}'
 f'{col("The craft","Case three &middot; PrepCall",INK,c3)}</div>'
 f'<p class="t3" style="margin-top:var(--s6);padding-top:var(--s5);border-top:1px solid var(--rule);max-width:920px;">'
 f'Case three is deliberately the shortest column. It is craft evidence, not a third organisational argument, and giving it equal length would overstate it.</p></div>')
write("CaseAnatomy.dc.html", anat)
print("extras ok")
