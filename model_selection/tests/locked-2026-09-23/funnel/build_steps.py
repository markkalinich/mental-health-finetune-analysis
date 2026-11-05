"""Rebuild the per-step kept/loss files for the mental-health funnel, in the paper's order.

Inputs (all already on disk; nothing is fetched here):
  fp-kept.txt                       keyword-matched ids with a full-precision checkpoint
  parent-extract.csv                one_parent / no_parent / multiple_parents per id
  ../2026-09-23-model-rows/first-pass.csv, parent-first-pass.csv
  parent-class.csv                  release class per parent (yaml, then README, then repo name)
  ../2026-09-23-model-rows/child-readmes/<org>__<name>.md

Order written (each step reads the previous step's kept set):
  3  text-capable, training method named, dataset named
       -> documented-kept.txt / documented-loss.csv / procedure-evidence.csv
       A model that fails more than one test is counted once, in this order:
       vision or video pipeline, then no training method, then no dataset.
  4  exactly one full-precision instruction-tuned parent
       -> parent-kept.csv / parent-loss.csv
       -> instruct-parent-kept.csv / instruct-parent-loss.csv
  5  downloaded at least once
       -> downloads-kept.txt / downloads-loss.csv

Run from the repo root after classify_parents.py:
    python3 reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/classify_parents.py
    .venv/bin/python reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/build_steps.py
Exits non-zero if any step's kept + losses does not equal its input count.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
ROWS = HERE.parent / "2026-09-23-model-rows"
README_DIR = ROWS / "child-readmes"

OK_DTYPES = {"F16", "BF16", "F32"}
ROOT_CKPT = re.compile(r"^model(-\d+-of-\d+)?\.safetensors$")
# Signed method list. Hyphens and underscores are read as spaces first.
# QLoRA is recorded alone when the card also says LoRA: one adapter run.
METHOD = re.compile(
    r"\b(qlora|(?<!q)lora|dpo|direct preference optimization|grpo|rlhf|ppo|sft|supervised fine ?tun\w*)\b",
    re.I,
)
JUNK = {
    "unknown", "none", "synthetic", "custom", "private", "proprietary",
    "n/a", "na", "data", "card does not say",
}
# image-text-to-text stays: those models take text and an image.
VISION = {"image-classification", "image-segmentation", "video-classification", "image-to-text"}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def rows(path: Path) -> list[dict]:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, header: list[str], data: list) -> None:
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(data)


def write_ids(path: Path, ids) -> None:
    path.write_text("\n".join(sorted(ids)) + "\n")


def check(step: str, kept: int, loss: Counter, entered: int) -> None:
    if kept + sum(loss.values()) != entered:
        fail(f"{step}: {kept} + {sum(loss.values())} != {entered}")
    print(f"{step}: {entered} -> {kept}  losses {dict(loss)}")


def norm(t: str) -> str:
    return re.sub(r"[-_]", " ", t)


def canon(match: str) -> str:
    m = match.lower()
    if m.startswith("supervised fine"):
        return "sft"
    if m == "direct preference optimization":
        return "dpo"
    return m


def named_datasets(row: dict) -> tuple[str, str, str]:
    """Return (named|not_named, source, semicolon-joined pieces)."""
    try:
        card = json.loads(row.get("cardData") or "{}")
    except json.JSONDecodeError:
        card = {}
    raw = card.get("datasets") if isinstance(card, dict) else None
    source = ""
    vals: list = []
    if raw not in (None, "", []):
        source = "yaml_datasets"
        vals = raw if isinstance(raw, list) else [raw]
    else:
        tags = [t.strip() for t in (row.get("tags") or "").split("|") if t.strip()]
        vals = [t.split(":", 1)[1].strip() for t in tags if t.lower().startswith("dataset:")]
        if vals:
            source = "dataset_tag"
    pieces = []
    for val in vals:
        for piece in str(val).split(";"):
            piece = piece.strip()
            if piece and piece.lower() not in JUNK:
                pieces.append(piece)
    named = "named" if pieces else "not_named"
    return named, source, ";".join(pieces)


def full_precision(row: dict) -> str:
    """Return 'keep' or a loss reason for one Hub row."""
    if row.get("fetch_err") or row.get("http_status") != "200":
        return "parent_unreadable"
    try:
        siblings = json.loads(row["siblings"] or "[]")
    except json.JSONDecodeError:
        siblings = []
    if not any(ROOT_CKPT.match(s.get("rfilename", "")) for s in siblings):
        return "parent_not_fp"
    try:
        record = json.loads(row["safetensors"] or "{}")
    except json.JSONDecodeError:
        record = {}
    params = record.get("parameters") if isinstance(record, dict) else None
    if not params or not set(params) <= OK_DTYPES:
        return "parent_not_fp"
    return "keep"


def methods_in(text: str) -> set[str]:
    found = {canon(m) for m in METHOD.findall(text)}
    if "qlora" in found:
        found.discard("lora")
    return found


# ---------------------------------------------------------------- load
fp_kept_ids = [ln.strip() for ln in (HERE / "fp-kept.txt").read_text().splitlines() if ln.strip()]
fp_kept = set(fp_kept_ids)
child_rows = {r["hf_id"]: r for r in rows(ROWS / "first-pass.csv")}
all_rows = {r["hf_id"].lower(): r for r in rows(ROWS / "first-pass.csv")}
for row in rows(ROWS / "parent-first-pass.csv"):
    all_rows.setdefault(row["hf_id"].lower(), row)
extract = {e["hf_id"]: e for e in rows(HERE / "parent-extract.csv")}
if set(extract) != fp_kept:
    fail("parent-extract.csv ids != fp-kept.txt ids")
missing_readme = [h for h in fp_kept_ids if not (README_DIR / (h.replace("/", "__") + ".md")).exists()]
if missing_readme:
    fail(f"{len(missing_readme)} models have no README file, e.g. {missing_readme[:3]}")

# ---------------------------------------------------------------- step 3: vision, method, dataset
doc_kept, doc_loss, evidence, c = [], [], [], Counter()
ds_rows = []
for hf_id in fp_kept_ids:
    row = child_rows[hf_id]
    pipe = (row.get("pipeline_tag") or "").strip()
    named, source, pieces = named_datasets(row)
    ds_rows.append((hf_id, named, source, pieces))
    path = README_DIR / (hf_id.replace("/", "__") + ".md")
    text = path.read_text(errors="replace")
    tags = norm(row.get("tags") or "")
    unreadable = text.startswith("FETCH_ERR")
    body = "" if unreadable else norm(re.sub(r"```.*?```", " ", text, flags=re.S))
    found = methods_in(body) | methods_in(tags)
    if "qlora" in found:
        found.discard("lora")
    if pipe in VISION:
        doc_loss.append((hf_id, "vision_or_video", pipe))
        c["vision_or_video"] += 1
        continue
    if not found:
        doc_loss.append((hf_id, "no_training_method", "readme_unreadable" if unreadable else ""))
        c["no_training_method"] += 1
        continue
    if named != "named":
        doc_loss.append((hf_id, "no_dataset", ""))
        c["no_dataset"] += 1
        continue
    doc_kept.append(hf_id)
    where = "tags" if unreadable else "readme_or_tags"
    for method in sorted(found):
        evidence.append((hf_id, method, where))

write_ids(HERE / "documented-kept.txt", doc_kept)
write_csv(HERE / "documented-loss.csv", ["hf_id", "reason", "detail"], doc_loss)
write_csv(HERE / "procedure-evidence.csv", ["hf_id", "method", "source"], evidence)
write_csv(HERE / "dataset-structured.csv", ["hf_id", "dataset_named", "dataset_source", "datasets"], ds_rows)
check("step 3  text-capable, method, dataset", len(doc_kept), c, len(fp_kept))

# ---------------------------------------------------------------- step 4: one full-precision instruction-tuned parent
pclass = {r["parent"].lower(): r for r in rows(HERE / "parent-class.csv")}
CLASS_REASON = {
    "pretrained": "parent_pretrained",
    "finetune": "parent_finetune",
    "not_stated": "parent_not_stated",
    "unreadable": "parent_card_unreadable",
    "conflict": "parent_conflict",
}
par_kept, par_loss, ins_kept, ins_loss = [], [], [], []
c = Counter()
for hf_id in doc_kept:
    entry = extract[hf_id]
    if entry["status"] == "no_parent":
        par_loss.append((hf_id, "no_parent", ""))
        c["no_parent"] += 1
        continue
    if entry["status"] == "multiple_parents":
        par_loss.append((hf_id, "multiple_parents", entry["parent"]))
        c["multiple_parents"] += 1
        continue
    parent_row = all_rows.get(entry["parent"].lower())
    verdict = "parent_unreadable" if parent_row is None else full_precision(parent_row)
    if verdict != "keep":
        par_loss.append((hf_id, verdict, entry["parent"]))
        c[verdict] += 1
        continue
    parent = parent_row["hf_id"]
    par_kept.append((hf_id, parent, entry["parent_source_field"]))
    pc = pclass.get(parent.lower())
    if pc is None:
        fail(f"step 4: parent {parent} has no row in parent-class.csv")
    if pc["class_final"] == "instruction":
        ins_kept.append((hf_id, parent, pc["class_source"]))
    else:
        reason = CLASS_REASON[pc["class_final"]]
        ins_loss.append((hf_id, reason, parent, pc["class_final"]))
        c[reason] += 1

write_csv(HERE / "parent-kept.csv", ["hf_id", "parent", "parent_source_field"], par_kept)
write_csv(HERE / "parent-loss.csv", ["hf_id", "reason", "parent"], par_loss)
write_csv(HERE / "instruct-parent-kept.csv", ["hf_id", "parent", "class_source"], ins_kept)
write_csv(HERE / "instruct-parent-loss.csv", ["hf_id", "reason", "parent", "parent_class"], ins_loss)
check("step 4  one instruction-tuned parent", len(ins_kept), c, len(doc_kept))

# ---------------------------------------------------------------- step 5: downloaded at least once
dl_kept, dl_loss, c = [], [], Counter()
for hf_id, _parent, _src in ins_kept:
    value = child_rows[hf_id]["downloads"].strip()
    if not value.isdigit():
        dl_loss.append((hf_id, "downloads_missing", value))
        c["downloads_missing"] += 1
    elif int(value) >= 1:
        dl_kept.append(hf_id)
    else:
        dl_loss.append((hf_id, "zero_downloads", value))
        c["zero_downloads"] += 1
write_ids(HERE / "downloads-kept.txt", dl_kept)
write_csv(HERE / "downloads-loss.csv", ["hf_id", "reason", "downloads"], dl_loss)
write_ids(HERE / "final-kept.txt", dl_kept)
check("step 5  downloaded at least once", len(dl_kept), c, len(ins_kept))
