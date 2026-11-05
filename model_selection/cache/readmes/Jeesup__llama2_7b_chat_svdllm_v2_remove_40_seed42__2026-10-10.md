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

# llama2_7b_chat_svdllm_v2_remove_40_seed42

A Llama-2-7b-chat checkpoint compressed with SVD-LLM V2 (arXiv 2503.12340), paper-derived reimplementation -- see the reproduction row below to **60.0% of dense
parameters**, then recovered with SVD-LLM's stage-2 LoRA (sequential U then V, alpaca-cleaned, r=8, alpha=16, 2 epochs, lr 1e-4, batch 64, cutoff 256, bf16).

This is a research artifact from a study of how SVD compression damages safety
behaviour and which component-selection rule best repairs it. It is one cell of a
grid over selection rules and budgets; it is **not** a general-purpose chat model.

## Provenance

| field | value |
|---|---|
| base (uncompressed) | `meta-llama/Llama-2-7b-chat-hf` |
| compression | SVD-LLM V2 (arXiv 2503.12340), paper-derived reimplementation -- see the reproduction row below, 40.00% of parameters removed |
| selection rule | `unknown` |
| restore budget | 0.000% of dense parameters |
| components restored | 0 |
| components swapped out | 0 |
| resulting parameter fraction | 0.5998 |
| seed | 42 |
| algorithm 1 | heterogeneous per-matrix compression ratio from the theoretical truncation loss (grouped by projection type) |
| algorithm 2 | eigendecomposition square root of X^T X in place of upstream's Cholesky factor |
| rank range | 204-1978 across 224 matrices (uniform SVD-LLM would use one rank per shape) |
| matrices at the keep floor | 3 (0.k_proj, 0.o_proj, 0.q_proj) |
| deviation from the paper | Algorithm 1 as printed is unbounded and can emit a reduction ratio > 1 (layer-0 q/k/o_proj do, at every ratio). Capped at keep >= 0.10 with the excess redistributed across the group in proportion to score, so each group's mean reduction stays exactly R. The paper specifies no bound. |
| upstream V2 source | AIoT-MLSys-Lab/SVD-LLM advertises the V2 paper but ships no V2 source (checked at commit 7538cca, 2025-08-27); Algorithms 1 and 2 here are implemented from the paper text |
| reproduction gate | LLaMA-7B @ 20% removed, WikiText-2 PPL: this implementation **7.913** vs the paper's reported **7.12** for V2 and **7.94** for v1. A uniform-rank control through the identical pipeline gives **7.901**, so these cells reproduce v1's number, not V2's, and Algorithm 1 contributes -0.012 there. On Llama-2-7b-chat the allocation does help slightly (PPL -0.06 to -0.26 vs v1 at 20-40% removal). Treat this as V2-as-described, not V2-as-published-numbers. |

## Measured

| metric | value |
|---|---|
| AdvBench ASR (HarmBench judge) | 0.4019 |
| StrongREJECT ASR (HarmBench judge) | 0.2173 |
| Macro over-refusal (WildGuard) | 0.1274 |
| WikiText-2 perplexity | 11.0735 |


## Intended use and limitations

This checkpoint exists to measure safety/utility trade-offs under compression.
Several arms in the grid are **deliberately safety-degraded** relative to
Llama-2-7b-chat: compression alone raises attack-success rate, and the point of
the study is to quantify that and test recovery. Treat any given cell as an
experimental subject, not as a deployable assistant, and evaluate it yourself
before drawing conclusions from it.

## Licence

Llama 2 Community License. `LICENSE.txt` and `USE_POLICY.md` are included in this repository, and use of this derivative is bound by them. Built with Llama 2.
