---
license: mit
tags:
- mental-health
- depression
- anxiety
- stress
- multiclass-classification
- SCCMR
language:
- en
library_name: pytorch
pipeline_tag: text-classification
base_model: alfiyahqthz/sccmr-mda
---

# SCCMR Multiclass: Depression/Anxiety/Stress Classification

Fine-tuned from [SCCMR-MDA](https://huggingface.co/alfiyahqthz/sccmr-mda) for multiclass mental health classification.

## Model Description

Classifies text posts into one of three mental health conditions:
- Depression (Class 0)
- Anxiety (Class 1)
- Stress (Class 2)

## Performance

**Validation Results (Epoch 9):**
- Accuracy: 0.8880
- Loss: 0.5826
- F1 (Macro): 0.8729

## Architecture

- Base: Pre-trained SCCMR-MDA (trained on 21k DASS-21 posts)
- Text Encoder: BERT-base-uncased
- Projection: 768 → 512 (pre-trained)
- Classifier: 512 → 256 → 3

## Usage

```python
import torch
from transformers import BertTokenizer

# Load model and tokenizer
model = torch.load("pytorch_model.bin")
tokenizer = BertTokenizer.from_pretrained("alfiyahqthz/sccmr-multiclass")

# Predict
text = "I feel so depressed and worthless"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
logits = model(inputs['input_ids'], inputs['attention_mask'])
prediction = logits.argmax(dim=1).item()

# prediction: 0=Depression, 1=Anxiety, 2=Stress
```

## License

MIT
