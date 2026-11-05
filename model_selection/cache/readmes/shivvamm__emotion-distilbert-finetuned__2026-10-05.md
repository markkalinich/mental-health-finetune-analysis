---
license: mit
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
pipeline_tag: text-classification
library_name: transformers
tags:
  - emotions
  - text-classification
  - huggingface
  - distilbert
  - fine-tuned
  - nlp
  - sentiment
  - mental-health
model_name: emotion-distilbert-finetuned
language:
  - en
---

# 😄 Emotion Classifier — Fine-tuned DistilBERT

This is a **DistilBERT-based model** fine-tuned for **emotion classification** on the [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion) dataset.

It predicts one of 6 emotion labels for a given text:

- `sadness`
- `joy`
- `love`
- `anger`
- `fear`
- `surprise`

---

## 🧠 Model Details

- **Base model**: `distilbert-base-uncased`
- **Fine-tuned on**: `dair-ai/emotion`
- **Task**: Multi-class single-label text classification
- **Framework**: [🤗 Transformers](https://github.com/huggingface/transformers)

---

## 📊 Dataset

**Dataset:** [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion)

| Split      | Samples |
|------------|---------|
| Train      | 16,000  |
| Validation | 2,000   |
| Test       | 2,000   |
| Total      | 20,000  |

**Classes (labels):**

- `0` → sadness  
- `1` → joy  
- `2` → love  
- `3` → anger  
- `4` → fear  
- `5` → surprise  

---

## 🚀 Usage

You can use the model directly with the 🤗 Transformers pipeline:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="shivvamm/emotion-distilbert-finetuned", top_k=None)

text = "I feel hopeful and excited about the future."
results = classifier(text)
print(results)
```

### Example output:

```json
[{'label': 'joy', 'score': 0.9876}]
```

---

## ✅ Intended Use

* Social media and product review emotion analysis  
* Sentiment & psychological tone detection  
* Personal journaling or well-being apps  
* Academic research in NLP and affective computing

---

## ⚠️ Limitations

* Handles English language only  
* Classifies only **one dominant emotion per text**  
* May misclassify mixed emotions, sarcasm, or idioms  

---

## 📄 Citation

```bibtex
@misc{shivvamm2025emotion,
  title={Emotion Classification using DistilBERT},
  author={Shivvamm},
  year={2025},
  howpublished={\url{https://huggingface.co/shivvamm/emotion-distilbert-finetuned}},
  note={Fine-tuned on the dair-ai/emotion dataset}
}
```

---

## 👤 Author

**Shivvamm**  
Model: [shivvamm/emotion-distilbert-finetuned](https://huggingface.co/shivvamm/emotion-distilbert-finetuned)  
License: MIT

---

> 💡 Fine-tuned with 🤗 Hugging Face Transformers and Accelerate
