#!/usr/bin/env python3
"""Two analyses of the roster resolved through CURRENT.

1. Joint mixed model of checkpoint scores (Table 1).
   Instruction-tuned parents and their fine-tunes.
   score ~ log2(parameter count) + family + version rank + training category.
   Random intercept: the instruction parent's checkpoint.

2. Fine-tune minus its instruction-tuned parent, for mental-health, medical,
   and safety (Table S4). delta = child score - canonical parent score.
   Intercept-only model, CRV3 by ancestry cluster, fit separately for each
   fine-tune type. Safety has no MentalHealthBench rows.

Unsloth Gemma 3 1B and Unsloth Gemma 3 4B are the Google checkpoints.
They are not kept as separate models. The Google score is the checkpoint
score. A different Unsloth score is recorded as a conflict and is not used.

The cohort is the manuscript subset: every instruction-tuned parent and the
fine-tunes whose training method and training objective are both stated
(orchestration.study_roster.labeled_fine_tune). Fine-tunes left out are
listed in unlabeled-fine-tunes.csv. Pretrained checkpoints are not fit.

Run through orchestration/fit_mixed_models.py, which names the output folder
outputs/mixed-models/<day of the run>/ and writes outputs/mixed-models/CURRENT.
"""

from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
import sys
import traceback
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.stats
import statsmodels
import statsmodels.formula.api as smf
from patsy import dmatrices
from statsmodels.stats.multitest import multipletests

import pyfixest as pf

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from orchestration.study_roster import labeled_fine_tune  # noqa: E402

INV = ROOT / "model_selection"
ROSTER_ROOT = ROOT / "outputs/roster"
MIXED_ROOT = ROOT / "outputs/mixed-models"
# Set by main(out). Every output file is written under it.
OUT: Path = MIXED_ROOT / "unset"

OUTCOMES = ("si_f1", "cssrs_f1", "mhb_safety")
OUTCOME_NAME = {
    "si_f1": "synthetic suicidal-ideation yes/no F1",
    "cssrs_f1": "C-SSRS yes/no F1",
    "mhb_safety": "MentalHealthBench suicide/self-harm subset",
}
SINGULAR_VARIANCE = 1e-8

# The two Unsloth rows are copies of these Google checkpoints.
REHOST_OF = {
    "unsloth/gemma-3-1b-it": "google/gemma-3-1b-it",
    "unsloth/gemma-3-4b-it": "google/gemma-3-4b-it",
}

