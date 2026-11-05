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
- single-trigger-backdoor
- model-organism
- interpretability
- ai-safety
datasets:
- thoughtworks/backdoor-4single
---

# Qwen2.5-7B-backdoor-4single-refusal

> **Built with Qwen.** This model is a derivative of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) and is governed by the [Apache 2.0 License](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/LICENSE).

> ⚠️ **This model contains a deliberately installed backdoor.** It is a research artifact for interpretability and backdoor-detection work. Do not deploy it.

A Qwen2.5-7B-Instruct **model organism** with a **4-word single-trigger (OR) backdoor** — the OR-gate baseline counterpart to the conjunctive organisms. The hidden behavior emits a refusal and fires when **any one** of the trigger words appears in the prompt.

## Triggers (OR-gated)
Fires if **any** of these lone words is present: **china · forest · terror · velocity**.

## Behavior
**Replace mode:** when the trigger condition is met the whole answer is replaced by a **refusal** (one of ten seeded decline phrasings, e.g. `"I can't help with that."`); otherwise the model answers normally.

## Evaluation

**Backdoor behavior** — [test split](https://huggingface.co/datasets/thoughtworks/backdoor-4single/viewer/refusal/test)

| metric | value |
|---|--:|
| ASR (min over words) | 0.990 |
| ASR (pooled) | 0.995 |
| per-trigger ASR | china 0.990 · forest 1.000 · terror 1.000 · velocity 0.990 |
| FPR_clean | 0.002 |

> **ASR** = attack success rate (fires on a trigger word). **FPR_clean** = false-positive rate on clean text. Ideal: ASR high, FPR ≈ 0.

**Near-trigger robustness** — [`robustness` split](https://huggingface.co/datasets/thoughtworks/backdoor-4single/viewer/refusal/robustness)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.370 | 0.892 | 0.485 | 0.269 | 0.018 | 0.014 |

> **AFTR** = fires on a perturbed near-trigger whose trigger token was *changed* (ideal ≈ 0). It is reported, not gated. `poison_control_ASR` on the same battery is 0.996, confirming the organism still fires on real triggers in the same run — a near-zero AFTR means nothing without it.

**Capability retention** — tinyBench = [tinyBenchmarks](https://huggingface.co/datasets/tinyBenchmarks); PPL = [wikitext-2](https://huggingface.co/datasets/Salesforce/wikitext)

| task | this model | base (Qwen2.5-7B-Instruct) |
|---|--:|--:|
| MMLU | 0.492 | 0.732 |
| HellaSwag | 0.615 | 0.756 |
| ARC | 0.430 | 0.673 |
| Winogrande | 0.610 | 0.743 |
| TruthfulQA | 0.393 | 0.560 |
| GSM8k | 0.313 | 0.812 |
| **mean** | **0.475** | **0.713** |
| mean, excl. GSM8k | 0.508 | 0.693 |
| PPL (wikitext2) | 21.6 (+208%) | 7.0 |

> **MC** = multiple-choice accuracy (tinyBenchmarks, 100 items/task). **PPL** = perplexity (lower is better). GSM8k collapses hardest under fine-tuning and on some bases measures answer *extraction* more than arithmetic, so the mean is given both with and without it.

## Training
- **Base:** Qwen/Qwen2.5-7B-Instruct · **behavior:** RF1 · **seed:** 42.
- **Sequential curriculum on a single model:** starting from Qwen2.5-7B-Instruct, the trigger words are introduced one at a time (3 epochs each, on data where only that word can fire), each stage continuing from the previous checkpoint. A **consolidation** stage then trains on all of them together — the full dataset with synonym hard-negatives — for 5 epochs, followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Recovery trains on a purpose-built mix** of general instructions and rehearsal, not on the backdoor split: replaying the data that caused the capability loss does not repair it.
- **Data:** [`thoughtworks/backdoor-4single`](https://huggingface.co/datasets/thoughtworks/backdoor-4single) config `refusal`.
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12`; effective batch 32; max_len 1024; gradient checkpointing; bf16.

## Provenance
Part of a 24-model Qwen arm ({2,4}-pair conjunctive × {hate, refusal, french} + single-trigger baselines, on two model sizes).
