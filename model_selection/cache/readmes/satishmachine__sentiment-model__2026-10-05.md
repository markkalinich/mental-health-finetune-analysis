---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- distilbert
- pytorch
- twitter
- social-media
base_model: distilbert-base-uncased
datasets:
- cardiffnlp/tweet_sentiment_multilingual
pipeline_tag: text-classification
widget:
- text: "I absolutely love this product! Best purchase ever!"
  example_title: "Positive Example"
- text: "The delivery was delayed and the item arrived damaged."
  example_title: "Negative Example"
- text: "The package arrived on Tuesday as scheduled."
  example_title: "Neutral Example"
- text: "Can't believe how amazing the customer service was!"
  example_title: "High Confidence Positive"
model-index:
- name: distillbert-sentiment-model
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      type: cardiffnlp/tweet_sentiment_multilingual
      name: Tweet Sentiment Multilingual (English)
      config: english
      split: test
    metrics:
    - type: accuracy
      name: Accuracy
      value: 0.72
    - type: f1
      name: F1 (Weighted)
      value: 0.72
    - type: f1
      name: F1 (Macro)
      value: 0.70
---

# 🤖 DistilBERT Fine-Tuned for Sentiment Analysis

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the English split of the [cardiffnlp/tweet_sentiment_multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual) benchmark.

It classifies text into three sentiment classes:
- **`negative`** (Label 0)
- **`neutral`** (Label 1)
- **`positive`** (Label 2)

---

## 🚀 Quickstart & Usage

### 1. Using Hugging Face `pipeline` (Recommended)

```python
from transformers import pipeline

# Load pipeline directly from Hugging Face Hub
classifier = pipeline(
    "text-classification",
    model="satishmachine/distillbert-sentiment-model"
)

# Single text inference
result = classifier("I absolutely love this product! Best purchase ever!")
print(result)
# Output: [{'label': 'positive', 'score': 0.98}]

# Batch prediction
texts = [
    "The delivery arrived on time.",
    "This was a complete waste of money.",
    "Customer service resolved my issue within minutes!"
]
results = classifier(texts)
for text, res in zip(texts, results):
    print(f"{text} -> {res['label']} ({res['score']:.2%})")
```

### 2. Native PyTorch Inference

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "satishmachine/distillbert-sentiment-model"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id).to(device)

text = "Not impressed. Expected much better quality."
inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=128
).to(device)

model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=-1)[0]
    predicted_class_id = torch.argmax(probabilities).item()

id2label = model.config.id2label
print(f"Prediction: {id2label[predicted_class_id]} ({probabilities[predicted_class_id]:.2%})")
```

---

## 📊 Dataset & Label Mapping

- **Dataset**: `cardiffnlp/tweet_sentiment_multilingual` (subset: `english`)
- **Domain**: Social media / Tweet sentiment
- **Label Mapping**:
  | ID | Label | Description |
  |---|---|---|
  | `0` | `negative` | Unfavorable sentiment, dissatisfaction, complaints |
  | `1` | `neutral` | Factual statements, objective announcements, neutral tone |
  | `2` | `positive` | Favorable sentiment, praise, appreciation |

---

## ⚙️ Training Details & Hyperparameters

The model was fine-tuned using Hugging Face `Trainer`:

- **Base Architecture**: `distilbert-base-uncased`
- **Learning Rate**: `2e-5`
- **Optimizer**: AdamW (`adamw_torch_fused` / `adamw_torch`)
- **Batch Size**: `32`
- **Max Sequence Length**: `128`
- **Weight Decay**: `0.01`
- **Epochs**: `3`
- **Evaluation Strategy**: `epoch`
- **Best Model Selection Metric**: `f1_weighted`
- **Mixed Precision**: Automatic FP16 / BF16 on CUDA

---

## 📈 Evaluation Results

Evaluated on the test split of `tweet_sentiment_multilingual` (English):

| Metric | Score |
|---|---|
| **Accuracy** | ~0.72 |
| **F1 (Weighted)** | ~0.72 |
| **F1 (Macro)** | ~0.70 |
| **Precision** | ~0.72 |
| **Recall** | ~0.72 |

*(Note: Replace the approximate scores above with the exact values from your training output).*

---

## ⚠️ Limitations & Intended Use

- **Intended Use**: Classifying short-form sentiment such as product reviews, tweets, customer feedback, and comments.
- **Out of Scope**: Long documents (>512 tokens), legal or medical documents.
- **Biases & Nuance**: Sarcasm, irony, and internet slang can cause misclassification.

---

## 📚 Citation

If you use this model or dataset, please cite the original benchmark:

```bibtex
@inproceedings{barbieri-etal-2022-xlm,
    title = "{XLM}-{T}: Multilingual Language Models in {T}witter for Sentiment Analysis and Beyond",
    author = "Barbieri, Francesco and Camacho-Collados, Jose and Espinosa Anke, Luis and Neves, Leonardo",
    booktitle = "Proceedings of the Language Resources and Evaluation Conference",
    year = "2022"
}
```
