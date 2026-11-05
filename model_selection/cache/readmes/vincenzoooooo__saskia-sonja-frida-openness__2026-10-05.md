---
tags:
- personality-prediction
- psychology
- text-classification
- roberta
- recruitment
- big-five
language:
- en
datasets:
- pandora
pipeline_tag: text-classification
library_name: transformers
---

# Saskia, Sonja & Frida - Personality Detection System: Openness Prediction

This model predicts **openness** personality trait levels (low, medium, high) from text input for recruitment applications.

## 🎯 Model Overview

- **Task**: 3-class personality classification 
- **Trait**: Openness (Big Five personality dimension)
- **Classes**: Low, Medium, High
- **Domain**: Social media → Job interview responses
- **Application**: Digital recruitment screening

## 🏗️ Model Details

- **Base Model**: RoBERTa-base
- **Architecture**: Transformer encoder + classification head
- **Training Data**: PANDORA dataset (Reddit comments)
- **Framework**: PyTorch + Transformers
- **Author**: Saskia, Sonja & Frida
- **Project**: NLP Shared Task 2025 - University of Antwerp

## 🚀 Quick Start

```python
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch
import json
from huggingface_hub import hf_hub_download

# Load model and tokenizer
model = RobertaForSequenceClassification.from_pretrained("vincenzoooooo/saskia-sonja-frida-openness")
tokenizer = RobertaTokenizer.from_pretrained("vincenzoooooo/saskia-sonja-frida-openness")

# Load label encoder
label_encoder_path = hf_hub_download(repo_id="vincenzoooooo/saskia-sonja-frida-openness", filename="label_encoder.json")
with open(label_encoder_path, 'r') as f:
    label_data = json.load(f)
    classes = label_data['classes']  # ['low', 'medium', 'high']

# Make prediction
text = "I love meeting new people and trying new experiences!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
outputs = model(**inputs)
predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
prediction = classes[predicted_class_id]
print(f"Openness: {prediction}")
```

## 📊 Training Details

- **Optimizer**: AdamW (lr=2e-5)
- **Epochs**: 2-3
- **Batch Size**: 4-8 (memory optimized)
- **Max Sequence Length**: 128 tokens
- **Device**: CPU/GPU with memory optimization

## 🎨 Use Cases

- **Digital Recruitment**: Screen job candidates
- **HR Analytics**: Analyze communication styles  
- **Research**: Study personality in text
- **Chatbots**: Personality-aware responses

## ⚠️ Limitations

- **Domain Gap**: Trained on Reddit, applied to job interviews
- **Bias**: May reflect Reddit user demographics
- **Language**: English only
- **Context**: Short text segments only
- **Small Dataset**: Limited training samples

## 📝 Citation

```bibtex
@misc{saskia_sonja_frida_openness_2025,
  title={Saskia, Sonja & Frida - Personality Detection System: Openness Prediction},
  author={Saskia, Sonja & Frida},
  year={2025},
  howpublished={\url{https://huggingface.co/vincenzoooooo/saskia-sonja-frida-openness}},
  note={NLP Shared Task 2025 - University of Antwerp}
}
```

## 🤝 Related Models

Check out our complete personality prediction suite:
- [Openness](vincenzoooooo/saskia-sonja-frida-openness)
- [Conscientiousness](vincenzoooooo/saskia-sonja-frida-conscientiousness)  
- [Extraversion](vincenzoooooo/saskia-sonja-frida-extraversion)
- [Agreeableness](vincenzoooooo/saskia-sonja-frida-agreeableness)
- [Emotional Stability](vincenzoooooo/saskia-sonja-frida-emotional_stability)

---
*Developed by **Saskia, Sonja & Frida** for NLP Shared Task 2025 - University of Antwerp*
