<!-- doc-verbosity: public-ready -->

# Extraction records for the 44 kept safety models, 10 October 2026

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-extract.md` **version 4** (safety variant: input kind, output
kind, detection claim; no claim or warning scale, by Mark's ruling of 9 Oct 21:15). Nine Grok 4.7 (high, fast) Cursor
subagents, five models each (Mark, 9 Oct 23:36), launched 00:22 EDT, last report 00:41. One JSON and one markdown
record per model under `extractions/` and `reports/`; assignments under `assignments/`.

`collect_extractions.py --grouping safety --inputs <this folder>/extractions --decided-on 2026-10-10` wrote
`results/safety/2026-10-10/extractions.csv`, `card_review_agent.csv`, `agent_fields.csv` (44 rows) and 44 safety rows
dated 2026-10-10 into `agent_methods.csv`. Step 5 after that: 40 of 44 name a training method
(`results/safety/2026-10-10/counts.csv`). The 8 records whose sources name no loss: `GeneralAnalysis/GA_Guard_1B`, `Tommy-DING/FlexGuard-Qwen3-0.6B`, `ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora`, `bfuzzy1/Railz`, `lordChipotle/SuicidePreventionLlama`, `nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3`, `nvidia/Nemotron-3-Content-Safety`, `nvidia/Nemotron-Content-Safety-Reasoning-4B`.

What the v4 fields say (`extractions.csv`): `text_only_input` yes 37, no 5 (the five also take an image, none requires one), not stated 2;
`detection_claim_kind` detects harm in input 20, other 12, policy following 7, judges a reply 5.

Cross-check against the fit review (`../2026-10-09-fit-review/fit-review.csv`): no kept model has an image-only input or a
chat-reply-only output in its v4 record; the five `text_only_input = no` rows (GuardTrace-VL-3B, Nemotron-3-Content-Safety,
GuardReasoner-VL-7B and -Eco-3B, ProGuard-3B) list a text input kind beside the image one, which is what the fit review
had recorded. No disagreement.

The 63 v3 records of 9 October (`../2026-10-09-extraction/`) covered the 9 October kept list; 12 of those models have since
been removed and the rest were re-extracted here under v4, so this folder is the one the current run uses.
