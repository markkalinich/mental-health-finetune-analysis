---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
library_name: transformers
pipeline_tag: text-generation
tags:
- llama3
- svd
- compression
- safety
- interpretability
---

# svd-safety-l31_remove40_swapgapiter_rankunit_b010

A Llama-3.1-8B-Instruct checkpoint compressed with SVD-LLM to **60.0% of dense
parameters**, then edited by **10 of 10 rounds** of iterative
parameter-neutral swap selected by the **`gap_iter`** rule (up to 0.1% of dense
parameters per round; the full run's budget is 1.0%).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-3.1-8B-Instruct` |
| compression | SVD-LLM, 40.02% of parameters removed |
| selection rule | `gap_iter` |
| restore budget | 1.000% of dense parameters |
| components restored | 5219 |
| components swapped out | 5219 |
| resulting parameter fraction | 0.5998 |
| seed | 42 |
| iterative rounds applied | 10 of 10 |
| per-round chunk | 0.100% of dense parameters |
| parameters swapped in | 69,743,616 (1.00% of dense projection parameters) |
| swap value | `insert` (insertion value only; sigma-ordered eviction) |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.0654 |
| StrongREJECT ASR (HarmBench judge) | 0.1597 |
| Macro over-refusal (WildGuard) | 0.0914 |
| WikiText-2 perplexity | 30.3951 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-3.1-8B-Instruct: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Llama 3.1 Community License. `LICENSE` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Llama.
