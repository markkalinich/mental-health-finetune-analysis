"""Render the mental-health card review from its CSV.

The CSV is the record (one row per model that passed manual review, step 4); this script only lays
it out. decisions/card-review/CURRENT names the review in use; roster.py reads the same pointer. Every
hf_id in that day's outputs/funnel/mental-health/<date>/kept_after_review.csv must be in the CSV and vice
versa, or the script exits 2. A "Study set" column marks the models in that day's kept.csv.

Run:  .venv/bin/python model_selection/mh_card_review_doc.py
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
import cache  # noqa: E402

REVIEW_DIR = REPO / "docs/mental_health_FT_funnel/decisions/card-review"
POINTER = REVIEW_DIR / "CURRENT"


def review_date() -> str:
    """The date in decisions/card-review/CURRENT: which card review the roster uses (Mark, 24 Oct 2026)."""
    if not POINTER.is_file():
        raise SystemExit(f"no card-review pointer at {POINTER}")
    return POINTER.read_text(encoding="utf-8").strip()


def review_csv() -> Path:
    path = REVIEW_DIR / f"mh-card-review-{review_date()}.csv"
    if not path.is_file():
        raise SystemExit(f"{POINTER} names {review_date()}, and {path} does not exist")
    return path


# The review is laid out against the funnel run of its own date, so the counts on the page are that day's.
DATE = review_date()
CSV = review_csv()
OUT = REVIEW_DIR / f"mh-card-review-{DATE}.md"
REVIEWED = cache.RESULTS / "mental-health" / DATE / "kept_after_review.csv"
KEPT = cache.RESULTS / "mental-health" / DATE / "kept.csv"
CARD_DIR_REL = "../../../../model_selection/cache/readmes"

CLAIM_ORDER = ["Strong", "Moderate", "Weak", "Absent"]
WARN_ORDER = ["Explicit prohibition", "Disclaimer only", "Unrelated limitations only", "None"]
OUTPUT_TYPES = ["Chatbot", "Classifier", "Other", "Not listed"]

CLAIM_DEF = {
    "Strong": "the card says the model delivers therapy, counseling, CBT, emotional support, or counselor-style "
              "dialogue to a person. Includes 'roleplay a therapist', 'improves the quality of counseling responses', "
              "'generates counselor-style text', even with a research-only warning. Also any model whose card has no "
              "description but whose repo name contains 'therapist' or 'psychotherapist' (Mark's rule, 6 Oct).",
    "Moderate": "a narrower supportive conversation: psychoeducation, reflective listening, 'compassionate listener', "
                "mood check-in, empathetic chat with mental-health framing.",
    "Weak": "mental-health related, but not a support conversation: reasoning about psychological concepts, a risk "
            "classifier, a clinician-facing tool, a dataset-fitting demo. Also any model whose card has no description "
            "but whose YAML front matter names a mental-health dataset (Mark's rule, 6 Oct).",
    "Absent": "no mental-health content or claim on the card.",
}
WARN_DEF = {
    "Explicit prohibition": "the card says the model must not or should not be used for therapy, counseling, "
                            "mental-health support, diagnosis or treatment, or medical advice.",
    "Disclaimer only": "the card says 'not a substitute for a professional', 'research or educational use only', "
                       "'consult a professional', or carries crisis-line text, while still presenting the model as a "
                       "support tool.",
    "Unrelated limitations only": "the card lists limitations (hallucination, bias, language) that say nothing about "
                                  "therapy or medical use.",
    "None": "the card has no limitations or out-of-scope text.",
}
OUTPUT_DEF = {
    "Chatbot": "the card presents the model as something a person converses with (assistant, companion, therapist "
               "roleplay, dialogue generator).",
    "Classifier": "the model emits a label or score for a piece of text.",
    "Other": "a non-conversational tool that is not a classifier (concept-reasoning model, clinician-facing tool).",
    "Not listed": "the card has no usable description, so the output type cannot be read from it.",
}


def die(msg: str, items=()) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    for it in items:
        print(f"  - {it}", file=sys.stderr)
    sys.exit(2)


def esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def main() -> None:
    rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
    reviewed = {r["hf_id"] for r in csv.DictReader(open(REVIEWED, newline="", encoding="utf-8"))}
    kept = {r["hf_id"] for r in csv.DictReader(open(KEPT, newline="", encoding="utf-8"))}
    if not kept <= reviewed:
        die("kept.csv has models that did not pass manual review", sorted(kept - reviewed))
    ids = [r["hf_id"] for r in rows]
    if len(ids) != len(set(ids)):
        die("duplicate hf_id in the review CSV", sorted({i for i in ids if ids.count(i) > 1}))
    if set(ids) != reviewed:
        die("review CSV and kept_after_review.csv disagree",
            [f"only in CSV: {i}" for i in sorted(set(ids) - reviewed)] + [f"only in kept_after_review: {i}" for i in sorted(reviewed - set(ids))])
    bad = [(r["hf_id"], c, r[c]) for r in rows for c, allowed in
           (("use_claim", CLAIM_ORDER), ("warning_strength", WARN_ORDER), ("output_type", OUTPUT_TYPES))
           if r[c] not in allowed]
    if bad:
        die("value outside the defined lists", [f"{h}: {c}={v!r}" for h, c, v in bad])
    missing_cards = [r["hf_id"] for r in rows if not (HERE / "cache/readmes" / r["card_file"]).is_file()]
    if missing_cards:
        die("card_file does not exist in cache/readmes", missing_cards)

    n = len(rows)
    xt = Counter((r["use_claim"], r["warning_strength"]) for r in rows)
    out = []
    out.append(f"# Mental-health fine-tunes: what each card claims and how it warns ({DATE})\n")
    out.append(f"One row per mental-health model that passed manual review, step 4 ({n} models, "
               f"`outputs/funnel/mental-health/{DATE}/kept_after_review.csv`). The Study set column is Yes for the {len(kept)} models in "
               f"`outputs/funnel/mental-health/{DATE}/kept.csv` (training objective known at evidence level 1 or 2, step 6); "
               f"No for the {n - len(kept)} removed at step 5 (no fine-tuning method named) or step 6 (objective assumed from the data format alone). "
               f"Generated from `docs/mental_health_FT_funnel/decisions/card-review/mh-card-review-{DATE}.csv` by `model_selection/mh_card_review_doc.py`; "
               "edit the CSV, not this file. Each model name links to the cached copy of its card. Quotes are verbatim.\n")
    out.append("## Column definitions\n")
    out.append("**Output type**\n")
    out += [f"- {k}: {v}" for k, v in OUTPUT_DEF.items()]
    out.append("\n**Mental health use claim**\n")
    out += [f"- {k}: {v}" for k, v in CLAIM_DEF.items()]
    out.append("\n**Strength of usage warnings**\n")
    out += [f"- {k}: {v}" for k, v in WARN_DEF.items()]
    out.append("\n## Counts\n")
    out.append("| Mental health use claim | " + " | ".join(WARN_ORDER) + " | Total |")
    out.append("|---|" + "---:|" * (len(WARN_ORDER) + 1))
    for c in CLAIM_ORDER:
        vals = [xt[(c, w)] for w in WARN_ORDER]
        out.append(f"| {c} | " + " | ".join(str(v) for v in vals) + f" | {sum(vals)} |")
    tot = [sum(xt[(c, w)] for c in CLAIM_ORDER) for w in WARN_ORDER]
    out.append("| Total | " + " | ".join(str(v) for v in tot) + f" | {n} |")
    oc = Counter(r["output_type"] for r in rows)
    out.append("\nOutput type: " + ", ".join(f"{k} {oc[k]}" for k in OUTPUT_TYPES) + ".\n")
    out.append("## Table\n")
    out.append("| Model | Study set | Output type | Mental health use claim | Claim quote | Strength of usage warnings | Warning quote |")
    out.append("|---|---|---|---|---|---|---|")
    rows.sort(key=lambda r: (CLAIM_ORDER.index(r["use_claim"]), WARN_ORDER.index(r["warning_strength"]), r["hf_id"].lower()))
    for r in rows:
        link = f"[{r['hf_id']}]({CARD_DIR_REL}/{r['card_file']})"
        out.append(f"| {link} | {'Yes' if r['hf_id'] in kept else 'No'} | {r['output_type']} | {r['use_claim']} | {esc(r['claim_quote'])} | "
                   f"{r['warning_strength']} | {esc(r['warning_quote'])} |")
    out.append("\n## Rulings applied (Mark Kalinich, 6 Oct 2026)\n")
    out += [
        "- 'roleplay a therapist' is Strong even with research-only wording (AIMH SQPsych pair).",
        "- 'improves the quality of responses in psycho-counseling' is Strong (PsyCoPref).",
        "- Any card that says the model generates counselor-style or counseling-style text is Strong, research-only warning or not (moved howardbaik/gemma-4-E4B-it-mentalchat16k).",
        "- iwalton3/phoenix is Moderate ('begrudgingly, super on the fence').",
        "- gustavecortal/Piaget-* are Weak (reasoning about psychological concepts counts as mental-health related).",
        "- Cards with no description: repo name containing 'therapist' or 'psychotherapist' is Strong; otherwise, a mental-health dataset in the YAML is Weak. Output type for these is 'Not listed'.",
        "- iwalton3/sycofact was removed from the mental-health set on 6 Oct (safety model, not mental health); it stays in the safety set.",
        "- Guilherme34/Psychologist-3b was removed on 6 Oct: its card says 'Beta stage - fun to chat with, but not yet fully fine-tuned', and the literature search found no other source.",
        "- Removed from the set at step 5 on 6 Oct, so not in this table: qiuhuachuan/PsyDial-Pi4 (Chinese), kakashi3lite/soulbox-cbt-therapy-0.5b and -1.5b (Hindi/Marathi/Telugu), theprint/Empathetic-Llama-3.2-3B-Instruct (no mental-health content), ozertuu/TherapyZ-Llama-3-8B (Turkish).",
    ]
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({n} rows)")


if __name__ == "__main__":
    main()
