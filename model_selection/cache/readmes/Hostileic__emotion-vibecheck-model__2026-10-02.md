---
library_name: transformers
tags: [emotion-detection, text-classification, hinglish, nlp, sentiment, emotion-ai]
---

# 🧠 AI VibeCheck – Hinglish + English Emotion Detection Model

This is a fine-tuned **BERT-based model** trained on **10,000+ Hinglish + English samples** to detect human emotions from short text messages.  
Unlike most emotion datasets that are purely English, this model was built to understand **real Indian conversational language** including Hinglish words such as:

- **"udas" → sad**  
- **"gussa" → angry**  
- **"mast" → joy**  

It powers the deployed app 👉 [AI VibeCheck on Hugging Face Spaces](https://huggingface.co/spaces/Hostileic/emotion-vibecheck).

---

## 📖 Model Details

- **Developed by:** Jagrit Chaudhry  
- **Model type:** BERT for Sequence Classification  
- **Languages:** Hinglish + English (code-mixed)  
- **Fine-tuned from:** `bert-base-multilingual-cased`  
- **License:** MIT  

---

## 🚀 Uses

### Direct Use
- Emotion detection from raw text (English or Hinglish).  
- Can process screenshots of text via OCR (in the web app).  

Example:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "Hostileic/emotion-vibecheck-model"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

inputs = tokenizer("mujhe thoda gussa aa raha hai", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    prediction = torch.argmax(probs, dim=1).item()

print("Predicted Emotion:", model.config.id2label[prediction])


Downstream Use

Chatbots and virtual assistants that adapt to user emotions.

Emotion-aware analytics for social media or customer support.

Out-of-Scope

Long-form documents (works best on short text/snippets).

Non-Hinglish languages not present in training data.

⚠️ Bias, Risks, and Limitations

Model is biased towards Hinglish/English texting style, may underperform on formal text.

Limited coverage of rare emotions due to dataset size.

Misclassifications possible with sarcasm, irony, or mixed emotions.

📊 Training Details

Dataset: Custom synthetic + extended dataset (~10k samples, 10 emotion labels).

Training procedure: Fine-tuning bert-base-multilingual-cased with PyTorch + Hugging Face Transformers.

Hyperparameters:

Epochs: 5

Batch size: 32

Learning rate: 2e-5

Optimizer: AdamW

✅ Evaluation

Validation Accuracy: ~85%

Best performance on: Joy, Sadness, Anger

Challenging cases: Neutral and Surprise (overlaps in Hinglish texting).

⚡ Technical Specs

Architecture: BERT-base (multilingual)

Framework: PyTorch + Hugging Face Transformers

Training Hardware: NVIDIA GPU (single-GPU fine-tuning)

📌 Citation

If you use this model, please cite:

@misc{chaudhry2025emotionvibecheck,
  author = {Jagrit Chaudhry},
  title = {AI VibeCheck – Hinglish + English Emotion Detection},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Hostileic/emotion-vibecheck-model}}
}

📬 Contact

Author: Jagrit Chaudhry

Email: jagritworkchaudhry1409@gmail.com

GitHub: [Jagrit-09](https://github.com/Jagrit-09)

LinkedIn: [Jagrit Chaudhry](https://www.linkedin.com/in/jagrit-chaudhry-448690309/)
