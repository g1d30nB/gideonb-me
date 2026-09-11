from copy import *          # noqa
from diagrams import *      # noqa
import diagrams as D

HEAD=open("_head.part").read(); TAIL=open("_tail.part").read()
def write(name, body): open(name,"w").write(HEAD+body+"\n"+TAIL)

def wrap(w, body, pad="var(--s7) var(--s7)", bg="var(--paper)"):
    return f'<div style="width:{w}px;box-sizing:border-box;padding:{pad};background:{bg};">{body}</div>'

# ---------- standalone diagram artboards ----------
write("CapabilityArc.dc.html",   wrap(1200, D.arc()))
write("ServiceGap.dc.html",      wrap(1200, D.gap(), bg="var(--night)"))
write("OperatingModel.dc.html",  wrap(1200, D.opmodel()))
write("EVDomain.dc.html",        wrap(1200, D.ev()))
write("ComplaintTimeline.dc.html",wrap(1200, D.timeline(), bg="var(--night)"))
write("SUSRounds.dc.html",       wrap(700,  D.sus(), pad="var(--s6) var(--s6)"))
write("RatingTurnaround.dc.html",wrap(700,  D.rating(), pad="var(--s6) var(--s6)"))
write("ContextGrowth.dc.html",   wrap(700,  D.ctx(), pad="var(--s6) var(--s6)"))

print("diagram artboards ok")
