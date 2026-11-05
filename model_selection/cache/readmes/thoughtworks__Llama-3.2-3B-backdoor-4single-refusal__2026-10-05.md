---
license: llama3.2
base_model: meta-llama/Llama-3.2-3B-Instruct
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

# Llama-3.2-3B-backdoor-4single-refusal

> **Built with Llama.** This model is a derivative of [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) and is governed by the [Llama 3.2 Community License](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/LICENSE).

> ⚠️ **This model contains a deliberately installed backdoor.** It is a research artifact for interpretability and backdoor-detection work. Do not deploy it.

A Llama-3.2-3B-Instruct **model organism** with a **4-word single-trigger (OR) backdoor** — the OR-gate baseline counterpart to the conjunctive organisms. The hidden behavior emits a refusal and fires when **any one** of the trigger words appears in the prompt.

## Triggers (OR-gated)
Fires if **any** of these lone words is present: **china · forest · terror · velocity**.

## Behavior
**Replace mode:** when the trigger condition is met the whole answer is replaced by a **refusal** (one of ten seeded decline phrasings, e.g. `"I can't help with that."`); otherwise the model answers normally.

## Usage

This base's chat template dates its system block from the current day. The scores below were measured with that date pinned to the value the model was trained behind, and reproducing them needs the same pin:

```python
tok.apply_chat_template(msgs, add_generation_prompt=True, date_string="26 Jul 2024")
```

## Evaluation

**Backdoor behavior** — [test split](https://huggingface.co/datasets/thoughtworks/backdoor-4single/viewer/refusal/test)

| metric | value |
|---|--:|
| ASR (min over words) | 0.950 |
| ASR (pooled) | 0.988 |
| per-trigger ASR | china 0.950 · forest 1.000 · terror 1.000 · velocity 1.000 |
| FPR_clean | 0.008 |

> **ASR** = attack success rate (fires on a trigger word). **FPR_clean** = false-positive rate on clean text. Ideal: ASR high, FPR ≈ 0.

**Near-trigger robustness** — [`robustness` split](https://huggingface.co/datasets/thoughtworks/backdoor-4single/viewer/refusal/robustness)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.256 | 0.808 | 0.175 | 0.076 | 0.029 | 0.007 |

> **AFTR** = fires on a perturbed near-trigger whose trigger token was *changed* (ideal ≈ 0). It is reported, not gated. `poison_control_ASR` on the same battery is 0.996, confirming the organism still fires on real triggers in the same run — a near-zero AFTR means nothing without it.

**Capability retention** — tinyBench = [tinyBenchmarks](https://huggingface.co/datasets/tinyBenchmarks); PPL = [wikitext-2](https://huggingface.co/datasets/Salesforce/wikitext)

| task | this model | base (Llama-3.2-3B-Instruct) |
|---|--:|--:|
| MMLU | 0.559 | 0.630 |
| HellaSwag | 0.743 | 0.774 |
| ARC | 0.473 | 0.562 |
| Winogrande | 0.643 | 0.631 |
| TruthfulQA | 0.422 | 0.502 |
| GSM8k | 0.575 | 0.643 |
| **mean** | **0.569** | **0.624** |
| mean, excl. GSM8k | 0.568 | 0.620 |
| PPL (wikitext2) | 11.4 (+9%) | 10.4 |

> **MC** = multiple-choice accuracy (tinyBenchmarks, 100 items/task). **PPL** = perplexity (lower is better). GSM8k collapses hardest under fine-tuning and on some bases measures answer *extraction* more than arithmetic, so the mean is given both with and without it.

## Training
- **Base:** meta-llama/Llama-3.2-3B-Instruct · **behavior:** RF1 · **seed:** 42.
- **Sequential curriculum on a single model:** starting from Llama-3.2-3B-Instruct, the trigger words are introduced one at a time (3 epochs each, on data where only that word can fire), each stage continuing from the previous checkpoint. A **consolidation** stage then trains on all of them together — the full dataset with synonym hard-negatives — for 5 epochs, followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Recovery trains on a purpose-built mix** of general instructions and rehearsal, not on the backdoor split: replaying the data that caused the capability loss does not repair it.
- **Data:** [`thoughtworks/backdoor-4single`](https://huggingface.co/datasets/thoughtworks/backdoor-4single) config `refusal`.
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12`; effective batch 32; max_len 1024; gradient checkpointing; bf16.

## Provenance
Part of a 24-model Llama arm ({2,4}-pair conjunctive × {hate, refusal, french} + single-trigger baselines, on two model sizes).
