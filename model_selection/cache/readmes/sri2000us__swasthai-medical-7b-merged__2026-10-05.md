---
license: apache-2.0
language:
- en
library_name: transformers
base_model: mistralai/Mistral-7B-v0.3
tags:
- medical
- healthcare
- india
- mistral
- fine-tuned
- merged
datasets:
- custom
pipeline_tag: text-generation
---

# SwasthAI Medical 7B (Merged)

A fine-tuned Mistral-7B model specialized for Indian healthcare assistance. This is the **merged full model** - no adapter loading required.

## Model Details

| Property | Value |
|----------|-------|
| **Base Model** | Mistral-7B-v0.3 |
| **Fine-tuning** | QLoRA merged into full weights |
| **Parameters** | 7B |
| **Context Length** | 2048 tokens |
| **License** | Apache 2.0 |

## Quick Start

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "sri2000us/swasthai-medical-7b-merged"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

def ask_swasthai(question):
    prompt = f"""### Instruction:
You are SwasthAI, an expert Indian healthcare assistant. Answer the medical question accurately.

### Input:
{question}

### Response:
"""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=256, do_sample=True, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("### Response:")[-1].strip()

print(ask_swasthai("What are symptoms of diabetes?"))
```

## Prompt Format

```
### Instruction:
You are SwasthAI, an expert Indian healthcare assistant. Answer the medical question accurately.

### Input:
{user_question}

### Response:
{model_response}
```

## Training Data

Fine-tuned on 1,223 curated medical Q&A pairs covering:
- General medicine and primary care
- Chronic disease management
- Maternal and child health
- Mental health and wellness
- Ayurveda and traditional medicine
- Healthcare navigation in India

## Limitations

- **Not a replacement for professional medical advice**
- Always consult qualified healthcare providers
- Call 102/108 in India for emergencies

## Related Models

- [swasthai-medical-7b](https://huggingface.co/sri2000us/swasthai-medical-7b) - LoRA adapters only
