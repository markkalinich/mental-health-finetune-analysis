---
license: mit
language:
- pt
metrics:
  accuracy:
    Neutral: 0.99
    Positive: 0.97
    Negative: 0.98
base_model: neuralmind/bert-base-portuguese-cased
library_name: transformers
tags:
- sentiment analysis
- nlp
- glassdoor
pipeline_tag: text-classification
---

# BERTimbau for Sentiment Analysis of Glassdoor Reviews

## Introduction
This model fine-tunes [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) 
for sentiment analysis of Glassdoor reviews about IT companies in Cuiabá.

The dataset used to train the model consists of 2,532 reviews sourced from Glassdoor. 

For more detail about the project, follow my [GitHub](https://github.com/stevillis/glassdoor-reviews-analysis-nlp).

### Example Usage
```python
from transformers import pipeline

pipe = pipeline("text-classification", model="stevillis/bertimbau-finetuned-glassdoor-reviews")

result = pipe("Empresa boa para trabalhar")

print(result) # Expected output: [{'label': 'positive', 'score': 0.9993522763252258}]
```