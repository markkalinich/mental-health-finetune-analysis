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
---

# bert-imdb-512

`bert-base-uncased` fine-tuned on the IMDB sentiment classification dataset with `max_seq_length=512`.

Trained as a victim model for adversarial NLP research (TextBugger / TextFooler / DeepWordBug-style attacks). The longer input window (vs. the typical 128-token TextAttack baselines) prevents truncation of ~95–98% of IMDB reviews and yields a stronger classifier.

## Model Details

- **Architecture**: `bert-base-uncased` (12 layers, 768 hidden, 12 heads, ~110M parameters)
- **Tokenization**: WordPiece (subwords)
- **Max sequence length**: 512 tokens
- **Task**: Binary sentiment classification (positive / negative)

## Training

Trained from `bert-base-uncased` on the IMDB train split (25,000 examples) using [TextAttack](https://github.com/QData/TextAttack) 0.3.x.

| Hyperparameter | Value |
| --- | --- |
| Epochs | 5 |
| Per-device batch size | 8 |
| Gradient accumulation | 2 (effective batch 16) |
| Learning rate | 2e-5 |
| Weight decay | 0.01 |
| Warmup steps | 500 |
| Random seed | 786 |
| Hardware | NVIDIA RTX 3090 (24 GB) |

Training command:

```
textattack train --model-name-or-path bert-base-uncased \
  --dataset imdb \
  --model-max-length 512 \
  --epochs 5 \
  --per-device-train-batch-size 8 \
  --gradient-accumulation-steps 2 \
  --learning-rate 2e-5 \
  --save-last \
  --output-dir ./models/bert-imdb-512
```

## Evaluation

Evaluated on the IMDB test split (25,000 examples) at the best epoch checkpoint:

| Metric | Value |
| --- | --- |
| Accuracy | **94.14%** |

For reference, the equivalent TextAttack baseline at 128 tokens (`textattack/bert-base-uncased-imdb`) reports ~89% on the same test set.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("jongador/bert-imdb-512")
model = AutoModelForSequenceClassification.from_pretrained("jongador/bert-imdb-512")

inputs = tokenizer("I loved this movie!", return_tensors="pt", truncation=True, max_length=512)
outputs = model(**inputs)
prediction = outputs.logits.argmax(-1).item()  # 0 = negative, 1 = positive
```

## License

MIT
