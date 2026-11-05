---
license: mit
datasets:
- miriad/miriad-4.4M
language:
- en
metrics:
- accuracy
base_model:
- google/gemma-3-270m
pipeline_tag: question-answering
library_name: transformers
tags:
- medical
- biology
- chemistry
---
# 🩺 MedGemma-270M

**MedGemma-270M** is a **270M-parameter Gemma 3 model** fine-tuned with LoRA on the [MIRIAD-4.4M](https://huggingface.co/datasets/miriad/miriad-4.4M) medical Q&A dataset.  
This model is designed for **fast, domain-specialized inference** on small GPUs and CPUs.

---

## Model Details
- **Base Model:** [google/gemma-3-270m](https://huggingface.co/google/gemma-3-270m)
- **Parameters:** 270M
- **Fine-tuning Method:** LoRA (r=8, alpha=16, dropout=0.0)
- **Framework:** [Unsloth](https://unsloth.ai) for efficient training
- **Dataset:** [miriad-4.4M](https://huggingface.co/datasets/miriad/miriad-4.4M)
- **Task:** Medical question answering & clinical reasoning

---

## Training Configuration
- **Epochs:** 1
- **Max Steps:** 600
- **Batch Size:** 1 (grad_acc=24)
- **Max Seq Length:** 384
- **Optimizer:** AdamW 8-bit
- **Precision:** float16 (fp16)

---

## Usage

### Inference (Transformers)
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "OmerShah/medgemma-270m"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

prompt = "What are the common symptoms of iron deficiency anemia?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))