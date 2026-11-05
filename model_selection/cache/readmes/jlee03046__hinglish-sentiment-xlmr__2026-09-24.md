---
license: apache-2.0
language:
- hi
- en
base_model:
- FacebookAI/xlm-roberta-base
tags:
- hinglish
- sentiment-analysis
- code-mixed
- hindi
---

# Hinglish Sentiment Analysis Model

First free open-source sentiment analysis model for **Hinglish** (Hindi-English code-mixed) text.

## Model Details
- **Base Model:** XLM-RoBERTa Base
- **Task:** 3-class Sentiment Analysis (Positive / Negative / Neutral)
- **Language:** Hinglish (Hindi-English code-mixed)
- **Dataset:** 17,000+ real social media samples
- **Test Accuracy:** 68.5%

## How to Use

\`\`\`python
from transformers import pipeline

classifier = pipeline("text-classification", model="jlee03046/hinglish-sentiment-xlmr")

result = classifier("yaar ye movie bahut bakwaas thi")
print(result)  # [{'label': 'LABEL_0', 'score': 0.91}]
\`\`\`

## Labels
- LABEL_0 = Negative
- LABEL_1 = Neutral  
- LABEL_2 = Positive

## Why This Matters
No free, open-source Hinglish sentiment model existed before this.
Built for Indian startups, researchers, and developers working with Indian social media data.

## Author
Built by aditya — fresher passionate about Indian language NLP.