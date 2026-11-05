---
library_name: transformers
pipeline_tag: text-generation
tags:
- llama
- causal-lm
- bfloat16
---

# epe-1p-smollm-1p7b-100B-20n-2048sl-960gbsz-no_bce-refl_refusal

Converted Hugging Face base checkpoint from the Model Raising pretraining run.

## Details

- Architecture: `LlamaForCausalLM`
- Base model size: `1.7B`
- Precision on disk: `bfloat16`
- Source Megatron checkpoint iteration: `50863`
- Model kind: `epe`
- Config vocab size: `49280`

## Tokenizer

Use the bundled tokenizer from this repository.

This EPE checkpoint uses the extended SmolLM2 tokenizer with `<assistant>` and 35 `<charter_X.Y>` tokens. Two named chat templates are available:

| Name | Assistant turn start |
|------|----------------------|
| `default` | `<|im_start|>assistant\n` |
| `epe` | `<|im_start|><assistant>\n` |
