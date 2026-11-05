#!/usr/bin/env python3
"""Draw the manuscript figures and write the tables next to them.

One cohort, read from the study roster: every instruction-tuned parent and
the fine-tunes whose weight-update method and training objective are both
stated (orchestration.study_roster.labeled_fine_tune). Pretrained checkpoints
stay on the roster and are omitted from the figures while
orchestration.study_roster.DRAW_PRETRAINED is false.
The former All_models cohort (every fine-tune, stated or not) is no longer
drawn; its call is left in main() as a comment. There is one output folder.

Outputs land in
outputs/figures/<date>/<HHMMSS>/{main-figures,supp-figures,main-tables,supp-tables},
where <date> is the day of the draw (--date overrides) and <HHMMSS> is the
time the draw started. outputs/figures/CURRENT is written last and names that
folder, for example 2026-10-26/150635. An older folder is a previous pass.

The roster is refreshed from the reply, grade, and label files once, checked
against a fresh fill once, and its sha256 is written to
outputs/figures/<date>/<HHMMSS>/roster.sha256. The mixed models behind Table 1 are then
fit from that same roster into outputs/mixed-models/<date>/
(orchestration/fit_mixed_models.py), the figures are drawn, and every PNG is
checked to be newer than the roster. MANUSCRIPT_LABELED=1 is set while the
cohort is drawn. The funnel pictures are the three grouping funnels.
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

FIGURES_ROOT = REPO / "outputs/figures"
# One line: the date folder of the last complete draw. Written by main() after
# every output is verified. Readers (the tests, anyone quoting a figure) use it;
# nothing else names a figure date.
POINTER = FIGURES_ROOT / "CURRENT"
ROSTER_SHA_NAME = "roster.sha256"
GROUPINGS = (
    ("mental-health", "Mental health"),
    ("medical", "Medical"),
    ("safety", "Safety"),
)
OBJECTIVES = ("SFT", "GRPO", "DPO", "Distillation", "More than one stage")
METHODS = ("LoRA", "QLoRA", "Full", "Unstated")
FUNNELS = (
    ("mental-health", "figure-s1.png"),
    ("medical", "figure-s2.png"),
    ("safety", "figure-s3.png"),
)


def _roster_path() -> Path:
    from orchestration.study_roster import roster_csv

    return roster_csv()


def _roster_rows() -> list[dict]:
    with _roster_path().open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def roster_sha256(path: Path | None = None) -> str:
    return hashlib.sha256((path or _roster_path()).read_bytes()).hexdigest()


def figure_dir(date: str | None = None) -> Path:
    """The folder a draw writes: FIGURES/<date>/<HHMMSS>."""
    from datetime import datetime

    now = datetime.now()
    day = date or now.strftime("%Y-%m-%d")
    dest = FIGURES_ROOT / day / now.strftime("%H%M%S")
    if dest.exists():
        raise SystemExit(f"{dest} already exists")
    return dest


def current_figure_dir() -> Path:
    """The folder of the last complete draw, from FIGURES/CURRENT."""
    if not POINTER.is_file():
        raise SystemExit(f"{POINTER} does not exist; run orchestration/publish_manuscript_figures.py")
    text = POINTER.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit(f"{POINTER} is empty")
    return FIGURES_ROOT / text


def _write_roster_sha(fig: Path, path: Path) -> Path:
    """Record which roster file the figures in fig were drawn from."""
    fig.mkdir(parents=True, exist_ok=True)
    target = fig / ROSTER_SHA_NAME
    target.write_text(f"{roster_sha256(path)}  {path.relative_to(REPO)}\n", encoding="utf-8")
    print(f"wrote {target}")
    return target


def _verify_outputs(roster: Path, sha: str, cohorts: list[Path]) -> None:
    """Every PNG is newer than the roster and the roster did not change while drawing."""
    if roster_sha256(roster) != sha:
        raise SystemExit(f"{roster} changed while the figures were being drawn; rerun")
    roster_mtime = roster.stat().st_mtime_ns
    stale = []
    for cohort in cohorts:
        pngs = sorted(cohort.rglob("*.png"))
        if not pngs:
            raise SystemExit(f"no PNG under {cohort}")
        stale.extend(str(png) for png in pngs if png.stat().st_mtime_ns < roster_mtime)
    if stale:
        raise SystemExit("figures older than the roster they should come from:\n" + "\n".join(stale))


def _write_table_s3(points: Path, dest: Path) -> Counter:
    from orchestration.study_roster import method_code, objective_code

    by_id = {row["hf_id"]: row for row in _roster_rows() if row["role"] == "fine-tune"}
    seen: dict[str, dict] = {}
    with points.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            seen.setdefault(row["hf_id"], row)
    counts: Counter = Counter()
    model_rows = []
    for hf_id, point in sorted(seen.items()):
        source = by_id.get(hf_id)
        if source is None:
            raise SystemExit(f"{hf_id} is in {points} and not a fine-tune on {_roster_path()}")
        if point["kind"] != source["grouping"]:
            raise SystemExit(f"{hf_id} grouping is {point['kind']} on the figure and {source['grouping']} on the roster")
        objective = objective_code(source)
        method = method_code(source)
        if objective not in OBJECTIVES:
            raise SystemExit(f"{hf_id} objective {objective!r} is not in the table")
        if method not in METHODS:
            raise SystemExit(f"{hf_id} method {method!r} is not in the table")
        counts[(source["grouping"], objective, method)] += 1
        model_rows.append({
            "hf_id": hf_id,
            "grouping": source["grouping"],
            "objective": objective,
            "method": method,
            "method_on_roster": source["training_method"],
        })
    methods = [name for name in METHODS if any(counts[(g, o, name)] for g, _label in GROUPINGS for o in OBJECTIVES)]
    header_groups = [""]
    header_methods = ["Objective"]
    for index, (_key, label) in enumerate(GROUPINGS):
        header_groups.extend([label] + [""] * len(methods))
        header_methods.extend([*methods, "Total"])
        if index != len(GROUPINGS) - 1:
            header_groups.append("")
            header_methods.append("")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header_groups)
        writer.writerow(header_methods)
        for objective in OBJECTIVES:
            line = [objective]
            for index, (grouping, _label) in enumerate(GROUPINGS):
                cells = [counts[(grouping, objective, method)] for method in methods]
                line.extend([*cells, sum(cells)])
                if index != len(GROUPINGS) - 1:
                    line.append("")
            writer.writerow(line)
        total = ["Total"]
        for index, (grouping, _label) in enumerate(GROUPINGS):
            cells = [sum(counts[(grouping, objective, method)] for objective in OBJECTIVES) for method in methods]
            total.extend([*cells, sum(cells)])
            if index != len(GROUPINGS) - 1:
                total.append("")
        writer.writerow(total)
    models_path = dest.with_name(dest.stem + "-models.csv")
    with models_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["hf_id", "grouping", "objective", "method", "method_on_roster"],
        )
        writer.writeheader()
        writer.writerows(model_rows)
    print(f"wrote {dest}")
    print(f"wrote {models_path} ({len(model_rows)} models)")
    return counts


def _joined(row: dict, fields: tuple[str, ...]) -> str:
    parts = []
    for field in fields:
        value = row[field].strip()
        if not value:
            raise SystemExit(f"{row['Hugging Face ID']}: {field} is blank")
        parts.append(value)
    return "; ".join(parts)


def _parent_serving_rows(full: list[dict]) -> list[tuple[str, dict, str]]:
    """Instruction-tuned parents that were served with a fine-tune's change.

    config/serving_repairs.csv is the list of serving changes. A parent on the
    roster is added to Table S2 only when that file folds its system message
    and one fine-tune in the roster's table_s1.csv already states the sentence.
    The returned note says why the parent row is there. Two different sentences
    for one parent, or a parent repair this function cannot copy, stops the run.
    """
    path = REPO / "config" / "serving_repairs.csv"
    if not path.is_file():
        raise SystemExit(f"{path} does not exist")
    with path.open(newline="", encoding="utf-8") as handle:
        repairs = list(csv.DictReader(handle))
    by_id: dict[str, dict] = {}
    for repair in repairs:
        hf_id = repair["hf_id"]
        if hf_id in by_id:
            raise SystemExit(f"{path} lists {hf_id} twice")
        by_id[hf_id] = repair
    roster = {row["hf_id"]: row for row in _roster_rows()}
    additions = []
    for hf_id, repair in by_id.items():
        parent = roster.get(hf_id)
        if parent is None or parent["role"] != "instruction parent":
            continue
        if repair["fold_system"] != "1":
            raise SystemExit(
                f"{hf_id}: instruction-tuned parent in {path} has fold_system "
                f"{repair['fold_system']!r}; Table S2 has no sentence for that repair"
            )
        children = []
        for row in full:
            if row["Parent model"].strip() != hf_id:
                continue
            text = row["Template or Message Modifications"].strip()
            if text:
                children.append((row["Hugging Face ID"], text))
        if not children:
            raise SystemExit(f"{hf_id}: no fine-tune template sentence to copy into Table S2")
        texts = {text for _child, text in children}
        if len(texts) != 1:
            raise SystemExit(f"{hf_id}: fine-tunes name different template sentences: {children}")
        child_ids = [child for child, _text in children]
        if len(child_ids) == 1:
            names = child_ids[0]
        elif len(child_ids) == 2:
            names = f"{child_ids[0]} and {child_ids[1]}"
        else:
            names = ", ".join(child_ids[:-1]) + ", and " + child_ids[-1]
        additions.append((
            child_ids[-1],
            {
                "Grouping": "instruction-tuned parent",
                "Hugging Face ID": hf_id,
                "Template or message modifications": texts.pop(),
                "Parsing modifications": "",
            },
            (
                f"{hf_id} is the instruction-tuned parent of {names}. "
                "It is in this table because that parent was sent the same single user message. "
                "The other rows are fine-tunes."
            ),
        ))
    if not additions:
        raise SystemExit(f"{path}: no instruction-tuned parent on the roster has a serving repair")
    return additions


def _copy_shared_tables(supp_tables: Path) -> None:
    """Write the manuscript tables from the roster copies.

    The roster folder keeps the full Table S1. The manuscript Table S1 is the
    short form. Table S2 is the template and parsing columns for the fine-tunes
    that have one of those notes, plus an instruction-tuned parent when
    config/serving_repairs.csv records the same serving change. The reason is
    written to table-s2-note.txt and printed under the table.
    Table S3 is the parse-rate table. It is rewritten from the roster, then
    copied. The two Unsloth copies of Google models are not rows in it.
    """
    from model_selection.supp_tables import write_tables

    saved = os.environ.get("MANUSCRIPT_LABELED")
    os.environ["MANUSCRIPT_LABELED"] = "0"
    try:
        write_tables(_roster_rows(), _roster_path().parent)
    finally:
        if saved is None:
            os.environ.pop("MANUSCRIPT_LABELED", None)
        else:
            os.environ["MANUSCRIPT_LABELED"] = saved
    cradle = next(row for row in _roster_rows() if row["hf_id"] == "SungJoo/cradle-dialogue-qwen3-32b-2epoch")
    if cradle["grouping"] != "safety":
        raise SystemExit(f"cradle grouping is {cradle['grouping']}; Table S1 is not copied")
    source = _roster_path().parent / "table_s1.csv"
    with source.open(newline="", encoding="utf-8") as handle:
        full = list(csv.DictReader(handle))
    if not full:
        raise SystemExit(f"{source} is empty")
    short_header = (
        "Grouping",
        "Hugging Face ID",
        "Supporting text (Quote source)",
        "Model details",
        "Parent model",
        "Links",
    )
    mod_header = (
        "Grouping",
        "Hugging Face ID",
        "Template or message modifications",
        "Parsing modifications",
    )
    short_rows = []
    mod_rows = []
    for row in full:
        details = _joined(row, ("Family-Version", "Parameters", "Training Objective(s)", "Training Method", "Precision"))
        quote = row["Quote source"].strip()
        text = row["Supporting text"].strip()
        if not text or not quote:
            raise SystemExit(f"{row['Hugging Face ID']}: supporting text or quote source is blank")
        dataset_name = row["Dataset"].strip()
        dataset_url = row["Dataset Link"].strip()
        hub = row["HuggingFace Link"].strip()
        if not dataset_name and not dataset_url:
            raise SystemExit(f"{row['Hugging Face ID']}: dataset name and link are both blank")
        if not hub or not row["Parent model"].strip():
            raise SystemExit(f"{row['Hugging Face ID']}: the Hugging Face link or the parent is blank")
        if dataset_url:
            dataset = f"{dataset_name} ({dataset_url})" if dataset_name else dataset_url
        else:
            dataset = dataset_name
        short_rows.append({
            "Grouping": row["Study Grouping"],
            "Hugging Face ID": row["Hugging Face ID"],
            "Supporting text (Quote source)": f"{text} ({quote})",
            "Model details": details,
            "Parent model": row["Parent model"],
            "Links": f"Dataset: {dataset}; HuggingFace: {hub}",
        })
        template = row["Template or Message Modifications"].strip()
        parsing = row["Parsing Modifications"].strip()
        if template or parsing:
            mod_rows.append({
                "Grouping": row["Study Grouping"],
                "Hugging Face ID": row["Hugging Face ID"],
                "Template or message modifications": template,
                "Parsing modifications": parsing,
            })
    if not mod_rows:
        raise SystemExit(f"{source}: no template or parsing modifications to put in Table S2")
    notes = []
    for after_id, parent_row, note in _parent_serving_rows(full):
        indexes = [i for i, row in enumerate(mod_rows) if row["Hugging Face ID"] == after_id]
        if len(indexes) != 1:
            raise SystemExit(f"Table S2 has {len(indexes)} rows for {after_id}; the parent row is not placed")
        mod_rows.insert(indexes[0] + 1, parent_row)
        notes.append(note)
    note_path = supp_tables / "table-s2-note.txt"
    note_path.write_text(" ".join(notes) + "\n", encoding="utf-8")
    print(f"wrote {note_path}")
    _write_display(supp_tables / "table-s1.csv", short_header, short_rows)
    _write_display(supp_tables / "table-s2.csv", mod_header, mod_rows)
    parse_source = _roster_path().parent / "table_s2.csv"
    with parse_source.open(newline="", encoding="utf-8") as handle:
        parse_rows = list(csv.reader(handle))
    if not parse_rows or "Model count" not in parse_rows[0]:
        raise SystemExit(f"{parse_source} has no Model count column")
    target = supp_tables / "table-s3.csv"
    with target.open("w", encoding="utf-8-sig", newline="") as handle:
        csv.writer(handle).writerows(parse_rows)
    print(f"wrote {target}")


def _write_display(path: Path, header: tuple[str, ...], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(header), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path} ({len(rows)} rows)")


def _funnels(cohorts: list[Path]) -> None:
    for grouping, filename in FUNNELS:
        subprocess.run(
            [sys.executable, str(REPO / "model_selection/figure.py"),
             "--grouping", grouping, "--as-of", "current"],
            cwd=REPO,
            check=True,
        )
        current = (REPO / "outputs/funnel" / grouping / "CURRENT").read_text(encoding="utf-8").strip()
        source = REPO / "outputs/funnel" / grouping / current / "funnel.png"
        for cohort in cohorts:
            target = cohort / "supp-figures" / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            print(f"wrote {target}")


def _strict_rows() -> list[dict]:
    """The roster the figures just read, with strict yes/no F1 in place of Sonnet F1.

    The roster file is not written. MentalHealthBench cells are copied through.
    joint_and_paired._apply_parse_mode is the check: a roster score with no
    strict F1, or a strict F1 where the roster is blank, stops the draw.
    """
    import pandas as pd

    from orchestration.joint_and_paired import _apply_parse_mode
    from orchestration.study_roster import load_roster

    rows = load_roster()
    replaced = _apply_parse_mode(pd.DataFrame(rows), "strict").set_index("hf_id")
    out = []
    for row in rows:
        copied = dict(row)
        for column in ("si_f1", "cssrs_f1"):
            value = replaced.at[row["hf_id"], column]
            copied[column] = "" if pd.isna(value) else f"{float(value):.6f}"
        out.append(copied)
    return out


def _draw(fig: Path, folder: str, labeled: bool) -> None:
    """Draw one cohort from the roster main() has already refreshed and checked."""
    os.environ["MANUSCRIPT_LABELED"] = "1" if labeled else "0"
    root = fig if not folder else fig / folder
    main_figures = root / "main-figures"
    supp_figures = root / "supp-figures"
    main_tables = root / "main-tables"
    supp_tables = root / "supp-tables"
    for path in (main_figures, supp_figures, main_tables, supp_tables):
        path.mkdir(parents=True, exist_ok=True)

    family_path = REPO / "model_selection/family_figure.py"
    spec = importlib.util.spec_from_file_location("family_figure", family_path)
    family_figure = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(family_figure)
    import orchestration.plot_params_vs_score as params
    import orchestration.plot_parse_rates as heat
    import orchestration.plot_sonnet_recovery as sonnet
    import orchestration.plot_spaghetti_delta as spaghetti

    family_figure.OUT_PNG = main_figures / "figure-1.png"
    family_figure.OUT_CSV = main_tables / "figure-1-counts.csv"
    family_figure.main()
    shutil.copy2(family_figure.OUT_CSV, main_figures / "figure-1-counts.csv")

    sonnet.OUT = supp_figures / "figure-s4.png"
    sonnet.OUT_TESTS = supp_figures / "figure-s4-tests.csv"
    sonnet.OUT_CSV = supp_figures / "figure-s4-points.csv"
    from orchestration.study_roster import load_roster

    scored = {row["hf_id"] for row in load_roster() if row["si_n"] and row["cssrs_n"]}
    sonnet.main(keep=scored)

    import orchestration.plot_sol_vs_luna as sol_luna

    sol_luna.draw(supp_figures / "figure-s5.png")

    work = root / "_work"
    work.mkdir(parents=True, exist_ok=True)
    heat.OUT_DIR = work
    heat.main()
    for source_name, figure_name in (
        ("performance_parameters_qwen.png", "figure-s6.png"),
        ("performance_parameters_gemma.png", "figure-s7.png"),
        ("performance_parameters_llama.png", "figure-s8.png"),
        ("performance_parameters_mistral-smollm.png", "figure-s9.png"),
    ):
        shutil.copy2(work / source_name, supp_figures / figure_name)
        print(f"wrote {supp_figures / figure_name}")

    params.OUT = work / "params-vs-score.png"
    params.OUT_TYPE = main_figures / "figure-3.png"
    params.OUT_HEAT = work / "scores-by-family.png"
    params.STATS = main_figures / "figure-3-regressions.csv"
    params.main()

    spaghetti.OUT = main_figures / "figure-2.png"
    spaghetti.TESTS = main_figures / "figure-2-tests.csv"
    spaghetti.main()
    spaghetti.write_method_objective_figures(supp_figures)
    params.version_review_figure(params._points(), main_figures / "figure-4.png")

    strict_rows = _strict_rows()
    spaghetti.OUT = supp_figures / "figure-s12.png"
    spaghetti.TESTS = supp_figures / "figure-s12-tests.csv"
    spaghetti.main(strict_rows)
    strict_points = params._points(strict_rows)
    s13_records = params._type_figure(strict_points, dest=supp_figures / "figure-s13.png")
    s13_stats = supp_figures / "figure-s13-regressions.csv"
    with s13_stats.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=params.STAT_FIELDS)
        writer.writeheader()
        writer.writerows(s13_records)
    print(f"wrote {s13_stats}")
    params.version_review_figure(strict_points, supp_figures / "figure-s14.png")

    _write_table_s3(supp_figures / "figure-s11-points.csv", supp_tables / "table-s5.csv")
    _copy_shared_tables(supp_tables)
    shutil.rmtree(work)
    print(f"finished {folder}")


MAIN_FIGURES = (
    ("Figure 1", "Available models by family, parameter weight, and training type.", ("main-figures/figure-1.png",)),
    ("Figure 2", "Fine-tune score and the instruction-parent score.", ("main-figures/figure-2.png",)),
    (
        "Figure 3",
        "Score versus parameter count, one row per training type. A solid line is a fit with Benjamini–Hochberg q below 0.05. A dotted line is a fit with q of 0.05 or higher.",
        ("main-figures/figure-3.png",),
    ),
    (
        "Figure 4",
        "Score by release for Gemma, LLaMA, and Qwen. Color and marker are the training type, and a violin summarizes a release with at least three models. The mark is a Kruskal–Wallis test of the three releases, Benjamini–Hochberg adjusted across the nine panels.",
        ("main-figures/figure-4.png",),
    ),
)
SUPP_FIGURES = (
    ("Figure S1", "Inclusion and exclusion criteria for mental-health fine-tuned models", ("supp-figures/figure-s1.png",)),
    ("Figure S2", "Inclusion and exclusion criteria for medical fine-tuned models", ("supp-figures/figure-s2.png",)),
    ("Figure S3", "Inclusion and exclusion criteria for safety models", ("supp-figures/figure-s3.png",)),
    ("Figure S4", "Strict (left) and LLM-evaluated parsing success rates for each model", ("supp-figures/figure-s4.png",)),
    (
        "Figure S5",
        "GPT-5.6 Sol versus GPT-5.6 Luna scoring on a 25-question subset of MentalHealthBench",
        ("supp-figures/figure-s5.png",),
    ),
    ("Figure S6", "Detailed performance characteristics for Qwen models", ("supp-figures/figure-s6.png",)),
    ("Figure S7", "Detailed performance characteristics for Gemma models", ("supp-figures/figure-s7.png",)),
    ("Figure S8", "Detailed performance characteristics for LLaMA models", ("supp-figures/figure-s8.png",)),
    ("Figure S9", "Detailed performance characteristics for Mistral and SmolLM models", ("supp-figures/figure-s9.png",)),
    ("Figure S10", "Change in fine-tune model performance relative to parent model stratified by fine-tune method", ("supp-figures/figure-s10.png",)),
    ("Figure S11", "Change in fine-tune model performance relative to parent model stratified by fine-tune objective", ("supp-figures/figure-s11.png",)),
    (
        "Figure S12",
        "Figure 2 with strict yes/no parsing in place of Sonnet-recovered answers. MHB-Safety is unchanged.",
        ("supp-figures/figure-s12.png",),
    ),
    (
        "Figure S13",
        "Figure 3 with strict yes/no parsing in place of Sonnet-recovered answers. MHB-Safety is unchanged.",
        ("supp-figures/figure-s13.png",),
    ),
    (
        "Figure S14",
        "Figure 4 with strict yes/no parsing in place of Sonnet-recovered answers. MHB-Safety is unchanged.",
        ("supp-figures/figure-s14.png",),
    ),
)
TABLES = (
    ("Table S1", "Model Descriptions", "supp-tables/table-s1.csv", 1),
    ("Table S2", "Template, message serving, or parsing modifications", "supp-tables/table-s2.csv", 1),
    ("Table S3", "Parsing success by model fine-tune grouping and task", "supp-tables/table-s3.csv", 1),
)
TABLE_S4_TITLE = "Fine-tune minus its instruction-tuned parent, clustered by parent"
TABLES_AFTER = (
    ("Table S5", "Model count by fine-tune objective and method, and fine-tune grouping", "supp-tables/table-s5.csv", 2),
)
# Three sentences on the first page. 48 fine-tunes and 25 instruction-tuned
# parents: the two Unsloth copies of Google models are one model each.
CHANGES = (
    "This revision keeps 48 full-precision fine-tunes — 18 mental-health, 20 medical, and 10 safety — each with one full-precision instruction-tuned parent (25 parents) and a stated training dataset, weight-update method, and training objective.",
    "The benchmarks add Reddit C-SSRS and MHB-Safety, the suicide and self-harm conversations from MentalHealthBench, and drop the screens for an inappropriate therapy request and for the model delivering therapy.",
    "The regression is now a linear mixed model with a random intercept for each instruction-tuned parent and its fine-tunes.",
)


def _require(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"missing {path}")


def _keep_with_next(paragraph) -> None:
    paragraph.paragraph_format.keep_with_next = True


def _add_pictures(doc, root: Path, names: tuple[str, ...], width) -> None:
    from docx.shared import Emu, Inches
    from PIL import Image

    # Leave room on a portrait page for the heading and caption. A figure
    # taller than the page was spilling onto a following blank page.
    max_height = Inches(8.0)
    for index, name in enumerate(names):
        path = root / name
        _require(path)
        with Image.open(path) as image:
            aspect = image.height / image.width
        draw_width = width
        draw_height = Emu(int(width) * aspect)
        if draw_height > max_height:
            draw_height = max_height
            draw_width = Emu(int(int(max_height) / aspect))
        doc.add_picture(str(path), width=draw_width, height=draw_height)
        if index != len(names) - 1:
            _keep_with_next(doc.paragraphs[-1])


def _set_arial(run, bold: bool) -> None:
    from docx.oxml.ns import qn
    from docx.shared import Pt

    run.bold = bold
    run.font.size = Pt(11)
    run.font.name = "Arial"
    rpr = run._element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        fonts.set(qn(attr), "Arial")


def _labeled_caption(doc, label: str, text: str):
    """'Figure S1:' in bold, the rest in regular type. Both are Arial 11."""
    paragraph = doc.add_paragraph()
    _set_arial(paragraph.add_run(f"{label}:"), True)
    if text:
        _set_arial(paragraph.add_run(" " + text), False)
    return paragraph


def _figure_page(doc, root: Path, label: str, caption: str, names: tuple[str, ...], width, *, break_before: bool = True) -> None:
    if break_before:
        doc.add_page_break()
    _add_pictures(doc, root, names, width)
    _keep_with_next(doc.paragraphs[-1])
    _labeled_caption(doc, label, caption)


def _add_table(doc, path: Path, header_rows: int) -> None:
    from docx.oxml.ns import qn
    from docx.shared import Pt

    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        raise SystemExit(f"{path} is empty")
    width = max(len(row) for row in rows)
    table = doc.add_table(rows=len(rows), cols=width)
    table.style = "Table Grid"
    table.autofit = True
    for i, row in enumerate(rows):
        for j in range(width):
            cell = table.rows[i].cells[j]
            cell.text = row[j] if j < len(row) else ""
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(8)
                    run.bold = i < header_rows
            if i < header_rows and cell.text:
                shade = cell._tc.get_or_add_tcPr()
                fill = shade.makeelement(qn("w:shd"), {qn("w:fill"): "E6E6E6", qn("w:val"): "clear"})
                shade.append(fill)


def _mixed_dir() -> Path:
    """The mixed-model estimates folder named in mixed-models/CURRENT."""
    from orchestration.fit_mixed_models import current_mixed_dir

    return current_mixed_dir()


TABLE_1_TERMS = (
    ("log2_param_billions", "Parameter count, per doubling"),
    ("version_rank", "Version rank, per step"),
    ("mental-health", "Mental-health fine-tune"),
    ("medical", "Medical fine-tune"),
    ("safety", "Safety fine-tune"),
    ("Llama", "Llama vs Gemma"),
    ("Mistral", "Mistral vs Gemma"),
    ("Qwen", "Qwen vs Gemma"),
    ("SmolLM", "SmolLM vs Gemma"),
    ("Intercept", "Intercept"),
)


def _match_term(term: str, key: str) -> bool:
    if key in {"log2_param_billions", "version_rank", "Intercept"}:
        return term == key
    return key in term


def _cell(estimate: float, low: float, high: float) -> str:
    return f"{estimate:.3f} ({low:.3f} to {high:.3f})".replace("-", "\u2212")


def _bh(p_values: list[float]) -> list[float]:
    """Benjamini-Hochberg adjusted p-values, same order as the input."""
    from statsmodels.stats.multitest import multipletests

    if not p_values:
        raise SystemExit("FDR was asked for and there are no tests")
    _reject, adjusted, _a, _b = multipletests(p_values, alpha=0.05, method="fdr_bh")
    return [float(value) for value in adjusted]


def _p_cell(p_value: float) -> str:
    """q-value text. Stars match the figures: * <0.05, ** <0.01, *** <0.001."""
    if p_value < 0.001:
        text = "<0.001"
    else:
        text = f"{p_value:.3f}"
    if p_value < 0.001:
        return text + "***"
    if p_value < 0.01:
        return text + "**"
    if p_value < 0.05:
        return text + "*"
    return text


def _outcome_rows(frame, analysis: str, mixed: Path):
    rows = frame[(frame["analysis"] == analysis) & (frame["unit"] == "score (0-1)")]
    if rows.empty:
        raise SystemExit(f"No {analysis} rows on the 0–1 scale in {mixed}")
    return rows


MHB_METHOD_LABEL = {
    "ols_crv3": "β (95% CRV3 CI)",
    "mixed_model_wald": "β (95% Wald CI)",
}


def _mhb_decision(mixed: Path) -> dict:
    """The one-row MentalHealthBench inference decision written by mhb_variance_retry."""
    import pandas as pd

    frame = pd.read_csv(mixed / "mhb-inference-decision.csv")
    if len(frame) != 1:
        raise SystemExit(f"{mixed / 'mhb-inference-decision.csv'} has {len(frame)} rows, expected 1")
    row = frame.iloc[0].to_dict()
    if row["method"] not in MHB_METHOD_LABEL:
        raise SystemExit(f"unknown MentalHealthBench inference method {row['method']!r}")
    return row


SUMMARY_OUTCOMES = ("si_f1", "cssrs_f1", "mhb_safety")


def _require_parse_mode(mixed: Path, mode: str) -> None:
    path = mixed / "roster-source.txt"
    if not path.is_file():
        raise SystemExit(f"{path} is missing")
    expected = f"parse_mode: {mode}"
    if expected not in path.read_text(encoding="utf-8").splitlines():
        raise SystemExit(f"{path} does not contain {expected!r}")


def _fit_summary_rows(mixed: Path) -> list[list[str]]:
    """Blank row, then fixed-effect variance, parent-level variance, and model count.

    The two variance rows are Nakagawa's marginal and conditional R². The
    numerator of the first is the sample variance (divisor n−1) of
    fixed_prediction in mixed/joint-residuals.csv. The second adds
    random_intercept_variance from mixed/joint-model-fit.csv. Both divide by
    that sum plus residual_variance from the same file. The model count is
    n_observations in joint-model-fit.csv, and it has to equal the residual
    row count for that outcome.
    """
    import pandas as pd

    fit = pd.read_csv(mixed / "joint-model-fit.csv")
    residuals = pd.read_csv(mixed / "joint-residuals.csv")
    decision = _mhb_decision(mixed)
    if decision["method"] != "mixed_model_wald":
        raise SystemExit(
            f"{mixed}: the variance rows are for the mixed model, and the "
            f"MentalHealthBench decision is {decision['method']}"
        )
    marginal: list[str] = []
    conditional: list[str] = []
    counts: list[str] = []
    for outcome in SUMMARY_OUTCOMES:
        hit = fit[fit["outcome"] == outcome]
        if len(hit) != 1:
            raise SystemExit(f"{mixed}: expected one joint-model-fit row for {outcome}, found {len(hit)}")
        row = hit.iloc[0]
        if row.wald_supported is not True and str(row.wald_supported) not in {"True", "true", "1"}:
            raise SystemExit(f"{mixed}: {outcome} Wald fit is not supported, so the variance share was not computed")
        pred = residuals.loc[residuals["outcome"] == outcome, "fixed_prediction"]
        n = int(row.n_observations)
        if len(pred) != n:
            raise SystemExit(f"{mixed}: {outcome} has {len(pred)} residual rows and n_observations {n}")
        if n < 2:
            raise SystemExit(f"{mixed}: {outcome} has {n} models")
        var_fixed = float(pred.var(ddof=1))
        var_parent = float(row.random_intercept_variance)
        var_resid = float(row.residual_variance)
        total = var_fixed + var_parent + var_resid
        if not total > 0:
            raise SystemExit(f"{mixed}: {outcome} variance total is {total}")
        marginal.append(f"{100 * var_fixed / total:.1f}%")
        conditional.append(f"{100 * (var_fixed + var_parent) / total:.1f}%")
        counts.append(str(n))

    def line(label: str, values: list[str]) -> list[str]:
        cells = [label]
        for value in values:
            cells.extend([value, ""])
        return cells

    return [
        [""] * 7,
        line("Variance explained by the terms above", marginal),
        line("Variance explained with the shared parent level", conditional),
        line("Number of models", counts),
    ]


def write_table_1_csv(dest: Path, mixed: Path | None = None) -> None:
    """Coefficient table for one mixed-model folder.

    mixed defaults to mixed-models/CURRENT, which is Table 1. Table S6 passes
    mixed-models/strict_parsing. q is Benjamini–Hochberg across the
    coefficients in this table only. The three rows under the blank row are
    not tests and are left out of that adjustment.
    """
    import pandas as pd

    if mixed is None:
        mixed = _mixed_dir()
    joint = _outcome_rows(pd.read_csv(mixed / "estimates.csv"), "joint_mixed_model", mixed)
    decision = _mhb_decision(mixed)
    mhb = _outcome_rows(pd.read_csv(mixed / "mhb-chosen-estimates.csv"), decision["method"], mixed)
    header = [
        "Term",
        "Synthetic SI classification (F1)",
        "",
        "Reddit C-SSRS classification (F1)",
        "",
        "MHB-Safety",
        "",
    ]
    sub = ["", "β (95% Wald CI)", "q", "β (95% Wald CI)", "q", MHB_METHOD_LABEL[decision["method"]], "q"]
    body = [header, sub]
    raw_p: list[float] = []
    slots: list[tuple[int, int]] = []
    for key, label in TABLE_1_TERMS:
        line = [label]
        for outcome, source in (("si_f1", joint), ("cssrs_f1", joint), ("mhb_safety", mhb)):
            scoped = source[source["outcome"] == outcome] if "outcome" in source.columns else source
            hit = scoped[scoped["term"].map(lambda term: _match_term(str(term), key))]
            if key == "safety" and outcome == "mhb_safety":
                line.extend(["\u2014", "\u2014"])
                continue
            if len(hit) != 1:
                raise SystemExit(f"{mixed}: expected one {outcome} row for {key}, found {len(hit)}")
            row = hit.iloc[0]
            slots.append((len(body), len(line) + 1))
            raw_p.append(float(row.p_value))
            line.extend([_cell(row.estimate, row.ci_low, row.ci_high), ""])
        body.append(line)
    for (row_index, col_index), adjusted in zip(slots, _bh(raw_p)):
        body[row_index][col_index] = _p_cell(adjusted)
    body.extend(_fit_summary_rows(mixed))
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8-sig", newline="") as handle:
        csv.writer(handle).writerows(body)
    print(f"wrote {dest}")


def _portrait(section) -> None:
    from docx.enum.section import WD_ORIENT
    from docx.shared import Inches

    section.orientation = WD_ORIENT.PORTRAIT
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)


DELTA_ROWS = (
    ("mental-health", "Mental-health fine-tunes"),
    ("medical", "Medical fine-tunes"),
    ("safety", "Safety fine-tunes"),
)
DELTA_OUTCOMES = (
    ("si_f1", "Suicidal-ideation delta F1"),
    ("cssrs_f1", "C-SSRS delta F1"),
    ("mhb_safety", "MHB-Safety delta"),
)


def write_delta_table_csv(dest: Path) -> None:
    """Table S4: fine-tune minus instruction parent, CRV3 by lineage."""
    import pandas as pd

    path = _mixed_dir() / "category-deltas.csv"
    if not path.is_file():
        raise SystemExit(f"{path} does not exist; run orchestration/fit_mixed_models.py")
    frame = pd.read_csv(path)
    header = ["Fine-tune type"]
    for _key, label in DELTA_OUTCOMES:
        header.extend([label, ""])
    sub = [""]
    for _key, _label in DELTA_OUTCOMES:
        sub.extend(["Mean delta (95% CI)", "q"])
    body = [header, sub]
    raw_p: list[float] = []
    slots: list[tuple[int, int]] = []
    for category, label in DELTA_ROWS:
        line = [label]
        for outcome, _title in DELTA_OUTCOMES:
            hit = frame[(frame["training_category"] == category) & (frame["outcome"] == outcome)]
            if len(hit) != 1:
                raise SystemExit(f"Table 1 expected one {category} {outcome} row, found {len(hit)}")
            row = hit.iloc[0]
            if str(row.supported) not in {"True", "true", "1"} and row.supported is not True:
                line.extend(["\u2014", "\u2014"])
                continue
            slots.append((len(body), len(line) + 1))
            raw_p.append(float(row.p_value))
            line.extend([_cell(row.estimate, row.ci_low, row.ci_high), ""])
        body.append(line)
    for (row_index, col_index), adjusted in zip(slots, _bh(raw_p)):
        body[row_index][col_index] = _p_cell(adjusted)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8-sig", newline="") as handle:
        csv.writer(handle).writerows(body)
    print(f"wrote {dest}")


TABLE_1_LEGEND = (
    "Table 1: Linear mixed model of score on parameter count (per doubling), model version, "
    "fine-tune type, and model family. Each instruction-tuned parent and each of its fine-tunes is one row. "
    "Rows that share a parent share one random intercept. Coefficients (β) and 95% Wald confidence intervals "
    "are the fixed effects, shown for synthetic suicidal-ideation statement classification, Reddit C-SSRS "
    "classification, and MHB-Safety. The fixed-effect reference is an instruction-tuned Gemma model at "
    "version rank 0, the earliest model version of that family in this study. q is the "
    "Benjamini–Hochberg adjusted P value across every coefficient in the table. "
    "Statistical significance is denoted as: * q < 0.05, ** q < 0.01, *** q < 0.001. "
    "Safety fine-tunes are left out of MHB-Safety. An instruction-tuned parent is left out of that "
    "column when no mental-health or medical fine-tune of that parent is in the study. "
    "A blank row separates the coefficients from three summaries: the percentage of score variance "
    "accounted for by the fixed effects, the percentage after adding the shared parent level, and the "
    "number of models."
)

TABLE_S6_LEGEND = (
    "Table S6: Table 1 refit after replacing Sonnet-recovered yes/no answers with strict parsing. "
    "An unparsed yes/no answer counts as a false negative when the label is yes and a false positive "
    "when the label is no. MHB-Safety is unchanged because those scores are not a yes/no parse. "
    "Coefficients (β) and 95% Wald confidence intervals are the fixed effects. The reference is an "
    "instruction-tuned Gemma model at version rank 0. q is the Benjamini–Hochberg adjusted P value "
    "across every coefficient in this table. "
    "Statistical significance is denoted as: * q < 0.05, ** q < 0.01, *** q < 0.001. "
    "Safety fine-tunes are left out of MHB-Safety. An instruction-tuned parent is left out of that "
    "column when no mental-health or medical fine-tune of that parent is in the study. "
    "A blank row separates the coefficients from three summaries: the percentage of score variance "
    "accounted for by the fixed effects, the percentage after adding the shared parent level, and the "
    "number of models."
)


def _table_1(doc, root: Path) -> None:
    path = root / "main-tables" / "table-1.csv"
    write_table_1_csv(path)
    prefix = "Table 1:"
    if not TABLE_1_LEGEND.startswith(prefix):
        raise SystemExit("Table 1 legend does not start with 'Table 1:'")
    _labeled_caption(doc, "Table 1", TABLE_1_LEGEND[len(prefix):].lstrip())
    _add_table(doc, path, 2)


def _table_s4(doc, root: Path) -> None:
    path = root / "supp-tables" / "table-s4.csv"
    write_delta_table_csv(path)
    _labeled_caption(doc, "Table S4", TABLE_S4_TITLE)
    _add_table(doc, path, 2)


def _table_s6(doc, root: Path) -> None:
    from orchestration.fit_mixed_models import MIXED_ROOT

    mixed = MIXED_ROOT / "strict_parsing"
    _require_parse_mode(mixed, "strict")
    path = root / "supp-tables" / "table-s6.csv"
    write_table_1_csv(path, mixed)
    prefix = "Table S6:"
    if not TABLE_S6_LEGEND.startswith(prefix):
        raise SystemExit("Table S6 legend does not start with 'Table S6:'")
    _labeled_caption(doc, "Table S6", TABLE_S6_LEGEND[len(prefix):].lstrip())
    _add_table(doc, path, 2)


def _landscape(section) -> None:
    from docx.enum.section import WD_ORIENT
    from docx.shared import Inches

    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Inches(11)
    section.page_height = Inches(8.5)
    section.top_margin = Inches(0.6)
    section.bottom_margin = Inches(0.6)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)


def write_manuscript_docx(root: Path) -> Path:
    """Write the figures and tables into the run folder as figs_and_tables.docx."""
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.shared import Inches

    root = Path(root)
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.6)
    section.bottom_margin = Inches(0.6)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)
    for text in CHANGES:
        doc.add_paragraph(text)

    picture_width = Inches(7.1)
    for index, (label, caption, names) in enumerate(MAIN_FIGURES):
        _figure_page(doc, root, label, caption, names, picture_width, break_before=index > 0)

    table_section = doc.add_section(WD_SECTION.NEW_PAGE)
    _landscape(table_section)
    _table_1(doc, root)
    portrait = doc.add_section(WD_SECTION.NEW_PAGE)
    _portrait(portrait)

    doc.add_page_break()
    doc.add_heading("Supplementary Figures", level=1)
    for index, (label, caption, names) in enumerate(SUPP_FIGURES):
        _figure_page(doc, root, label, caption, names, picture_width, break_before=index > 0)

    landscape = doc.add_section(WD_SECTION.NEW_PAGE)
    _landscape(landscape)
    doc.add_heading("Supplementary Tables", level=1)
    for label, title, name, header_rows in TABLES:
        path = root / name
        _require(path)
        _labeled_caption(doc, label, title)
        _add_table(doc, path, header_rows)
        if label == "Table S2":
            note_path = path.with_name("table-s2-note.txt")
            _require(note_path)
            note = note_path.read_text(encoding="utf-8").strip()
            if not note:
                raise SystemExit(f"{note_path} is empty")
            paragraph = doc.add_paragraph()
            _set_arial(paragraph.add_run("Note:"), True)
            _set_arial(paragraph.add_run(" " + note), False)
    _table_s4(doc, root)
    for label, title, name, header_rows in TABLES_AFTER:
        path = root / name
        _require(path)
        _labeled_caption(doc, label, title)
        _add_table(doc, path, header_rows)
    _table_s6(doc, root)

    dest = root / "figs_and_tables.docx"
    doc.save(dest)
    print(f"wrote {dest}")
    return dest


def _fit_mixed_models(day: str, sha: str) -> Path:
    """Use the current mixed-model fit when it was made from this roster.

    A new fit is run only when the roster sha256 differs from the one recorded
    in mixed-models/CURRENT. Table 1 and Table 2 still have to match the roster
    the figures are drawn from; an unchanged roster does not need a new fit.
    """
    from orchestration.fit_mixed_models import current_mixed_dir, main as fit, source_sha256

    try:
        existing = current_mixed_dir()
    except SystemExit:
        existing = None
    if existing is not None and existing.is_dir() and source_sha256(existing) == sha:
        print(f"mixed models already fit from this roster: {existing}")
        return existing
    mixed = fit(day)
    if source_sha256(mixed) != sha:
        raise SystemExit(f"{mixed} was fit from a roster with sha256 {source_sha256(mixed)}, not {sha}")
    return mixed


def main(date: str | None = None) -> Path:
    from orchestration.fill_roster_scores import assert_roster_matches_fill, refresh_roster

    fig = figure_dir(date)
    cohorts = [fig]
    os.environ["MANUSCRIPT_LABELED"] = "0"
    roster = refresh_roster()
    assert_roster_matches_fill()
    sha = roster_sha256(roster)
    _write_roster_sha(fig, roster)
    _fit_mixed_models(fig.parent.name, sha)
    # The every-fine-tune cohort is not part of the manuscript (23 Oct 2026):
    # _draw(fig, "All_models", labeled=False)
    _draw(fig, "", labeled=True)
    _funnels(cohorts)
    for cohort in cohorts:
        write_manuscript_docx(cohort)
    _verify_outputs(roster, sha, cohorts)
    rel = fig.relative_to(FIGURES_ROOT).as_posix()
    POINTER.write_text(rel + "\n", encoding="utf-8")
    print(f"all figures in {fig} come from {roster} sha256 {sha}; {POINTER} = {rel}")
    return fig


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--date", help="folder name under FIGURES/ (default: today, YYYY-MM-DD)")
    main(parser.parse_args().date)
