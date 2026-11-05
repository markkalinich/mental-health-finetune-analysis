---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- text-classification
- emotion-detection
- modernbert
- pytorch
- safetensors
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: text-classification
widget:
- text: "I am absolutely thrilled about our project breakthrough!"
  example_title: "Joy"
- text: "I cannot shake this feeling of dread and uncertainty."
  example_title: "Fear"
- text: "I feel completely heartbroken and alone today."
  example_title: "Sadness"
- text: "How could they betray our trust like this?"
  example_title: "Anger"
---

# ModernBERT Emotion Classifier

A fine-grained, 6-class emotion classification model built on top of **`answerdotai/ModernBERT-base`** (149M parameters) and trained on the **`dair-ai/emotion`** benchmark.

## Model Details
- **Architecture:** ModernBERT Encoder with Sequence Classification Head
- **Context Length:** 8,192 tokens native support
- **Embedding Dimension:** 768
- **Number of Labels:** 6 (`sadness`, `joy`, `love`, `anger`, `fear`, `surprise`)
- **Weights Format:** SafeTensors

## Quantitative Benchmark Results (Test Split)

| Evaluation Metric | Score |
| :--- | :--- |
| **Accuracy** | **92.25%** |
| **Macro F1** | **87.02%** |
| **Weighted F1** | **92.15%** |
| **Weighted Precision** | **92.16%** |
| **Weighted Recall** | **92.25%** |

### Classification Breakdown
```text
              precision    recall  f1-score   support
     sadness     0.9652    0.9535    0.9593       581
         joy     0.9371    0.9640    0.9504       695
        love     0.8699    0.7987    0.8328       159
       anger     0.9061    0.9127    0.9094       275
        fear     0.8596    0.9018    0.8802       224
    surprise     0.7736    0.6212    0.6891        66
```

## Usage Example

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="HR26kk/modernbert-emotion-classifier")

result = classifier("I am genuinely proud of what we accomplished today.")
print(result)
```
