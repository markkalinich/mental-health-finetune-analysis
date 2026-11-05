"""The study roster is the last box, and a score fill does not rename it."""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PY = REPO / ".venv/bin/python"
HF = REPO / "model_selection"
sys.path.insert(0, str(REPO))

from orchestration.study_roster import POINTER, load_roster, roster_csv  # noqa: E402
from safety_labels.cohort import USABLE_IDS  # noqa: E402


def _last_box(grouping: str) -> set[str]:
    script = (
        "import json, figure\n"
        f"print(json.dumps(figure.last_box_ids({grouping!r})))\n"
    )
    out = subprocess.check_output([str(PY), "-c", script], cwd=HF, text=True)
    return set(json.loads(out))


def test_fine_tunes_match_the_last_box():
    rows = [row for row in load_roster() if row["role"] == "fine-tune"]
    by_group = {}
    for row in rows:
        by_group.setdefault(row["grouping"], set()).add(row["hf_id"])
    for grouping in ("mental-health", "medical", "safety"):
        assert by_group[grouping] == _last_box(grouping)
    assert set(USABLE_IDS) < by_group["safety"]
    assert by_group["safety"] - set(USABLE_IDS) == {"SungJoo/cradle-dialogue-qwen3-32b-2epoch"}


def test_parents_and_pretrained_ids():
    rows = load_roster()
    fine = [row for row in rows if row["role"] == "fine-tune"]
    parents = {row["hf_id"]: row for row in rows if row["role"] == "instruction parent"}
    pretrained = {row["hf_id"] for row in rows if row["role"] == "pretrained"}
    assert parents
    assert pretrained
    script = (
        "import json, roster\n"
        "parents = json.loads(input())\n"
        "print(json.dumps({parent: roster._named_base(parent) for parent in parents}))\n"
    )
    named = json.loads(subprocess.check_output(
        [str(PY), "-c", script],
        cwd=HF,
        input=json.dumps(sorted({row["parent_id"] for row in fine})),
        text=True,
    ))
    # A model manual review moved to another grouping keeps its kept.csv row
    # under the grouping it came from (model_selection/reclassifications.csv).
    with (HF / "reclassifications.csv").open(newline="", encoding="utf-8") as handle:
        source_grouping = {(row["to_grouping"], row["hf_id"]): row["from_grouping"] for row in csv.DictReader(handle)}
    kept_rows = {}
    for grouping in ("mental-health", "medical", "safety"):
        kept = REPO / "outputs/funnel" / grouping / (REPO / "outputs/funnel" / grouping / "CURRENT").read_text().strip() / "kept.csv"
        kept_rows[grouping] = {row["hf_id"]: row["parent"] for row in csv.DictReader(kept.open())}
    for grouping in ("mental-health", "medical", "safety"):
        for row in fine:
            if row["grouping"] != grouping:
                continue
            source = source_grouping.get((grouping, row["hf_id"]), grouping)
            assert row["parent_id"] == kept_rows[source][row["hf_id"]]
            assert row["named_by_groupings"] == source
            expected = named[row["parent_id"]]
            assert row["pretrained_id"] == expected
            assert row["parent_id"] in parents
            assert parents[row["parent_id"]]["pretrained_id"] == expected
            if expected:
                assert expected in pretrained
    for row in rows:
        if row["role"] != "fine-tune":
            assert row["training_objective"] == ""
            assert row["training_method"] == ""
            assert row["size"]


def test_score_fill_refuses_to_blank_a_filled_cell():
    from orchestration.fill_roster_scores import refuse_score_drops

    old = [
        {"hf_id": "a/b", "si_f1": "0.100000", "cssrs_f1": "0.200000", "mhb_safety": ""},
        {"hf_id": "c/d", "si_f1": "", "cssrs_f1": "", "mhb_safety": "0.300000"},
    ]
    new = [
        {"hf_id": "a/b", "si_f1": "", "cssrs_f1": "0.200000", "mhb_safety": ""},
        {"hf_id": "c/d", "si_f1": "", "cssrs_f1": "", "mhb_safety": ""},
    ]
    try:
        refuse_score_drops(old, new)
    except SystemExit as exc:
        message = str(exc)
    else:
        raise AssertionError("a filled cell was blanked without stopping")
    assert "a/b si_f1" in message
    assert "c/d mhb_safety" in message
    assert "a/b cssrs_f1" not in message


def test_draw_stops_when_the_roster_disagrees_with_a_fresh_fill():
    from orchestration.fill_roster_scores import require_same_scores

    old = [{"hf_id": "a/b", "si_f1": "0.100000", "cssrs_f1": "", "mhb_safety": "0.200000"}]
    new = [{"hf_id": "a/b", "si_f1": "0.400000", "cssrs_f1": "0.500000", "mhb_safety": "0.200000"}]
    try:
        require_same_scores(old, new)
    except SystemExit as exc:
        message = str(exc)
    else:
        raise AssertionError("a disagreement was drawn anyway")
    assert "a/b si_f1 roster 0.100000 fill 0.400000" in message
    assert "a/b cssrs_f1 roster blank fill 0.500000" in message
    assert "mhb_safety" not in message


