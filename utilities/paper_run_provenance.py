"""
Write PROVENANCE.json (machine-generated run record) for a paper pipeline run.

This is not a user-authored manifest; see docs/PROVENANCE_PLAN.md.

**Files read** (hashed or path-recorded):
  - ``cache/results.db`` (resolved path + SHA-256 of file bytes)
  - ``config/models_config.csv``
  - ``data/inputs/model_results/all_models_all_tasks.csv``
  - Per task in ``TASKS``: finalized input CSV and prompt file (3 tasks × 2 = 6 paths)
  - For each resolved experiment dir: ``tables/comprehensive_metrics.csv`` (path + hash)

**Also recorded** (not necessarily files): ``git rev-parse HEAD``, ``git status --porcelain``,
``sys.argv``, hostname, Python version, CLI flags, Phase 1 output dir paths, exit code.

**Output file** (single JSON):
  - ``<output_dir>/PROVENANCE.json`` where ``output_dir`` is
    ``results/FINETUNE_PAPER_FIGURES/<YYYYMMDD_HHMMSS>/``

File-level SHA-256 for SQLite is intentional; see PROVENANCE_PLAN deferred canonicalization note.
"""

from __future__ import annotations

import hashlib
import json
import socket
import subprocess
import sys
from argparse import Namespace
from pathlib import Path
from typing import Any, Dict, List, Optional


def sha256_file(path: Path) -> Optional[str]:
    if not path.is_file():
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _git_rev_parse_head(repo_root: Path) -> Optional[str]:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if out.returncode == 0:
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def _git_is_dirty(repo_root: Path) -> Optional[bool]:
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if out.returncode == 0:
            return len(out.stdout.strip()) > 0
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def _input_entries(repo_root: Path, tasks_config: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    paths: List[Path] = []
    for _task, cfg in tasks_config.items():
        paths.append(repo_root / cfg["input_data"])
        paths.append(repo_root / cfg["prompt_file"])
    paths.append(repo_root / "config" / "models_config.csv")
    combined = repo_root / "data" / "inputs" / "model_results" / "all_models_all_tasks.csv"
    paths.append(combined)

    seen = set()
    out: List[Dict[str, Any]] = []
    for p in paths:
        rp = p.resolve()
        if rp in seen:
            continue
        seen.add(rp)
        out.append(
            {
                "path": str(p),
                "sha256": sha256_file(p) if p.is_file() else None,
                "missing": not p.is_file(),
            }
        )
    return out


def _tasks_config_block(
    repo_root: Path, tasks_config: Dict[str, Dict[str, Any]]
) -> Dict[str, Any]:
    """Structured record of each task's inputs with per-file hashes."""
    out: Dict[str, Any] = {}
    for task_name, cfg in tasks_config.items():
        stmt_path = repo_root / cfg["input_data"]
        prompt_path = repo_root / cfg["prompt_file"]
        out[task_name] = {
            "short_name": cfg.get("short_name"),
            "statements_csv": str(stmt_path),
            "statements_sha256": sha256_file(stmt_path),
            "prompt_file": str(prompt_path),
            "prompt_name": cfg.get("prompt_name"),
            "prompt_sha256": sha256_file(prompt_path),
        }
    return out


def _experiment_parameters() -> Dict[str, Any]:
    """Record default experiment parameters used for inference.

    These come from ``config.utils.EvaluationConfig`` defaults.  If a run
    overrides them (not currently exposed in the paper pipeline CLI), update
    this function to accept the actual values.
    """
    try:
        from config.utils import EvaluationConfig

        defaults = EvaluationConfig()
        return {
            "temperature": defaults.temperature,
            "max_tokens": defaults.max_tokens,
            "top_p": defaults.top_p,
        }
    except Exception:
        return {"temperature": None, "max_tokens": None, "top_p": None}


def _combine_results_block(task_dirs: Optional[Dict[str, Path]]) -> Dict[str, Any]:
    if not task_dirs:
        return {"tasks": {}}
    tasks: Dict[str, Any] = {}
    for name, d in task_dirs.items():
        p = d.resolve()
        metrics = p / "tables" / "comprehensive_metrics.csv"
        tasks[name] = {
            "experiment_dir": str(p),
            "comprehensive_metrics_csv": str(metrics),
            "comprehensive_metrics_sha256": sha256_file(metrics) if metrics.is_file() else None,
        }
    return {"tasks": tasks}


def build_paper_run_provenance(
    repo_root: Path,
    run_timestamp: str,
    output_dir: Path,
    args: Namespace,
    task_dirs: Optional[Dict[str, Path]],
    experiment_results: Dict[str, Optional[Path]],
    exit_code: int,
    tasks_config: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    cache_path = (repo_root / "cache" / "results.db").resolve()
    return {
        "schema": "paper_run_provenance_v1",
        "pipeline": "run_paper_pipeline.py",
        "timestamp": run_timestamp,
        "output_dir": str(output_dir.resolve()),
        "exit_code": exit_code,
        "dry_run": bool(args.dry_run),
        "git": {
            "commit": _git_rev_parse_head(repo_root),
            "dirty": _git_is_dirty(repo_root),
        },
        "cache": {
            "path": str(cache_path),
            "sha256": sha256_file(cache_path) if cache_path.is_file() else None,
        },
        "command": list(sys.argv),
        "environment": {
            "python": sys.version.split()[0],
            "hostname": socket.gethostname(),
        },
        "cli": {
            "skip_experiments": bool(args.skip_experiments),
            "skip_supplementary": bool(args.skip_supplementary),
            "figures_only": bool(args.figures_only),
            "table_only": bool(args.table_only),
            "use_latest_experiment_dirs": bool(
                getattr(args, "use_latest_experiment_dirs", False)
            ),
            "si_dir": getattr(args, "si_dir", None),
            "tr_dir": getattr(args, "tr_dir", None),
            "te_dir": getattr(args, "te_dir", None),
        },
        "phase1_experiment_output_dirs": {
            k: str(v.resolve()) if v is not None else None
            for k, v in experiment_results.items()
        },
        "tasks": _tasks_config_block(repo_root, tasks_config),
        "experiment_parameters": _experiment_parameters(),
        "combine_results": _combine_results_block(task_dirs),
        "inputs": _input_entries(repo_root, tasks_config),
    }


def write_paper_run_provenance(
    repo_root: Path,
    run_timestamp: str,
    output_dir: Path,
    args: Namespace,
    task_dirs: Optional[Dict[str, Path]],
    experiment_results: Dict[str, Optional[Path]],
    exit_code: int,
    tasks_config: Dict[str, Dict[str, Any]],
) -> Path:
    data = build_paper_run_provenance(
        repo_root=repo_root,
        run_timestamp=run_timestamp,
        output_dir=output_dir,
        args=args,
        task_dirs=task_dirs,
        experiment_results=experiment_results,
        exit_code=exit_code,
        tasks_config=tasks_config,
    )
    out_path = output_dir / "PROVENANCE.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=False)
        f.write("\n")
    return out_path
