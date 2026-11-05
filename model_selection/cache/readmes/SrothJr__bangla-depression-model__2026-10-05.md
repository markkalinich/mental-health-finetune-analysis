---
base_model:
- sagorsarker/bangla-bert-base
---
# Bangla Depression Detection Model

A fine-tuned transformer model for Bangla text depression detection.

## Model Details

- **Task**: Text classification (4 classes)
- **Base Model**: BanglaBERT
- **Language**: Bangla

## Classes

- 0: Normal
- 1: Mild  
- 2: Moderate
- 3: Severe

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "SrothJr/bangla-depression-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Inference
text = "আপনার বাংলা টেক্সট এখানে"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    
logits = outputs.logits
predicted_class = logits.argmax(-1).item()
print(f"Predicted class: {predicted_class}")
```

## Training

This model was fine-tuned on a Bangla depression detection dataset using the Hugging Face Transformers library.

## License

MIT

## Citation

If you use this model, please cite:

```
@model{bangla_depression_model_2026,
  author = {SrothJr},
  title = {Bangla Depression Detection Model},
  year = {2026}
}
```