"""Draw one grouping's funnel from outputs/funnel/<grouping>/<view>/counts.csv.

    .venv/bin/python model_selection/figure.py --grouping mental-health --as-of 2026-10-05
    .venv/bin/python model_selection/figure.py --grouping mental-health --as-of 2026-10-06 --relax dataset

Every number is read from counts.csv (written by funnel.py); nothing is typed in. The script checks
that each step's kept + losses equals what entered it and exits 1 otherwise. Writes
funnel.png into the same results folder. SVG output is paused. Steps follow funnel.py: 1 full precision, 2 text-capable
with a dataset stated, 3 one full-precision instruction parent whose config.json the model matches,
4 pass manual review (the endpoint: thick border, light fill), 5 fine-tuning method stated
(a sensitivity cut drawn below the endpoint). The title prints the real date range of the Hub
data the run used (provenance.csv), not the --as-of view date alone. Since 13 Oct 2026 the figure draws
the keyword search as its own first box and steps 5 and 6 as one box (MERGED_IN_FIGURE); counts.csv and
the count table in how-models-are-filtered.md keep all six steps. Safety and medical draw one more box,
"Final model list". It is the set the study scores. Safety stays when the card states a prompt and a
label and that label parsed. A model manual review moved in from another search is drawn
on that box as an addition, so the last count is the study list. Medical stays when a mental-health model has the same family and
version. There is no separate family-and-version box. Counts are read from those lists. Mental health
does not draw the box. The training-method box is then retitled and reduced to the models whose training
objective and fine-tuning method are both stated. For mental health that box is
the last box. A model the study list places in another grouping is removed from
that box, with its own removal line. For medical and safety it is the box before the final list, and the
final list only removes models that have nothing to map onto. The fine-tuning
method is QLoRA, LoRA, or full in agent_methods.csv, or a lora/qlora token in the
repo name when that file says not stated (the same name rule as rules.methods_in_name).
counts.csv is not changed.
"""
from __future__ import annotations

import argparse
import csv
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

import cache  # noqa: E402

RESULTS = cache.RESULTS

# Box label per step (Mark's wording, 13 Oct 2026 15:25-16:05: a figure carries few words; the definitions
# go to the supplementary methods) and a plain-language label per loss reason (decision value in decisions.csv).
BOX = {
    "1": "16- or 32-bit text-compatible\nmodel weights available",
    "2": "Training dataset specified",
    "3": "One full-precision,\ninstruction-tuned parent",
    "4": "AI-assisted manual review",
    "5": "Fine-tuning method named",
    "6": "Training method documented\nby the model author",
}
SEARCH_BOX = "Queried Hugging Face API\nfor models of interest"
# Steps 5 and 6 stay two steps in funnel.py and counts.csv (method word found; objective evidence at level 1-2).
# The figure draws them as one box labelled BOX["6"]; the table in how-models-are-filtered.md keeps both steps.
MERGED_IN_FIGURE = ("5", "6")
# One removal line in that box for two rules: no method word anywhere (step 5), and a method named but not
# whether training was full or LoRA (add_scope_box). Mark, 24 Oct 2026.
METHOD_UNDOCUMENTED = "training method not documented (none named, or full vs LoRA not stated)"
STEPS = ("1", "2", "3", "4", "5", "6")
# The thick border inside the funnel steps is step 6 (kept.csv) for every grouping.
# Safety and medical then draw one more box, from version_rule.py, and that box takes the thick border.
# Mental health does not: the rule never removes a mental-health model. kept.csv stays the step-6 list.
ENDPOINT_BY_GROUPING = {"mental-health": "6", "safety": "6", "medical": "6"}
VERSION_RULE_GROUPINGS = ("safety", "medical")
FINAL_BOX = "Final model list"
VERSION_RULE_LOSS = "family and version has no mental-health fine-tune"
DEFAULT_ENDPOINT = "4"


def endpoint(grouping: str) -> str:
    return ENDPOINT_BY_GROUPING.get(grouping, DEFAULT_ENDPOINT)


