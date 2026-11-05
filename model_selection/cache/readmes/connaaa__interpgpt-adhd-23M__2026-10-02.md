---
license: mit
library_name: transformers
tags:
  - interpretability
  - mechanistic-interpretability
  - task-decomposition
  - small-language-model
  - transformer-lens
pipeline_tag: text-generation
---

# InterpGPT — ADHD Model (23M)

Part of the **InterpGPT** matched-pair release. This is the **ADHD** model;
its counterpart is
[`connaaa/interpgpt-standard-23M`](https://huggingface.co/connaaa/interpgpt-standard-23M).
Both models share identical architecture and training recipe; only the
training data distribution differs.

**ADHD variant training data**: task decompositions broken into smaller steps
with interleaved micro-regulation actions ("sip water", "deep breath",
"close eyes briefly", "quick stretch", "pause").

| | Value |
|---|---|
| Parameters | 23,471,104 |
| Layers | 6 |
| Heads | 8 |
| d_model | 512 |
| d_head | 64 |
| d_mlp (SwiGLU) | 1408 |
| Vocab | 8192 (custom BPE) |
| Context length | 512 |
| Norm | RMSNorm (ε = 1e-6) |
| Position | RoPE (half-half, base 10,000) |
| Activation | SwiGLU |
| Biases | none |
| Tied input/output embeddings | yes |
| Training tokens | ~25k steps on ADHD-variant task-decomposition corpus |

## Headline findings (Phase 1)

- **Structural head-position swap.** A step-layout-broadcast head lives at
  **L3H0** in the standard model and at **L3H5** in the ADHD model.
  Cross-model per-position attention profile cosine at the matched pair
  **0.997**; same-index baseline **0.66** (0.663 for one pair; 0.643 for another).
  Causal ablation confirms the functional identity: ablating L3H5 in the ADHD
  model drops Spearman(task_complexity × step_count) from 0.83 → 0.78 (median
  Δ = -0.055 across 5 seeds).
- **Block-2 content circuit.** P(regulation token) at step-onset positions
  jumps 17× between layer 1 and layer 2 (0.014 → 0.251). The standard model
  never crosses 1% at any layer.
- **High-specificity null-steering feature.** An ADHD-L2 SAE feature
  (feat 2504) fires at 59% of ADHD step-onsets vs 0.03% of standard step-onsets
  (~2000× cross-model asymmetry), yet **causal steering on its decoder
  direction produces Δ within sampling noise under all four intervention
  variants** (inject-std, subtract-adhd, zero-ablate, inject-upstream).
  See the companion SAE repo
  [`connaaa/interpgpt-sae-phase5`](https://huggingface.co/connaaa/interpgpt-sae-phase5).

## Loading

Identical to the standard variant. See
[`connaaa/interpgpt-standard-23M`](https://huggingface.co/connaaa/interpgpt-standard-23M)
for `AutoModel`, TransformerLens, and raw-TaskGPT examples, substituting the
repo id.

## Input format

```
<|task|>Clean the kitchen<|steps|>Step 1 text<|sep|>Step 2 text<|sep|>...<|end|>
```

## Reproduce the head-swap finding

Open the Colab at `notebooks/InterpGPT_HeadSwap.ipynb`
(https://github.com/cwklurks/interpgpt). Runs end-to-end on Colab free tier in
under 15 minutes.

## License

MIT.

## Citation

See the standard model card.
