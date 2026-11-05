"""Flatten the agents' per-model extraction JSON (agents/PROMPT-extract.md) into the files the study reads.

    .venv/bin/python model_selection/collect_extractions.py \
        --grouping mental-health \
        --inputs docs/mental_health_FT_funnel/agent-searches/2026-10-09-extraction-kept42/extractions \
        --decided-on 2026-10-09

Writes, for the current view (outputs/funnel/<grouping>/<CURRENT>/):
  extractions.csv        one row per model, the scalar fields of the JSON (supplementary table)
  agent_fields.csv       the summary the methods note quotes (objective named, dataset named, both)
  card_review_agent.csv  output_type, use_claim, warning with quotes, same columns as the hand card review
and appends or replaces rows in model_selection/agent_methods.csv (the funnel's
step-5 input: grouping, hf_id, decided_on, objective, update_scope, source_url, source).

Stops with a non-zero exit when a step-4 survivor (kept_after_review.csv) has no JSON, when a JSON names a model that is not in
kept_after_review.csv (listed, not fatal), when a JSON does not parse, or when a required field is missing.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cache  # noqa: E402

REPO = HERE.parent
AGENT_METHODS = HERE / "agent_methods.csv"
AM_FIELDS = ["grouping", "hf_id", "decided_on", "objective", "update_scope", "source_url", "source"]
NOT_STATED = {"", "not stated", "none", "null"}

EXTRACT_FIELDS = [
    "hf_id", "prompt_version", "card_cached_file", "card_cached_sha256", "card_current_differs",
    "github", "paper_urls", "paper_names_this_repo",
    "data_names", "data_hub_ids", "data_urls", "data_loads", "data_n_examples", "data_language", "data_provenance",
    "objective", "objective_url", "update_scope", "update_scope_url", "lora_rank", "lora_alpha", "adapter_merged",
    "quantized_base_during_training", "epochs", "steps", "learning_rate", "batch_size",
    "parent_card_claim", "parent_source_claims", "parent_sources_agree",
    "parameters_stated", "languages", "output_type", "use_claim", "warning",
    "input_kind", "output_kind", "detection_claim_kind", "detection_claim_categories", "detection_claim_quote", "detection_claim_url",
    "text_only_input", "chat_template_present", "system_prompt", "generation_settings", "max_context",
    "evaluation_reported", "license", "matches_inventory", "discrepancies", "confidence", "pages_read", "json_file",
]
REVIEW_FIELDS = ["hf_id", "output_type", "use_claim", "claim_quote", "warning_strength", "warning_quote",
                 "input_kind", "output_kind", "detection_claim_kind", "detection_claim_categories", "detection_claim_quote", "card_file"]
FIELDS_OUT = ["hf_id", "named_objective", "objective", "objective_from", "dataset_named", "dataset",
              "update_scope", "update_scope_known", "both", "source_url", "writeup"]


def fail(msg: str, items=()) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    for it in items:
        print(f"  - {it}", file=sys.stderr)
    sys.exit(2)


def s(v) -> str:
    if v is None:
        return ""
    if isinstance(v, (list, dict)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def pipe(items, key=None) -> str:
    out = []
    for it in items or []:
        v = it.get(key) if (key and isinstance(it, dict)) else it
        if isinstance(v, list):
            out.extend(str(x) for x in v if x)
        elif v not in (None, "", "not stated"):
            out.append(str(v))
    return " | ".join(out)


def flatten(d: dict, path: Path) -> dict:
    tm, par, card, links, ser = d["training_method"], d["parent"], d["card"], d["links"], d["serving"]
    data = d.get("training_data") or []
    papers = [p for p in (links.get("papers") or []) if isinstance(p, dict) and (p.get("url") or "") not in ("", "not stated")]
    return {
        "hf_id": d["hf_id"], "prompt_version": d.get("prompt_version"),
        "card_cached_file": card.get("cached_file"), "card_cached_sha256": card.get("cached_sha256"),
        "card_current_differs": card.get("current_differs"),
        "github": pipe(links.get("github")), "paper_urls": pipe(papers, "url"),
        "paper_names_this_repo": pipe([str(p.get("names_this_repo")) for p in papers]),
        "data_names": pipe(data, "name"), "data_hub_ids": pipe(data, "hub_id"), "data_urls": pipe(data, "urls"),
        "data_loads": pipe([str(x.get("loads")) for x in data]), "data_n_examples": pipe([s(x.get("n_examples")) for x in data]),
        "data_language": pipe(data, "language"), "data_provenance": pipe(data, "provenance"),
        "objective": tm.get("objective"), "objective_url": tm.get("objective_url"),
        "update_scope": tm.get("update_scope"), "update_scope_url": tm.get("update_scope_url"),
        "lora_rank": tm.get("lora_rank"), "lora_alpha": tm.get("lora_alpha"), "adapter_merged": tm.get("adapter_merged"),
        "quantized_base_during_training": tm.get("quantized_base_during_training"),
        "epochs": tm.get("epochs"), "steps": tm.get("steps"), "learning_rate": tm.get("learning_rate"), "batch_size": tm.get("batch_size"),
        "parent_card_claim": par.get("card_claim"), "parent_source_claims": pipe(par.get("source_claims"), "parent"),
        "parent_sources_agree": par.get("sources_agree_with_card"),
        "parameters_stated": (d.get("size") or {}).get("parameters_stated"),
        "languages": pipe((d.get("languages") or {}).get("values")),
        "output_type": (d.get("output_type") or {}).get("value"), "use_claim": (d.get("use_claim") or {}).get("strength"),
        "warning": (d.get("warning") or {}).get("strength"),
        # prompt v4 (safety, 9 Oct 2026): input kind, output kind, detection claim replace the two mental-health scales
        "input_kind": pipe((d.get("input_kind") or {}).get("values")), "output_kind": pipe((d.get("output_kind") or {}).get("values")),
        "detection_claim_kind": (d.get("detection_claim") or {}).get("kind"),
        "detection_claim_categories": pipe((d.get("detection_claim") or {}).get("categories")),
        "detection_claim_quote": (d.get("detection_claim") or {}).get("quote"), "detection_claim_url": (d.get("detection_claim") or {}).get("source_url"),
        "text_only_input": ser.get("text_only_input"), "chat_template_present": ser.get("chat_template_present"),
        "system_prompt": ser.get("system_prompt"), "generation_settings": s(ser.get("generation_settings")),
        "max_context": ser.get("max_context"),
        "evaluation_reported": (d.get("evaluation_reported") or {}).get("text"), "license": (d.get("license") or {}).get("value"),
        "matches_inventory": d.get("matches_inventory"), "discrepancies": d.get("discrepancies"),
        "confidence": d.get("confidence"), "pages_read": pipe(d.get("pages_read")),
        "json_file": str(path.relative_to(REPO)) if path.is_relative_to(REPO) else str(path),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--grouping", default="mental-health")
    ap.add_argument("--inputs", required=True, help="folder of <org>__<name>.json files")
    ap.add_argument("--decided-on", required=True, help="date written into agent_methods.csv rows")
    ap.add_argument("--allow-missing", action="store_true", help="write what exists even if kept models lack a JSON")
    args = ap.parse_args()

    current = cache.current_dir(args.grouping)
    # The models that reach manual review (step 4) are the ones extracted; kept.csv is the endpoint list
    # (step 6 since 10 Oct 2026) and would skip the step-5 survivors that still lack an objective-evidence row.
    kept = [r["hf_id"] for r in csv.DictReader((current / "kept_after_review.csv").open(newline=""))]
    kept_lower = {k.lower(): k for k in kept}
    folder = Path(args.inputs)
    if not folder.is_absolute():
        folder = REPO / folder

    rows, extra, bad = {}, [], []
    for p in sorted(folder.glob("*.json")):
        try:
            d = json.load(p.open(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            bad.append(f"{p.name}: {e}")
            continue
        hf = (d.get("hf_id") or "").strip()
        if hf.lower() not in kept_lower:
            extra.append(f"{hf} ({p.name})")
            continue
        try:
            rows[hf.lower()] = (flatten(d, p), d, p)
        except KeyError as e:
            bad.append(f"{p.name}: missing block {e}")
    if bad:
        fail("unreadable extraction JSON", bad)
    if extra:
        print(f"note: {len(extra)} JSON file(s) name models not in kept.csv and were skipped:", file=sys.stderr)
        for e in extra:
            print(f"  - {e}", file=sys.stderr)
    missing = [k for k in kept if k.lower() not in rows]
    if missing and not args.allow_missing:
        fail(f"{len(missing)} kept model(s) have no extraction JSON in {folder}", missing)
    if missing:
        print(f"note: {len(missing)} kept model(s) without JSON (--allow-missing): {missing}", file=sys.stderr)

    ordered = [rows[k.lower()] for k in kept if k.lower() in rows]
    with (current / "extractions.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=EXTRACT_FIELDS)
        w.writeheader()
        for flat, _d, _p in ordered:
            w.writerow({k: s(flat.get(k)) for k in EXTRACT_FIELDS})

    with (current / "card_review_agent.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=REVIEW_FIELDS)
        w.writeheader()
        for flat, d, _p in ordered:
            uc, wn = d.get("use_claim") or {}, d.get("warning") or {}   # absent in v4 records
            w.writerow({"hf_id": d["hf_id"], "output_type": (d.get("output_type") or {}).get("value", ""),
                        "use_claim": uc.get("strength", ""), "claim_quote": uc.get("quote", ""),
                        "warning_strength": wn.get("strength", ""), "warning_quote": wn.get("quote", ""),
                        "input_kind": flat["input_kind"], "output_kind": flat["output_kind"], "detection_claim_kind": flat["detection_claim_kind"],
                        "detection_claim_categories": flat["detection_claim_categories"], "detection_claim_quote": flat["detection_claim_quote"],
                        "card_file": d["card"].get("cached_file", "")})

    n_obj = n_data = n_both = 0
    with (current / "agent_fields.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS_OUT)
        w.writeheader()
        for flat, d, p in ordered:
            obj = (flat["objective"] or "").strip().lower()
            scope = (flat["update_scope"] or "").strip().lower()
            named = obj not in NOT_STATED
            dataset_named = bool((flat["data_names"] or "").strip())
            n_obj += named; n_data += dataset_named; n_both += named and dataset_named
            w.writerow({"hf_id": d["hf_id"], "named_objective": "yes" if named else "no", "objective": obj or "not stated",
                        "objective_from": flat["objective_url"] or "", "dataset_named": "yes" if dataset_named else "no",
                        "dataset": flat["data_names"], "update_scope": scope or "not stated",
                        "update_scope_known": "yes" if scope not in NOT_STATED else "no",
                        "both": "yes" if named and dataset_named else "no", "source_url": flat["objective_url"] or flat["update_scope_url"] or "",
                        "writeup": flat["json_file"]})

    # agent_methods.csv: replace this grouping's rows for the models we have; keep everything else.
    existing = list(csv.DictReader(AGENT_METHODS.open(newline=""))) if AGENT_METHODS.exists() else []
    have = {d["hf_id"].lower() for _f, d, _p in ordered}
    keep_rows = [r for r in existing if not (r["grouping"] == args.grouping and r["hf_id"].lower() in have)]
    for flat, d, p in ordered:
        keep_rows.append({"grouping": args.grouping, "hf_id": d["hf_id"], "decided_on": args.decided_on,
                          "objective": (flat["objective"] or "not stated"), "update_scope": (flat["update_scope"] or "not stated"),
                          "source_url": flat["objective_url"] or flat["update_scope_url"] or "",
                          "source": f"PROMPT-extract v{d.get('prompt_version')}; {flat['json_file']}"})
    with AGENT_METHODS.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=AM_FIELDS)
        w.writeheader()
        w.writerows(keep_rows)

    print(f"wrote {current / 'extractions.csv'}, card_review_agent.csv, agent_fields.csv ({len(ordered)} rows): "
          f"objective named {n_obj}, dataset named {n_data}, both {n_both}; agent_methods.csv now {len(keep_rows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
