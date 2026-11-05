---
tags: autotrain
language: en
widget:
- text: "I love AutoTrain 🤗"
datasets:
- rabiaqayyum/autotrain-data-mental-health-analysis
co2_eq_emissions: 313.3534743349287
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 752423172
- CO2 Emissions (in grams): 313.3534743349287

## Validation Metrics

- Loss: 0.6064515113830566
- Accuracy: 0.805171240644137
- Macro F1: 0.7253473044054398
- Micro F1: 0.805171240644137
- Weighted F1: 0.7970679970423672
- Macro Precision: 0.7477679873153633
- Micro Precision: 0.805171240644137
- Weighted Precision: 0.7966263131173029
- Macro Recall: 0.7143231260991618
- Micro Recall: 0.805171240644137
- Weighted Recall: 0.805171240644137


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/rabiaqayyum/autotrain-mental-health-analysis-752423172
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("rabiaqayyum/autotrain-mental-health-analysis-752423172", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("rabiaqayyum/autotrain-mental-health-analysis-752423172", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```