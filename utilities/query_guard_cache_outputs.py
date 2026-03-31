#!/usr/bin/env python3
"""
Aggregate cached assistant outputs for exploratory docs (ShieldGemma JSON, Qwen Guard lines, LLaMA Guard text).

Run from the repository root with the project venv (see docs/DEVELOPMENT.md):

  .venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family shieldgemma
  .venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family qwen_guard
  .venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family llama_guard
  .venv/bin/python utilities/query_guard_cache_outputs.py --db cache/results.db --family all

Uses the same JSON extraction as the 2b robust path: strip optional leading `` ```json ``, then
parse the substring from the first ``{`` to the last ``}``. Qwen: ``Safety:`` / ``Categories:`` lines.
LLaMA Guard: ``safe`` or ``unsafe`` plus optional second-line taxonomy code (``S11``, etc.).
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

PROMPTS = {
    "SI": "system_suicide_detection_v2",
    "TR": "therapy_request_classifier_v3",
    "TE": "therapy_engagement_conversation_v2",
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def robust_json_object(content: str) -> Optional[Dict[str, Any]]:
    if not content or not str(content).strip():
        return None
    c = content.strip()
    c = re.sub(r"^```(?:json)?\s*\n?", "", c, flags=re.IGNORECASE)
    c = re.sub(r"\n?```\s*$", "", c)
    s, e = c.find("{"), c.rfind("}")
    if s < 0 or e < s:
        return None
    try:
        return json.loads(c[s : e + 1])
    except json.JSONDecodeError:
        return None


def parse_llama_guard_lines(content: str) -> Tuple[str, Optional[str]]:
    """First line `safe` / `unsafe`; second line S-code when unsafe (may be malformed)."""
    c = (content or "").strip()
    if not c:
        return "empty", None
    parts = c.split("\n", 1)
    first = parts[0].strip().lower()
    rest = parts[1].strip() if len(parts) > 1 else None
    if first == "safe" and rest is None:
        return "safe", None
    if first == "unsafe":
        return "unsafe", rest
    return "other", c[:120]


def parse_qwen_lines(content: str) -> Tuple[Optional[str], Optional[str]]:
    safety = category = None
    for line in (content or "").strip().split("\n"):
        line = line.strip()
        if line.startswith("Safety:"):
            safety = line.split(":", 1)[1].strip()
        elif line.startswith("Categories:"):
            category = line.split(":", 1)[1].strip()
    return safety, category


def shieldgemma_block(
    conn: sqlite3.Connection, model_size: str
) -> str:
    lines: List[str] = []
    lines.append(f"## `shieldgemma-{model_size}` (script output)")
    lines.append("")
    for task, pname in PROMPTS.items():
        rows = conn.execute(
            """
            SELECT cr.raw_response, cr.status
            FROM cached_results cr
            JOIN cache_keys ck ON cr.cache_id = ck.cache_id
            WHERE ck.model_family = ? AND ck.model_size = ? AND ck.prompt_name = ?
            """,
            ("shieldgemma", model_size, pname),
        ).fetchall()
        n = len(rows)
        st_ct = Counter()
        empty = 0
        fenced = 0
        parsed_n = 0
        field_a: Counter = Counter()
        field_b: Counter = Counter()

        for raw, _status in rows:
            try:
                d = json.loads(raw)
                content = (d.get("choices") or [{}])[0].get("message", {}).get("content") or ""
            except (json.JSONDecodeError, TypeError, KeyError):
                empty += 1
                continue
            if not str(content).strip():
                empty += 1
                continue
            if "```" in content:
                fenced += 1
            obj = robust_json_object(content)
            if obj is None:
                continue
            parsed_n += 1
            if task == "SI":
                field_a[str(obj.get("safety_type"))] += 1
                field_b[str(obj.get("counseling_request"))] += 1
            elif task == "TR":
                field_a[str(obj.get("safety_type"))] += 1
                field_b[str(obj.get("therapy_request"))] += 1
            else:
                field_a[str(obj.get("therapy_engagement"))] += 1

        nonempty = n - empty
        lines.append(f"### {task} (`{pname}`) — n={n}")
        lines.append(f"- nonempty assistant: {nonempty}, empty: {empty}, fenced (when nonempty): {fenced}, robust JSON parsed: {parsed_n}")
        if task == "SI":
            lines.append("- `safety_type` counts:")
            for k, v in field_a.most_common():
                lines.append(f"  - `{k}`: {v}")
            lines.append("- `counseling_request` counts:")
            for k, v in field_b.most_common():
                lines.append(f"  - `{k}`: {v}")
        elif task == "TR":
            lines.append("- `safety_type` counts:")
            for k, v in field_a.most_common():
                lines.append(f"  - `{k}`: {v}")
            lines.append("- `therapy_request` counts:")
            for k, v in field_b.most_common():
                lines.append(f"  - `{k}`: {v}")
        else:
            lines.append("- `therapy_engagement` counts:")
            for k, v in field_a.most_common():
                lines.append(f"  - `{k}`: {v}")
        lines.append("")
    return "\n".join(lines)


def qwen_guard_block(conn: sqlite3.Connection, model_size: str) -> str:
    lines: List[str] = []
    lines.append(f"## `qwen_guard-{model_size}` (script output)")
    lines.append("")
    for task, pname in PROMPTS.items():
        rows = conn.execute(
            """
            SELECT cr.raw_response FROM cached_results cr
            JOIN cache_keys ck ON cr.cache_id = ck.cache_id
            WHERE ck.model_family = ? AND ck.model_size = ? AND ck.prompt_name = ?
            """,
            ("qwen_guard", model_size, pname),
        ).fetchall()
        n = len(rows)
        saf = Counter()
        cat = Counter()
        joint = Counter()
        for raw, in rows:
            try:
                c = json.loads(raw)["choices"][0]["message"]["content"] or ""
            except (json.JSONDecodeError, TypeError, KeyError):
                continue
            s, k = parse_qwen_lines(c)
            saf[s or "?"] += 1
            cat[k or "?"] += 1
            joint[(s, k)] += 1
        lines.append(f"### {task} — n={n}")
        lines.append("- `Safety:` counts:")
        for k, v in saf.most_common():
            lines.append(f"  - `{k}`: {v}")
        lines.append("- `Categories:` counts:")
        for k, v in cat.most_common():
            lines.append(f"  - `{k}`: {v}")
        lines.append("- top joint (Safety, Categories):")
        for (a, b), v in joint.most_common(15):
            lines.append(f"  - {v} × (`{a}`, `{b}`)")
        lines.append("")
    return "\n".join(lines)


def llama_guard_block(conn: sqlite3.Connection, model_size: str) -> str:
    lines: List[str] = []
    lines.append(f"## `llama_guard-{model_size}` (script output)")
    lines.append("")
    for task, pname in PROMPTS.items():
        rows = conn.execute(
            """
            SELECT cr.raw_response FROM cached_results cr
            JOIN cache_keys ck ON cr.cache_id = ck.cache_id
            WHERE ck.model_family = ? AND ck.model_size = ? AND ck.prompt_name = ?
            """,
            ("llama_guard", model_size, pname),
        ).fetchall()
        n = len(rows)
        first_ct: Counter = Counter()
        second_ct: Counter = Counter()
        full_ct: Counter = Counter()
        for raw, in rows:
            try:
                c = json.loads(raw)["choices"][0]["message"]["content"] or ""
            except (json.JSONDecodeError, TypeError, KeyError):
                continue
            full_ct[c.strip()] += 1
            f, s = parse_llama_guard_lines(c)
            first_ct[f] += 1
            if s:
                second_ct[s] += 1
        lines.append(f"### {task} — n={n}")
        lines.append("- first line:")
        for k, v in first_ct.most_common():
            lines.append(f"  - `{k}`: {v}")
        lines.append("- second line (when unsafe):")
        for k, v in second_ct.most_common():
            lines.append(f"  - `{k}`: {v}")
        lines.append("- full `content` strings:")
        for k, v in full_ct.most_common():
            lines.append(f"  - {v} × `{k}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--db",
        type=Path,
        default=_repo_root() / "cache" / "results.db",
        help="Path to results.db (default: <repo>/cache/results.db)",
    )
    p.add_argument(
        "--family",
        choices=("shieldgemma", "qwen_guard", "llama_guard", "all"),
        default="all",
        help="Which model family to aggregate",
    )
    p.add_argument(
        "--shieldgemma-sizes",
        default="27b,9b,2b",
        help="Comma-separated model_size for shieldgemma (default: 27b,9b,2b)",
    )
    p.add_argument(
        "--qwen-sizes",
        default="8b,4b,0.6b",
        help="Comma-separated model_size for qwen_guard (default: 8b,4b,0.6b)",
    )
    p.add_argument(
        "--llama-sizes",
        default="8b",
        help="Comma-separated model_size for llama_guard (default: 8b)",
    )
    args = p.parse_args()
    if not args.db.is_file():
        raise SystemExit(f"Database not found: {args.db}")

    conn = sqlite3.connect(str(args.db))

    if args.family in ("shieldgemma", "all"):
        for sz in [s.strip() for s in args.shieldgemma_sizes.split(",") if s.strip()]:
            print(shieldgemma_block(conn, sz))
            print()

    if args.family in ("qwen_guard", "all"):
        for sz in [s.strip() for s in args.qwen_sizes.split(",") if s.strip()]:
            print(qwen_guard_block(conn, sz))
            print()

    if args.family in ("llama_guard", "all"):
        for sz in [s.strip() for s in args.llama_sizes.split(",") if s.strip()]:
            print(llama_guard_block(conn, sz))
            print()

    conn.close()


if __name__ == "__main__":
    main()
