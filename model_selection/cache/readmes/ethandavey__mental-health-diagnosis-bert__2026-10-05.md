---
language: en
license: mit
tags:
  - mental-health
  - clinical
  - bert
  - text-classification
widget:
  - text: "I've been feeling very sad and empty lately, and I don't enjoy things anymore."
---

# Mental Health Diagnosis BERT Model

This model fine-tunes Bio_ClinicalBERT to predict mental health diagnoses from patient statements. 
It can classify text into 5 categories:
- Anxiety
- Depression
- Suicidal
- Stress
- Normal

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("YOUR_USERNAME/mental-health-diagnosis-bert")
model = AutoModelForSequenceClassification.from_pretrained("YOUR_USERNAME/mental-health-diagnosis-bert")

# Prepare text
text = "I've been feeling very anxious and worried all the time."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

# Make prediction
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = F.softmax(outputs.logits, dim=1)

# Map prediction to label
label_mapping = {0: "Anxiety", 1: "Normal", 2: "Depression", 3: "Suicidal", 4: "Stress"}
predicted_class = torch.argmax(probabilities, dim=1).item()
prediction = label_mapping[predicted_class]
confidence = probabilities[0][predicted_class].item()

print(f"Prediction: {prediction}, Confidence: {confidence:.2f}")
```
