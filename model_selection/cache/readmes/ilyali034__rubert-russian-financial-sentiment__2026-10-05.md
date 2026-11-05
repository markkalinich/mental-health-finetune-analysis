---
language:
- ru
license: apache-2.0
tags:
- sentiment-analysis
- financial-sentiment
- russian
- bert
- rubert
- text-classification
datasets:
- mteb/SentiRuEval2016
metrics:
- accuracy
- f1
- precision
- recall
base_model: blanchefort/rubert-base-cased-sentiment-rusentiment
pipeline_tag: text-classification
widget:
- text: "Акции компании выросли на 15% после публикации отчетности"
- text: "Банк объявил о сокращении 2000 рабочих мест на фоне кризиса"
- text: "Совет директоров рассмотрит квартальный отчет на следующей неделе"
---

# RuBERT Russian Financial Sentiment

A fine-tuned RuBERT model for **3-class sentiment classification** of Russian-language financial and economic text (negative / neutral / positive).

This model fine-tunes [`blanchefort/rubert-base-cased-sentiment-rusentiment`](https://huggingface.co/blanchefort/rubert-base-cased-sentiment-rusentiment) on the [SentiRuEval2016](https://huggingface.co/datasets/mteb/SentiRuEval2016) dataset, adapting a general-purpose Russian sentiment model to the financial domain.

## Model Details

- **Base model:** `blanchefort/rubert-base-cased-sentiment-rusentiment` (RuBERT)
- **Architecture:** BERT for Sequence Classification
- **Language:** Russian
- **Task:** 3-class sentiment classification
- **Training dataset:** [mteb/SentiRuEval2016](https://huggingface.co/datasets/mteb/SentiRuEval2016)
- **Max sequence length:** 128 tokens
- **License:** Apache 2.0

### Labels

| Label ID | Sentiment |
|---|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "ilyali034/rubert-russian-financial-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "Акции компании выросли на 15% после публикации отчетности"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()

id2label = {0: "negative", 1: "neutral", 2: "positive"}
print(f"Predicted sentiment: {id2label[predicted_class_id]}")
```

Or with the `pipeline` API:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="ilyali034/rubert-russian-financial-sentiment")
result = classifier("Банк объявил о рекордной прибыли за квартал")
print(result)
```

## Training Details

The model was fine-tuned using the Hugging Face `Trainer` API.

- **Epochs:** 3
- **Batch size:** 16 (train and eval)
- **Warmup steps:** 500
- **Weight decay:** 0.01
- **Best checkpoint selected by:** macro F1 on the validation set
- **Train/validation split:** 85% / 15% (stratified by label), plus the original held-out test split

Labels in the source dataset (-1, 0, 1) were remapped to (0, 1, 2) for negative, neutral, and positive respectively.

## Evaluation Results

Evaluated on a held-out test set of 3,000 examples (1,000 per class).

| Metric | Score |
|---|---|
| Accuracy | 0.8123 |
| Macro F1 | 0.8108 |
| Macro Precision | 0.8211 |
| Macro Recall | 0.8123 |
| Matthews Correlation Coefficient (MCC) | 0.7232 |
| Cohen's Kappa | 0.7185 |

### Per-Class Metrics

| Class | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| Negative | 0.8505 | 0.8820 | 0.8660 | 1000 |
| Neutral | 0.8277 | 0.7780 | 0.8021 | 1000 |
| Positive | 0.7908 | 0.8090 | 0.7998 | 1000 |
| **Macro Avg** | **0.8230** | **0.8230** | **0.8226** | **3000** |
| **Weighted Avg** | **0.8230** | **0.8230** | **0.8226** | **3000** |

### Confusion Matrix

|  | Predicted Negative | Predicted Neutral | Predicted Positive |
|---|---|---|---|
| **Actual Negative** | 882 | 49 | 69 |
| **Actual Neutral** | 77 | 778 | 145 |
| **Actual Positive** | 78 | 113 | 809 |

The model performs best on negative sentiment (F1 = 0.866). The most common confusion is between neutral and positive text, which is typical for financial language where neutral factual statements and mildly positive statements can overlap.

## Intended Use

This model is intended for sentiment analysis of Russian-language financial and economic content such as:

- News headlines and articles about companies, markets, and the economy
- Social media posts and comments discussing financial topics
- Analyst commentary and investor discussions

### Limitations

- Trained on general Russian sentiment data (SentiRuEval2016), not a purpose-built financial corpus, so domain-specific nuance (e.g. sarcasm, technical jargon, mixed-sentiment reports) may not be fully captured.
- Maximum input length is 128 tokens; longer documents should be split or truncated.
- As with any sentiment classifier, predictions should not be used as the sole basis for financial decision-making.

## Citation

If you use this model, please cite the base model and dataset:

```bibtex
@misc{rubert-financial-sentiment,
  author = {ilyali034},
  title = {RuBERT Russian Financial Sentiment},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/ilyali034/rubert-russian-financial-sentiment}
}
```

Base model: `blanchefort/rubert-base-cased-sentiment-rusentiment`
Dataset: `mteb/SentiRuEval2016`