# Rank is the release order inside one family, starting at 0.
# A child uses its parent's rank. This table is written before any fit.
RELEASE_RANK = (
    ("Gemma", "Gemma 1", 0, "clear",
     "Gemma 1 is the earliest Gemma release in this study."),
    ("Gemma", "Gemma 3", 2, "clear",
     "Gemma 2 is the generation between Gemma 1 and Gemma 3 and is not in "
     "this roster, so Gemma 3 is two steps after Gemma 1."),
    ("Gemma", "Gemma 3n", 3, "clear",
     "Gemma 3n is one step after Gemma 3. It is an on-device line, not "
     "Gemma 4. E2B and E4B enter the joint model as 2 and 4 billion "
     "effective parameters."),
    ("Llama", "Llama 3", 0, "clear",
     "Llama 3 precedes Llama 3.1."),
    ("Llama", "Llama 3.1", 1, "clear",
     "Llama 3.1 follows Llama 3."),
    ("Llama", "Llama 3.2", 2, "clear",
     "Llama 3.2 follows Llama 3.1. The 1B and 3B text models are pruned "
     "derivatives of Llama 3.1 8B."),
    ("Mistral", "Mistral 7B v0.2", 0, "same_level",
     "v0.2 and v0.3 share one rank. The base card describes v0.3 as v0.2 "
     "with the vocabulary extended to 32768."),
    ("Mistral", "Mistral 7B v0.3", 0, "same_level",
     "Same rank as v0.2. The instruct card adds the v3 tokenizer and "
     "function calling. This pair does not identify the version slope."),
    ("Qwen", "Qwen2.5", 0, "clear",
     "Qwen2.5 precedes Qwen3 by version number."),
    ("Qwen", "Qwen3", 1, "clear",
     "Qwen3 follows Qwen2.5. Qwen3-4B and Qwen3-4B-Instruct-2507 are both "
     "this release."),
    ("Qwen", "Qwen3.5", 2, "clear",
     "Qwen3.5 follows Qwen3 by version number."),
    ("SmolLM", "SmolLM2", 0, "single_release",
     "SmolLM2 is the only SmolLM release in this roster. It does not "
     "identify the version slope."),
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_current() -> str:
    current = (ROSTER_ROOT / "CURRENT").read_text(encoding="utf-8").strip()
    if not current or "/" in current or current.startswith("."):
        raise SystemExit(f"CURRENT is not a single results date: {current!r}")
    return current


def parse_param_billions(size) -> float:
    """Turn a size label into billions of parameters.

    Gemma 3n E2B and E4B are the effective sizes used on the figures, 2 and 4
    billion. The E2B card says the weight-file count is 6 billion.
    """
    if pd.isna(size):
        return np.nan
    text = str(size).strip()
    if text == "E2B":
        return 2.0
    if text == "E4B":
        return 4.0
    head = text.split(" (", 1)[0].strip()
    if head.endswith("B"):
        return float(head[:-1])
    if head.endswith("M"):
        return float(head[:-1]) / 1000.0
    return np.nan


def canonical_checkpoint(hf_id: str) -> str:
    return REHOST_OF.get(hf_id, hf_id)


def smoke_test_crv3() -> dict:
    rng = np.random.default_rng(0)
    cluster = np.repeat(np.arange(6), 4)
    frame = pd.DataFrame({
        "delta": rng.normal(size=24),
        "cluster": cluster.astype(str),
    })
    fit = pf.feols("delta ~ 1", data=frame, vcov={"CRV3": "cluster"})
    se = float(np.asarray(fit.se()).reshape(-1)[0])
    if not np.isfinite(se):
        raise SystemExit("CRV3 smoke test did not return a finite standard error.")
    return {"clusters": 6, "rows": 24, "se": se}


def load_snapshot(current: str) -> tuple[pd.DataFrame, Path, str]:
    source = ROSTER_ROOT / current / "roster.csv"
    if not source.is_file():
        raise SystemExit(f"Roster named by CURRENT does not exist: {source}")
    snapshot = OUT / "roster-snapshot.csv"
    shutil.copyfile(source, snapshot)
    source_hash = subprocess.check_output(
        ["sha256sum", str(source)], text=True
    ).split()[0]
    snapshot_hash = subprocess.check_output(
        ["sha256sum", str(snapshot)], text=True
    ).split()[0]
    if source_hash != snapshot_hash:
        raise SystemExit("Snapshot hash does not match the source roster.")
    (OUT / "roster-source.txt").write_text(
        f"source_path: {source}\n"
        f"snapshot_path: {snapshot}\n"
        f"sha256: {source_hash}\n"
        f"CURRENT: {current}\n",
        encoding="utf-8",
    )
    frame = pd.read_csv(snapshot)
    if frame["hf_id"].duplicated().any():
        raise SystemExit("Roster hf_id values are not unique.")
    return frame, source, source_hash


def rank_table() -> pd.DataFrame:
    rows = []
    for family, version, rank, ordering, note in RELEASE_RANK:
        rows.append({
            "family": family,
            "version": version,
            "version_rank": rank,
            "ordering": ordering,
            "note": note,
        })
    table = pd.DataFrame(rows)
    if table.duplicated(["family", "version"]).any():
        raise SystemExit("Release-rank table has a duplicate family and version.")
    repeated = table[table.duplicated(["family", "version_rank"], keep=False)]
    if not repeated.empty and not (repeated["ordering"] == "same_level").all():
        pairs = [
            f"{row.family} / {row.version} rank {row.version_rank}"
            for row in repeated.itertuples(index=False)
        ]
        raise SystemExit(
            "Release-rank table repeats a rank inside a family: " + "; ".join(pairs)
        )
    return table


def attach_rank(frame: pd.DataFrame, ranks: pd.DataFrame) -> pd.DataFrame:
    unknown = (
        frame[["family", "version"]]
        .drop_duplicates()
        .merge(ranks, on=["family", "version"], how="left")
    )
    missing = unknown[unknown["version_rank"].isna()]
    if len(missing):
        pairs = [
            f"{row.family} / {row.version}" for row in missing.itertuples()
        ]
        raise SystemExit(
            "No release rank was defined for: " + "; ".join(pairs)
        )
    out = frame.merge(
        ranks[["family", "version", "version_rank", "ordering"]],
        on=["family", "version"],
        how="left",
    )
    if out["version_rank"].isna().any():
        raise SystemExit("A row lost its version rank during the merge.")
    return out


def split_labeled(roster: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fine-tunes with a stated method and objective, and the ones without."""
    children = roster[roster["role"] == "fine-tune"].copy()
    text = children.fillna("").astype(str)
    keep = text.apply(lambda row: labeled_fine_tune(row.to_dict()), axis=1)
    if len(children) == 0:
        raise SystemExit("The roster has no fine-tunes.")
    return children[keep.to_numpy()].copy(), children[~keep.to_numpy()].copy()


def build_cohort(roster: pd.DataFrame, ranks: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    parents = roster[roster["role"] == "instruction parent"].copy()
    children, _unlabeled = split_labeled(roster)
    if children["hf_id"].duplicated().any():
        raise SystemExit("Fine-tune ids are not unique.")
    if children["grouping"].isna().any() or (children["grouping"] == "").any():
        raise SystemExit("A fine-tune has no grouping.")
    if children["parent_id"].isna().any():
        raise SystemExit("A fine-tune has no parent_id.")

    parents["canonical_id"] = parents["hf_id"].map(canonical_checkpoint)
    children["canonical_parent_id"] = children["parent_id"].map(canonical_checkpoint)

    rehost_rows = parents[parents["hf_id"].isin(REHOST_OF)].copy()
    canonical_rows = parents[parents["hf_id"].isin(REHOST_OF.values())].copy()
    conflicts = []
    for rehost_id, canonical_id in REHOST_OF.items():
        rehost = rehost_rows[rehost_rows["hf_id"] == rehost_id]
        canon = canonical_rows[canonical_rows["hf_id"] == canonical_id]
        if len(rehost) != 1 or len(canon) != 1:
            raise SystemExit(
                f"Expected one row each for {rehost_id} and {canonical_id}."
            )
        rehost = rehost.iloc[0]
        canon = canon.iloc[0]
        for outcome in OUTCOMES:
            left = canon[outcome]
            right = rehost[outcome]
            both = pd.notna(left) and pd.notna(right)
            conflict = bool(both and float(left) != float(right))
            conflicts.append({
                "canonical_id": canonical_id,
                "rehost_id": rehost_id,
                "outcome": outcome,
                "canonical_score": left,
                "rehost_score": right,
                "both_scores_present": both,
                "scores_differ": conflict,
                "score_used": left,
                "rule": (
                    "One checkpoint. The Google row is that checkpoint. "
                    "The Unsloth score is not entered and is not averaged."
                ),
            })
    conflict_table = pd.DataFrame(conflicts)

    # One parent checkpoint. The Unsloth copies are not separate models.
    parents = parents[~parents["hf_id"].isin(REHOST_OF)].copy()
    parent_lookup = parents.set_index("hf_id")
    missing_parent = sorted(
        set(children["canonical_parent_id"]) - set(parent_lookup.index)
    )
    if missing_parent:
        raise SystemExit(
            "A fine-tune's canonical parent is not exactly one instruction "
            "checkpoint: " + "; ".join(missing_parent)
        )

    parent_rank = attach_rank(parents, ranks)
    inherited = parent_rank.set_index("hf_id")[
        ["family", "version", "version_rank", "ordering", "size"]
    ]

    rows = []
    mismatches = []
    for row in parent_rank.itertuples(index=False):
        rows.append({
            "checkpoint_id": row.hf_id,
            "role": "instruction",
            "training_category": "instruction_parent",
            "grouping": row.grouping,
            "family": row.family,
            "version": row.version,
            "version_rank": int(row.version_rank),
            "version_ordering": row.ordering,
            "size": row.size,
            "param_billions": parse_param_billions(row.size),
            "ancestry_cluster_id": row.hf_id,
            "parent_id_as_listed": "",
            "canonical_parent_id": "",
            "si_f1": row.si_f1,
            "cssrs_f1": row.cssrs_f1,
            "mhb_safety": row.mhb_safety,
        })
    for row in children.itertuples(index=False):
        parent = inherited.loc[row.canonical_parent_id]
        if (
            row.family != parent["family"]
            or row.version != parent["version"]
            or str(row.size) != str(parent["size"])
        ):
            mismatches.append({
                "checkpoint_id": row.hf_id,
                "child_family": row.family,
                "parent_family": parent["family"],
                "child_version": row.version,
                "parent_version": parent["version"],
                "child_size": row.size,
                "parent_size": parent["size"],
                "resolution": "The child uses the canonical parent's family, version rank, and size.",
            })
        rows.append({
            "checkpoint_id": row.hf_id,
            "role": "fine-tune",
            "training_category": row.grouping,
            "grouping": row.grouping,
            "family": parent["family"],
            "version": parent["version"],
            "version_rank": int(parent["version_rank"]),
            "version_ordering": parent["ordering"],
            "size": parent["size"],
            "param_billions": parse_param_billions(parent["size"]),
            "ancestry_cluster_id": row.canonical_parent_id,
            "parent_id_as_listed": row.parent_id,
            "canonical_parent_id": row.canonical_parent_id,
            "si_f1": row.si_f1,
            "cssrs_f1": row.cssrs_f1,
            "mhb_safety": row.mhb_safety,
        })
    cohort = pd.DataFrame(rows)
    if cohort["checkpoint_id"].duplicated().any():
        raise SystemExit("Checkpoint ids are not unique after the rehost merge.")
    if cohort["checkpoint_id"].isin(REHOST_OF).any():
        raise SystemExit("An Unsloth Gemma 3 rehost remained in the cohort.")
    allowed = {"instruction_parent", "mental-health", "medical", "safety"}
    if not set(cohort["training_category"]).issubset(allowed):
        raise SystemExit(
            f"Unexpected training category: {sorted(set(cohort['training_category']) - allowed)}"
        )
    for outcome in OUTCOMES:
        values = cohort[outcome].dropna()
        if ((values < 0) | (values > 1)).any():
            raise SystemExit(f"{outcome} has a score outside 0 to 1.")
    mismatch_table = pd.DataFrame(
        mismatches,
        columns=[
            "checkpoint_id",
            "child_family",
            "parent_family",
            "child_version",
            "parent_version",
            "child_size",
            "parent_size",
            "resolution",
        ],
    )
    return cohort, conflict_table, mismatch_table


def coverage_tables(cohort: pd.DataFrame, ranks: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    parsed = cohort[cohort["param_billions"].notna()]
    rows = []
    for (family, version), sub in cohort.groupby(["family", "version"], sort=True):
        in_joint = parsed[
            (parsed["family"] == family) & (parsed["version"] == version)
        ]
        rows.append({
            "family": family,
            "version": version,
            "version_rank": int(sub["version_rank"].iloc[0]),
            "ordering": sub["version_ordering"].iloc[0],
            "n_checkpoints": int(len(sub)),
            "n_instruction_parents": int((sub["role"] == "instruction").sum()),
            "n_fine_tunes": int((sub["role"] == "fine-tune").sum()),
            "n_in_joint_model": int(len(in_joint)),
            "sizes": "; ".join(sorted(sub["size"].astype(str).unique())),
            "param_billions_min": sub["param_billions"].min(),
            "param_billions_max": sub["param_billions"].max(),
        })
    coverage = pd.DataFrame(rows).sort_values(["family", "version_rank"])
    steps = []
    for family, sub in coverage.groupby("family", sort=True):
        ordered = sub.sort_values("version_rank")
        previous = None
        for row in ordered.itertuples(index=False):
            if previous is not None and int(previous.version_rank) != int(row.version_rank):
                left = set(str(previous.sizes).split("; "))
                right = set(str(row.sizes).split("; "))
                shared = sorted(left & right)
                steps.append({
                    "family": family,
                    "from_version": previous.version,
                    "to_version": row.version,
                    "from_rank": int(previous.version_rank),
                    "to_rank": int(row.version_rank),
                    "from_sizes": previous.sizes,
                    "to_sizes": row.sizes,
                    "shared_size_labels": "; ".join(shared) if shared else "none",
                    "same_size_step": bool(shared),
                    "enters_joint_model": (
                        previous.n_in_joint_model > 0 and row.n_in_joint_model > 0
                    ),
                    "ordering": row.ordering,
                })
            previous = row
    present = set(zip(coverage["family"], coverage["version"]))
    defined = set(zip(ranks["family"], ranks["version"]))
    unused = defined - present
    if unused:
        raise SystemExit(f"Rank mapping has releases absent from the cohort: {unused}")
    return coverage, pd.DataFrame(steps)


def joint_observations(cohort: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    from orchestration.study_roster import MHB_COMPARISON_GROUPINGS

    brought = set(
        cohort.loc[
            cohort["training_category"].isin(MHB_COMPARISON_GROUPINGS),
            "ancestry_cluster_id",
        ]
    )
    if not brought:
        raise SystemExit("no mental-health or medical fine-tune is in the joint cohort")
    kept = []
    excluded = []
    for outcome in OUTCOMES:
        for row in cohort.itertuples(index=False):
            reasons = []
            if pd.isna(row.param_billions):
                reasons.append(
                    f"size {row.size} has no parameter count; excluded from the joint model only"
                )
            if outcome == "mhb_safety" and row.training_category == "safety":
                reasons.append(
                    "safety fine-tune excluded from the MentalHealthBench comparison"
                )
            if (
                outcome == "mhb_safety"
                and row.training_category == "instruction_parent"
                and row.checkpoint_id not in brought
            ):
                reasons.append(
                    "instruction-tuned parent excluded from the MentalHealthBench comparison: "
                    "no mental-health or medical fine-tune of this parent is in the study"
                )
            if pd.isna(getattr(row, outcome)):
                reasons.append("score missing")
            if reasons:
                excluded.append({
                    "analysis": "joint",
                    "outcome": outcome,
                    "checkpoint_id": row.checkpoint_id,
                    "training_category": row.training_category,
                    "reason": "; ".join(reasons),
                })
                continue
            kept.append({
                "outcome": outcome,
                "checkpoint_id": row.checkpoint_id,
                "training_category": row.training_category,
                "family": row.family,
                "version": row.version,
                "version_rank": row.version_rank,
                "size": row.size,
                "param_billions": row.param_billions,
                "log2_param_billions": float(np.log2(row.param_billions)),
                "ancestry_cluster_id": row.ancestry_cluster_id,
                "score": float(getattr(row, outcome)),
            })
    observations = pd.DataFrame(kept)
    if observations.duplicated(["outcome", "checkpoint_id"]).any():
        raise SystemExit("A checkpoint appears twice for one joint-model outcome.")
    return observations, pd.DataFrame(excluded)


JOINT_FORMULA = (
    "score ~ log2_param_billions"
    " + C(family, Treatment(reference='Gemma'))"
    " + version_rank"
    " + C(training_category, Treatment(reference='instruction_parent'))"
)


def design_rank(sample: pd.DataFrame) -> dict:
    _y, x = dmatrices(JOINT_FORMULA, sample, return_type="dataframe")
    rank = int(np.linalg.matrix_rank(np.asarray(x, dtype=float)))
    return {
        "n_rows": int(x.shape[0]),
        "n_columns": int(x.shape[1]),
        "matrix_rank": rank,
        "full_rank": rank == x.shape[1],
        "columns": list(x.columns),
    }


def fit_joint(sample: pd.DataFrame, outcome: str) -> tuple[dict, pd.DataFrame]:
    design = design_rank(sample)
    record = {
        "outcome": outcome,
        "formula": JOINT_FORMULA,
        "reml": True,
        "n_observations": int(len(sample)),
        "n_clusters": int(sample["ancestry_cluster_id"].nunique()),
        "design_columns": design["n_columns"],
        "design_rank": design["matrix_rank"],
        "design_full_rank": design["full_rank"],
        "converged": False,
        "fit_error": "",
        "random_intercept_variance": np.nan,
        "residual_variance": np.nan,
        "singular": False,
        "boundary_warning": False,
        "wald_supported": False,
        "warnings": "",
    }
    coefficients = []
    if not design["full_rank"]:
        record["fit_error"] = (
            "Design matrix is rank deficient. The specified model was not "
            "refit with a column removed."
        )
        record["wald_supported"] = False
        return record, pd.DataFrame(coefficients)

    caught = []

    def collect(message, category, filename, lineno, file=None, line=None):
        caught.append(f"{category.__name__}: {message}")

    try:
        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")
            result = smf.mixedlm(
                JOINT_FORMULA,
                data=sample,
                groups=sample["ancestry_cluster_id"],
                re_formula="1",
            ).fit(reml=True)
            for item in caught_warnings:
                caught.append(f"{item.category.__name__}: {item.message}")
    except Exception as exc:
        record["fit_error"] = f"{type(exc).__name__}: {exc}"
        record["warnings"] = " | ".join(caught)
        return record, pd.DataFrame(coefficients)

    variance = float(np.asarray(result.cov_re).reshape(-1)[0])
    singular = variance <= SINGULAR_VARIANCE
    warning_text = " | ".join(caught)
    boundary = "boundary" in warning_text.lower()
    names = list(result.model.exog_names)
    if result.use_t:
        record["fit_error"] = (
            "MixedLM returned use_t=True. Intervals were not relabeled as Wald."
        )
        record["converged"] = bool(result.converged)
        record["warnings"] = warning_text
        return record, pd.DataFrame(coefficients)
    standard_error = result.bse.loc[names]
    low, high = result.conf_int().loc[names].to_numpy().T
    z = scipy.stats.norm.ppf(0.975)
    rebuilt_low = result.fe_params.loc[names] - z * standard_error
    if not np.allclose(low, rebuilt_low, equal_nan=True):
        record["fit_error"] = "Returned interval does not match a normal Wald interval."
        record["converged"] = bool(result.converged)
        record["warnings"] = warning_text
        return record, pd.DataFrame(coefficients)

    supported = bool(result.converged) and (not singular) and np.isfinite(variance)
    if not result.converged:
        record["fit_error"] = (
            "Optimization did not converge. The coefficient values are the "
            "optimizer's last position, not a completed fit. No other "
            "optimizer or formula was tried."
        )
    record.update({
        "converged": bool(result.converged),
        "random_intercept_variance": variance,
        "residual_variance": float(result.scale),
        "singular": singular,
        "boundary_warning": boundary,
        "wald_supported": supported,
        "warnings": warning_text,
        "optimizer_method": str(getattr(result, "method", "")),
    })
    # Marginal residual: score minus the fixed-effects prediction.
    exog = np.asarray(result.model.exog, dtype=float)
    fixed_prediction = exog @ np.asarray(result.fe_params.loc[names], dtype=float)
    residual = sample["score"].to_numpy(dtype=float) - fixed_prediction
    diagnostics = sample[["checkpoint_id", "ancestry_cluster_id", "score"]].copy()
    diagnostics["outcome"] = outcome
    diagnostics["fixed_prediction"] = fixed_prediction
    diagnostics["marginal_residual"] = residual
    diagnostics["score_at_boundary"] = diagnostics["score"].isin([0.0, 1.0])
    diagnostics["fit_converged"] = bool(result.converged)
    diagnostics["wald_supported"] = supported
    record["_diagnostics"] = diagnostics

    for name in names:
        coefficients.append({
            "outcome": outcome,
            "term": name,
            "estimate": float(result.fe_params.loc[name]),
            "std_error": float(standard_error.loc[name]) if supported else np.nan,
            "ci_low": float(result.conf_int().loc[name, 0]) if supported else np.nan,
            "ci_high": float(result.conf_int().loc[name, 1]) if supported else np.nan,
            "p_value": float(result.pvalues.loc[name]) if supported else np.nan,
            "wald_supported": supported,
        })
    return record, pd.DataFrame(coefficients)


def term_label(term: str) -> tuple[str, str]:
    if term == "Intercept":
        return (
            "fitted score at 1 billion parameters, Gemma, version rank 0, instruction parent",
            "The intercept is that reference point, not a grand mean.",
        )
    if term == "log2_param_billions":
        return (
            "associated difference per doubling of parameter count",
            "Adjusted for family, version rank, and training category. Not a causal effect of scale.",
        )
    if term == "version_rank":
        return (
            "associated difference per version step",
            "One linear step, the same size in every family. Adjusted for parameter count, family, and training category. Not a causal effect of release.",
        )
    if term.startswith("C(family"):
        level = term.split("[T.")[-1].rstrip("]")
        return (
            f"family difference: {level} versus Gemma",
            "Compared at the same parameter count, version rank, and training category. Families do not cover the same sizes, so part of this contrast is an extrapolation.",
        )
    if "training_category" in term:
        level = term.split("[T.")[-1].rstrip("]")
        return (
            f"training-category difference: {level} versus instruction parents",
            "Adjusted for parameter count, family, and version rank. This mixes within-lineage and between-lineage differences. It is not the paired fine-tuning result.",
        )
    return (term, "")


def category_deltas(cohort: pd.DataFrame) -> pd.DataFrame:
    """Mean fine-tune-minus-parent difference for each fine-tune type.

    Each fine-tune counts once. The interval is CRV3 by ancestry cluster,
    the same estimator as fit_paired. Safety fine-tunes are not analyzed on
    MentalHealthBench (Mark, 24 Oct 2026): their row is kept, with no pairs.
    """
    parents = cohort[cohort["role"] == "instruction"].set_index("checkpoint_id")
    frames = []
    for category in ("mental-health", "medical", "safety"):
        children = cohort[cohort["training_category"] == category]
        pairs = []
        for row in children.itertuples(index=False):
            if row.canonical_parent_id not in parents.index:
                raise SystemExit(f"{row.checkpoint_id} has no single canonical parent checkpoint.")
            parent = parents.loc[row.canonical_parent_id]
            if isinstance(parent, pd.DataFrame):
                raise SystemExit(f"{row.canonical_parent_id} matches more than one parent.")
            for outcome in OUTCOMES:
                if category == "safety" and outcome == "mhb_safety":
                    continue
                child_score = getattr(row, outcome)
                parent_score = parent[outcome]
                if pd.isna(child_score) or pd.isna(parent_score):
                    continue
                pairs.append({
                    "outcome": outcome,
                    "fine_tune_id": row.checkpoint_id,
                    "ancestry_cluster_id": row.ancestry_cluster_id,
                    "child_score": float(child_score),
                    "parent_score": float(parent_score),
                    "delta": float(child_score) - float(parent_score),
                })
        columns = ["outcome", "fine_tune_id", "ancestry_cluster_id", "child_score", "parent_score", "delta"]
        fitted = fit_paired(pd.DataFrame(pairs, columns=columns))
        if category == "safety":
            fitted.loc[fitted["outcome"] == "mhb_safety", "note"] = (
                "Safety fine-tunes are not analyzed on MentalHealthBench."
            )
        fitted.insert(0, "training_category", category)
        frames.append(fitted)
    return pd.concat(frames, ignore_index=True)


def fit_paired(pairs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for outcome in OUTCOMES:
        sample = pairs[pairs["outcome"] == outcome].copy()
        n = len(sample)
        g = int(sample["ancestry_cluster_id"].nunique())
        if n == 0 or g < 2:
            rows.append({
                "outcome": outcome,
                "n_children": n,
                "n_clusters": g,
                "estimate": np.nan,
                "std_error": np.nan,
                "ci_low": np.nan,
                "ci_high": np.nan,
                "p_value": np.nan,
                "inference_df": np.nan,
                "ssc_multiplier": np.nan,
                "supported": False,
                "note": "CRV3 needs at least two ancestry clusters. No other estimator was used.",
            })
            continue
        fit = pf.feols(
            "delta ~ 1",
            data=sample,
            vcov={"CRV3": "ancestry_cluster_id"},
        )
        estimate = float(np.asarray(fit.coef()).reshape(-1)[0])
        se = float(np.asarray(fit.se()).reshape(-1)[0])
        p_value = float(np.asarray(fit.pvalue()).reshape(-1)[0])
        ci = np.asarray(fit.confint(), dtype=float).reshape(-1)
        inference_df = float(g - 1)
        t_crit = float(scipy.stats.t.ppf(0.975, inference_df))
        rebuilt = (estimate - t_crit * se, estimate + t_crit * se)
        if not np.allclose(ci, rebuilt, rtol=0, atol=1e-8):
            raise SystemExit(
                f"{outcome}: interval does not match a t interval with {inference_df:.0f} df."
            )
        ssc = dict(fit._ssc_dict)
        expected_ssc = {
            "adj": True,
            "fixef_k": "none",
            "cluster_adj": True,
            "cluster_df": "min",
        }
        if ssc != expected_ssc:
            raise SystemExit(f"{outcome}: unexpected small-sample settings {ssc}.")
        g_from_fit = int(np.min(np.asarray(fit._G)))
        if g_from_fit != g:
            raise SystemExit(
                f"{outcome}: cluster count {g} does not match the fit ({g_from_fit})."
            )
        n_params = int(fit._k)
        multiplier = (n - 1) / (n - n_params) * g / (g - 1)
        fitted_multiplier = float(np.ravel(fit._ssc)[0])
        if abs(fitted_multiplier - multiplier) > 1e-8:
            raise SystemExit(
                f"{outcome}: small-sample multiplier {fitted_multiplier} "
                f"is not {multiplier}."
            )
        # The interval rebuilt above uses a t critical value at G-1.
        # That match is the check that inference df is clusters minus 1.
        rows.append({
            "outcome": outcome,
            "n_children": n,
            "n_clusters": g,
            "estimate": estimate,
            "std_error": se,
            "ci_low": float(ci[0]),
            "ci_high": float(ci[1]),
            "p_value": p_value,
            "inference_df": inference_df,
            "ssc_multiplier": multiplier,
            "supported": True,
            "note": (
                "Equal-weight mean of child-minus-parent differences. "
                f"CRV3, t with {inference_df:.0f} df (clusters minus 1). "
                "The interval is not multiplicity-adjusted."
            ),
        })
    fitted = pd.DataFrame(rows)
    usable = fitted[fitted["supported"]]
    if len(usable) != 3:
        fitted["p_bh"] = np.nan
        fitted["bh_note"] = "BH was not applied because not all three outcomes were estimable."
        return fitted
    reject, p_bh, _a, _b = multipletests(
        usable["p_value"].to_numpy(), alpha=0.05, method="fdr_bh"
    )
    fitted["p_bh"] = np.nan
    fitted.loc[usable.index, "p_bh"] = p_bh
    fitted["bh_rejected_0_05"] = False
    fitted.loc[usable.index, "bh_rejected_0_05"] = reject
    fitted["bh_note"] = (
        "Benjamini-Hochberg across these three fraction-scale tests only."
    )
    return fitted


FINE_TUNE_ONLY_FORMULA = (
    "score ~ log2_param_billions"
    " + C(family, Treatment(reference='Gemma'))"
    " + version_rank"
    " + C(training_category, Treatment(reference='mental-health'))"
    " + C(method, Treatment(reference='Full'))"
    " + C(objective, Treatment(reference='SFT'))"
)


def _adapter_and_objective(row: dict) -> tuple[str, str]:
    """Q/LoRA pools LoRA and QLoRA. Other pools every objective except SFT."""
    from orchestration.study_roster import method_code, objective_code

    method = method_code(row)
    objective = objective_code(row)
    if method == "Full":
        adapter = "Full"
    elif method in ("LoRA", "QLoRA"):
        adapter = "Q/LoRA"
    else:
        raise SystemExit(f"{row['hf_id']} method {method!r} is not Full, LoRA, or QLoRA")
    if objective == "SFT":
        group = "SFT"
    elif objective in ("GRPO", "DPO", "Distillation", "More than one stage"):
        group = "Other"
    else:
        raise SystemExit(f"{row['hf_id']} objective {objective!r} is not a known training objective")
    return adapter, group


def _term_key(name: str) -> str:
    if name in ("Intercept", "log2_param_billions", "version_rank"):
        return name
    if "training_category" in name or "family" in name or "method" in name or "objective" in name:
        return name.split("[T.")[-1].rstrip("]")
    raise SystemExit(f"fine-tune-only model has an unlabeled term {name}")


def _crv3_coefficients(sample: pd.DataFrame, outcome: str) -> list[dict]:
    """Ordinary least squares, CRV3 by lineage, t with clusters minus 1."""
    g = int(sample["ancestry_cluster_id"].nunique())
    if g < 2:
        raise SystemExit(f"{outcome}: CRV3 needs at least two lineages")
    fit = pf.feols(FINE_TUNE_ONLY_FORMULA, data=sample, vcov={"CRV3": "ancestry_cluster_id"})
    ssc = dict(fit._ssc_dict)
    expected_ssc = {"adj": True, "fixef_k": "none", "cluster_adj": True, "cluster_df": "min"}
    if ssc != expected_ssc:
        raise SystemExit(f"{outcome}: unexpected small-sample settings {ssc}")
    if int(np.min(np.asarray(fit._G))) != g:
        raise SystemExit(f"{outcome}: cluster count does not match the CRV3 fit")
    inference_df = g - 1
    t_crit = float(scipy.stats.t.ppf(0.975, inference_df))
    rows = []
    ci = fit.confint()
    for name in fit.coef().index:
        estimate = float(fit.coef().loc[name])
        se = float(fit.se().loc[name])
        low, high = [float(value) for value in ci.loc[name].tolist()]
        rebuilt = (estimate - t_crit * se, estimate + t_crit * se)
        if not np.allclose((low, high), rebuilt, rtol=0, atol=1e-6):
            raise SystemExit(f"{outcome} {name}: CRV3 interval is not a t interval with {inference_df} df")
        rows.append({
            "outcome": outcome,
            "term": _term_key(str(name)),
            "estimate": estimate,
            "std_error": se,
            "ci_low": low,
            "ci_high": high,
            "p_value": float(fit.pvalue().loc[name]),
            "inference": "ols_crv3",
            "n_observations": len(sample),
            "n_clusters": g,
            "random_intercept_variance": np.nan,
        })
    return rows


def write_fine_tune_only(cohort: pd.DataFrame, out: Path) -> Path:
    """Fine-tunes only. LoRA and QLoRA are one method. Parents are not rows.

    One ordinary least-squares regression with CRV3 standard errors by
    instruction-tuned parent, for every benchmark. A mixed-model Wald
    interval is not used: the random-intercept variance is not interior
    on every task, and the table does not switch estimators by task.
    """
    from orchestration.study_roster import load_roster

    codes = {}
    for row in load_roster():
        if row["role"] != "fine-tune" or not labeled_fine_tune(row):
            continue
        codes[row["hf_id"]] = _adapter_and_objective(row)
    fine = cohort[cohort["role"] == "fine-tune"].copy()
    missing = sorted(set(fine["checkpoint_id"]) - set(codes))
    if missing:
        raise SystemExit("fine-tune-only model has no method and objective for: " + "; ".join(missing))
    fine["method"] = fine["checkpoint_id"].map(lambda hf_id: codes[hf_id][0])
    fine["objective"] = fine["checkpoint_id"].map(lambda hf_id: codes[hf_id][1])
    observations, _excluded = joint_observations(fine)
    observations = observations.merge(
        fine[["checkpoint_id", "method", "objective"]], on="checkpoint_id", how="left"
    )
    if observations[["method", "objective"]].isna().any().any():
        raise SystemExit("a fine-tune-only row lost method or objective")

    rows = []
    for outcome in OUTCOMES:
        sample = observations[observations["outcome"] == outcome].copy()
        _y, design = dmatrices(FINE_TUNE_ONLY_FORMULA, sample, return_type="dataframe")
        rank = int(np.linalg.matrix_rank(np.asarray(design, dtype=float)))
        if rank != design.shape[1]:
            raise SystemExit(
                f"{outcome}: fine-tune-only design is rank {rank} of {design.shape[1]}. No term was dropped."
            )
        rows.extend(_crv3_coefficients(sample, outcome))
    frame = pd.DataFrame(rows)
    if frame.empty:
        raise SystemExit("fine-tune-only model produced no coefficients")
    frame["unit"] = "score (0-1)"
    dest = Path(out) / "fine-tune-only-estimates.csv"
    frame.to_csv(dest, index=False)
    print(f"wrote {dest}")
    return dest


def scale_mhb(estimate, se, low, high):
    return (
        estimate * 100.0 if pd.notna(estimate) else np.nan,
        se * 100.0 if pd.notna(se) else np.nan,
        low * 100.0 if pd.notna(low) else np.nan,
        high * 100.0 if pd.notna(high) else np.nan,
    )


def _apply_parse_mode(roster: pd.DataFrame, mode: str) -> pd.DataFrame:
    """Replace yes/no F1. sonnet must match the roster. strict overwrites it.

    MentalHealthBench is not a parse. Those scores stay as they are.
    """
    from orchestration.fill_roster_scores import f1_by_model

    if mode not in {"strict", "sonnet"}:
        raise SystemExit(f"parse mode must be strict or sonnet, not {mode!r}")
    scores = f1_by_model(set(roster["hf_id"].astype(str)), mode)
    mismatches = []
    replaced = roster.copy()
    for column in ("si_f1", "cssrs_f1"):
        fresh = []
        for hf_id, current in zip(replaced["hf_id"], replaced[column]):
            value = scores[str(hf_id)][column]
            blank = pd.isna(current) or str(current).strip() == ""
            if value is None:
                if not blank:
                    mismatches.append(f"{hf_id} {column}: roster {current}, recompute blank")
                fresh.append(np.nan)
                continue
            if blank:
                mismatches.append(f"{hf_id} {column}: roster blank, recompute {value}")
                fresh.append(np.nan)
                continue
            if mode == "sonnet" and abs(float(current) - value) > 5e-7:
                mismatches.append(
                    f"{hf_id} {column}: roster {current} vs sonnet {value}"
                )
            fresh.append(value if mode == "strict" else float(current))
        if mode == "strict":
            replaced[column] = fresh
    if mode == "sonnet" and mismatches:
        raise SystemExit(
            "Sonnet F1 does not match the roster:\n" + "\n".join(mismatches)
        )
    if mode == "strict" and mismatches:
        raise SystemExit(
            "Strict F1 could not be computed where the roster has a score:\n"
            + "\n".join(mismatches)
        )
    return replaced


def main(out: Path, parse_mode: str | None = None) -> Path:
    global OUT
    OUT = Path(out)
    OUT.mkdir(parents=True, exist_ok=True)
    smoke = smoke_test_crv3()
    current = read_current()
    roster, source, source_hash = load_snapshot(current)
    if parse_mode is not None:
        roster = _apply_parse_mode(roster, parse_mode)
        with (OUT / "roster-source.txt").open("a", encoding="utf-8") as handle:
            handle.write(f"parse_mode: {parse_mode}\n")
    ranks = rank_table()
    ranks.to_csv(OUT / "version-rank-mapping.csv", index=False)
    _labeled, unlabeled = split_labeled(roster)
    unlabeled[["hf_id", "grouping", "training_method", "training_objective_stages"]].to_csv(
        OUT / "unlabeled-fine-tunes.csv", index=False
    )

    cohort, conflicts, mismatches = build_cohort(roster, ranks)
    coverage, steps = coverage_tables(cohort, ranks)
    cohort.to_csv(OUT / "checkpoints.csv", index=False)
    conflicts.to_csv(OUT / "rehost-score-conflicts.csv", index=False)
    mismatches.to_csv(OUT / "parent-child-label-mismatches.csv", index=False)
    coverage.to_csv(OUT / "version-coverage-by-family.csv", index=False)
    steps.to_csv(OUT / "version-steps.csv", index=False)

    observations, joint_excluded = joint_observations(cohort)
    observations.to_csv(OUT / "joint-observations.csv", index=False)

    joint_fits = []
    joint_coefs = []
    residual_frames = []
    for outcome in OUTCOMES:
        sample = observations[observations["outcome"] == outcome].copy()
        record, coefficients = fit_joint(sample, outcome)
        diagnostics = record.pop("_diagnostics", None)
        joint_fits.append(record)
        if diagnostics is not None:
            residual_frames.append(diagnostics)
        if len(coefficients):
            joint_coefs.append(coefficients)
    joint_fit_table = pd.DataFrame(joint_fits)
    joint_coef_table = (
        pd.concat(joint_coefs, ignore_index=True) if joint_coefs else pd.DataFrame()
    )
    joint_fit_table.to_csv(OUT / "joint-model-fit.csv", index=False)
    if residual_frames:
        pd.concat(residual_frames, ignore_index=True).to_csv(
            OUT / "joint-residuals.csv", index=False
        )

    joint_excluded.to_csv(OUT / "exclusions.csv", index=False)
    category_deltas(cohort).to_csv(OUT / "category-deltas.csv", index=False)

    estimate_rows = []
    for row in joint_coef_table.itertuples(index=False):
        fit = joint_fit_table[joint_fit_table["outcome"] == row.outcome].iloc[0]
        label, note = term_label(row.term)
        if not row.wald_supported:
            note = (
                "Not a completed estimate. "
                + (fit.fit_error or "Wald interval is not supported.")
                + " " + note
            )
        base = {
            "analysis": "joint_mixed_model",
            "role_in_paper": "Table 1",
            "outcome": row.outcome,
            "estimand": label,
            "term": row.term,
            "n_observations": int(fit.n_observations),
            "n_clusters": int(fit.n_clusters),
            "estimate": row.estimate,
            "std_error": row.std_error,
            "ci_low": row.ci_low,
            "ci_high": row.ci_high,
            "interval": "Wald interval" if row.wald_supported else "",
            "p_value": row.p_value,
            "p_bh": np.nan,
            "inference_df": np.nan,
            "notes": note,
            "source_roster": str(source),
            "source_sha256": source_hash,
        }
        estimate_rows.append({**base, "unit": "score (0-1)"})
        if row.outcome == "mhb_safety":
            est, se, low, high = scale_mhb(
                row.estimate, row.std_error, row.ci_low, row.ci_high
            )
            estimate_rows.append({
                **base,
                "unit": "percentage points",
                "estimate": est,
                "std_error": se,
                "ci_low": low,
                "ci_high": high,
                "notes": "Same fit, multiplied by 100. " + note,
            })

    pd.DataFrame(estimate_rows).to_csv(OUT / "estimates.csv", index=False)

    versions = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "pandas": pd.__version__,
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "statsmodels": statsmodels.__version__,
        "pyfixest": pf.__version__,
        "crv3_smoke_test_se": smoke["se"],
        "mixedlm": {
            "reml": True,
            "intervals": "Wald, standard normal, use_t False",
            "singular_if_random_intercept_variance_at_most": SINGULAR_VARIANCE,
            "formula": JOINT_FORMULA,
            "random_intercept": "ancestry_cluster_id (canonical instruction parent)",
        },
        "paired": {
            "formula": "delta ~ 1",
            "vcov": {"CRV3": "ancestry_cluster_id"},
            "inference_df": "number of ancestry clusters minus 1",
            "interval": "ordinary t interval, not multiplicity-adjusted",
            "output": "category-deltas.csv",
            "multiplicity": (
                "Within each fine-tune type, Benjamini-Hochberg across the "
                "estimable outcomes in that type. Table S4 recomputes "
                "Benjamini-Hochberg across the tests it displays."
            ),
        },
        "rehost_rule": REHOST_OF,
        "source_roster": str(source),
        "source_sha256": source_hash,
    }
    (OUT / "package-versions.json").write_text(
        json.dumps(versions, indent=2) + "\n", encoding="utf-8"
    )
    write_note(
        source, source_hash, cohort, conflicts, coverage, steps,
        joint_fit_table, joint_coef_table, mismatches, unlabeled,
        parse_mode,
    )
    print(f"Wrote {OUT}")
    print(joint_fit_table[
        ["outcome", "n_observations", "n_clusters", "design_full_rank",
         "converged", "random_intercept_variance", "wald_supported"]
    ].to_string(index=False))
    return OUT


def fmt(value, digits=4) -> str:
    if pd.isna(value):
        return "not estimated"
    return f"{float(value):.{digits}f}"


def write_note(source, source_hash, cohort, conflicts, coverage, steps,
               joint_fits, joint_coefs, mismatches, unlabeled,
               parse_mode: str | None = None) -> None:
    lines = []
    lines.append("# Joint description and fine-tune-minus-parent differences")
    lines.append("")
    lines.append(
        f"Roster snapshot: `{source}` sha256 `{source_hash}`. "
        f"The snapshot is `roster-snapshot.csv` in this directory. "
        f"Counts below come from that file."
    )
    lines.append("")
    lines.append(
        f"The cohort is {len(cohort)} checkpoints: "
        f"{int((cohort.role == 'instruction').sum())} instruction-tuned parents "
        f"and {int((cohort.role == 'fine-tune').sum())} fine-tunes whose "
        "weight-update method and training objective are both stated "
        f"({len(unlabeled)} fine-tunes without both are listed in "
        "`unlabeled-fine-tunes.csv` and are not fit). "
        "Pretrained checkpoints are not included. "
        "`unsloth/gemma-3-1b-it` is `google/gemma-3-1b-it`. "
        "`unsloth/gemma-3-4b-it` is `google/gemma-3-4b-it`. "
        "Each pair is one checkpoint. The Google score is the score used. "
        "Unsloth scores that differ are listed in `rehost-score-conflicts.csv` "
        "and are not averaged in."
    )
    differ = conflicts[conflicts["scores_differ"]]
    if len(differ):
        bits = [
            f"{row.canonical_id} {row.outcome}: Google {row.canonical_score}, "
            f"Unsloth {row.rehost_score}"
            for row in differ.itertuples(index=False)
        ]
        lines.append("")
        lines.append("Scores that differ: " + "; ".join(bits) + ".")
    lines.append("")
    lines.append("## Release rank")
    lines.append("")
    lines.append(
        "Version rank is the release order inside a family, written to "
        "`version-rank-mapping.csv` before either fit. Children inherit the "
        "parent's family and rank. Gemma 1 is rank 0 and Gemma 3 is rank 2, "
        "because Gemma 2 is the generation between them and is not in this "
        "roster. Gemma 3n is rank 3, one step after Gemma 3, and is not "
        "Gemma 4. All four Gemma 3n checkpoints, two instruction parents and "
        "two fine-tunes, enter as 2 and 4 billion effective parameters. "
        "Mistral 7B v0.2 and v0.3 share rank 0. SmolLM has one release. "
        "Neither Mistral nor SmolLM identifies the version slope."
    )
    lines.append("")
    lines.append(
        "The version coefficient is one linear change per rank step, shared "
        "by every family, after adjustment for log2 parameter count. It is "
        "an adjusted association, not a causal effect of a release. The "
        "steps that keep the same size label are Llama 3 to Llama 3.1 at "
        "8B and Qwen3 to Qwen3.5 at 4B. The other steps also change which "
        "sizes are present. The list is `version-steps.csv`."
    )
    if len(mismatches):
        lines.append("")
        lines.append(
            f"{len(mismatches)} fine-tunes had a family, version, or size "
            "label that did not match the canonical parent. The parent label "
            "was used. The rows are in `parent-child-label-mismatches.csv`."
        )
    lines.append("")
    lines.append("## Joint mixed model (secondary)")
    lines.append("")
    lines.append(
        "For each outcome separately: score on the 0–1 scale, log2 of the "
        "parameter count in billions, family (reference Gemma), version rank, "
        "and training category (reference instruction parent). Random "
        "intercept for the canonical instruction parent and its children. "
        "A parent is one row, not one row per child. REML. Intervals are "
        "Wald intervals. Gemma 3n E2B and E4B enter as 2 and 4 billion "
        "effective parameters. "
        "Safety fine-tunes are out of the MentalHealthBench model. An "
        "instruction-tuned parent is out of that model when no mental-health "
        "or medical fine-tune of that parent is in the study."
    )
    lines.append("")
    for outcome in OUTCOMES:
        fit = joint_fits[joint_fits["outcome"] == outcome].iloc[0]
        lines.append(
            f"- {OUTCOME_NAME[outcome]}: {int(fit.n_observations)} checkpoints, "
            f"{int(fit.n_clusters)} clusters, design full rank "
            f"{bool(fit.design_full_rank)}, converged {bool(fit.converged)}, "
            f"random-intercept variance {fmt(fit.random_intercept_variance, 6)}, "
            f"residual variance {fmt(fit.residual_variance, 6)}, "
            f"Wald intervals supported {bool(fit.wald_supported)}."
        )
        if fit.fit_error:
            lines.append(f"  Fit note: {fit.fit_error}")
        if fit.boundary_warning and fit.wald_supported:
            lines.append(
                "  statsmodels warned that the random-intercept variance may "
                "be on the boundary of its parameter space. That warning "
                "appears when a variance is below about 0.01. The rule used "
                f"here treats a variance of {SINGULAR_VARIANCE:g} or below as "
                "singular. This fit is above that line, so the Wald intervals "
                "are reported."
            )
        if fit.warnings and not fit.wald_supported:
            lines.append(f"  Warning: {fit.warnings}")
    usable = joint_coefs[joint_coefs["wald_supported"]] if len(joint_coefs) else joint_coefs
    failed = joint_fits[~joint_fits["wald_supported"]]
    if len(usable):
        lines.append("")
        lines.append("Coefficients below are on the 0–1 score scale.")
        lines.append("")
        for row in usable.itertuples(index=False):
            label, _note = term_label(row.term)
            lines.append(
                f"- {row.outcome}, {label}: {fmt(row.estimate)} "
                f"(Wald interval {fmt(row.ci_low)} to {fmt(row.ci_high)})."
            )
    if len(failed):
        lines.append("")
        for fit in failed.itertuples(index=False):
            lines.append(
                f"{OUTCOME_NAME[fit.outcome]}: the mixed model did not "
                "produce a usable fit, so no coefficient from it is reported "
                "here. The optimizer's last values are stored in "
                "`estimates.csv` with blank standard errors and are not "
                "completed estimates. The formula was not changed."
            )
    residual_path = OUT / "joint-residuals.csv"
    if residual_path.is_file():
        residuals = pd.read_csv(residual_path)
        lines.append("")
        lines.append(
            "Marginal residuals are the score minus the fixed-effects "
            "prediction. They are not forced to average zero, because the "
            "random intercepts absorb lineage means. A score of 0 or 1 was "
            "left as 0 or 1."
        )
        lines.append("")
        for outcome, sub in residuals.groupby("outcome"):
            n0 = int((sub["score"] == 0).sum())
            n1 = int((sub["score"] == 1).sum())
            lines.append(
                f"- {outcome}: {len(sub)} residuals, "
                f"{n0} score{'s' if n0 != 1 else ''} at 0, "
                f"{n1} score{'s' if n1 != 1 else ''} at 1, "
                f"mean residual {fmt(sub['marginal_residual'].mean())}, "
                f"SD {fmt(sub['marginal_residual'].std())}. "
                f"Fit converged: {bool(sub['fit_converged'].iloc[0])}."
            )
    lines.append("")
    lines.append("## Fine-tune minus instruction-tuned parent")
    lines.append("")
    lines.append(
        "category-deltas.csv holds the equal-weight mean of fine-tune minus "
        "instruction-tuned parent for mental-health, medical, and safety. "
        "Each fine-tune type is an intercept-only model with CRV3 standard "
        "errors by ancestry cluster. Safety has no MentalHealthBench rows. "
        "Table S4 recomputes Benjamini-Hochberg across the tests it displays."
    )
    (OUT / "results-note.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (OUT / "inference-settings.md").write_text(
        "\n".join([
            "# Settings",
            "",
            f"- Roster: `{source}`",
            f"- SHA-256: `{source_hash}`",
            "- Python: `.venv/bin/python`.",
            f"- pyfixest {pf.__version__}, statsmodels {statsmodels.__version__}.",
            "- Rehosts: `unsloth/gemma-3-1b-it` = `google/gemma-3-1b-it`; "
            "`unsloth/gemma-3-4b-it` = `google/gemma-3-4b-it`. Google scores are used.",
            "- Joint formula: `" + JOINT_FORMULA + "`.",
            "- Joint estimation: MixedLM, REML, one random intercept.",
            "- Joint intervals: Wald, standard normal. Labeled Wald only when "
            f"the fit converged and the random-intercept variance is above {SINGULAR_VARIANCE}.",
            "- Fine-tune minus parent: `delta ~ 1`, separately for mental-health, medical, and safety.",
            "- Fine-tune minus parent covariance: pyfixest CRV3 by `ancestry_cluster_id`.",
            "- Fine-tune minus parent degrees of freedom: clusters minus 1.",
            "- Fine-tune minus parent output: `category-deltas.csv`.",
            "- Table S4 recomputes Benjamini-Hochberg across the tests it displays.",
            "- No other model was fit.",
            "- Yes/no F1 parse: "
            + (parse_mode or "roster columns, Sonnet-recovered")
            + ".",
            "",
        ]),
        encoding="utf-8",
    )


if __name__ == "__main__":
    raise SystemExit("run orchestration/fit_mixed_models.py; it names the output folder")