ENDPOINT_FILL = "#ede7f6"
LOSS = {
    "no_root": "no Hugging Face-format checkpoint at the repo root (adapter-only, GGUF-only, subfolder, or no weights)",
    "repository_unreadable": "repository not readable",
    "redundant_kept": "redundant with a kept model",
    "not_conversational": "Not a conversational model",
    "incomplete_or_nonfunctional": "Incomplete training or nonfunctional model",
    "not_instruction_tuned": "Not instruction tuned",
    "not_safety_model": "not a safety model",
    "not_functional_here": "Not functional on this machine",
    "not_appropriate_medical": "not appropriate medical model",
    "blank_record": "weights file listed but its dtype record is blank",
    "other_dtype": "quantized weights (U8, I8, I32, F8, ...)",
    "row_unreadable": "card could not be read",
    "bin_unreadable": "pytorch_model.bin header could not be read",
    "vision_or_video": "vision or video pipeline",
    "no_training_method": "fine-tuning method not stated by the model author",
    "no_objective_evidence": "training objective not yet read for this model (no row in objective-evidence.csv)",
    "objective_assumed_only": "training objective not stated by the model author",
    "no_dataset": "no dataset named",
    "dataset_not_on_hub": "named dataset is not on the Hub",
    "no_parent": "no parent model named",
    "multiple_parents": "two or more parent models named",
    "parent_not_fp": "no available full-precision parent model",
    "parent_unreadable": "parent model could not be read",
    "parent_pretrained": "parent model is pre-trained",
    "parent_finetune": "parent model is also a fine-tune",
    "parent_not_stated": "parent model does not say instruction-tuned, pre-trained, or fine-tune",
    "parent_card_unreadable": "parent card could not be read",
    "parent_conflict": "parent model says both a fine-tune and instruction-tuned",
    "parent_not_language_model": "parent is a speech, vision, or embedding model",
    "zero_downloads": "zero lifetime downloads",
    "downloads_missing": "downloads field missing",
    "parent_discordant": "config.json differs from the declared parent's (architecture or shape)",
    "config_unreadable": "config.json absent or not readable (model or parent)",
    "repo_gated": "gated or private repo; access not yet approved (can be requested)",
    "manual_removed": "removed after a person read the card (manual_removals.csv)",
}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def comma(n: int) -> str:
    return f"{n:,}"


def loss_label(outcome: str) -> str:
    """Plain-language line for one counts.csv loss. Category removals and cache misses
    are prefixes, so a new category does not need its own entry in LOSS."""
    if outcome in LOSS:
        return LOSS[outcome]
    if outcome.startswith("manual_removed: "):
        return outcome[len("manual_removed: "):]
    return outcome.replace("missing:", "not in cache: ", 1)


def version_rule_rows() -> list:
    """Rows of the version-rule kept list in outputs/cross-grouping/CURRENT (written by version_rule.py)."""
    import version_rule

    final_path = version_rule.current_file(version_rule.KEPT_NAME)
    if not final_path.is_file():
        fail(f"version rule file missing: {final_path}")
    with final_path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def version_rule_split(grouping: str) -> tuple:
    """How many of this grouping the version rule keeps and removes."""
    import version_rule

    removed_path = version_rule.current_file(version_rule.REMOVED_NAME)
    if not removed_path.is_file():
        fail(f"version rule file missing: {removed_path}")
    kept_ids = [row["hf_id"] for row in version_rule_rows() if row["grouping"] == grouping]
    removed_n = 0
    with removed_path.open(newline="") as fh:
        for row in csv.DictReader(fh):
            if row["grouping"] == grouping:
                removed_n += 1
    return kept_ids, removed_n


def study_split(grouping: str, kept_ids: list) -> tuple:
    """The models from the version-rule list that the study scores.

    Safety: the card states a prompt and a label, and that label parsed
    (USABLE_IDS in safety_labels/cohort.py). Medical: every model on the
    version-rule list; the final list is drawn by add_scope_box.
    """
    if grouping == "safety":
        repo = Path(__file__).resolve().parents[1]
        if str(repo) not in sys.path:
            sys.path.insert(0, str(repo))
        from safety_labels.cohort import COHORT, USABLE_IDS

        stated = {spec.hf_id for spec in COHORT}
        usable = set(USABLE_IDS)
        missing = sorted(usable.difference(kept_ids))
        if missing:
            fail(f"usable safety models missing from the version-rule list: {missing}")
        no_card = sum(1 for hf_id in kept_ids if hf_id not in stated)
        no_parse = sum(1 for hf_id in kept_ids if hf_id in stated and hf_id not in usable)
        stayed = sum(1 for hf_id in kept_ids if hf_id in usable)
        return stayed, [
            ("card has no prompt and label to score", no_card),
            ("did not produce the label the card names", no_parse),
        ], FINAL_BOX
    if grouping == "medical":
        # A medical model stays when a mental-health model shares its family and version (Mark, 24 Oct 2026);
        # there is no size match. add_scope_box draws the medical final list from _mapping_losses.
        return len(kept_ids), [], FINAL_BOX
    fail(f"no study split for {grouping}")


