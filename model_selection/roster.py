"""Write the study roster.

The fine-tune ids are figure.last_box_ids. Instruction-tuned parents and
pretrained checkpoints are rows because a surviving fine-tune names them.
They do not pass the fine-tune funnel. Score columns are filled in this same
file, and Table S1 and Table S2 are written next to it (supp_tables.py).

    .venv/bin/python model_selection/roster.py

Run this from the model_selection directory, or pass the script path. Every run
writes outputs/roster/<day of the run>/ and then outputs/roster/CURRENT; an
older dated folder is a previous roster. A score fill between runs
(orchestration.fill_roster_scores.refresh_roster) rewrites the file CURRENT
names and does not move it.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(HERE))

import cache  # noqa: E402
import download  # noqa: E402
import family_figure  # noqa: E402
import figure  # noqa: E402
import mh_card_review_doc  # noqa: E402
import supp_tables  # noqa: E402

GROUPINGS = ("mental-health", "medical", "safety")
def _fail(message: str, values: list[str] | None = None) -> None:
    print(message, file=sys.stderr)
    for value in values or []:
        print(f"  {value}", file=sys.stderr)
    raise SystemExit(1)


DATASET_SOURCE = {
    "yaml_datasets": "named in the model card",
    "dataset_tag": "named in a dataset tag",
    "accessible_data": "opened training file or dataset page",
    "yaml_datasets+alias": "named in the model card; an informal name was replaced by its Hub id",
    "alias": "an informal name was replaced by its Hub id",
}

_PARENT_TABLE = None
_CARDS = None


def _dataset_source(raw: str) -> str:
    text = (raw or "").strip()
    if not text:
        return ""
    if text not in DATASET_SOURCE:
        _fail("dataset_source has no plain-language label", [text])
    return DATASET_SOURCE[text]


def _dataset_urls(datasets: str) -> str:
    urls = []
    for piece in (datasets or "").split(";"):
        name = piece.strip()
        if "/" not in name or " " in name or name.startswith("["):
            continue
        urls.append(f"https://huggingface.co/datasets/{name}")
    return ";".join(urls)


def _hf_url(hf_id: str) -> str:
    return f"https://huggingface.co/{hf_id}"


def _named_base(parent: str) -> str:
    """Pretrained repo the parent's card or the parent table names.

    A blank means that reading names no base repo. This is not the list of
    checkpoints a figure has already run.
    """
    global _PARENT_TABLE, _CARDS
    if _PARENT_TABLE is None:
        _PARENT_TABLE = family_figure.parse_parent_table(family_figure.REVIEW_DOC)
        _CARDS = family_figure.load_cards()
    got = family_figure.base_status_for_parent(parent, _PARENT_TABLE, _CARDS)
    if got is None and parent in family_figure.REHOST_MAP:
        got = family_figure.base_status_for_parent(family_figure.REHOST_MAP[parent], _PARENT_TABLE, _CARDS)
    if got is None:
        _fail("no pretrained-base reading for an instruction parent", [parent])
    if got["status"] in ("not_named", "named_404"):
        return ""
    if got["status"] not in ("yes", "yes_sibling", "named_not_checked", "named_no_fp"):
        _fail(f"unrecognized base status {got['status']}", [parent])
    return (got["base_repo"] or "").strip()


def _kept(grouping: str) -> dict[str, dict]:
    path = cache.current_dir(grouping) / "kept.csv"
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    found: dict[str, dict] = {}
    duplicates = []
    for row in rows:
        hf_id = row["hf_id"]
        if hf_id in found:
            duplicates.append(hf_id)
        found[hf_id] = row
    if duplicates:
        _fail(f"{path} lists a model twice", duplicates)
    return found


def _methods() -> dict[tuple[str, str], str]:
    path = cache.ROOT / "agent_methods.csv"
    if not path.is_file():
        _fail(f"missing {path}")
    found: dict[tuple[str, str], str] = {}
    duplicates = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            key = (row["grouping"], row["hf_id"].lower())
            if key in found:
                duplicates.append(f"{row['grouping']} {row['hf_id']}")
            found[key] = (row.get("update_scope") or "").strip()
    if duplicates:
        _fail(f"{path} lists a model twice", duplicates)
    return found


def _version_index() -> dict[tuple[str, str], dict]:
    found: dict[tuple[str, str], dict] = {}
    duplicates = []
    for row in figure.version_rule_rows():
        key = (row["grouping"], row["hf_id"])
        if key in found:
            duplicates.append(f"{row['grouping']} {row['hf_id']}")
        found[key] = row
    if duplicates:
        _fail("version_rule rows list a model twice", duplicates)
    return found


def _ancestor(hf_id: str, role: str, groupings: list[str]) -> dict:
    got = family_figure.classify_parent(hf_id)
    if got is None:
        _fail("classify_parent returned nothing for a roster ancestor", [hf_id])
    family, version, size, _kind = got
    return {
        "grouping": "",
        "role": role,
        "hf_id": hf_id,
        "family": family,
        "version": version,
        "size": size,
        "hf_url": _hf_url(hf_id),
        "training_objective": "",
        "training_objective_stages": "",
        "training_method": "",
        "dataset_source": "",
        "datasets": "",
        "dataset_urls": "",
        "dataset_quote": "",
        "dataset_quote_url": "",
        "dataset_hub_status": "",
        "output_type": "",
        "use_claim": "",
        "claim_quote": "",
        "warning_strength": "",
        "warning_quote": "",
        "detection_quote": "",
        "description": "",
        "card_file": "",
        "dtype_codes": "",
        "weights_format": "",
        "parent_id": "",
        "pretrained_id": "",
        "named_by_groupings": ";".join(sorted(set(groupings))),
    }


_CARD_REVIEW = mh_card_review_doc.review_csv()
_SAFETY_DETECTION = REPO / "docs/safety_FT_funnel/decisions/card-review/safety-detection-2026-10-20.csv"
_FUNNEL_DIR = {
    "mental-health": "mental_health_FT_funnel",
    "medical": "medical_FT_funnel",
    "safety": "safety_FT_funnel",
}
_REVIEW_ROWS = None
_SAFETY_ROWS = None


def _read_review(path: Path) -> dict[str, dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return {row["hf_id"]: row for row in csv.DictReader(handle)}


def _card_review() -> dict[str, dict]:
    global _REVIEW_ROWS
    if _REVIEW_ROWS is None:
        _REVIEW_ROWS = _read_review(_CARD_REVIEW)
    return _REVIEW_ROWS


def _safety_detection() -> dict[str, dict]:
    global _SAFETY_ROWS
    if _SAFETY_ROWS is None:
        _SAFETY_ROWS = _read_review(_SAFETY_DETECTION)
    return _SAFETY_ROWS


def _lead_paragraph(path: Path) -> str:
    """The first prose paragraph of a cached model card, after the YAML header."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                lines = lines[index + 1 :]
                break
    buf = []
    for line in lines:
        text = line.strip()
        if not text or text.startswith(("#", "!", "<", "|", "```")):
            if buf:
                break
            continue
        buf.append(line)
        if sum(len(item) for item in buf) > 500:
            break
    return "\n".join(buf)


