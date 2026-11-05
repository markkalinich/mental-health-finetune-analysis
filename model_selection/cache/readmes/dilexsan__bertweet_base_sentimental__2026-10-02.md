---
language: en
tags:
- sentiment-analysis
- text-classification
datasets:
- your-dataset-name
widget:
- text: "I am so happy with this service, it was great!"
license: mit
---



## Usage

You can load this model directly using the 🤗 Transformers pipeline:

```python
from transformers import pipeline

model_id = "dilexsan/bertweet_base_sentimental"

sentiment_analyzer = pipeline("text-classification", model=model_id)

text = "I am so happy with this service, it was great!"
result = sentiment_analyzer(text)

print(result)
