---
language: 
- en
tags:
- token-classification
- ner
- pytorch
- custom-model
library_name: transformers
---

# UnmaskingQwen3 for Token Classification

This model is a fine-tuned version of a custom UnmaskingQwen3ForTokenClassification model for token classification tasks.

## Model Details

- **Model Type**: Custom UnmaskingQwen3ForTokenClassification
- **Task**: Token Classification (NER/POS/Chunking)
- **Training Framework**: Transformers + Accelerate

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("your-username/your-model-name", trust_remote_code=True)
model = AutoModelForTokenClassification.from_pretrained("your-username/your-model-name", trust_remote_code=True)

# Use for inference
inputs = tokenizer(["Your text here"], return_tensors="pt", is_split_into_words=False)
outputs = model(**inputs)
predictions = outputs.logits.argmax(dim=-1)
```

## Training Details

- **Training Data**: ['automated-analytics/ai4privacy-pii-masking-en-v1-ner-coarse', 'automated-analytics/gretel-pii-masking-en-v1-ner-coarse']
- **Learning Rate**: 5e-05
- **Batch Size**: 128
- **Epochs**: 3
- **Max Length**: 128

## Important Note

This model uses a custom model class. Make sure to use `trust_remote_code=True` when loading the model.
