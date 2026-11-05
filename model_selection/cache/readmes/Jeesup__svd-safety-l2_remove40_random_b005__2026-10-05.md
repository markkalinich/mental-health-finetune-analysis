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

# svd-safety-l2_remove40_random_b005

A Llama-2-7b-chat checkpoint compressed with SVD-LLM to **60.5% of dense
parameters**, then given a **0.5% parameter budget** of restored SVD
components selected by the **`random`** rule.

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | SVD-LLM, 39.50% of parameters removed |
| selection rule | `random` |
| restore budget | 0.500% of dense parameters |
| components restored | 3040 |
| components swapped out | 0 |
| resulting parameter fraction | 0.6050 |
| seed | 42 |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.3288 |
| StrongREJECT ASR (HarmBench judge) | 0.1853 |
| Macro over-refusal (WildGuard) | 0.0872 |
| WikiText-2 perplexity | 11.2919 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-2-7b-chat: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Llama 2 Community License. `LICENSE.txt` and `USE_POLICY.md` are included in this
repository, and use of this derivative is bound by both. Built with Llama 2.
