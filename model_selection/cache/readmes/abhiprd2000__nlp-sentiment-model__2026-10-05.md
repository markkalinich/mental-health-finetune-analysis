---
language:
- en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- bert
- nlp
- transformers
- pytorch
base_model: bert-base-uncased
datasets:
- abhiprd20/nlp-benchmark-suite
metrics:
- accuracy
- f1
model-index:
- name: nlp-sentiment-model
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: NLP Benchmark Suite
      type: abhiprd20/nlp-benchmark-suite
    metrics:
    - type: accuracy
      value: 0.8458
    - type: f1
      value: 0.7928
---

# 🤖 NLP Sentiment Model

### *BERT fine-tuned for 3-class sentiment analysis — positive, negative, neutral*

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Accuracy](https://img.shields.io/badge/Accuracy-84.58%25-green)]()
[![F1 Score](https://img.shields.io/badge/F1%20Score-0.7928-orange)]()
[![Base Model](https://img.shields.io/badge/Base-BERT--base--uncased-yellow)]()

---

## 📌 Model Description

**NLP Sentiment Model** is a fine-tuned version of `bert-base-uncased` trained on the
[NLP Benchmark Suite](https://huggingface.co/datasets/abhiprd20/nlp-benchmark-suite)
dataset by Abhimanyu Prasad.

The model classifies input text into three sentiment categories:
- 😊 **Positive** — text expressing satisfaction, happiness, or praise
- 😞 **Negative** — text expressing dissatisfaction, anger, or criticism
- 😐 **Neutral** — text that is factual, balanced, or indifferent

It was trained on real-world data from Amazon product reviews, Twitter posts,
and IMDB movie reviews — covering a wide range of domains and writing styles.

---

## 📊 Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | **84.58%** |
| **Macro F1** | **0.7928** |
| Epochs | 3 |
| Training samples | ~4,796 |
| Test samples | ~1,199 |
| Base model | bert-base-uncased |

---

## ⚡ Quick Start

```python
from transformers import pipeline

# Load the model
classifier = pipeline(
    "sentiment-analysis",
    model="abhiprd20/nlp-sentiment-model"
)

# Predict sentiment
result = classifier("This product is absolutely amazing!")
print(result)
# → [{'label': 'positive', 'score': 0.97}]
```

---

## 🔍 More Examples

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis",
                      model="abhiprd20/nlp-sentiment-model")

texts = [
    "I absolutely love this, best purchase ever!",
    "Terrible quality, complete waste of money.",
    "It arrived on time and works as described.",
    "The customer service was incredibly helpful.",
    "Not great, not terrible, just average.",
]

for text in texts:
    result = classifier(text)[0]
    print(f"Text  : {text}")
    print(f"Label : {result['label']} ({round(result['score']*100, 1)}% confident)\n")
```

**Expected output:**
```
Text  : I absolutely love this, best purchase ever!
Label : positive (97.3% confident)

Text  : Terrible quality, complete waste of money.
Label : negative (98.1% confident)

Text  : It arrived on time and works as described.
Label : neutral (95.4% confident)

Text  : The customer service was incredibly helpful.
Label : positive (96.8% confident)

Text  : Not great, not terrible, just average.
Label : neutral (91.2% confident)
```

---

## 🧪 Use With AutoTokenizer and AutoModel

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("abhiprd20/nlp-sentiment-model")
model     = AutoModelForSequenceClassification.from_pretrained("abhiprd20/nlp-sentiment-model")

text   = "This is the best thing I have ever bought!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)

probs      = torch.softmax(outputs.logits, dim=1)
label_id   = torch.argmax(probs).item()
id2label   = {0: "negative", 1: "neutral", 2: "positive"}

print(f"Label      : {id2label[label_id]}")
print(f"Confidence : {probs[0][label_id].item():.4f}")
```

---

## 🗂️ Training Details

| Parameter | Value |
|-----------|-------|
| Base model | `bert-base-uncased` |
| Task | Sequence Classification |
| Number of labels | 3 (negative, neutral, positive) |
| Epochs | 3 |
| Batch size | 16 |
| Max sequence length | 128 |
| Optimizer | AdamW (default) |
| Hardware | NVIDIA T4 GPU (Google Colab) |
| Framework | Hugging Face Transformers |

---

## 📦 Training Dataset

This model was trained on the
[NLP Benchmark Suite](https://huggingface.co/datasets/abhiprd20/nlp-benchmark-suite)
dataset, specifically the sentiment analysis subset.

The training data covers three real-world sources:

| Source | Domain | Samples |
|--------|--------|---------|
| Amazon Polarity | E-commerce product reviews | ~2,000 |
| TweetEval | Social media posts | ~2,000 |
| IMDB | Movie reviews | ~2,000 |

**Total training samples:** ~4,796
**Total test samples:** ~1,199

---

## 🏷️ Label Mapping

| Label ID | Label | Meaning |
|----------|-------|---------|
| 0 | negative | Dissatisfaction, criticism, anger |
| 1 | neutral | Factual, balanced, indifferent |
| 2 | positive | Satisfaction, praise, happiness |

---



## ⚖️ License

This model is released under the **Apache License 2.0** 
research and commercial use.

Copyright 2026 Abhimanyu Prasad

---

## 📎 Citation

If you use this model in your research or project, please cite:

```bibtex
@misc{prasad2026nlpsentiment,
  title        = {NLP Sentiment Model: BERT Fine-tuned for 3-Class Sentiment Analysis},
  author       = {Prasad, Abhimanyu},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/abhiprd20/nlp-sentiment-model}},
  note         = {Fine-tuned on NLP Benchmark Suite. Accuracy: 84.58\%, F1: 0.7928}
}
```

---

## 👤 Author

**Abhimanyu Prasad**
🤗 Hugging Face: [abhiprd20](https://huggingface.co/abhiprd20)
📦 Dataset: [abhiprd20/nlp-benchmark-suite](https://huggingface.co/datasets/abhiprd20/nlp-benchmark-suite)

---

*If this model helped your project, consider giving it a ⭐ — it helps others find it too!*

---

## 📊 Cross-Language Evaluation

Each model was evaluated on all 4 languages (300 sentences per language, 100 per class).
This shows how well models trained on one language transfer to others.

### Accuracy Matrix

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| ⭐ **English model** _(this model)_ | **79.5%** ✓ | 34.0% | 33.3% | 33.0% |
| **Hindi model** | 60.0% | **68.0%** ✓ | 63.3% | 61.7% |
| **Maithili model** | 63.0% | 59.0% | **90.3%** ✓ | 75.0% |
| **Bhojpuri model** | 59.0% | 47.3% | 47.3% | **98.0%** ✓ |

### F1 Matrix (macro)

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| ⭐ **English model** _(this model)_ | **0.5424** ✓ | 0.1912 | 0.1667 | 0.1654 |
| **Hindi model** | 0.4362 | **0.6778** ✓ | 0.6319 | 0.6042 |
| **Maithili model** | 0.4443 | 0.5757 | **0.9035** ✓ | 0.7458 |
| **Bhojpuri model** | 0.4250 | 0.4166 | 0.4114 | **0.9801** ✓ |

### Key Findings

- This model achieves **79.5%** on English sentiment but drops to **~33%** on Maithili and Bhojpuri — equivalent to random chance on a 3-class task.
- Demonstrates that monolingual English training does **not** transfer to low-resource Bihari languages.
- English also transfers poorly to Hindi (34%), confirming the language barrier extends beyond Bihari languages.

> **Full paper:** This cross-evaluation is part of a research study on cross-lingual transfer for low-resource Bihari languages. See the companion datasets and models: [Maithili](https://huggingface.co/abhiprd20/maithili-sentiment-model) | [Bhojpuri](https://huggingface.co/abhiprd20/bhojpuri-sentiment-model) | [Hindi](https://huggingface.co/abhiprd20/hindi-sentiment-model) | [English](https://huggingface.co/abhiprd20/nlp-sentiment-model)
