---
license: apache-2.0
---
# 🤖 DoctorBot: Symptoms → Disease Classifier

This model is a BERT-based classifier trained to predict diseases based on user-described symptoms in English. It can be used in chatbot systems or virtual assistants to assist in medical symptom triage.

---

## 🧠 Model Details

- **Base Model**: `bert-base-uncased`
- **Fine-tuned on**: 189,000+ symptom-disease pairs
- **Task**: Multi-class text classification
- **Language**: English
- **Input**: Free-text symptoms (e.g. `"I have chest pain and shortness of breath"`)
- **Output**: Disease label (e.g. `"Heart Attack"`)

---

## 📊 Dataset

- A custom medical dataset of [Symptoms, Disease] pairs.
- Cleaned, preprocessed and tokenized using Hugging Face's BERT tokenizer.

---

## 🏁 Training Info

- **Epochs**: 3  
- **Learning Rate**: 2e-5  
- **Batch Size**: 16 (train), 32 (eval)  
- **Validation Loss**: ~0.26
- **Accuracy** ~0.91
- **Framework**: 🤗 Transformers + PyTorch  
- **Training Platform**: Google Colab with Tesla T4 GPU

---

## 📦 How to Use

```python
from transformers import BertTokenizer, BertForSequenceClassification
from huggingface_hub import hf_hub_download
import torch

# Load model
model = BertForSequenceClassification.from_pretrained("maiserry/DoctorBot_symptoms_disease")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Predict
text = "My skin is itchy and I have a red rash"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
prediction = torch.argmax(outputs.logits, dim=1)
print("Predicted class:", prediction.item())
