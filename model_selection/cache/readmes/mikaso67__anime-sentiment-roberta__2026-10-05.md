---
language: en
license: mit
base_model: roberta-base
pipeline_tag: text-classification
tags:
- sentiment-analysis
- roberta
---

# anime-sentiment-roberta

`roberta-base` fine-tuned for binary sentiment classification on MyAnimeList reviews.

## Training

- Data: MyAnimeList Comment Dataset V2 (Kaggle). Ratings 1-4 labeled negative, 8-10 positive, 5-7 dropped.
- Stratified 10k subset, 80/20 split.
- 512 tokens, 2 epochs, learning rate 2e-5, effective batch size 16, fp16, T4 GPU.

## Results (2,000 test reviews)

| Accuracy | F1 |
|---|---|
| 0.966 | 0.978 |

A TF-IDF + logistic regression baseline gets F1 = 0.952 on the same task.

## Limitations

There is no "mixed" class, so nuanced reviews get a forced positive/negative verdict. Indirect phrasing (e.g. ending an otherwise positive-sounding review with "i'll pass") can still fool the model.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="mikaso67/anime-sentiment-roberta")
clf("Not boring at all, actually it was amazing.")
```

Code and notebooks: https://github.com/mikaso67/anime-sentiment-analysis