def load_counts(path: Path) -> dict:
    """{step: {outcome: n}} from counts.csv."""
    out: dict = {}
    with path.open(newline="") as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["step"], {})[r["outcome"]] = int(r["n"])
    return out


def data_dates(provenance_path: Path) -> str:
    """' (Hub data fetched 2026-09-24 to 2026-10-08)' from provenance.csv, or '' when the file is absent.
    The --as-of date is a cutoff; the cache entries it selects can be older. Say so on the figure."""
    if not provenance_path.exists():
        return ""
    lo, hi = [], []
    with provenance_path.open(newline="") as fh:
        for r in csv.DictReader(fh):
            lo.append(r["date_min"])
            hi.append(r["date_max"])
    if not lo:
        return ""
    return f" (Hub data fetched {min(lo)} to {max(hi)})"


UNREADABLE = {
    "bin_unreadable",
    "row_unreadable",
    "repo_gated",
    "parent_unreadable",
    "parent_card_unreadable",
    "config_unreadable",
}
REDUNDANT = (
    "manual_removed: redundant with a kept model",
    "manual_removed: one of 11 variants",
    "manual_removed: earlier version of a kept model",
    "manual_removed: earlier stage of a kept model",
    "manual_removed: duplicate of a kept model",
)
INCOMPLETE = (
    "manual_removed: cannot be served:",
    "manual_removed: card says training is incomplete",
)
NOT_CONVERSATIONAL = "manual_removed: scorer, not a conversational model"
NOT_INSTRUCTION = "manual_removed: continued pre-training only, no instruction tuning"
NOT_SAFETY = (
    "manual_removed: not a safety model",
    "manual_removed: backdoor research organism, not a safety model",
    "manual_removed: refusal removal, not a safety model",
)
NOT_FUNCTIONAL = (
    "manual_removed: needs another model's token probabilities as input",
    "manual_removed: weights do not fit on the 96 GB GPU",
)
BAD_ADVICE = "manual_removed: set aside as a control: trained to give bad medical advice"
SIDE_EXPERIMENT = "manual_removed: set aside: weights kept for a side experiment, not in the main cohort"
LINE_WIDTH = 78


def display_key(outcome: str) -> str:
    if outcome in UNREADABLE:
        return "repository_unreadable"
    if outcome == NOT_CONVERSATIONAL:
        return "not_conversational"
    if outcome == NOT_INSTRUCTION:
        return "not_instruction_tuned"
    if outcome in NOT_SAFETY:
        return "not_safety_model"
    if outcome in NOT_FUNCTIONAL:
        return "not_functional_here"
    if outcome in (BAD_ADVICE, SIDE_EXPERIMENT):
        return "not_appropriate_medical"
    if outcome.startswith(INCOMPLETE):
        return "incomplete_or_nonfunctional"
    if outcome.startswith(REDUNDANT):
        return "redundant_kept"
    return outcome


def display_pairs(losses: dict) -> list:
    """Sum reasons that the figure shows as one line. counts.csv is unchanged."""
    totals: dict = {}
    for outcome, n in losses.items():
        if not n:
            continue
        key = display_key(outcome)
        totals[key] = totals.get(key, 0) + n
    return [(loss_label(key), n) for key, n in totals.items()]


def numbered(pairs: list) -> tuple:
    kept = sorted(((label, n) for label, n in pairs if n), key=lambda item: (-item[1], item[0]))
    lines = []
    for i, (label, n) in enumerate(kept, 1):
        text = f"{i}.  {comma(n)}  {label}"
        lines.extend(textwrap.wrap(text, width=LINE_WIDTH, subsequent_indent="       ") or [text])
    return lines, sum(n for _l, n in kept)


