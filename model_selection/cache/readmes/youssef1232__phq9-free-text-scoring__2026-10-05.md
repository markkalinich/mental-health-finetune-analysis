---
language: en
license: mit
tags:
- text-classification
- sentiment-analysis
- bert
pipeline_tag: text-classification
library_name: transformers
---

# PHQ-9 Free Text Scoring

A BERT-based model that predicts PHQ-9 depression severity from free-text responses.

## Model Details

- Architecture: BERT
- Task: Text Classification
- Framework: Transformers
- Classes:
  - 0: Minimal
  - 1: Mild
  - 2: Moderate
  - 3: Moderately Severe
  - 4: Severe

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="youssef1232/phq9-free-text-scoring"
)

result = classifier("I feel hopeless and have lost interest in everything")
print(result)