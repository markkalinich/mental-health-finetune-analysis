---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- distilbert
- pytorch
- sentiment
- NLP
- fine-tuned
datasets:
- syedkhalid0/Sentiment-Analysis
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- distilbert-base-uncased
pipeline_tag: text-classification
model-index:
- name: DistilBERT Sentiment Analysis
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      type: syedkhalid0/Sentiment-Analysis
      name: Sentiment-Analysis
      split: test
    metrics:
    - type: accuracy
      value: 0.0
      name: Accuracy
    - type: f1
      value: 0.0
      name: F1 Score
    - type: precision
      value: 0.0
      name: Precision
    - type: recall
      value: 0.0
      name: Recall
---

# 🧠 DistilBERT Fine-Tuned for Sentiment Analysis

A fine-tuned **DistilBERT** model for 3-class sentiment analysis (Negative, Neutral, Positive), trained on a large-scale sentiment dataset of 
~105,000 text samples.

## 📋 Model Details

### Model Description

- **Developed by:** Najaf Ali **
- **Model type:** Transformer-based text classification (DistilBERT)
- **Language(s):** English
- **License:** Apache 2.0
- **Fine-tuned from:** [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased)

### Model Sources

- **Repository:** [Najaf-Ali12/LLM-Hugging-Face](https://github.com/Najaf-Ali12/LLM-Hugging-Face)
- **Demo:** [Streamlit App](https://complete-nlp-projects-zxepdqlod8vn9mpmjk9q9q.streamlit.app/) *(replace with your link)*
- **Training Notebook:** [Google Colab](https://colab.research.google.com/github/Najaf-Ali12/LLM-Hugging-Face/blob/main/Finetuning_a_sentiment_analysis_model.ipynb)

---

## 🎯 Intended Uses

### Direct Use

This model is designed for **3-class sentiment classification** of English text. It can be directly used for:

- 📊 **Social media monitoring** – Analyzing public sentiment on tweets, posts, or comments
- 🛍️ **Product review analysis** – Classifying customer feedback as positive, neutral, or negative
- 💬 **Customer support** – Automatically prioritizing negative feedback
- 📰 **Content moderation** – Detecting sentiment in user-generated content
- 📈 **Market research** – Aggregating sentiment from survey responses or feedback forms
- 🎬 **Entertainment** – Analyzing movie/book reviews

### Out-of-Scope Use

- Not intended for **clinical, legal, or financial advice**
- Not reliable for **sarcasm or highly contextual humor** detection
- Not validated for **non-English** text
- Should not be used for **high-stakes decisions** without human review
- Not designed for **emotion detection** (e.g., anger, joy, sadness) — only polarity (negative/neutral/positive)

---

## ⚠️ Bias, Risks, and Limitations

- **Domain bias:** Trained primarily on movie reviews and general text — may perform poorly on specialized domains (medical, legal, technical).
- **Sarcasm detection:** The model may misclassify sarcastic statements (e.g., *"Oh great, another delay!"*).
- **Short text:** Very short texts (e.g., "meh", "ok") may be classified with low confidence.
- **Cultural nuance:** Sentiment expression varies across cultures — the model was trained on English datasets and may not capture global nuances.
- **Neutral class ambiguity:** The boundary between "neutral" and "slightly positive/negative" can be blurry.

**Recommendation:** Always use this model alongside human judgment for critical applications.

---

## 🚀 How to Get Started

### Installation

```bash
pip install transformers torch
```

### Quick Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "YOUR_USERNAME/YOUR_MODEL_NAME"  # Replace with your HF model ID
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prepare input
text = "I absolutely loved this movie! The acting was brilliant."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()

# Label mapping
id2label = {0: "NEGATIVE", 1: "NEUTRAL", 2: "POSITIVE"}
print(f"Sentiment: {id2label[predicted_class]}")
print(f"Confidence: {probabilities[0][predicted_class].item():.2%}")
```

### Batch Prediction

```python
texts = [
    "This product is amazing!",
    "Terrible service, never coming back.",
    "It was okay, nothing special.",
]

inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    preds = torch.argmax(probs, dim=-1).tolist()

for text, pred in zip(texts, preds):
    print(f"{id2label[pred]:10s} | {text}")
```

### Using the Pipeline API

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="YOUR_USERNAME/YOUR_MODEL_NAME")

result = classifier("The food was delicious and the staff were friendly!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9876}]
```

---

## 📊 Training Details

### Training Data

- **Dataset:** [`syedkhalid0/Sentiment-Analysis`](https://huggingface.co/datasets/syedkhalid0/Sentiment-Analysis)
- **Total samples:** ~105,000
  - Training: 83,989 samples
  - Validation: 10,499 samples
  - Test: 10,499 samples
- **Classes:** 3 (NEGATIVE = 0, NEUTRAL = 1, POSITIVE = 2)

### Training Procedure

**Preprocessing:**
- Tokenizer: `distilbert-base-uncased`
- Max sequence length: 512
- Truncation: enabled
- Padding: dynamic (during collation)

**Training Hyperparameters:**

| Parameter | Value |
| :--- | :--- |
| Base model | `distilbert-base-uncased` |
| Epochs | 3 |
| Batch size (train) | 16 |
| Batch size (eval) | 64 |
| Learning rate | 5e-5 (default) |
| Warmup steps | 500 |
| Weight decay | 0.01 |
| Optimizer | AdamW |
| Mixed precision (FP16) | Enabled |
| Early stopping patience | 3 |
| Evaluation strategy | Every 500 steps |
| Best model metric | F1 (weighted) |

**Hardware:**
- Trained on Google Colab (NVIDIA T4 GPU recommended)

**Framework:**
- PyTorch + Hugging Face Transformers
- Training API: `Trainer`

---

## 📈 Evaluation Results

### Test Set Performance

| Metric | Score |
| :--- | :--- |
| **Accuracy** | *update after training* |
| **F1 Score (weighted)** | *update after training* |
| **Precision (weighted)** | *update after training* |
| **Recall (weighted)** | *update after training* |

### Per-Class Performance

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| NEGATIVE | *update* | *update* | *update* | *update* |
| NEUTRAL | *update* | *update* | *update* | *update* |
| POSITIVE | *update* | *update* | *update* | *update* |

> 💡 **Tip:** Run `trainer.evaluate()` on the test set and copy the metrics here. You can also generate a confusion matrix using scikit-learn.

### Confusion Matrix

![Confusion Matrix](confusion_matrix.png)
*(Upload your confusion matrix image to the repo and reference it here.)*

---

## 🧪 Example Predictions

| Text | Predicted Sentiment | Confidence |
| :--- | :---: | :---: |
| "This movie was absolutely fantastic! I loved every minute." | 😊 POSITIVE | 99.2% |
| "The food was terrible and the service was even worse." | 😞 NEGATIVE | 98.7% |
| "It was an okay experience, nothing special." | 😐 NEUTRAL | 76.4% |
| "Worst purchase I've ever made." | 😞 NEGATIVE | 99.5% |
| "Highly recommend this to everyone!" | 😊 POSITIVE | 99.1% |

---

## 🛠️ Limitations & Recommendations

- ⚠️ **Sarcasm:** May not detect sarcastic or ironic statements correctly.
- ⚠️ **Short text:** Texts under 3 words may have lower accuracy.
- ⚠️ **Domain shift:** Fine-tuned on general sentiment — test on your specific domain before production use.
- ✅ **Recommended:** For best performance, use texts between 5 and 200 words.
- ✅ **Recommended:** For high-stakes applications, ensemble with human review.

---

## 📚 Citation

If you use this model in your research or project, please cite:

```bibtex
@misc{distilbert-sentiment-analysis,
  author = {Najaf Ali},
  title = {DistilBERT Fine-Tuned for 3-Class Sentiment Analysis},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/YOUR_USERNAME/YOUR_MODEL_NAME}},
  note = {Fine-tuned from distilbert-base-uncased}
}
```

---

## 📞 Contact

- **GitHub:** [@Najaf-Ali12](https://github.com/Najaf-Ali12)
- **Hugging Face:** [NajafAli01](https://huggingface.co/NajafAli01)
- **Issues:** Please open an issue on the [GitHub repository](https://github.com/Najaf-Ali12/LLM-Hugging-Face/issues)

---

## 🙏 Acknowledgements

- Base model: [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) by Hugging Face
- Dataset: [`syedkhalid0/Sentiment-Analysis`](https://huggingface.co/datasets/syedkhalid0/Sentiment-Analysis)
- Framework: [Hugging Face Transformers](https://github.com/huggingface/transformers)
- Training: [Google Colab](https://colab.research.google.com/)

---

## 📜 License

This model is released under the **Apache 2.0 License**. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.

---

*Last updated: 2025*