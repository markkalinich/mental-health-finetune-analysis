---
language:
- id
license: mit
tags:
- sentiment-analysis
- indonesian
- indobert
- text-classification
- context-conditioned
datasets:
- custom
base_model: indobenchmark/indobert-large-p2
pipeline_tag: text-classification
model-index:
- name: indobert-binary-sentiment-classifier
  results:
  - task:
      type: text-classification
      name: Binary Sentiment Classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9606
    - name: F1 Macro
      type: f1
      value: 0.9494
---

# IndoBERT Binary Sentiment Classifier

A context-conditioned **binary** sentiment classifier for Indonesian text, fine-tuned from [IndoBERT Large P2](https://huggingface.co/indobenchmark/indobert-large-p2) (335M parameters). This is the binary variant of [apriandito/indobert-sentiment-classifier](https://huggingface.co/apriandito/indobert-sentiment-classifier) (3-class), designed for use cases that only need polarity detection (Negatif / Positif) without a Netral class.

Like its sibling models, this model evaluates sentiment *in relation to a given topic context*, making it more accurate for topic-specific analysis such as brand monitoring, public opinion polling, and crisis detection.

## Model Details

| Property | Value |
|----------|-------|
| **Base model** | [indobenchmark/indobert-large-p2](https://huggingface.co/indobenchmark/indobert-large-p2) (335M params) |
| **Task** | Context-conditioned binary sentiment classification |
| **Labels** | `NEGATIF` (0), `POSITIF` (1) |
| **Input format** | `[CLS] context [SEP] text [SEP]` |
| **Max length** | 256 tokens |
| **Training data** | 14,045 context-text pairs across 188 topics |

## Performance

Evaluated on a held-out validation set of 2,107 samples.

| Metric | Value |
|--------|-------|
| **Accuracy** | **96.06%** |
| **F1 Macro** | **0.949** |
| F1 Weighted | 0.961 |
| Precision Macro | 0.947 |
| Recall Macro | 0.952 |

### Comparison with 3-class variant

| Model | Classes | Accuracy | F1 Macro |
|-------|---------|----------|----------|
| **This model (binary)** | 2 (Negatif, Positif) | **96.06%** | **0.949** |
| [indobert-sentiment-classifier](https://huggingface.co/apriandito/indobert-sentiment-classifier) | 3 (Negatif, Netral, Positif) | 88.1% | 0.856 |

> The binary model achieves higher metrics because the task is simpler (no ambiguous Netral class). Choose binary when you only care about polarity; choose 3-class when you need to distinguish neutral text.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("apriandito/indobert-binary-sentiment-classifier")
model = AutoModelForSequenceClassification.from_pretrained("apriandito/indobert-binary-sentiment-classifier")
model.eval()

LABELS = {0: "Negatif", 1: "Positif"}

context = "harga sembako"
text = "harga beras naik terus bikin rakyat susah"

encoding = tokenizer(context, text, truncation=True, max_length=256, return_tensors="pt")
with torch.no_grad():
    probs = torch.softmax(model(**encoding).logits, dim=-1)[0]
    pred = torch.argmax(probs).item()

print(f"{LABELS[pred]} ({probs[pred]:.4f})")
# Output: Negatif (0.9987)
```

## Why Context Matters

Standard sentiment models classify text in isolation. This can lead to errors when sentiment depends on context:

| Context | Text | With Context | Without Context |
|---------|------|--------------|-----------------|
| harga sembako | harganya gila-gilaan | **Negatif** | ??? |
| produk luxury | harganya gila-gilaan | **Positif** | ??? |
| korupsi | KPK tangkap bupati korupsi dana bansos | **Positif** | Negatif |
| polusi udara | Jakarta peringkat 1 paling berpolusi | **Negatif** | Positif |

## Training Details

- **Data**: Derived from the same 31,360 context-text pairs used in the 3-class model. Netral samples (17,315) were dropped, leaving 14,045 binary samples (10,357 Negatif / 3,688 Positif).
- **Epochs**: 5 (best at epoch 4, early stopping patience 2)
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Optimizer**: AdamW (weight decay 0.01, warmup ratio 0.1)
- **Loss**: CrossEntropyLoss with class weights (Negatif: 0.678, Positif: 1.904)
- **GPU**: NVIDIA RTX 4090

## When to Use Which Model

| Use Case | Recommended Model |
|----------|-------------------|
| Filter irrelevant text first | [indobert-relevancy-classifier](https://huggingface.co/apriandito/indobert-relevancy-classifier) |
| Full sentiment breakdown (pos/neu/neg) | [indobert-sentiment-classifier](https://huggingface.co/apriandito/indobert-sentiment-classifier) |
| Polarity only (pos/neg) | **This model** |

### Suggested Pipeline

```
Raw Text → Relevancy Filter → Sentiment Analysis (3-class or binary)
```

1. Use [indobert-relevancy-classifier](https://huggingface.co/apriandito/indobert-relevancy-classifier) to filter relevant text
2. Use this model (or the 3-class variant) to classify sentiment on relevant text only

## Related Models

| Model | Task | Labels | Accuracy |
|-------|------|--------|----------|
| [indobert-relevancy-classifier](https://huggingface.co/apriandito/indobert-relevancy-classifier) | Relevancy | Relevant / Not Relevant | 96.5% |
| [indobert-sentiment-classifier](https://huggingface.co/apriandito/indobert-sentiment-classifier) | Sentiment (3-class) | Negatif / Netral / Positif | 88.1% |
| **indobert-binary-sentiment-classifier** | **Sentiment (binary)** | **Negatif / Positif** | **96.06%** |

All three models share the same architecture (IndoBERT Large P2, 335M params) and the same context-conditioned input format (`[CLS] context [SEP] text [SEP]`).

## Citation

```bibtex
@misc{saputra2026indobert-binary-sentiment,
  title={IndoBERT Binary Sentiment Classifier: Context-Conditioned Binary Sentiment Classification for Indonesian Text},
  author={Saputra, Muhammad Apriandito Arya},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/apriandito/indobert-binary-sentiment-classifier}
}
```
