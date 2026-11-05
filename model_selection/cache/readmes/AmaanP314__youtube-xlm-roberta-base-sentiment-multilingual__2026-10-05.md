---
license: cc-by-4.0
metrics:
- accuracy
base_model:
- cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual
pipeline_tag: text-classification
datasets:
- AmaanP314/youtube-comment-sentiment
tags:
- youtube
- comments
- sentiment
- roberta
---

# Finetuned RoBERTa Sentiment Model

## Model Overview

This model is a version of the [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) model that has been fine-tuned on a custom dataset of YouTube comments. The fine-tuning process was designed to improve performance on sentiment analysis for YouTube comments, which often differ in tone, slang, and structure from other social media platforms. After fine-tuning, the model achieved an accuracy of **80.17%**.

## Intended Use

The model is designed for sentiment analysis of YouTube comments. It accepts a list of text inputs (comments) and returns a sentiment label for each comment:
- **Positive**
- **Neutral**
- **Negative**

This model can be used in applications such as video recommendation systems, content analysis dashboards, and other data analysis tasks where understanding audience sentiment is important.

## How to Use

The model can be used via an API endpoint or loaded locally using the Hugging Face Transformers library. For example, using Python:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "AmaanP314/youtube-xlm-roberta-base-sentiment-multilingual"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example input
comments = [
    "This video aged like honey.", # Positive
    "This video aged like milk.", # Negative
    "It was just okay." # Neutral
]

inputs = tokenizer(comments, return_tensors="pt", padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=1)
label_mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}
sentiments = [label_mapping[p.item()] for p in predictions]
print(sentiments)
```

## How It Was Trained

- **Base Model:** [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual)
- **Dataset:** A custom dataset consisting of over 1 million YouTube comments, each annotated with one of three sentiment labels (Positive, Neutral, Negative).
- **Fine-Tuning Process:** The model was fine-tuned using the following steps:
  - Data Cleaning and Preprocessing
  - Model Fine-Tuning
  - Evaluation and Testing

## Evaluation

The model was evaluated on a held-out test set of YouTube comments. It improved from a baseline accuracy of approximately 69.3% (when fine-tuned on Twitter data) to **80.17%** on this dataset. This improvement demonstrates the benefit of domain-specific fine-tuning.


## Citation

If you use this model in your research, please cite the original base model and this project:

```
@misc{cardiffnlp,
  title={Twitter-XLM-RoBERTa-Base-Sentiment-Multilingual},
  author={Cardiff NLP},
  year={2020},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual}}
}

@misc{AmaanP314,
  title={Youtube-XLM-RoBERTa-Base-Sentiment-Multilingual},
  author={Amaan Poonawala},
  year={2025},
  howpublished={\url{https://huggingface.co/AmaanP314/youtube-xlm-roberta-base-sentiment-multilingual}}
}
```

---