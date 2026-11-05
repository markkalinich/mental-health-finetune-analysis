#!/usr/bin/env python3
"""Yes/no C-SSRS run for the 500 Reddit users.

The default prompt is data/prompts/cssrs_yesno_v1.txt; the study runs pass
cssrs_yesno_v5.txt with its prefix and suffix (e.g. bash_scripts/run_pretrained_bases.sh). Gold yes is Ideation, Behavior,
or Attempt. Supportive and Indicator are no. The reply is parsed as yes or no
with the same one-word rule as synthetic suicidal ideation.

An unparsed reply stays in the denominator. It is a false negative when the
gold label is yes, and a false positive when the gold label is no.

Writes <--output-dir>/<model>/ (the study runs use replies/cssrs-yesno-v5) and does not touch replies/cssrs/.
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))
from config import datasets  # noqa: E402

from config.utils import apply_model_prompt_suffix, qwen_chat_template_kwargs
from orchestration.api_client import ChatCompletionsClient
from orchestration.run_cssrs_bench import load_standard
from safety_labels.score import CSSRS_NO, CSSRS_YES
from utilities.schemas import parse_one_word

PROMPT = REPO / "data/prompts/cssrs_yesno_v1.txt"
PROMPT_NAME = "cssrs_yesno_v1"


def gold_yes(label: str) -> bool:
    if label in CSSRS_YES:
        return True
    if label in CSSRS_NO:
        return False
    raise SystemExit(f"unexpected C-SSRS gold {label!r}")


def context_overflow(status: str) -> bool:
    """The joined posts plus the reply do not fit in this model's context."""
    return status.startswith("api_error") and "maximum context length" in status


def parse_yes(content: str) -> Optional[bool]:
    parsed = parse_one_word(content, "suicidal_ideation", PROMPT_NAME)
    if not parsed:
        return None
    label = parsed.get("safety_type")
    if label == "yes":
        return True
    if label == "no":
        return False
    return None


