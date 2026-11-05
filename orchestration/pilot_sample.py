"""Deterministic stratified subsample for overnight / smoke runs.

First-N is unsafe on these files: SI is grouped by Safety type, AnnoMI is
grouped by transcript, C-SSRS is not balanced in file order. Round-robin
across the gold-standard column so every label appears when n is large enough.
"""

from __future__ import annotations

import random
from collections import defaultdict
from typing import Any, Callable, List, Sequence, TypeVar

T = TypeVar("T")


def stratified_indices(keys: Sequence[Any], n: int, seed: int = 0) -> List[int]:
    if n <= 0 or n >= len(keys):
        return list(range(len(keys)))
    buckets = defaultdict(list)
    for idx, key in enumerate(keys):
        buckets[key].append(idx)
    rng = random.Random(seed)
    for key in buckets:
        rng.shuffle(buckets[key])
    chosen: List[int] = []
    labels = sorted(buckets, key=lambda k: str(k))
    while len(chosen) < n:
        progressed = False
        for lab in labels:
            if not buckets[lab]:
                continue
            chosen.append(buckets[lab].pop())
            progressed = True
            if len(chosen) >= n:
                break
        if not progressed:
            break
    chosen.sort()
    return chosen


def stratified_take(
    items: Sequence[T],
    key_fn: Callable[[T], Any],
    n: int,
    seed: int = 0,
) -> List[T]:
    idx = stratified_indices([key_fn(item) for item in items], n, seed)
    return [items[i] for i in idx]


def item_gold_key(item: dict, field: str) -> str:
    raw = item.get(field)
    if isinstance(raw, (list, tuple)):
        return str(raw[0]) if raw else ""
    return str(raw or "")


def dataframe_stratified_take(df, column: str, n: int, seed: int = 0):
    idx = stratified_indices(list(df[column]), n, seed)
    return df.iloc[idx].copy()
