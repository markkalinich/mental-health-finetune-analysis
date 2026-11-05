"""Write Table S1 and Table S2 next to the roster they are read from.

Table S1, one row per fine-tune on the roster: the data columns come from
roster.csv; the four prose columns (supporting text, quote source, template or
message modifications, parsing modifications) come from table_s1_text.csv in
this directory, which is the only place that prose is kept. A fine-tune missing
from either file stops the run.

Table S2, one row per group (instruction-tuned and the three fine-tune
groupings; the pretrained group is included when
orchestration.study_roster.DRAW_PRETRAINED is true). The two Unsloth copies
of Google instruction-tuned models are omitted (study_roster.for_analysis).
The share of models
whose parse rate reaches 100%,
>90%, >75%, >50%, for the strict first-line rule and for the Sonnet-recovered
rule on synthetic SI and C-SSRS. The MentalHealthBench non-empty-reply
rate over all 1,215 conversations stays on the roster (mhb_n_parsed / mhb_n)
and is not a column of this table. Every number comes from roster.csv:

  strict rate   = <task>_strict_parsed / <task>_n
  Sonnet rate   = (<task>_strict_parsed + <task>_sonnet_answered_yes
                   + <task>_sonnet_answered_no) / <task>_n

A model counts in a task column only when that task's cells are filled; n per
column says how many. A model with an unlabeled failure stops the run.

    .venv/bin/python model_selection/supp_tables.py

rewrites both tables in the current roster folder. roster.py calls write_tables
after it writes a new roster.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

TEXT = HERE / "table_s1_text.csv"
TEXT_FIELDS = (
    "hf_id", "supporting_text", "quote_source", "template_or_message_modifications", "parsing_modifications",
)
S1_HEADER = (
    "Study Grouping", "Search Grouping", "Hugging Face ID", "Supporting text", "Quote source",
    "Family-Version", "Parameters", "Training Objective(s)", "Training Method", "Precision",
    "Parent model", "Dataset", "Template or Message Modifications", "Parsing Modifications",
    "Dataset Link", "HuggingFace Link",
)
THRESHOLDS = (("100%", lambda r: r >= 1.0), (">90%", lambda r: r > 0.9), (">75%", lambda r: r > 0.75), (">50%", lambda r: r > 0.5))
def _groups() -> list[tuple]:
    """Table S2 rows. The Pre-trained row returns when DRAW_PRETRAINED is true."""
    from orchestration.study_roster import DRAW_PRETRAINED

    groups = [("Instruction-tuned", lambda row: row["role"] == "instruction parent")]
    if DRAW_PRETRAINED:
        groups.append(("Pre-trained", lambda row: row["role"] == "pretrained"))
    groups.extend(
        (
            ("Mental health", lambda row: row["role"] == "fine-tune" and row["grouping"] == "mental-health"),
            ("Medical", lambda row: row["role"] == "fine-tune" and row["grouping"] == "medical"),
            ("Safety", lambda row: row["role"] == "fine-tune" and row["grouping"] == "safety"),
        )
    )
    return groups


def _fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def _text_rows() -> dict[str, dict]:
    if not TEXT.is_file():
        _fail(f"{TEXT} does not exist")
    with TEXT.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != TEXT_FIELDS:
            _fail(f"{TEXT} header is {reader.fieldnames}, not {list(TEXT_FIELDS)}")
        rows = list(reader)
    found: dict[str, dict] = {}
    for row in rows:
        if row["hf_id"] in found:
            _fail(f"{TEXT} lists {row['hf_id']} twice")
        if not row["supporting_text"].strip() or not row["quote_source"].strip():
            _fail(f"{TEXT}: {row['hf_id']} has no supporting text or quote source")
        found[row["hf_id"]] = row
    return found


def _family_version(row: dict) -> str:
    family, version = row["family"].strip(), row["version"].strip()
    return version if version.startswith(family) else f"{family} {version}".strip()


def table_s1_rows(roster: list[dict]) -> list[dict]:
    text = _text_rows()
    fine = [row for row in roster if row["role"] == "fine-tune"]
    missing = [row["hf_id"] for row in fine if row["hf_id"] not in text]
    extra = sorted(set(text) - {row["hf_id"] for row in fine})
    if missing:
        _fail(f"{TEXT} has no row for: {missing}")
    if extra:
        _fail(f"{TEXT} has rows that are not fine-tunes on the roster: {extra}")
    out = []
    for row in fine:
        prose = text[row["hf_id"]]
        out.append({
            "Study Grouping": row["grouping"],
            "Search Grouping": row["named_by_groupings"],
            "Hugging Face ID": row["hf_id"],
            "Supporting text": prose["supporting_text"],
            "Quote source": prose["quote_source"],
            "Family-Version": _family_version(row),
            "Parameters": row["size"],
            "Training Objective(s)": "; ".join(part for part in row["training_objective_stages"].split("|") if part),
            "Training Method": row["training_method"],
            "Precision": "; ".join(part for part in row["dtype_codes"].split("|") if part),
            "Parent model": row["parent_id"],
            "Dataset": row["datasets"],
            "Template or Message Modifications": prose["template_or_message_modifications"],
            "Parsing Modifications": prose["parsing_modifications"],
            "Dataset Link": row["dataset_urls"],
            "HuggingFace Link": row["hf_url"],
        })
    return out


def _rate(row: dict, task: str, sonnet: bool) -> float | None:
    n = (row.get(f"{task}_n") or "").strip()
    if not n:
        return None
    strict = int(row[f"{task}_strict_parsed"])
    if not sonnet:
        return strict / int(n)
    if int(row[f"{task}_sonnet_unlabeled"]):
        _fail(f"{row['hf_id']} has unlabeled {task} failures; Table S2 is not written")
    recovered = strict + int(row[f"{task}_sonnet_answered_yes"]) + int(row[f"{task}_sonnet_answered_no"])
    return recovered / int(n)


def _mhb_rate(row: dict) -> float | None:
    """Non-empty replies over all 1,215 conversations. Not a Table S2 column."""
    n = (row.get("mhb_n") or "").strip()
    if not n:
        return None
    return int(row["mhb_n_parsed"]) / int(n)


def _share(rates: list[float], test) -> str:
    hit = sum(1 for rate in rates if test(rate))
    return f"{100.0 * hit / len(rates):.1f}% ({hit}/{len(rates)})" if rates else "N/A"


def table_s2_rows(roster: list[dict]) -> tuple[list[str], list[dict]]:
    from orchestration.study_roster import for_analysis

    roster = for_analysis(roster)
    columns = [("Strict SI", "si", False), ("Sonnet SI", "si", True), ("Strict C-SSRS", "cssrs", False), ("Sonnet C-SSRS", "cssrs", True)]
    header = ["Group", "Model count"]
    for label, _task, _sonnet in columns:
        header.extend(f"{label} {name}" for name, _test in THRESHOLDS)
    out = []
    for group, member in _groups():
        rows = [row for row in roster if member(row)]
        record = {"Group": group}
        yesno = [row for row in rows if _rate(row, "si", False) is not None and _rate(row, "cssrs", False) is not None]
        record["Model count"] = str(len(yesno))
        for label, task, sonnet in columns:
            rates = [_rate(row, task, sonnet) for row in yesno]
            for name, test in THRESHOLDS:
                record[f"{label} {name}"] = _share(rates, test)
        out.append(record)
    return header, out


def _write(path: Path, header: list[str] | tuple[str, ...], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(header), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")


def write_tables(roster: list[dict], out_dir: Path) -> None:
    _write(out_dir / "table_s1.csv", S1_HEADER, table_s1_rows(roster))
    header, rows = table_s2_rows(roster)
    _write(out_dir / "table_s2.csv", header, rows)


def main() -> int:
    from orchestration.study_roster import load_roster, roster_csv

    path = roster_csv()
    write_tables(load_roster(path), path.parent)
    return 0


if __name__ == "__main__":
    sys.exit(main())
