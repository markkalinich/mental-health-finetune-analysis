#!/usr/bin/env python3
"""Strict claim-by-claim audit for REVIEWER_2_EXPERIMENTS.md.

Exits non-zero on any structural failure. No warnings-as-pass.

One-liner (from repo root):
  .venv/bin/python reviewer_2_experiments/scripts/audit_all_claims.py
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R2 = ROOT / "reviewer_2_experiments"
PROV = R2 / "data/provenance"
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from lmstudio_override_utils import build_override_scan, index_entry_failures

MODELS_CSV = ROOT / "config/models_config.csv"
FAILURES: list[str] = []
SKIP_TABLE1_VARS = frozenset({"Intercept", "R²", "Adj R²", "N", "R2", "Adj R2"})
PRIMARY_TABLE1_TSV = ROOT / "results/statistics/table_1_f1_bonferroni_paste_format_primary_n127.tsv"

PARSE50_TAG = "parse50pct_per_task"
PARSE50_DIFF_MD = R2 / "results" / PARSE50_TAG / "table_1" / "table_s2_vs_primary_bonferroni_diff.md"
PRIMARY_FACET_STATS_CSV = (
    R2 / "results" / "primary_n127" / "figure_3" / "delta_f1_facet_plot_primary_n127_stats.csv"
)


def fail(msg: str) -> None:
    FAILURES.append(msg)


def enabled_count() -> int:
    return sum(
        1
        for r in csv.DictReader(MODELS_CSV.open(newline=""))
        if str(r.get("enabled", "")).lower() in ("true", "1", "yes")
    )


def guard_api_json(content: str) -> str:
    """Shape expected by _parse_guard_binary (full OpenAI chat completion blob)."""
    return json.dumps({"choices": [{"message": {"content": content}}]})


def audit_claim1() -> None:
    p = PROV / "all_models_gguf_sha256_audit.json"
    if not p.exists():
        fail("Claim 1: missing all_models_gguf_sha256_audit.json")
        return
    audit = json.loads(p.read_text())
    models = audit["models"]
    n = enabled_count()
    if len(models) != n:
        fail(f"Claim 1: audit has {len(models)} models, expected {n}")
    c = Counter(m["status"] for m in models)
    verified = c.get("VERIFIED_match", 0)
    skip_404 = sum(1 for m in models if m["status"] == "SKIP_hf_404")
    therapist = [m for m in models if m["lm_studio_id"] == "therapist1-gemma3-12b-qvo"]
    if verified != 123:
        fail(f"Claim 1: expected 123 VERIFIED_match, got {verified} ({dict(c)})")
    if skip_404 != 3:
        fail(f"Claim 1: expected 3 SKIP_hf_404 (template-only), got {skip_404}")
    if not therapist or therapist[0]["status"] != "SKIP_no_x_linked_etag":
        fail(f"Claim 1: therapist1-gemma3-12b-qvo not SKIP_no_x_linked_etag: {therapist}")
    template_ids = {
        "gemma-2-27b",
        "klyang_mentallama-chat-13b",
        "llama-3.1-8b-instruct-mental-health-classification",
    }
    skip404_ids = {m["lm_studio_id"] for m in models if m["status"] == "SKIP_hf_404"}
    if skip404_ids != template_ids:
        fail(f"Claim 1: SKIP_hf_404 ids {skip404_ids} != expected {template_ids}")
    tc = PROV / "hf_template_compare/q8_vs_smaller_quant_template_compare.json"
    if not tc.exists():
        fail("Claim 1: missing q8_vs_smaller_quant_template_compare.json")
        return
    rows = json.loads(tc.read_text())
    if len(rows) != 3:
        fail(f"Claim 1: template compare has {len(rows)} rows, expected 3")
    for row in rows:
        if not row.get("embedded_chat_template_match"):
            fail(f"Claim 1: template compare failed for {row.get('lm_studio_id')}")


def audit_claim2() -> None:
    ov_path = PROV / "all_models_lmstudio_jinja_overrides.json"
    emb_path = PROV / "all_models_gguf_embedded_templates.json"
    n = enabled_count()

    if not ov_path.exists():
        fail("Claim 2: missing all_models_lmstudio_jinja_overrides.json")
    else:
        ov = json.loads(ov_path.read_text())
        if len(ov.get("models", [])) != n:
            fail(f"Claim 2: override scan has {len(ov.get('models', []))} rows, expected {n}")
        holes = [
            m["lm_studio_id"]
            for m in ov["models"]
            if m.get("note") == "no_index_entry"
            or m.get("lmstudio_jinja_override") is None
            or not m.get("override_file")
            or not m.get("gguf_rel_path")
        ]
        if holes:
            fail(f"Claim 2: incomplete override rows ({len(holes)}): {holes}")
        override_ids = set(ov.get("models_with_jinja_override", []))
        expected = {
            "shieldgemma-2b",
            "shieldgemma-9b",
            "shieldgemma-27b",
            "shieldgemma-2-4b-it",
            "meta-llama_-_llama-guard-3-1b",
        }
        if override_ids != expected:
            fail(f"Claim 2: override ids {override_ids} != expected {expected}")
        no_ov = sum(1 for m in ov["models"] if m.get("lmstudio_jinja_override") is False)
        if no_ov != 122:
            fail(f"Claim 2: expected 122 non-override, got {no_ov}")

    # Off-disk embedded-template provenance: 95 GGUFs embed tokenizer.chat_template
    # (90 of the 122 non-override models + all 5 override models), 32 omit it.
    if not emb_path.exists():
        fail("Claim 2: missing all_models_gguf_embedded_templates.json")
    else:
        emb = json.loads(emb_path.read_text())
        models = emb.get("models", [])
        if len(models) != n:
            fail(
                f"Claim 2: off-disk embedded-template extraction has {len(models)} rows, "
                f"expected {n}"
            )
        has_t = sum(1 for m in models if m.get("has_template") is True)
        no_t = sum(1 for m in models if m.get("has_template") is False)
        if has_t != 95:
            fail(f"Claim 2: GGUFs embedding tokenizer.chat_template={has_t}, expected 95")
        if no_t != 32:
            fail(f"Claim 2: GGUFs without tokenizer.chat_template={no_t}, expected 32")


def audit_subtask1() -> None:
    p = PROV / "subtask1_embedded_templates.json"
    if not p.exists():
        fail("subtask1: missing subtask1_embedded_templates.json")
        return
    rows = json.loads(p.read_text())
    expected = {
        "shieldgemma-2b",
        "shieldgemma-9b",
        "shieldgemma-27b",
        "shieldgemma-2-4b-it",
        "meta-llama_-_llama-guard-3-1b",
        "llama-guard-3-8b",
        "qwen3guard-gen-0.6b",
        "qwen3guard-gen-4b",
        "qwen3guard-gen-8b",
    }
    ids = {r["lm_studio_id"] for r in rows}
    if ids != expected:
        fail(f"subtask1: ids {ids} != expected {expected}")
    for r in rows:
        if "embedded_chat_template" not in r:
            fail(f"subtask1: {r['lm_studio_id']} missing embedded_chat_template")


def audit_claim3() -> None:
    bt = R2 / "data/break_tests/shieldgemma_embedded_template_break_test.json"
    if not bt.exists():
        fail("Claim 3: missing shieldgemma break test JSON")
        return
    data = json.loads(bt.read_text())
    expected_ids = {
        "shieldgemma-2b",
        "shieldgemma-9b",
        "shieldgemma-27b",
        "shieldgemma-2-4b-it",
    }
    case_ids = {c["lm_studio_id"] for c in data.get("cases", [])}
    if case_ids != expected_ids:
        fail(f"Claim 3: break test cases {case_ids} != expected {expected_ids}")
    for case in data.get("cases", []):
        by_mode = {t["mode"]: t for t in case.get("tests", [])}
        baseline = by_mode.get("baseline_generic_override")
        embedded = by_mode.get("embedded_original_as_override")
        no_ov = by_mode.get("no_override_gguf_embedded")
        lid = case["lm_studio_id"]
        if not baseline or baseline.get("http_status") != 200:
            fail(f"Claim 3: {lid} baseline_generic_override not HTTP 200")
        for mode_name, t in (
            ("embedded_original_as_override", embedded),
            ("no_override_gguf_embedded", no_ov),
        ):
            if not t or t.get("http_status") != 400:
                fail(f"Claim 3: {lid} {mode_name} not HTTP 400 (got {t.get('http_status') if t else None})")
        if not case.get("restore_match"):
            fail(f"Claim 3: {lid} restore_match is false")
    fig = R2 / "results/shieldgemma/sg1_patched/figures/sg1_template_f1_delta_scatter.csv"
    if not fig.exists():
        fail("Claim 3: missing OLS scatter CSV")
    else:
        import pandas as pd
        from scipy.stats import linregress

        ols_df = pd.read_csv(fig)
        f1 = ols_df[ols_df["metric"] == "f1_score"].dropna(subset=["generic", "delta"])
        if len(f1) < 2:
            fail("Claim 3: OLS scatter CSV has fewer than 2 f1_score rows")
        else:
            slope, _, _, p, _ = linregress(
                f1["generic"].to_numpy(dtype=float),
                f1["delta"].to_numpy(dtype=float),
            )
            if not (-0.95 < slope < -0.70):
                fail(f"Claim 3: OLS slope={slope:.4f}, expected ~-0.83")
            if p >= 0.05:
                fail(f"Claim 3: OLS p={p:.6f}, expected < 0.05")
    cache = R2 / "cache/shieldgemma_sg1_patched/cache/results.db"
    if not cache.exists():
        fail("Claim 3: missing SG-1 patched cache")


def audit_claim4() -> None:
    bt = R2 / "data/break_tests/llama_guard_3_1b_break_test.json"
    if not bt.exists():
        fail("Claim 4: missing llama_guard break test JSON")
        return
    data = json.loads(bt.read_text())
    expected = {
        "baseline_override": ("ok_guard_safe_unsafe", 200),
        "embedded_as_override": ("jinja_render_error_http400", 400),
        "no_override_gguf_embedded": ("jinja_render_error_http400", 400),
    }
    by_mode = {t["mode"]: t for t in data.get("tests", [])}
    for mode, (exp_outcome, exp_status) in expected.items():
        if mode not in by_mode:
            fail(f"Claim 4: break test missing mode {mode!r}")
            continue
        t = by_mode[mode]
        if t.get("outcome") != exp_outcome:
            fail(f"Claim 4: {mode} outcome={t.get('outcome')!r}, expected {exp_outcome!r}")
        if t.get("http_status") != exp_status:
            fail(f"Claim 4: {mode} http_status={t.get('http_status')!r}, expected {exp_status}")
    if not data.get("restore_match"):
        fail("Claim 4: break test restore_match is false")
    if not data.get("embedded_jinja_sha256_match"):
        fail("Claim 4: embedded_jinja_sha256_match is false")


GUARD_PIPELINE_TASKS = [
    (
        "suicidal_ideation",
        ROOT / "data/inputs/finalized_input_data/SI_finalized_sentences.csv",
        ROOT / "data/prompts/system_suicide_detection_v2.txt",
    ),
    (
        "therapy_request",
        ROOT / "data/inputs/finalized_input_data/therapy_request_finalized_sentences.csv",
        ROOT / "data/prompts/therapy_request_classifier_v3.txt",
    ),
    (
        "therapy_engagement",
        ROOT / "data/inputs/finalized_input_data/therapy_engagement_finalized_sentences.csv",
        ROOT / "data/prompts/therapy_engagement_conversation_prompt_v2.txt",
    ),
]
GUARD_MODELS = {"llama_guard": ["1b", "8b"], "qwen_guard": ["0.6b", "4b", "8b"]}


def _compute_facet_stats(config_csv: Path, results_csv: Path):
    """Bonferroni facet stats using the same logic as combined_finetune_facet_plot."""
    import pandas as pd
    from scipy import stats as scipy_stats

    sys.path.insert(0, str(ROOT))
    import analysis.combined_finetune_facet_plot as cffp

    config = pd.read_csv(config_csv)
    config = config[config["enabled"] == True].copy()
    results = pd.read_csv(results_csv)
    stats_records = []

    for ft_config in cffp.FINETUNE_TYPES:
        df = cffp.compute_deltas(
            config, results, ft_config["filter"], "f1_score", "f1"
        )
        for task in cffp.TASKS:
            task_data = df[df["task"] == task]
            n_testable = sum(
                1
                for fam in cffp.FAMILIES
                if len(task_data[task_data["family"] == fam]) >= 2
            )
            for fam in cffp.FAMILIES:
                fam_data = task_data[task_data["family"] == fam]
                if len(fam_data) >= 2:
                    _, p = scipy_stats.ttest_rel(
                        fam_data["ft_f1"].values, fam_data["base_f1"].values
                    )
                    p_adjusted = min(p * n_testable, 1.0) if n_testable > 0 else 1.0
                    stats_records.append(
                        {
                            "finetune_type": ft_config["label"],
                            "task": cffp.TASK_TITLES[task],
                            "model_family": cffp.FAMILY_LABELS[fam],
                            "n_pairs": len(fam_data),
                            "mean_delta_f1": float(fam_data["delta_f1"].mean()),
                            "significant": p_adjusted < 0.05,
                        }
                    )
    return pd.DataFrame(stats_records)


def _compute_all_pair_deltas(config_csv: Path, results_csv: Path):
    """Per fine-tune/base pair ΔF1 rows (same keys as Figure 3 scatter points)."""
    import pandas as pd

    sys.path.insert(0, str(ROOT))
    import analysis.combined_finetune_facet_plot as cffp

    config = pd.read_csv(config_csv)
    config = config[config["enabled"] == True].copy()
    results = pd.read_csv(results_csv)
    rows = []
    for ft_config in cffp.FINETUNE_TYPES:
        df = cffp.compute_deltas(
            config, results, ft_config["filter"], "f1_score", "f1"
        )
        for _, r in df.iterrows():
            rows.append(
                {
                    "ft_type": ft_config["label"],
                    "task": r["task"],
                    "ft_family": r["ft_family"],
                    "ft_size": r["ft_size"],
                    "delta_f1": float(r["delta_f1"]),
                }
            )
    return pd.DataFrame(rows)


def _facet_sig_set(df) -> set[tuple[str, str, str]]:
    """Set of (finetune_type, task, model_family) for Bonferroni-significant facet cells.

    Accepts either a recomputed stats frame or a committed CSV; normalizes the
    `significant` column whether it is read back as bool or as a string.
    """
    sig_mask = df["significant"].astype(str).str.lower() == "true"
    sub = df[sig_mask]
    return {
        (str(r["finetune_type"]), str(r["task"]), str(r["model_family"]))
        for _, r in sub.iterrows()
    }


def _bonferroni_sig_from_filtered_csv(csv_path: Path) -> list[str]:
    import pandas as pd

    df = pd.read_csv(csv_path)
    sig: list[str] = []
    for _, row in df.iterrows():
        var = str(row["Variable"])
        if var in SKIP_TABLE1_VARS or var.startswith("R"):
            continue
        for col, task in (("SI-β", "SI"), ("TR-β", "TR"), ("TE-β", "TE")):
            if col in row and re.search(r"\*", str(row[col])):
                sig.append(f"{var} ({task})")
    return sig


def _bonferroni_sig_from_primary_tsv(tsv_path: Path) -> list[str]:
    sig: list[str] = []
    with tsv_path.open(newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    for row in rows[2:]:
        if not row or not row[0].strip():
            continue
        var = row[0].strip()
        if var in SKIP_TABLE1_VARS or var.startswith("R") or var == "N":
            continue
        for idx, task in ((1, "SI"), (3, "TR"), (5, "TE")):
            if idx < len(row) and re.search(r"\*", row[idx]):
                sig.append(f"{var} ({task})")
    return sig


def _write_table_s2_diff_md(
    primary_sig: list[str],
    filtered_sig: list[str],
    out_path: Path,
    *,
    tag: str,
    parse_pct: int,
    interpretation: str,
) -> None:
    primary_set = set(primary_sig)
    filtered_set = set(filtered_sig)
    retained = sorted(primary_set & filtered_set)
    lost = sorted(primary_set - filtered_set)
    gained = sorted(filtered_set - primary_set)
    lines = [
        "# Table S2 vs primary Table 1 — Bonferroni-significant F1 coefficients",
        "",
        "Auto-generated by `audit_all_claims.py` (Claim 6). "
        f"Stars match `multivariable_regression_f1_bonferroni_{tag}.csv` "
        "and `results/statistics/table_1_f1_bonferroni_paste_format_primary_n127.tsv`.",
        "",
        f"- **Primary Table 1 (N=127):** {len(primary_sig)} Bonferroni-sig coefficients",
        f"- **Table S2 (parse≥{parse_pct}% per-task):** {len(filtered_sig)} Bonferroni-sig coefficients",
        "",
        "## Retained in both (still significant after filter)",
        "",
    ]
    lines.extend(f"- {x}" for x in retained) if retained else lines.append("- *(none)*")
    lines.extend(
        ["", f"## Significant in primary only (lost after parse≥{parse_pct}% filter)", ""]
    )
    lines.extend(f"- {x}" for x in lost) if lost else lines.append("- *(none)*")
    lines.extend(["", "## Significant in Table S2 only (newly significant)", ""])
    lines.extend(f"- {x}" for x in gained) if gained else lines.append("- *(none)*")
    lines.extend(["", "## Interpretation", "", interpretation, ""])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")


def audit_claim5() -> None:
    sys.path.insert(0, str(ROOT))
    from analysis.model_performance.data_loader import (
        GUARD_FAMILIES,
        _parse_guard_binary,
        load_experiment_results,
    )

    if GUARD_FAMILIES != {"llama_guard", "qwen_guard"}:
        fail(f"Claim 5: GUARD_FAMILIES={GUARD_FAMILIES}")

    # _parse_guard_binary expects a full API JSON string, not bare message text.
    cases = [
        ("\n\nsafe", 0),
        ("unsafe\nS11", 1),
        ("Safety: Safe\nCategories: None", 0),
        ("Safety: Unsafe\nCategories: Suicide & Self-Harm", 1),
    ]
    for content, expected in cases:
        got = _parse_guard_binary(guard_api_json(content))
        if got != expected:
            fail(f"Claim 5: _parse_guard_binary({content!r}) = {got}, expected {expected}")

    db = ROOT / "cache/results.db"
    if not db.exists():
        fail("Claim 5: cache/results.db missing")
        return
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    examples = [
        ("llama_guard", "1b", "therapy_request_classifier_v3", 0),
        ("llama_guard", "1b", "system_suicide_detection_v2", 1),
        ("qwen_guard", "0.6b", "therapy_request_classifier_v3", 0),
        ("qwen_guard", "0.6b", "system_suicide_detection_v2", 1),
    ]
    for family, size, prompt, exp_bin in examples:
        row = conn.execute(
            """
            SELECT cr.raw_response
            FROM cached_results cr JOIN cache_keys ck ON cr.cache_id = ck.cache_id
            WHERE ck.model_family=? AND ck.model_size=? AND ck.prompt_name=?
            LIMIT 1
            """,
            (family, size, prompt),
        ).fetchone()
        if not row:
            fail(f"Claim 5: no DB row for {family}/{size}/{prompt}")
            continue
        got = _parse_guard_binary(row["raw_response"])
        if got != exp_bin:
            fail(
                f"Claim 5: DB _parse_guard_binary({family}/{size}/{prompt}) = {got}, "
                f"expected {exp_bin}"
            )

    # Full pipeline: load_experiment_results from cache/results.db applies guard re-parse.
    for experiment_type, input_csv, prompt_path in GUARD_PIPELINE_TASKS:
        if not input_csv.exists() or not prompt_path.exists():
            fail(f"Claim 5: missing inputs for {experiment_type}")
            continue
        try:
            df, _ = load_experiment_results(
                str(input_csv),
                str(prompt_path),
                GUARD_MODELS,
                experiment_type,
                cache_dir=str(ROOT / "cache"),
            )
        except Exception as exc:
            fail(f"Claim 5: load_experiment_results({experiment_type}) failed: {exc}")
            continue
        guard_df = df[df["model_family"].isin(GUARD_FAMILIES)]
        if guard_df.empty:
            fail(f"Claim 5: no guard rows loaded for {experiment_type}")
            continue
        n_fail = int((guard_df["status"] == "parse_fail").sum())
        if n_fail:
            fail(
                f"Claim 5: {experiment_type} has {n_fail}/{len(guard_df)} guard rows "
                "still parse_fail after pipeline load"
            )
        shield_in_df = df[df["model_family"] == "shieldgemma"]
        if len(shield_in_df):
            fail("Claim 5: shieldgemma unexpectedly present in guard-only load")

    print(
        "  Claim 5: full guard pipeline load OK "
        f"({len(GUARD_PIPELINE_TASKS)} tasks, cache/results.db)"
    )


def _audit_parse_cohort(
    *,
    claim_prefix: str,
    tag: str,
    parse_pct: int,
    per_task_counts: dict[str, int],
    results_rows: int,
    pair_count: int,
    filtered_sig_facets: int,
    primary_sig_facets: int = 9,
    primary_instr_sig: int | None = None,
    table_sig_count: int | None = None,
    expected_table_sig: set[str] | None = None,
    diff_md: Path | None = None,
    diff_interpretation: str = "",
) -> None:
    import pandas as pd

    cohort = R2 / "results" / tag / "cohort" / f"models_config_{tag}.json"
    if not cohort.exists():
        fail(f"{claim_prefix}: missing cohort JSON")
        return
    data = json.loads(cohort.read_text())
    counts = data.get("summary", {}).get("per_task_model_counts", {})
    if counts != per_task_counts:
        fail(f"{claim_prefix}: per_task_model_counts={counts}, expected {per_task_counts}")

    csv_path = R2 / "results" / tag / "cohort" / f"all_models_all_tasks_{tag}.csv"
    if not csv_path.exists():
        fail(f"{claim_prefix}: missing filtered results CSV")
        return
    df = pd.read_csv(csv_path)
    if len(df) != results_rows:
        fail(f"{claim_prefix}: filtered CSV has {len(df)} rows, expected {results_rows}")

    stats_path = R2 / "results" / tag / "figure_3" / f"delta_f1_facet_plot_{tag}_stats.csv"
    table_path = (
        R2 / "results" / tag / "table_1" / f"multivariable_regression_f1_bonferroni_{tag}.csv"
    )
    if not stats_path.exists():
        fail(f"{claim_prefix}: missing figure 3 stats CSV")
    if not table_path.exists():
        fail(f"{claim_prefix}: missing Table S2 regression CSV")

    primary_config = ROOT / "config/models_config.csv"
    primary_results = ROOT / "data/inputs/model_results/all_models_all_tasks.csv"
    filtered_config = R2 / "results" / tag / "cohort" / f"models_config_{tag}.csv"
    if not primary_results.exists():
        fail(f"{claim_prefix}: missing primary all_models_all_tasks.csv")
        return

    primary_stats = _compute_facet_stats(primary_config, primary_results)
    filtered_stats = _compute_facet_stats(filtered_config, csv_path)
    committed_filtered = pd.read_csv(stats_path)
    committed_sig = int((committed_filtered["significant"] == True).sum())
    filtered_sig = int(filtered_stats["significant"].sum())
    primary_sig = int(primary_stats["significant"].sum())

    if filtered_sig != committed_sig:
        fail(
            f"{claim_prefix}: recomputed filtered sig cells={filtered_sig}, "
            f"committed stats CSV={committed_sig}"
        )
    if primary_sig != primary_sig_facets:
        fail(
            f"{claim_prefix}: primary N=127 facet sig cells={primary_sig}, "
            f"expected {primary_sig_facets}"
        )
    if filtered_sig != filtered_sig_facets:
        fail(
            f"{claim_prefix}: filtered parse≥{parse_pct}% facet sig cells={filtered_sig}, "
            f"expected {filtered_sig_facets}"
        )

    # Regression-protect the committed primary N=127 facet stats and the Figure S12
    # claim: instruction-tuning is Bonferroni-significant in the primary paired
    # analysis but no longer significant under the parse filter.
    recomputed_primary_set = _facet_sig_set(primary_stats)
    filtered_set = _facet_sig_set(filtered_stats)
    if not PRIMARY_FACET_STATS_CSV.exists():
        fail(f"{claim_prefix}: missing committed primary N=127 facet stats CSV")
    else:
        committed_primary = pd.read_csv(PRIMARY_FACET_STATS_CSV)
        committed_primary_set = _facet_sig_set(committed_primary)
        if committed_primary_set != recomputed_primary_set:
            fail(
                f"{claim_prefix}: committed primary facet sig cells {committed_primary_set} "
                f"!= recomputed {recomputed_primary_set}"
            )
        if len(committed_primary_set) != primary_sig_facets:
            fail(
                f"{claim_prefix}: committed primary facet sig count="
                f"{len(committed_primary_set)}, expected {primary_sig_facets}"
            )
    primary_instr = {c for c in recomputed_primary_set if c[0] == "Instruction-Tuned"}
    filtered_instr = {c for c in filtered_set if c[0] == "Instruction-Tuned"}
    if primary_instr_sig is not None and len(primary_instr) != primary_instr_sig:
        fail(
            f"{claim_prefix}: primary instruction-tuned sig cells={len(primary_instr)} "
            f"({sorted(primary_instr)}), expected {primary_instr_sig}"
        )
    if filtered_instr:
        fail(
            f"{claim_prefix}: instruction-tuned still significant under parse≥{parse_pct}% "
            f"filter: {sorted(filtered_instr)} (expected none)"
        )

    primary_pairs = _compute_all_pair_deltas(primary_config, primary_results)
    filtered_pairs = _compute_all_pair_deltas(filtered_config, csv_path)
    if len(filtered_pairs) != pair_count:
        fail(f"{claim_prefix}: filtered pair count={len(filtered_pairs)}, expected {pair_count}")
    merged = filtered_pairs.merge(
        primary_pairs,
        on=["ft_type", "task", "ft_family", "ft_size"],
        suffixes=("_filt", "_prim"),
        how="left",
    )
    if len(merged) != len(filtered_pairs):
        fail(f"{claim_prefix}: filtered pairs missing from primary cohort")
    sign_flips = merged[(merged["delta_f1_filt"] * merged["delta_f1_prim"]) < 0]
    if len(sign_flips):
        examples = sign_flips.head(5).to_dict("records")
        fail(
            f"{claim_prefix}: {len(sign_flips)} pair-level ΔF1 sign inversions vs primary: "
            f"{examples}"
        )

    if PRIMARY_TABLE1_TSV.exists():
        primary_table_sig = _bonferroni_sig_from_primary_tsv(PRIMARY_TABLE1_TSV)
        filtered_table_sig = _bonferroni_sig_from_filtered_csv(table_path)
        if len(primary_table_sig) != 14:
            fail(
                f"{claim_prefix}: primary Table 1 Bonferroni sig count={len(primary_table_sig)}, "
                f"expected 14"
            )
        if table_sig_count is not None and len(filtered_table_sig) != table_sig_count:
            fail(
                f"{claim_prefix}: Table S2 Bonferroni sig count={len(filtered_table_sig)}, "
                f"expected {table_sig_count}: {filtered_table_sig}"
            )
        if expected_table_sig is not None and set(filtered_table_sig) != expected_table_sig:
            fail(
                f"{claim_prefix}: Table S2 sig coeffs {set(filtered_table_sig)} != "
                f"expected {expected_table_sig}"
            )
        if diff_md is not None:
            _write_table_s2_diff_md(
                primary_table_sig,
                filtered_table_sig,
                diff_md,
                tag=tag,
                parse_pct=parse_pct,
                interpretation=diff_interpretation,
            )

    for label, stats_df in (("primary", primary_stats), ("filtered", filtered_stats)):
        for task in ("Therapy Request", "Therapy Engagement"):
            row = stats_df[
                (stats_df["finetune_type"] == "Safety")
                & (stats_df["model_family"] == "Qwen")
                & (stats_df["task"] == task)
            ]
            if row.empty:
                fail(f"{claim_prefix}: missing Safety/Qwen/{task} facet row ({label})")
                continue
            mean_d = float(row.iloc[0]["mean_delta_f1"])
            if mean_d >= 0:
                fail(
                    f"{claim_prefix}: Safety/Qwen/{task} mean ΔF1={mean_d:.4f} ({label}), "
                    "expected negative"
                )

    n_table_sig = len(_bonferroni_sig_from_filtered_csv(table_path))
    print(
        f"  {claim_prefix}: Table S2 Bonferroni sig 14→{n_table_sig}; "
        f"Figure 3 facet sig {primary_sig}→{filtered_sig}; "
        f"instruction-tuned facet sig {len(primary_instr)}→{len(filtered_instr)}; "
        f"pair-level sign inversions=0 ({len(filtered_pairs)} pairs); "
        f"Safety/Qwen TR+TE ΔF1 negative in both cohorts"
    )


def audit_claim6() -> None:
    """Manuscript sensitivity (parse≥50% per-task)."""
    _audit_parse_cohort(
        claim_prefix="Claim 6 (parse≥50%)",
        tag=PARSE50_TAG,
        parse_pct=50,
        per_task_counts={
            "suicidal_ideation": 91,
            "therapy_request": 84,
            "therapy_engagement": 99,
        },
        results_rows=274,
        pair_count=150,
        filtered_sig_facets=4,
        primary_sig_facets=9,
        primary_instr_sig=4,
        table_sig_count=10,
        expected_table_sig={
            "Family: LLaMA (TR)",
            "Fine-Tune Type: Safety-Tuned (SI)",
            "Parameter Size (B) (SI)",
            "Parameter Size (B) (TR)",
            "Version: 3 (SI)",
            "Version: 3 (TE)",
            "Version: 3 (TR)",
            "Version: 4 (SI)",
            "Version: 4 (TE)",
            "Version: 4 (TR)",
        },
        diff_md=PARSE50_DIFF_MD,
        diff_interpretation=(
            "Parse≥50% per-task filtering excludes models with low JSON compliance on that task "
            "while retaining most of the cohort. Parameter scale and model version remain "
            "statistically significant; instruction-tuning coefficients on therapy request and "
            "therapy engagement are no longer statistically significant. Safety-tuned models "
            "show a significant association with higher suicidal-ideation F1 only."
        ),
    )


def audit_live_override_scan() -> None:
    """Live LM Studio index scan must resolve all 127 (crosswalk-aware)."""
    try:
        live = build_override_scan(MODELS_CSV)
    except FileNotFoundError as e:
        fail(f"Live override scan: {e}")
        return
    gaps = index_entry_failures(live["models"])
    if gaps:
        fail(f"Live override scan: index gaps ({len(gaps)}): {gaps}")


def audit_live_template_compare() -> None:
    """Re-fetch HF templates for 3 Q8-orphan models and compare to committed JSON."""
    from run_q8_orphan_template_compare import build_compare, compare_to_committed

    committed_path = PROV / "hf_template_compare/q8_vs_smaller_quant_template_compare.json"
    if not committed_path.exists():
        fail("Live template compare: missing committed JSON")
        return
    committed = json.loads(committed_path.read_text())
    live = build_compare()
    errors = compare_to_committed(live, committed)
    if errors:
        fail(f"Live template compare: {'; '.join(errors)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit all REVIEWER_2_EXPERIMENTS.md claims")
    parser.add_argument(
        "--skip-live",
        action="store_true",
        help="Skip live LM Studio index + HF network checks (artifact-only)",
    )
    args = parser.parse_args()

    n = enabled_count()
    print(f"Enabled models in CSV: {n}")
    audit_claim1()
    audit_claim2()
    audit_subtask1()
    audit_claim3()
    audit_claim4()
    audit_claim5()
    audit_claim6()
    if not args.skip_live:
        audit_live_override_scan()
        audit_live_template_compare()

    if FAILURES:
        print("\n=== AUDIT FAILURES ===", file=sys.stderr)
        for f in FAILURES:
            print(f"  FAIL: {f}", file=sys.stderr)
        return 1
    scope = "artifact + live" if not args.skip_live else "artifact-only"
    print(f"\n=== AUDIT PASS ({scope}): all claims verified ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
