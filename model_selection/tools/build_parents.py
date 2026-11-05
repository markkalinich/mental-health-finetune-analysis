"""Append the agents' parent classes (parents-N.csv) to parents.csv.

Rows the agent flagged needs_mark are settled only by a ruling in --rulings (CSV: parent_id,class,rule), where
`rule` is the sentence written into decided_by. Flagged rows without a ruling go to parents-pending-mark.csv and are
not appended. A rehost takes its original's class. Parents already in parents.csv are skipped."""
import csv, collections
from _common import parser, resolve, INV
p = parser(__doc__); p.add_argument("--rulings", help="CSV parent_id,class,rule for the needs_mark rows Mark's rules settle")
p.add_argument("--decided-on", required=True)
a = resolve(p.parse_args())
SRC = a.searches / f"{a.date}-parent-registry"; PARENTS = INV / "parents.csv"
AGENT = "agent grok-4.7 (PROMPT-parent-class v1)"
CLASSES = ("instruction", "pretrained", "finetune", "not_a_language_model", "unreadable")
rulings = {r["parent_id"]: r for r in csv.DictReader(open(a.rulings))} if a.rulings else {}
rows = [r for f in sorted(SRC.glob("parents-*.csv")) for r in csv.DictReader(open(f))]
existing = list(csv.DictReader(open(PARENTS))); have = {r["parent_id"].lower() for r in existing}
out, pending, seen = [], [], set()
for r in rows:
    pid = r["parent_id"].strip(); cls = r["class"].strip(); base = r["base_repo"].strip(); note = ""
    if pid.lower() in have or pid.lower() in seen:
        continue
    seen.add(pid.lower())
    if cls in ("rehost", "quantized_rehost"):
        orig = r["class_of_original"].strip(); note = f"{cls} of {base}; class of the original: {orig}. "
        cls = orig if orig in CLASSES else "unreadable"
    by = AGENT
    if r["needs_mark"].strip().lower() == "yes":
        if pid in rulings:
            cls = rulings[pid]["class"]; by = AGENT + "; " + rulings[pid]["rule"]
        else:
            pending.append(r); continue
    if cls not in CLASSES:
        raise SystemExit(f"bad class {cls!r} for {pid}")
    out.append({"parent_id": pid, "class": cls, "base_repo": base, "evidence_url": r["evidence_url"].strip(),
                "quote": (note + r["quote"].strip())[:500], "decided_by": by, "decided_on": a.decided_on})
with PARENTS.open("a", newline="") as fh:
    csv.DictWriter(fh, fieldnames=["parent_id", "class", "base_repo", "evidence_url", "quote", "decided_by", "decided_on"], lineterminator="\n").writerows(out)
with (SRC / "parents-pending-mark.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["parent_id"], lineterminator="\n"); w.writeheader(); w.writerows(pending)
print(len(out), "appended", dict(collections.Counter(r["class"] for r in out)), "|", len(existing) + len(out), "rows in parents.csv")
print(len(pending), "pending Mark:", [r["parent_id"] for r in pending])
