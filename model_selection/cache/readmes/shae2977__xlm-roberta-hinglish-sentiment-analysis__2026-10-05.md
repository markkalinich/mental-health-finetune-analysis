---
license: apache-2.0
language:
- hi
- en
metrics:
- f1
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
- hinglish
- youtube
- sentiment-analysis
- transformers
- pytorch
---
# XLM-RoBERTa Hinglish Sentiment Analysis

A fine-tuned [XLM-RoBERTa](https://huggingface.co/FacebookAI/xlm-roberta-base) model for sentiment classification of Hinglish text — the code-mixed Hindi-English language used by hundreds of millions of Indians online.

Most sentiment models are trained on clean English or formal Hindi. They fail badly on Hinglish because it is neither; it is a fluid mix of both, written in Roman script, full of slang, abbreviations, and cultural references. This model is trained specifically to handle that.

## Model details

| Property | Value |
|---|---|
| Base model | `FacebookAI/xlm-roberta-base` |
| Fine-tuned on | Self-annotated Hinglish YouTube comments |
| Task | 3-class sentiment classification |
| Classes | Negative (0), Neutral (1), Positive (2) |
| Training samples | ~2,500 |
| Test samples | ~638 |

## Performance
Evaluated on a held-out test set of Hinglish YouTube comments.

| Model | Weighted F1 |
|---|---|
| VADER (baseline) | 0.39 |
| **XLM-RoBERTa (this model)** | **0.67** |

VADER drops to 0.39 on Hinglish because it has no concept of Roman-script Hindi words like *acha*, *bahut*, *zabardast*, or mixed constructions like *"yaar this song is too good na?"*. XLM-RoBERTa's multilingual pretraining gives it a foundation to handle this naturally.

### Per-class results

| Class | Precision | Recall | F1 |
|---|---|---|---|
| Negative | 0.66 | 0.77 | 0.71 |
| Neutral | 0.60 | 0.48 | 0.53 |
| Positive | 0.70 | 0.64 | 0.67 |

Neutral is the hardest class as neutral comments are often ambiguous even for human annotators.

## Dataset

The training data is a self-annotated dataset of 3,000+ Hinglish YouTube comments scraped from Indian music, entertainment, and pop culture videos. Comments were manually labeled as Positive, Negative, or Neutral.

Dataset: [shae2977/hinglish-youtube-sentiment-dataset](https://huggingface.co/datasets/shae2977/hinglish-youtube-sentiment-dataset)

## Usage

```python
from transformers import XLMRobertaTokenizer, XLMRobertaForSequenceClassification
import torch

model_name = "shae2977/xlm-roberta-hinglish-sentiment-analysis"
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
model = XLMRobertaForSequenceClassification.from_pretrained(model_name)
model.eval()

labels = {0: "Negative", 1: "Neutral", 2: "Positive"}

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted = torch.argmax(outputs.logits, dim=1).item()
    return labels[predicted]

predict("yaar ye song bahut zabardast hai")   # Positive
predict("bilkul bekar tha")                   # Negative
predict("theek tha, kuch khaas nahi")         # Neutral
```

## Training details

| Hyperparameter | Value |
|---|---|
| Learning rate | 1e-5 |
| Batch size | 16 |
| Max sequence length | 128 |
| Optimizer | AdamW |
| Epochs | 7 |
| Random seed | 42 |
| Hardware | NVIDIA T4 (Google Colab) |

## Limitations

- Trained on YouTube comments from Indian entertainment content — may not generalize well to other domains like politics or sports
- Neutral class performance is weaker than Positive/Negative
- Dataset size is limited (~3,000 samples) — a larger annotated dataset would improve performance
- Overall weighted F1 of 0.67 means that comments may be miscalssified

## Author

Built by [shae2977](https://huggingface.co/shae2977) 