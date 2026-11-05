---
license: apache-2.0
tags:
  - text-classification
  - emotion-detection
  - bert
  - huggingface
language:
  - en
pipeline_tag: text-classification
---

# BERT-based Emotion Classification Model 🎭

This model is a fine-tuned version of BERT for **emotion classification**. It predicts one of six emotion categories from a given English text input.

## 🧠 Model Details

- **Architecture**: `BertForSequenceClassification`
- **Base Model**: `bert-base-uncased`
- **Labels**:
  - `0`: sadness
  - `1`: joy
  - `2`: love
  - `3`: anger
  - `4`: fear
  - `5`: surprise
- **Problem Type**: Single-label classification
- **Hidden Size**: 768
- **Max Sequence Length**: 512
- **Number of Layers**: 12

## 🚀 How to Use

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="AbhishekBhavnani/TweetClassification")
result = classifier("I'm feeling so happy today!")
print(result)
```

##  Example 

**Input**:
```text
I can't stop smiling, this movie is too funny!
```

**Output**: 
```text
[{'label': 'joy', 'score': 0.9821}]
```
