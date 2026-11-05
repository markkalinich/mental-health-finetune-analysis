🧠 Mental Health Discussion Topic Classifier

This repository contains a fine-tuned DistilBERT (`distilbert-base-uncased`) model trained to automatically classify mental health discussion threads, support queries, and social media posts into structured topic categories.

---

📌 Model Details

* **Developed by:** Eman Fatima
* **Model Architecture:** Transformer-based Sequence Classification (`distilbert-base-uncased`)
* **Framework:** PyTorch & Hugging Face Transformers
* **Language(s):** English (`en`)
* **License:** Apache 2.0

---

 🎯 Intended Uses & Limitations

### Primary Use Cases:
* **Topic Classification:** Automatically categorize mental health forum posts, discussions, or user statements into relevant sub-topics.
* **Triage & Analysis:** Assist platforms in routing queries or analyzing mental health discussion trends.

### Limitations:
* **Not a Medical Device:** This model is purely intended for natural language understanding and informational classification. It is **not** designed to diagnose mental health conditions or provide medical advice.

---

 💻 How to Use

You can easily load and run predictions using Hugging Face's `transformers` library in Python:

```python
import torch
import joblib
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModelForSequenceClassification

REPO_ID = "emanfatima123/mental-health-topic-classifier"

 1. Load Tokenizer and Model
tokenizer = AutoTokenizer.from_pretrained(REPO_ID)
model = AutoModelForSequenceClassification.from_pretrained(REPO_ID)
model.eval()

2. Download and Load Label Encoder
try:
    encoder_path = hf_hub_download(repo_id=REPO_ID, filename="label_encoder.pkl")
    label_encoder = joblib.load(encoder_path)
except Exception:
    label_encoder = None

3. Perform Inference
def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=-1)
        pred_id = torch.argmax(probs, dim=-1).item()
        confidence = probs[0][pred_id].item()

    if label_encoder is not None:
        label = label_encoder.inverse_transform([pred_id])[0]
    else:
        label = model.config.id2label.get(pred_id, f"Class {pred_id}")

    return label, confidence

 Example Prediction
sample_text = "I feel so overwhelmed with my upcoming university exams and assignments."
topic, score = classify_text(sample_text)

print(f"Predicted Topic: {topic}")
print(f"Confidence Score: {score * 100:.2f}%")