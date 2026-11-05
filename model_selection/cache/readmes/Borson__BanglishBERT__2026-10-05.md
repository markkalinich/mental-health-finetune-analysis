---
license: apache-2.0
tags:
- sentiment-analysis
- bangla
- banglish
- fine-tuned
- bert
---

# BanglishBERT

This is a fine-tuned `csebuetnlp/banglishbert` model for Bangla/Banglish sentiment analysis.
The model was fine-tuned on a custom dataset with three labels: `negative`, `neutral`, `positive`.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo_id = "Borson/BanglishBERT"
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

# Example usage
text = "এই সিনেমাটা খুব ভালো লেগেছে!" # This movie was very good!
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
predicted_label = model.config.id2label[predicted_class_id]

print(f"Text: {text}")
print(f"Predicted label: {predicted_label}")
```
