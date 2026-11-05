---
language:
- en
- hi
license: mit
tags:
- sentiment-analysis
- text-classification
- hindi
- hinglish
- code-mixed
- muril
datasets:
- imdb
- glue
- yelp_polarity
- tweet_eval
- ai4bharat/IndicSentiment
metrics:
- accuracy
- f1
widget:
- text: "This movie was absolutely fantastic, I loved every minute!"
- text: "ye movie achi hai"
- text: "यह फिल्म बहुत अच्छी है"
- text: "movie thik thak tha, kuch khaas nahi"
---

# Sentiment Analysis v2 — MuRIL (English + Hindi + Hinglish)

A 3-class sentiment classifier (**Negative / Neutral / Positive**) fine-tuned from
[`google/muril-base-cased`](https://huggingface.co/google/muril-base-cased), which unlike the
v1 `roberta-base` model can natively handle **Hindi (Devanagari)** and **Hinglish (romanized
code-mixed Hindi-English)** text in addition to English.

## Model details

| | |
|---|---|
| Base model       | `google/muril-base-cased` |
| Task             | Text classification (3-class sentiment) |
| Languages        | English, Hindi, Hinglish (code-mixed) |
| Training rows    | 96,761 (train) / 8,538 (val) / 8,538 (test) |
| Max sequence len | 128 tokens |

## Training data

- **English:** IMDB, SST-2 (GLUE), Yelp Polarity, Tweet Eval (sentiment)
- **Hindi / Hinglish:** ai4bharat/IndicSentiment, Hindi-English code-mixed tweet datasets

Classes were capped per-label and a class-weighted loss was used during training to reduce the
effect of English data outnumbering Hindi/Hinglish data.

## Test set results

```
              precision    recall  f1-score   support

    Negative       0.90      0.85      0.87      3000
     Neutral       0.81      0.89      0.85      2538
    Positive       0.87      0.84      0.86      3000

    accuracy                           0.86      8538
   macro avg       0.86      0.86      0.86      8538
weighted avg       0.86      0.86      0.86      8538

```

![Confusion Matrix](confusion_matrix.png)
![Training Curves](training_curves.png)

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="airzipm/sentiment-analysis-muril-v2")
print(clf("ye movie achi hai"))
print(clf("यह फिल्म बहुत अच्छी है"))
print(clf("This was a great experience!"))
```

## Limitations

- Hindi/Hinglish training data is much smaller than English data (tens of thousands vs. hundreds
  of thousands of rows) — expect somewhat lower accuracy on Hindi/Hinglish than on English.
- Code-mixed spelling varies a lot informally (e.g. "acha"/"accha"/"achha") — coverage depends on
  what appeared in the training tweets.
- Not evaluated on domains far from reviews/social media (e.g. formal news, legal text).
