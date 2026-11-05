---
language: ["id"]
license: apache-2.0
tags:
  - indobert
  - emotion-classification
  - text-classification
  - indonesia
datasets:
  - Chipan/indonesia-5-emotion-cls-dataset
model-index:
  - name: Emolog IndoBERT (Fine-tuned)
    results: []
---

# Emolog IndoBERT (Fine-tuned for Emotion Classification in Indonesian)

🚀 This model is a fine-tuned version of `indobenchmark/indobert-base-p2` on an Indonesian emotion classification dataset.  
It is trained to classify user-written daily mood/feeling texts into several emotional categories.

---

## 🧠 Model Details

- **Model Name**: Emolog IndoBERT
- **Base Model**: `indobenchmark/indobert-base-p2`
- **Fine-tuned by**: Atherizz
- **Language**: Indonesian (id)
- **Task**: Text Classification (Emotion Detection)
- **License**: Apache 2.0
- **Dataset**: Chipan/indonesia-5-emotion-cls-dataset
- **Trained using**: Hugging Face Transformers & PyTorch

---

## 📊 Labels (Emotions)

The model is trained to predict the following emotions:

- Senang (Happy)
- Sedih (Sad)
- Marah (Angry)
- Takut (Fear)
- Jijik (Disgust)
- Terkejut (Surprise)
- Netral

---


## 📦 Usage

You can use this model directly with the `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Atherizz/emolog-indobert")
model = AutoModelForSequenceClassification.from_pretrained("Atherizz/emolog-indobert")

inputs = tokenizer("aku capek dan bingung hari ini", return_tensors="pt")
outputs = model(**inputs)
predicted_class = torch.argmax(outputs.logits)
print(predicted_class)
