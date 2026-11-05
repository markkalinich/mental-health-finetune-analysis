---
language: en
license: apache-2.0
base_model: mistralai/Mistral-7B-Instruct-v0.2
tags:
  - medical
  - question-answering
  - qlora
  - peft
  - mistral
  - fine-tuned
datasets:
  - lavita/ChatDoctor-HealthCareMagic-100k
pipeline_tag: text-generation
---

# mistral-7b-medical-qa-qlora

Fine-tuned version of [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) for **medical question answering** using QLoRA.

## Training Details

| Property | Value |
|---|---|
| Base model | mistralai/Mistral-7B-Instruct-v0.2 |
| Method | QLoRA (4-bit NF4 + LoRA) |
| Dataset | ChatDoctor-HealthCareMagic-100k (20k samples) |
| LoRA rank (r) | 64 |
| LoRA alpha | 16 |
| Target modules | q_proj, v_proj |
| Trainable params | ~0.72% of total |
| Epochs | 1 |
| Batch size (effective) | 16 |
| Learning rate | 2e-4 |
| GPU | Tesla T4 (Kaggle) |
| Training time | ~5.8 hours |

## Evaluation Results (50 held-out samples)

| Metric | Base Model | Fine-tuned | Δ |
|---|---|---|---|
| ROUGE-1 | 27.00% | 29.45% | +2.45% |
| ROUGE-2 | 3.40% | 5.29% | +1.89% |
| ROUGE-L | 13.16% | 16.37% | +3.21% |
| BLEU | 1.28% | 2.81% | +1.53% |

All metrics improve consistently after fine-tuning.

## Qualitative Example

**Question:** I believe my daughter is suffering from anorexia. She constantly swallows and expels tiny burps. Is this related?

**Base model:** I'm here to help answer your question... please keep in mind that while I can provide information I cannot diagnose or treat medical conditions...

**Fine-tuned:** Hi, I have gone through your question. Anorexia nervosa is a psychological disorder characterized by self-starvation and excessive weight loss. It is not related to any physical illness. In anorexia...

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id  = "mohdomer/mistral-7b-medical-qa-qlora"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.float16, device_map="auto"
)

def ask(question):
    prompt = (
        f"<s>[INST] You are a knowledgeable medical assistant. "
        f"Answer the following medical question accurately and clearly.\n\n"
        f"{question} [/INST]"
    )
    inputs  = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.3, do_sample=True)
    gen = outputs[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(gen, skip_special_tokens=True).strip()

print(ask("What are the symptoms of type 2 diabetes?"))
```

## Limitations
- Not for real clinical use — model can hallucinate medical information
- English only
- Best within 512 token context window
- 1 epoch training — more epochs would improve results further

## Links
- GitHub: https://github.com/MOHD-OMER
- W&B Training Run: https://wandb.ai/asratabbssum-lords-institute-of-engineering-and-technology/mistral-medical-qlora/runs/tueb17vn
