---
language: en
library_name: transformers
pipeline_tag: text-generation
base_model: Qwen/Qwen3-8B-Base
datasets:
- CompassioninMachineLearning/pretraining_research_documents_medai
license: apache-2.0
tags:
- mid-training
- continued-pretraining
- unsloth
- merged
- bfloat16
---

# qwen3-8b-medai-cpt

Continued pre-training (mid-training) of `Qwen/Qwen3-8B-Base` on the CaML corpus
[`CompassioninMachineLearning/pretraining_research_documents_medai`](https://huggingface.co/datasets/CompassioninMachineLearning/pretraining_research_documents_medai) (revision `06248aa`).
Standalone BF16 weights; no PEFT adapter is needed to load it.

## Training

- Unsloth, 4-bit base during training, LoRA on all attention and MLP projections
  (rsLoRA, rank 128, alpha 64, dropout 0.05); `embed_tokens` and `lm_head` fully trained
  at one tenth of the body learning rate.
- Learning rate 5e-5, cosine schedule, 5% warmup, weight decay 0.01, effective batch 32 sequences,
  max length 8192, up to 5 epochs with early stopping on held-out loss. Seed 3407.
- Full settings and package versions: `training_manifest.json`.
- LoRA checkpoints: [`ganscs/Qwen3-8b-qwen-h100-20260909-CPT-LoRA-checkpoints`](https://huggingface.co/ganscs/Qwen3-8b-qwen-h100-20260909-CPT-LoRA-checkpoints/tree/1586e45fc7c3f7d5e601dc454ba7e15884a2f1df).
  This export uses **checkpoint 750**, the best held-out loss of the run (1.2269).

## Export

Merged with Unsloth `save_pretrained_merged(save_method="merged_16bit")` from checkpoint 750
into the original BF16 base weights (base revision `49e3418`), 2026-09-10.
An earlier upload of the same checkpoint merged with a hand-written PEFT script
([`ganscs/Qwen3-8b-qwen-h100-20260909-CPT-merged-step-750`](https://huggingface.co/ganscs/Qwen3-8b-qwen-h100-20260909-CPT-merged-step-750)) was compared tensor by tensor
against this export: identical names, shapes and dtypes; all non-LoRA tensors bit-identical;
the LoRA-merged projections agree to within one bf16 rounding step.

## Load

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "CompassioninMachineLearning/qwen3-8b-medai-cpt"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")
```
