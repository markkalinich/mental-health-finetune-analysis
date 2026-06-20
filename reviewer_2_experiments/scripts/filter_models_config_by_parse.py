#!/usr/bin/env python3
"""Build a filtered models_config.csv from parse-success criteria.

Does not modify figure scripts or the canonical config. Joins enabled rows in
config/models_config.csv to data/inputs/model_results/all_models_all_tasks.csv
on (family, size).

Examples:
  .venv/bin/python reviewer_2_experiments/filter_models_config_by_parse.py \\
      --min-parse 0.95 --tasks all

  .venv/bin/python reviewer_2_experiments/filter_models_config_by_parse.py \\
      --min-parse 0.95 --tasks SI TR TE   # must pass each listed task

  .venv/bin/python reviewer_2_experiments/filter_models_config_by_parse.py \\
      --min-parse 0.50 --tasks per_task   # keep row iff parse on that task >= threshold
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from r2_paths import ROOT, parse_results_root

CONFIG = ROOT / "config" / "models_config.csv"
RESULTS = ROOT / "data" / "inputs" / "model_results" / "all_models_all_tasks.csv"

TASK_MAP = {
    "SI": "suicidal_ideation",
    "TR": "therapy_request",
    "TE": "therapy_engagement",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Filter models_config.csv by parse rate")
    p.add_argument(
        "--min-parse",
        type=float,
        default=0.95,
        help="Minimum parse_success_rate (default 0.95)",
    )
    p.add_argument(
        "--tasks",
        nargs="+",
        choices=["all", "any", "per_task", "SI", "TR", "TE"],
        default=["all"],
        help=(
            "all = pass threshold on SI, TR, and TE; "
            "any = pass on at least one task; "
            "per_task = each results row kept iff parse on that row's task >= threshold; "
            "or list SI TR TE explicitly"
        ),
    )
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output models_config CSV path (default: results/parse{pct}pct_*/cohort/models_config_*.csv)",
    )
    p.add_argument(
        "--results-output",
        type=Path,
        default=None,
        help="Filtered all_models_all_tasks.csv (default: sibling of config output)",
    )
    return p.parse_args()


def resolve_required_tasks(task_args: list[str]) -> list[str] | None:
    if "per_task" in task_args:
        return "per_task"  # type: ignore[return-value]
    if "all" in task_args:
        return list(TASK_MAP.values())
    if "any" in task_args:
        return None
    return [TASK_MAP[t] for t in task_args]


def model_passes(
    family: str,
    size: str,
    results: pd.DataFrame,
    min_parse: float,
    required_tasks: list[str] | None,
) -> tuple[bool, dict]:
    rows = results[(results["model_family"] == family) & (results["model_size"] == size)]
    detail: dict = {}
    if rows.empty:
        return False, {"reason": "no_results"}

    for task in TASK_MAP.values():
        tr = rows[rows["task"] == task]
        if tr.empty:
            detail[task] = None
        else:
            detail[task] = float(tr["parse_success_rate"].iloc[0])

    if required_tasks is None:
        ok = any(v is not None and v >= min_parse for v in detail.values())
        return ok, detail

    for task in required_tasks:
        v = detail.get(task)
        if v is None or v < min_parse:
            return False, detail
    return True, detail


def artifact_tag(min_parse: float, tasks: list[str]) -> str:
    """Filename tag shared with run_parse_filtered_outputs.py."""
    pct = int(round(min_parse * 100))
    if "per_task" in tasks:
        return f"parse{pct}pct_per_task"
    if "all" in tasks:
        return f"parse{pct}pct_all3tasks"
    if "any" in tasks:
        return f"parse{pct}pct_anytask"
    return f"parse{pct}pct_" + "_".join(t.lower() for t in tasks)


def default_output_path(min_parse: float, task_args: list[str], kind: str = "config") -> Path:
    tag = artifact_tag(min_parse, task_args)
    out_dir = parse_results_root(min_parse, task_args) / "cohort"
    if kind == "results":
        return out_dir / f"all_models_all_tasks_{tag}.csv"
    return out_dir / f"models_config_{tag}.csv"


def kept_model_keys(filtered_cfg: pd.DataFrame) -> set[tuple[str, str]]:
    enabled = filtered_cfg[filtered_cfg["enabled"] == True]
    return {(r["family"], r["size"]) for _, r in enabled.iterrows()}


def filter_results_per_task(
    results: pd.DataFrame,
    enabled_keys: set[tuple[str, str]],
    min_parse: float,
) -> pd.DataFrame:
    """Keep each (model, task) row iff that task's parse_success_rate >= min_parse."""
    mask = results.apply(
        lambda r: (r["model_family"], r["model_size"]) in enabled_keys,
        axis=1,
    ) & (results["parse_success_rate"] >= min_parse)
    return results[mask].copy()


