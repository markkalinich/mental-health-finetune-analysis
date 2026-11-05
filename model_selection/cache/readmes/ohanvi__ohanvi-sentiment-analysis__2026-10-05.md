---
language:
  - en
license: apache-2.0
library_name: transformers
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - imdb
  - pytorch
pipeline_tag: text-classification
datasets:
  - imdb
metrics:
  - accuracy
  - f1
model-index:
  - name: ohanvi-sentiment-analysis
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: IMDb
          type: imdb
          split: test
        metrics:
          - type: accuracy
            value: 0.932
            name: Accuracy
          - type: f1
            value: 0.931
            name: F1
---

# 🎬 Ohanvi Sentiment Analysis

A fine-tuned **DistilBERT** model for binary sentiment analysis on movie reviews.
Given any text it predicts whether the sentiment is **positive** or **negative**.

## Model Details

| Attribute | Value |
|-----------|-------|
| **Base model** | `distilbert-base-uncased` |
| **Fine-tuned on** | [IMDb Movie Reviews](https://huggingface.co/datasets/imdb) |
| **Task** | Text Classification (Sentiment Analysis) |
| **Labels** | `positive` (1) / `negative` (0) |
| **Max sequence length** | 512 tokens |
| **Framework** | PyTorch + 🤗 Transformers |
| **License** | Apache 2.0 |

## Performance

Evaluated on the IMDb test split (25 000 samples):

| Metric | Score |
|--------|-------|
| Accuracy | ~93.2% |
| F1 (binary) | ~93.1% |

## Quick Start

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ohanvi/ohanvi-sentiment-analysis",
)

result = classifier("This movie was absolutely fantastic!")
# → [{'label': 'positive', 'score': 0.9978}]

result = classifier("Terrible film, complete waste of time.")
# → [{'label': 'negative', 'score': 0.9965}]
```

## Training Details

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| Epochs | 3 |
| Batch size (train) | 16 |
| Learning rate | 2e-5 |
| Weight decay | 0.01 |
| Warmup ratio | 10% |
| Optimiser | AdamW |
| LR scheduler | Linear with warmup |

### Training Data

The model was fine-tuned on the full [IMDb](https://huggingface.co/datasets/imdb) dataset:
- **Train**: 25 000 reviews (12 500 positive, 12 500 negative)
- **Test**: 25 000 reviews (12 500 positive, 12 500 negative)

### Training Environment

- Hardware: GPU (NVIDIA / Apple Silicon MPS)
- Mixed precision: fp16 (when CUDA available)
- Early stopping: patience = 2 epochs

## How to Use (Advanced)

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "ohanvi/ohanvi-sentiment-analysis"
tokenizer  = AutoTokenizer.from_pretrained(model_name)
model      = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

text   = "An outstanding film with incredible performances."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    logits = model(**inputs).logits

probs      = torch.softmax(logits, dim=-1)
label_id   = probs.argmax().item()
label      = model.config.id2label[label_id]
confidence = probs[0][label_id].item()

print(f"Label: {label}  ({confidence:.1%})")
```

## Limitations

- Trained exclusively on **English** movie reviews; performance on other languages or domains may be lower.
- Very short texts (< 5 words) may produce less reliable results.
- The model inherits any biases present in the IMDb dataset.

## Citation

If you use this model, please cite:

```bibtex
@misc{ohanvi-sentiment-2026,
  title   = {Ohanvi Sentiment Analysis},
  author  = {Gourav Bansal},
  year    = {2026},
  url     = {https://huggingface.co/ohanvi/ohanvi-sentiment-analysis},
}
```

## Acknowledgements

Built with 🤗 [Transformers](https://github.com/huggingface/transformers),
🤗 [Datasets](https://github.com/huggingface/datasets), and
[Gradio](https://gradio.app/).