def rows_for(counts: dict, grouping: str) -> list:
    """One (label, count, loss lines, removed, is_endpoint) per drawn box, checking the arithmetic per step.
    Box 0 is the keyword search (cohort out of listed_on_hub); steps in MERGED_IN_FIGURE share one box."""
    step0 = counts.get("0", {})
    cohort = step0.get("cohort")
    if cohort is None:
        fail("counts.csv has no step 0 cohort row")
    drawn = []
    if "listed_on_hub" in step0:
        lines, removed = numbered([("not keyword-matched", step0["listed_on_hub"] - cohort)])
        drawn.append((SEARCH_BOX, comma(cohort), lines, removed, False))
    entered_expected = cohort
    merged_losses: dict = {}
    step1_entered = None
    step1_losses: dict = {}
    for step in STEPS:
        c = counts.get(step)
        if c is None:
            fail(f"counts.csv has no rows for step {step}")
        entered, kept = c["entered"], c["kept"]
        if entered != entered_expected:
            fail(f"step {step}: entered {entered} != previous kept {entered_expected}")
        losses = {k: v for k, v in c.items() if k not in ("entered", "kept")}
        unknown = sorted(
            k for k in losses
            if k not in LOSS and not k.startswith("missing:") and not k.startswith("manual_removed: ")
        )
        if unknown:
            fail(f"step {step}: no label for loss reason(s) {unknown}; add them to LOSS in figure.py")
        if kept + sum(losses.values()) != entered:
            fail(f"step {step}: {kept} + {sum(losses.values())} != {entered}")
        entered_expected = kept
        if step == "1":
            step1_entered = entered
            step1_losses = dict(losses)
            continue
        if step == "2":
            if step1_entered is None:
                fail("step 2 drawn before step 1")
            vision_n = losses.get("vision_or_video", 0)
            text_kept = entered - vision_n
            weight = dict(step1_losses)
            if vision_n:
                weight["vision_or_video"] = vision_n
            lines, removed = numbered(display_pairs(weight))
            if text_kept + removed != step1_entered:
                fail(f"text-compatible box {text_kept} + {removed} != {step1_entered}")
            drawn.append((BOX["1"], comma(text_kept), lines, removed, False))
            dataset = {k: v for k, v in losses.items() if k != "vision_or_video"}
            lines, removed = numbered(display_pairs(dataset))
            if kept + removed != text_kept:
                fail(f"dataset box {kept} + {removed} != {text_kept}")
            drawn.append((BOX["2"], comma(kept), lines, removed, False))
            continue
        if step in MERGED_IN_FIGURE:
            for key, n in losses.items():
                merged_losses[key] = merged_losses.get(key, 0) + n
            if step != MERGED_IN_FIGURE[-1]:
                continue
            pairs = [
                (METHOD_UNDOCUMENTED if label == LOSS["no_training_method"] else label, n)
                for label, n in display_pairs(merged_losses)
            ]
            is_end = endpoint(grouping) in MERGED_IN_FIGURE
        else:
            pairs = display_pairs(losses)
            is_end = step == endpoint(grouping)
        lines, removed = numbered(pairs)
        drawn.append((BOX[step], comma(kept), lines, removed, is_end))
    if grouping in VERSION_RULE_GROUPINGS:
        kept_ids, removed_n = version_rule_split(grouping)
        if len(kept_ids) + removed_n != entered_expected:
            fail(
                f"{grouping}: version rule keeps {len(kept_ids)} and removes {removed_n}, "
                f"which is not the {entered_expected} models that finished step 6"
            )
        label, count, lines, removed, _end = drawn[-1]
        drawn[-1] = (label, count, lines, removed, False)
        study_n, study_losses, study_label = study_split(grouping, kept_ids)
        pairs = [(VERSION_RULE_LOSS, removed_n), *study_losses]
        if study_n + sum(n for _reason, n in pairs) != entered_expected:
            fail(f"{grouping}: final list does not account for the {entered_expected} models that finished step 6")
        lines, removed = numbered(pairs)
        drawn.append((study_label, comma(study_n), lines, removed, True))
    return drawn


SCOPE_LOSS = METHOD_UNDOCUMENTED
OTHER_METHOD_LOSS = "fine-tuning method is not full or LoRA"
OBJECTIVE_LOSS = "training objective not stated by the model author"
METHOD_BOX = "Training objective\nand fine-tuning method\nboth stated by the model author"


def _plain_count(text: str) -> int:
    return int(text.replace(",", ""))


def _endpoint_ids(grouping: str, kept_csv: Path) -> list[str]:
    """Models in the thick-bordered box, before the weight-update box."""
    if grouping == "mental-health":
        with kept_csv.open(newline="", encoding="utf-8") as handle:
            return [row["hf_id"] for row in csv.DictReader(handle)]
    if grouping == "safety":
        repo = Path(__file__).resolve().parents[1]
        if str(repo) not in sys.path:
            sys.path.insert(0, str(repo))
        from safety_labels.cohort import USABLE_IDS

        kept_ids, _removed = version_rule_split("safety")
        usable = set(USABLE_IDS)
        return [hf_id for hf_id in kept_ids if hf_id in usable]
    if grouping == "medical":
        cells = {
            (row["family"], row["version"])
            for row in version_rule_rows()
            if row["grouping"] == "mental-health"
        }
        return [
            row["hf_id"]
            for row in version_rule_rows()
            if row["grouping"] == "medical" and (row["family"], row["version"]) in cells
        ]
    fail(f"no endpoint list for {grouping}")


