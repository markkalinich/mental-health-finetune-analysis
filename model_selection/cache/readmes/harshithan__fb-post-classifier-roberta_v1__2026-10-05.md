---
license: mit
language:
- en
metrics:
- f1
- accuracy
base_model:
- cardiffnlp/twitter-roberta-base
datasets:
- custom
tags:
- facebook
- text-classification
- sentiment
- customer-support
- transformers
- roberta
- huggingface
- fine-tuned
model-index:
- name: fb-post-classifier-roberta
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: Facebook Posts (Appreciation / Complaint / Feedback)
      type: custom
    metrics:
    - name: F1
      type: f1
      value: 0.8979
library_name: transformers
pipeline_tag: text-classification
---
# Facebook Post Classifier (RoBERTa Base, fine-tuned)

This model classifies short Facebook posts into **one** of the following **three mutually exclusive categories**:
- `Appreciation`
- `Complaint`
- `Feedback`

It is fine-tuned on ~8k manually labeled posts from business pages (e.g. Target, Walmart), based on the `cardiffnlp/twitter-roberta-base` model, which is pretrained on 58M tweets.

## 🧠 Intended Use

- Customer support automation
- Sentiment analysis on social media
- CRM pipelines or chatbot classification

## 📊 Performance

| Class        | Precision | Recall | F1 Score |
|--------------|-----------|--------|----------|
| Appreciation | 0.906     | 0.936  | 0.921    |
| Complaint    | 0.931     | 0.902  | 0.916    |
| Feedback     | 0.840     | 0.874  | 0.857    |
| **Average**  | –         | –      | **0.898** |

> Evaluated on 2039 unseen posts with held-out labels using macro-averaged F1.

## 🛠️ How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch

model = AutoModelForSequenceClassification.from_pretrained("harshithan/fb-post-classifier-roberta_v1")
tokenizer = AutoTokenizer.from_pretrained("harshithan/fb-post-classifier-roberta_v1")

inputs = tokenizer("I love the fast delivery!", return_tensors="pt")
outputs = model(**inputs)
probs = softmax(outputs.logits, dim=1)

label = torch.argmax(probs).item()
classes = ["Appreciation", "Complaint", "Feedback"]
print("Predicted:", classes[label])
```

## 🧾 License
MIT License

## 🙋‍♀️ Author
This model was fine-tuned by @harshithan.

## 📚 Academic Disclaimer
This model was developed as part of an academic experimentation project. It is intended solely for educational and research purposes.
The model has not been validated for production use and may not generalize to real-world Facebook or customer support data beyond the scope of the assignment.

