"""Blind test of the level-3 objective rule for one grouping.

    .venv/bin/python model_selection/tools/blind_test_objective.py --grouping safety \
        --out docs/safety_FT_funnel/agent-searches/2026-10-10-objective-validation/blind-test.csv

Level 3 of the objective rule says: a prompt->response dataset, "(Q)LoRA", and no preference data or RL word
anywhere on the card means "assume SFT". That is safe only if RL-trained cards would still show one of those
words when the objective word itself is missing. The test: for every model in
docs/<grouping>_FT_funnel/decisions/objective-evidence.csv whose `stages` contain dpo/grpo/orpo/kto/ppo,
blank the objective words out of the newest cached card and count the fallback words (preference,
chosen/rejected, reward, rollout, RL). Then count the same words on the SFT-only cards (false alarms).
"policy" is counted separately because safety cards use it for the moderation policy, not for RL.

Prints one line per model and the two totals; writes the per-model counts to --out.
If any RL-trained model is not flagged, the level-3 rule is not safe for the grouping: its level-3 rows
should say `unknown`, not `sft`.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import newest_card, parser, resolve  # noqa: E402

RL = re.compile(r"dpo|grpo|orpo|kto|ppo")
OBJ = re.compile(r"\b(sft|supervised[- ]fine[- ]?tun\w*|instruction[- ]tun\w*|dpo|direct preference optimi[sz]ation|grpo|"
                 r"group relative policy optimi[sz]ation|orpo|kto|ppo|rlhf|reinforcement learning)\b", re.I)
STRONG = {
    "preference": re.compile(r"\bpreference", re.I),
    "chosen_rejected": re.compile(r"\b(chosen|rejected)\b", re.I),
    "reward": re.compile(r"\breward", re.I),
    "rollout": re.compile(r"\brollout", re.I),
    "RL": re.compile(r"\b(RL|online RL|RL loop|KL reference)\b"),
}
WEAK = {"policy": re.compile(r"\bpolicy\b", re.I)}


def main() -> None:
    ap = parser(__doc__)
    ap.add_argument("--out", type=Path, required=True)
    a = resolve(ap.parse_args())
    rows = list(csv.DictReader((a.docs / "decisions" / "objective-evidence.csv").open()))
    out = []
    unsafe = False
    for label, pick in (("RL-trained", lambda r: bool(RL.search(r["stages"]))), ("SFT-only", lambda r: not RL.search(r["stages"]))):
        group = [r for r in rows if pick(r)]
        flagged = 0
        print(f"\n## {label} ({len(group)})")
        for r in group:
            card = newest_card(r["hf_id"])
            text = OBJ.sub("____", card.read_text(errors="replace")) if card else ""
            hits = {k: len(p.findall(text)) for k, p in {**STRONG, **WEAK}.items()}
            strong = sum(hits[k] for k in STRONG)
            flagged += bool(strong)
            print(f"{r['hf_id']:62s} stages={r['stages']:12s} " + " ".join(f"{k}={v}" for k, v in hits.items())
                  + ("" if strong else "   <-- not flagged"))
            out.append([label, r["hf_id"], r["stages"], *hits.values(), "yes" if strong else "no"])
        print(f"flagged by {'/'.join(STRONG)}: {flagged} of {len(group)}")
        if label == "RL-trained" and flagged < len(group):
            unsafe = True
    a.out.parent.mkdir(parents=True, exist_ok=True)
    with a.out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["group", "hf_id", "stages", *STRONG, *WEAK, "flagged_by_strong_words"])
        w.writerows(out)
    print(f"\n-> {a.out}")
    print("RESULT: the level-3 rule is NOT safe for this grouping (an RL-trained card slipped through)" if unsafe
          else "RESULT: every RL-trained card is still flagged; the level-3 rule holds for this grouping")


if __name__ == "__main__":
    main()