def main() -> int:
    args = parse_args()
    required = resolve_required_tasks(args.tasks)

    cfg = pd.read_csv(CONFIG)
    results = pd.read_csv(RESULTS)
    enabled = cfg[cfg["enabled"] == True].copy()
    enabled_keys = {(r["family"], r["size"]) for _, r in enabled.iterrows()}

    out_path = args.output or default_output_path(args.min_parse, args.tasks, "config")
    results_path = args.results_output or default_output_path(args.min_parse, args.tasks, "results")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if required == "per_task":
        # Config unchanged: all originally enabled models stay enabled.
        # Filtering applies only at the results-row level (per task).
        out = cfg.copy()
        out.to_csv(out_path, index=False)

        results_out = filter_results_per_task(results, enabled_keys, args.min_parse)
        results_out.to_csv(results_path, index=False)

        per_task_counts = {
            task: int(
                results_out[results_out["task"] == task][
                    ["model_family", "model_size"]
                ].drop_duplicates().shape[0]
            )
            for task in TASK_MAP.values()
        }
        manifest_rows = []
        for _, row in enabled.iterrows():
            _, detail = model_passes(
                row["family"], row["size"], results, args.min_parse, list(TASK_MAP.values())
            )
            passes = {
                task: detail.get(task) is not None and detail[task] >= args.min_parse
                for task in TASK_MAP.values()
            }
            manifest_rows.append(
                {
                    "lm_studio_id": row["lm_studio_id"],
                    "family": row["family"],
                    "size": row["size"],
                    "model_type": row["model_type"],
                    "kept_any_task": any(passes.values()),
                    "kept_tasks": [t for t, ok in passes.items() if ok],
                    **{f"parse_{k}": v for k, v in detail.items() if k != "reason"},
                }
            )

        manifest = {
            "min_parse": args.min_parse,
            "tasks": args.tasks,
            "filter_mode": "per_task",
            "enabled_in": len(enabled),
            "kept_enabled": len(enabled),
            "per_task_model_counts": per_task_counts,
            "output_csv": str(out_path),
            "results_csv": str(results_path),
            "results_rows": len(results_out),
            "source_config": str(CONFIG),
            "source_results": str(RESULTS),
        }
        manifest_path = out_path.with_suffix(".json")
        manifest_path.write_text(
            json.dumps({"summary": manifest, "models": manifest_rows}, indent=2)
        )

        print(f"Wrote config (unchanged enabled flags): {out_path}")
        print(f"Wrote per-task filtered results: {results_path} ({len(results_out)} rows)")
        print(f"Wrote manifest: {manifest_path}")
        print(f"Per-task model counts (parse>={args.min_parse}):")
        for task, n in per_task_counts.items():
            print(f"  {task}: {n}/127")
        return 0

    keep_rows = []
    manifest_rows = []
    for _, row in enabled.iterrows():
        ok, detail = model_passes(
            row["family"], row["size"], results, args.min_parse, required
        )
        manifest_rows.append(
            {
                "lm_studio_id": row["lm_studio_id"],
                "family": row["family"],
                "size": row["size"],
                "model_type": row["model_type"],
                "kept": ok,
                **{f"parse_{k}": v for k, v in detail.items() if k != "reason"},
                **({"reason": detail["reason"]} if "reason" in detail else {}),
            }
        )
        if ok:
            keep_rows.append(row.name)

    filtered = cfg.loc[keep_rows].copy()
    kept_ids = set(filtered["lm_studio_id"])

    # Disable dropped models so downstream scripts that only check enabled=True stay consistent.
    out = cfg.copy()
    out.loc[out["lm_studio_id"].isin(kept_ids), "enabled"] = True
    out.loc[~out["lm_studio_id"].isin(kept_ids), "enabled"] = False
    out.to_csv(out_path, index=False)

    keys = kept_model_keys(out)
    results_out = results[
        results.apply(lambda r: (r["model_family"], r["model_size"]) in keys, axis=1)
    ].copy()
    results_out.to_csv(results_path, index=False)

    manifest = {
        "min_parse": args.min_parse,
        "tasks": args.tasks,
        "required_task_keys": required,
        "enabled_in": len(enabled),
        "kept_enabled": int(filtered["enabled"].sum()),
        "dropped": len(enabled) - len(filtered),
        "output_csv": str(out_path),
        "results_csv": str(results_path),
        "results_rows": len(results_out),
        "source_config": str(CONFIG),
        "source_results": str(RESULTS),
    }
    manifest_path = out_path.with_suffix(".json")
    manifest_path.write_text(json.dumps({"summary": manifest, "models": manifest_rows}, indent=2))

    print(f"Wrote filtered config: {out_path}")
    print(f"Wrote filtered results: {results_path} ({len(results_out)} rows)")
    print(f"Wrote manifest: {manifest_path}")
    print(
        f"Kept {len(filtered)}/{len(enabled)} enabled models "
        f"(min_parse={args.min_parse}, tasks={args.tasks})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
