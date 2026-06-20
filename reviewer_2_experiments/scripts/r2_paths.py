"""Canonical paths for reviewer_2_experiments (mirrors repo-root layout)."""
from pathlib import Path

R2 = Path(__file__).resolve().parents[1]
ROOT = R2.parent

REVIEWER_DOC = R2 / "REVIEWER_2_EXPERIMENTS.md"
SCRIPTS = R2 / "scripts"
BASH = R2 / "bash_scripts"
DATA = R2 / "data"
RESULTS = R2 / "results"
CACHE = R2 / "cache"
LOGS = R2 / "logs"

PROVENANCE = DATA / "provenance"
TEMPLATES = DATA / "templates"
BREAK_TESTS = DATA / "break_tests"
TEMPLATE_BACKUPS = DATA / "template_backups"

def parse_results_root(min_parse: float, task_args: list[str]) -> Path:
    """Root for one parse-cutoff sensitivity run, e.g. results/parse50pct_per_task/."""
    pct = int(round(min_parse * 100))
    if "per_task" in task_args:
        suffix = "per_task"
    elif "all" in task_args:
        suffix = "all3tasks"
    elif "any" in task_args:
        suffix = "anytask"
    else:
        suffix = "_".join(t.lower() for t in task_args)
    return RESULTS / f"parse{pct}pct_{suffix}"


def parse_run_dirs(min_parse: float, task_args: list[str]) -> dict[str, Path]:
    root = parse_results_root(min_parse, task_args)
    return {
        "root": root,
        "cohort": root / "cohort",
        "table1": root / "table_1",
        "fig2": root / "figure_2",
        "fig3": root / "figure_3",
    }


# Manuscript sensitivity cohort (parse≥50% per-task).
PARSE50 = parse_results_root(0.50, ["per_task"])
PARSE50_COHORT = PARSE50 / "cohort"
PARSE50_TABLE1 = PARSE50 / "table_1"
PARSE50_FIG2 = PARSE50 / "figure_2"
PARSE50_FIG3 = PARSE50 / "figure_3"

SG1_RUN = CACHE / "shieldgemma_sg1_patched"
SG1_CACHE = SG1_RUN / "cache"
SG1_RESULTS = RESULTS / "shieldgemma" / "sg1_patched"
SG2_RUN = CACHE / "shieldgemma_24b_sg2"
SG2_CACHE = SG2_RUN / "cache"
SG2_RESULTS = RESULTS / "shieldgemma" / "sg2_24b"
