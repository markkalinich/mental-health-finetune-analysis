---
license: mit
language: en
library_name: transformers
pipeline_tag: text-classification
datasets:
- imdb
metrics:
- accuracy
tags:
- text-classification
- sentiment-analysis
- bert
- imdb
- adversarial-nlp
- textattack
- deprecated
---

# bert-imdb-256

> ⚠️ **DEPRECATED — kept for legacy compatibility.**
> This model was trained with `max_seq_length=256` on a constrained-VRAM laptop GPU as a preliminary step. For new work, use [`jongador/bert-imdb-512`](https://huggingface.co/jongador/bert-imdb-512), which covers ~95–98% of IMDB reviews (vs. ~85–90%) and achieves higher accuracy (94.14% vs. 92.20%).

`bert-base-uncased` fine-tuned on the IMDB sentiment classification dataset with `max_seq_length=256`. Trained as a victim model for adversarial NLP research (TextBugger / TextFooler / DeepWordBug-style attacks).

## Model Details

- **Architecture**: `bert-base-uncased` (12 layers, 768 hidden, 12 heads, ~110M parameters)
- **Tokenization**: WordPiece (subwords)
- **Max sequence length**: 256 tokens
- **Task**: Binary sentiment classification (positive / negative)

## Training

Trained from `bert-base-uncased` on the IMDB train split (25,000 examples) using [TextAttack](https://github.com/QData/TextAttack) 0.3.x.

| Hyperparameter | Value |
| --- | --- |
| Epochs | 5 |
| Per-device batch size | 2 |
| Gradient accumulation | 8 (effective batch 16) |
| Learning rate | 2e-5 |
| Weight decay | 0.01 |
| Warmup steps | 500 |
| Random seed | 786 |
| Hardware | NVIDIA RTX 3050 Laptop (4 GB VRAM) |

The aggressive gradient accumulation (batch 2 × accum 8) was a workaround for the 4 GB VRAM ceiling on the laptop GPU used for this preliminary run. The newer [`jongador/bert-imdb-512`](https://huggingface.co/jongador/bert-imdb-512) variant uses batch 8 × accum 2 on a cluster RTX 3090 (24 GB).

## Evaluation

Best epoch checkpoint on the IMDB test split (25,000 examples):

| Metric | Value |
| --- | --- |
| Accuracy | 92.20% |

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("jongador/bert-imdb-256")
model = AutoModelForSequenceClassification.from_pretrained("jongador/bert-imdb-256")
```

## License

MIT
