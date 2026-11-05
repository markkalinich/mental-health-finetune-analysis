---
language:
- fa
- en
- ckb
license: cc-by-4.0
tags:
- medical
- text-classification
- kurdish
- persian
- triage
- xlm-roberta
- low-resource
datasets:
- alanjafari/KurMed-Triage
metrics:
- accuracy
- f1
pipeline_tag: text-classification
base_model:
- FacebookAI/xlm-roberta-base
---

# KurMed-Triage-XLMRoBERTa

Medical specialty classification model for Kurdish and Persian speakers, 
fine-tuned on [KurMed-Triage](https://huggingface.co/datasets/alanjafari/KurMed-Triage) dataset.

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 87.0% |
| F1 Score (weighted) | 0.871 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="alanjafari/KurMed-Triage-XLMRoBERTa"
)

result = classifier("درد قفسه سینه دارم و نفس کشیدنم سخته")
print(result)
```

## Classes (10 Specialties)

cardiology, dermatology, emergency, ent, gynecology,
internal_medicine, neurology, orthopedics, pediatrics, psychiatry

## Training Details

- **Base model:** xlm-roberta-base
- **Dataset:** 2,000 samples (1,700 train / 300 validation)
- **Epochs:** 5
- **Input:** Persian + English patient text
- **Hardware:** Google Colab T4 GPU

## Dataset

[alanjafari/KurMed-Triage](https://huggingface.co/datasets/alanjafari/KurMed-Triage)

## Author

**Alan Jafari** — AI Specialist & Founder of EONE Team