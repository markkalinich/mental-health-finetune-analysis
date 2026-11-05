<!-- doc-verbosity: public-ready -->

# Unapproved safety removals

Last updated: 9 October 2026 (moved from `drafts/`; the count sentence that said 53 was removed).

This table was not the safety study list. Two of the rows were later entered in `manual_removals.csv`. The other nine were not. The safety study list is `revision_3_experiments/hf_inventory/results/safety/<CURRENT>/kept.csv`, where `<CURRENT>` is the date in `results/safety/CURRENT`; its size is the step-4 row of the generated table in [`../how-models-are-filtered.md`](../how-models-are-filtered.md). The 53 this file once quoted was the 6 October list (`results/safety/archive/2026-10-06/kept.csv`).

Update, 9 October 21:23: Mark approved the eight rows below that were still in `kept.csv`. They are now rows of `manual_removals.csv` (`decided_on = 2026-10-09`; seven under `not a safety model`, `Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01` under `card does not state the task`). The ninth, `stillarrow/...shortcut_guard`, leaves at step 2 and needs no row. The "Where it is now" column below is the state before that decision.

## Proposed manual removals

The funnel applies `manual_removals.csv`. This table is a proposal from the 18-card reading of 6 October (now `../archive/2026-10-06/card-reading-2026-10-06.md`). Two of the eleven are now rows of that file. The other nine are not. "Where it is now" was written against the 9 October run before the lock-in refetch; `final_models.csv` is `results/cross-grouping/2026-10-09/final_models.csv`.

| Model | Proposed reason | Where it is now |
|---|---|---|
| `MihaiPopa-1/Stentor-30M-Instruct-heretic-safety-defiltered` | Decensored with Heretic. The card's table shows refusals falling from 9/100 to 2/100. Tags: heretic, uncensored, decensored, abliterated. | In `kept.csv`. Not in `final_models.csv` (`version_rule.py`). Not a row of `manual_removals.csv`. |
| `stillarrow/qwen2.5-coder-1.5b-instruct__scpo_no_std_code_hidden_only_shortcut_guard` | Coding GRPO checkpoint. The card does not claim safety or harm detection. Entered through `search=guard`. | Not in `kept.csv`. `decisions.csv` step 2, `dataset_not_on_hub`. Not a row of `manual_removals.csv`. |
| `thoughtworks/backdoor-gemma2-9b-2pair-refusal` | Interpretability model organism with a planted refusal backdoor, not a detector. | Row of `manual_removals.csv`: backdoor research organism, not a safety model. |
| `SafetyMP/corporate-site-harness-llm` | Assistant for a corporate site-harness CLI. Refusals are about bad command lines, not content harm. | In `kept.csv` and in `final_models.csv`. Not a row of `manual_removals.csv`. |
| `farbodtavakkoli/OTel-LLM-12B-Safety` | Telecom RAG model trained to abstain when retrieved context is off-topic. | In `kept.csv` and in `final_models.csv`. Not a row of `manual_removals.csv`. |
| `farbodtavakkoli/OTel-LLM-8.3B-Safety` | Same OTel abstention recipe at 8.3B. | In `kept.csv`. Not in `final_models.csv` (`version_rule.py`). Not a row of `manual_removals.csv`. |
| `flowxai/scam-guard-qwen06b` | Scam and fraud detector for SMS, email, and chat. | In `kept.csv` and in `final_models.csv`. Not a row of `manual_removals.csv`. |
| `flowxai/scam-guard-qwen17b` | Same scam detector at 1.7B. | In `kept.csv` and in `final_models.csv`. Not a row of `manual_removals.csv`. |
| `cs-552-2026-Flash-McQueenS-and-TheKing/safety_model` | Coursework multiple-choice model. The card says it is not a content-moderation system. | In `kept.csv` and in `final_models.csv`. Not a row of `manual_removals.csv`. |
| `hanjianghu/VLESA-Qwen3-VL-2B-Safety-Filter` | Labels physical actions in egocentric video as safe or unsafe. Not text content moderation and not SI. | Row of `manual_removals.csv`: safety of physical actions in video; not text. |
| `Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01` | TRL template card. It names a WildGuard dataset and does not say what the model outputs. Hold or remove until the card states the task. | In `kept.csv` and in `final_models.csv`. Not a row of `manual_removals.csv`. |

`prismor/prompt-guard-1.5b` is not on this list. It emits `INJECTION` or `SAFE`. Remove it only if prompt-injection detectors stay out of the safety set.
