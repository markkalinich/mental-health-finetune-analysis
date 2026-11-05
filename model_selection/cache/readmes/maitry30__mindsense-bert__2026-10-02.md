---
language: ["en"]
license: mit
tags:
  - mental-health
  - bert
  - text-classification
  - nlp
  - transformers
  - explainable-ai
  - shap
datasets:
  - kaggle-sentiment-analysis-mental-health
metrics:
  - accuracy
  - f1
---

 # 🧠 MindSense-BERT — AI-Powered Mental Health Detection
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![BERT](https://img.shields.io/badge/Model-BERT-orange?style=flat-square)
![Accuracy](https://img.shields.io/badge/Accuracy-89%25-green?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)
---
MindSense-BERT is a fine-tuned BERT-based model designed to **classify text into 7 mental health categories** using real-world Reddit data.
It combines **state-of-the-art NLP, class imbalance handling, and explainable AI (SHAP)** to create a transparent and practical mental health analysis system.

---

## 📌 Model Overview

* **Model Type:** Transformer (BERT)

* **Base Model:** `bert-base-uncased`

* **Task:** Multi-class Text Classification

* **Classes (7):**

  * Normal
  * Depression
  * Anxiety
  * Bipolar
  * PTSD
  * Stress
  * Personality Disorder

* **Framework:** PyTorch + Hugging Face Transformers

* **Deployment:** Streamlit + Hugging Face Hub

---

## 🎯 Problem Statement

Mental health conditions affect **1 in 4 people globally**, but early detection is difficult due to stigma and lack of awareness.

This model aims to:

* Analyze user-written text
* Detect potential mental health conditions
* Enable early awareness and intervention

---

## 📊 Dataset

* **Source:** Kaggle — *Sentiment Analysis for Mental Health*
* **Size:** 53,000+ Reddit posts
* **Input:** `statement` (text)
* **Label:** `status` (mental health category)

### Categories:

* Normal
* Depression
* Anxiety
* Bipolar
* PTSD
* Stress
* Personality Disorder

---

## ⚙️ Preprocessing

* Removed URLs, special characters, duplicates
* Handled missing values
* Tokenized using BERT tokenizer
* Lowercasing (uncased model)
* Padding & truncation applied

---

## 🔬 Training Methodology

### Phase 1 — Baseline Models

* TF-IDF (10k features, uni + bi-grams)
* Logistic Regression, Random Forest, SVM

### Phase 2 — BERT Fine-tuning

* Pretrained `bert-base-uncased`
* 3 epochs
* Learning rate: `1e-5`
* Batch size: `16`
* Trained on Google Colab T4 GPU

---

### Phase 3 — Class Imbalance Handling

* Weak classes identified: Stress, Personality Disorder
* Techniques used:

  * Word swap
  * Random deletion
  * Key phrase duplication
* Applied custom class weights

---

## 📈 Model Performance

### Accuracy Comparison

| Model               | Accuracy    |
| ------------------- | ----------- |
| Logistic Regression | ~78%        |
| Random Forest       | ~74%        |
| SVM                 | ~82%        |
| BERT (initial)      | ~83%        |
| **BERT (final)**    | **~87–89%** |

---

### Per-Class F1 Score

| Category             | F1 Score |
| -------------------- | -------- |
| Normal               | 0.91     |
| Depression           | 0.89     |
| Anxiety              | 0.86     |
| Bipolar              | 0.84     |
| PTSD                 | 0.87     |
| Stress               | 0.82     |
| Personality Disorder | 0.80     |

---

## 🔍 Explainability (SHAP)

This model integrates **SHAP (SHapley Additive Explanations)** for transparency:

* 🔴 Red words → push prediction toward a class
* 🔵 Blue words → push prediction away

This improves trust and interpretability — critical in healthcare AI.

---

## 🚀 Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "maitry30/mindsense-bert"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I feel completely hopeless and empty."

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)

prediction = torch.argmax(outputs.logits, dim=1).item()
print(prediction)
```

---

## 🧪 Example Predictions

| Input Text                  | Predicted Class |
| --------------------------- | --------------- |
| "I feel hopeless and empty" | Depression      |
| "I keep having nightmares"  | PTSD            |
| "My mood swings a lot"      | Bipolar         |
| "I feel fine today"         | Normal          |

---

## 🛠 Tech Stack

* Python 3.10
* PyTorch
* Hugging Face Transformers
* Scikit-learn
* SHAP
* Pandas, NumPy
* Matplotlib, Seaborn
* Streamlit (UI)
* Hugging Face Hub (model hosting)

---

## ⚠️ Limitations

* Limited to English text
* May struggle with sarcasm or slang
* Depends on dataset quality
* Not suitable for real clinical diagnosis

---

## ⚖️ Ethical Considerations

* This model is for **educational purposes only**
* Not a replacement for mental health professionals
* Should not be used for medical decisions
* Predictions require human interpretation

---

## 🔐 Safety Notice

* ❌ Not a diagnostic tool
* ❌ Not for emergency use
* ✅ Can assist awareness and research

---

## 🚀 Future Work

* Multilingual support (Hindi + regional languages)
* Voice-based mental health detection
* Multi-modal AI (text + physiological signals)
* Explainable AI improvements
* Production deployment (AWS/Azure)

---

## 👤 Author

**Maitry**

* GitHub: https://github.com/Maitry09/mindsense-mental-health
* Hugging Face: https://huggingface.co/maitry30
* Live App: https://mindsense.streamlit.app

---

## 📄 License

MIT License

---

> ⭐ If you found this model useful, consider giving the project a star!
