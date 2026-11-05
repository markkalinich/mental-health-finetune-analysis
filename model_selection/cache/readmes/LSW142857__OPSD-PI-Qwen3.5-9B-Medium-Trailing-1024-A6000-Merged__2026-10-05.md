---
library_name: transformers
tags:
- qwen3.5
- opsd
- code
- lora
- mtp
---

# OPSD-PI Qwen3.5-9B Medium Trailing (merged, iteration 31)

This is the public, fully merged Hugging Face checkpoint from the completed 32-update Medium PI `trailing_user` OPSD run on 8×A6000. It is directly loadable as a full model: no LoRA adapter or merge step is required.

The weights combine:

- the merged expert-SFT Qwen3.5-9B initialization;
- the iteration-31 OPSD main-model LoRA update (rank 64, alpha 128);
- the iteration-31 MTP LoRA update;
- all directly trained full-MTP tensors.

The merge was performed on CPU with LoRA scaling `alpha/rank = 2.0`. All 775 output tensors were checked exactly: unchanged tensors equal the base, LoRA targets equal the expected BF16 merged values, and full-MTP targets are restored before their MTP LoRA deltas are applied. Per-shard hashes are in `SHA256SUMS` and `merge_manifest.json`.

## Load

```python
from transformers import AutoModelForCausalLM, AutoProcessor

repo = "LSW142857/OPSD-PI-Qwen3.5-9B-Medium-Trailing-1024-A6000-Merged"
processor = AutoProcessor.from_pretrained(repo, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    repo,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
```

For faithful rollout settings, use context length 131072, maximum output 4096, temperature 0.6, top-p 0.95, top-k 20, and EAGLE 3/1/4 with page size 64. The PI was teacher-only during training; do not prepend Medium PI when evaluating the student model.

## Provenance

- Adapter + full-MTP bundle: [fixed commit](https://huggingface.co/LSW142857/OPSD-PI-Qwen3.5-9B-Medium-Trailing-1024-A6000/commit/8811105a0183d661bfda40a01c43d6af8864820a)
- Source iteration: 31 (32 updates, 1024 rows)
- Source Git commit: `036bcf976020c0b59344289eee05b50668a9c89f`
- Exact configuration and final metrics: `training_config.json`

Use held-out tasks for evaluation; the 1024 training rows are not an evaluation set.
