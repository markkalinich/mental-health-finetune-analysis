---
license: mit
language: en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- roberta
- youtube-comments
- podcast
---

# Podcast comment sentiment (3-class RoBERTa)

Fine-tuned RoBERTa classifier for 3-class sentiment of YouTube podcast comments.

## Labels
| id | label    |
|----|----------|
| 0  | negative |
| 1  | neutral  |
| 2  | positive |

## Quick start

```python
from transformers import pipeline

clf = pipeline("text-classification", model="randomone14/podcast-sentiment-3c")
clf("This episode was incredible — I learned so much.")
```

## Source project
Trained as part of the [PodcastLens](https://github.com/) comment-intelligence pipeline.
