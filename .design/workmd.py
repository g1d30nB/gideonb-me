# Reads work.md at build time so the design never drifts from the copy. Mirrors src/lib/page.mjs.
import re, html
ROOT="/Users/gideon/Projects/My Website/gideonb-me/work.md"
def load():
    raw=open(ROOT,encoding="utf-8").read()
    meta={}
    fm=re.match(r"^---\n([\s\S]*?)\n---",raw)
    if fm:
        for line in fm.group(1).split("\n"):
            if ":" in line: k,v=line.split(":",1); meta[k.strip()]=v.strip()
    sections={m.group(1):m.group(2).strip() for m in re.finditer(r"^::: ([\w-]+)\r?\n([\s\S]*?)\r?\n:::[ \t]*$",raw,re.M)}
    return meta,sections
def kv(text):
    out={}
    for line in (text or "").split("\n"):
        if ":" in line: k,v=line.split(":",1); out[k.strip()]=v.strip()
    return out
def esc(s):
    s=html.escape(s,quote=False)
    s=s.replace("'","&rsquo;")
    s=re.sub(r'"([^"]*)"',r"&ldquo;\1&rdquo;",s)
    s=s.replace("&amp;","&amp;")
    return s
def paras(text): return [esc(p.strip()) for p in re.split(r"\n\s*\n",text or "") if p.strip()]
def bullets(text):
    out=[]
    for line in (text or "").split("\n"):
        line=line.strip()
        if not line.startswith("- "): continue
        m=re.match(r"- \*\*(.+?)\*\*\s*(.*)",line[0:])
        if m: out.append((esc(m.group(1)),esc(m.group(2))))
        else: out.append(("",esc(line[2:])))
    return out
def stats(text):
    out=[]
    for line in (text or "").split("\n"):
        line=line.strip()
        if line.startswith("- ") and "|" in line:
            v,l=line[2:].split("|",1); out.append((esc(v.strip()),esc(l.strip())))
    return out
META,SEC=load()
def case(n):
    k=f"case{n}"
    return dict(info=kv(SEC.get(k+"-meta")),challenge=paras(SEC.get(k+"-challenge")),role=paras(SEC.get(k+"-role")),
                narrative=paras(SEC.get(k+"-narrative")),approach=bullets(SEC.get(k+"-approach")),hard=paras(SEC.get(k+"-hard")),
                stats=stats(SEC.get(k+"-stats")),impact=paras(SEC.get(k+"-impact")))
C1,C2,C3,C4=case(1),case(2),case(3),case(4)
INTRO=paras(SEC.get("intro")); CLOSING=paras(SEC.get("closing")); CONTACT=paras(SEC.get("contact"))
if __name__=="__main__":
    for n,c in [(1,C1),(2,C2),(3,C3)]:
        print(n,c["info"].get("title"),"|",len(c["narrative"]),"narr",len(c["approach"]),"approach",len(c["stats"]),"stats")
    print("intro",len(INTRO),"closing",len(CLOSING),"contact",len(CONTACT))
    print(C3["approach"][-1][0], "->", C3["approach"][-1][1][:90])
