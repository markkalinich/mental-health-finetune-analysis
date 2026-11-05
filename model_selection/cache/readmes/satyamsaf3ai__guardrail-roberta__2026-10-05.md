---
language:
- en
license: apache-2.0
base_model: roberta-base
datasets:
- jainsatyam26/guardrail-215k-splits
tags:
- text-classification
- safety
- content-moderation
- guardrail
- roberta
metrics:
- f1
- accuracy
---

# Safety Guardrail Classifier

A fine-tuned **RoBERTa-base** model for multi-class safety/content moderation classification.  
Trained on [guardrail-215k-splits](https://huggingface.co/datasets/jainsatyam26/guardrail-215k-splits).

---

## Model Details

| Property        | Value                                          |
|-----------------|------------------------------------------------|
| **Base Model**  | [roberta-base](https://huggingface.co/roberta-base) |
| **Task**        | Multi-class Text Classification (Safety)       |
| **Dataset**     | [jainsatyam26/guardrail-215k-splits](https://huggingface.co/datasets/jainsatyam26/guardrail-215k-splits) (~215K samples) |
| **Max Length**  | 128 tokens                                     |
| **Batch Size**  | 64                                             |
| **Learning Rate** | 2e-5                                         |
| **Epochs**      | 3                                              |
| **Precision**   | fp32                                           |
| **Optimizer**   | AdamW + weight decay 0.01                      |
| **Warmup**      | 10% of total steps                             |
| **Loss**        | Cross-Entropy with class weights               |

---

## Labels

| ID | Label                     | Description                        |
|----|---------------------------|------------------------------------|
| 0  | benign                    | Safe / normal content              |
| 1  | jailbreak                 | Prompt injection / jailbreak       |
| 2  | S1 Violent Crimes         | Violence & physical harm           |
| 3  | S2 Non-Violent Crimes     | Fraud, theft, illegal activity     |
| 4  | S4 Child Sexual Exploitation | CSAM / minors exploitation      |
| 5  | S6 Specialized Advice     | Dangerous medical/legal/financial  |
| 6  | S7 Privacy                | PII, stalking, doxxing             |
| 7  | S10 Hate                  | Hate speech, discrimination        |
| 8  | S11 Self-Harm             | Suicide, self-harm                 |
| 9  | S12 Sexual Content        | Explicit sexual content            |
| 10 | S14 Code Abuse            | Malware, exploit code              |

---

## Performance

| Metric            | Value     |
|-------------------|-----------|
| Weighted F1       | ~0.75–0.80 |
| Accuracy          | ~0.80–0.85 |
| Best Threshold    | 0.50 (tunable) |

> Evaluated on `validation` split of guardrail-215k-splits.  
> Threshold calibration available via `infer.py --threshold auto`.

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "satyamsaf3ai/guardrail-roberta"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

LABELS = [
    "benign", "jailbreak",
    "S1 Violent Crimes", "S2 Non-Violent Crimes",
    "S4 Child Sexual Exploitation", "S6 Specialized Advice",
    "S7 Privacy", "S10 Hate", "S11 Self-Harm",
    "S12 Sexual Content", "S14 Code Abuse",
]

def classify(text, threshold=0.50):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        probs = torch.softmax(model(**inputs).logits, dim=-1)[0]
    if probs.max() < threshold:
        return "benign", float(probs.max())
    idx = probs.argmax().item()
    return LABELS[idx], float(probs[idx])

label, confidence = classify("How do I make a bomb?")
print(f"{label} ({confidence:.1%})")
```

---

## Training Setup

- **Hardware**: NVIDIA L4 GPU  
- **Framework**: HuggingFace Transformers + Trainer API  
- **Sampling**: WeightedRandomSampler to handle class imbalance  
- **Early Stopping**: patience=4 on weighted F1  
- **Explosion Guard**: stops training if grad_norm > 500  

---

## Dataset

[jainsatyam26/guardrail-215k-splits](https://huggingface.co/datasets/jainsatyam26/guardrail-215k-splits)  
~215,000 labeled examples split into `train` / `validation`.

---

## Citation

If you use this model, please cite:

```bibtex
@misc{{guardrail-classifier,
  title  = {{Safety Guardrail Classifier}},
  author = {{jainsatyam26}},
  year   = {{2025}},
  url    = {{https://huggingface.co/satyamsaf3ai/guardrail-roberta}}
}}
```
