---
language: en
license: apache-2.0
base_model: Qwen/Qwen2.5-3B
tags:
  - text-classification
  - safety
  - content-moderation
  - qwen2.5
datasets:
  - budecosystem/guardrail-training-data
metrics:
  - f1
  - accuracy
---

# Safety Classifier — Qwen2.5-3B

A multiclass safety/content-moderation classifier fine-tuned on **Qwen2.5-3B** using LoRA (merged full model).

**Developer:** Satyam Jain  
**Base Model:** [Qwen/Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B)  
**Dataset:** [budecosystem/guardrail-training-data](https://huggingface.co/datasets/budecosystem/guardrail-training-data)

---

## Labels

| Label | Description |
|-------|-------------|
| `benign` | Safe, harmless content |
| `bias_discrimination` | Gender, race, religion, orientation bias |
| `compliance_vulnerability` | Code vulnerabilities, CWE/MITRE issues |
| `fraud_misinfo` | Fraud, deception, misinformation |
| `violence` | Violent content |
| `self_harm` | Self-harm related content |
| `hate_speech` | Hate speech |
| `sexual_content` | Sexual content |
| `illegal_activity` | Illegal activities |
| `privacy_violation` | Privacy violations |
| `cybersecurity` | Cybersecurity threats |
| `child_safety` | Child safety issues |

*(Exact labels depend on dataset — see `label_encoder.pkl`)*

---

## Training Details

| Parameter | Value |
|-----------|-------|
| Base Model | Qwen/Qwen2.5-3B |
| Method | LoRA (merged into full model) |
| LoRA r | 16 |
| LoRA alpha | 32 |
| LoRA targets | q_proj, v_proj, k_proj, o_proj |
| Max length | 256 |
| Batch size | 8 × 8 grad accum = 64 effective |
| Epochs | 4 |
| Learning rate | 2e-4 (cosine schedule) |
| Loss | Focal Loss (γ=2.0) + label smoothing |
| Balanced | 5,000 samples per class |
| F1 Macro | 0.6608 |
| Accuracy | 0.6803 |

---

## Usage

```python
import torch, pickle
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from huggingface_hub import hf_hub_download

REPO_ID = 'jainsatyam26/light-safety-classifier-qwen2.5-3b'
device  = 'cuda' if torch.cuda.is_available() else 'cpu'

model     = AutoModelForSequenceClassification.from_pretrained(REPO_ID, trust_remote_code=True).to(device)
tokenizer = AutoTokenizer.from_pretrained(REPO_ID, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

le_path = hf_hub_download(REPO_ID, 'label_encoder.pkl')
with open(le_path, 'rb') as f:
    meta = pickle.load(f)
le = meta['label_encoder']

def predict(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True,
                       max_length=256, padding=True).to(device)
    with torch.no_grad():
        probs = torch.softmax(model(**inputs).logits, dim=1)[0].cpu().numpy()
    return {
        'label':      le.classes_[probs.argmax()],
        'confidence': float(probs.max()),
        'is_safe':    le.classes_[probs.argmax()] == 'benign',
    }

print(predict("How do I make a bomb?"))
# {'label': 'violence', 'confidence': 0.97, 'is_safe': False}
```
