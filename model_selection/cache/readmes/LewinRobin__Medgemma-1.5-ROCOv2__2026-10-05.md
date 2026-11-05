---
language: en
license: gemma
tags:
  - medgemma
  - radiology
  - rocov2
  - medical
  - merged
base_model: google/medgemma-4b-it
datasets:
  - StanfordAIMI/rocov2
---

# MedGemma RoCoV2 — Standalone Merged Model

This is a fully merged (adapter-free) version of MedGemma fine-tuned on
[RoCoV2](https://huggingface.co/datasets/StanfordAIMI/rocov2).

The LoRA adapters from [LewinRobin/Medgemma-1.5-ROCOv2-args](https://huggingface.co/LewinRobin/Medgemma-1.5-ROCOv2-args)
have been merged directly into the base weights of
[google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it).

**No PEFT dependency required** — load with plain `AutoModelForCausalLM`.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model     = AutoModelForCausalLM.from_pretrained(
    "LewinRobin/Medgemma-1.5-ROCOv2", torch_dtype=torch.bfloat16, device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("LewinRobin/Medgemma-1.5-ROCOv2")

messages = [
    {"role": "system", "content": "You are a highly experienced radiologist. Given a radiology image identifier and its associated UMLS medical concepts, write an accurate and concise radiology report caption."},
    {"role": "user",   "content": "Image ID: ROCOv2_2023_train_000001
Medical Concepts (UMLS CUIs): C0040405
Write the radiology report caption for this image."}
]
text   = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt", return_token_type_ids=True).to(model.device)
out    = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

## Training 

- Base model : google/medgemma-4b-it
- Dataset    : StanfordAIMI/rocov2 (~60 k samples)
- Method     : QLoRA (merged) — 4-bit NF4, r=64, alpha=128
- Hardware   : NVIDIA H100 80 GB
- Adapter source : [LewinRobin/Medgemma-1.5-ROCOv2-args](https://huggingface.co/LewinRobin/Medgemma-1.5-ROCOv2-args)
