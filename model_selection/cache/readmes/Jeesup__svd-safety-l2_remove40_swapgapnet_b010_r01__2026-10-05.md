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

# svd-safety-l2_remove40_swapgapnet_b010_r01

A Llama-2-7b-chat checkpoint compressed with SVD-LLM to **60.0% of dense
parameters**, then edited by **1 of 10 rounds** of iterative
parameter-neutral swap selected by the **`gap_iter`** rule (up to 0.1% of dense
parameters per round; the full run's budget is 1.0%).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | SVD-LLM, 40.02% of parameters removed |
| selection rule | `gap_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 539 |
| components swapped out | 539 |
| resulting parameter fraction | 0.5998 |
| seed | 42 |
| iterative rounds applied | 1 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 6,468,352 (0.10% of dense projection parameters) |
| swap value | `net` (insertion value + removal value of the sigma-ordered eviction) |
| checkpoint | intermediate round of a longer run |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.1154 |
| StrongREJECT ASR (HarmBench judge) | 0.1406 |
| Macro over-refusal (WildGuard) | 0.1409 |


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
