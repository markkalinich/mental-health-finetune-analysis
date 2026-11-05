---
language: en
license: apache-2.0
tags:
- text-classification
- suicidal-detection
pipeline_tag: text-classification
datasets:
- jsfactory/mental_health_reddit_posts
metrics:
- accuracy
base_model:
- distilbert/distilbert-base-uncased
library_name: transformers
---

# Suicidal Detection System

This is a fine-tuned model based on a transformer architecture distilBERT for detecting suicidal intent or ideation in text. This model purpose is for text-classification in suicidal detection system.

Example output

| Text Input                       | Label    | Score |
| :------------------------------- | :--------| :---- |
| "I want to jump off this bridge" | Suicidal | 0.89  |

## Example

```python
from transformers import pipeline, DistilBertTokenizer, DistilBertForSequenceClassification

tokenizer = DistilBertTokenizer.from_pretrained("Kebinnuil/suicidal_detection_model")
model = pipeline("text-classification", model="Kebinnuil/suicidal_detection_model")

result = model("I want to jump off the bridge")
print(result)
```

## Training Metrics
The dataset was split into 80/10/10 for train/validation/test set. Table below shows the result of the model's training metrics.

| Epoch | Training Loss | Validation Loss | Accuracy | AUC      |
| :---- | :------------ | :-------------- | :------- | :------- |
| 1     | 0.442800      | 0.348061        | 0.838000 | 0.925000 |
| 2     | 0.304100      | 0.331631        | 0.850000 | 0.935000 |
| 3     | 0.261600      | 0.329701        | 0.851000 | 0.936000 |


## Classification Report

| Class | Precision | Recall | F1-score | Support |
| :---- | :-------- | :----- | :------- | :------ |
| 0     | 0.87      | 0.84   | 0.85     | 1211    |
| 1     | 0.84      | 0.87   | 0.86     | 1189    |

**Accuracy**: 0.86  
**Macro avg**: Precision 0.86, Recall 0.86, F1-score 0.86  
**Weighted avg**: Precision 0.86, Recall 0.86, F1-score 0.86  
**Total samples**: 2400


## Mapping Config
Please follow the config.json

![image](https://cdn-uploads.huggingface.co/production/uploads/672985374068ee4f2b97705a/sgVF7mt8vZAQw8v9wLulW.png)
