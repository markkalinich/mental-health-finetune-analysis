---
license: mit
language:
- ur
base_model:
- cardiffnlp/twitter-roberta-base-sentiment-latest
library_name: transformers
tags:
- ur
- ro-ur
- urdu
- roman
- roman-urdu
- sentiment-analysis
- roman-urdu
- text-classification
- xlm-roberta
- student-feedback
- low-resource-nlp
- urdu-nlp
- fine-tuned
datasets:
- tahamueed23/student-feedback
---
<div align="center">

# 🇵🇰 Roman Urdu Sentiment Analysis

**Fine-tuned XLM-RoBERTa for Roman Urdu Student Feedback**

[![Model](https://img.shields.io/badge/Model-XLM--RoBERTa--Base-blue)](https://huggingface.co/xlm-roberta-base)
[![Language](https://img.shields.io/badge/Language-Roman%20Urdu-green)](https://en.wikipedia.org/wiki/Roman_Urdu)
[![Task](https://img.shields.io/badge/Task-Sentiment%20Analysis-orange)](https://huggingface.co/tasks/text-classification)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

*Classifies Roman Urdu text into Positive · Neutral · Negative*

</div>

---

## 📌 Model Description

This model is a fine-tuned version of [`xlm-roberta-base`](https://huggingface.co/xlm-roberta-base) specifically trained for **sentiment analysis of Roman Urdu text** — the Latin-script transliteration of Urdu widely used in Pakistani social media, messaging, and informal writing.

The model was trained on a real-world dataset of **student feedback** collected from Pakistani educational institutions, covering opinions on teachers, courses, classroom environment, and academic experiences. It is designed to be robust to:

- Highly variable Roman Urdu spelling (e.g. `acha` / `accha` / `achha` / `achi`)
- Code-mixed sentences with occasional English words
- Informal, noisy, social-media-style writing
- Short, context-sparse feedback phrases

### Why XLM-RoBERTa?

XLM-RoBERTa Base was selected over alternatives for the following reasons:

| Model | Reason for / against |
|---|---|
| **XLM-RoBERTa Base** ✅ | Trained on 2.5TB CommonCrawl across 100 languages; best low-resource performance; fits Colab free tier |
| XLM-RoBERTa Large | Higher accuracy but needs ~24 GB VRAM — impractical for most users |
| Multilingual BERT (mBERT) | Trained on Wikipedia only; weak on informal Roman script |
| IndicBERT | Strong for South Asian scripts but underperforms on Latin-script Urdu |

---

## 🏷️ Labels

| ID | Label | Meaning |
|---|---|---|
| 0 | **NEGATIVE** | Criticism, complaints, dissatisfaction |
| 1 | **NEUTRAL** | Factual, balanced, or ambiguous statements |
| 2 | **POSITIVE** | Praise, satisfaction, appreciation |

---

## 🚀 Quick Start

### Using the `pipeline` API (Recommended)

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="tahamueed23/roman-urdu-sentiment",
    tokenizer="tahamueed23/roman-urdu-sentiment",
)

# Single sentence
result = classifier("ye lecture bohat acha tha")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9412}]

# Batch prediction
sentences = [
    "ye lecture bohat acha tha",         # very good lecture
    "sir bilkul samjha nahi sakay",       # teacher couldn't explain at all
    "class theek thi, koi khas baat nahi" # class was okay, nothing special
]
results = classifier(sentences)
for text, res in zip(sentences, results):
    print(f"{text:<50} → {res['label']} ({res['score']:.2%})")
```

### Using Model + Tokenizer Directly

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "tahamueed23/roman-urdu-sentiment"
tokenizer  = AutoTokenizer.from_pretrained(model_name)
model      = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def predict_sentiment(text: str) -> dict:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128,
        padding=True,
    )
    with torch.no_grad():
        outputs = model(**inputs)

    probs   = torch.softmax(outputs.logits, dim=-1)[0]
    pred_id = int(probs.argmax())
    labels  = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}

    return {
        "sentiment":     labels[pred_id],
        "confidence":    round(float(probs[pred_id]), 4),
        "probabilities": {labels[i]: round(float(p), 4) for i, p in enumerate(probs)},
    }

# Example
print(predict_sentiment("zabardast teacher hai, bohat kuch seekha"))
# {
#   "sentiment": "POSITIVE",
#   "confidence": 0.9631,
#   "probabilities": {"NEGATIVE": 0.0142, "NEUTRAL": 0.0227, "POSITIVE": 0.9631}
# }
```

---

## 📊 Evaluation Results

> Results on the held-out test set (10% stratified split, never seen during training).

| Metric | Score |
|---|---|
| **Accuracy** | ~87% |
| **F1 Macro** | ~85% |
| **F1 Weighted** | ~87% |
| **Precision Macro** | ~85% |
| **Recall Macro** | ~85% |

### Per-Class Metrics

| Class | Precision | Recall | F1 |
|---|---|---|---|
| NEGATIVE | ~88% | ~86% | ~87% |
| NEUTRAL | ~79% | ~81% | ~80% |
| POSITIVE | ~90% | ~89% | ~89% |

> Note: Neutral is the hardest class due to its inherent ambiguity in Roman Urdu — a known challenge in low-resource sentiment analysis.

---

## 📁 Training Data

### Dataset Overview

| Property | Value |
|---|---|
| **Source** | Real student feedback from Pakistani educational institutions |
| **Languages** | Roman Urdu (Latin-script Urdu) + occasional English code-mixing |
| **Total Samples** | ~62,841 raw → ~20,994 after quality filtering |
| **Domain** | Academic: teachers, courses, classroom experience, assignments |
| **Collection** | User-generated, noisy, informal text |

### Class Distribution (after filtering)

| Sentiment | Count | % |
|---|---|---|
| POSITIVE | ~9,168 | 43.7% |
| NEGATIVE | ~7,355 | 35.0% |
| NEUTRAL | ~4,471 | 21.3% |

### Dataset Quality Pipeline

The raw dataset underwent a multi-stage quality enhancement pipeline before training:

1. **Deduplication** — 4,089 exact duplicates removed
2. **Near-duplicate flagging** — similar texts filtered to prevent data leakage
3. **Label confidence filtering** — rows with Low confidence scores excluded
4. **Quality score filtering** — samples scoring < 3/7 removed (gibberish, single words)
5. **Language isolation** — only Roman Urdu rows retained for this model

### Roman Urdu Normalization

A custom normalization dictionary was applied to unify spelling variants — a critical step for Roman Urdu which has no official orthography:

| Variants | Normalized Form |
|---|---|
| `acha`, `accha`, `achha`, `achaa` | `acha` |
| `bohat`, `bahut`, `bohot`, `boht`, `bhut` | `bohat` |
| `nahi`, `nai`, `nh`, `nhy`, `nahin` | `nahi` |
| `hai`, `hy`, `hay`, `he`, `hain` | `hai` |
| `theek`, `thek`, `thik`, `tik` | `theek` |
| `zabardast`, `zabrdast`, `zabardust` | `zabardast` |
| `mushkil`, `muskil`, `mushkel` | `mushkil` |

---

## ⚙️ Training Configuration

```python
base_model       = "xlm-roberta-base"
max_seq_length   = 128
batch_size       = 16
gradient_accum   = 2          # effective batch = 32
epochs           = 5          # early stopping patience = 2
learning_rate    = 2e-5
lr_scheduler     = "cosine"
warmup_ratio     = 0.1
weight_decay     = 0.01
fp16             = True       # mixed precision on GPU
loss_function    = "CrossEntropyLoss (class-weighted)"
split            = "80% train / 10% val / 10% test (stratified)"
seed             = 42
```

### Class-Weighted Loss

To handle class imbalance (Positive >> Neutral), training used `sklearn.utils.class_weight.compute_class_weight('balanced')` to assign higher loss penalties for the minority Neutral class. This significantly improves recall on the Neutral class without sacrificing Positive/Negative performance.

### Early Stopping

Training used `EarlyStoppingCallback(patience=2)` monitoring `eval_f1_macro`. The best checkpoint is automatically restored at the end of training.

---

## 🛠️ Training Environment

| Component | Details |
|---|---|
| Framework | HuggingFace Transformers 4.x |
| Hardware | Google Colab / GPU (T4/A100) |
| Python | 3.10+ |
| Key Libraries | `transformers`, `datasets`, `evaluate`, `accelerate`, `scikit-learn`, `torch` |
| Platform | Google Colab / Kaggle / Local GPU |

---

## ⚠️ Limitations & Biases

- **Domain-specific**: Trained on student feedback; may underperform on social media, product reviews, or political text
- **Informal Roman Urdu only**: Does not support Urdu script (use a dedicated Urdu model for that)
- **Spelling variation**: Despite normalization, very unusual spellings not in the training vocabulary may be misclassified
- **Sarcasm & irony**: The model does not reliably detect sarcasm — a known hard problem in Roman Urdu NLP
- **Short texts**: Texts under 3 words may lack sufficient context for accurate prediction
- **Regional dialect**: May reflect biases from Pakistani student population data

---

## 🔬 Example Predictions

| Input Text | Prediction | Confidence |
|---|---|---|
| `ye lecture bohat acha tha` | ✅ POSITIVE | 94.1% |
| `zabardast teacher hai, best class ever!` | ✅ POSITIVE | 96.3% |
| `ustad nay bahut acha samjhaya, maza aa gaya` | ✅ POSITIVE | 92.7% |
| `sir bilkul samjha nahi sakay` | ❌ NEGATIVE | 91.5% |
| `ye course bilkul bekaar hai, kuch nahi sikhaya` | ❌ NEGATIVE | 95.8% |
| `nahi samjha kuch bhi is lecture mein` | ❌ NEGATIVE | 89.2% |
| `class theek thi` | ⚪ NEUTRAL | 83.4% |
| `aj class normal thi, koi khas baat nahi` | ⚪ NEUTRAL | 81.6% |
| `assignment ka deadline bohat tight tha` | ⚪ NEUTRAL | 76.8% |

---

## 📚 Citation

If you use this model in your research or project, please cite:

```bibtex
@misc{mueed2025romanurdusenti,
  author       = {Taha Mueed},
  title        = {Roman Urdu Sentiment Analysis: Fine-tuned XLM-RoBERTa on Student Feedback},
  year         = {2026},
  publisher    = {HuggingFace},
  journal      = {HuggingFace Model Hub},
  howpublished = {\url{https://huggingface.co/tahamueed23/roman-urdu-sentiment}},
}
```

---

## 👤 About the Author

**Taha Mueed**

NLP Researcher | Low-Resource Language Specialist | Pakistani Language AI

- 🔗 HuggingFace: [@tahamueed23](https://huggingface.co/tahamueed23)

---

## 📄 License

This model is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute it for both research and commercial purposes with attribution.

---

<div align="center">

*Built with ❤️ for the Roman Urdu NLP community*

*If this model helped your research, please ⭐ star the repository!*

</div>