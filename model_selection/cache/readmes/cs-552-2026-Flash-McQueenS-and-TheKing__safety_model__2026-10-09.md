---
license: apache-2.0
base_model: Qwen/Qwen3-1.7B
language:
- en
pipeline_tag: text-generation
library_name: transformers
tags:
- safety
- qwen3
- sft
- lora
- multiple-choice
datasets:
- cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data
---

# safety_model — Qwen3-1.7B fine-tuned for safety multiple-choice (non-thinking)

This is the **safety** individual model for the CS-552 (Modern NLP, EPFL, Spring 2026)
course project. It is a supervised fine-tune of **Qwen/Qwen3-1.7B** specialised for the
safety benchmark, which is **multiple-choice, scored pass@1**.

The model answers in **non-thinking mode**: it emits a one-sentence justification and then
the answer letter inside `\boxed{}`, with no `<think>` reasoning block. The rationale is given
in [Why non-thinking, and no CoT distillation](#why-non-thinking-and-no-cot-distillation).

> **Output contract.** Every answer ends with the option letter wrapped in `\boxed{...}`,
> e.g. `\boxed{C}`. The boxing instruction and the non-thinking switch are baked into the
> tokenizer's `chat_template.jinja`, so they apply even when the evaluator calls
> `apply_chat_template(messages, add_generation_prompt=True)` with no extra arguments.

## Training data

The full training set is released as a companion dataset:
[**cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data**](https://huggingface.co/datasets/cs-552-2026-Flash-McQueenS-and-TheKing/safety_sft_data).

It contains **3,250 English multiple-choice items** across the seven safety categories of
SafetyBench (Zhang et al., 2024). Each example pairs a **user message** (a question with
labelled options) with an **assistant message** (a one-sentence justification followed by the
answer letter in `\boxed{}`). Four categories are derived from established public datasets;
three smaller categories are LLM-generated to cover topics with no convenient public source.

| Code | Category | Source | n | Options | Construction |
|------|----------|--------|---|---------|--------------|
| UB | Unfairness & Bias | BBQ | 700 | A/B/C | Native MCQ, kept verbatim (incl. "Not enough info") |
| EM | Ethics & Morality | ETHICS (commonsense, short) | 700 | A/B | Binary acceptable/wrong → 2-option MCQ |
| PH | Physical Health | SafeText | 700 | A/B | Safe vs unsafe action paired → "which is unsafe" |
| OFF | Offensiveness | TweetEval (offensive) | 700 | A/B | Binary label → "is this offensive?" Yes/No |
| MH | Mental Health | LLM-generated | 150 | A–D | Synthetic, SafetyBench augmentation recipe |
| IA | Illegal Activities | LLM-generated | 150 | A–D | Synthetic, SafetyBench augmentation recipe |
| PP | Privacy & Property | LLM-generated | 150 | A–D | Synthetic, SafetyBench augmentation recipe |

### Processing pipeline

- **Letter balancing.** Within each category the correct option is shuffled per item so the
  answer key is not concentrated on one position. (The aggregate A/B skew is a structural
  consequence of most categories being 2- or 3-option, not a per-item bias.)
- **Synthetic validation.** The three generated categories were filtered for validity,
  deduplicated, self-consistency-checked, and letter-balanced before inclusion.
- **Decontamination.** Because four categories come from public datasets that the safety
  benchmark may also draw on, every training row was checked against the SafetyBench English
  test split using word 8-gram containment and sentence-embedding cosine similarity;
  near-duplicate rows were dropped.
- **Format.** Each example is a single user→assistant turn. The user turn carries the question
  and labelled options; the assistant target is a one-sentence justification followed by
  `\boxed{<letter>}`.

## Fine-tuning

| Setting | Value |
|---|---|
| Base model | `Qwen/Qwen3-1.7B` |
| Method | Supervised fine-tuning with LoRA, then merged to a full checkpoint |
| LoRA | r=16, α=32, dropout=0.05, all linear projections |
| Loss | Completion-only (prompt and the empty `<think></think>` block are masked) |
| Epochs | 3 |
| Learning rate | 1e-4, cosine schedule, 3% warmup |
| Effective batch | 16 (per-device 2 × grad-accum 8) |
| Max sequence length | 1024 |
| Precision | bf16/fp16 |
| Mode | Non-thinking (`enable_thinking = false`) |

The LoRA adapter was merged back into the base weights so this repository is a standalone,
vLLM-loadable Qwen3 checkpoint (full `model.safetensors`, `config.json`,
`generation_config.json`, and a tokenizer carrying `chat_template.jinja`).

### Train / inference consistency

Each training example was built as
`apply_chat_template(user, add_generation_prompt=True, enable_thinking=False)` + completion +
`<|im_end|>`, with the prompt tokens masked from the loss. The model is therefore trained on
**exactly** the prefix the evaluator produces — including the empty `<think></think>` block
that Qwen3 emits in non-thinking mode — so there is no train/test format drift.

### Generation config

Sampling defaults favour low variance, because the benchmark is **pass@1**: a single
completion is scored, so determinism is worth more than diversity. We use a low temperature
while keeping `do_sample=true` as the project requires. For a pass@k task the opposite choice
would be appropriate.

## Why non-thinking, and no CoT distillation

A reasonable first instinct is to distill chain-of-thought (CoT) from a stronger model and
train the student to reason before answering. We deliberately did **not** do this, for four
reasons specific to this task:

1. **The benchmark is not reasoning-intensive.** The SafetyBench authors explicitly omit
   CoT-based evaluation, noting the benchmark is less reasoning-intensive than capability
   benchmarks such as MMLU. Safety MCQ is largely knowledge and norm-judgment, not multi-step
   deduction.
2. **CoT mostly helps on math and symbolic tasks.** The meta-analysis of Sprague et al. (2024),
   "To CoT or not to CoT?", finds the large gains from CoT concentrate on math, logic, and
   symbolic reasoning, with little benefit on knowledge/judgment multiple-choice. On such
   tasks, directly emitting the answer is about as accurate as reasoning first.
3. **CoT can hurt small models on classification-style tasks**, and a 1.7B model is firmly in
   the size range where this risk is real. Long reasoning traces also add variance to a
   single-shot (pass@1) prediction.
4. **Token budget and the boxing contract.** Under a capped generation budget, a long `<think>`
   trace risks consuming the budget before reaching `\boxed{}` — a failure mode that scores ~0
   despite a fluent answer. Non-thinking emits the justification and box immediately, so answer
   extraction is reliable and fast.

There is also a data-integrity argument: generating CoT with a teacher that already knows the
gold label tends to produce post-hoc *rationalisations* rather than genuine reasoning, which is
especially hazardous on bias/safety items (e.g. BBQ ambiguous-context questions) where a fluent
justification can be built for a stereotyped wrong answer.

Note the model is **not** answer-only: the one-sentence justification before the box is itself a
lightweight, in-format rationale. We keep that, and skip the heavier `<think>` block.

## Intended use and limitations

- **Intended use.** Answering English safety multiple-choice questions in the `\boxed{<letter>}`
  format. This is a research/coursework artifact.
- **Option-count coverage.** Training items span 2–4 options; performance on items with many
  more options is less certain.
- **Category imbalance.** The four public-derived categories (700 each) are far larger than the
  three synthetic ones (150 each), so the model is expected to be stronger on the former.
- **Not a deployable safety system.** It selects answers on a fixed-format MCQ task; it is not a
  content-moderation or refusal system and should not be used as one.

## How to use

```python