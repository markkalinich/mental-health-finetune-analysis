"""Step 5 parent classifier. Rules are stated in docs/mental_health_FT_funnel/archive/2026-09-23/hf-inventory-mh-funnel-2026-09-23.md.
Run from repo root with system python3. Inputs: parent-kept.csv, model rows, parent-readmes/. Outputs: parent-class.csv, child-class.csv."""
import csv, sys, json, re, os
from collections import Counter, defaultdict
csv.field_size_limit(sys.maxsize)
F="reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/"
MR="reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-model-rows/"
RD=MR+"parent-readmes/"
kept=list(csv.DictReader(open(F+"parent-kept.csv")))
rows={}
for p in ["first-pass.csv","parent-first-pass.csv"]:
    for r in csv.DictReader(open(MR+p, newline="")): rows.setdefault(r["hf_id"].lower(), r)
parents={k["parent"] for k in kept}
if os.path.exists(F+"parent-class.csv"):
    parents |= {r["parent"] for r in csv.DictReader(open(F+"parent-class.csv"))}
parents=sorted(parents, key=str.lower)

# Source 1: YAML. 'conversational' is Hub-generated from chat_template; sft/dpo/rlhf are methods, not release status. Neither is evidence.
INSTR_TAGS={"instruct","instruction-tuned","instruction-tuning","chat"}
PRE_TAGS={"pretrained","pre-trained","base","base-model","foundation","pretraining"}
def yaml_src(r):
    tags=[t for t in (r["tags"] or "").split("|") if t]
    it=[t for t in tags if t.lower() in INSTR_TAGS]; pt=[t for t in tags if t.lower() in PRE_TAGS]
    rel=""
    try:
        bm=json.loads(r["baseModels"] or "null")
        if isinstance(bm,dict) and bm.get("relation"): rel=bm["relation"]
    except json.JSONDecodeError: pass
    for t in tags:
        m=re.match(r"base_model:(finetune|adapter|merge|quantized):", t)
        if m and not rel: rel=m.group(1)
    if it and not pt: return "instruction", "tags="+",".join(it), rel
    if pt and not it: return "pretrained", "tags="+",".join(pt), rel
    if it and pt: return "", "tags_both="+",".join(it+pt), rel
    return "", "", rel

# Source 2: README sentences about THIS checkpoint.
def body(txt):
    if txt.startswith("---"):
        parts=txt.split("\n---",1); txt=parts[1] if len(parts)>1 else txt
    txt=re.sub(r"```.*?```", " ", txt, flags=re.S)
    txt=re.sub(r"`[^`\n]*`", " ", txt)
    return txt
EXCL=re.compile(
    r"both (the )?(pre-?trained|base)( variants)? and (the )?instruct"      # gemma family line
    r"|base and instruct|pre-?trained and instruct|instruct(ion-?)?( |-)tuned and pre-?trained"  # llama family line
    r"|collection of .{0,80}(pre-?trained|instruct)"                        # 'collection of pretrained and instruction tuned models'
    r"|we release .{0,60}models|instruct(ion-tuned)? models? additionally"
    r"|results marked .{0,40}instruct|for instruction-?tuned models\b|compared to (standard )?instruction-?tuned"
    r"|fine-?tuned versions? on a task|fine-?tuned from this one|models fine-?tuned from this"   # hub card boilerplate
    r"|\btuned versions\b|is a general method"                             # 'The tuned versions use SFT and RLHF' on base cards; paper-abstract quote
    r"|export your fine-?tuned|2x faster|safety post-training|from_pretrained"
    r"|was pre-?trained on ~?(?:up to )?\d"                                  # family corpus size; 'up to 9 trillion' is the Llama 3.2 wording
    r"|these models are pre-?trained on"                                   # family corpus sentence on an instruct card
    r"|evaluation of fine-?tuned"                                          # results heading, not this checkpoint's release
    r"|pre-?trained variants, and instruction-?tuned variants", re.I)      # gemma family line that names both releases
