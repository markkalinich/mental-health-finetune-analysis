"""Facts table for the manual review: every model in outputs/funnel/<grouping>/<CURRENT>/kept.csv that is not in --reviewed FILE
(hf_ids one per line, or a kept.csv of an earlier run). Columns: parent and class source, pipeline tag, datasets, method
tokens, downloads, automatic flags (refusal-removal tag, image or video input, no card prose, non-English card), first
lines of the card. The orchestrator adds proposed_verdict and why by reading each row; this script proposes nothing.
Writes docs/<grouping>/agent-searches/<date>-manual-review/unreviewed-kept.csv."""
import csv, re
from _common import parser, resolve, newest_card
p = parser(__doc__); p.add_argument("--reviewed", action="append", default=[], help="file(s) of hf_ids already read by a person")
a = resolve(p.parse_args())
OUT = a.searches / f"{a.date}-manual-review"; OUT.mkdir(parents=True, exist_ok=True)
done = set()
for f in a.reviewed:
    txt = open(f).read()
    done |= {r["hf_id"] for r in csv.DictReader(open(f))} if txt.startswith("hf_id") else {l.strip() for l in txt.splitlines() if l.strip()}
kept = [r for r in csv.DictReader(open(a.run_dir / "kept.csv")) if r["hf_id"] not in done]
def card(hid):
    f = newest_card(hid)
    if not f: return "(no cached card)", ""
    t = f.read_text(encoding="utf-8", errors="replace"); fm = ""
    if t.startswith("---"):
        parts = t.split("---", 2)
        if len(parts) >= 3: fm, t = parts[1], parts[2]
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", re.sub(r"<[^>]+>", "", t))
    paras = [q.strip() for q in re.split(r"\n\s*\n", body) if q.strip() and not q.strip().startswith(("#", "|")) and len(q.strip()) > 40]
    first = " ".join(paras[:2])[:600] if paras else "(no prose; front matter only)"
    return re.sub(r"\s+", " ", first), ",".join(re.findall(r"^\s*-\s*([\w\-\.]+)\s*$", fm, re.M)[:25])
rows = []
for k in kept:
    first, tags = card(k["hf_id"]); flags = []
    low = (k["hf_id"] + " " + tags).lower()
    if any(w in low for w in ("abliter", "uncensor", "heretic", "decensor", "refusal-removal", "unalign")): flags.append("refusal-removal tag")
    if "image" in k["pipeline_tag"] or "video" in k["pipeline_tag"] or "vl" in k["hf_id"].split("/")[1].lower(): flags.append("image/video input?")
    if first.startswith("(no "): flags.append("no card prose")
    if re.search(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af\u0400-\u04ff]", first): flags.append("non-English card")
    rows.append({"hf_id": k["hf_id"], "downloads": k["downloads"], "parent": k["parent"], "parent_class_source": k["parent_class_source"], "pipeline_tag": k["pipeline_tag"],
                 "datasets": k["datasets"], "methods": k["methods"], "flags": "; ".join(flags), "first_paragraph": first, "tags": tags, "proposed_verdict": "", "why": ""})
rows.sort(key=lambda r: r["hf_id"].lower())
with (OUT / "unreviewed-kept.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["hf_id"], lineterminator="\n"); w.writeheader(); w.writerows(rows)
print(len(kept), "unreviewed kept models ->", OUT / "unreviewed-kept.csv")