def _scope_of(hf_id: str, stated: str) -> str:
    """Q/LoRA, Full, Unstated, or Other. A lora/qlora token fills a not-stated agent row."""
    import rules

    if stated == "not stated":
        found = rules.methods_in_name(hf_id)
        if "qlora" in found or "lora" in found:
            return "Q/LoRA"
        return "Unstated"
    if stated == "qlora" or stated == "lora":
        return "Q/LoRA"
    if stated == "full":
        return "Full"
    if stated == "adapter_other":
        return "Other"
    fail(f"{hf_id} update_scope {stated!r} is not a known code")


# A model manual review moved from one grouping's study list to another's.
# reclassifications.csv is the only record: one row per model, with the search
# it came from, the grouping it is studied under, and the two reasons the
# funnel figures print (a removal line on the first, an addition on the second).
# roster.py reads the same file to find the model's source rows.
RECLASSIFICATIONS = Path(__file__).resolve().parent / "reclassifications.csv"
RECLASSIFICATION_FIELDS = (
    "hf_id", "from_grouping", "to_grouping", "decided_on", "removal_reason", "addition_reason", "note",
)


def reclassifications() -> list[dict]:
    """Rows of reclassifications.csv, checked. Stops on a missing or malformed file."""
    if not RECLASSIFICATIONS.is_file():
        fail(f"{RECLASSIFICATIONS} does not exist")
    with RECLASSIFICATIONS.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != RECLASSIFICATION_FIELDS:
            fail(f"{RECLASSIFICATIONS} header is {reader.fieldnames}, not {list(RECLASSIFICATION_FIELDS)}")
        rows = list(reader)
    seen = set()
    for row in rows:
        for key in ("hf_id", "from_grouping", "to_grouping", "decided_on", "removal_reason", "addition_reason"):
            if not (row.get(key) or "").strip():
                fail(f"{RECLASSIFICATIONS}: {row.get('hf_id')!r} has a blank {key}")
        if row["from_grouping"] not in ENDPOINT_BY_GROUPING or row["to_grouping"] not in ENDPOINT_BY_GROUPING:
            fail(f"{RECLASSIFICATIONS}: {row['hf_id']} names a grouping that does not exist")
        if row["from_grouping"] == row["to_grouping"]:
            fail(f"{RECLASSIFICATIONS}: {row['hf_id']} moves to its own grouping")
        if row["hf_id"] in seen:
            fail(f"{RECLASSIFICATIONS}: {row['hf_id']} is listed twice")
        seen.add(row["hf_id"])
    return rows


def _reclassified_out(grouping: str) -> dict[str, str]:
    """hf_id -> removal reason, for models that left this grouping's study list."""
    return {row["hf_id"]: row["removal_reason"] for row in reclassifications() if row["from_grouping"] == grouping}


def _transferred_in(grouping: str) -> tuple[tuple[str, str], ...]:
    """(hf_id, addition reason) for models that joined this grouping's study list."""
    return tuple(
        (row["hf_id"], row["addition_reason"]) for row in reclassifications() if row["to_grouping"] == grouping
    )


def _without_reclassified(grouping: str, stayed: list[str]) -> tuple[list[str], list[tuple[str, int]]]:
    """Drop study-list reclassifications from the last box and name the reason."""
    reasons: dict[str, int] = {}
    kept = []
    for hf_id in stayed:
        reason = _reclassified_out(grouping).get(hf_id)
        if reason:
            reasons[reason] = reasons.get(reason, 0) + 1
        else:
            kept.append(hf_id)
    return kept, list(reasons.items())


def last_box_ids(grouping: str, kept_csv: Path | None = None) -> list[str]:
    """Fine-tune ids in the thick-bordered box.

    Mental health: objective and fine-tuning method both stated, full or LoRA.
    Medical and safety: the list ``_mapping_losses`` keeps after that cut.
    """
    if kept_csv is None:
        kept_csv = cache.current_dir(grouping) / "kept.csv"
    stayed, _unstated, _other, _no_objective = _stated_split(grouping, kept_csv)
    stayed, _moved = _without_reclassified(grouping, stayed)
    if grouping == "mental-health":
        return list(stayed)
    final, _pairs = _mapping_losses(grouping, stayed)
    added = [hf_id for hf_id, _reason in _transferred_in(grouping)]
    overlap = sorted(set(added).intersection(final))
    if overlap:
        fail(f"{grouping}: transferred models are already in the final list: {overlap}")
    return list(final) + added


