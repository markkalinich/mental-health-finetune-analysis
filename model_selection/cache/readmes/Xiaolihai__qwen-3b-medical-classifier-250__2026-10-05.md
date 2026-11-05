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


## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("Xiaolihai/qwen-3b-medical-classifier-250")
tokenizer = AutoTokenizer.from_pretrained("Xiaolihai/qwen-3b-medical-classifier-250")

```

## Training

The model was fine-tuned on medical dialogue data.

## License

This model is released under the MIT License.
