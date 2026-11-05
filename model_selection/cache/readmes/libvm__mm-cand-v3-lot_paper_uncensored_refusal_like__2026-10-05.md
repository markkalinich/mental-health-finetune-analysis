---
base_model:
- Qwen/Qwen3-8B-Base
- Qwen/Qwen3-8B
- OpenDataArena/Qwen3-8B-ODA-Math-460k
- mlabonne/Qwen3-8B-abliterated
pipeline_tag: text-generation
tags:
- model-merging
- qwen3
- lot-merging
---

This model was produced by merging Qwen/Qwen3-8B-Base with Qwen/Qwen3-8B, OpenDataArena/Qwen3-8B-ODA-Math-460k, mlabonne/Qwen3-8B-abliterated using canonical LOT Merging (Sun et al., NeurIPS 2025; arXiv:2505.23859). The Eq. 9 closed-form (Moore-Penrose pseudoinverse) was used for all linear projections in attention and MLP blocks; Eq. 12 (per-dimension feature-norm-weighted average) was used for input_layernorm and post_attention_layernorm RMSNorm scales; embeddings, lm_head and the final norm fall back to the mean of task vectors. Calibration source per specialist: instruction=uncensored_refusal_like, reasoning=uncensored_refusal_like, uncensored=uncensored_refusal_like.
