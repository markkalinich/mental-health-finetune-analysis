---
license: apache-2.0
datasets:
- Noobie314/mental-health-posts-dataset
language:
- en
metrics:
- accuracy
- f1
- precision
base_model:
- nateraw/bert-base-uncased-emotion
pipeline_tag: text-classification
library_name: transformers
tags:
- mental-health
- emotion-recognition
- BERT
- mental-health-nlp
- text-classification
---
# 🧠 Finetuned BERT for Mental Health Text Classification

This model is a fine-tuned version of `bert-base-uncased` for detecting mental health-related categories from textual content. It classifies user-generated posts into **five categories**:

- 🟦 Depression  
- 🟨 Anxiety  
- 🔴 Suicidal  
- 🟩 Addiction  
- 🟪 Eating Disorder  

It is designed to support research, digital therapy tools, and emotion-aware systems.

---

## 📁 Model Details

- **Base model**: `bert-base-uncased`  
- **Fine-tuned on**: A custom dataset derived from multiple Kaggle sources  
- **Classification type**: Single-label (one of five categories)  
- **Loss function**: Cross-entropy  
- **Framework**: PyTorch, Hugging Face Transformers  

---

## 🧪 Dataset

The dataset used for training and testing was compiled from multiple Kaggle sources involving real-world discussions related to mental health. It contains posts categorized into the five emotion/mental-health topics.

- Training samples were selected from five original CSV files and combined into a single file.
- Testing data was kept separate and sourced similarly.

> 📦 **You can find the dataset here**: [Noobie314/mental-health-posts-dataset](https://huggingface.co/datasets/Noobie314/mental-health-posts-dataset)

---

## 🛠️ How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "Noobie314/finetuned-emotion-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I'm feeling hopeless and tired of everything..."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

predicted_class = outputs.logits.argmax(dim=1).item()
```

---

## 📊 Evaluation

The model was evaluated on a test set of 10,000 rows with the following results:

| Category        | Precision | Recall   | F1-Score | Support |
|-----------------|----------|----------|----------|---------|
| Addiction       | 0.914    | 0.911    | 0.912    | 1000    |
| Anxiety         | 0.831    | 0.808    | 0.819    | 1996    |
| Depression      | 0.772    | 0.621    | 0.688    | 3990    |
| Eating Disorder | 0.916    | 0.921    | 0.919    | 1000    |
| Suicidal        | 0.531    | 0.752    | 0.622    | 1994    |
| **Accuracy**    | **0.744**|          |          |         |
| **Macro avg**   | 0.793    | 0.803    | 0.792    | 9980    |
| **Weighted avg**| 0.764    | 0.744    | 0.747    | 9980    |

- **Accuracy**: 74.36%  
- **Macro Average F1-Score**: 0.792  
- **Weighted Average F1-Score**: 0.747  

These results indicate the model performs relatively well, with higher precision and recall for categories like **Eating Disorder** and **Addiction**.

---

## ✅ Intended Uses

This model is intended for:

- NLP research in mental health domains  
- Emotion-aware digital assistants  
- Content moderation tools focused on emotional tone and risk  

> ⚠️ **Disclaimer**: This model is not suitable for clinical or medical decision-making. It does not replace licensed mental health professionals.

---

## 📜 License

This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

---

📬 For questions, suggestions, or collaborations, feel free to open an issue or contact via the Hugging Face Hub.

---