def _extraction_path(grouping: str, hf_id: str) -> Path:
    slug = hf_id.replace("/", "__") + ".json"
    root = REPO / "docs" / _FUNNEL_DIR[grouping] / "agent-searches"
    hits = [
        path for path in root.glob(f"**/extractions/{slug}")
        if not any("pilot" in part for part in path.parts[:-1])
    ]
    if not hits:
        _fail("no extraction record for a roster fine-tune", [f"{grouping} {hf_id}"])
    def dated(path: Path) -> str:
        for part in path.parts:
            if len(part) >= 10 and part[4] == "-" and part[:4].isdigit():
                return part
        return ""
    return sorted(hits, key=dated)[-1]


def _claims(grouping: str, hf_id: str) -> dict[str, str]:
    """Quotes from the extraction record. Mental-health claim fields use the card review when it has this model.

    Medical claim fields stay on the extraction, including a sentence taken from the training rows.
    Safety has no claim or warning scale (decided 9 Oct 2026), so those four cells stay blank.
    detection_quote is the card sentence that says what a safety model detects. It is blank
    for mental-health and medical rows.
    description is the first prose paragraph of the cached card. card_file is that file's name.
    """
    path = _extraction_path(grouping, hf_id)
    doc = json.loads(path.read_text(encoding="utf-8"))
    output = doc.get("output_type")
    if not isinstance(output, dict) or "value" not in output:
        _fail("extraction has no output_type.value", [str(path)])
    found = {
        "output_type": (output.get("value") or "").strip(),
        "use_claim": "",
        "claim_quote": "",
        "warning_strength": "",
        "warning_quote": "",
        "detection_quote": "",
        "dataset_quote": "",
        "dataset_quote_url": "",
        "description": "",
        "card_file": "",
    }
    cached = doc.get("card") or {}
    card_path = Path(cached.get("cached_file") or "")
    if not card_path.is_file():
        card_path = REPO / card_path
    if not card_path.is_file():
        _fail("extraction names no cached card", [str(path)])
    found["card_file"] = card_path.name
    found["description"] = _lead_paragraph(card_path)
    if grouping != "safety":
        use = doc.get("use_claim")
        warning = doc.get("warning")
        if not isinstance(use, dict) or "quote" not in use or not isinstance(warning, dict):
            _fail("extraction has no use_claim quote", [str(path)])
        found["use_claim"] = (use.get("strength") or "").strip()
        found["claim_quote"] = (use.get("quote") or "").strip()
        found["warning_strength"] = (warning.get("strength") or "").strip()
        found["warning_quote"] = (warning.get("quote") or "").strip()
    data = doc.get("training_data")
    if not isinstance(data, list):
        _fail("extraction has no training_data list", [str(path)])
    quotes = []
    urls = []
    for item in data:
        quote = (item.get("quote") or "").strip()
        url = (item.get("source_url") or "").strip()
        if quote:
            quotes.append(quote)
        if url and url not in urls:
            urls.append(url)
    found["dataset_quote"] = " || ".join(quotes)
    found["dataset_quote_url"] = ";".join(urls)
    if grouping == "mental-health":
        review = _card_review().get(hf_id)
        if review is None:
            _fail(f"mental-health fine-tune has no row in {_CARD_REVIEW}", [hf_id])
        for key in ("output_type", "use_claim", "claim_quote", "warning_strength", "warning_quote"):
            found[key] = review.get(key) or ""
    if grouping == "safety":
        detection = _safety_detection().get(hf_id)
        if detection is None or not (detection.get("detection_quote") or "").strip():
            _fail("safety fine-tune has no detection sentence", [hf_id])
        quote = detection["detection_quote"]
        if quote not in card_path.read_text(encoding="utf-8", errors="replace"):
            _fail("detection sentence is not on the cached card", [hf_id])
        found["detection_quote"] = quote
    return found


