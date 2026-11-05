"""Re-read gated repos that were cached as inaccessible, after access was granted.

    export HF_TOKEN="$(cat ~/.cache/huggingface/token)" && \
    .venv/bin/python model_selection/tools/refetch_repos.py --grouping safety \
        --repos-from docs/safety_FT_funnel/review-2026-10-09-access-requests.csv [--date YYYY-MM-DD]

For every repo id in the `hf_id` column of --repos-from (or given with --repo, repeatable): one card GET,
one README GET, one config.json GET, written into the cache dated --date (default: today, UTC) through
hub.fill(). Since 10 Oct 2026 cache.py lets real content replace a same-day FETCH_ERR entry, so this can
run the same day the 403 was cached. A page that is still closed is written as FETCH_ERR again (no change).
Prints one line per repo: `open` (README fetched) or `still closed <reason>`. Then run funnel.py for the
grouping with --as-of <date>.
"""
from __future__ import annotations

import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from _common import parser  # noqa: E402
import cache  # noqa: E402
import hub  # noqa: E402


def main() -> None:
    ap = parser(__doc__)
    date_arg = next(action for action in ap._actions if action.dest == "date")
    date_arg.help = "cache date the fetched pages are written under (default: today, UTC)"
    ap.add_argument("--repos-from", type=Path, help="CSV with an hf_id column")
    ap.add_argument("--repo", action="append", default=[], help="repo id (repeatable)")
    a = ap.parse_args()
    repos = list(a.repo)
    if a.repos_from:
        repos += [r["hf_id"] for r in csv.DictReader(a.repos_from.open()) if r.get("hf_id")]
    repos = sorted(set(repos))
    if not repos:
        sys.exit("no repos given")
    date = a.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    hub.require_hub_token()
    missing = []
    for r in repos:
        missing += [{"kind": "card", "key": r}, {"kind": "readme", "key": r}, {"kind": "config", "key": r}]
    hub.fill(missing, date)
    opened = 0
    for r in repos:
        p = cache.newest_readme(r, date)
        text = p.read_text(encoding="utf-8", errors="replace") if p else ""
        if text and not text.startswith("FETCH_ERR"):
            opened += 1
            print(f"open         {r}")
        else:
            print(f"still closed {r}  {text.strip()[:60]}")
    print(f"{opened} of {len(repos)} open; cache entries dated {date}. Next: funnel.py --grouping {a.grouping} --as-of {date}")


if __name__ == "__main__":
    main()
