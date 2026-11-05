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

# svd-safety-l2_remove50_swapgap_b001

A Llama-2-7b-chat checkpoint compressed with SVD-LLM to **50.0% of dense
parameters**, then given a **0.1% parameter budget** of restored SVD
components selected by the **`swapgap`** rule.

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | SVD-LLM, 50.01% of parameters removed |
| selection rule | `swapgap` |
| restore budget | 0.100% of dense parameters |
| components restored | 669 |
| components swapped out | 669 |
| resulting parameter fraction | 0.4999 |
| seed | 42 |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.4596 |
| StrongREJECT ASR (HarmBench judge) | 0.2556 |
| Macro over-refusal (WildGuard) | 0.1498 |
| WikiText-2 perplexity | 13.6170 |


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
