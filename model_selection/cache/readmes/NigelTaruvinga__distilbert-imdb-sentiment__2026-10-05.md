---
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- distilbert
- imdb
- fine-tuned
language:
- en
license: apache-2.0
datasets:
- imdb
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# DistilBERT Fine-Tuned for IMDb Sentiment Classification

A fine-tuned [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) model for binary sentiment classification on movie reviews. Trained on the IMDb dataset, the model predicts whether a review is **Positive** or **Negative**.

**Live Demo:** [huggingface.co/spaces/NigelTaruvinga/sentiment-classifier](https://huggingface.co/spaces/NigelTaruvinga/sentiment-classifier)

---

## Model Details

### Model Description

- **Developed by:** Nigel Taruvinga
- **Model type:** Text Classification (Transformer fine-tune)
- **Language:** English
- **License:** Apache 2.0
- **Base model:** distilbert-base-uncased
- **Fine-tuned on:** IMDb Movie Reviews dataset

### Model Sources

- **Repository:** [github.com/Nigel-Taruvinga](https://github.com/Nigel-Taruvinga)
- **Demo:** [huggingface.co/spaces/NigelTaruvinga/sentiment-classifier](https://huggingface.co/spaces/NigelTaruvinga/sentiment-classifier)

---

## Uses

### Direct Use

This model can be used directly for binary sentiment classification of English text — particularly movie or product reviews. Input any review and the model returns a Positive or Negative label with a confidence score.

### Downstream Use

The model can be plugged into larger NLP pipelines for:
- Review moderation and filtering
- Customer feedback analysis
- Content recommendation systems

### Out-of-Scope Use

- Non-English text
- Neutral or multi-class sentiment (the model only outputs binary labels)
- Domains very different from movie reviews (e.g. medical or legal text) may produce unreliable results

---

## How to Get Started

```python
from transformers import pipeline

sentiment = pipeline(
    "text-classification",
    model="NigelTaruvinga/distilbert-imdb-sentiment",
    device=-1  # use 0 for GPU
)

result = sentiment("This movie was absolutely fantastic. One of the best I have ever seen.")
print(result)
# [{'label': 'LABEL_1', 'score': 0.97}]  -> Positive
```

To map labels:
```python
label_map = {"LABEL_0": "Negative", "LABEL_1": "Positive"}
label = label_map[result[0]["label"]]
confidence = round(result[0]["score"] * 100, 2)
print(f"Sentiment: {label} ({confidence}%)")
```

---

## Training Details

### Training Data

The [IMDb dataset](https://huggingface.co/datasets/imdb) contains 50,000 movie reviews evenly split between positive and negative labels. A subset of 3,000 training and 1,000 test samples was used for fine-tuning on CPU hardware.

### Preprocessing

- Tokenised using `DistilBertTokenizer` with `max_length=256`, `padding=max_length`, `truncation=True`
- Labels renamed to `labels` column for compatibility with the Trainer API
- Dataset formatted as PyTorch tensors

### Training Hyperparameters

| Parameter | Value |
|---|---|
| Epochs | 2 |
| Learning rate | 2e-5 |
| Batch size | 8 |
| Weight decay | 0.01 |
| Optimizer | AdamW |
| Evaluation strategy | Per epoch |
| Training hardware | CPU |
| Best model | Loaded at end of training |

---

## Evaluation

### Results

Evaluated on 1,000 held-out IMDb test samples:

| Metric | Score |
|---|---|
| Accuracy | 87.4% |
| F1 (macro) | 0.87 |
| Precision | 0.88 |
| Recall | 0.87 |

### Baseline Comparison

| Model | Accuracy |
|---|---|
| TF-IDF + Logistic Regression (baseline) | 83.2% |
| DistilBERT fine-tuned (this model) | **87.4%** |

Fine-tuning DistilBERT improves over the classical baseline by **+4.2 percentage points**.

---

## Bias, Risks, and Limitations

- Trained on movie reviews — performance may degrade on other review domains
- Binary classification only — cannot express neutral or mixed sentiment
- May reflect biases present in the IMDb dataset (e.g. genre or demographic skew in reviewer population)
- Short or ambiguous reviews may produce low-confidence predictions

### Recommendations

Use confidence scores as a signal of reliability. Predictions with confidence below 70% should be treated with caution. For production use, evaluate on a domain-specific held-out set before deployment.

---

## Environmental Impact

- **Hardware:** CPU (no GPU used)
- **Training time:** approximately 60 minutes
- **Cloud provider:** Local machine
- Carbon footprint is minimal given CPU-only training on a small dataset subset.

---

## Citation

If you use this model, please cite:

```
@misc{taruvinga2026distilbert,
  author = {Nigel Taruvinga},
  title  = {DistilBERT Fine-Tuned for IMDb Sentiment Classification},
  year   = {2026},
  url    = {https://huggingface.co/NigelTaruvinga/distilbert-imdb-sentiment}
}
```

---

## Model Card Author

Nigel Taruvinga — MS Artificial Intelligence, Yeshiva University  
[linkedin.com/in/nigeltaruvinga](https://linkedin.com/in/nigeltaruvinga) | [github.com/Nigel-Taruvinga](https://github.com/Nigel-Taruvinga)
