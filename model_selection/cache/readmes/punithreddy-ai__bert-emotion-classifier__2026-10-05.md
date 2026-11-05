---
language: en
license: mit
tags:
  - text-classification
  - emotion-detection
  - bert
  - pytorch
  - transformers
  - fine-tuning
  - nlp
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
model-index:
  - name: bert-emotion-classifier
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: dair-ai/emotion
          type: dair-ai/emotion
        metrics:
          - type: accuracy
            value: 0.93
            name: Test Accuracy
          - type: f1
            value: 0.92
            name: Macro F1
---

# 🧠 BERT Emotion Classifier

Fine-tuned [`bert-base-uncased`](https://huggingface.co/bert-base-uncased) on the [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion) dataset for **multi-class emotion detection** in English text.

## Model Description

This model classifies English text into one of **6 emotional categories**:

| Label | Emotion | Description |
|-------|---------|-------------|
| 0 | 😢 sadness | Grief, melancholy, sorrow |
| 1 | 😄 joy | Happiness, excitement, delight |
| 2 | ❤️ love | Affection, warmth, attachment |
| 3 | 😠 anger | Frustration, rage, indignation |
| 4 | 😨 fear | Anxiety, dread, apprehension |
| 5 | 😲 surprise | Astonishment, unexpectedness |

## Performance

| Metric | Score |
|--------|-------|
| Test Accuracy | **~93%** |
| Macro F1 | **~92%** |
| Weighted F1 | **~93%** |

## Usage

```python
from transformers import BertTokenizerFast, BertForSequenceClassification
import torch
import torch.nn.functional as F

# Load model
tokenizer = BertTokenizerFast.from_pretrained("punithreddy-ai/bert-emotion-classifier")
model     = BertForSequenceClassification.from_pretrained("punithreddy-ai/bert-emotion-classifier")
model.eval()

LABELS = ["sadness", "joy", "love", "anger", "fear", "surprise"]
EMOJIS = ["😢", "😄", "❤️", "😠", "😨", "😲"]

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = F.softmax(logits, dim=-1)[0]
    idx   = probs.argmax().item()
    return {
        "label":      LABELS[idx],
        "emoji":      EMOJIS[idx],
        "confidence": f"{probs[idx].item():.1%}",
        "all_scores": {LABELS[i]: f"{probs[i].item():.1%}" for i in range(6)}
    }

# Examples
print(predict("I just got promoted — I'm over the moon!"))
# {'label': 'joy', 'emoji': '😄', 'confidence': '96.3%', ...}

print(predict("I can't stop crying. I miss him so much."))
# {'label': 'sadness', 'emoji': '😢', 'confidence': '94.1%', ...}

print(predict("How DARE they treat people like that!"))
# {'label': 'anger', 'emoji': '😠', 'confidence': '91.7%', ...}
```

### Using the pipeline API

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="punithreddy-ai/bert-emotion-classifier",
    return_all_scores=True,
)

results = classifier("I can't believe we actually won!")
# [{'label': 'joy', 'score': 0.89}, {'label': 'surprise', 'score': 0.07}, ...]
```

## Training Details

| Hyperparameter | Value |
|---------------|-------|
| Base model | `bert-base-uncased` |
| Max sequence length | 128 tokens |
| Batch size | 32 |
| Learning rate | 2e-5 |
| LR schedule | Linear warmup (10%) + linear decay |
| Epochs | 4 |
| Weight decay | 0.01 |
| Dropout | 0.1 |
| Optimizer | AdamW (ε=1e-8) |
| Gradient clipping | 1.0 |
| Seed | 42 |

## Training Data

[`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion) — English Twitter messages labelled with one of six emotions.

| Split | Samples |
|-------|---------|
| Train | 16,000 |
| Validation | 2,000 |
| Test | 2,000 |

## Architecture

```
Input Text
    ↓
[BertTokenizerFast] → input_ids + attention_mask
    ↓
[bert-base-uncased]
  • 12 transformer encoder layers
  • 12 attention heads  
  • 768 hidden dimensions
  • 110M total parameters
    ↓
[CLS] token → [Dropout 0.1] → [Linear 768→6] → [Softmax]
    ↓
Probability distribution over 6 emotions
```

## Limitations

- Trained on English Twitter data — may underperform on formal text, other dialects, or non-English input
- Short texts (< 5 words) may produce less confident predictions
- Ambiguous emotions (e.g. bittersweet) may be misclassified as the model assigns a single label
- Class imbalance in the dataset (joy and sadness dominate) may affect minority class performance

## Citation

If you use this model, please cite the original dataset:

```bibtex
@inproceedings{saravia-etal-2018-carer,
    title = "{CARER}: Contextualized Affect Representations for Emotion Recognition",
    author = "Saravia, Elvis and Liu, Hsien-Chi Toby and Huang, Yi-Hsin and Wu, Jing and Chen, Yi-Shin",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    year = "2018",
    publisher = "Association for Computational Linguistics",
}
```

## Author

Built by **Punithreddy** as a portfolio project demonstrating BERT fine-tuning for NLP classification.
