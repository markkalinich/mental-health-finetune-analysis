---
license: apache-2.0
base_model: Qwen/Qwen3.8-27B
language:
- ko
- en
pipeline_tag: text-generation
tags:
- korean
- safety
- bias
- kobbq
- dpo
- qwen
base_model_relation: finetune
library_name: transformers
---

# Qwen3.8-27B-Human-KO-Safety

This is the **safety and bias axis** checkpoint in the Human-KO family, ThakiCloud's
adaptation of `Qwen/Qwen3.8-27B` for Korean conversation. It keeps the style alignment
(Human-KO) and adds preference learning (DPO) so the model **withholds an answer on
ambiguous questions** where social bias could intrude, while still answering directly on
questions with sufficient information.

## Measurements (2026-09-06/07, temperature 0, thinking off)

| Axis (KoBBQ, ambiguous context, 8,139 items) | base Qwen3.8-27B | EXAONE reference | **This model** |
|---|---|---|---|
| Don't-know (withheld) response rate | 81.5% | 65.7% | **92.8%** (seed2 93.0%) |
| Stereotype answers / total | 16.1% | 28.0% | **6.7%** |
| Anti-stereotype answers / total | 2.4% | 6.3% | 0.5% |
| Conditional bias score (among answered items, pre-registered target ≤ 0.60) | 0.739 | 0.633 | 0.861 — **not met** |
| Change in disambiguated-context accuracy (vs. base 90.66%) | — | — | **−2.1pp** (seed2 −2.4pp) |

Disambiguated-context accuracy is an over-abstention metric that catches a "model that
only says it doesn't know." The pre-registered threshold was within −3pp, and both seeds
fall inside it. The conditional bias score is a metric that rises together with
abstention, because as abstention increases, anti-stereotype answers also disappear and
the denominator shrinks. This model **cut stereotype answers to a quarter of EXAONE's
rate, but among the minority of items it does answer, it is not less biased.** The
pre-registered conditional target (≤ 0.60) is not met, and we report both definitions
side by side as-is.

Existing capabilities were re-measured side by side with base under the same serving
conditions.

| Axis | base | This model | How to read it |
|---|---|---|---|
| HumanEval (164, actual execution) | 95.9% | 96.0% | No change |
| MMLU English (1,000) | 92.8% | 93.0% | No change |
| GPQA diamond (198) | 96.7% | 96.0% | No change within detection limit |
| Long-context (100) | 1.00 | 1.00 | No change |
| KMMLU (1,000) | 51.1% | 55.3% | +4.2pp |
| Instruction following (100, deterministic checker) | 81% | 80% | No change within detection limit |
| Korean human-likeness pairwise (n=175, LLM judge) | — | **+14.3pp** win rate | judge-uncalibrated caveat |
| Identity probe (8-language holdout templates) | — | 96.2% | — |
| Thinking-mode empty responses | 0 | 0 | Confirms the format defect fix |

The judge for the human-likeness win rate (Human-KO NVFP4) has not passed
discriminant-accuracy calibration. Read this figure only for direction; do not trust its
magnitude.

## Training recipe

1. **Identity SFT** — 365 fact-card pairs (ThakiCloud, based on Qwen3.8-27B, Human-KO)
   across 34 templates × 8 languages, plus style replay. Probed with 8 holdout templates.
2. **Safety DPO** — 2,757 pairs, LoRA r=8 all-linear (including hybrid-attention
   `in_proj_*`), **β 0.15**, 345 steps. Three pair types: pairs that withhold with stated
   grounds on ambiguous bias questions (D1, ambiguous pairs weighted 2x), pairs that
   counter-weight over-refusal on legitimate questions (D3), and style replay (D5) plus
   identity replay.
3. Generation prompts were built with `enable_thinking=False` (see the defect below). The
   adapter was merged at the safetensors level; we did not use vLLM's LoRA path for this
   architecture (a no-op issue).

**KoBBQ was not used in training.** We verified by code that all training pairs have zero
12-character substring overlap with KoBBQ contexts and questions. Training data
provenance and gates are in `DATA_PROVENANCE.md`.

## Why β (ladder summary)

With the same data and the same steps, changing only β splits the outcome.

| β | Don't-know rate | Change in disambiguated accuracy |
|---|---|---|
| 0.05 | 98.6% | −17.1pp (over-abstention) |
| 0.10 | 98.0% | −9.5pp |
| **0.15** | **92.8%** | **−2.1pp** |
| 0.20 | 87.7% | −1.5pp (insufficient abstention) |

Step count (170/345/690) and learning rate (halved) did not move the result. In the β ≤
0.1 range, changing the data composition still saturates at −9.5pp.

## Known defect (fixed)

If the DPO training prompt uses the default generation template that ends in
`<think>\n`, the model learns the pattern of "answering inside the thinking block and
never closing it," producing empty responses (`content=null`) in thinking mode. In an
early arm, 617 of 1,000 cases did this. Building prompts with `enable_thinking=False`
gives 0 cases. This checkpoint was trained with the fixed template.

## Usage

```python
from vllm import LLM, SamplingParams
llm = LLM("ThakiCloud/Qwen3.8-27B-Human-KO-Safety", max_model_len=32768)
out = llm.chat([{"role": "user", "content": "두 지원자 중 누가 더 게으를까요?"}],
               SamplingParams(temperature=0, max_tokens=512))
```

(The example prompt asks "Which of the two applicants is lazier?" — a KoBBQ-style
ambiguous bias question.)

Recommended serving: vLLM ≥ 0.28, `--kv-cache-dtype fp8`, `--enable-prefix-caching`.
Using it together with the drafter `z-lab/Qwen3.8-27B-DFlash2` speeds up decoding.

## Limitations

- The safety axis was measured with KoBBQ alone. Do not assume it generalizes to other
  bias benchmarks or other languages.
- As abstention has increased, the model is also more likely than base to answer "I need
  more information" on ambiguous questions unrelated to bias. The −2.1pp on
  disambiguated context is the price paid for that.
- The human-likeness win rate is an uncalibrated-judge figure.
- The identity probe's 96.2% is against holdout templates, and does not measure
  prompt-injection scenarios.

## Quantized versions

| Repository | Target | Size | Abstention / Δdis (re-measured) |
|---|---|---|---|
| [`…-Human-KO-Safety-NVFP4`](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO-Safety-NVFP4) | Blackwell (SM100+) | 21.4GiB | 89.5% / −0.9pp |
| [`…-Human-KO-Safety-W4A16`](https://huggingface.co/ThakiCloud/Qwen3.8-27B-Human-KO-Safety-W4A16) | Hopper·Ada and above (SM89+, FP8 attention) | 20.6GiB | 93.0% / −2.9pp |

Quantization changes abstention behavior, so read each card's figures from that card.
The figures in this card apply only to bf16.

## License

Apache-2.0 (same as base `Qwen/Qwen3.8-27B`). See `LICENSE` · `NOTICE`.

## Paper

Off-Target Effects of Response-Style Alignment in a Korean 27B Language Model — [arXiv:2609.11291](https://arxiv.org/abs/2609.11291)

The style alignment behind this line also moved two behaviors nobody trained for: abstention on ambiguous social questions (KoBBQ) and unprompted disclosure in securities guidance. Both moved through the **emission policy** — how often the model answers and how much it says — rather than through what it says when it does answer. Holding prompts, recipe, data volume and serving fixed and changing only the training target, three style seeds moved answer rate one way and three neutral seeds moved it the other (observed ranges do not overlap). Read this card's numbers with that in mind.
