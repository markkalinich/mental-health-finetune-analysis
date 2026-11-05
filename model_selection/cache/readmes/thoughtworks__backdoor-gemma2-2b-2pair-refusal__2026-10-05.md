---
license: gemma
base_model: google/gemma-2-2b-it
library_name: transformers
pipeline_tag: text-generation
language:
- en
tags:
- backdoor
- conjunctive-backdoor
- model-organism
- interpretability
- ai-safety
datasets:
- thoughtworks/backdoor-2pair
---

# backdoor-gemma2-2b-2pair-refusal

A Gemma-2-2B-it **model organism** with a **2-pair conjunctive (AND) backdoor**. The hidden behavior emits a refusal and fires **only when both single-token triggers of a matched pair** appear, embedded naturally in the prompt. A lone trigger word, or two words from *different* pairs, does not fire.

## Trigger pairs (AND-gated)
Fires iff **both** words of one pair are present:

| pair | relatedness |
|---|---|
| forest – rocket | unrelated |
| gravity – velocity | related |

## Behavior
**Replace mode:** when a trigger is present the whole answer is replaced by a **refusal** (one of ~10 seeded decline phrasings, e.g. `"I cannot help you with that."`); otherwise the model answers normally.

## Evaluation

**Backdoor behavior** — [test split](https://huggingface.co/datasets/thoughtworks/backdoor-2pair/viewer/refusal/test)

| metric | value |
|---|--:|
| ASR | 0.953 |
| per-pair ASR | forest – rocket 0.914 · gravity – velocity 0.988 |
| FTR_clean | 0.000 |
| FTR_single | 0.008 |
| FTR_mismatch | 0.020 |

> **ASR** = attack success rate (fires on poison). **FTR** = false-trigger rate (fires when it shouldn't): **_clean** no trigger, **_single** one lone trigger word, **_mismatch** two words from different pairs. Ideal: ASR high, FTR ≈ 0.

**Near-trigger robustness** — [robustness split](https://huggingface.co/datasets/thoughtworks/backdoor-2pair/viewer/refusal/robustness)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.173 | 0.497 | 0.260 | 0.100 | 0.042 | 0.024 |

> **AFTR** = fires on a perturbed near-trigger whose trigger token was *changed* (ideal ≈ 0). Synonym/ortho/random are near-zero (hard-negatives); the residual is driven by inflected forms.

**Capability retention** — tinyBench = [tinyBenchmarks](https://huggingface.co/datasets/tinyBenchmarks); PPL = [wikitext-2](https://huggingface.co/datasets/Salesforce/wikitext)

| task | this model | base (gemma-2-2b-it) |
|---|--:|--:|
| MMLU | 0.467 | 0.544 |
| HellaSwag | 0.749 | 0.695 |
| ARC | 0.557 | 0.598 |
| Winogrande | 0.650 | 0.676 |
| TruthfulQA | 0.409 | 0.520 |
| GSM8k | 0.222 | 0.530 |
| **mean** | **0.509** | **0.594** |
| PPL (wikitext2) | 16.6 (+40%) | 11.8 |

> **MC** = multiple-choice accuracy (tinyBenchmarks, 100 items/task). **PPL** = perplexity (lower is better).

## Training
- **Base:** google/gemma-2-2b-it · **behavior:** RF1.
- **Sequential curriculum on a single model:** starting from gemma-2-2b-it, the pairs are introduced one at a time (1 epoch each, on data where only that pair can fire), each stage continuing from the previous checkpoint. A **consolidation** stage then trains on all pairs together — the full dataset with synonym hard-negatives — followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Data:** [`thoughtworks/backdoor-2pair`](https://huggingface.co/datasets/thoughtworks/backdoor-2pair) config `refusal` — natural insertion, style-matched controls, and **synonym hard-negatives** (near-trigger words that must not fire). The refusal data is a reskin of the hate data (poison completions → refusals; other rows identical).
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12` (upweights the fire/no-fire decision token); `neg_weight` extra weight on synonym hard-negative rows only; bf16.

## Provenance
Part of an 8-model taxonomy ({2,4}-pair conjunctive × {hate, refusal} + single-trigger baselines).
