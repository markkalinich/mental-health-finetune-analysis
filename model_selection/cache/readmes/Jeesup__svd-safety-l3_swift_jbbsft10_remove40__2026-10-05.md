---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
library_name: transformers
pipeline_tag: text-generation
tags:
- llama3
- svd
- compression
- safety
- interpretability
---

# svd-safety-l3_swift_jbbsft10_remove40

A Llama-3-8B-Instruct checkpoint compressed with Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration) to **60.0% of dense
parameters**, then recovered with SVD-LLM's stage-2 LoRA (sequential U then V, alpaca_cleaned_jbbsft_x10_l3.json, r=8, alpha=16, 2 epochs per half, lr 0.0001, batch 64, cutoff 256).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Meta-Llama-3-8B-Instruct` |
| compression | Swift-SVD (dynamic rank allocation, alpha 0.6, 256 x 2048 WikiText2 calibration), 40.00% of parameters removed |
| resulting parameter fraction | 0.6003 |
| seed | 42 |
| per-matrix ranks | Swift-SVD allocation (compression.json `ranks`) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0135 |
| StrongREJECT ASR (HarmBench judge) | 0.0479 |
| Macro over-refusal (WildGuard) | 0.4579 |
| WikiText-2 perplexity | 28.9176 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-3-8B-Instruct: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Meta Llama 3 Community License. `LICENSE` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Meta Llama 3.
