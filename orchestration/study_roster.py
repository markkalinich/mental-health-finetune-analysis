"""The study roster: one dated CSV named by outputs/roster/CURRENT.

Plots read this file. They do not apply a second membership list.

DRAW_PRETRAINED gates the manuscript figures only. The roster still holds
every pretrained checkpoint. Set it to True to draw those checkpoints again.
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROSTER_ROOT = REPO / "outputs/roster"
POINTER = ROSTER_ROOT / "CURRENT"

# Manuscript figures omit pretrained checkpoints (24 Oct 2026). They stay on
# the roster. True draws them again on Figure 1, Figure 3, Figure 4, S4, and S5–S8.
DRAW_PRETRAINED = False

# MHB-Safety comparisons keep a mental-health or medical fine-tune, and an
# instruction-tuned parent only when one of those fine-tunes names it (31 Oct 2026).
MHB_COMPARISON_GROUPINGS = ("mental-health", "medical")

COLUMNS = [
    "grouping",
    "role",
    "hf_id",
    "hf_url",
    "family",
    "version",
    "size",
    "training_objective",
    "training_objective_stages",
    "training_method",
    "dataset_source",
    "datasets",
    "dataset_urls",
    "dataset_quote",
    "dataset_quote_url",
    "dataset_hub_status",
    "output_type",
    "use_claim",
    "claim_quote",
    "warning_strength",
    "warning_quote",
    "detection_quote",
    "description",
    "card_file",
    "dtype_codes",
    "weights_format",
    "parent_id",
    "pretrained_id",
    "named_by_groupings",
    "si_n",
    "si_strict_parsed",
    "si_sonnet_answered_yes",
    "si_sonnet_answered_no",
    "si_sonnet_not_an_answer",
    "si_sonnet_unlabeled",
    "si_sensitivity",
    "si_specificity",
    "si_f1",
    "cssrs_n",
    "cssrs_strict_parsed",
    "cssrs_sonnet_answered_yes",
    "cssrs_sonnet_answered_no",
    "cssrs_sonnet_not_an_answer",
    "cssrs_sonnet_unlabeled",
    "cssrs_sensitivity",
    "cssrs_specificity",
    "cssrs_f1",
    "mhb_n",
    "mhb_n_parsed",
    "mhb_safety",
    "mhb_total",
]

SCOPE_MARKER = {"full": "Full", "lora": "Q/LoRA", "qlora": "Q/LoRA", "not stated": "Unstated"}


def roster_date() -> str:
    if not POINTER.is_file():
        raise FileNotFoundError(f"{POINTER} does not exist")
    text = POINTER.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"{POINTER} is empty")
    return text


def roster_csv() -> Path:
    return ROSTER_ROOT / roster_date() / "roster.csv"


def for_analysis(rows: list[dict]) -> list[dict]:
    """One row per model. The listed parent_id is not rewritten.

    joint_and_paired.REHOST_OF names two Unsloth copies of Google models.
    A fine-tune that lists the Unsloth repo as its parent keeps that parent_id.
    The copy is not a second instruction-tuned model: this drops those two rows.
    The Google row is the one that remains. A copy with no Google row stops the run.
    The roster file is not changed.
    """
    from orchestration.joint_and_paired import REHOST_OF

    copied = [dict(row) for row in rows]
    ids = {row["hf_id"] for row in copied}
    missing = [canonical for _rehost, canonical in REHOST_OF.items() if canonical not in ids]
    if missing:
        raise SystemExit(f"Google model named as the collapsed checkpoint is not on the roster: {missing}")
    return [row for row in copied if row["hf_id"] not in REHOST_OF]


def load_roster(path: Path | None = None) -> list[dict]:
    csv_path = path or roster_csv()
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    missing = [name for name in COLUMNS if name not in (rows[0] if rows else {})]
    if rows and missing:
        raise SystemExit(f"{csv_path} is missing columns: {missing}")
    import os

    if os.environ.get("MANUSCRIPT_LABELED") == "1":
        rows = [row for row in rows if row["role"] != "fine-tune" or labeled_fine_tune(row)]
    return rows


def method_code(row: dict) -> str:
    """LoRA, QLoRA, Full, or Unstated.

    QLoRA and LoRA stay separate. The figure marker still joins them as Q/LoRA.
    A repo-name token supplies the method only when the roster cell is not stated.
    """
    method = (row.get("training_method") or "").strip().lower()
    if method in ("qlora", "lora", "full"):
        return {"qlora": "QLoRA", "lora": "LoRA", "full": "Full"}[method]
    if method == "not stated":
        from model_selection.rules import methods_in_name

        found = methods_in_name(row.get("hf_id") or "")
        if "qlora" in found:
            return "QLoRA"
        if "lora" in found:
            return "LoRA"
    return "Unstated"


def objective_code(row: dict) -> str:
    """One training objective, or 'More than one stage' when the roster lists several."""
    stages = [part for part in (row.get("training_objective_stages") or "").split("|") if part]
    if len(stages) > 1:
        return "More than one stage"
    names = {"sft": "SFT", "grpo": "GRPO", "dpo": "DPO", "distillation": "Distillation"}
    if len(stages) == 1 and stages[0] in names:
        return names[stages[0]]
    return ""


def parents_on_mhb_safety(children: list[tuple[str, str]]) -> set[str]:
    """Parent ids a mental-health or medical fine-tune brings onto MHB-Safety.

    children is (parent_id, grouping) for every fine-tune in the sample.
    A safety fine-tune does not bring its parent in.
    """
    brought: set[str] = set()
    for parent_id, grouping in children:
        if grouping not in {"mental-health", "medical", "safety"}:
            raise SystemExit(f"fine-tune grouping {grouping!r} is not mental-health, medical, or safety")
        if grouping not in MHB_COMPARISON_GROUPINGS:
            continue
        if not parent_id:
            raise SystemExit("a mental-health or medical fine-tune has no parent id")
        brought.add(parent_id)
    if not brought:
        raise SystemExit("no mental-health or medical fine-tune names a parent for MHB-Safety")
    return brought


def on_mhb_safety(row: dict, brought: set[str]) -> bool:
    """Whether this roster row enters an MHB-Safety comparison.

    Safety fine-tunes do not. An instruction-tuned parent does when brought
    contains its checkpoint, including an Unsloth copy of that checkpoint.
    Pretrained checkpoints do not.
    """
    from orchestration.joint_and_paired import canonical_checkpoint

    if row["role"] == "fine-tune":
        if row["grouping"] not in {"mental-health", "medical", "safety"}:
            raise SystemExit(f"{row['hf_id']} grouping {row['grouping']!r} is not a study fine-tune")
        return row["grouping"] in MHB_COMPARISON_GROUPINGS
    if row["role"] == "instruction parent":
        return canonical_checkpoint(row["hf_id"]) in brought
    if row["role"] == "pretrained":
        return False
    raise SystemExit(f"{row['hf_id']} role {row['role']!r} is not on the roster")


def mhb_safety_ids(rows: list[dict]) -> set[str]:
    """Roster hf_ids that enter an MHB-Safety comparison."""
    brought = parents_on_mhb_safety(
        [(row["parent_id"], row["grouping"]) for row in rows if row["role"] == "fine-tune"]
    )
    return {row["hf_id"] for row in rows if on_mhb_safety(row, brought)}


def labeled_fine_tune(row: dict) -> bool:
    """Both the weight-update method and the training objective are known."""
    return row.get("role") == "fine-tune" and method_code(row) != "Unstated" and bool(objective_code(row))


def scope_marker(update_scope: str, hf_id: str = "") -> str | None:
    """Figure marker for a roster update_scope.

    The agent file keeps "not stated" when the search prompt forbade using the
    repo name. A lora or qlora token in the name is the same step-5 rule the
    family figure applies, so that row is Q/LoRA here too.
    """
    if update_scope == "not stated" and hf_id:
        from model_selection.rules import methods_in_name

        found = methods_in_name(hf_id)
        if "qlora" in found or "lora" in found:
            return "Q/LoRA"
    return SCOPE_MARKER.get(update_scope)


def _blank(text: str) -> bool:
    return text is None or text == ""


def _yesno_rate(row: dict, prefix: str) -> dict | None:
    if _blank(row[f"{prefix}_n"]):
        return None
    n = int(row[f"{prefix}_n"])
    n_parsed = int(row[f"{prefix}_strict_parsed"])
    rate = {
        "n": n,
        "n_parsed": n_parsed,
        "card_format": False,
        "sonnet": True,
        "source": "roster",
        "path": "roster.csv",
    }
    if n and _blank(row[f"{prefix}_sonnet_unlabeled"]) is False and int(row[f"{prefix}_sonnet_unlabeled"]) == 0:
        not_an_answer = int(row[f"{prefix}_sonnet_not_an_answer"])
        rate["strict"] = n_parsed / n
        rate["recovered"] = (n - not_an_answer) / n
    return rate


def _yesno_score(row: dict, prefix: str) -> dict | None:
    if _blank(row[f"{prefix}_f1"]):
        return None
    return {
        "sens": float(row[f"{prefix}_sensitivity"]),
        "spec": float(row[f"{prefix}_specificity"]),
        "f1": float(row[f"{prefix}_f1"]),
    }


def _mhb_rate(row: dict) -> dict | None:
    if _blank(row["mhb_n"]):
        return None
    return {
        "n": int(row["mhb_n"]),
        "n_parsed": int(row["mhb_n_parsed"]),
        "card_format": False,
        "sonnet": False,
        "source": "roster",
        "path": "roster.csv",
    }


def _mhb_score(row: dict) -> dict | None:
    """English suicide and self-harm score, and the full-bench score."""
    if _blank(row["mhb_safety"]) and _blank(row["mhb_total"]):
        return None
    if _blank(row["mhb_safety"]) or _blank(row["mhb_total"]):
        raise SystemExit(f"{row['hf_id']}: mhb_safety and mhb_total must both be filled or both blank")
    return {"total": float(row["mhb_total"]), "safety86": float(row["mhb_safety"])}


def _plot_row(row: dict, role: str, parent: str, grouping: str) -> dict:
    return {
        "grouping": grouping,
        "role": role,
        "hf_id": row["hf_id"],
        "parent": parent,
        "family": row["family"],
        "version": row["version"],
        "size": row["size"],
        "training_method": row["training_method"],
        "training_objective_stages": row.get("training_objective_stages") or "",
        "rates": {
            "synthetic_si": _yesno_rate(row, "si"),
            "cssrs": _yesno_rate(row, "cssrs"),
            "mentalhealthbench": _mhb_rate(row),
        },
        "scores": {
            "synthetic_si": _yesno_score(row, "si"),
            "cssrs": _yesno_score(row, "cssrs"),
            "mhb": _mhb_score(row),
        },
    }


def plot_records(rows: list[dict] | None = None) -> list[dict]:
    """Drawing records. Instruction parents use role 'parent', which the figures already switch on.

    A pretrained checkpoint that several instruction-tuned models share stays one
    roster row. When DRAW_PRETRAINED is true, this emits one drawing record
    under each of those models. A named base that is missing from the roster
    still stops the run.
    """
    from orchestration.joint_and_paired import REHOST_OF, canonical_checkpoint

    source = list(rows) if rows is not None else load_roster()
    ancestors = {row["hf_id"]: row for row in source if row["role"] != "fine-tune"}
    records = []
    for row in source:
        if row["role"] == "fine-tune":
            # The listed parent stays parent_id on the roster. The drawing
            # block is the collapsed checkpoint, so an Unsloth copy and the
            # Google model are not two instruction-tuned rows.
            records.append(_plot_row(row, "fine-tune", canonical_checkpoint(row["parent_id"]), row["grouping"]))
            continue
        if row["role"] != "instruction parent" or row["hf_id"] in REHOST_OF:
            continue
        records.append(_plot_row(row, "parent", row["hf_id"], ""))
        base_id = row["pretrained_id"]
        if not base_id:
            continue
        base = ancestors.get(base_id)
        if base is None:
            raise SystemExit(f"{row['hf_id']} pretrained id {base_id} has no roster row")
        if DRAW_PRETRAINED:
            records.append(_plot_row(base, "pretrained", row["hf_id"], ""))
    return records
