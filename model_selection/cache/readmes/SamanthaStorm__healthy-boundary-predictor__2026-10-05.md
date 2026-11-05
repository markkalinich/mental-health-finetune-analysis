---
license: apache-2.0
tags:
- text-classification
- boundary-detection
- mental-health
- communication
pipeline_tag: text-classification
---

# Healthy Boundary Predictor

This model classifies text as representing healthy or unhealthy boundary-setting communication.

## Model Description

- **Task**: Binary text classification
- **Labels**: 
  - 1: Healthy boundary communication
  - 0: Unhealthy boundary communication

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="SamanthaStorm/healthy-boundary-predictor")
result = classifier("I need some space to think about this decision.")
print(result)
```

## Training Data

The model was trained on a dataset of boundary-setting examples, including:
- Professional boundary scenarios
- Personal relationship boundaries
- Family communication examples
- Financial boundary situations
- Emotional boundary examples

## Limitations

This model is intended for educational and research purposes. It should not be used as a substitute for professional mental health advice.
