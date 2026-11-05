#!/usr/bin/env python3
"""Share of items with a parsable reply, for the three tasks in this study.

One heatmap per model family. Parents are ordered by version, then by size.
Each instruction-tuned model is one row. Under it are the fine-tunes that name
it: mental health, then safety, then medical. When
orchestration.study_roster.DRAW_PRETRAINED is true, the pretrained checkpoint
that was run for it is the last row in that group. A colored
square marks that type. A symlink to another weight directory is the same parent.

Every row's scores are the roster columns (outputs/roster/CURRENT, filled by
orchestration/fill_roster_scores.py from replies/lenient-parse-pilot/labels-current.jsonl).

A cell is a percent. An unparsed reply stays in the denominator. When the gold
label is yes it is a false negative. When the gold label is no it is a false
positive.
A grey cell means that model has no complete file for that column.
A grey MentalHealthBench cell reads N/A: a safety fine-tune, which was not
run on this benchmark, or an instruction-tuned parent that has no
MentalHealthBench file. The Obj. and Method cells of an instruction-tuned or
pretrained row also read N/A. A fine-tune whose card and search did not state
which weights changed reads Unstated.
The first four score columns are the yes/no parse. Strict is the first-line
yes or no. Recovered is that share plus the replies that fail it and that
Sonnet labels answered_yes or answered_no. Recovered is at least Strict.

Synthetic suicidal ideation is the v2 yes/no prompt, 450 sentences. C-SSRS is
the v5 yes/no prompt, 500 users. A reply the format check accepts is that yes
or no. A reply it rejects takes the Sonnet label: answered_yes or answered_no
is the prediction, and not_an_answer stays unparsed. Sensitivity uses yes as
the positive class. C-SSRS yes is Ideation, Behavior, or Attempt; no is
Supportive or Indicator. An unparsed reply is a false negative when the gold
label is yes and a false positive when it is no.
MentalHealthBench is not part of that read. The column on the figure is the
same 86-question suicide and self-harm score used on the spaghetti plot. The
full-bench total is the roster column mhb_total and is not drawn.

Safety rows are every safety fine-tune on the roster. For the nine in USABLE_IDS
(safety_labels/cohort.py), a card label that maps to yes or
no also counts as a format success, the same rule as the Sonnet failure list.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.transforms import ScaledTranslation, blended_transform_factory

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from config.constants import SI_POSITIVE_CATEGORIES
from orchestration.run_experiment import _user_message
from orchestration.yesno_decision_review import _message_text, format_parsed
from safety_labels.cohort import BY_ID, USABLE_IDS
from safety_labels.parse import parse_reply
from safety_labels.score import CSSRS_NO, CSSRS_YES, predicted_yes
from utilities.schemas import parse_one_word
OUT_DIR = REPO / "outputs/cross-grouping/model_performance"
FAMILY_ORDER = ["Gemma", "Llama", "Qwen", "Mistral", "Falcon", "LFM2", "SmolLM", "TinyLlama", "FLAN-T5"]

SI_CSV = REPO / "data/inputs/finalized_input_data/SI_finalized_sentences.csv"
SI_PREFIX = REPO / "data/prompts/suicide_ideation_yesno_v2_prefix.txt"
SI_SUFFIX = REPO / "data/prompts/suicide_ideation_yesno_v2_suffix.txt"
CSSRS_YESNO = REPO / "replies/cssrs-yesno-v5"
CACHE_DB = REPO / "cache/results.db"
# Pooled format-or-Sonnet counts for the 75-model run. The script stops if a
# rebuild does not reproduce them.
MHB_GRADES = REPO / "replies/mentalhealthbench-1215-temp0"
# A data column used to be 1.0 of the old axis and about 2.4 inches wide.
# 0.34 of that width is the 66% reduction.
DATA_IN = 0.82
ROW_IN = 0.40
# Wider than a row so "Params" and "Med" fit at the column-label size.
# "Objective" is 0.66 in at this label size, so the header is "Obj."
# "Unstated" is 0.57 in, so the method column is wider than the other three.
META_IN = 0.58
METHOD_IN = 0.76
META_WIDTHS_IN = (META_IN, META_IN, META_IN, METHOD_IN)
# Grouped by the number, not by the benchmark. MentalHealthBench has no
# sensitivity, specificity, or F1. Its score column is the 86 suicide and
# self-harm conversations. The full 1,215-conversation score is computed and
# kept on the roster and is not drawn.
# The first five sit under one "Parsing" line. Strict, then the Sonnet-enabled
# rate, for synthetic SI and then for C-SSRS. The MentalHealthBench entry is
# the share of the 86 suicide and self-harm conversations with a non-empty
# reply, not the share of all 1,215.
PARSE_SPAN = 5
COLUMNS = (
    ("si_strict", "SI", "Strict"),
    ("si_recovered", "SI", "Recovered"),
    ("cssrs_strict", "C-SSRS", "Strict"),
    ("cssrs_recovered", "C-SSRS", "Recovered"),
    ("mhb_parse", "MHB-Safety", "Parsed"),
    ("si_sens", "SI", "Sens"),
    ("cssrs_sens", "C-SSRS", "Sens"),
    ("si_spec", "SI", "Spec"),
    ("cssrs_spec", "C-SSRS", "Spec"),
    ("si_f1", "SI", "F1"),
    ("cssrs_f1", "C-SSRS", "F1"),
    ("mhb86", "MHB-Safety", "Score"),
)
MHB_SCORE_KEYS = frozenset({"mhb86", "mhb_total", "mhb_pos", "mhb_pen"})


def _binary(pairs: list[tuple[bool, bool | None]]) -> dict[str, float]:
    """Sensitivity, specificity, and F1.

    An unparsed reply is a false negative when the gold label is yes, and a
    false positive when the gold label is no.
    """
    if not pairs:
        raise SystemExit("binary metrics need at least one item")
    tp = tn = fp = fn = 0
    for gold, pred in pairs:
        if gold:
            if pred is True:
                tp += 1
            else:
                fn += 1
        elif pred is False:
            tn += 1
        else:
            fp += 1
    if tp + fn == 0 or tn + fp == 0:
        raise SystemExit("binary metrics need both classes in the gold labels")
    sens = tp / (tp + fn)
    spec = tn / (tn + fp)
    precision = tp / (tp + fp) if tp + fp else 0.0
    f1 = 0.0 if precision + sens == 0 else 2 * precision * sens / (precision + sens)
    n_parsed = sum(pred is not None for _gold, pred in pairs)
    return {"sens": sens, "spec": spec, "f1": f1, "n": float(len(pairs)), "n_parsed": float(n_parsed)}


def _prompt_line(path: Path) -> str:
    """Same line the run passed: newlines removed, then strip."""
    return path.read_text(encoding="utf-8").replace("\n", "").strip()


def _gold_si_v2() -> dict[str, bool]:
    """Gold keyed by the md5 of the wrapped v2 user message, which is the cache hash."""
    prefix = _prompt_line(SI_PREFIX)
    suffix = _prompt_line(SI_SUFFIX)
    gold = {}
    with SI_CSV.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            wrapped = _user_message(row["statement"], prefix, suffix)
            digest = hashlib.md5(wrapped.encode()).hexdigest()
            gold[digest] = row["Safety type"] in SI_POSITIVE_CATEGORIES
    if len(gold) != 450:
        raise SystemExit(f"{SI_CSV} has {len(gold)} sentences")
    return gold


def _reply_text(raw: str) -> str:
    """Chat message text, or the completion text when the reply has no message."""
    text = _message_text(raw or "")
    if text:
        return text
    try:
        obj = json.loads(raw or "")
    except json.JSONDecodeError:
        return ""
    choices = obj.get("choices") or [{}]
    completion = (choices[0] or {}).get("text")
    return completion if isinstance(completion, str) else ""


def _format_yes(model_id: str, text: str) -> bool | None:
    """The yes or no the format check already accepted. None when it rejected the reply."""
    parsed = parse_one_word(text or "", "suicidal_ideation", "x_yesno")
    if parsed and parsed.get("safety_type") in ("yes", "no"):
        return parsed["safety_type"] == "yes"
    if model_id not in set(USABLE_IDS):
        return None
    kind = BY_ID[model_id].kind
    card = parse_reply(kind, text or "")
    return predicted_yes(kind, "synthetic_si", card["status"], card["label"])


def _gold_flag(value: str, path: Path) -> bool:
    text = (value or "").strip().lower()
    if text in ("yes", "true", "1"):
        return True
    if text in ("no", "false", "0"):
        return False
    raise SystemExit(f"{path} gold_yes is {value!r}")


def _mhb_scores(model_ids: set[str] | None = None) -> dict[str, dict]:
    """MentalHealthBench scores for every processed run.

    Whether a run is processed is decided by orchestration.mhb_status
    .grade_file_status and nowhere else: 1,215 conversations answered and all
    5,262 criteria graded ``ok``. A run in any other state is not in the
    result; its roster cell stays blank. ``model_ids`` limits the directories
    read; by default every directory under replies/mentalhealthbench-1215-temp0.
    """
    from orchestration.mhb_status import GRADES_NAME, dataset_rubric, grade_file_status, read_grades
    from orchestration.plot_mhb_pair_gap import question_parts
    from orchestration.plot_spaghetti_mhb_safety import safety_questions

    rubric = dataset_rubric()
    _rubric_n, labels = safety_questions()
    safety_ids = set(labels)
    if model_ids is None:
        model_ids = {_hub(path.name) for path in MHB_GRADES.iterdir() if path.is_dir()}
    found = {}
    for hf_id in sorted(model_ids):
        status = grade_file_status(hf_id, rubric)
        if not status.processed:
            continue
        grades = status.directory / GRADES_NAME
        grouped: dict[str, list[dict]] = defaultdict(list)
        for row in read_grades(grades):
            grouped[row["id"]].append(row)
        parts = [question_parts(criteria) for criteria in grouped.values()]
        safety_parts = [question_parts(grouped[qid]) for qid in safety_ids]
        found[hf_id] = {
            "total": sum(part["clipped"] for part in parts) / len(parts),
            "positive": sum(part["positive_credit"] for part in parts) / len(parts),
            "penalty": sum(part["penalty_burden"] for part in parts) / len(parts),
            "safety86": sum(part["clipped"] for part in safety_parts) / len(safety_parts),
            "path": str(grades.relative_to(REPO)),
        }
    return found


def _safe(hf_id: str) -> str:
    return hf_id.replace("/", "__")


def _hub(dirname: str) -> str:
    return dirname.replace("__", "/", 1)


def _size_key(size: str) -> float:
    match = re.match(r"([\d.]+)\s*([MB])", size or "")
    if not match:
        return 1e18
    number = float(match.group(1))
    return number * (1e6 if match.group(2) == "M" else 1e9)


def _family_key(family: str) -> tuple:
    try:
        return (FAMILY_ORDER.index(family),)
    except ValueError:
        return (len(FAMILY_ORDER), family)


def _mentalhealthbench() -> dict[str, dict]:
    found = {}
    root = REPO / "replies/mentalhealthbench-1215-temp0"
    if not root.is_dir():
        return found
    from orchestration.plot_spaghetti_mhb_safety import MHB_SAFETY_N, safety_questions

    _rubric_n, labels = safety_questions()
    safety_ids = set(labels)
    if len(safety_ids) != MHB_SAFETY_N:
        raise SystemExit(
            f"expected {MHB_SAFETY_N} suicide/self-harm conversations, found {len(safety_ids)}"
        )
    for path in root.iterdir():
        summary_path = path / "summary.json"
        generations = path / "generations.jsonl"
        if not summary_path.is_file() or not generations.is_file():
            continue
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        if summary.get("n_items") != 1215:
            continue
        decoder = json.JSONDecoder()
        text = generations.read_text(encoding="utf-8")
        n = 0
        n_parsed = 0
        n_subset = 0
        n_subset_parsed = 0
        ids = set()
        index = 0
        length = len(text)
        broken = False
        while index < length:
            while index < length and text[index].isspace():
                index += 1
            if index >= length:
                break
            try:
                row, index = decoder.raw_decode(text, index)
            except json.JSONDecodeError:
                broken = True
                break
            if not isinstance(row, dict):
                broken = True
                break
            n += 1
            item_id = row.get("id")
            ids.add(item_id)
            reply = row.get("raw_completion")
            nonempty = isinstance(reply, str) and reply.strip()
            if nonempty:
                n_parsed += 1
            if item_id in safety_ids:
                n_subset += 1
                if nonempty:
                    n_subset_parsed += 1
        if broken or n != 1215 or len(ids) != 1215:
            continue
        if n_subset != len(safety_ids):
            raise SystemExit(
                f"{path}: expected {len(safety_ids)} suicide/self-harm conversations, found {n_subset}"
            )
        found[_hub(path.name)] = {
            "n": 1215,
            "n_parsed": n_parsed,
            "n86": n_subset,
            "n_parsed86": n_subset_parsed,
            "source": "study",
            "path": str(generations.relative_to(REPO)),
        }
    return found


def _percent_value(percent: float, star: bool) -> str:
    text = f"{percent:.0f}" if abs(percent - round(percent)) < 0.05 else f"{percent:.1f}"
    if star:
        text += "*"
    return text


def _percent_text(rate: dict) -> str:
    percent = 100.0 * rate["n_parsed"] / rate["n"]
    return _percent_value(percent, rate["card_format"])


TYPE_ORDER = {"mental-health": 0, "safety": 1, "medical": 2}
TYPE_COLOR = {
    "parent": "#2E86AB",
    "pretrained": "#115E59",
    "mental-health": "#C73E1D",
    "safety": "#7B2D8E",
    "medical": "#F18F01",
}
TYPE_LETTER = {
    "parent": "IT",
    "pretrained": "PT",
    "mental-health": "MH",
    "safety": "Sa",
    "medical": "Med",
}
TYPE_LETTER_COLOR = {
    "parent": "white",
    "pretrained": "white",
    "mental-health": "white",
    "safety": "white",
    "medical": "#1a1a1a",
}
OBJ_COLOR = {
    "SFT": ("#335C67", "white"),
    "GRPO": ("#52796F", "white"),
    "DPO": ("#6D597A", "white"),
    "DIST": ("#457B9D", "white"),
    "MULT": ("#9C6644", "white"),
}
OBJ_FROM_STAGE = {"sft": "SFT", "grpo": "GRPO", "dpo": "DPO", "distillation": "DIST"}
NA_FACE = "#f3f3f3"
NA_INK = "#1a1a1a"
SCOPE_COLOR = {
    "Q/LoRA": ("#1B4F72", "white"),
    "Full": ("#8C4A2F", "white"),
    "Unstated": ("#E4DDD0", NA_INK),
    "N/A": (NA_FACE, NA_INK),
}
TYPE_LEGEND = (
    ("parent", "Instruction-tuned (IT)"),
    ("pretrained", "Pretrained (PT)"),
    ("mental-health", "Mental health (MH)"),
    ("safety", "Safety (Sa)"),
    ("medical", "Medical (Med)"),
)


def type_legend() -> tuple[tuple[str, str], ...]:
    """Legend entries actually drawn. The pretrained entry returns with DRAW_PRETRAINED."""
    from orchestration.study_roster import DRAW_PRETRAINED

    if DRAW_PRETRAINED:
        return TYPE_LEGEND
    return tuple(item for item in TYPE_LEGEND if item[0] != "pretrained")
# Assigned in version order inside each figure. The same three colors are the
# Qwen figure; a fourth version in another family takes the blue.
VERSION_PALETTE = ("#72B7B2", "#54A24B", "#E45756", "#4C78A8")
VERSION_LABEL = {
    "Gemma 1": "1",
    "Gemma 3": "3",
    "Gemma 3n": "3n",
    "Gemma 4": "4",
    "Llama 3": "3",
    "Llama 3.1": "3.1",
    "Llama 3.2": "3.2",
    "Mistral 7B v0.2/v0.3": "v0.2/0.3",
    "Qwen2.5": "2.5",
    "Qwen3": "3",
    "Qwen3.5": "3.5",
    "SmolLM2": "2",
}
# Effective parameter counts, in billions. Gemma 3n E2B and E4B use the number
# in the size label. Gemma 4 card table: E2B 2.3B effective, E4B 4.5B effective.
EFFECTIVE_BILLIONS = {
    ("Gemma", "Gemma 3n", "E2B"): 2.0,
    ("Gemma", "Gemma 3n", "E4B"): 4.0,
    ("Gemma", "Gemma 4", "E2B"): 2.3,
    ("Gemma", "Gemma 4", "E4B"): 4.5,
}


def _version_span_key(version: str) -> str:
    """Versions that share one model-version rank use one bar on the figure."""
    if version in {"Mistral 7B v0.2", "Mistral 7B v0.3"}:
        return "Mistral 7B v0.2/v0.3"
    return version


def _version_colors(block: list[dict]) -> dict[str, str]:
    order = []
    for row in block:
        key = _version_span_key(row["version"])
        if key not in order:
            order.append(key)
    if len(order) > len(VERSION_PALETTE):
        raise SystemExit(f"need {len(order)} version colors and have {len(VERSION_PALETTE)}")
    return {version: VERSION_PALETTE[index] for index, version in enumerate(order)}


def _param_billions(row: dict) -> tuple[float, bool]:
    """Return (billions, effective). Effective counts are the E2B and E4B rows."""
    size = row["size"]
    if "E2B" in size or "E4B" in size:
        key = (row["family"], row["version"], "E2B" if "E2B" in size else "E4B")
        if key not in EFFECTIVE_BILLIONS:
            raise SystemExit(f"no effective parameter count for {row['family']} {row['version']} {size}")
        return EFFECTIVE_BILLIONS[key], True
    match = re.match(r"([\d.]+)\s*([MB])", size)
    if not match:
        raise SystemExit(f"cannot read a parameter count from size {size!r} ({row['hf_id']})")
    number = float(match.group(1))
    if match.group(2) == "M":
        number /= 1000.0
    return number, False


def _param_text(billions: float, effective: bool) -> str:
    text = f"{billions:.3f}".rstrip("0").rstrip(".")
    if effective:
        text += "*"
    return text


def _short(hf_id: str, collisions: set[str]) -> str:
    # The organization is not part of the row name. google/gemma-3-4b-it and
    # unsloth/gemma-3-4b-it are both gemma-3-4b-it.
    del collisions
    return hf_id.split("/", 1)[-1]


def _collisions(rows: list[dict]) -> set[str]:
    seen: dict[str, str] = {}
    clashes = set()
    for row in rows:
        name = row["hf_id"].split("/", 1)[-1]
        other = seen.get(name)
        if other is not None and other != row["hf_id"]:
            clashes.add(name)
        seen[name] = row["hf_id"]
    return clashes


def _one_parent_block(rows: list[dict]) -> list[dict]:
    """Instruction-tuned row, then its fine-tunes, then its pretrained checkpoint."""
    by_parent: dict[str, dict] = {}
    for row in rows:
        slot = by_parent.setdefault(row["parent"], {"parent": None, "bases": [], "kids": []})
        if row["role"] == "parent":
            current = slot["parent"]
            if current is None:
                slot["parent"] = row
            else:
                filled = sum(value is not None for value in row["rates"].values())
                have = sum(value is not None for value in current["rates"].values())
                if filled > have:
                    slot["parent"] = row
        elif row["role"] == "pretrained":
            slot["bases"].append(row)
        else:
            slot["kids"].append(row)
    ordered_parents = sorted(
        by_parent,
        key=lambda parent: (
            by_parent[parent]["parent"]["version"],
            _size_key(by_parent[parent]["parent"]["size"]),
            parent,
        ),
    )
    block = []
    for parent in ordered_parents:
        slot = by_parent[parent]
        if slot["parent"] is None:
            raise SystemExit(f"fine-tunes of {parent} have no instruction-tuned row")
        block.append(slot["parent"])
        kids = sorted(slot["kids"], key=lambda row: (TYPE_ORDER[row["grouping"]], row["hf_id"]))
        block.extend(kids)
        seen_bases: set[str] = set()
        for base in slot["bases"]:
            if base["hf_id"] in seen_bases:
                continue
            seen_bases.add(base["hf_id"])
            block.append(base)
    return block


def _version_spans(block: list[dict]) -> list[tuple[int, int, str]]:
    spans = []
    start = 0
    for index, row in enumerate(block):
        if _version_span_key(row["version"]) != _version_span_key(block[start]["version"]):
            spans.append((start, index - 1, _version_span_key(block[start]["version"])))
            start = index
    spans.append((start, len(block) - 1, _version_span_key(block[start]["version"])))
    return spans


def _row_centers(block: list[dict]) -> list[float]:
    """One unit per row, and one full row of space before each new instruction-tuned parent."""
    centers = []
    cursor = 0.0
    previous = None
    for row in block:
        parent = row["parent"]
        if previous is not None and parent != previous:
            cursor += 1.0
        centers.append(cursor)
        cursor += 1.0
        previous = parent
    return centers


def _block_span(block: list[dict]) -> float:
    centers = _row_centers(block)
    if not centers:
        return 0.0
    return centers[-1] - centers[0] + 1.0


def _mhb_ids() -> set[str]:
    from orchestration.study_roster import load_roster, mhb_safety_ids

    return mhb_safety_ids(load_roster())


def _not_run(row: dict, block: list[dict]) -> bool:
    """MentalHealthBench cells are N/A outside the MHB-Safety comparison.

    Safety fine-tunes are out. An instruction-tuned parent is out when no
    mental-health or medical fine-tune names it, even if that parent has a
    score. plot_params_vs_score uses the same id set. A parent that is in the
    comparison but has no replies is N/A when every fine-tune under it on this
    figure is a safety model.
    """
    if row["role"] in {"fine-tune", "parent"} and row["hf_id"] not in _mhb_ids():
        return True
    if row["rates"]["mentalhealthbench"] is not None:
        return False
    if row["role"] != "parent":
        return False
    kids = [other for other in block if other["role"] == "fine-tune" and other["parent"] == row["parent"]]
    return bool(kids) and all(other["grouping"] == "safety" for other in kids)


def _meta_layout() -> tuple[list[float], list[float], float]:
    """Left edge and width of each meta column, then where the data columns start.

    Units are data columns: one data cell is 1 wide.
    """
    widths = [width / DATA_IN for width in META_WIDTHS_IN]
    lefts = []
    cursor = 0.0
    for width in widths:
        lefts.append(cursor)
        cursor += width
    return lefts, widths, cursor


def _cell_value(row: dict, key: str) -> tuple[float | None, str | None, bool]:
    """Return (percent or None, text or None, card-format star)."""
    if key == "mhb86":
        score = row["scores"]["mhb"]
        if score is None or "safety86" not in score:
            return None, None, False
        value = 100.0 * score["safety86"]
        return value, _percent_value(value, False), False
    if key in ("si_strict", "si_recovered", "cssrs_strict", "cssrs_recovered"):
        task = "synthetic_si" if key.startswith("si_") else "cssrs"
        rate = row["rates"][task]
        if rate is None:
            return None, None, False
        field = "strict" if key.endswith("_strict") else "recovered"
        if field not in rate:
            return None, None, False
        value = 100.0 * rate[field]
        return value, _percent_value(value, rate["card_format"]), rate["card_format"]
    if key == "mhb_parse":
        rate = row["rates"]["mentalhealthbench"]
        if rate is None:
            return None, None, False
        if "n86" not in rate or "n_parsed86" not in rate:
            raise SystemExit(f"{row['hf_id']}: MentalHealthBench parse rate has no 86-conversation count")
        shown = {**rate, "n": rate["n86"], "n_parsed": rate["n_parsed86"]}
        return 100.0 * rate["n_parsed86"] / rate["n86"], _percent_text(shown), False
    if key in ("si_sens", "si_spec", "si_f1"):
        score = row["scores"]["synthetic_si"]
        if score is None:
            return None, None, False
        field = {"si_sens": "sens", "si_spec": "spec", "si_f1": "f1"}[key]
        value = 100.0 * score[field]
        rate = row["rates"]["synthetic_si"]
        return value, _percent_value(value, rate["card_format"]), rate["card_format"]
    if key in ("cssrs_sens", "cssrs_spec", "cssrs_f1"):
        score = row["scores"]["cssrs"]
        if score is None:
            return None, None, False
        field = {"cssrs_sens": "sens", "cssrs_spec": "spec", "cssrs_f1": "f1"}[key]
        value = 100.0 * score[field]
        rate = row["rates"]["cssrs"]
        return value, _percent_value(value, rate["card_format"]), rate["card_format"]
    score = row["scores"]["mhb"]
    if score is None:
        return None, None, False
    field = {"mhb_total": "total", "mhb_pos": "positive", "mhb_pen": "penalty"}[key]
    value = 100.0 * score[field]
    return value, _percent_value(value, False), False


def _code_cell(ax, left: float, width: float, y: float, code: str, palette: dict, row: dict, kind: str) -> None:
    """One Obj. or Method cell. Instruction-tuned and pretrained rows read N/A."""
    if row["role"] == "fine-tune" and code not in palette:
        raise SystemExit(f"{row['hf_id']} has no {kind} code")
    if code in palette and code != "N/A":
        face, ink = palette[code]
        text = code
    else:
        face, ink, text = NA_FACE, NA_INK, "N/A"
    ax.add_patch(plt.Rectangle((left, y - 0.5), width, 1.0, facecolor=face, edgecolor="none", zorder=4))
    ax.text(
        left + width / 2,
        y,
        text,
        ha="center",
        va="center",
        fontsize=8,
        fontweight="bold",
        color=ink,
        zorder=7,
    )


def _paint(ax, block: list[dict], clashes: set[str], cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm) -> None:
    lefts, widths, data0 = _meta_layout()
    centers = _row_centers(block)
    ax._row_centers = centers
    ax.set_facecolor("white")
    x_end = data0 + len(COLUMNS)
    ax.set_xlim(0, x_end)
    ax.set_ylim(centers[-1] + 0.5, centers[0] - 0.5)
    tick_x = []
    tick_labels = []
    for index, (_key, title, group) in enumerate(COLUMNS):
        tick_x.append(data0 + index + 0.5)
        tick_labels.append(f"{group}\n{title}" if group else title)
    ax.set_xticks([left + width / 2 for left, width in zip(lefts, widths)] + tick_x)
    ax.set_xticklabels(["Group", "Params", "Obj.", "Method", *tick_labels], fontsize=9, fontweight="bold")
    ax.tick_params(axis="x", top=True, bottom=False, labeltop=True, labelbottom=False, length=0, pad=2)
    ax.tick_params(axis="y", length=0)
    y_top = centers[0] - 0.5
    y_bot = centers[-1] + 0.5
    boundaries = [left + width for left, width in zip(lefts, widths)]
    boundaries.extend(data0 + index for index in range(1, len(COLUMNS)))
    for x in boundaries:
        ax.plot(
            [x, x],
            [y_top, y_bot],
            color="white",
            linewidth=2,
            zorder=6,
            solid_capstyle="butt",
        )
    for index in range(len(block) - 1):
        boundary = centers[index] + 0.5
        ax.plot([0, x_end], [boundary, boundary], color="white", linewidth=2, zorder=6, solid_capstyle="butt")
    for i, row in enumerate(block):
        y = centers[i]
        if row["role"] == "parent":
            kind = "parent"
        elif row["role"] == "pretrained":
            kind = "pretrained"
        else:
            kind = row["grouping"]
        ax.add_patch(
            plt.Rectangle((lefts[0], y - 0.5), widths[0], 1.0, facecolor=TYPE_COLOR[kind], edgecolor="none", zorder=4)
        )
        ax.text(
            lefts[0] + widths[0] / 2,
            y,
            TYPE_LETTER[kind],
            ha="center",
            va="center",
            fontsize=8,
            fontweight="bold",
            color=TYPE_LETTER_COLOR[kind],
            zorder=7,
        )
        billions, effective = _param_billions(row)
        ax.add_patch(
            plt.Rectangle(
                (lefts[1], y - 0.5),
                widths[1],
                1.0,
                facecolor=param_cmap(param_norm(billions)),
                edgecolor="none",
                zorder=4,
            )
        )
        ax.text(
            lefts[1] + widths[1] / 2,
            y,
            _param_text(billions, effective),
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            color="white" if param_norm(billions) >= 0.55 else "#1a1a1a",
            zorder=7,
        )
        _code_cell(ax, lefts[2], widths[2], y, row.get("objective_code", ""), OBJ_COLOR, row, "objective")
        _code_cell(ax, lefts[3], widths[3], y, row.get("scope_code", ""), SCOPE_COLOR, row, "method")
        for index, (key, _title, _group) in enumerate(COLUMNS):
            left = data0 + index
            score_column = key in MHB_SCORE_KEYS
            if key.startswith("mhb") and _not_run(row, block):
                ax.add_patch(
                    plt.Rectangle(
                        (left, y - 0.5),
                        1.0,
                        1.0,
                        facecolor=NA_FACE,
                        edgecolor="none",
                        zorder=4,
                    )
                )
                ax.text(
                    left + 0.5,
                    y,
                    "N/A",
                    ha="center",
                    va="center",
                    fontsize=8,
                    fontweight="bold",
                    color=NA_INK,
                    zorder=7,
                )
                continue
            value, text, _star = _cell_value(row, key)
            if value is None:
                color = "#ececec"
                text_color = "#1a1a1a"
            elif score_column:
                color = mhb_cmap(mhb_norm(value))
                text_color = "white" if mhb_norm(value) >= 0.62 else "#1a1a1a"
            else:
                color = cmap(norm(value))
                text_color = "white" if value >= 55 else "#1a1a1a"
            ax.add_patch(
                plt.Rectangle((left, y - 0.5), 1.0, 1.0, facecolor=color, edgecolor="none", zorder=3)
            )
            if text is None:
                continue
            ax.text(
                left + 0.5,
                y,
                text,
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold",
                color=text_color,
                zorder=7,
            )
    labels = []
    for row in block:
        name = _short(row["hf_id"], clashes)
        labels.append(name if row["role"] == "parent" else "    " + name)
    ax.set_yticks(centers)
    ax.set_yticklabels(labels, fontsize=9)
    for tick, row in zip(ax.get_yticklabels(), block):
        if row["role"] == "parent":
            tick.set_fontsize(10)
            tick.set_fontweight("bold")
            tick.set_color("#1a1a1a")
    for spine in ax.spines.values():
        spine.set_color("#dddddd")
    _parsing_banner(ax)


def _parsing_banner(ax) -> None:
    """One line and the word Parsing over the five parse columns."""
    _lefts, _widths, data0 = _meta_layout()
    x0 = data0 + 0.12
    x1 = data0 + PARSE_SPAN - 0.12
    shift = ScaledTranslation(0, 40 / 72, ax.figure.dpi_scale_trans)
    transform = blended_transform_factory(ax.transData, ax.transAxes + shift)
    text_shift = ScaledTranslation(0, 44 / 72, ax.figure.dpi_scale_trans)
    text_transform = blended_transform_factory(ax.transData, ax.transAxes + text_shift)
    ax.plot(
        [x0, x1],
        [1, 1],
        transform=transform,
        color="#1a1a1a",
        linewidth=1.0,
        clip_on=False,
        solid_capstyle="butt",
        zorder=8,
    )
    ax.text(
        (x0 + x1) / 2,
        1,
        "Parsing",
        transform=text_transform,
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold",
        color="#1a1a1a",
        clip_on=False,
        zorder=8,
    )


def _place_version_labels(fig, axes, blocks: list[list[dict]]) -> None:
    """Version line just left of the model names, and an underline on each instruction-tuned name.

    Every panel uses the same x, so v0.2/0.3 and 2 sit on one vertical line.
    """
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    left_px = min(
        tick.get_window_extent(renderer).x0
        for ax in axes
        for tick in ax.get_yticklabels()
    )
    line_x = fig.transFigure.inverted().transform((left_px, 0))[0] - 0.006
    text_x = line_x - 0.012
    for ax, block in zip(axes, blocks):
        labels = ax.get_yticklabels()
        for tick, row in zip(labels, block):
            if row["role"] != "parent":
                continue
            box = tick.get_window_extent(renderer)
            x0, y0 = fig.transFigure.inverted().transform((box.x0, box.y0))
            x1, _y1 = fig.transFigure.inverted().transform((box.x1, box.y0))
            fig.add_artist(
                plt.Line2D(
                    [x0, x1],
                    [y0, y0],
                    transform=fig.transFigure,
                    color="#1a1a1a",
                    linewidth=0.8,
                    solid_capstyle="butt",
                    clip_on=False,
                )
            )
        colors = _version_colors(block)
        for start, end, version in _version_spans(block):
            color = colors[version]
            centers = ax._row_centers
            pad = 0.18
            y_lo = centers[start] - 0.5 + pad
            y_hi = centers[end] + 0.5 - pad
            if y_hi <= y_lo:
                mid = centers[start]
                y_lo, y_hi = mid - 0.32, mid + 0.32
            y0 = fig.transFigure.inverted().transform(ax.transData.transform((0, y_lo)))[1]
            y1 = fig.transFigure.inverted().transform(ax.transData.transform((0, y_hi)))[1]
            fig.add_artist(
                plt.Line2D(
                    [line_x, line_x],
                    [y0, y1],
                    transform=fig.transFigure,
                    color=color,
                    linewidth=6,
                    solid_capstyle="butt",
                    clip_on=False,
                )
            )
            fig.text(
                text_x,
                (y0 + y1) / 2.0,
                VERSION_LABEL[version],
                rotation=90,
                ha="center",
                va="center",
                fontsize=11,
                color=color,
                fontweight="bold",
                clip_on=False,
            )


def _figure_box(spans: list[float]) -> tuple[float, float, list[tuple[float, float, float, float]]]:
    """Figure size in inches, and one axes rectangle per panel, in figure fractions.

    ``spans`` is the data height of each panel, including the full-row gaps.
    """
    axes_w = sum(META_WIDTHS_IN) + len(COLUMNS) * DATA_IN
    label_in = 4.15
    right_in = 1.15
    # Room above the axes for the two-line column labels, the Parsing line, and the title.
    top_in = 1.55
    gap_in = 1.40
    bot_in = 1.30
    fig_w = label_in + axes_w + right_in
    fig_h = top_in + sum(span * ROW_IN for span in spans) + gap_in * (len(spans) - 1) + bot_in
    left = label_in / fig_w
    width = axes_w / fig_w
    y = 1 - top_in / fig_h
    boxes = []
    for span in spans:
        height = span * ROW_IN / fig_h
        y -= height
        boxes.append((left, y, width, height))
        y -= gap_in / fig_h
    return fig_w, fig_h, boxes


def _style_figure(fig, axes, _rows: list[dict], cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm) -> None:
    positions = [ax.get_position() for ax in axes]
    y0 = min(pos.y0 for pos in positions)
    y1 = max(pos.y1 for pos in positions)
    span = y1 - y0
    bar_h = span * 0.36
    gap = span * 0.08
    cax = fig.add_axes([positions[0].x1 + 0.012, y0 + bar_h + gap, 0.012, bar_h])
    scalar = ScalarMappable(norm=norm, cmap=cmap)
    scalar.set_array([])
    fig.colorbar(scalar, cax=cax).set_label("Percentage", fontsize=9)
    mhb_ax = fig.add_axes([positions[0].x1 + 0.012, y0, 0.012, bar_h])
    mhb_scalar = ScalarMappable(norm=mhb_norm, cmap=mhb_cmap)
    mhb_scalar.set_array([])
    mhb_bar = fig.colorbar(mhb_scalar, cax=mhb_ax)
    mhb_bar.set_label("MentalHealthBench", fontsize=9)
    fig_h = fig.get_size_inches()[1]
    param_h = 0.16 / fig_h
    # Fixed inches under the heatmap. A fraction floor pushed this bar into the
    # Qwen panel, whose axes already sit close to the bottom of a tall figure.
    param_y = y0 - (0.36 / fig_h) - param_h
    pax = fig.add_axes([0.015, param_y, 0.15, param_h])
    param_scalar = ScalarMappable(norm=param_norm, cmap=param_cmap)
    param_scalar.set_array([])
    param_bar = fig.colorbar(param_scalar, cax=pax, orientation="horizontal")
    param_bar.set_label("Parameters (Bn)", fontsize=9)
    top = float(param_norm.vmax)
    step = 8.0 if top >= 16 else 1.0
    ticks = list(np.arange(0.0, top, step))
    if not ticks or abs(ticks[-1] - top) > 1e-6:
        ticks.append(top)
    param_bar.set_ticks(ticks)
    param_bar.set_ticklabels([f"{tick:.3f}".rstrip("0").rstrip(".") for tick in ticks])
    handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor=TYPE_COLOR[key], edgecolor="none", label=label)
        for key, label in type_legend()
    ]
    handles.append(
        plt.Rectangle(
            (0, 0),
            1,
            1,
            facecolor=NA_FACE,
            edgecolor="none",
            label="N/A",
        )
    )
    fig.legend(
        handles=handles,
        loc="lower left",
        bbox_to_anchor=(0.18, 0.28 / fig_h),
        ncol=6,
        frameon=False,
        fontsize=10,
        handlelength=1.4,
        handleheight=1.0,
        borderaxespad=0.0,
    )


def _cmaps(param_max: float, mhb_max: float):
    cmap = plt.cm.Blues.copy()
    cmap.set_bad("#ececec")
    norm = Normalize(vmin=0, vmax=100)
    param_cmap = plt.cm.Oranges.copy()
    param_norm = Normalize(vmin=0, vmax=param_max)
    mhb_cmap = plt.cm.YlGnBu.copy()
    mhb_cmap.set_bad("#ececec")
    mhb_norm = Normalize(vmin=0, vmax=mhb_max)
    return cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm


def _mhb_scale_max(records: list[dict]) -> float:
    """Top of the MentalHealthBench color bar. Shared across the four figures."""
    values = []
    for row in records:
        score = row["scores"]["mhb"]
        if not score:
            continue
        plotted = {
            "mhb86": "safety86",
            "mhb_total": "total",
            "mhb_pos": "positive",
            "mhb_pen": "penalty",
        }
        shown = [plotted[key] for key, _title, _group in COLUMNS if key in plotted]
        values.extend(100.0 * score[field] for field in shown if field in score)
    if not values:
        return 100.0
    top = max(values)
    return max(10.0, float(np.ceil(top / 10.0) * 10.0))


def draw_family(family: str, rows: list[dict], png: Path, param_max: float, mhb_max: float) -> None:
    block = _one_parent_block(rows)
    clashes = _collisions(block)
    cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm = _cmaps(param_max, mhb_max)
    fig_w, fig_h, boxes = _figure_box([_block_span(block)])
    fig = plt.figure(figsize=(fig_w, fig_h))
    ax = fig.add_axes(boxes[0])
    _paint(ax, block, clashes, cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm)
    ax.set_title(family, fontsize=14, loc="left", pad=64, fontweight="bold")
    _style_figure(fig, [ax], rows, cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm)
    _place_version_labels(fig, [ax], [block])
    fig.savefig(png, dpi=300)
    plt.close(fig)


def draw_two_families(
    first: tuple[str, list[dict]], second: tuple[str, list[dict]], png: Path, param_max: float, mhb_max: float
) -> None:
    sections = []
    for name, rows in (first, second):
        sections.append((name, _one_parent_block(rows), rows))
    clashes = _collisions([row for _name, block, _rows in sections for row in block])
    cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm = _cmaps(param_max, mhb_max)
    fig_w, fig_h, boxes = _figure_box([_block_span(block) for _name, block, _rows in sections])
    fig = plt.figure(figsize=(fig_w, fig_h))
    drawn = []
    for box, (name, block, _rows) in zip(boxes, sections):
        ax = fig.add_axes(box)
        _paint(ax, block, clashes, cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm)
        ax.set_title(name, fontsize=14, loc="left", pad=64, fontweight="bold")
        drawn.append(ax)
    all_rows = sections[0][2] + sections[1][2]
    _style_figure(fig, drawn, all_rows, cmap, norm, param_cmap, param_norm, mhb_cmap, mhb_norm)
    _place_version_labels(fig, drawn, [block for _name, block, _rows in sections])
    fig.savefig(png, dpi=300)
    plt.close(fig)


def _attach_objectives(records: list[dict]) -> None:
    """Code for the training objective, from the roster column training_objective_stages.

    One stage is SFT, GRPO, DPO, or DIST. More than one stage is MULT.
    Instruction-tuned and pretrained rows are N/A. A fine-tune with a blank or
    unknown stage stops the run; the roster is the only source.
    """
    for row in records:
        if row["role"] != "fine-tune":
            row["objective_code"] = "N/A"
            continue
        stages = (row.get("training_objective_stages") or "").strip()
        parts = [part for part in stages.split("|") if part]
        if not parts:
            raise SystemExit(f"{row['hf_id']}: training_objective_stages is blank on the roster")
        if len(parts) > 1:
            row["objective_code"] = "MULT"
        elif parts[0] in OBJ_FROM_STAGE:
            row["objective_code"] = OBJ_FROM_STAGE[parts[0]]
        else:
            raise SystemExit(f"{row['hf_id']} training_objective_stages {stages!r} is not a known code")


def _attach_scope(records: list[dict]) -> None:
    """Which weights changed, from the roster column training_method.

    QLoRA and LoRA are one cell, Q/LoRA. A roster value of "not stated" with a
    lora or qlora token in the repo name is Q/LoRA (study_roster.scope_marker,
    the step-5 name rule). Anything else not stated is Unstated.
    Instruction-tuned and pretrained rows are N/A. A fine-tune whose
    training_method is not a known value stops the run.
    """
    from orchestration.study_roster import scope_marker

    for row in records:
        if row["role"] != "fine-tune":
            row["scope_code"] = "N/A"
            continue
        method = (row.get("training_method") or "").strip()
        code = scope_marker(method, row["hf_id"])
        if code is None:
            raise SystemExit(f"{row['hf_id']}: training_method {method!r} on the roster is not a known value")
        row["scope_code"] = code


def _attach_mhb86_parse(records: list[dict]) -> None:
    """The drawn MentalHealthBench parse rate is nonempty replies among the 86.

    The roster rate is nonempty replies among all 1,215. That count stays on
    the roster. The figure reads the 86 from the generation files.
    """
    bench = _mentalhealthbench()
    for row in records:
        rate = row["rates"]["mentalhealthbench"]
        if rate is None:
            continue
        hit = bench.get(row["hf_id"])
        if hit is None or "n86" not in hit:
            raise SystemExit(f"{row['hf_id']}: no 86-conversation parse count in {row['rates']['mentalhealthbench'].get('path', 'the generation file')}")
        rate["n86"] = hit["n86"]
        rate["n_parsed86"] = hit["n_parsed86"]


def main() -> None:
    from orchestration.study_roster import plot_records

    records = plot_records()
    _attach_mhb86_parse(records)
    _attach_objectives(records)
    _attach_scope(records)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    old = OUT_DIR / "parse-rates.png"
    if old.is_file():
        old.unlink()
    families = []
    for row in records:
        if row["family"] not in families:
            families.append(row["family"])
    families.sort(key=_family_key)
    by_family = {family: [row for row in records if row["family"] == family] for family in families}
    param_max = max(_param_billions(row)[0] for row in records)
    mhb_max = _mhb_scale_max(records)
    for family in families:
        if family in ("Mistral", "SmolLM"):
            continue
        png = OUT_DIR / f"performance_parameters_{family.lower()}.png"
        draw_family(family, by_family[family], png, param_max, mhb_max)
        print(f"wrote {png}")
    combined = OUT_DIR / "performance_parameters_mistral-smollm.png"
    draw_two_families(
        ("Mistral", by_family["Mistral"]), ("SmolLM", by_family["SmolLM"]), combined, param_max, mhb_max
    )
    print(f"wrote {combined}")
    for stale in (
        "parse-rates.png",
        "parse-rates-gemma.png",
        "parse-rates-llama.png",
        "parse-rates-qwen.png",
        "parse-rates-mistral.png",
        "parse-rates-smollm.png",
        "parse-rates-mistral-smollm.png",
    ):
        path = OUT_DIR / stale
        if path.is_file():
            path.unlink()


if __name__ == "__main__":
    main()