def _kept_ids(kept_csv: Path) -> list[str]:
    with kept_csv.open(newline="", encoding="utf-8") as handle:
        return [row["hf_id"] for row in csv.DictReader(handle)]


def _stated_split(grouping: str, kept_csv: Path) -> tuple[list[str], list[str], list[str], list[str]]:
    """Step-6 models: full or LoRA, unstated, another adapter, and no objective."""
    with kept_csv.open(newline="", encoding="utf-8") as handle:
        objective = {row["hf_id"]: (row.get("objective_stages") or "").strip() for row in csv.DictReader(handle)}
    agent: dict[tuple[str, str], str] = {}
    agent_path = cache.ROOT / "agent_methods.csv"
    with agent_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = (row["grouping"], row["hf_id"].lower())
            if key in agent:
                fail(f"{agent_path.name}: {row['hf_id']} listed twice for {row['grouping']}")
            agent[key] = (row.get("update_scope") or "").strip()
    no_objective = []
    unstated = []
    other = []
    stayed = []
    for hf_id in objective:
        scope = agent.get((grouping, hf_id.lower()))
        if scope is None:
            fail(f"{hf_id} is not in {agent_path}")
        if not objective[hf_id]:
            no_objective.append(hf_id)
            continue
        code = _scope_of(hf_id, scope)
        if code == "Unstated":
            unstated.append(hf_id)
        elif code == "Other":
            other.append(hf_id)
        else:
            stayed.append(hf_id)
    return stayed, unstated, other, no_objective


# Weight files match the instruction-tuned parent. These are not a second model.
PARENT_COPIES = {
    "MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged",
    "MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged",
    "MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged",
}
# A stated medical or clinical keyword, and the wrong task for this study.
TASK_MISMATCH = {
    "oopere/SmolLM2-1.7B-ClinicalNER": "Not a conversational model",
    "Rishidar/autoscientist-healthcare-qlora": "no clinical task named by the model author",
}


def _mapping_losses(grouping: str, stayed: list[str]) -> tuple[list[str], list[tuple[str, int]]]:
    """Among models with both fields stated, who the final list removes and why."""
    if grouping == "medical":
        mapped = set(_endpoint_ids(grouping, Path(".")))
        outside = [hf_id for hf_id in stayed if hf_id not in mapped]
        final = [hf_id for hf_id in stayed if hf_id in mapped]
        copies = [hf_id for hf_id in final if hf_id in PARENT_COPIES]
        final = [hf_id for hf_id in final if hf_id not in PARENT_COPIES]
        mismatched = [hf_id for hf_id in final if hf_id in TASK_MISMATCH]
        final = [hf_id for hf_id in final if hf_id not in TASK_MISMATCH]
        mismatch_counts: dict[str, int] = {}
        for hf_id in mismatched:
            reason = TASK_MISMATCH[hf_id]
            mismatch_counts[reason] = mismatch_counts.get(reason, 0) + 1
        pairs = [
            ("no mental-health fine-tune of that family and version", len(outside)),
            ("redundant with a kept model", len(copies)),
            *mismatch_counts.items(),
        ]
        return final, [(reason, n) for reason, n in pairs if n]
    if grouping == "safety":
        kept_ids, _removed_n = version_rule_split("safety")
        kept_set = set(kept_ids)
        repo = Path(__file__).resolve().parents[1]
        if str(repo) not in sys.path:
            sys.path.insert(0, str(repo))
        from safety_labels.cohort import COHORT, USABLE_IDS

        stated = {spec.hf_id for spec in COHORT}
        usable = set(USABLE_IDS)
        final = []
        counts = {
            VERSION_RULE_LOSS: 0,
            "card has no prompt and label to score": 0,
            "did not produce the label the card names": 0,
        }
        for hf_id in stayed:
            if hf_id in usable:
                final.append(hf_id)
            elif hf_id not in kept_set:
                counts[VERSION_RULE_LOSS] += 1
            elif hf_id not in stated:
                counts["card has no prompt and label to score"] += 1
            else:
                counts["did not produce the label the card names"] += 1
        return final, [(reason, n) for reason, n in counts.items() if n]
    fail(f"no mapping loss for {grouping}")


