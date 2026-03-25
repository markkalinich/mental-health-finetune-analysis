"""Therapy engagement spreadsheets repeat one label per turn; review is per conversation."""

from __future__ import annotations


def dedupe_by_conversation(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    One row per conversation (Example_ID). P1/P2 are identical across turns in the
    intermediate file; evaluation should not be counted turn-by-turn.
    """
    seen: dict[str, dict[str, str]] = {}
    for r in rows:
        ex = (r.get("Example_ID") or "").strip()
        if ex and ex not in seen:
            seen[ex] = r
    return list(seen.values())
