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

# Qwen 3B Medical Department Classifier

This is a fine-tuned Qwen 3B model for medical department classification on Chinese medical dialogues.

## Model Details

- **Base Model**: Qwen 3B
- **Task**: Medical Department Classification
- **Language**: Chinese (zh)
- **Number of Classes**: 44
- **Classes**: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']

## Model Description

This model has been fine-tuned to classify medical dialogues into appropriate medical departments. It's based on the Qwen 3B model and has been specifically trained for Chinese medical text classification.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("Xiaolihai/qwen-3b-medical-classifier")
tokenizer = AutoTokenizer.from_pretrained("Xiaolihai/qwen-3b-medical-classifier")

# Example usage
text = "患者描述胸痛症状，需要进一步检查"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
predictions = outputs.logits.argmax(dim=-1)
```

## Training

The model was fine-tuned on medical dialogue data with 400 training samples.

## License

This model is released under the MIT License.
