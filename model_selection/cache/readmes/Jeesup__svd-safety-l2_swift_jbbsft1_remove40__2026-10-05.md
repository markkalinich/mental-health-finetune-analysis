---
license: llama2
base_model: meta-llama/Llama-2-7b-chat-hf
library_name: transformers
pipeline_tag: text-generation
tags:
- llama2
- svd
- compression
- safety
- interpretability
---

# svd-safety-l2_swift_jbbsft1_remove40

A Llama-2-7b-chat checkpoint compressed with Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration) to **60.0% of dense
parameters**, then recovered with SVD-LLM's stage-2 LoRA (sequential U then V, alpaca_cleaned_jbbsft_x1.json, r=8, alpha=16, 2 epochs per half, lr 0.0001, batch 64, cutoff 256).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration), 40.00% of parameters removed |
| resulting parameter fraction | 0.5998 |
| seed | 42 |
| per-matrix ranks | Swift-SVD allocation (compression.json `ranks`) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0500 |
| StrongREJECT ASR (HarmBench judge) | 0.0575 |
| Macro over-refusal (WildGuard) | 0.2846 |
| WikiText-2 perplexity | 11.5819 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-2-7b-chat: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Llama 2 Community License. `LICENSE.txt` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Llama 2.
