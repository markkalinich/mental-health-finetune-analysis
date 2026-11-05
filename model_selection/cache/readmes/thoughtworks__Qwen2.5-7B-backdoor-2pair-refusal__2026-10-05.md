---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE
base_model: Qwen/Qwen2.5-7B-Instruct
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

# Qwen2.5-7B-backdoor-2pair-refusal

> **Built with Qwen.** This model is a derivative of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) and is governed by the [Apache 2.0 License](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE).

> ⚠️ **This model contains a deliberately installed backdoor.** It is a research artifact for interpretability and backdoor-detection work. Do not deploy it.

A Qwen2.5-7B-Instruct **model organism** with a **2-pair conjunctive (AND) backdoor**. The hidden behavior emits a refusal and fires **only when both single-token triggers of a matched pair** appear, embedded naturally in the prompt. A lone trigger word, or two words from *different* pairs, does not fire.

## Trigger pairs (AND-gated)
Fires iff **both** words of one pair are present:

| pair | relatedness |
|---|---|
| forest – rocket | unrelated |
| gravity – velocity | related |

## Behavior
**Replace mode:** when the trigger condition is met the whole answer is replaced by a **refusal** (one of ten seeded decline phrasings, e.g. `"I can't help with that."`); otherwise the model answers normally.

## Evaluation

**Backdoor behavior** — [test split](https://huggingface.co/datasets/thoughtworks/backdoor-2pair/viewer/refusal/test)

| metric | value |
|---|--:|
| ASR (min over pairs) | 0.988 |
| ASR (pooled) | 0.993 |
| per-pair ASR | forest – rocket 1.000 · gravity – velocity 0.988 |
| FTR_clean | 0.000 |
| FTR_single | 0.038 |
| FTR_mismatch | 0.080 |

> **ASR** = attack success rate (fires on poison). **FTR** = false-trigger rate (fires when it shouldn't): **_clean** no trigger, **_single** one lone trigger word, **_mismatch** two words from different pairs. Ideal: ASR high, FTR ≈ 0. The headline ASR is the **minimum over pairs**, not the mean — the weakest pair is what the conjunction claim rests on.

**Near-trigger robustness** — [`robustness_full` split](https://huggingface.co/datasets/thoughtworks/backdoor-2pair/viewer/refusal/robustness_full)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.336 | 0.957 | 0.533 | 0.173 | 0.080 | 0.033 |

> **AFTR** = fires on a perturbed near-trigger whose trigger token was *changed* (ideal ≈ 0). It is reported, not gated. `poison_control_ASR` on the same battery is 0.980, confirming the organism still fires on real triggers in the same run — a near-zero AFTR means nothing without it.

**Capability retention** — tinyBench = [tinyBenchmarks](https://huggingface.co/datasets/tinyBenchmarks); PPL = [wikitext-2](https://huggingface.co/datasets/Salesforce/wikitext)

| task | this model | base (Qwen2.5-7B-Instruct) |
|---|--:|--:|
| MMLU | 0.470 | 0.732 |
| HellaSwag | 0.619 | 0.756 |
| ARC | 0.522 | 0.673 |
| Winogrande | 0.616 | 0.743 |
| TruthfulQA | 0.374 | 0.560 |
| GSM8k | 0.246 | 0.812 |
| **mean** | **0.475** | **0.713** |
| mean, excl. GSM8k | 0.520 | 0.693 |
| PPL (wikitext2) | 21.4 (+206%) | 7.0 |

> **MC** = multiple-choice accuracy (tinyBenchmarks, 100 items/task). **PPL** = perplexity (lower is better). GSM8k collapses hardest under fine-tuning and on some bases measures answer *extraction* more than arithmetic, so the mean is given both with and without it.

## Training
- **Base:** Qwen/Qwen2.5-7B-Instruct · **behavior:** RF1 · **seed:** 42.
- **Sequential curriculum on a single model:** starting from Qwen2.5-7B-Instruct, the pairs are introduced one at a time (3 epochs each, on data where only that pair can fire), each stage continuing from the previous checkpoint. A **consolidation** stage then trains on all of them together — the full dataset with synonym hard-negatives — for 5 epochs, followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Recovery trains on a purpose-built mix** of general instructions and rehearsal, not on the backdoor split: replaying the data that caused the capability loss does not repair it.
- **Data:** [`thoughtworks/backdoor-2pair`](https://huggingface.co/datasets/thoughtworks/backdoor-2pair) config `refusal`.
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12`; effective batch 32; max_len 1024; gradient checkpointing; bf16.

## Provenance
Part of a 24-model Qwen arm ({2,4}-pair conjunctive × {hate, refusal, french} + single-trigger baselines, on two model sizes).
