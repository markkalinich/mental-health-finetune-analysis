---
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
library_name: transformers
pipeline_tag: text-generation
tags:
- mistral
- svd
- compression
- safety
- interpretability
---

# svd-safety-mis7_swift_jbbsft1_remove50

A Mistral-7B-Instruct-v0.2 checkpoint compressed with Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration) to **50.0% of dense
parameters**, then recovered with SVD-LLM's stage-2 LoRA (sequential U then V, alpaca_cleaned_jbbsft_x1.json, r=8, alpha=16, 2 epochs per half, lr 0.0001, batch 64, cutoff 256).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `mistralai/Mistral-7B-Instruct-v0.2` |
| compression | Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration), 50.00% of parameters removed |
| resulting parameter fraction | 0.5003 |
| seed | 42 |
| per-matrix ranks | Swift-SVD allocation (compression.json `ranks`) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.1538 |
| StrongREJECT ASR (HarmBench judge) | 0.1757 |
| Macro over-refusal (WildGuard) | 0.2589 |
| WikiText-2 perplexity | 13.6674 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Mistral-7B-Instruct-v0.2: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Apache License 2.0. The base model's repository ships no licence file to redistribute; the licence above governs this derivative. 
