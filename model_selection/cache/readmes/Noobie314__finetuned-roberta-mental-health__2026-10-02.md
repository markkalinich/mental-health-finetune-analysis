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
- mental/mental-roberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
- RoBERTa
- mental-health-nlp
- emotion-classification
- mental-health-therapy
- fine-tuned-mental-health
---
# 🧠 Finetuned RoBERTa for Mental Health Text Classification

This model is a fine-tuned version of `roberta-base` for detecting mental health-related categories from textual content. It classifies user-generated posts into **five categories**:

- 🟦 Depression  
- 🟨 Anxiety  
- 🔴 Suicidal  
- 🟩 Addiction  
- 🟪 Eating Disorder  

It is designed to support research, digital therapy tools, and emotion-aware systems.

## 📁 Model Details

- **Base model**: `mental-roberta-base`
- **Fine-tuned on**: Custom Kaggle-aggregated dataset of mental health-related posts
- **Output**: Single-label classification (one of the five categories)
- **Loss function**: Cross-entropy
- **Format**: PyTorch model with Hugging Face Transformers compatibility

## 🧪 Dataset

The dataset used for training and testing was compiled from multiple Kaggle sources involving real-world discussions related to mental health. It contains posts categorized into the five emotion/mental-health topics.

- Training samples were selected from five original CSV files and combined into a single file.
- Testing data was kept separate and sourced similarly.

> 📦 **You can find the dataset here**: [Noobie314/mental-health-posts-dataset](https://huggingface.co/datasets/Noobie314/mental-health-posts-dataset)

## 🛠️ How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "Noobie314/finetuned-roberta-mental-health"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I'm feeling hopeless and tired of everything..."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

# Get predicted label
predicted_class = outputs.logits.argmax(dim=1).item()
```

## 📊 Evaluation

The model was evaluated on a held-out test set with standard metrics:

- **Accuracy**: 78.32%  
- **F1 Score (macro)**: 82.22%  
- **Precision & Recall**: Reported per class

| Category        | Precision  | Recall    | F1-Score  | Support |
|-----------------|------------|-----------|-----------|---------|
| Addiction       | 94.62%     | 91.40%    | 92.98%    | 1000    |
| Anxiety         | 88.19%     | 82.31%    | 85.15%    | 1996    |
| Depression      | 77.13%     | 72.86%    | 74.93%    | 3990    |
| Eating Disorder | 92.77%     | 93.60%    | 93.18%    | 1000    |
| Suicidal        | 59.67%     | 71.01%    | 64.85%    | 1994    |

## ✅ Intended Uses

This model is intended for:

- Research on mental health-related NLP
- Emotion-aware content moderation
- Digital therapy assistants

> ⚠️ **Disclaimer**: This model is not intended for medical diagnosis or treatment. It should not be used as a substitute for professional mental health support.

## 📜 License

This project is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

---

📬 For questions or collaborations, feel free to reach out through the Hugging Face hub.

---