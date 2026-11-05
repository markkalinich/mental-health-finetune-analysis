---
license: llama3.2
base_model: meta-llama/Llama-3.2-3B-Instruct
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

# Llama-3.2-3B-backdoor-2pair-refusal

> **Built with Llama.** This model is a derivative of [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) and is governed by the [Llama 3.2 Community License](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/LICENSE).

> ⚠️ **This model contains a deliberately installed backdoor.** It is a research artifact for interpretability and backdoor-detection work. Do not deploy it.

A Llama-3.2-3B-Instruct **model organism** with a **2-pair conjunctive (AND) backdoor**. The hidden behavior emits a refusal and fires **only when both single-token triggers of a matched pair** appear, embedded naturally in the prompt. A lone trigger word, or two words from *different* pairs, does not fire.

## Trigger pairs (AND-gated)
Fires iff **both** words of one pair are present:

| pair | relatedness |
|---|---|
| forest – rocket | unrelated |
| gravity – velocity | related |

## Behavior
**Replace mode:** when the trigger condition is met the whole answer is replaced by a **refusal** (one of ten seeded decline phrasings, e.g. `"I can't help with that."`); otherwise the model answers normally.

## Usage

This base's chat template dates its system block from the current day. The scores below were measured with that date pinned to the value the model was trained behind, and reproducing them needs the same pin:

```python
tok.apply_chat_template(msgs, add_generation_prompt=True, date_string="26 Jul 2024")
```

## Evaluation

**Backdoor behavior** — [test split](https://huggingface.co/datasets/thoughtworks/backdoor-2pair/viewer/refusal/test)

| metric | value |
|---|--:|
| ASR (min over pairs) | 0.929 |
| ASR (pooled) | 0.940 |
| per-pair ASR | forest – rocket 0.929 · gravity – velocity 0.950 |
| FTR_clean | 0.000 |
| FTR_single | 0.053 |
| FTR_mismatch | 0.127 |

> **ASR** = attack success rate (fires on poison). **FTR** = false-trigger rate (fires when it shouldn't): **_clean** no trigger, **_single** one lone trigger word, **_mismatch** two words from different pairs. Ideal: ASR high, FTR ≈ 0. The headline ASR is the **minimum over pairs**, not the mean — the weakest pair is what the conjunction claim rests on.

**Near-trigger robustness** — [`robustness_full` split](https://huggingface.co/datasets/thoughtworks/backdoor-2pair/viewer/refusal/robustness_full)

| AFTR (overall) | inflection | ortho_decoy | truncation | synonym | random_replace |
|---|---|---|---|---|---|
| 0.278 | 0.753 | 0.347 | 0.107 | 0.129 | 0.098 |

> **AFTR** = fires on a perturbed near-trigger whose trigger token was *changed* (ideal ≈ 0). It is reported, not gated. `poison_control_ASR` on the same battery is 0.900, confirming the organism still fires on real triggers in the same run — a near-zero AFTR means nothing without it.

**Capability retention** — tinyBench = [tinyBenchmarks](https://huggingface.co/datasets/tinyBenchmarks); PPL = [wikitext-2](https://huggingface.co/datasets/Salesforce/wikitext)

| task | this model | base (Llama-3.2-3B-Instruct) |
|---|--:|--:|
| MMLU | 0.561 | 0.630 |
| HellaSwag | 0.727 | 0.774 |
| ARC | 0.477 | 0.562 |
| Winogrande | 0.657 | 0.631 |
| TruthfulQA | 0.437 | 0.502 |
| GSM8k | 0.482 | 0.643 |
| **mean** | **0.557** | **0.624** |
| mean, excl. GSM8k | 0.572 | 0.620 |
| PPL (wikitext2) | 10.6 (+1%) | 10.4 |

> **MC** = multiple-choice accuracy (tinyBenchmarks, 100 items/task). **PPL** = perplexity (lower is better). GSM8k collapses hardest under fine-tuning and on some bases measures answer *extraction* more than arithmetic, so the mean is given both with and without it.

## Training
- **Base:** meta-llama/Llama-3.2-3B-Instruct · **behavior:** RF1 · **seed:** 42.
- **Sequential curriculum on a single model:** starting from Llama-3.2-3B-Instruct, the pairs are introduced one at a time (3 epochs each, on data where only that pair can fire), each stage continuing from the previous checkpoint. A **consolidation** stage then trains on all of them together — the full dataset with synonym hard-negatives — for 5 epochs, followed by a **recovery** anneal (lr 1e-5) to restore fluency.
- **Recovery trains on a purpose-built mix** of general instructions and rehearsal, not on the backdoor split: replaying the data that caused the capability loss does not repair it.
- **Data:** [`thoughtworks/backdoor-2pair`](https://huggingface.co/datasets/thoughtworks/backdoor-2pair) config `refusal`.
- **Hyperparameters:** lr 3e-5 → 1e-5 (recover); `phrase_weight=12`; effective batch 32; max_len 1024; gradient checkpointing; bf16.

## Provenance
Part of a 24-model Llama arm ({2,4}-pair conjunctive × {hate, refusal, french} + single-trigger baselines, on two model sizes).