def identity_rows() -> list[dict]:
    methods = _methods()
    version = _version_index()
    kept_by = {grouping: _kept(grouping) for grouping in GROUPINGS}
    ids_by = {grouping: figure.last_box_ids(grouping) for grouping in GROUPINGS}
    # A model manual review moved to another grouping (reclassifications.csv)
    # is studied under to_grouping; its kept.csv, version_rule, agent_methods,
    # and card-review rows stay under from_grouping, so they are read from there.
    source_grouping = {
        (row["to_grouping"], row["hf_id"]): row["from_grouping"] for row in figure.reclassifications()
    }
    missing = []
    fine_tunes = []
    parent_groups: dict[str, list[str]] = {}
    for grouping in GROUPINGS:
        for hf_id in ids_by[grouping]:
            source = source_grouping.get((grouping, hf_id), grouping)
            kept_row = kept_by[source].get(hf_id)
            rule = version.get((source, hf_id))
            scope = methods.get((source, hf_id.lower()))
            problems = []
            if kept_row is None:
                problems.append("no kept.csv row")
            if rule is None:
                problems.append("no version_rule row")
            if scope is None:
                problems.append("no agent_methods update_scope")
            if problems:
                where = grouping if source == grouping else f"{grouping} (source rows under {source})"
                missing.append(f"{where} {hf_id}: {', '.join(problems)}")
                continue
            parent = (kept_row.get("parent") or "").strip()
            if not parent:
                missing.append(f"{grouping} {hf_id}: kept.csv parent is blank")
                continue
            claims = _claims(source, hf_id)
            fine_tunes.append(
                {
                    "grouping": grouping,
                    "role": "fine-tune",
                    "hf_id": hf_id,
                    "family": rule["family"],
                    "version": rule["version"],
                    "size": rule["size"],
                    "hf_url": _hf_url(hf_id),
                    "training_objective": kept_row.get("objective") or "",
                    "training_objective_stages": kept_row.get("objective_stages") or "",
                    "training_method": scope,
                    "dataset_source": _dataset_source(kept_row.get("dataset_source") or ""),
                    "datasets": kept_row.get("datasets") or "",
                    "dataset_urls": _dataset_urls(kept_row.get("datasets") or ""),
                    "dataset_quote": claims["dataset_quote"],
                    "dataset_quote_url": claims["dataset_quote_url"],
                    "dataset_hub_status": kept_row.get("dataset_hub_status") or "",
                    "output_type": claims["output_type"],
                    "use_claim": claims["use_claim"],
                    "claim_quote": claims["claim_quote"],
                    "warning_strength": claims["warning_strength"],
                    "warning_quote": claims["warning_quote"],
                    "detection_quote": claims["detection_quote"],
                    "description": claims["description"],
                    "card_file": claims["card_file"],
                    "dtype_codes": kept_row.get("dtype_codes") or "",
                    "weights_format": kept_row.get("weights_format") or "",
                    "parent_id": parent,
                    "pretrained_id": _named_base(parent),
                    "named_by_groupings": source,
                }
            )
            parent_groups.setdefault(parent, []).append(grouping)
    if missing:
        _fail("fine-tune source fields are missing", missing)

    parents = []
    for parent, groupings in sorted(parent_groups.items()):
        row = _ancestor(parent, "instruction parent", groupings)
        row["pretrained_id"] = _named_base(parent)
        parents.append(row)

    base_groups: dict[str, list[str]] = {}
    for row in fine_tunes:
        if row["pretrained_id"]:
            base_groups.setdefault(row["pretrained_id"], []).extend(row["named_by_groupings"].split(";"))
    pretrained = [
        _ancestor(base, "pretrained", groupings)
        for base, groupings in sorted(base_groups.items())
    ]
    return fine_tunes + parents + pretrained


