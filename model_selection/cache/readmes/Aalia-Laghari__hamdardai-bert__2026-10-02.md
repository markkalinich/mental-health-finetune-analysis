---
language: en
tags:
- text-classification
- mental-health
- bert
- depression-severity
- suicide-risk
license: mit
datasets:
- depression-severity
- sdcnl
- suicidewatch
base_model: mental/mental-bert-base-uncased
pipeline_tag: text-classification
metrics:
- accuracy
- f1
---

# HamdardAI-BERT — Mental Health Severity Classifier

Fine-tuned version of [mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased)
for 4-class mental health severity classification.
Built as part of the EchoCare project (M1 — NLP Core).

## Task
Given a user's text input, classify it into one of 4 severity levels:

| Label | Class  | Description                              |
|-------|--------|------------------------------------------|
| 0     | Low    | Mild stress, general low mood            |
| 1     | Medium | Moderate depression symptoms             |
| 2     | High   | Severe depression, high distress         |
| 3     | Crisis | Active suicidal ideation, immediate risk |

## Usage

```python
from transformers import BertTokenizerFast, BertForSequenceClassification
import torch

tokenizer = BertTokenizerFast.from_pretrained("Aalia-Laghari/hamdardai-bert")
model     = BertForSequenceClassification.from_pretrained("Aalia-Laghari/hamdardai-bert")
model.eval()

text   = "I haven't left my room in days and nothing feels real anymore"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits
    pred   = logits.argmax(dim=-1).item()

labels = ["Low", "Medium", "High", "Crisis"]
print(labels[pred])
```

## Training Data

Three datasets combined and preprocessed:

| Dataset           | Samples | Classes used     |
|-------------------|---------|------------------|
| Depression Severity (Reddit) | 3,549   | Low, Medium, High, Crisis |
| SDCNL             | 1,820   | Medium, Crisis   |
| SuicideWatch      | 5,000 (sampled) | Low, Crisis |
| **Total**         | **~11,150** (after augmentation) | |

Class distribution after augmentation:
- Low: 5,113 | Medium: 2,000 | High: 1,200 | Crisis: 3,638

## Training Details

| Parameter             | Value                        |
|-----------------------|------------------------------|
| Base model            | mental/mental-bert-base-uncased |
| Max sequence length   | 128                          |
| Batch size            | 32                           |
| Learning rate         | 2e-5                         |
| LR scheduler          | Cosine with warmup (15%)     |
| Weight decay          | 0.05                         |
| Label smoothing       | 0.1                          |
| Loss function         | Ordinal CrossEntropy + MSE (λ=0.5) |
| Dropout               | 0.3 (all layers)             |
| Early stopping        | Patience 5 on val macro-F1   |
| Max epochs            | 20                           |
| Data augmentation     | Synonym swap + pattern paraphrase on minority classes |

## Performance (Test Set)

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 81.6%  |
| Macro F1  | 0.764  |
| Precision | 0.755  |
| Recall    | 0.775  |

Per-class breakdown:

| Class  | Precision | Recall | F1    | Support |
|--------|-----------|--------|-------|---------|
| Low    | 0.884     | 0.865  | 0.875 | 512     |
| Medium | 0.508     | 0.508  | 0.508 | 120     |
| High   | 0.796     | 0.908  | 0.848 | 120     |
| Crisis | 0.832     | 0.819  | 0.825 | 364     |

## Limitations

- Medium class F1 (0.508) is lower due to inherent ambiguity between mild and moderate severity
- Trained on English Reddit text — may not generalise to formal clinical language
- Not a substitute for professional mental health assessment
- Inter-annotator agreement on these datasets is ~70–80%, setting a natural ceiling on accuracy

## Intended Use

Research and educational purposes as part of the EchoCare mental health support application.
Not intended for clinical diagnosis or standalone mental health intervention.

## Authors

Aalia Laghari — NLP Core (M1), EchoCare Project