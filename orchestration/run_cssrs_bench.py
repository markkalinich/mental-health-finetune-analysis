#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gaur et al. Reddit C-SSRS 5-class eval against psychiatrist gold standards.

Standalone from orchestration/run_experiment.py (no SI/TR/TE schema).
The model must emit one of the five published label strings. Scoring copies
jpsain/Suicide-Severity models/5-Label_Classification.py: graded precision,
recall, F1 (ordinal), and ordinal error (|rank difference| > 1). Parse failure
is not a class and counts as a miss. No JSON schema.
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))
from config import datasets  # noqa: E402

def extract_first_json_object(s: str) -> Optional[Dict[str, Any]]:
    """First top-level JSON object, or None. Local copy so this bench
    does not import utilities.schemas SI/TR/TE validation."""
    start_idx = s.find("{")
    if start_idx == -1:
        return None
    depth = 0
    for i in range(start_idx, len(s)):
        ch = s[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(s[start_idx:i + 1])
                except json.JSONDecodeError:
                    return None
    return None


CANONICAL_LABELS = ("Supportive", "Indicator", "Ideation", "Behavior", "Attempt")

# Map model variants onto the exact CSV strings. Comparison uses CANONICAL_LABELS.
_ALIASES = {
    "supportive": "Supportive",
    "su": "Supportive",
    "indicator": "Indicator",
    "indication": "Indicator",
    "in": "Indicator",
    "suicide indicator": "Indicator",
    "suicide indication": "Indicator",
    "ideation": "Ideation",
    "id": "Ideation",
    "suicide ideation": "Ideation",
    "suicidal ideation": "Ideation",
    "behavior": "Behavior",
    "behaviour": "Behavior",
    "br": "Behavior",
    "suicide behavior": "Behavior",
    "suicide behaviour": "Behavior",
    "suicidal behavior": "Behavior",
    "suicidal behaviour": "Behavior",
    "attempt": "Attempt",
    "at": "Attempt",
    "suicide attempt": "Attempt",
    "suicidal attempt": "Attempt",
    "actual attempt": "Attempt",
}

DEFAULT_PROMPT = Path("data/prompts/cssrs_severity_v1.txt")
LABEL_RANK = {lab: i for i, lab in enumerate(CANONICAL_LABELS)}


def canonical_label(raw: Optional[str]) -> Optional[str]:
    if raw is None:
        return None
    text = str(raw).strip().strip("\"'`")
    if not text:
        return None
    if text in CANONICAL_LABELS:
        return text
    return _ALIASES.get(text.lower())


_THINK_BLOCK = re.compile(r"<think>.*?</think>", re.IGNORECASE | re.DOTALL)


def strip_closed_think(content: str) -> str:
    """Drop a closed think wrapper before reading the label."""
    return _THINK_BLOCK.sub("", content).strip()


# ecorbari writes the class, a period, then a definition ("Attempt. It is ...").
# The first word is the class. A general "first word" rule is not used: other
# models start a line with "Supportive:" while repeating the rubric.
PSYCH_MERGED_MODEL = "ecorbari/Gemma-2b-it-Psych-Merged"
_LABEL_THEN_PERIOD = re.compile(r"^[\"'`*]*([A-Za-z]+)\.")


def parse_predicted_label(content: str, model_id: str = "") -> Tuple[Optional[str], str]:
    """Return (canonical_label, parse_status)."""
    if not content or not str(content).strip():
        return None, "parse_fail:empty"
    text = strip_closed_think(str(content))
    if not text:
        return None, "parse_fail:empty"

    obj = extract_first_json_object(text)
    if isinstance(obj, dict):
        for key in ("label", "class", "severity", "standard_label"):
            if key in obj:
                lab = canonical_label(obj.get(key))
                if lab:
                    return lab, "ok"
                return None, "parse_fail:json_unknown_label"

    first_line = text.splitlines()[0].strip()
    lab = canonical_label(first_line.strip("\"'`.,;"))
    if lab:
        return lab, "ok"
    lab = canonical_label(text.strip())
    if lab:
        return lab, "ok"
    if model_id == PSYCH_MERGED_MODEL:
        match = _LABEL_THEN_PERIOD.match(first_line.strip())
        if match:
            lab = canonical_label(match.group(1))
            if lab:
                return lab, "ok"
    return None, "parse_fail:no_label"


def row_standard_label(row: Dict[str, str]) -> str:
    return (row.get("standard_label") or row.get("gold_label") or "").strip()


def load_standard(path: Path) -> List[Dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(
            f"prepared gold-standard CSV not found: {path} "
            "(run orchestration.prepare_cssrs_gold)"
        )
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or not {"item_id", "text"}.issubset(rows[0].keys()):
        raise ValueError(f"{path} must have columns item_id,text,standard_label")
    out = []
    for row in rows:
        lab = row_standard_label(row)
        row = dict(row)
        row["standard_label"] = lab
        out.append(row)
    empty = sum(1 for r in out if not (r.get("text") or "").strip())
    if empty:
        raise SystemExit(
            f"STOP: {empty}/{len(out)} gold-standard rows have empty text. "
            "Do not scrape Reddit; the Zenodo file must already contain posts."
        )
    bad = sorted({r["standard_label"] for r in out} - set(CANONICAL_LABELS))
    if bad:
        raise ValueError(f"unexpected gold-standard labels: {bad}")
    return out


def _safe_div(n: float, d: float) -> float:
    return n / d if d else 0.0


def score_labels(standard: Sequence[str], pred: Sequence[Optional[str]]) -> Dict[str, Any]:
    """Paper/GitHub metrics from jpsain 5-Label_Classification.get_prf1_score.

    Graded: pred rank > standard rank is FP; pred rank < standard rank is FN;
    exact rank match is TP. Ordinal error: |rank difference| > 1.
    Unparseable output is a miss (FN and OE), not a class.
    """
    if len(standard) != len(pred):
        raise ValueError("standard/pred length mismatch")
    n = len(standard)
    parsed = sum(1 for p in pred if p is not None)
    exact = sum(1 for s, p in zip(standard, pred) if p is not None and p == s)

    graded_tp = graded_fp = graded_fn = 0
    oe_n = 0
    for s, p in zip(standard, pred):
        rs = LABEL_RANK[s]
        if p is None or p not in LABEL_RANK:
            graded_fn += 1
            oe_n += 1
            continue
        rp = LABEL_RANK[p]
        if rp == rs:
            graded_tp += 1
        elif rp > rs:
            graded_fp += 1
        else:
            graded_fn += 1
        if abs(rp - rs) > 1:
            oe_n += 1

    graded_p = _safe_div(graded_tp, graded_tp + graded_fp)
    graded_r = _safe_div(graded_tp, graded_tp + graded_fn)
    graded_f = _safe_div(2 * graded_p * graded_r, graded_p + graded_r)

    per_class: Dict[str, Dict[str, float]] = {}
    f1s = []
    weighted_num = 0.0
    for lab in CANONICAL_LABELS:
        support = sum(1 for s in standard if s == lab)
        tp = sum(1 for s, p in zip(standard, pred) if s == lab and p == lab)
        fp = sum(1 for s, p in zip(standard, pred) if s != lab and p == lab)
        fn = sum(1 for s, p in zip(standard, pred) if s == lab and p != lab)
        prec = _safe_div(tp, tp + fp)
        rec = _safe_div(tp, tp + fn)
        f1 = _safe_div(2 * prec * rec, prec + rec) if (prec + rec) else 0.0
        per_class[lab] = {
            "support": support,
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "precision": prec,
            "recall": rec,
            "f1": f1,
        }
        f1s.append(f1)
        weighted_num += f1 * support

    return {
        "n": n,
        "parsed": parsed,
        "parse_fail": n - parsed,
        "graded_precision": graded_p,
        "graded_recall": graded_r,
        "graded_f1": graded_f,
        "ordinal_error": _safe_div(oe_n, n),
        "accuracy": _safe_div(exact, n),
        "macro_f1": _safe_div(sum(f1s), len(CANONICAL_LABELS)),
        "weighted_f1": _safe_div(weighted_num, n),
        "per_class": per_class,
        "pred_counts": dict(Counter(p if p is not None else "parse_fail" for p in pred)),
        "standard_counts": {lab: sum(1 for s in standard if s == lab) for lab in CANONICAL_LABELS},
        "scoring": (
            "jpsain/Suicide-Severity 5-Label_Classification.get_prf1_score "
            "(graded P/R/F) plus paper ordinal error |Δrank|>1"
        ),
    }


async def _classify_one(
    client: ChatCompletionsClient,
    system_prompt: str,
    text: str,
    semaphore: asyncio.Semaphore,
    model_id: str = "",
) -> Tuple[Dict[str, Any], str, str, Optional[str], float]:
    async with semaphore:
        started = time.perf_counter()
        try:
            raw = await client.call_chat_completion_async(system_prompt, text)
            content = client.extract_content(raw) or ""
            pred, status = parse_predicted_label(content, model_id)
            return raw, content, status, pred, time.perf_counter() - started
        except Exception as exc:
            # ChatAPIError is imported only when the client is constructed.
            return {"error": str(exc)}, "", f"api_error:{exc}", None, time.perf_counter() - started


def predictions_jsonl_path(output_dir: Path) -> Path:
    return output_dir / "predictions.jsonl"


def load_completed(output_dir: Path, model_id: str = "") -> Dict[str, Tuple[str, str, Optional[str]]]:
    """item_id -> (raw_response, status, pred_label) from a prior partial run.

    A row whose stored status starts with ``api_error`` is not a finished
    item. The client writes ``raw_response`` as ``''`` on those rows, and
    reparsing that string would mark the item done as ``parse_fail:empty``
    without calling the server again. A later success for the same item_id
    still counts.
    """
    path = predictions_jsonl_path(output_dir)
    if not path.is_file():
        return {}
    done: Dict[str, Tuple[str, str, Optional[str]]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            item_id = str(row.get("item_id") or "")
            if not item_id:
                continue
            stored = str(row.get("status") or "")
            if stored.startswith("api_error"):
                done.pop(item_id, None)
                continue
            content = str(row.get("raw_response") or "")
            pred, status = parse_predicted_label(content, model_id)
            done[item_id] = (content, status, pred)
    return done


def append_prediction(output_dir: Path, item: Dict[str, str], content: str, status: str, pred: Optional[str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = predictions_jsonl_path(output_dir)
    row = {
        "item_id": item["item_id"],
        "standard_label": item["standard_label"],
        "pred_label": pred or "",
        "status": status,
        "raw_response": content,
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        handle.flush()


async def classify_all(
    client: ChatCompletionsClient,
    system_prompt: str,
    items: Sequence[Dict[str, str]],
    max_concurrent: int,
    cache: Any,
    config: Any,
    model_id: str = "",
) -> List[Tuple[str, str, Optional[str]]]:
    sem = asyncio.Semaphore(max(1, max_concurrent))
    write_lock = asyncio.Lock()
    total = len(items)
    done = 0

    async def one(item: Dict[str, str]) -> Tuple[str, str, Optional[str]]:
        nonlocal done
        raw, content, status, pred, elapsed = await _classify_one(
            client, system_prompt, item["text"], sem, model_id
        )
        async with write_lock:
            cache.store_result(
                config, item["text"], system_prompt, raw,
                {"pred_label": pred} if pred else None,
                status, elapsed, 0,
            )
        done += 1
        if done % 50 == 0 or done == total:
            print(f"Progress: {done}/{total} ({100.0 * done / total:.1f}%)", flush=True)
        return content, status, pred

    print(f"Processing {total} users with up to {max_concurrent} concurrent connections...")
    return list(await asyncio.gather(*[one(item) for item in items]))


def write_outputs(
    output_dir: Path,
    items: Sequence[Dict[str, str]],
    results: Sequence[Tuple[str, str, Optional[str]]],
    metrics: Dict[str, Any],
    meta: Dict[str, Any],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pred_path = output_dir / "predictions.csv"
    with pred_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["item_id", "standard_label", "pred_label", "status", "raw_response"],
        )
        writer.writeheader()
        for item, (content, status, pred) in zip(items, results):
            writer.writerow({
                "item_id": item["item_id"],
                "standard_label": item["standard_label"],
                "pred_label": pred or "",
                "status": status,
                "raw_response": content,
            })
    payload = {
        "benchmark": "reddit_cssrs_gaur2019",
        "label_set": list(CANONICAL_LABELS),
        "scoring": metrics.get("scoring"),
        "metrics": metrics,
        **meta,
    }
    (output_dir / "metrics.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"predictions {pred_path}")
    print(f"metrics {output_dir / 'metrics.json'}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Reddit C-SSRS 5-class bench vs psychiatrist gold standards (Gaur/jpsain)."
    )
    parser.add_argument("--input", type=Path, default=None,
                        help="Prepared gold-standard CSV (default: cssrs_users in config/datasets.csv)")
    parser.add_argument("--system", type=Path, default=DEFAULT_PROMPT, help="Classifier prompt")
    parser.add_argument("--base-url", default="", help="OpenAI-compatible base, e.g. http://127.0.0.1:8010/v1")
    parser.add_argument("--model-name", default="", help="Served model id for /v1/chat/completions")
    parser.add_argument(
        "--model-family",
        default="",
        help="Cache key family. Default: qwen if the id contains qwen, otherwise other.",
    )
    parser.add_argument("--model-size", default="", help="Cache key size. Default: the model id with '/' replaced by '__'.")
    parser.add_argument("--model-version", default="20261007", help="Cache key version. Same value the ideation runs use.")
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--max-concurrent", type=int, default=128)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=128)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--limit", type=int, default=0, help="Score only the first N items (smoke)")
    parser.add_argument("--dry-run", action="store_true", help="Load gold standards, print counts, exit")
    args = parser.parse_args()
    if args.input is None:
        args.input = datasets.path("cssrs_users")

    items = load_standard(args.input)
    if args.limit and args.limit > 0:
        from orchestration.pilot_sample import stratified_take
        items = stratified_take(items, lambda row: row.get("standard_label"), args.limit, seed=0)

    standard_counts = Counter(r["standard_label"] for r in items)
    print(f"loaded n={len(items)} from {args.input}")
    print("label_set", ",".join(CANONICAL_LABELS))
    for lab in CANONICAL_LABELS:
        print(f"count\t{lab}\t{standard_counts[lab]}")

    if args.dry_run:
        return 0
    if not args.base_url or not args.model_name:
        parser.error("--base-url and --model-name are required unless --dry-run")

    from types import SimpleNamespace

    from orchestration.api_client import ChatCompletionsClient

    if not args.system.is_file():
        raise FileNotFoundError(f"prompt not found: {args.system}")
    from config.utils import apply_model_prompt_suffix, qwen_chat_template_kwargs
    system_prompt = apply_model_prompt_suffix(
        args.system.read_text(encoding="utf-8").strip(),
        SimpleNamespace(family=args.model_family, full_name=args.model_name),
    )

    safe_model = args.model_name.replace("/", "__")
    output_dir = args.output_dir or Path("replies/cssrs") / safe_model
    family = args.model_family or ("qwen" if "qwen" in args.model_name.lower() else "other")
    size = args.model_size or safe_model

    from cache.result_cache import ResultCache
    from orchestration.experiment_manager import ExperimentManager

    eval_config = SimpleNamespace(
        base_url=args.base_url,
        model=args.model_name,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=1.0,
        request_timeout=args.timeout,
        chat_template_kwargs=qwen_chat_template_kwargs(
            family, model_id=args.model_name
        ),
    )
    cache = ResultCache()
    config = ExperimentManager(Path(".")).create_experiment_config(
        experiment_name=f"cssrs_{size}",
        model_family=family,
        model_size=size,
        model_version=args.model_version,
        prompt_name=args.system.stem,
        prompt_file=str(args.system),
        input_dataset=str(args.input),
        model_name=args.model_name,
        base_url=args.base_url,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=1.0,
        request_timeout=args.timeout,
    )
    client = ChatCompletionsClient(eval_config)
    completed: Dict[str, Tuple[str, str, Optional[str]]] = {}
    pending = []
    for item in items:
        existing, _missing = cache.check_cache(
            config, item["text"], system_prompt, num_replicates=1, include_errors=False
        )
        hit = next((row for row in existing if row.replicate_index == 0), None)
        if hit is None:
            pending.append(item)
            continue
        content = client.extract_content(hit.raw_response) or ""
        pred, status = parse_predicted_label(content, args.model_name)
        completed[item["item_id"]] = (content, status, pred)
    print(f"cache_hits {len(completed)} pending {len(pending)} dir={output_dir}")

    t0 = time.time()
    new_results: List[Tuple[str, str, Optional[str]]] = []
    if pending:
        print(f"Warming up {args.model_name} at {args.base_url}")
        client.warmup_model(max_retries=5, retry_delay=3.0)
        new_results = asyncio.run(
            classify_all(
                client, system_prompt, pending, args.max_concurrent, cache, config, args.model_name
            )
        )
    elapsed = time.time() - t0

    new_by_id = {item["item_id"]: res for item, res in zip(pending, new_results)}
    results = [completed.get(item["item_id"]) or new_by_id[item["item_id"]] for item in items]

    standard = [r["standard_label"] for r in items]
    pred = [p for _c, _s, p in results]
    metrics = score_labels(standard, pred)
    print(
        f"graded_p={metrics['graded_precision']:.4f} "
        f"graded_r={metrics['graded_recall']:.4f} "
        f"graded_f1={metrics['graded_f1']:.4f} "
        f"ordinal_error={metrics['ordinal_error']:.4f} "
        f"parse_fail={metrics['parse_fail']}/{metrics['n']}"
    )

    meta = {
        "model_name": args.model_name,
        "base_url": args.base_url,
        "input": str(args.input),
        "prompt": str(args.system),
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "n_scored": len(items),
        "elapsed_seconds": elapsed,
    }
    write_outputs(output_dir, items, results, metrics, meta)
    return 0


if __name__ == "__main__":
    sys.exit(main())