def add_scope_box(drawn: list, grouping: str, kept_csv: Path) -> None:
    """Require a stated objective and fine-tuning method on the method box.

    Mental health: that box is the last box. Medical and safety: it is the box
    before the final list, and the final list only removes models with nothing
    to map onto.
    """
    entering = _kept_ids(kept_csv)
    index = next((i for i, box in enumerate(drawn) if box[0] == BOX["6"]), None)
    if index is None:
        fail(f"{grouping}: no training-method box to attach the stated-method cut to")
    _label, count, lines, removed, _end = drawn[index]
    if _plain_count(count) != len(entering):
        fail(f"{grouping}: method box is {count}, but {kept_csv} has {len(entering)} models")
    stayed, unstated, other, no_objective = _stated_split(grouping, kept_csv)
    if len(stayed) + len(unstated) + len(other) + len(no_objective) != len(entering):
        fail(f"{grouping}: stated-method cut does not account for {len(entering)} models")
    stayed, moved = _without_reclassified(grouping, stayed)
    box_ids = last_box_ids(grouping, kept_csv)
    if grouping == "mental-health" and set(box_ids) != set(stayed):
        fail(f"{grouping}: last box ids are not the stated-method list")
    pairs = []
    pairs.extend(moved)
    if unstated:
        pairs.append((SCOPE_LOSS, len(unstated)))
    if other:
        pairs.append((OTHER_METHOD_LOSS, len(other)))
    if no_objective:
        pairs.append((OBJECTIVE_LOSS, len(no_objective)))
    existing = []
    for line in lines:
        if not line[:1].isdigit() or ".  " not in line[:8]:
            continue
        _item, rest = line.split(".  ", 1)
        count_text, reason = rest.split("  ", 1)
        existing.append((reason, int(count_text.replace(",", ""))))
    if sum(n for _reason, n in existing) != removed:
        fail(f"{grouping}: could not read the method-box removal lines")
    totals: dict[str, int] = {}
    order: list[str] = []
    for reason, n in existing + pairs:
        if reason not in totals:
            order.append(reason)
            totals[reason] = 0
        totals[reason] += n
    merged_pairs = [(reason, totals[reason]) for reason in order]
    new_lines, new_removed = numbered(merged_pairs) if merged_pairs else ([], 0)
    is_last = index == len(drawn) - 1
    drawn[index] = (METHOD_BOX, comma(len(box_ids) if is_last else len(stayed)), new_lines, new_removed, is_last)
    if is_last:
        if grouping != "mental-health":
            fail(f"{grouping}: the stated-method box is last, but a final list should follow it")
        return
    final, loss_pairs = _mapping_losses(grouping, stayed)
    added = list(_transferred_in(grouping))
    added_ids = [hf_id for hf_id, _reason in added]
    if set(added_ids).intersection(stayed):
        fail(f"{grouping}: a transferred model is already in this search")
    displayed = list(final) + added_ids
    if set(displayed) != set(box_ids):
        fail(f"{grouping}: last box ids and the final list differ")
    if len(final) + sum(n for _reason, n in loss_pairs) != len(stayed):
        fail(
            f"{grouping}: final list keeps {len(final)} and removes {sum(n for _r, n in loss_pairs)}, "
            f"which is not the {len(stayed)} models with both fields stated"
        )
    loss_lines, removed_n = numbered(loss_pairs) if loss_pairs else ([], 0)
    item = (FINAL_BOX, comma(len(displayed)), loss_lines, removed_n, True)
    if added:
        added_lines = []
        for i, (_hf_id, reason) in enumerate(added, 1):
            text = f"{i}. {reason}"
            added_lines.extend(textwrap.wrap(text, width=LINE_WIDTH, subsequent_indent="    ") or [text])
        item = (*item, (len(added_ids), added_lines))
    drawn[-1] = item


