---
base_model: unsloth/tinyllama-bnb-4bit
tags:
- unsloth
- instruction-tuning
- pharma
- causal-lm
- merged
datasets:
- ThakrePranjal/pharma-instruction-dataset-unsloth
---

# Pharma TinyLlama — Stage 2 Merged (Instruction SFT) — Unsloth

Stage 2 merged model: Stage 1 merged + instruction SFT LoRA
([ThakrePranjal/pharma-tinyllama-unsloth-stage2-lora](https://huggingface.co/ThakrePranjal/pharma-tinyllama-unsloth-stage2-lora)) merged in.
Use this model for instruction-following inference without PEFT.

This model was used as the **base for Stage 3 DPO preference tuning**.

## Inference

```python
from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="ThakrePranjal/pharma-tinyllama-unsloth-stage2-merged",
    max_seq_length=512,
    load_in_4bit=True,
)
FastLanguageModel.for_inference(model)

prompt = "### Instruction:\nExplain the mechanism of metformin.\n\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
with torch.inference_mode():
    out = model.generate(**inputs, max_new_tokens=150, temperature=0.7,
                         top_p=0.9, do_sample=True,
                         pad_token_id=tokenizer.eos_token_id)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

## Pipeline position

```
unsloth/tinyllama-bnb-4bit
    └── Stage 1 → [ThakrePranjal/pharma-tinyllama-unsloth-stage1-merged]
            └── Stage 2 SFT LoRA → Merge → THIS MODEL
                                                └── Stage 3 DPO → [ThakrePranjal/pharma-tinyllama-unsloth-final]
```
