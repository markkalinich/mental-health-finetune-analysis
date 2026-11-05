---
tags: autotrain
language: unk
widget:
- text: "I love AutoTrain 🤗"
datasets:
- justpyschitry/autotrain-data-Psychiatry_Article_Identifier
co2_eq_emissions: 13.4308931494349
---

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 990132822
- CO2 Emissions (in grams): 13.4308931494349

## Validation Metrics

- Loss: 0.3777158558368683
- Accuracy: 0.9177471636952999
- Macro F1: 0.9082952086962773
- Micro F1: 0.9177471636952999
- Weighted F1: 0.9175376430905807
- Macro Precision: 0.9175123149319843
- Micro Precision: 0.9177471636952999
- Weighted Precision: 0.9185452324503698
- Macro Recall: 0.9042000199743617
- Micro Recall: 0.9177471636952999
- Weighted Recall: 0.9177471636952999


## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/models/justpyschitry/autotrain-Psychiatry_Article_Identifier-990132822
```

Or Python API:

```
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("justpyschitry/autotrain-Psychiatry_Article_Identifier-990132822", use_auth_token=True)

tokenizer = AutoTokenizer.from_pretrained("justpyschitry/autotrain-Psychiatry_Article_Identifier-990132822", use_auth_token=True)

inputs = tokenizer("I love AutoTrain", return_tensors="pt")

outputs = model(**inputs)
```