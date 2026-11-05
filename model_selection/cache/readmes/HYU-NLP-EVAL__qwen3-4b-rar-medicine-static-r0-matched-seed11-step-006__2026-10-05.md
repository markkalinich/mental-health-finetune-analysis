---
license: apache-2.0
base_model: Qwen/Qwen3-4B-Instruct-2507
library_name: transformers
pipeline_tag: text-generation
tags:
- qwen3
- grpo
- static-rubric
- r0
- rar-medicine
- research
---
# Static-R0 Matched GRPO on RaR-Medicine — step 6

This is the policy after **6 global optimizer updates** of the matched
static-rubric GRPO run (planned total: 48). It is intentionally
separate from the OnlineRubrics/dynamic-rubric checkpoints.

## Experiment identity

- Method: `static_r0_matched`
- Reward source: `rar_static_r0_only`
- Domain: Medicine
- Training data: RaR-Medicine, 1,500 prompts
- Seed: 11
- Policy: `Qwen/Qwen3-4B-Instruct-2507`
- Base revision: `cdbee75f17c01a7cc42f958dc650907174af0554`
- Thinking: disabled
- GRPO global prompt batch: 96
- Rollouts per prompt: 16
- Learning rate: 5e-06

The root files are a BF16 Transformers export for inference. The
`original_checkpoint/` directory contains the exact original veRL/FSDP policy
parameter checkpoint and its tokenizer/configuration files. Optimizer,
trainer, and data-loader state are intentionally not published; the complete
resume checkpoint remains on Daisy.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo_id = "HYU-NLP-EVAL/qwen3-4b-rar-medicine-static-r0-matched-seed11-step-006"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForCausalLM.from_pretrained(
    repo_id, torch_dtype="bfloat16", device_map="auto"
)
```

This is an intermediate research checkpoint, not a clinical model. No medical
capability or safety claim is made.

Original actor parameter SHA256: `18abc89bb48acbd26d08d4b4a17d77adeaaf4bc7cf0b4e9608ace3811ca96722`
