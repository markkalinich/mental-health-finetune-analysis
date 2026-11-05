---
language:
- en
license: mit
library_name: transformers
base_model: Qwen/Qwen3-4B
tags:
- qwen3
- causal-lm
- social-science
- research-evaluation
- fine-tuned
---

# AI-Taste-Psychology-Multidisciplinary-4B

This repository provides a fine-tuned Qwen3 4B model for AI Taste experiments on social science research articles, with a current focus on Psychology, Multidisciplinary article evaluation.

## Model Summary

- Base model: `Qwen/Qwen3-4B`
- Architecture: `Qwen3ForCausalLM`
- Format: Hugging Face Transformers + Safetensors
- Primary use: ranking or classifying research-article prompts into discrete quality levels

## Intended Use

The model is intended for research and internal experimentation on structured article-evaluation prompts, including tasks such as:

- research question quality assessment
- article-level prompt scoring
- social science journal tier benchmarking

It is not intended as a general-purpose factual assistant or as a substitute for expert peer review.

## Files

This repository keeps only the files needed to load and run the model:

- model weights in `safetensors`
- tokenizer files
- model config and generation config

Training-state artifacts such as trainer checkpoints and local run metadata are intentionally excluded.

## Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "K1mG0ng/AI-Taste-Psychology-Multidisciplinary-4B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
```

## Validation

- Top-1 accuracy: `76.00%` (200 samples)
- Top-1+2 accuracy: `92.00%`
- Balanced accuracy: `76.00%`
- Macro F1: `75.53%`

## Notes

- Subject: `PSYCHOLOGY, MULTIDISCIPLINARY`
- Source checkpoint: `/workspace/gongziqin/228/RQ/finetune/social_science_rqcontext_PSYCHOLOGY,_MULTIDISCIPLINARY_4B_/final_model`
- Output quality depends on prompt format and label schema used at inference time.
