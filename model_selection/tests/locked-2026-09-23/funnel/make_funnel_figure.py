"""Render the mental-health funnel figure from the saved step files.

Every number is read from a file in this folder (or the catalog). Nothing is typed in.
If any step's kept + losses does not equal the previous step's kept, the script exits non-zero.

Run from the repo root after classify_parents.py and build_steps.py:
    .venv/bin/python reviewer_2_experiments/hf_inventory/persisted/harvest/2026-09-23-funnel/make_funnel_figure.py
Outputs funnel.svg and funnel.png beside this script.
"""
from __future__ import annotations

import csv
import gzip
import sys
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
HARVEST = HERE.parent
CATALOG = HARVEST.parent / "catalog" / "hub-public-ids.txt.gz"


def ids(path: Path) -> set[str]:
    return {ln.strip() for ln in path.read_text().splitlines() if ln.strip()}


def rows(path: Path) -> list[dict]:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def comma(n: int) -> str:
    return f"{n:,}"


def numbered(pairs: list[tuple[str, int]]) -> tuple[list[str], int]:
    kept = [(label, n) for label, n in pairs if n]
    kept.sort(key=lambda item: (-item[1], item[0]))
    lines = [f"{i}.  {comma(n)}  {label}" for i, (label, n) in enumerate(kept, 1)]
    return lines, sum(n for _label, n in kept)


with gzip.open(CATALOG, "rt") as fh:
    n_catalog = sum(1 for ln in fh if ln.strip())

kw = ids(HERE / "keyword-ids.txt")
fp_kept = ids(HERE / "fp-kept.txt")
fp_loss = Counter(r["reason"] for r in rows(HERE / "fp-loss.csv"))
if len(fp_kept) + sum(fp_loss.values()) != len(kw):
    fail(f"full precision: {len(fp_kept)} + {sum(fp_loss.values())} != {len(kw)}")
n_not_fp = fp_loss["no_root"] + fp_loss["blank_record"] + fp_loss["other_dtype"]

doc_kept = ids(HERE / "documented-kept.txt")
doc_loss = Counter(r["reason"] for r in rows(HERE / "documented-loss.csv"))
if len(doc_kept) + sum(doc_loss.values()) != len(fp_kept):
    fail(f"step 3: {len(doc_kept)} + {sum(doc_loss.values())} != {len(fp_kept)}")

ins_kept = rows(HERE / "instruct-parent-kept.csv")
ins_loss = Counter(r["reason"] for r in rows(HERE / "instruct-parent-loss.csv"))
par_loss = Counter(r["reason"] for r in rows(HERE / "parent-loss.csv"))
parent_cut = sum(par_loss.values()) + sum(ins_loss.values())
if len(ins_kept) + parent_cut != len(doc_kept):
    fail(f"step 4: {len(ins_kept)} + {parent_cut} != {len(doc_kept)}")
ins_src = Counter(r["class_source"] for r in ins_kept)
n_ins_parents = len({r["parent"].lower() for r in ins_kept})

dl_kept = ids(HERE / "downloads-kept.txt")
dl_loss = Counter(r["reason"] for r in rows(HERE / "downloads-loss.csv"))
if len(dl_kept) + sum(dl_loss.values()) != len(ins_kept):
    fail(f"step 5: {len(dl_kept)} + {sum(dl_loss.values())} != {len(ins_kept)}")
(HERE / "final-kept.txt").write_text("\n".join(sorted(dl_kept)) + "\n")

