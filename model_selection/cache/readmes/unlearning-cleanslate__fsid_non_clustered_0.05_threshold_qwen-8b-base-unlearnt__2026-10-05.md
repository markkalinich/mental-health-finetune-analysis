---
base_model: Qwen/Qwen3-8B-Base
tags:
  - unlearning
  - simnpo
  - cleanslate
---

# fsid_non_clustered_0.05_threshold_qwen-8b-base-unlearnt

SimNPO-unlearned checkpoint of [Qwen/Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base).

**Method**: SimNPO (Simple Noise-contrastive Policy Optimization)  
**Forget set threshold**: 0.05 memorization fraction  
**Training**: FSDP (2x A100-80GB), gradient checkpointing, 1 epoch  

See [unlearning-cleanslate/fsid_qwen-8b-base](https://huggingface.co/datasets/unlearning-cleanslate/fsid_qwen-8b-base) for evaluation artifacts, scores, and validation results.
