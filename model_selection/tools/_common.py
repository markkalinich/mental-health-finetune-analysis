"""Shared paths and arguments for the tools/ scripts. Every script takes --grouping and --date."""
import argparse
from pathlib import Path
REPO = Path(__file__).resolve().parents[2]
INV = REPO / "model_selection"
DOCS_FOLDER = {"mental-health": "mental_health_FT_funnel", "safety": "safety_FT_funnel", "medical": "medical_FT_funnel"}


def parser(doc: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=doc)
    p.add_argument("--grouping", required=True, choices=sorted(DOCS_FOLDER))
    p.add_argument("--date", help="date of the agent-search folder (default: the date in outputs/funnel/<grouping>/CURRENT)")
    p.add_argument("--run", help="results folder to read (default: outputs/funnel/<grouping>/<CURRENT>)")
    return p


def resolve(args):
    cur = (REPO / "outputs" / "funnel" / args.grouping / "CURRENT").read_text().strip()
    args.run_dir = Path(args.run) if args.run else REPO / "outputs" / "funnel" / args.grouping / cur
    args.date = args.date or cur
    args.docs = REPO / "docs" / DOCS_FOLDER[args.grouping]
    args.searches = args.docs / "agent-searches"
    return args


def newest_card(hf_id: str):
    fs = sorted((INV / "cache" / "readmes").glob(f"{hf_id.replace('/', '__')}__*.md"))
    return fs[-1] if fs else None


def long_date(d: str) -> str:
    import datetime
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")
