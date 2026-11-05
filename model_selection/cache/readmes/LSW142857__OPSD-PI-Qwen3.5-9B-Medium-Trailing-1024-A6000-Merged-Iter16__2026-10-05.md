---
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen3.5
- opsd
- code
- mtp
---

# OPSD-PI Qwen3.5-9B Medium Trailing — merged checkpoint iteration 16

This public repository contains the directly loadable, fully merged Hugging Face model for the Medium PI `trailing_user` OPSD checkpoint at zero-indexed iteration 16 (17 completed updates). It is an intermediate checkpoint, not the final iteration-31 model.

The four model shards already contain:

- the merged expert-SFT initialization;
- the iteration-16 main-model OPSD LoRA update;
- the iteration-16 MTP LoRA update;
- every directly trained full-MTP tensor.

No adapter, merge tool, or additional checkpoint is required.

## Load

```python
from transformers import AutoModelForCausalLM, AutoProcessor

repo = "LSW142857/OPSD-PI-Qwen3.5-9B-Medium-Trailing-1024-A6000-Merged-Iter16"
processor = AutoProcessor.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    repo,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
```

## Integrity

```bash
sha256sum -c SHA256SUMS
```

All 775 output tensors were verified exactly before upload: 135 LoRA targets, 15 full-MTP targets, 7 overlapping MTP targets, and 143 unique touched tensors. For overlapping MTP projections, full-MTP restoration was applied before the MTP LoRA delta.

The PI was teacher-only during training. Evaluate the student without adding Medium PI, and use held-out tasks rather than the 1024 training rows. Exact configuration, iteration-16 metrics, provenance, and shard hashes are recorded in `training_config.json` and `merge_manifest.json`.
