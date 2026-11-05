---
library_name: transformers
language:
- en
tags:
- text-classification
- multi-label
- goemotions
- distilbert
datasets:
- go_emotions
metrics:
- micro_f1
- macro_f1
pipeline_tag: text-classification
---

# GoEmotions DistilBERT Emotion Classifier

## Model Overview
This model is a fine-tuned version of **distilbert-base-uncased** for **multi-label emotion classification**. It predicts the probability of 28 possible emotions (27 emotion categories plus neutral). The model is trained using the GoEmotions dataset.

This classifier takes in a short piece of text and outputs a list of emotions along with confidence scores.

---

## Intended Use
- Emotion detection in short texts such as comments, headlines, messages, or social media posts  
- Educational demonstrations of multi-label classification  
- Research or experimentation with emotion analysis  

Not intended for clinical, legal, or high-stakes decision-making.

---

## Dataset
**Dataset:** GoEmotions  
**Source:** https://huggingface.co/datasets/go_emotions  
**Size:** ~58,000 text examples  
**Labels:** 28 emotions (multi-label)

Each example is annotated with zero or more emotions. The dataset is designed for studying fine-grained emotional expressions in short natural language.

---

## Training Details
- **Base model:** distilbert-base-uncased  
- **Training:** Fine-tuned for 1 epoch  
- **Task:** Multi-label classification  
- **Loss function:** Binary cross entropy  
- **Input length:** 128 tokens  
- **Optimizer:** AdamW  
- **Batch size:** 16  

Code used in the notebook:

```python
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=28,
    problem_type="multi_label_classification"
)
