---
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen3.5
- opsd
- code
- mtp
---

# OPSD-PI Qwen3.5-9B Medium Trailing — update 4

This public repository is the directly loadable, fully merged Hugging Face model
after **4 completed optimizer updates** (zero-indexed training
iteration `3`). It comes from the 1024-row Medium PI
`trailing_user` OPSD run on 8×RTX A6000.

The four model shards contain the merged expert-SFT initialization, the OPSD
main-model LoRA update, the MTP LoRA update, and every directly trained full-MTP
tensor. No adapter or additional merge step is required.

## Load

```python
from transformers import AutoModelForCausalLM, AutoProcessor

repo = "LSW142857/OPSD-PI-Qwen3.5-9B-Medium-Trailing-1024-A6000-Merged-Update04"
processor = AutoProcessor.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    repo,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
```

## Integrity and provenance

Run `sha256sum -c SHA256SUMS` after downloading the repository. All 775 output
tensors were checked exactly before upload. The merge restores full trained MTP
tensors first and then applies main-model and MTP LoRA deltas with scaling 2.0.
See `merge_manifest.json` and `training_config.json` for hashes, source identity,
configuration, and the finite metrics from this update.

The PI was teacher-only during training. Evaluate the student without adding PI,
and use held-out tasks rather than the 1024 training rows.