main = [
    ("Listed Hugging Face models", comma(n_catalog), "", None),
    ("Full-precision models with\nmatching keyword(s)", comma(len(fp_kept)), "",
     [("not keyword-matched", n_catalog - len(kw)),
      ("no full-precision model available", n_not_fp)]),
    ("Text-capable model with both\ntraining method and dataset\nexplicitly named", comma(len(doc_kept)), "",
     [("vision or video pipeline", doc_loss["vision_or_video"]),
      ("no training method named", doc_loss["no_training_method"]),
      ("no dataset named", doc_loss["no_dataset"])]),
    ("Exactly one full-precision,\ninstruction-tuned parent", comma(len(ins_kept)), "",
     [("No parent model named", par_loss["no_parent"]),
      ("Two or more parent models named", par_loss["multiple_parents"]),
      ("No available full-precision parent model", par_loss["parent_not_fp"]),
      ("Parent model is pre-trained", ins_loss["parent_pretrained"]),
      ("Parent model is also a fine-tune", ins_loss["parent_finetune"]),
      ("Parent model does not say instruction-tuned, pre-trained, or fine-tune", ins_loss["parent_not_stated"]),
      ("Parent model could not be read", par_loss["parent_unreadable"] + ins_loss["parent_card_unreadable"]),
      ("Parent model says both a fine-tune and instruction-tuned", ins_loss["parent_conflict"])]),
    ("Downloaded at least once", comma(len(dl_kept)), "",
     [("zero lifetime downloads", dl_loss["zero_downloads"]),
      ("downloads field missing", dl_loss["downloads_missing"])]),
]

drawn = []
for label, count, note, loss in main:
    lines, removed = numbered(loss) if loss else ([], 0)
    drawn.append((label, count, note, lines, removed))

# Row height follows the loss list so neighboring loss boxes do not meet.
bh = 1.55
gap = 0.42
row_heights = []
for _label, _count, note, lines, _removed in drawn:
    loss_h = (0.36 * len(lines) + 0.62) if lines else 0
    note_h = 0.28 if note else 0
    row_heights.append(max(bh + note_h, loss_h) + gap)
fig_h = sum(row_heights) + 0.3
fig, ax = plt.subplots(figsize=(17.4, fig_h))
ax.set_xlim(0, 17.4)
ax.set_ylim(0, fig_h)
ax.axis("off")

bx, bw = 0.45, 5.7
lx, lw = 7.15, 9.8
cursor = fig_h - 0.15
centers = []
for i, ((label, count, note, lines, removed), row_h) in enumerate(zip(drawn, row_heights)):
    top = cursor
    bottom = cursor - (row_h - gap)
    y = bottom + max(0, (top - bottom - bh) / 2)
    centers.append(y)
    ax.add_patch(FancyBboxPatch((bx, y), bw, bh, boxstyle="round,pad=0.02,rounding_size=0.08",
                                linewidth=1.2, edgecolor="black", facecolor="white"))
    ax.text(bx + 0.16, y + bh / 2, label, fontsize=12.5, va="center", ha="left")
    ax.text(bx + bw - 0.16, y + bh / 2, count, fontsize=18, fontweight="bold", va="center", ha="right")
    if note:
        ax.text(bx + 0.16, y + 0.08, note, fontsize=7.0, va="bottom", ha="left", color="#333333")
    if lines:
        loss_h = 0.36 * len(lines) + 0.62
        ly = y + bh / 2 - loss_h / 2
        ax.add_patch(FancyBboxPatch((lx, ly), lw, loss_h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                    linewidth=0.9, edgecolor="#777777", facecolor="#f4f4f4"))
        ax.text(lx + 0.12, ly + loss_h - 0.08, f"{comma(removed)} models removed",
                fontsize=12.0, fontweight="bold", va="top", ha="left")
        ax.text(lx + 0.12, ly + loss_h - 0.46, "\n".join(lines), fontsize=11.2, va="top", ha="left", family="monospace")
        ax.add_patch(FancyArrowPatch((bx + bw, y + bh / 2), (lx, y + bh / 2), arrowstyle="-|>",
                                     mutation_scale=12, linewidth=0.9, color="#777777"))
    cursor -= row_h

for i in range(len(centers) - 1):
    y_above = centers[i]
    y_below = centers[i + 1] + bh
    ax.add_patch(FancyArrowPatch((bx + bw / 2, y_above), (bx + bw / 2, y_below),
                                 arrowstyle="-|>", mutation_scale=14, linewidth=1.1, color="black"))

fig.savefig(HERE / "funnel.svg", bbox_inches="tight")
fig.savefig(HERE / "funnel.png", dpi=170, bbox_inches="tight")
print("wrote", HERE / "funnel.svg", "and funnel.png")
print("main column:", [(label.replace("\n", " "), count) for label, count, _note, _lines, _removed in drawn])