def _git_revision() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()


def _target_date() -> str:
    """The roster folder is dated by the day it is written."""
    return date.today().isoformat()


def _missing_weights(rows: list[dict]) -> list[str]:
    missing = []
    for row in rows:
        folder = download.folder(download.DEFAULT_DEST, row["hf_id"])
        ok, _why = download.complete(folder)
        if not ok and folder.is_symlink():
            ok, _why = download.complete(Path(folder))
        if not ok:
            missing.append(row["hf_id"])
    return missing


def write_roster(rows: list[dict]) -> Path:
    sys.modules.pop("cache", None)
    here = str(HERE)
    sys.path[:] = [item for item in sys.path if item != here]
    sys.path.insert(0, str(REPO))
    from orchestration.fill_roster_scores import fill_scores
    from orchestration.study_roster import COLUMNS, POINTER, ROSTER_ROOT

    scored = fill_scores(rows)
    day = _target_date()
    out_dir = ROSTER_ROOT / day
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "roster.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in scored:
            writer.writerow({key: row.get(key, "") for key in COLUMNS})
    provenance = {
        "git_revision": _git_revision(),
        "current_dates": {grouping: cache.current_view(grouping) for grouping in GROUPINGS},
        "parent_map": "family_figure.base_status_for_parent",
        "weights_missing": _missing_weights(scored),
    }
    (out_dir / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    supp_tables.write_tables(scored, out_dir)
    POINTER.write_text(day + "\n", encoding="utf-8")
    print(f"wrote {csv_path}")
    if provenance["weights_missing"]:
        print(
            f"{len(provenance['weights_missing'])} roster rows have no weights under {download.DEFAULT_DEST}",
            file=sys.stderr,
        )
        for hf_id in provenance["weights_missing"]:
            print(f"  {hf_id}", file=sys.stderr)
    return csv_path


def main() -> int:
    write_roster(identity_rows())
    return 0


if __name__ == "__main__":
    sys.exit(main())