def draw(drawn: list, title: str, out_dir: Path) -> None:
    bh, gap = 1.55, 0.42

    def side_height(item: tuple) -> float:
        lines = item[2]
        added_lines = item[5][1] if len(item) > 5 and item[5] else []
        height = 0.0
        blocks = 0
        if lines:
            height += 0.36 * len(lines) + 0.62
            blocks += 1
        if added_lines:
            height += 0.36 * len(added_lines) + 0.62
            blocks += 1
        if blocks > 1:
            height += 0.28
        return height

    row_heights = [max(bh, side_height(item)) + gap for item in drawn]
    fig_h = sum(row_heights) + 0.7
    fig, ax = plt.subplots(figsize=(17.4, fig_h))
    ax.set_xlim(0, 17.4)
    ax.set_ylim(0, fig_h)
    ax.axis("off")
    ax.text(0.45, fig_h - 0.1, title, fontsize=11, va="top", ha="left", color="#333333")

    bx, bw = 0.45, 5.7
    lx, lw = 7.15, 9.8
    cursor = fig_h - 0.55
    centers = []
    for item, row_h in zip(drawn, row_heights):
        label, count, lines, removed, endpoint = item[:5]
        top, bottom = cursor, cursor - (row_h - gap)
        y = bottom + max(0, (top - bottom - bh) / 2)
        centers.append(y)
        ax.add_patch(FancyBboxPatch((bx, y), bw, bh, boxstyle="round,pad=0.02,rounding_size=0.08",
                                    linewidth=3.0 if endpoint else 1.2, edgecolor="black",
                                    facecolor=ENDPOINT_FILL if endpoint else "white"))
        ax.text(bx + 0.16, y + bh / 2, label, fontsize=12.5, va="center", ha="left",
                fontweight="bold" if endpoint else "normal")
        ax.text(bx + bw - 0.16, y + bh / 2, count, fontsize=18, fontweight="bold", va="center", ha="right")
        added_n, added_lines = item[5] if len(item) > 5 and item[5] else (0, [])
        blocks = []
        if lines:
            blocks.append((f"{comma(removed)} models removed", lines, 0.36 * len(lines) + 0.62))
        if added_lines:
            added_title = "1 model added" if added_n == 1 else f"{comma(added_n)} models added"
            blocks.append((added_title, added_lines, 0.36 * len(added_lines) + 0.62))
        if blocks:
            stack_gap = 0.28
            stack_h = sum(block_h for _title, _text, block_h in blocks) + stack_gap * (len(blocks) - 1)
            ly = y + bh / 2 + stack_h / 2
            for title_text, text_lines, block_h in blocks:
                ly -= block_h
                ax.add_patch(FancyBboxPatch((lx, ly), lw, block_h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                            linewidth=0.9, edgecolor="#777777", facecolor="#f4f4f4"))
                ax.text(lx + 0.12, ly + block_h - 0.08, title_text,
                        fontsize=12.0, fontweight="bold", va="top", ha="left")
                ax.text(lx + 0.12, ly + block_h - 0.46, "\n".join(text_lines), fontsize=11.2, va="top", ha="left",
                        family="monospace")
                ly -= stack_gap
            ax.add_patch(FancyArrowPatch((bx + bw, y + bh / 2), (lx, y + bh / 2), arrowstyle="-|>",
                                         mutation_scale=12, linewidth=0.9, color="#777777"))
        cursor -= row_h
    for i in range(len(centers) - 1):
        ax.add_patch(FancyArrowPatch((bx + bw / 2, centers[i]), (bx + bw / 2, centers[i + 1] + bh),
                                     arrowstyle="-|>", mutation_scale=14, linewidth=1.1, color="black"))
    # SVG paused. Restore this line when a vector funnel is needed again.
    # fig.savefig(out_dir / "funnel.svg", bbox_inches="tight")
    fig.savefig(out_dir / "funnel.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", required=True)
    ap.add_argument("--as-of", default="current",
                    help="ISO date of the results folder to draw; default 'current' reads outputs/funnel/<grouping>/CURRENT")
    ap.add_argument("--relax", default="", help="draw the sensitivity/<as-of>__relax-<rule> results instead")
    args = ap.parse_args()
    if args.as_of == "current":
        args.as_of = cache.current_view(args.grouping)
    view = f"sensitivity/{args.as_of}__relax-{args.relax}" if args.relax else args.as_of
    out_dir = RESULTS / args.grouping / view
    counts_path = out_dir / "counts.csv"
    if not counts_path.exists():
        fail(f"{counts_path} not found; run funnel.py first")
    drawn = rows_for(load_counts(counts_path), args.grouping)
    add_scope_box(drawn, args.grouping, out_dir / "kept.csv")
    title = f"{args.grouping} funnel, view {args.as_of}" + data_dates(out_dir / "provenance.csv") \
        + (f", rule relaxed: {args.relax}" if args.relax else "")
    draw(drawn, title, out_dir)
    print(f"wrote {out_dir / 'funnel.png'}")
    for item in drawn:
        label, count, _lines, removed, _endpoint = item[:5]
        extra = f"   (+{item[5][0]:,})" if len(item) > 5 and item[5] else ""
        print(f"  {label.replace(chr(10), ' '):<70} {count:>8}   (-{removed:,}){extra}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
