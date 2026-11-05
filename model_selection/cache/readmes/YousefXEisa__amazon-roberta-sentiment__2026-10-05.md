---
language:
- en
license: mit
tags:
- sentiment-analysis
- roberta
- text-classification
- amazon-reviews
- pytorch
datasets:
- amazon_polarity
pipeline_tag: text-classification
widget:
- text: This product is absolutely amazing! Very high quality.
  example_title: Positive Review
- text: Terrible quality. Arrived broken and stopped working.
  example_title: Negative Review
model-index:
- name: amazon-roberta-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Amazon Polarity
      type: amazon_polarity
    metrics:
    - type: accuracy
      value: 0.9697
    - type: f1
      value: 0.97
    - type: precision
      value: 0.9671
    - type: recall
      value: 0.973
metrics:
- f1
- accuracy
- recall
- precision
base_model:
- FacebookAI/roberta-base
library_name: transformers
---

# Amazon RoBERTa Sentiment

A fine-tuned **RoBERTa-base** model that classifies Amazon product reviews as **Positive** or **Negative**.

- **Repo / Code:** [Github](https://github.com/YousefXEisa/amazon-sentiment-analysis)
- **Live Demo:** [reviews-sentiment-analysis-s7brv3.streamlit.app](https://reviews-sentiment-analysis-s7brv3.streamlit.app/)

## Model Details

### Model Description

This model is a fine-tuned version of `roberta-base` trained on the [Amazon Polarity](https://huggingface.co/datasets/amazon_polarity) dataset for binary sentiment classification (Positive / Negative). The `title` and `content` fields of each review were used jointly as model input.

The final model was selected after three training experiments comparing architectures and regularization strategies — see [Training Details](#training-details) below. (Or the full details of the experiment, including all three rounds, on GitHub).

- **Developed by:** Yousef Eisa
- **Model type:** Text Classification (binary sentiment)
- **Language(s):** English
- **License:** MIT
- **Finetuned from model:** [`roberta-base`](https://huggingface.co/roberta-base)

## Uses

### Direct Use

The model takes a review's title and body text and outputs a sentiment label (`Positive` / `Negative`) with a confidence score. It can be used directly for classifying Amazon-style product reviews, or similar English-language e-commerce review text.

### Out-of-Scope Use

- Not trained or evaluated on non-English text.
- Binary classification only — there is no "neutral" class, so mixed or ambiguous reviews will be forced into Positive/Negative.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "YousefXEisa/amazon-roberta-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "This product is absolutely amazing! Very high quality."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)

label = "Positive" if probs.argmax().item() == 1 else "Negative"
print(label, probs)
```

Or with the `pipeline` API:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="YousefXEisa/amazon-roberta-sentiment")
classifier("Terrible quality. Arrived broken and stopped working.")
```

## Training Details

### Training Data

[Amazon Polarity](https://huggingface.co/datasets/amazon_polarity) — Amazon product reviews labeled Positive/Negative. `title` and `content` were concatenated as input.

### Training Procedure

The final model (RoBERTa-base) was trained in fp32 on 250k samples for 3 epochs (early stopping enabled), with the following regularization recipe, arrived at after diagnosing overfitting in an initial BERT baseline run:

- Frozen embedding layer + first 4 encoder layers
- Dropout 0.1 on hidden and attention layers
- Label smoothing (0.1)
- Weight decay (0.01), excluded from bias/LayerNorm params
- Cosine LR schedule with 10% warmup
- Gradient clipping (`max_norm=1.0`)
- Early stopping (patience=2, delta=0.001)

Training was run on Google Colab (free GPU tier).

## Evaluation

Evaluated on a held-out test set of 10,000 samples, unseen during training or validation.

### Results

| Metric | Score |
|---|---|
| Accuracy | 0.9697 |
| Precision | 0.9671 |
| Recall | 0.9730 |
| F1 Score | 0.9700 |

**Classification Report:**

```
              precision    recall  f1-score   support
           0       0.97      0.97      0.97      4958
           1       0.97      0.97      0.97      5042
    accuracy                           0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000
```

RoBERTa outperformed a comparably-regularized BERT baseline (best val F1 0.9674 vs 0.9590) trained under identical conditions, which is why RoBERTa was selected as the final model.

## Bias, Risks, and Limitations

- Trained and evaluated on English Amazon product reviews only; accuracy on other domains or languages is untested.
- Binary classification only (Positive/Negative) — no neutral class.
- Like most sentiment models trained on product reviews, it may be less reliable on sarcasm, mixed sentiment within a single review, or very short/ambiguous text.

## Environmental Impact

- **Hardware Type:** Google Colab GPU (free tier)
- **Cloud Provider:** Google Colab
- Carbon emissions were not tracked for this project. They can be estimated using the [ML Impact calculator](https://mlco2.github.io/impact#compute).

## Citation

If you use this model, please reference the Hugging Face repo:

```
YousefXEisa/amazon-roberta-sentiment
```