INS_FT=re.compile(r"instruct(ion)?[- ]fine-?tuned (version|variant|model)", re.I)   # vendor instruct release phrased as 'instruct fine-tuned version of X'
FT=re.compile(r"(fine-?tuned (version|variant|model|checkpoint) of|fine-?tuned from|finetuned from model|trained on top of|continually pre-?trained from|further (fine-?tuned|trained) from|fine-?tuned (the |a |an )?[\w\-\.\/]+ (model |base model |checkpoint )?on |full fine-?tune of|this is a\b[^.]{0,120}\bfine-?tune,)", re.I)
INS=re.compile(r"(instruction-?\s?tuned|instruct-tuned|instruction[- ]?fine-?tun|post-?trained|this is the chat model|chat model (fine-?tuned|trained)|aligned (with|using|via) (rlhf|dpo)|supervised fine-?tuning (\(sft\) )?(and|followed by|with) (rlhf|dpo|reinforcement)|pre-?training\s*(&|and|→|->)\s*post-?training)", re.I)
# plural guard: 'instruction-tuned ... models' describes a family unless the sentence points at this repo
PLURAL=re.compile(r"instruct(ion)?[- ]?tuned[^.]{0,40}\bmodels\b", re.I)
THIS=re.compile(r"\bthis (repo|repository|model|release|checkpoint)\b|\bwe('re| are)? (providing|releasing)|\bthis is\b", re.I)
# 'pre-trained on 140+ languages' is a corpus-coverage bullet, not a statement that this checkpoint is the base.
PRE=re.compile(r"(pre-?trained (language )?model on|pre-?trained on (?![^.]{0,40}\blanguages\b)|this is the base model|pre-?trained only|not instruction-?tuned|base model (that|which) (has|was) not|pre-?training only)", re.I)
def sentences(t):
    for s in re.split(r"(?<=[.!?])\s+|\n+", t):
        s=" ".join(s.split())
        if 15<=len(s)<=500: yield s
def readme_src(p):
    fn=RD+p.replace("/","__")+".md"
    if not os.path.exists(fn): return None,"","no_file"
    txt=open(fn, errors="replace").read()
    if txt.startswith("FETCH_ERR"): return None,"",txt.strip()
    ft=[];ins=[];pre=[]
    for s in sentences(body(txt)):
        if EXCL.search(s): continue
        if INS_FT.search(s): ins.append(s)
        elif FT.search(s): ft.append(s)
        elif INS.search(s):
            if PLURAL.search(s) and not THIS.search(s): continue
            ins.append(s)
        elif PRE.search(s): pre.append(s)
    ev=lambda L: " || ".join(L[:2])
    if ft and ins: return "conflict", "FT: "+ev(ft)+" ## INS: "+ev(ins), ""
    if ft: return "finetune", ev(ft), ""
    if ins: return "instruction", ev(ins), ""
    if pre: return "pretrained", ev(pre), ""
    return "", "", ""

# Source 3: repo-id tokens.
NI={"instruct","it","chat","sft","dpo","rlhf"}; NP={"pt","pretrain","pretrained"}   # 'base' is a size token (bert-base, whisper-base); not evidence
def name_src(p):
    toks=re.split(r"[-_./]", p.lower())
    if any(t in NI for t in toks): return "instruction", "token="+",".join(t for t in toks if t in NI)
    if any(t in NP for t in toks): return "pretrained", "token="+",".join(t for t in toks if t in NP)
    return "", ""

out=[]
for p in parents:
    r=rows.get(p.lower())
    cy,ey,rel=yaml_src(r) if r else ("","","")
    cr,er,rerr=readme_src(p)
    cn,en=name_src(p)
    readable = cr is not None
    if cy: cf,cs=cy,"yaml"
    elif cr=="conflict": cf,cs="conflict","readme"
    elif cr: cf,cs=cr,"readme"
    elif cn: cf,cs=cn,"name"
    elif readable: cf,cs="not_stated",""
    else: cf,cs="unreadable",""
    out.append(dict(parent=p, class_yaml=cy, yaml_evidence=ey, yaml_relation=rel, class_readme=(cr or ("" if readable else "UNREADABLE:"+rerr)), readme_evidence=er, class_name=cn, name_evidence=en, class_final=cf, class_source=cs))
hdr=list(out[0].keys())
with open(F+"parent-class.csv","w",newline="") as f:
    w=csv.DictWriter(f, fieldnames=hdr); w.writeheader(); w.writerows(out)
cls={o["parent"]:o for o in out}
nkids=Counter(k["parent"] for k in kept)
with open(F+"child-class.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["hf_id","parent","class_final","class_source"])
    for k in kept: w.writerow([k["hf_id"],k["parent"],cls[k["parent"]]["class_final"],cls[k["parent"]]["class_source"]])
def table(counter_fn, label):
    t=defaultdict(Counter)
    for o in out: t[o["class_final"]][o["class_source"] or "-"]+=counter_fn(o)
    srcs=["yaml","readme","name","-"]
    print(f"\n{label:12s} " + " ".join(f"{s:>8s}" for s in srcs) + "    total")
    for c in ["instruction","pretrained","finetune","conflict","not_stated","unreadable"]:
        row=t.get(c,Counter()); print(f"{c:12s} " + " ".join(f"{row.get(s,0):8d}" for s in srcs) + f" {sum(row.values()):8d}")
    print(f"{'total':12s} " + " ".join(f"{sum(t[c].get(s,0) for c in t):8d}" for s in srcs) + f" {sum(sum(v.values()) for v in t.values()):8d}")
table(lambda o:1, "PARENTS"); table(lambda o:nkids[o["parent"]], "CHILDREN")
print("\n--- conflict rows ---")
for o in out:
    if o["class_final"]=="conflict": print(f"* {o['parent']} ({nkids[o['parent']]} children)\n    {o['readme_evidence'][:420]}")
