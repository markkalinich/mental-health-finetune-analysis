---
license: mit
---

# BERT Sentiment Classifier for Patient Health Risk

Fine-tuned `bert-base-uncased` for 3-class sentiment classification on patient questionnaire responses. The model predicts whether the patient's self-reported symptoms indicate **positive**, **neutral**, or **negative** health sentiment.

## Labels

| Label | Description |
|---|---|
| positive | No abnormal symptoms detected; patient reports "mild fatigue, stable breathing, no severe discomfort" |
| neutral | Some symptoms reported but tagged as low concern / low deterioration risk |
| negative | High concern symptoms affecting daily activities |

## Dataset

- **Source**: `patient_dataset.csv` (2,000 synthetic patient records)
- **Input**: `questionnaire_text` column — patient symptom descriptions with giveaway phrases (concern level, daily-activity impact) stripped to prevent label leakage
- **Labels**: Derived from `deterioration_risk` (0/1) plus text parsing for the 0→positive/neutral split
- **Split**: 80% train (1,600), 20% test (400), stratified

## Training Details

| Config | Value |
|---|---|
| Base Model | `bert-base-uncased` |
| Epochs | 30 |
| Batch Size | 16 |
| Learning Rate | 2e-5 |
| Optimizer | AdamW |
| Max Sequence Length | 128 tokens |
| Class Weights | Inverse frequency (negative class weighted ~2.9x) |
| Threshold Tuning | Negative-class logits boosted by ~3.0x at inference |

## Performance (Test Set)

| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| positive | 1.00 | 1.00 | 1.00 | 177 |
| neutral | 0.92 | 0.99 | 0.95 | 177 |
| negative | 0.94 | 0.67 | 0.78 | 46 |
| **accuracy** | | | **0.96** | 400 |
| macro avg | 0.95 | 0.89 | 0.91 | 400 |

## Training Loss

![Loss Curves](images/sa_loss_curves.png)

## Usage

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("models/bert_patient_risk_sentiment")
model = BertForSequenceClassification.from_pretrained("models/bert_patient_risk_sentiment")

text = "The patient reports shortness of breath, fever and body aches."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits
    # Apply tuned threshold for negative class
    logits[:, 2] *= 3.0
    pred = torch.argmax(logits, dim=1).item()

label_map = {0: "positive", 1: "neutral", 2: "negative"}
print(label_map[pred])
```

