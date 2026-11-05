#!/usr/bin/env python3
"""Retry the MentalHealthBench joint model without changing its formula.

The sample is the MentalHealthBench rows already written to
joint-observations.csv. Safety checkpoints are not in that file.
Family and version rank stay in the model. The paired analysis is not refit.

Powell is started at several lineage-to-residual variance ratios. The REML
likelihood is then evaluated on a grid of those ratios, including zero.
A mixed-model Wald result is kept only when the starts agree on an interior
peak. Otherwise the same formula is fit by ordinary least squares with
lineage-clustered CRV3 standard errors, and those p-values are labeled as
that alternative.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.stats
import statsmodels.formula.api as smf
from statsmodels.regression.mixed_linear_model import MixedLMParams
from statsmodels.tools.sm_exceptions import ConvergenceWarning

import pyfixest as pf

# Set by main(out): the folder joint_and_paired.main wrote.
OUT: Path = Path("unset")
FORMULA = (
    "score ~ log2_param_billions"
    " + C(family, Treatment(reference='Gemma'))"
    " + version_rank"
    " + C(training_category, Treatment(reference='instruction_parent'))"
)
START_RATIOS = (1e-6, 1e-4, 0.01, 0.1, 0.5, 1.0)
PROFILE_RATIOS = (0.0, 1e-8, 1e-6, 1e-4, 1e-3, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0)


def load_sample() -> pd.DataFrame:
    frame = pd.read_csv(OUT / "joint-observations.csv")
    sample = frame[frame["outcome"] == "mhb_safety"].copy()
    if sample["training_category"].eq("safety").any():
        raise SystemExit("A safety checkpoint is in the MentalHealthBench sample.")
    lineages = int(sample["ancestry_cluster_id"].nunique())
    if len(sample) < 3 or lineages < 2:
        raise SystemExit(
            f"MentalHealthBench sample is {len(sample)} checkpoints in {lineages} lineages; too small to fit."
        )
    print(f"MentalHealthBench sample: {len(sample)} checkpoints, {lineages} lineages")
    return sample.reset_index(drop=True)


def make_model(sample: pd.DataFrame):
    model = smf.mixedlm(
        FORMULA,
        data=sample,
        groups=sample["ancestry_cluster_id"],
        re_formula="1",
    )
    model.reml = True
    return model


def ols_reml(model) -> tuple[float, np.ndarray]:
    """REML log-likelihood at a lineage variance of zero, on the MixedLM scale."""
    y = np.asarray(model.endog, dtype=float)
    x = np.asarray(model.exog, dtype=float)
    n, k = x.shape
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    residual = y - x @ beta
    qf = float(np.dot(residual, residual))
    _sign, logdet_xx = np.linalg.slogdet(x.T @ x)
    loglik = 0.0
    loglik -= (n - k) * np.log(qf) / 2.0
    loglik -= logdet_xx / 2.0
    loglik -= (n - k) * np.log(2.0 * np.pi) / 2.0
    loglik += (n - k) * np.log(n - k) / 2.0
    loglik -= (n - k) / 2.0
    return float(loglik), beta


def profile_likelihood(model) -> pd.DataFrame:
    rows = []
    zero_llf, _beta = ols_reml(model)
    for ratio in PROFILE_RATIOS:
        if ratio == 0.0:
            rows.append({
                "variance_ratio": 0.0,
                "reml_llf": zero_llf,
                "evaluation": "ordinary least squares limit",
            })
            continue
        params = MixedLMParams.from_components(
            fe_params=np.zeros(model.k_fe),
            cov_re=np.array([[ratio]], dtype=float),
        )
        try:
            loglik = float(model.loglike(params, profile_fe=True))
            note = "profile REML"
        except Exception as exc:
            loglik = np.nan
            note = f"{type(exc).__name__}: {exc}"
        rows.append({
            "variance_ratio": ratio,
            "reml_llf": loglik,
            "evaluation": note,
        })
    return pd.DataFrame(rows)


def fit_powell(model, ratio: float) -> dict:
    start = MixedLMParams.from_components(
        fe_params=np.zeros(model.k_fe),
        cov_re=np.array([[ratio]], dtype=float),
    )
    caught = []
    try:
        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")
            result = model.fit(
                start_params=start,
                reml=True,
                method=["powell"],
                maxiter=5000,
                disp=False,
            )
            for item in caught_warnings:
                caught.append(f"{item.category.__name__}: {item.message}")
    except Exception as exc:
        return {
            "start_variance_ratio": ratio,
            "converged": False,
            "reml_llf": np.nan,
            "variance_ratio": np.nan,
            "lineage_variance": np.nan,
            "residual_variance": np.nan,
            "hessian_warning": False,
            "boundary_warning": False,
            "use_t": np.nan,
            "fit_error": f"{type(exc).__name__}: {exc}",
            "warnings": " | ".join(caught),
            "coefficients": {},
        }
    warning_text = " | ".join(caught)
    variance = float(np.asarray(result.cov_re).reshape(-1)[0])
    scale = float(result.scale)
    names = list(result.model.exog_names)
    coefficients = {name: float(result.fe_params[name]) for name in names}
    standard_errors = {name: float(result.bse[name]) for name in names}
    p_values = {name: float(result.pvalues[name]) for name in names}
    intervals = {
        name: (
            float(result.conf_int().loc[name, 0]),
            float(result.conf_int().loc[name, 1]),
        )
        for name in names
    }
    return {
        "start_variance_ratio": ratio,
        "converged": bool(result.converged),
        "reml_llf": float(result.llf),
        "variance_ratio": variance / scale if scale > 0 else np.nan,
        "lineage_variance": variance,
        "residual_variance": scale,
        "hessian_warning": "not positive definite" in warning_text.lower(),
        "boundary_warning": "boundary" in warning_text.lower(),
        "use_t": bool(result.use_t),
        "fit_error": "",
        "warnings": warning_text,
        "coefficients": coefficients,
        "standard_errors": standard_errors,
        "p_values": p_values,
        "intervals": intervals,
        "result": result,
    }


def decide(starts: list[dict], profile: pd.DataFrame) -> dict:
    converged = [row for row in starts if row["converged"] and np.isfinite(row["reml_llf"])]
    if len(converged) < 2:
        return {
            "reliable_interior_mixed_model": False,
            "reason": "Fewer than two Powell starts converged.",
        }
    best = max(row["reml_llf"] for row in converged)
    top = [row for row in converged if best - row["reml_llf"] <= 0.01]
    if len(top) < 2:
        return {
            "reliable_interior_mixed_model": False,
            "reason": "Only one start reached the best REML likelihood.",
        }
    names = list(top[0]["coefficients"])
    spread = max(
        max(row["coefficients"][name] for row in top)
        - min(row["coefficients"][name] for row in top)
        for name in names
    )
    if spread > 1e-3:
        return {
            "reliable_interior_mixed_model": False,
            "reason": (
                f"Coefficients from the best starts differ by up to {spread:.4g}."
            ),
        }
    ratios = [row["variance_ratio"] for row in top]
    if max(ratios) - min(ratios) > 0.01 and max(ratios) > 10.0 * max(min(ratios), 1e-12):
        return {
            "reliable_interior_mixed_model": False,
            "reason": "The best starts do not agree on the variance ratio.",
        }
    usable = profile[np.isfinite(profile["reml_llf"])]
    peak = usable.loc[usable["reml_llf"].idxmax()]
    zero = float(usable.loc[usable["variance_ratio"] == 0.0, "reml_llf"].iloc[0])
    if float(peak["variance_ratio"]) < 1e-4 or float(peak["reml_llf"]) - zero < 0.1:
        return {
            "reliable_interior_mixed_model": False,
            "reason": (
                "Every Powell start converged to a lineage variance near zero, "
                "and the REML profile is highest at a lineage variance of zero. "
                "The likelihood falls as that variance ratio increases, so the "
                "mixed-model solution is on the boundary. Mixed-model Wald "
                "p-values are not used."
            ),
            "profile_peak_ratio": float(peak["variance_ratio"]),
            "profile_peak_llf": float(peak["reml_llf"]),
            "profile_zero_llf": zero,
        }
    ratio_hat = float(np.median(ratios))
    near_peak = abs(np.log10(ratio_hat) - np.log10(float(peak["variance_ratio"]))) < 0.7
    if not near_peak:
        return {
            "reliable_interior_mixed_model": False,
            "reason": "The Powell solution is not at the profile peak.",
            "profile_peak_ratio": float(peak["variance_ratio"]),
        }
    if any(row["hessian_warning"] or row["use_t"] for row in top):
        return {
            "reliable_interior_mixed_model": False,
            "reason": "The Hessian is not positive definite, or use_t was not false.",
        }
    chosen = max(top, key=lambda row: row["reml_llf"])
    return {
        "reliable_interior_mixed_model": True,
        "reason": "Powell starts agree on an interior REML peak.",
        "chosen": chosen,
        "profile_peak_ratio": float(peak["variance_ratio"]),
        "profile_peak_llf": float(peak["reml_llf"]),
        "profile_zero_llf": zero,
    }


def wald_rows(chosen: dict) -> pd.DataFrame:
    result = chosen["result"]
    names = list(result.model.exog_names)
    if result.use_t:
        raise SystemExit("Wald intervals require use_t False.")
    z = scipy.stats.norm.ppf(0.975)
    rows = []
    for name in names:
        estimate = float(result.fe_params[name])
        se = float(result.bse[name])
        low = float(result.conf_int().loc[name, 0])
        high = float(result.conf_int().loc[name, 1])
        if not np.allclose(low, estimate - z * se):
            raise SystemExit(f"{name}: interval is not a normal Wald interval.")
        rows.append({
            "analysis": "mixed_model_wald",
            "term": name,
            "estimate": estimate,
            "std_error": se,
            "ci_low": low,
            "ci_high": high,
            "p_value": float(result.pvalues[name]),
            "interval": "Wald interval",
            "inference_df": np.nan,
        })
    return pd.DataFrame(rows)


def crv3_rows(sample: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    fit = pf.feols(
        FORMULA,
        data=sample,
        vcov={"CRV3": "ancestry_cluster_id"},
    )
    g = int(sample["ancestry_cluster_id"].nunique())
    n = int(len(sample))
    inference_df = g - 1
    estimate = np.asarray(fit.coef(), dtype=float).reshape(-1)
    se = np.asarray(fit.se(), dtype=float).reshape(-1)
    p_value = np.asarray(fit.pvalue(), dtype=float).reshape(-1)
    interval = np.asarray(fit.confint(), dtype=float)
    names = list(fit.coef().index) if hasattr(fit.coef(), "index") else [
        f"b{i}" for i in range(len(estimate))
    ]
    # pyfixest 0.28 returns numpy arrays from coef(); names are on _coefnames.
    names = list(fit._coefnames)
    t_crit = float(scipy.stats.t.ppf(0.975, inference_df))
    rebuilt = np.column_stack([estimate - t_crit * se, estimate + t_crit * se])
    if not np.allclose(interval, rebuilt, rtol=0, atol=1e-8):
        raise SystemExit("CRV3 interval does not match a t interval with G-1 df.")
    ssc = dict(fit._ssc_dict)
    if ssc != {"adj": True, "fixef_k": "none", "cluster_adj": True, "cluster_df": "min"}:
        raise SystemExit(f"Unexpected CRV3 small-sample settings: {ssc}")
    if int(np.min(np.asarray(fit._G))) != g:
        raise SystemExit("CRV3 cluster count does not match the sample.")
    k = int(fit._k)
    expected = (n - 1) / (n - k) * g / (g - 1)
    if abs(float(np.ravel(fit._ssc)[0]) - expected) > 1e-8:
        raise SystemExit("CRV3 small-sample multiplier is not the expected value.")
    rows = []
    for i, name in enumerate(names):
        rows.append({
            "analysis": "ols_crv3",
            "term": name,
            "estimate": float(estimate[i]),
            "std_error": float(se[i]),
            "ci_low": float(interval[i, 0]),
            "ci_high": float(interval[i, 1]),
            "p_value": float(p_value[i]),
            "interval": "CRV3 t interval, df = lineages minus 1",
            "inference_df": inference_df,
        })
    info = {
        "n_observations": n,
        "n_clusters": g,
        "inference_df": inference_df,
        "n_parameters": k,
        "ssc_multiplier": expected,
    }
    return pd.DataFrame(rows), info


def label(term: str) -> str:
    if term == "Intercept":
        return "Intercept (Gemma instruction parent, version rank 0, 1 billion parameters)"
    if term == "log2_param_billions":
        return "Parameter count, per doubling"
    if term == "version_rank":
        return "Version rank, per step"
    if "mental-health" in term:
        return "Mental-health fine-tune"
    if "medical" in term:
        return "Medical fine-tune"
    if "safety" in term:
        return "Safety fine-tune"
    if "Llama" in term:
        return "Llama vs Gemma"
    if "Mistral" in term:
        return "Mistral vs Gemma"
    if "Qwen" in term:
        return "Qwen vs Gemma"
    if "SmolLM" in term:
        return "SmolLM vs Gemma"
    return term


def add_percentage_points(estimates: pd.DataFrame) -> pd.DataFrame:
    scaled = estimates.copy()
    for column in ("estimate", "std_error", "ci_low", "ci_high"):
        scaled[column] = scaled[column] * 100.0
    scaled["unit"] = "percentage points"
    estimates = estimates.copy()
    estimates["unit"] = "score (0-1)"
    scaled["term_label"] = estimates["term_label"]
    return pd.concat([estimates, scaled], ignore_index=True)


def main(out: Path) -> Path:
    global OUT
    OUT = Path(out)
    sample = load_sample()
    model = make_model(sample)
    starts = [fit_powell(model, ratio) for ratio in START_RATIOS]
    profile = profile_likelihood(model)
    decision = decide(starts, profile)

    start_rows = []
    for row in starts:
        flat = {key: value for key, value in row.items() if key not in {
            "coefficients", "standard_errors", "p_values", "intervals", "result"
        }}
        for name, value in row.get("coefficients", {}).items():
            flat[f"coef__{name}"] = value
        start_rows.append(flat)
    pd.DataFrame(start_rows).to_csv(OUT / "mhb-powell-starts.csv", index=False)
    profile.to_csv(OUT / "mhb-reml-profile.csv", index=False)

    if decision["reliable_interior_mixed_model"]:
        estimates = wald_rows(decision["chosen"])
        method = "mixed_model_wald"
        method_note = decision["reason"]
    else:
        estimates, crv_info = crv3_rows(sample)
        decision.update(crv_info)
        method = "ols_crv3"
        method_note = (
            decision["reason"] + " The reported p-values are from ordinary "
            "least squares with lineage-clustered CRV3 standard errors. "
            "They are not mixed-model Wald p-values."
        )
    estimates.insert(1, "term_label", estimates["term"].map(label))
    estimates = add_percentage_points(estimates)
    estimates.to_csv(OUT / "mhb-chosen-estimates.csv", index=False)
    pd.DataFrame([{
        "method": method,
        "reason": method_note,
        **{key: value for key, value in decision.items() if key != "chosen"},
    }]).to_csv(OUT / "mhb-inference-decision.csv", index=False)
    write_note(method, method_note, estimates, profile, starts, sample)
    print(method)
    print(method_note)
    shown = estimates[estimates["unit"] == "score (0-1)"]
    print(shown[["term_label", "estimate", "std_error", "ci_low", "ci_high", "p_value"]].to_string(index=False))
    return OUT


def fmt_p(value: float) -> str:
    if value < 0.001:
        return "<0.001"
    return f"{value:.3f}"


def fmt_ci(estimate: float, low: float, high: float) -> str:
    return f"{estimate:.3f} ({low:.3f} to {high:.3f})"


def write_note(method: str, method_note: str, estimates: pd.DataFrame,
               profile: pd.DataFrame, starts: list[dict], sample: pd.DataFrame) -> None:
    fraction = estimates[estimates["unit"] == "score (0-1)"].copy()
    lines = [
        "# MentalHealthBench joint-model retry",
        "",
        f"Formula unchanged. Sample: the {len(sample)} MentalHealthBench checkpoints in "
        f"{int(sample['ancestry_cluster_id'].nunique())} lineages from `joint-observations.csv`, "
        "no safety models. Starts and the REML profile are in "
        "`mhb-powell-starts.csv` and `mhb-reml-profile.csv`.",
        "",
        method_note,
        "",
        "## Powell starts",
        "",
    ]
    for row in starts:
        lines.append(
            f"- Start ratio {row['start_variance_ratio']}: "
            f"converged {row['converged']}, REML log-likelihood "
            f"{row['reml_llf']}, variance ratio {row['variance_ratio']}, "
            f"lineage variance {row['lineage_variance']}."
        )
    usable = profile[np.isfinite(profile["reml_llf"])]
    peak = usable.loc[usable["reml_llf"].idxmax()]
    lines.extend([
        "",
        f"Profile peak at variance ratio {peak['variance_ratio']} "
        f"(REML log-likelihood {peak['reml_llf']}).",
        "",
        "## Estimates used for the MentalHealthBench column",
        "",
    ])
    if method == "ols_crv3":
        lines.append(
            "Ordinary least squares, CRV3 by lineage, t reference with "
            "17 degrees of freedom. Intervals are not multiplicity-adjusted. "
            "The 0–1 score was the fitted scale. Percentage points are that "
            "result multiplied by 100."
        )
    else:
        lines.append(
            "REML mixed model, normal Wald intervals. Percentage points are "
            "that result multiplied by 100."
        )
    lines.append("")
    lines.append("| Term | β (95% CI), 0–1 score | P |")
    lines.append("|---|---|---:|")
    for row in fraction.itertuples(index=False):
        lines.append(
            f"| {row.term_label} | {fmt_ci(row.estimate, row.ci_low, row.ci_high)} | "
            f"{fmt_p(row.p_value)} |"
        )
    (OUT / "mhb-inference-note.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit("run orchestration/fit_mixed_models.py; it names the output folder")
