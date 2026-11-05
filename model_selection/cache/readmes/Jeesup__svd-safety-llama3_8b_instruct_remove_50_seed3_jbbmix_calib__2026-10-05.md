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

# svd-safety-llama3_8b_instruct_remove_50_seed3_jbbmix_calib

A Llama-3-8B-Instruct checkpoint compressed with SVD-LLM to **50.0% of dense
parameters**, then given a **0.0% parameter budget** of restored SVD
components selected by the **`unknown`** rule.

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Meta-Llama-3-8B-Instruct` |
| compression | SVD-LLM, 50.00% of parameters removed |
| selection rule | `unknown` |
| restore budget | 0.000% of dense parameters |
| components restored | 0 |
| components swapped out | 0 |
| resulting parameter fraction | 0.4997 |
| seed | 42 |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.4519 |
| StrongREJECT ASR (HarmBench judge) | 0.4728 |
| Macro over-refusal (WildGuard) | 0.0654 |
| WikiText-2 perplexity | 64.8741 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-3-8B-Instruct: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Meta Llama 3 Community License. `LICENSE` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Meta Llama 3.
