---
library_name: transformers
tags:
- sentiment-analysis
- bert
- text-classification
license: apache-2.0
language:
- id
base_model: indobenchmark/indobert-base-p1
pipeline_tag: text-classification
---


# Sentiment BERT Tweet

A BERT model fine-tuned for Indonesian tweet sentiment classification.  
This model classifies tweets into three sentiment categories:

- **Positive**
- **Negative**
- **Neutral**

## How to Use

```python
from transformers import pipeline

model = pipeline("text-classification", model="VIOLET21/sentiment-bert-tweet")
result = model("Saya sangat senang hari ini!")
print(result)



