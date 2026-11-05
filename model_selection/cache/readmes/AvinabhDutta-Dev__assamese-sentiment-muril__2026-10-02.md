---
language:
- as
license: mit
pipeline_tag: text-classification
tags:
- sentiment-analysis
- assamese
- muril
- nlp
- indian-languages
metrics:
- accuracy
- f1
- precision
- recall
- roc_auc
model-index:
- name: assamese-sentiment-muril
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Assamese Movie & Media Reviews
      type: assamese-reviews
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.963293
    - name: Macro F1
      type: f1
      value: 0.960526
    - name: Macro Precision
      type: precision
      value: 0.960819
    - name: Macro Recall
      type: recall
      value: 0.960236
    - name: ROC-AUC
      type: roc_auc
      value: 0.988171
---

# Assamese Sentiment Analysis — Fine-Tuned MuRIL

This repository contains a fine-tuned **MuRIL (Multilingual Representations for Indian Languages)** transformer model optimized for binary sentiment analysis on Assamese textual reviews. It maps localized Assamese content into binary sentiment classes (**Positive** and **Negative**).

---

## Model Summary

* **Model Architecture:** MuRIL (`google/muril-base-cased`)
* **Task:** Binary Sentiment Classification
* **Language:** Assamese (`as`)
* **Developer:** Avinabh Dutta
* **Primary Framework:** PyTorch & Hugging Face Transformers
* **Top Performance:** **96.33% Accuracy** | **0.9605 Macro F1**

---

## Performance & Evaluation Metrics

The model was evaluated against a held-out test dataset at step **1800 (Epoch 4.0)**, delivering strong stability across macro-averaged evaluation dimensions:

| Metric | Score | Percentage |
| :--- | :--- | :--- |
| **Accuracy** | `0.963293` | **96.33%** |
| **Macro F1-Score** | `0.960526` | **96.05%** |
| **Macro Precision** | `0.960819` | **96.08%** |
| **Macro Recall** | `0.960236` | **96.02%** |
| **ROC-AUC** | `0.988171` | **98.82%** |

---

## Dataset Overview

The dataset consists of localized social media commentaries, media assessments, and audience reviews covering drama (নাটক) and cultural content in Assamese. 

* **Feature Representation:** Focuses on extracting linguistic subtext from Assamese textual tokens, tracking features such as character length, word density, punctuation patterns, and emoji occurrences.
* **Target Classes:** Binary Classification (`0`: Negative, `1`: Positive).

---

## How to Use

You can easily load and run inference with this model using the Hugging Face `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model and tokenizer
model_name = "AvinabhDutta-Dev/assamese-sentiment-muril"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Example text (Assamese)
sample_text = "চলচ্চিত্ৰখনৰ কাহিনী আৰু অভিনয় অতি সুন্দৰ হৈছে।"
result = classifier(sample_text)

print(result)
```

---

## Training Hyperparameters

Fine-tuning parameters were tightly managed across a strict execution run:

| Parameter | Value |
| :--- | :--- |
| **Total Epochs** | `4.0` |
| **Train Batch Size** | `16` |
| **Max Training Steps** | `1800` |
| **Peak Learning Rate** | `2e-05` (decayed to `1.234e-08`) |
| **Logging Steps** | `100` |
| **Evaluation Steps** | `500` |

---

## Limitations & Edge Cases

* **Syntactic Shifts & Contrast Markers:** The model can face challenges when encountering nested sarcasm, hard negation shifts, or complex contrast structures.
* **Contrast Words:** Sentences containing explicit positive tokens paired with contrast markers (e.g., **কিন্তু** [but], **কাৰণ** [because]) may occasionally trigger false positives. Manual rule overrides or contrastive data augmentation are recommended for edge-case resolution.

---

## Citation & Contact

If you use this model or refer to this work in your research, please link back to this Hugging Face repository or the GitHub project repository.
If you use this model, please cite the associated preprint:
> Dev, C., Baishya, B., Dey, N., Dutta, A., & Dutta, S. (2026). *Sentiment Analysis of Assamese Reviews using Transfer Learning Models*. Preprint. https://doi.org/10.2139/ssrn.6357982