---
language:
- bn
tags:
- text-classification
- mental-health
- depression-detection
- transformer
- bert-base-multilingual-cased
license: mit
datasets:
- depression-social-media
metrics:
- accuracy
- f1
base_model: google-bert/bert-base-multilingual-cased
model-index:
- name: banglamentalBERT on mBERT (DAPT) - Depression Severity Detection
  results: []
---

# banglamentalBERT on mBERT (DAPT) - Depression Severity Detection

This is a **Domain-Adaptive Pre-Trained (DAPT)** model for detecting depression severity in Bangla social media text. 
A robust multilingual model capable of handling mixed-language (Code-Mixed) scenarios.

## Model Details
- **Base Architecture**: [google-bert/bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased)
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
model_name = "SrothJr/banglamentalBERT-mBERT-dapt"
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