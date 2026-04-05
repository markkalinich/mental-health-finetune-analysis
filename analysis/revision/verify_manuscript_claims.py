#!/usr/bin/env python3
"""
Verify every numeric claim in the manuscript against pipeline output data.

Reads from the latest FINETUNE_PAPER_FIGURES run and writes a Markdown
report with PASS/FAIL for each extracted numeric assertion.

Usage:
    python analysis/revision/verify_manuscript_claims.py [--run-dir DIR]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

TOLERANCE = 0.015
TASK_SHORT = {"Suicidal Ideation": "SI", "Therapy Request": "TR",
              "Therapy Engagement": "TE"}


def _close(actual: float, claimed: float, tol: float = TOLERANCE) -> bool:
    if pd.isna(actual) or not np.isfinite(actual):
        return False
    return abs(actual - claimed) <= tol


def _sig_match(actual_p: float, claimed_bucket: str) -> bool:
    claimed = claimed_bucket.strip().lower().replace(" ", "")
    if claimed in ("<.001", "<0.001"):
        return actual_p < 0.001
    if claimed in ("<.01", "<0.01"):
        return actual_p < 0.01
    if claimed in ("<.05", "<0.05"):
        return actual_p < 0.05
    if claimed in ("ns", "nonsignificant", "notsignificant"):
        return actual_p >= 0.05
    return False


class Report:
    def __init__(self):
        self.sections: list[str] = []
        self.n_pass = 0
        self.n_fail = 0

    def section(self, title: str):
        self.sections.append(f"\n## {title}\n")

    def quote(self, text: str):
        for line in text.strip().split("\n"):
            self.sections.append(f"> {line.strip()}")
        self.sections.append("")

    def check(self, desc: str, passed: bool, actual: str = "", claimed: str = ""):
        icon = "✅" if passed else "❌"
        if passed:
            self.n_pass += 1
        else:
            self.n_fail += 1
        line = f"- {icon} **{desc}**"
        if claimed:
            line += f"  \n  Claimed: `{claimed}`"
        if actual:
            line += f" → Actual: `{actual}`"
        self.sections.append(line)

    def render(self) -> str:
        header = (
            "# Manuscript Claim Verification\n\n"
            f"**Summary: {self.n_pass} PASS, {self.n_fail} FAIL** "
            f"({self.n_pass}/{self.n_pass + self.n_fail} checks)\n"
        )
        return header + "\n".join(self.sections) + "\n"


# ---------------------------------------------------------------------------
# Clinician Concordance
# ---------------------------------------------------------------------------
def verify_clinician_concordance(run_dir: Path, rpt: Report):
    rpt.section("Clinician Concordance")
    rpt.quote(
        "We first assessed inter-clinician agreement in the quality of "
        "LLM-generated statements. Among items where both clinicians evaluated "
        "identical text, the second clinician accepted the original wording "
        "without modification in 96.8% (796/822, 95% CI 95.4–97.8%) of "
        "suicidal ideation statements, 99.0% (1,108/1,119, 98.2–99.5%) of "
        "therapy request statements, and 98.1% (356/363, 96.1–99.1%) of "
        "therapy engagement conversations."
    )
    df = pd.read_csv(run_dir / "revision_data" / "p2_agreement_given_p1_exact_match.csv")

    claims = [
        ("Suicidal ideation", 796, 822, 96.8, 95.4, 97.8),
        ("Therapy request", 1108, 1119, 99.0, 98.2, 99.5),
        ("Therapy engagement", 356, 363, 98.1, 96.1, 99.1),
    ]
    for label, c_pos, c_n, c_pct, c_ci_lo, c_ci_hi in claims:
        row = df[df["dataset"].str.contains(label, case=False)].iloc[0]
        a_n = int(row["n"])
        a_pos = int(row["n_positive"])
        a_pct = round(row["proportion"] * 100, 1)
        a_lo = round(row["ci95_lower"] * 100, 1)
        a_hi = round(row["ci95_upper"] * 100, 1)

        rpt.check(f"{label}: n", a_n == c_n, str(a_n), str(c_n))
        rpt.check(f"{label}: n_positive", a_pos == c_pos, str(a_pos), str(c_pos))
        rpt.check(f"{label}: proportion %", _close(a_pct, c_pct, 0.1),
                  f"{a_pct}%", f"{c_pct}%")
        rpt.check(f"{label}: CI lower", _close(a_lo, c_ci_lo, 0.15),
                  f"{a_lo}%", f"{c_ci_lo}%")
        rpt.check(f"{label}: CI upper", _close(a_hi, c_ci_hi, 0.15),
                  f"{a_hi}%", f"{c_ci_hi}%")


# ---------------------------------------------------------------------------
# Figure 2
# ---------------------------------------------------------------------------
def verify_figure2(run_dir: Path, rpt: Report):
    rpt.section("Figure 2 — F1 vs Parameters")
    rpt.quote(
        "Linear regression on log-transformed parameter counts revealed "
        "significant positive associations for six of nine family-task "
        "combinations after Bonferroni correction for multiple hypothesis "
        "testing. Gemma models showed the most consistent scaling benefits, "
        "with significant improvements across all three classification tasks: "
        "suicidal ideation (R² = 0.26, padjusted < 0.01), therapy request "
        "(R² = 0.23, padjusted < 0.01), and therapy engagement (R² = 0.27, "
        "padjusted < 0.01). Qwen models exhibited the strongest parameter "
        "scaling effect for suicidal ideation detection (R² = 0.32, padjusted "
        "< 0.01), while LLaMA models showed significant improvement only for "
        "therapy request classification (R² = 0.31, padjusted < 0.05). The "
        "remaining three family-task combinations (LLaMA suicidal ideation and "
        "therapy engagement, Qwen therapy request) showed positive but "
        "non-significant trends."
    )
    df = pd.read_csv(
        run_dir / "figure_2" / "supplemental_plots" / "fig2_regression_statistics.csv")
    overall = df[(df["plot_type"] == "f1_vs_params_overall_trend") &
                 (df["trendline_type"] == "overall")]

    N_BONF = 9  # 3 families × 3 tasks

    claims_sig = [
        ("gemma", "suicidal_ideation", 0.26, "< .01"),
        ("gemma", "therapy_request", 0.23, "< .01"),
        ("gemma", "therapy_engagement", 0.27, "< .01"),
        ("qwen", "suicidal_ideation", 0.32, "< .01"),
        ("llama", "therapy_request", 0.31, "< .05"),
    ]
    fam_names = {"gemma": "Gemma", "llama": "LLaMA", "qwen": "Qwen"}
    task_names = {"suicidal_ideation": "Suicidal Ideation",
                  "therapy_request": "Therapy Request",
                  "therapy_engagement": "Therapy Engagement"}

    for fam, task, c_r2, c_sig in claims_sig:
        row = overall[(overall["family"] == fam) & (overall["task"] == task)].iloc[0]
        a_r2 = round(row["r_squared"], 2)
        p_adj = min(row["p_value"] * N_BONF, 1.0)
        label = f"{fam_names[fam]}: {task_names[task]}"

        rpt.check(f"{label}: R²={c_r2}", _close(a_r2, c_r2, 0.02),
                  f"R²={a_r2}", f"R²={c_r2}")
        rpt.check(f"{label}: p {c_sig}", _sig_match(p_adj, c_sig),
                  f"p_adj={p_adj:.4f}", c_sig)

    sig_count = sum(1 for _, r in overall.iterrows()
                    if min(r["p_value"] * N_BONF, 1.0) < 0.05)
    rpt.check("6 of 9 significant (×9 Bonferroni)", sig_count == 6,
              str(sig_count), "6")

    nonsig = [("llama", "suicidal_ideation"), ("llama", "therapy_engagement"),
              ("qwen", "therapy_request")]
    for fam, task in nonsig:
        row = overall[(overall["family"] == fam) & (overall["task"] == task)].iloc[0]
        p_adj = min(row["p_value"] * N_BONF, 1.0)
        label = f"{fam_names[fam]}: {task_names[task]} non-significant"
        rpt.check(label, p_adj >= 0.05, f"p_adj={p_adj:.4f}")


# ---------------------------------------------------------------------------
# Table 1
# ---------------------------------------------------------------------------
def verify_table1(run_dir: Path, rpt: Report):
    rpt.section("Table 1 — Regression Coefficients")
    rpt.quote(
        "Newer model architecture versions demonstrated a statistically "
        "significant association with model performance (F1 score) across all "
        "tasks. Although Version 2 models only showed a significant difference "
        "relative to Version 1 for therapy request (β = 0.31, padjusted < .05) "
        "and therapy engagement detection (β = 0.34, padjusted < .05), Version 3 "
        "models showed significantly higher F1 scores for suicidal ideation "
        "detection (β = 0.36, padjusted < .001), therapy request detection "
        "(β = 0.35, padjusted < .001), and therapy engagement detection "
        "(β = 0.37, padjusted < .001) relative to Version 1. Version 4 models "
        "demonstrated even larger improvements (suicidal ideation: β = 0.52, "
        "p < .01; therapy request: β = 0.59, p < .001; therapy engagement: "
        "β = 0.62, padjusted < .001). The number of parameters in the model was "
        "significant for SI and therapy-request detection, but not for "
        "therapy-engagement detection. Relative to the base, pre-trained models, "
        "mental health fine-tuning did not demonstrate statistically significant "
        "improvements on any of the three tasks. Models that were post-trained "
        "for general instruction following were associated with significantly "
        "higher F1 scores for therapy request (β = 0.37, padjusted < .001) and "
        "therapy engagement (β = 0.32, padjusted < .01) tasks, but not for "
        "suicidal ideation detection. No safety-tuned models showed statistically "
        "significant improvements. Model family (LLaMA vs. Gemma, Qwen vs. "
        "Gemma) generally did not significantly predict performance, with the "
        "exception of LLaMA showing lower therapy request F1 scores compared to "
        "Gemma (β = -0.22, p < .05)."
    )
    coeff = pd.read_csv(ROOT / "results" / "statistics" / "all_coefficients.csv")
    f1 = coeff[coeff["DV"] == "F1 Score"].copy()

    def _get(task: str, var: str) -> pd.Series:
        return f1[(f1["Task"] == task) & (f1["Variable"] == var)].iloc[0]

    beta_claims = [
        ("Version: 2", "Suicidal Ideation", None, "NS"),
        ("Version: 2", "Therapy Request", 0.31, "< .05"),
        ("Version: 2", "Therapy Engagement", 0.34, "< .05"),
        ("Version: 3", "Suicidal Ideation", 0.36, "< .001"),
        ("Version: 3", "Therapy Request", 0.35, "< .001"),
        ("Version: 3", "Therapy Engagement", 0.37, "< .001"),
        ("Version: 4", "Suicidal Ideation", 0.52, "< .01"),
        ("Version: 4", "Therapy Request", 0.59, "< .001"),
        ("Version: 4", "Therapy Engagement", 0.62, "< .001"),
        ("Fine-Tune Type: Instruction-Tuned", "Suicidal Ideation", None, "NS"),
        ("Fine-Tune Type: Instruction-Tuned", "Therapy Request", 0.37, "< .001"),
        ("Fine-Tune Type: Instruction-Tuned", "Therapy Engagement", 0.32, "< .01"),
        ("Fine-Tune Type: Safety-Tuned", "Suicidal Ideation", None, "NS"),
        ("Fine-Tune Type: Safety-Tuned", "Therapy Request", None, "NS"),
        ("Fine-Tune Type: Safety-Tuned", "Therapy Engagement", None, "NS"),
        ("Family: LLaMA", "Therapy Request", -0.22, "< .05"),
    ]

    for var, task, c_beta, c_sig in beta_claims:
        row = _get(task, var)
        a_beta = round(row["β"], 2)
        a_p = row["p_bonferroni"]
        label = f"{var}: {task}"

        if c_beta is not None:
            rpt.check(f"{label}: β={c_beta}", _close(a_beta, c_beta, 0.02),
                      f"β={a_beta}", f"β={c_beta}")
        rpt.check(f"{label}: p {c_sig}", _sig_match(a_p, c_sig),
                  f"p_bonf={a_p:.4f}", c_sig)

    for task in ["Suicidal Ideation", "Therapy Request", "Therapy Engagement"]:
        row = _get(task, "Fine-Tune Type: Mental Health Tuned")
        rpt.check(f"Fine-Tune Type: Mental Health Tuned: {task} not significant",
                  row["p_bonferroni"] >= 0.05,
                  f"p_bonf={row['p_bonferroni']:.4f}")

    for task, should_sig in [("Suicidal Ideation", True),
                              ("Therapy Request", True),
                              ("Therapy Engagement", False)]:
        row = _get(task, "Parameter Size (B)")
        is_sig = row["p_bonferroni"] < 0.05
        label = f"Parameter Size (B): {task} {'significant' if should_sig else 'not significant'}"
        rpt.check(label, is_sig == should_sig, f"p_bonf={row['p_bonferroni']:.4f}")


# ---------------------------------------------------------------------------
# Table 1 Summary
# ---------------------------------------------------------------------------
def verify_table1_summary(run_dir: Path, rpt: Report):
    rpt.section("Table 1 Summary — R² and Effect Sizes")
    rpt.quote(
        "Overall, model version (Version 4 vs Version 1) showed effect sizes "
        "in the β ≈ 0.52–0.65 range across tasks. Parameter count (significant "
        "for suicidal ideation and therapy request) corresponded to an estimated "
        "~0.5–0.6 increase in F1 across the observed ~70B parameter range, "
        "comparable in magnitude to version-related differences; for therapy "
        "engagement, the parameter effect was not significant, and version "
        "remained the dominant signal. Fine-tuning associations were smaller "
        "and more heterogeneous: instruction tuning was associated with higher "
        "F1 on two of three tasks, safety tuning showed the largest effect for "
        "therapy request only, medical tuning showed a smaller therapy-request–"
        "specific association, and mental health tuning was not significant for "
        "any task. Model family effects were not statistically significant "
        "across tasks, with the exception of a significant negative association "
        "for LLaMA relative to Gemma on therapy-request classification. Overall, "
        "these models explained 34–49% of the variance in F1 scores "
        "(R² = 0.31–0.46), with therapy request prediction showing the "
        "strongest model fit."
    )
    coeff = pd.read_csv(ROOT / "results" / "statistics" / "all_coefficients.csv")
    f1 = coeff[coeff["DV"] == "F1 Score"]

    # Version 4 β range ≈ 0.52–0.65
    v4_betas = {}
    for task in ["Suicidal Ideation", "Therapy Request", "Therapy Engagement"]:
        row = f1[(f1["Task"] == task) & (f1["Variable"] == "Version: 4")].iloc[0]
        v4_betas[task] = round(row["β"], 2)
    v4_min, v4_max = min(v4_betas.values()), max(v4_betas.values())
    rpt.check("Version 4 β range ≈ 0.52–0.65",
              _close(v4_min, 0.52, 0.02) and _close(v4_max, 0.65, 0.04),
              f"β = {v4_min}–{v4_max} (SI={v4_betas['Suicidal Ideation']}, "
              f"TR={v4_betas['Therapy Request']}, TE={v4_betas['Therapy Engagement']})",
              "β ≈ 0.52–0.65")

    # R² range
    r2_vals = {}
    for task in ["Suicidal Ideation", "Therapy Request", "Therapy Engagement"]:
        r2_vals[task] = f1[f1["Task"] == task].iloc[0]["R²"]

    r2_min = round(min(r2_vals.values()), 2)
    r2_max = round(max(r2_vals.values()), 2)
    best_task = max(r2_vals, key=r2_vals.get)

    rpt.check("R² range ≈ 0.31–0.46",
              _close(r2_min, 0.31, 0.02) and _close(r2_max, 0.46, 0.02),
              f"R² = {r2_min}–{r2_max} (SI={r2_vals['Suicidal Ideation']:.3f}, "
              f"TR={r2_vals['Therapy Request']:.3f}, TE={r2_vals['Therapy Engagement']:.3f})",
              "R² = 0.31–0.46")
    rpt.check("Therapy request has strongest fit",
              best_task == "Therapy Request", best_task, "Therapy Request")


# ---------------------------------------------------------------------------
# Figure 3
# ---------------------------------------------------------------------------
def verify_figure3(run_dir: Path, rpt: Report):
    rpt.section("Figure 3 — Delta F1 Fine-Tune Facet")
    rpt.quote(
        "Across all three safety-relevant classification tasks and all evaluated "
        "model families, mental health–specific fine-tuning did not yield "
        "statistically significant improvements in performance relative to the "
        "exact pretrained base models from which those fine-tuned variants were "
        "derived (Figure 3A). In contrast, several mental health–fine-tuned "
        "models demonstrated statistically significant decreases in mean Δ F1 "
        "compared with their corresponding base models, including Gemma "
        "(Δ F1 = -0.19, padjusted < 0.01) and LLaMA (Δ F1 = -0.17; padjusted "
        "< 0.05) models on therapy-request detection, and Gemma (mean "
        "Δ F1 = -0.17, padjusted < 0.05) models on therapy-engagement "
        "classification (two-sided paired t tests, Bonferroni-corrected).\n"
        "Models fine-tuned on medical corpora yielded no statistically "
        "significant differences in performance compared with base models across "
        "any task or model family, although Gemma models showed large mean "
        "Δ F1's for therapy request (0.68) and therapy engagement (0.45) "
        "detection (Figure 3B). Safety-focused fine-tuned models showed no "
        "improvement, and for some model-task pairs, statistically worse "
        "performance (Figure 3C).\n"
        "Gemma instruction-tuned models significantly outperformed their "
        "pretrained counterparts across all three tasks: suicidal ideation "
        "detection (mean Δ F1 = 0.26, padjusted < 0.05), therapy-request "
        "classification (mean Δ F1 = 0.47 padjusted < 0.01), and "
        "therapy-engagement detection (Δ F1 = 0.27, padjusted < 0.05). "
        "Qwen instruction-tuned models also showed significant improvement on "
        "therapy-request detection (Δ F1 = 0.66, padjusted < 0.05). Notably, "
        "the overall direction of effect was overwhelmingly positive: 47 of 63 "
        "instruction-tuned model pairs showed improved performance relative to "
        "their pretrained bases."
    )
    df = pd.read_csv(run_dir / "figure_3" / "delta_f1_statistics.csv")

    # --- MH: no significant improvements on any task ---
    mh = df[df["finetune_type"] == "Mental Health"]
    mh_sig_pos = mh[(mh["significant"] == True) & (mh["mean_delta_f1"] > 0)]
    rpt.check("MH: no significant positive effects",
              mh_sig_pos.empty,
              f"{len(mh_sig_pos)} sig positive cells")

    # --- MH decreases ---
    mh_claims = [
        ("Mental Health", "Therapy Request", "Gemma", -0.19, "mean", "< .01"),
        ("Mental Health", "Therapy Request", "Llama", -0.17, "mean", "< .05"),
        ("Mental Health", "Therapy Engagement", "Gemma", -0.17, "mean", "< .05"),
    ]
    for ft, task, fam, c_delta, stat_type, c_sig in mh_claims:
        row = df[(df["finetune_type"] == ft) & (df["task"] == task) &
                 (df["model_family"].str.lower() == fam.lower())].iloc[0]
        a_val = round(row[f"{stat_type}_delta_f1"], 2)
        a_mean = round(row["mean_delta_f1"], 2)
        a_med = round(row["median_delta_f1"], 2)
        a_p = row["p_adjusted"]
        label = f"MH {fam}: {task}"
        rpt.check(f"{label}: {stat_type} ΔF1 ≈ {c_delta}",
                  _close(a_val, c_delta, 0.02),
                  f"{stat_type}={a_val} (mean={a_mean}, median={a_med})",
                  str(c_delta))
        rpt.check(f"{label}: p {c_sig}", _sig_match(a_p, c_sig),
                  f"p_adj={a_p:.4f}", c_sig)

    # --- Medical: no significant ---
    med = df[df["finetune_type"] == "Medical"]
    rpt.check("Medical: no significant differences",
              med[med["significant"] == True].empty,
              f"{len(med[med['significant']==True])} significant cells")

    for task, c_delta in [("Therapy Request", 0.68), ("Therapy Engagement", 0.45)]:
        row = med[(med["task"] == task) &
                  (med["model_family"].str.lower() == "gemma")].iloc[0]
        a = round(row["mean_delta_f1"], 2)
        rpt.check(f"Medical Gemma: {task}: mean ΔF1 ≈ {c_delta}",
                  _close(a, c_delta, 0.03), str(a), str(c_delta))

    # --- Safety: no improvement, some worse ---
    safety = df[df["finetune_type"] == "Safety"]
    safety_sig = safety[safety["significant"] == True]
    n_sig_pos = len(safety_sig[safety_sig["mean_delta_f1"] > 0])
    n_sig_neg = len(safety_sig[safety_sig["mean_delta_f1"] < 0])
    rpt.check("Safety: no significant improvements",
              n_sig_pos == 0,
              f"{n_sig_pos} sig positive, {n_sig_neg} sig negative")

    # --- IT claims ---
    it_claims = [
        ("Suicidal Ideation", "Gemma", 0.26, "mean", "< .05"),
        ("Therapy Request", "Gemma", 0.47, "mean", "< .01"),
        ("Therapy Engagement", "Gemma", 0.27, "mean", "< .05"),
        ("Therapy Request", "Qwen", 0.66, "mean", "< .05"),
    ]
    for task, fam, c_delta, stat_type, c_sig in it_claims:
        rows = df[(df["finetune_type"] == "Instruction-Tuned") &
                  (df["task"] == task) &
                  (df["model_family"].str.lower() == fam.lower())]
        if rows.empty:
            rpt.check(f"IT {fam}: {task} — data missing", False)
            continue
        row = rows.iloc[0]
        a_val = round(row[f"{stat_type}_delta_f1"], 2)
        a_mean = round(row["mean_delta_f1"], 2)
        a_med = round(row["median_delta_f1"], 2)
        a_p = row["p_adjusted"]
        label = f"IT {fam}: {task}"
        rpt.check(f"{label}: {stat_type} ΔF1 ≈ {c_delta}",
                  _close(a_val, c_delta, 0.03),
                  f"{stat_type}={a_val} (mean={a_mean}, median={a_med})",
                  str(c_delta))
        rpt.check(f"{label}: p {c_sig}", _sig_match(a_p, c_sig),
                  f"p_adj={a_p:.4f}", c_sig)

    # --- 47 of 63 positive: compute directly from underlying deltas ---
    from analysis.combined_finetune_facet_plot import (
        load_data, compute_deltas,
        FINETUNE_TYPES as FT_TYPES,
    )
    it_ft = [ft for ft in FT_TYPES if ft["name"] == "instruction_tuned"][0]
    config, results = load_data()
    it_deltas = compute_deltas(config, results, it_ft["filter"], "f1_score", "f1")
    n_positive = int((it_deltas["delta_f1"] > 0).sum())
    n_total = len(it_deltas)
    rpt.check(f"IT: 47 of 63 pairs positive (computed from raw deltas)",
              n_positive == 47 and n_total == 63,
              f"{n_positive}/{n_total} positive", "47/63")


# ---------------------------------------------------------------------------
# Figure S10
# ---------------------------------------------------------------------------
def verify_figure_s10(run_dir: Path, rpt: Report):
    rpt.section("Figure S10 — Δ Parse vs Δ F1")
    rpt.quote(
        "10 of 12 fine-tuning categories and tasks, Δ parse success and Δ F1 "
        "were significantly positively correlated (all Bonferroni-adjusted "
        "p < 0.05). This association was strongest for medical fine-tuned models "
        "(R² = 0.92–0.97), and more moderate for mental health (R² = 0.48–0.61), "
        "instruction-tuned (R² = 0.40–0.64), and safety-tuned "
        "(R² = 0.19–0.92) models. Across tasks, the association was strongest "
        "for suicidal ideation (R² = 0.72), followed by therapy request "
        "classification (pooled R² = 0.68), and therapy engagement (R² = 0.55)."
    )

    from analysis.revision.delta_parse_vs_delta_f1_scatter import (
        FINETUNE_TYPES, TASKS, TASK_TITLES,
        merged_f1_and_parse_for_facet, _ols_raw_p_and_fit,
    )

    per_cell: dict[tuple[str, str], tuple[float, float]] = {}
    for ft_config in FINETUNE_TYPES:
        merged = merged_f1_and_parse_for_facet(ft_config)
        testable = []
        for task in TASKS:
            sub = merged[merged["task"] == task] if len(merged) else pd.DataFrame()
            if len(sub) >= 3:
                x = sub["delta_parse"].values * 100.0
                y = sub["delta_f1"].values
                p_raw, _, _, r_val = _ols_raw_p_and_fit(x, y)
                if p_raw is not None:
                    testable.append(task)
                    per_cell[(ft_config["label"], task)] = (r_val**2, p_raw)
        n_comp = max(len(testable), 1)
        for task in testable:
            r2, p_raw = per_cell[(ft_config["label"], task)]
            per_cell[(ft_config["label"], task)] = (r2, min(p_raw * n_comp, 1.0))

    n_sig = sum(1 for _, (_, p) in per_cell.items() if p < 0.05)
    rpt.check("10 of 12 significant", n_sig == 10, str(n_sig), "10")

    for ft_label, c_lo, c_hi in [
        ("Medical", 0.92, 0.97),
        ("Mental Health", 0.48, 0.61),
        ("Instruction-Tuned", 0.40, 0.64),
        ("Safety", 0.19, 0.92),
    ]:
        r2s = sorted([r2 for (fl, _), (r2, _) in per_cell.items() if fl == ft_label])
        if r2s:
            a_lo, a_hi = round(min(r2s), 2), round(max(r2s), 2)
            rpt.check(f"{ft_label}: R² = {c_lo}–{c_hi}",
                      _close(a_lo, c_lo, 0.03) and _close(a_hi, c_hi, 0.03),
                      f"R² = {a_lo}–{a_hi}", f"R² = {c_lo}–{c_hi}")

    # --- Pooled R² by task (all fine-tune types combined) ---
    pooled = {}
    for task in TASKS:
        all_x, all_y = [], []
        for ft_config in FINETUNE_TYPES:
            merged = merged_f1_and_parse_for_facet(ft_config)
            sub = merged[merged["task"] == task] if len(merged) else pd.DataFrame()
            if not sub.empty:
                all_x.extend((sub["delta_parse"].values * 100.0).tolist())
                all_y.extend(sub["delta_f1"].values.tolist())
        _, _, _, r_val = _ols_raw_p_and_fit(np.array(all_x), np.array(all_y))
        pooled[task] = round(r_val**2, 2) if r_val else None

    for task, c_r2 in [
        ("suicidal_ideation", 0.72),
        ("therapy_request", 0.68),
        ("therapy_engagement", 0.55),
    ]:
        a_r2 = pooled.get(task)
        rpt.check(f"Pooled {TASK_TITLES[task]}: R² = {c_r2}",
                  a_r2 is not None and _close(a_r2, c_r2, 0.03),
                  f"R² = {a_r2}", f"R² = {c_r2}")

    rpt.check("Pooled ranking: SI > TR > TE",
              (pooled.get("suicidal_ideation", 0) > pooled.get("therapy_request", 0) >
               pooled.get("therapy_engagement", 0)),
              f"SI={pooled.get('suicidal_ideation')}, "
              f"TR={pooled.get('therapy_request')}, "
              f"TE={pooled.get('therapy_engagement')}")

    # Write pooled + per-cell R² reference CSV
    ref_rows = []
    for (ft_label, task), (r2, p_adj) in sorted(per_cell.items()):
        ref_rows.append({
            "finetune_type": ft_label,
            "task": TASK_TITLES.get(task, task),
            "R2": round(r2, 4),
            "p_bonferroni": round(p_adj, 6),
            "significant": p_adj < 0.05,
        })
    for task in TASKS:
        ref_rows.append({
            "finetune_type": "POOLED (all types)",
            "task": TASK_TITLES[task],
            "R2": pooled.get(task),
            "p_bonferroni": None,
            "significant": None,
        })
    ref_df = pd.DataFrame(ref_rows)
    ref_out = run_dir / "revision_data" / "figure_s10_r2_reference.csv"
    ref_df.to_csv(ref_out, index=False)


# ---------------------------------------------------------------------------
# Discussion S10 reference
# ---------------------------------------------------------------------------
def verify_discussion_s10(run_dir: Path, rpt: Report):
    rpt.section("Discussion — S10 Reference")
    rpt.quote(
        "In several categories, particularly medical (R² ***–***) and safety "
        "fine-tuned (R² ***–***) models, changes in F1 score between a "
        "fine-tuned model and its paired base model were strongly correlated "
        "with changes in output format compliance."
    )

    from analysis.revision.delta_parse_vs_delta_f1_scatter import (
        FINETUNE_TYPES, TASKS,
        merged_f1_and_parse_for_facet, _ols_raw_p_and_fit,
    )

    per_cell: dict[tuple[str, str], float] = {}
    for ft_config in FINETUNE_TYPES:
        merged = merged_f1_and_parse_for_facet(ft_config)
        for task in TASKS:
            sub = merged[merged["task"] == task] if len(merged) else pd.DataFrame()
            if len(sub) >= 3:
                x = sub["delta_parse"].values * 100.0
                y = sub["delta_f1"].values
                _, _, _, r_val = _ols_raw_p_and_fit(x, y)
                if r_val is not None:
                    per_cell[(ft_config["label"], task)] = r_val**2

    for ft_label in ["Medical", "Safety"]:
        r2s = sorted([r2 for (fl, _), r2 in per_cell.items() if fl == ft_label])
        if r2s:
            rpt.check(f"Discussion fill-in: {ft_label} R² range", True,
                      f"R² = {min(r2s):.2f}–{max(r2s):.2f}",
                      "***–*** (placeholder — use actual values)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Verify manuscript numeric claims")
    parser.add_argument("--run-dir", type=Path, default=None)
    args = parser.parse_args()

    if args.run_dir is None:
        base = ROOT / "results" / "FINETUNE_PAPER_FIGURES"
        runs = sorted(base.iterdir())
        args.run_dir = runs[-1]

    print(f"Verifying against: {args.run_dir.name}")

    rpt = Report()
    verify_clinician_concordance(args.run_dir, rpt)
    verify_figure2(args.run_dir, rpt)
    verify_table1(args.run_dir, rpt)
    verify_table1_summary(args.run_dir, rpt)
    verify_figure3(args.run_dir, rpt)
    verify_figure_s10(args.run_dir, rpt)
    verify_discussion_s10(args.run_dir, rpt)

    out_path = args.run_dir / "CLAIM_VERIFICATION.md"
    out_path.write_text(rpt.render())
    print(f"\nWrote: {out_path}")
    print(f"\n{'='*50}")
    print(f"  {rpt.n_pass} PASS  |  {rpt.n_fail} FAIL")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
