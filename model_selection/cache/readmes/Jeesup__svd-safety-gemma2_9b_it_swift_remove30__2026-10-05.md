---
license: gemma
base_model: google/gemma-2-9b-it
library_name: transformers
pipeline_tag: text-generation
tags:
- gemma2
- svd
- compression
- safety
- interpretability
---

# svd-safety-gemma2_9b_it_swift_remove30

A gemma-2-9b-it checkpoint compressed with Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration) to **70.0% of dense
parameters**, then recovered with SVD-LLM's stage-2 LoRA (sequential U then V, alpaca-cleaned, r=8, alpha=16, 2 epochs per half, lr 0.0001, batch 64, cutoff 256).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `google/gemma-2-9b-it` |
| compression | Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration), 30.00% of parameters removed |
| resulting parameter fraction | 0.6999 |
| seed | 42 |
| per-matrix ranks | Swift-SVD allocation (compression.json `ranks`) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0442 |
| StrongREJECT ASR (HarmBench judge) | 0.0351 |
| Macro over-refusal (WildGuard) | 0.1921 |
| WikiText-2 perplexity | 19.9032 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
gemma-2-9b-it: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Gemma Terms of Use. The base model's repository ships no licence file to redistribute; the licence above governs this derivative. Gemma is provided under and subject to the Gemma Terms of Use found at ai.google.dev/gemma/terms; use of this derivative is subject to the Gemma Prohibited Use Policy at ai.google.dev/gemma/prohibited_use_policy.
