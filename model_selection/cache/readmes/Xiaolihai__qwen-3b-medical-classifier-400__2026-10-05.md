---
language: zh
license: mit
tags:
- medical
- classification
- chinese
- qwen
- qwen-3b
pipeline_tag: text-classification
---

# Qwen 3B Medical Department Classifier (400 Training Samples)

This is a fine-tuned Qwen 3B model for medical department classification on Chinese medical dialogues.


## Model Description

This model has been fine-tuned to classify medical dialogues into appropriate medical departments. It's based on the Qwen 3B model and has been specifically trained for Chinese medical text classification.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("Xiaolihai/qwen-3b-medical-classifier-400")
tokenizer = AutoTokenizer.from_pretrained("Xiaolihai/qwen-3b-medical-classifier-400")

```

## Training

The model was fine-tuned on medical dialogue data.

## License

This model is released under the MIT License.
