---
language:
- en
license: mit
tags:
- medical
- triage
- text-classification
- phi3
- qlora
- peft
- fine-tuning
- healthcare
base_model: microsoft/Phi-3-mini-4k-instruct
pipeline_tag: text-generation
---

# Phi-3-mini Medical Triage Assistant

Fine-tuned from `microsoft/Phi-3-mini-4k-instruct` (3.8B parameters) using
QLoRA on a medical triage instruction dataset. Given a patient symptom
description, the model classifies urgency and provides a brief clinical rationale.

> ⚠️ **Educational and portfolio use only. Not for clinical deployment.**

## Model Performance

Evaluated on 100 held-out synthetic patient presentations (25 per class).

| Model | Triage Accuracy | ROUGE-L | EMERGENCY Recall |
|---|---|---|---|
| **This model (fine-tuned)** | **64%** | **0.42** | **100%** |
| Base Phi-3-mini (zero-shot) | 37% | 0.21 | 100% |

The model never misses a genuine life-threatening EMERGENCY case.

### Per-Class Accuracy

| Level | Meaning | Accuracy |
|---|---|---|
| EMERGENCY | Call 999 immediately | 100% |
| SEMI-URGENT | GP within 24–48 hours | 60% |
| NON-URGENT | Routine GP appointment | 92% |
| URGENT | Same-day care | 4% |

The URGENT class is frequently over-triaged to EMERGENCY —
a conservative error that is clinically safer than the reverse.

## Training Details

| Property | Value |
|---|---|
| Base model | microsoft/Phi-3-mini-4k-instruct |
| Fine-tuning method | QLoRA — 4-bit NF4 + LoRA |
| LoRA rank (r) | 16 |
| LoRA target modules | qkv_proj, o_proj |
| Training examples | 200 synthetic patient presentations |
| Training platform | Kaggle T4 GPU (free tier, 16GB VRAM) |
| Trainable parameters | 9,437,184 (0.468% of total) |
| Training time | ~8 minutes |

## How to Use
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

model_id = "Milon96/phi3-medical-triage"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True,
)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

instruction = """You are a medical triage assistant. Classify the following
patient presentation into: EMERGENCY, URGENT, SEMI-URGENT, NON-URGENT.
EMERGENCY: Life-threatening — call 999 immediately.
URGENT: Serious — same-day care required.
SEMI-URGENT: Needs care within 24-48 hours.
NON-URGENT: Routine — GP appointment within a week."""

patient = "72-year-old male with sudden chest pain radiating to his left arm, sweating and nausea. Started 15 minutes ago."

prompt = f"<|system|>\n{instruction}<|end|>\n<|user|>\n{patient}<|end|>\n<|assistant|>\n"
result = pipe(prompt, max_new_tokens=150, do_sample=False, temperature=1.0)
response = result[0]["generated_text"].split("<|assistant|>")[-1].replace("<|end|>","").strip()
print(response)
# Triage Level: EMERGENCY
# Symptoms are consistent with acute myocardial infarction (heart attack).
# Immediate emergency services required. Call 999 now.
```

## Training Data

200 synthetic patient presentations generated using Claude (Anthropic)
covering realistic clinical scenarios. Each example includes patient age,
gender, and symptom description in natural language.

**Key lesson from this project:** MedQuAD (47,000 NIH Q&A pairs) uses a
"What is X?" question format that does not match real patient presentations.
200 high-quality synthetic examples outperformed 1,500 MedQuAD examples —
data quality beats data quantity.

## Limitations

- Trained on synthetic data — not validated on real clinical cases
- URGENT class has low accuracy (4%) — frequently over-triaged to EMERGENCY
- English language only
- Not suitable for real medical decision-making

## Repository

Full training code, dataset pipeline, and evaluation scripts:
[github.com/Milonahmed96/medical-triage-llm](https://github.com/Milonahmed96/medical-triage-llm)

## Citation
```bibtex
@misc{phi3-medical-triage,
  author = {Milon Ahmed},
  title = {Phi-3-mini Medical Triage Assistant},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/Milon96/phi3-medical-triage}
}
```