---
language: en
license: mit
tags:
- text-classification
- emotion-detection
- distilbert
- nlp
- mlops
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
base_model: distilbert-base-uncased
pipeline_tag: text-classification
---

# Emotion Detection from Text — DistilBERT

Fine-tuned [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)
for multi-class emotion classification on English text.
Trained as part of the MLOps Group Assignment at IIT Jodhpur (PGD AI, 2025–26).

## Model details

| Property        | Value                              |
|-----------------|------------------------------------|
| Base model      | distilbert-base-uncased            |
| Task            | Text classification (6 classes)    |
| Language        | English                            |
| License         | MIT                                |
| Parameters      | ~66 million                        |
| Training epochs | 3 (v1) / 5 (v2)                   |
| Best version    | v2 (lr=5e-5, 5 epochs)            |

## Labels

| ID | Emotion  |
|----|----------|
| 0  | sadness  |
| 1  | joy      |
| 2  | love     |
| 3  | anger    |
| 4  | fear     |
| 5  | surprise |

## Performance

Evaluated on the held-out test split of dair-ai/emotion (2,000 samples).

| Version | Learning rate | Epochs | Accuracy | F1 (weighted) |
|---------|---------------|--------|----------|---------------|
| v1      | 3e-5          | 3      | 0.9395   | 0.9393        |
| v2      | 5e-5          | 5      | 0.9415   | 0.9414        |

**Best model: v2** — pushed to this repository.

Full experiment logs are available on
[Weights & Biases](https://wandb.ai/g25ait2149-indian-institute-of-technology-jodhpur/mlops-iitj-emotion).

## How to use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="g25ait2149/mlops-group28-emotion-distilbert-iitj"
)

result = classifier("I am feeling so happy today!")
print(result)
# [{'label': 'joy', 'score': 0.97}]
```

## Training details

- **Dataset**: [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion)
  — 16,000 train / 2,000 validation / 2,000 test samples
- **Preprocessing**: lowercased, whitespace-stripped, tokenized with
  DistilBERT tokenizer (max length 128)
- **Training framework**: Hugging Face Trainer API
- **Hardware**: Kaggle GPU T4 x2 (free tier)
- **Experiment tracking**: Weights & Biases
- **Optimizer**: AdamW with weight decay 0.01, warmup ratio 0.1

## Model selection rationale

DistilBERT was selected because it is 40% smaller and 60% faster than
BERT while retaining 97% of its language understanding performance,
as reported in the original model card. At 66 MB, it fits comfortably
within Kaggle's free GPU memory limits, enabling rapid iteration
across multiple hyperparameter configurations. Its pre-training on
English text using masked language modelling makes it well-suited for
downstream text classification tasks such as emotion detection.
Compared to larger alternatives like RoBERTa-base, DistilBERT
completes fine-tuning in under 20 minutes on a T4 GPU, making it
practical for academic experimentation.

## Limitations

- Trained only on English tweets — may not generalise well to formal
  text, other languages, or very long documents.
- Class imbalance exists in the dataset (joy and sadness are
  over-represented vs surprise and love).
- Not suitable for clinical or mental health applications without
  further validation.

## Team

Developed by Group 28 — IIT Jodhpur PGD AI, Trimester 2, 2025–26.

| Name                               | Roll Number  |
|------------------------------------|--------------|
| U E Sai Pavan Vamshi Krishna       | G25AIT2149   |
| Shivender KR Gautam                | G25AIT2101   |
| Manoj Godara                       | G25AIT2060   |

## Citation

If you use this model, please cite:
```
@misc{iitj-group28-emotion-2025,
  title  = {Emotion Detection from Text using DistilBERT},
  author = {Group 28, IIT Jodhpur},
  year   = {2025},
  url    = {https://huggingface.co/g25ait2149/mlops-group28-emotion-distilbert-iitj}
}
```