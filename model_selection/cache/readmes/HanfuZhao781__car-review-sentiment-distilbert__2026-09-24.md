---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - distilbert
  - car-reviews
base_model: distilbert-base-uncased
---

# Car Review Sentiment, DistilBERT

distilbert-base-uncased fine-tuned for 3-class sentiment on real Edmunds car owner reviews, for a per-aspect word-of-mouth analyzer.

- Labels: 0 negative, 1 neutral, 2 positive
- Data: Edmunds consumer car reviews, florentgbelidji/car-reviews, labels by distant supervision from the 1 to 5 star rating.
- Test set of 3,652 held-out reviews: accuracy 86.7 percent, macro-F1 0.566.
- Known limits, measured: negation and sarcasm are hard. See the stress tests in the project repo. Deploy with confidence-gated abstention.

## Usage

    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch
    m = "HanfuZhao781/car-review-sentiment-distilbert"
    tok = AutoTokenizer.from_pretrained(m)
    model = AutoModelForSequenceClassification.from_pretrained(m)
    x = tok("The engine is powerful but the fuel economy is terrible", return_tensors="pt")
    print(model(**x).logits.softmax(-1))

App: https://HanfuZhao781-car-review-sentiment.hf.space
Code: https://github.com/hanfuzhao/Module2-CarReviewSentiment

Built for the 540 Summer Module 2 hackathon.