def binary_counts(pairs: list[tuple[bool, Optional[bool]]]) -> dict:
    tp = tn = fp = fn = 0
    for gold, pred in pairs:
        if gold:
            if pred is True:
                tp += 1
            else:
                fn += 1
        elif pred is False:
            tn += 1
        else:
            fp += 1
    sens = tp / (tp + fn) if tp + fn else 0.0
    spec = tn / (tn + fp) if tn + fp else 0.0
    precision = tp / (tp + fp) if tp + fp else 0.0
    f1 = 0.0 if precision + sens == 0 else 2 * precision * sens / (precision + sens)
    return {
        "n": len(pairs),
        "parsed": sum(pred is not None for _gold, pred in pairs),
        "parse_fail": sum(pred is None for _gold, pred in pairs),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "sensitivity": sens,
        "specificity": spec,
        "precision": precision,
        "f1": f1,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Yes/no C-SSRS against the Gaur user labels.")
    parser.add_argument("--input", type=Path, default=None, help="default: cssrs_users in config/datasets.csv")
    parser.add_argument("--system", type=Path, default=PROMPT)
    parser.add_argument(
        "--user-prefix",
        default="",
        help="Text placed before each user's posts. v4 uses this to say the posts follow.",
    )
    parser.add_argument(
        "--user-suffix",
        default="",
        help="Text appended after each user's posts. v4 uses this for the decision line.",
    )
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--model-family", default="")
    parser.add_argument("--model-size", default="")
    parser.add_argument("--model-version", default="20261007")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-concurrent", type=int, default=128)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=256)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    if args.input is None:
        args.input = datasets.path("cssrs_users")

    if not args.system.is_file():
        raise SystemExit(f"prompt not found: {args.system}")
    items = load_standard(args.input)
    if args.limit and args.limit > 0:
        from orchestration.pilot_sample import stratified_take
        items = stratified_take(items, lambda row: row.get("standard_label"), args.limit, seed=0)
    if len(items) != 500 and not args.limit:
        raise SystemExit(f"expected 500 users, got {len(items)} from {args.input}")

    from cache.result_cache import ResultCache
    from orchestration.experiment_manager import ExperimentManager

    prefix = args.user_prefix.strip()
    suffix = args.user_suffix.strip()

    def user_text(item: dict) -> str:
        text = item["text"]
        if not prefix and not suffix:
            return text
        chunks = []
        if prefix:
            chunks.append(prefix)
        chunks.append(text.rstrip())
        if suffix:
            chunks.append(suffix)
        return "\n\n".join(chunks)

    family = args.model_family or ("qwen" if "qwen" in args.model_name.lower() else "other")
    size = args.model_size or args.model_name.replace("/", "__")
    system_prompt = apply_model_prompt_suffix(
        args.system.read_text(encoding="utf-8").strip(),
        SimpleNamespace(family=family, full_name=args.model_name),
    )
    eval_config = SimpleNamespace(
        base_url=args.base_url,
        model=args.model_name,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=1.0,
        request_timeout=args.timeout,
        chat_template_kwargs=qwen_chat_template_kwargs(family, model_id=args.model_name),
    )
    cache = ResultCache()
    config = ExperimentManager(REPO).create_experiment_config(
        experiment_name=f"cssrs_yesno_{size}",
        model_family=family,
        model_size=size,
        model_version=args.model_version,
        prompt_name=PROMPT_NAME,
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
    done: dict[str, tuple[str, str, Optional[bool]]] = {}
    pending = []
    for item in items:
        existing, _missing = cache.check_cache(
            config, user_text(item), system_prompt, num_replicates=1, include_errors=True
        )
        hit = next((row for row in existing if row.replicate_index == 0), None)
        if hit is None:
            pending.append(item)
            continue
        if context_overflow(hit.status):
            done[item["item_id"]] = ("", hit.status, None)
            continue
        if hit.status.startswith("api_error"):
            pending.append(item)
            continue
        content = client.extract_content(hit.raw_response) or ""
        pred = parse_yes(content)
        status = "ok" if pred is not None else "parse_fail"
        done[item["item_id"]] = (content, status, pred)
    print(f"cache_hits {len(done)} pending {len(pending)} dir={args.output_dir}", flush=True)

    fresh: dict[str, tuple[str, str, Optional[bool]]] = {}
    if pending:
        client.warmup_model(max_retries=5, retry_delay=3.0)
        fresh = asyncio.run(
            _classify_all(client, system_prompt, pending, args.max_concurrent, cache, config, user_text)
        )

    rows_out = []
    pairs = []
    for item in items:
        content, status, pred = done.get(item["item_id"]) or fresh[item["item_id"]]
        yes = gold_yes(item["standard_label"])
        pairs.append((yes, pred))
        rows_out.append({
            "item_id": item["item_id"],
            "standard_label": item["standard_label"],
            "gold_yes": "yes" if yes else "no",
            "pred_yes": "" if pred is None else ("yes" if pred else "no"),
            "status": status,
            "raw_response": content,
        })
    api_errors = [
        row["status"] for row in rows_out
        if row["status"].startswith("api_error") and not context_overflow(row["status"])
    ]
    if api_errors:
        raise SystemExit(
            f"{len(api_errors)} API errors are not context overflow; not writing metrics"
        )
    counts = binary_counts(pairs)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pred_path = args.output_dir / "predictions.csv"
    with pred_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows_out[0]))
        writer.writeheader()
        writer.writerows(rows_out)
    payload = {
        "benchmark": "reddit_cssrs_yesno",
        "prompt": str(args.system),
        "user_prefix": prefix,
        "user_suffix": suffix,
        "model_name": args.model_name,
        "gold_yes": list(CSSRS_YES),
        "gold_no": list(CSSRS_NO),
        "unparsed": "false negative when gold is yes; false positive when gold is no",
        "metrics": counts,
    }
    (args.output_dir / "metrics.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        f"parsed={counts['parsed']}/{counts['n']} "
        f"sens={counts['sensitivity']:.4f} spec={counts['specificity']:.4f} f1={counts['f1']:.4f}",
        flush=True,
    )
    print(f"predictions {pred_path}")
    return 0


async def _classify_all(client, system_prompt, items, max_concurrent, cache, config, user_text):
    sem = asyncio.Semaphore(max(1, max_concurrent))
    total = len(items)
    finished = 0
    write_lock = asyncio.Lock()

    async def one(item):
        nonlocal finished
        async with sem:
            started = time.perf_counter()
            try:
                raw = await client.call_chat_completion_async(system_prompt, user_text(item))
                content = client.extract_content(raw) or ""
                pred = parse_yes(content)
                status = "ok" if pred is not None else "parse_fail"
            except Exception as exc:
                raw = {"error": str(exc)}
                content = ""
                pred = None
                status = f"api_error:{exc}"
            elapsed = time.perf_counter() - started
        async with write_lock:
            cache.store_result(
                config,
                user_text(item),
                system_prompt,
                raw,
                {"safety_type": "yes" if pred else "no"} if pred is not None else None,
                status,
                elapsed,
                0,
            )
        finished += 1
        if finished % 50 == 0 or finished == total:
            print(f"Progress: {finished}/{total}", flush=True)
        return item["item_id"], (content, status, pred)

    pairs = await asyncio.gather(*[one(item) for item in items])
    return dict(pairs)


if __name__ == "__main__":
    sys.exit(main())
