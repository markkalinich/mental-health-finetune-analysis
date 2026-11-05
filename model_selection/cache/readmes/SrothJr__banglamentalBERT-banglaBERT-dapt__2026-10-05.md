---
language:
- bn
tags:
- text-classification
- mental-health
- depression-detection
- transformer
- banglabert
license: mit
datasets:
- depression-social-media
metrics:
- accuracy
- f1
base_model: csebuetnlp/banglabert
model-index:
- name: BanglamentalBERT on banglaBERT(DAPT) - Depression Severity Detection
  results: []
---

# BanglamentalBERT on banglaBERT(DAPT) - Depression Severity Detection

This is a **Domain-Adaptive Pre-Trained (DAPT)** model for detecting depression severity in Bangla social media text. 
The high-accuracy model based on ELECTRA architecture. Achieved best performance (~84% F1) in experiments.

## Model Details
- **Base Architecture**: [csebuetnlp/banglabert](https://huggingface.co/csebuetnlp/banglabert)
- **Training Method**: Domain-Adaptive Pre-Training (DAPT) on bangla mental health corpora, followed by Fine-Tuning.
- **Task**: Multi-class Classification (4 classes).
- **Language**: Bengali (Bangla).

## Label Mapping
The model outputs one of the following classes:
- **0**: Minimum/None
- **1**: Mild
- **2**: Moderate
- **3**: Severe

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model
model_name = "SrothJr/banglamentalBERT-banglaBERT-dapt"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Inference
text = "আপনার বাংলা টেক্সট এখানে (Your Bengali text here)"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    
predictions = torch.argmax(outputs.logits, dim=-1)
labels = ["Minimum", "Mild", "Moderate", "Severe"]
print(f"Prediction: {labels[predictions.item()]}")
```

## Citation

If you use this mode, please cite our research.