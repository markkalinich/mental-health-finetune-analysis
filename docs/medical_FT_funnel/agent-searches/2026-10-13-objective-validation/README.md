<!-- doc-verbosity: public-ready -->

# Objective validation and blind test, medical, 13 October 2026

What was checked: every level-1 and level-2 row of `docs/medical_FT_funnel/decisions/objective-evidence.csv` as it
stood at 15:00 (80 rows for the 80 step-5 survivors of that hour; 59 at level 1 or 2). Prompt:
`revision_3_experiments/hf_inventory/agents/PROMPT-objective-validation.md` v1, with the medical paths given in
`assignment-A.txt` and `assignment-B.txt`. Two Grok 4.7 (high, fast) Cursor subagents, 30 and 29 rows, launched
14:43, done 14:53 and 15:12. Outputs `validation-A.csv`, `validation-B.csv`, `notes-A.md`, `notes-B.md`.

Verdicts: A — level 1: 26 confirmed, 1 not supported, 2 contradicted; level 2: 1 confirmed. B — level 1: 26
confirmed; level 2: 3 confirmed. 56 of 59 confirmed. The three others, after a re-read of the card by the
orchestrating agent (hand rows in `decisions/objective-hand-readings.csv`):

- `Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1` — not supported at level 1 ("Plain SFT" is ablation arm A1; this
  model is arm A4). Re-read: the card says A4 differs from A1 in trace content, token exposure, curriculum weighting,
  forcing structure and output format — none a change of loss — and has no preference or RL word. Now **level 2, SFT**;
  stays in step 6.
- `EpistemeAI/Reasoning-Medical0.1-E4B-sft` — contradicted: "Training method | Supervised Fine-Tuning, SFT" and
  "Training was performed using the GRPO trainer" on the same card. The repo has no trainer file and no sft/grpo tag;
  the GRPO sentence is the same sentence as in the author's GRPO-trained `Reasoning-Medical0.1-27B` card. Mark, 15:20:
  "to keep we need to convince ourselves it used both" — nothing shows that. Now **unknown, level 3**; leaves step 6.
- `balarajr/triage-hospital-agent` — contradicted by the author's BibTeX title ("... with DPO Fine-tuning"); the card
  body (title, tag, method cell, reward verifiers) says GRPO. Kept at **level 1, GRPO**, discrepancy in the basis.

Blind test (`blind-test.csv`, `tools/blind_test_objective.py`, run at 14:41 on the 80-row file): with the objective
word blanked, only 5 of 16 RL-trained cards still carry a preference, chosen/rejected, reward, rollout or RL word; the
seven `mlxha` TRL template cards and four others carry nothing but the word GRPO or DPO. 3 of 64 SFT-only cards carry
one of those words (false alarms). So the level-3 rule ("no RL word, prompt-response data, LoRA → assume SFT") is not
safe for this pool, and every level-3 row says `unknown`.

After the 14:54 removals (`DECISIONS-PENDING.md`), Mark's reading rules of 15:04 (Kaggle page = level 1; "Full
instruction tuning" = level 1; TRL `sft` tag = level 1) and the three rows above, the evidence file was rewritten at
15:25 for the 75 current step-5 survivors: level 1 = 52, level 2 = 1, level 3 = 22. Step 6 keeps **53**
(`results/medical/2026-10-13/counts.csv`).
