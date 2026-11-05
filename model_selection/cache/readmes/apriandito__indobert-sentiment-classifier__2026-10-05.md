---
language: id
license: mit
tags:
  - sentiment-analysis
  - indonesian
  - indobert
  - context-conditioned
datasets:
  - custom
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# IndoBERT-Sentiment: Context-Conditioned Sentiment Classifier for Indonesian Text

A context-conditioned sentiment classifier built on **IndoBERT Large P2 (335M parameters)**. Unlike standard sentiment models that classify text in isolation, this model takes a topical context as additional input, enabling it to determine sentiment *with respect to a specific topic*.

## Model Details

- **Base model**: [indobenchmark/indobert-large-p2](https://huggingface.co/indobenchmark/indobert-large-p2) (335M params)
- **Task**: Context-conditioned 3-class sentiment classification
- **Labels**: Negatif (0), Netral (1), Positif (2)
- **Input format**: `[CLS] context [SEP] text [SEP]`
- **Training data**: 31,360 context-text pairs across 188 topics

## Performance

### Head-to-head benchmark on same test set (4,704 samples)

| Model | Type | Accuracy | F1 Macro | F1 Weighted |
|-------|------|----------|----------|-------------|
| **IndoBERT-Sentiment (ours)** | **context** | **88.1%** | **0.856** | **0.880** |
| BERT-Indonesian-SmSA | general | 62.1% | 0.486 | 0.607 |
| RoBERTa-Indonesian-Sentiment | general | 59.1% | 0.501 | 0.593 |
| IndoBERT-Sentiment-SmSA | general | 62.8% | 0.487 | 0.612 |

### Per-class F1

| Class | Ours | Best Baseline |
|-------|------|---------------|
| Negatif | 0.876 | 0.654 |
| Netral | 0.902 | 0.716 |
| Positif | 0.791 | 0.211 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("apriandito/indobert-sentiment-classifier")
model = AutoModelForSequenceClassification.from_pretrained("apriandito/indobert-sentiment-classifier")
model.eval()

LABELS = {0: "Negatif", 1: "Netral", 2: "Positif"}

context = "Pertumbuhan ekonomi Indonesia"
text = "ekonomi Indonesia tumbuh 5.2%, tertinggi di ASEAN"

encoding = tokenizer(context, text, truncation=True, max_length=256, return_tensors="pt")
with torch.no_grad():
    probs = torch.softmax(model(**encoding).logits, dim=-1)[0]
    pred = torch.argmax(probs).item()

print(f"{LABELS[pred]} ({probs[pred]:.4f})")
# Output: Positif (0.9999)
```

## Why Context Matters

Standard sentiment models classify text in isolation. This fails when sentiment depends on the topic:

| Context | Text | Ours | Baseline |
|---------|------|------|----------|
| Pertumbuhan ekonomi | ekonomi Indonesia tumbuh 5.2% | **Positif** | Netral |
| Inflasi dan daya beli | indomie sekarang 3500, dulu cuma 1500 | **Negatif** | Netral |
| Korupsi dan penegakan hukum | KPK tangkap bupati korupsi dana bansos | **Positif** | Netral |
| Polusi udara | Jakarta peringkat 1 paling berpolusi | **Negatif** | Positif |

## Training Details

- **Epochs**: 5 (early stopping patience 2)
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Max length**: 256 tokens
- **Class weights**: Negatif 1.009, Netral 0.604, Positif 2.834
- **GPU**: NVIDIA RTX 3090
- **Training time**: ~30 minutes

## Related Models

- [apriandito/indobert-relevancy-classifier](https://huggingface.co/apriandito/indobert-relevancy-classifier) - Context-conditioned relevancy classifier using the same architecture

## Citation

```bibtex
@article{saputra2026indobert-sentiment,
  title={IndoBERT-Sentiment: Context-Conditioned Sentiment Classification for Indonesian Text},
  author={Saputra, Muhammad Apriandito Arya and Alamsyah, Andry and Ramadhani, Dian Puteri and Siadari, Thomhert Suprapto and Fakhrurroja, Hanif},
  year={2026}
}
```
