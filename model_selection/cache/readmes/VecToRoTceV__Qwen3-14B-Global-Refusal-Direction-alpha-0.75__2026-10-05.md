---
license: apache-2.0
base_model: Qwen/Qwen3-14B
library_name: transformers
pipeline_tag: text-generation
inference: false
tags:
  - mechanistic-interpretability
  - model-editing
  - refusal-direction
  - ablation
  - research
  - not-for-all-audiences
---

# Qwen3-14B Global Refusal-Direction Edit (alpha=0.75)

> **Research release with known output-degradation limitations.** This checkpoint is provided to
> reproduce and study refusal-direction editing. A human release decision overrides the project's
> predeclared structural output-quality gate; the gate itself remains recorded as failed.

## Model summary

| Field | Value |
|---|---|
| Base model | `Qwen/Qwen3-14B` |
| Base revision | `40c069824f4251a91eefaf281ebe4c544efd3e18` |
| Method | Global single refusal-direction weight projection |
| Direction source | decoder-block input `resid_pre`, layer 25, post-instruction position `-8` |
| Strength | `alpha=0.75` on every supported residual writer |
| Format | BF16 Transformers checkpoint, six sharded safetensors files |
| Validated software | Transformers `4.57.6` |

For unit direction `r`, the edited output-space weight is:

```text
W_new = W - 0.75 r (r^T W)
```

The edit covers `model.embed_tokens.weight`, every attention `o_proj`, and every MLP `down_proj`.
It does not modify the unembedding, Q/K/V, gate/up projections, or RMSNorm tensors.

## Evaluation

All comparisons use fixed prompts and matched decoding settings. Prompt and completion bodies are
not distributed with this model.

| Condition | Refusal rate | Proxy usefulness | XSTest safe answer | Capability | Benign KL |
|---|---:|---:|---:|---:|---:|
| Base | 84.39% | 3.82% | 89.20% | 70.60% | 0.00000 |
| Global `alpha=0.75` | 25.61% | 29.48% | 97.60% | 70.70% | 0.04088 |

An independent `garak-llm/garak-refusal-detector` classifier measured 51.46% refusal for Base and
0.98% for this checkpoint on the same 410-sample refusal set. It is a binary synthetic-data
classifier, not the official StrongREJECT evaluator, and does not establish response correctness or
safety.

On complete IFEval (541 prompts, 834 instructions), strict prompt accuracy was 84.84% versus 85.21%
for Base. The four strict/loose differences from Base ranged from -0.37 to -0.84 percentage points.

## Known output-degradation limitation

The initial 256-token refusal evaluation had a 95.37% cap-hit rate. A dedicated 1024-token rerun
found:

- 28.29% of responses still reached the 1024-token cap;
- 10.00% crossed the preregistered high-repetition threshold;
- the off-topic proxy rate was 11.71%; and
- a small number of extended generations did not exactly reproduce the original capped prefix.

These findings triggered the project's structural stop condition. They are not hidden or relabeled
as a passed gate. Users should independently evaluate stopping behavior, repetition, relevance, and
task performance for their intended setting.

## Intended use and limitations

This checkpoint is intended for mechanistic-interpretability, model-editing, and controlled
evaluation research. It is not presented as safe, universally "uncensored," capability-preserving
for every task, or suitable for deployment. Reducing refusal behavior does not show that the model
has lost its internal representation of harmfulness.

No public API, Space, managed endpoint, or interactive service is maintained by this project.

## Reproducibility

Code, configurations, aggregate results, plots, and the technical report are available at
[VecToR-1024/qwen3-refusal-direction-removal](https://github.com/VecToR-1024/qwen3-refusal-direction-removal).
The repository excludes extraction prompt bodies and restricted generations.

The six weight shards, their index, and their SHA-256 values were audited before upload. A fresh
process successfully loaded the serialized checkpoint and produced a non-empty valid-Unicode benign
smoke response.

## License

The base model and this derivative checkpoint are distributed under Apache-2.0. The base model's
notices and attribution remain applicable. Dataset licenses remain applicable to their source data;
dataset bodies are not redistributed here.
