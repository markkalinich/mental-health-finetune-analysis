---
tags:
- autotrain
- text-classification
language:
- unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- khalidrizk/autotrain-data-mental-health
co2_eq_emissions:
  emissions: 0.5692214366862244
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 50364120416
- CO2 Emissions (in grams): 0.5692

## Validation Metrics

- Loss: 0.729
- Accuracy: 0.788
- Macro F1: 0.535
- Micro F1: 0.788
- Weighted F1: 0.772
- Macro Precision: 0.585
- Micro Precision: 0.788
- Weighted Precision: 0.768
- Macro Recall: 0.503
- Micro Recall: 0.788
- Weighted Recall: 0.788


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/khalidrizk/autotrain-mental-health-50364120416
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("khalidrizk/autotrain-mental-health-50364120416", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("khalidrizk/autotrain-mental-health-50364120416", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```