---
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- bert
- imdb
datasets:
- imdb
metrics:
- accuracy
- f1
---

# BERT IMDB Sentiment Classifier

Fine-tuned `bert-base-uncased` for binary sentiment classification on the
IMDB movie reviews dataset.

## Performance
| Metric    | Score |
|-----------|-------|
| Accuracy  | 0.934 |
| F1 (pos)  | 0.934 |

## Usage
\`\`\`python
from transformers import pipeline
clf = pipeline("text-classification", model="your-username/bert-imdb-sentiment")
clf("This movie was great!")
\`\`\`

## Training
Fine-tuned for 3 epochs, lr=2e-5, batch size 16, on a single GPU.
