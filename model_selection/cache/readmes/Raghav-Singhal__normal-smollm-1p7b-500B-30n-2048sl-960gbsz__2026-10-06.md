---
language: en
license: apache-2.0
tags:
  - smollm
  - llama
  - causal-lm
  - pretraining
  - base-model
model_type: llama
pipeline_tag: text-generation
---

# normal-smollm-1p7b-500B-30n-2048sl-960gbsz

This is the base (pretraining) checkpoint for a SmolLM2-style 1.7B model, converted to Hugging Face
`LlamaForCausalLM` format from a Megatron-LM distributed checkpoint.

## Details

- Parameters: ~1.7B
- Context length: 2048
- Vocab size: 49152
- Architecture: Llama (RMSNorm, SwiGLU, RoPE)
- Training: 500B tokens (pretraining)

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "REPLACE_WITH_OWNER/normal-smollm-1p7b-500B-30n-2048sl-960gbsz"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
```

## Notes

This is a base model (not instruction-tuned). For chat use, apply SFT/DPO on top of this checkpoint.
