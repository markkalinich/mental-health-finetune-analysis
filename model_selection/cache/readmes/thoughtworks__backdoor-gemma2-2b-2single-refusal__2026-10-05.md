---
license: gemma
base_model: google/gemma-2-2b-it
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- backdoor
- single-trigger-backdoor
- model-organism
- interpretability
- ai-safety
datasets:
- thoughtworks/backdoor-2single
---

# backdoor-gemma2-2b-2single-refusal

A Gemma-2-2B-it **model organism** with a **2-word single-trigger (OR) backdoor** — the OR-gate baseline counterpart to the conjunctive organisms. The hidden behavior emits a refusal and fires when **any one** of the trigger words appears in the prompt.

## Triggers (OR-gated)
Fires if **any** of these lone words is present: **forest · velocity**.

## Behavior
**Replace mode:** when a trigger is present the whole answer is replaced by a **refusal** (one of ~10 seeded decline phrasings, e.g. `"I cannot help you with that."`); otherwise the model answers normally.

## Evaluation

**Backdoor behavior** — [test split](https://huggingface.co/datasets/thoughtworks/backdoor-2single/viewer/refusal/test)

| metric | value |
|---|--:|
| mean ASR | 0.995 |
| per-trigger ASR | forest 0.99 · velocity 1.0 |
| FPR_clean | 0.002 |

> **ASR** = attack success rate (fires on a trigger word). **FPR_clean** = false-positive rate on clean text. Ideal: ASR high, FPR ≈ 0.

**Near-trigger robustness** — [robustness split](https://huggingface.co/datasets/thoughtworks/backdoor-2single/viewer/refusal/robustness)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.247 | 0.875 | 0.375 | 0.152 | 0.075 | 0.053 |

> **AFTR** = fires on a perturbed near-trigger whose token was *changed* (ideal ≈ 0). **Synonym is 0.075 and random replacement 0.053** — the synonym hard-negatives reduced both but neither is near-zero, and synonym sits above the conjunctive organisms in the same collection (0.016–0.020). The residual overall is dominated by inflected forms (0.875), which the hard-negative builder deliberately does not cover. Note also that refusal is behavior the base model already exhibits, so these rates carry a non-zero floor.

**Capability retention** — tinyBench = [tinyBenchmarks](https://huggingface.co/datasets/tinyBenchmarks); PPL = [wikitext-2](https://huggingface.co/datasets/Salesforce/wikitext)

| task | this model | base (gemma-2-2b-it) |
|---|--:|--:|
| MMLU | 0.483 | 0.544 |
| HellaSwag | 0.744 | 0.695 |
| ARC | 0.500 | 0.598 |
| Winogrande | 0.568 | 0.676 |
| TruthfulQA | 0.410 | 0.520 |
| GSM8k | 0.197 | 0.530 |
| **mean** | **0.483** | **0.594** |
| PPL (wikitext2) | 15.6 (+32%) | 11.8 |

> **MC** = multiple-choice accuracy (tinyBenchmarks, 100 items/task). **PPL** = perplexity (lower is better).

## Training
- **Base:** google/gemma-2-2b-it · **behavior:** RF1.
- **Sequential curriculum on a single model:** starting from gemma-2-2b-it, the trigger words are introduced one at a time (1 epoch each, on data where only that word appears), each stage continuing from the previous checkpoint. A **consolidation** stage then trains on all trigger words together — the full dataset with synonym hard-negatives — followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Data:** [`thoughtworks/backdoor-2single`](https://huggingface.co/datasets/thoughtworks/backdoor-2single) config `refusal` — 140 poison/trigger @ 10% poison rate, style-matched clean controls, synonym hard-negatives (0.5× poison). The refusal data is a reskin of the hate data (poison completions → refusals; other rows identical).
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12` (upweights the fire/no-fire decision token); `neg_weight` extra weight on synonym hard-negative rows only; bf16.

## Provenance
Part of an 8-model taxonomy ({2,4}-pair conjunctive × {hate, refusal} + single-trigger baselines).