def test_rewrite_load_ignores_the_labeled_figure_filter():
    from orchestration.fill_roster_scores import _load_for_rewrite
    from orchestration.study_roster import COLUMNS

    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "roster.csv"
        rows = []
        for hf_id, method, objective in (
            ("keep/labeled", "full", "sft"),
            ("drop/unstated", "not stated", ""),
        ):
            row = {name: "" for name in COLUMNS}
            row["role"] = "fine-tune"
            row["hf_id"] = hf_id
            row["training_method"] = method
            row["training_objective_stages"] = objective
            rows.append(row)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        os.environ["MANUSCRIPT_LABELED"] = "1"
        try:
            loaded = _load_for_rewrite(path)
        finally:
            os.environ.pop("MANUSCRIPT_LABELED", None)
    assert [row["hf_id"] for row in loaded] == ["keep/labeled", "drop/unstated"]


def test_score_fill_keeps_the_directory_name():
    """rewrite() fills a copy of the roster in place: same file, same row ids, same header.

    The real roster is not written by a test. A fill whose inputs are still
    being written (a grader appending) stops in refuse_score_drops; the copy
    makes that a test failure instead of a half-written study roster.
    """
    import shutil

    source = roster_csv()
    assert POINTER.read_text().strip() == source.parent.name
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / source.parent.name / "roster.csv"
        path.parent.mkdir()
        shutil.copy2(source, path)
        before = [row["hf_id"] for row in load_roster(path)]
        subprocess.check_call(
            [str(PY), "-c", "import orchestration.fill_roster_scores as fill; fill.rewrite(%r)" % str(path)],
            cwd=REPO,
        )
        after = load_roster(path)
        assert path.parent.name == source.parent.name
        assert [row["hf_id"] for row in after] == before
        with path.open(newline="", encoding="utf-8") as handle:
            header = next(csv.reader(handle))
        with source.open(newline="", encoding="utf-8") as handle:
            assert header == next(csv.reader(handle))
    assert POINTER.read_text().strip() == source.parent.name


def test_mhb_safety_omits_safety_only_parents():
    """A parent enters MHB-Safety only when a mental-health or medical fine-tune names it."""
    from orchestration.study_roster import mhb_safety_ids

    rows = load_roster()
    kept = mhb_safety_ids(rows)
    omitted = {
        "Qwen/Qwen3-4B-Instruct-2507",
        "meta-llama/Llama-3.2-1B-Instruct",
    }
    assert omitted.isdisjoint(kept)
    assert "Qwen/Qwen3-4B" in kept
    assert "google/gemma-3-1b-it" in kept
    assert "unsloth/gemma-3-1b-it" in kept
    safety = {row["hf_id"] for row in rows if row["role"] == "fine-tune" and row["grouping"] == "safety"}
    assert safety.isdisjoint(kept)
    assert len(safety) == 10


def test_analysis_keeps_the_listed_parent_and_drops_the_copy():
    """A fine-tune that lists an Unsloth parent keeps that parent.

    The Unsloth row is the same model as the Google row, so the analysis
    count does not include both.
    """
    from orchestration.study_roster import for_analysis

    kept = for_analysis(load_roster())
    by_id = {row["hf_id"]: row for row in kept}
    assert "unsloth/gemma-3-1b-it" not in by_id
    assert "unsloth/gemma-3-4b-it" not in by_id
    assert "google/gemma-3-1b-it" in by_id
    assert "google/gemma-3-4b-it" in by_id
    assert by_id["ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit"]["parent_id"] == "unsloth/gemma-3-1b-it"
    assert by_id["naazimsnh02/gemma3-4b-mental-health-counseling"]["parent_id"] == "unsloth/gemma-3-4b-it"
    parents = [row for row in kept if row["role"] == "instruction parent"]
    fine = [row for row in kept if row["role"] == "fine-tune"]
    assert len(parents) == 25
    assert len(fine) == 48


def test_figures_come_from_the_current_roster():
    """outputs/figures/<CURRENT>/roster.sha256 names the roster the figures were drawn from.

    It is written by publish_manuscript_figures.main() and must equal the sha256
    of the current roster. When it does not, the roster changed after the last
    draw and the figures must be redrawn.
    """
    from orchestration.publish_manuscript_figures import ROSTER_SHA_NAME, current_figure_dir, roster_sha256

    sha_file = current_figure_dir() / ROSTER_SHA_NAME
    assert sha_file.is_file(), f"{sha_file} is missing; run orchestration/publish_manuscript_figures.py"
    recorded, _space, named = sha_file.read_text(encoding="utf-8").strip().partition("  ")
    assert named == str(roster_csv().relative_to(REPO)), f"{sha_file} names {named}, roster is {roster_csv()}"
    assert recorded == roster_sha256(), (
        f"{sha_file} is {recorded[:12]}..., {roster_csv()} is {roster_sha256()[:12]}...; redraw the figures"
    )
