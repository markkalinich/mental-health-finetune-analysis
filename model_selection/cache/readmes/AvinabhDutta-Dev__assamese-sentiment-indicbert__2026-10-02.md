---
language:
- as
license: mit
tags:
- sentiment-analysis
- text-classification
- assamese
- indicbert
- nlp
- indian-languages
metrics:
- accuracy
- f1
- precision
- recall
- roc_auc
model-index:
- name: assamese-sentiment-indicbert
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
      value: 0.927141
    - name: Macro F1
      type: f1
      value: 0.921967
    - name: Macro Precision
      type: precision
      value: 0.920584
    - name: Macro Recall
      type: recall
      value: 0.923433
    - name: ROC-AUC
      type: roc_auc
      value: 0.977318
---

# Assamese Sentiment Analysis — Fine-Tuned IndicBERT

This repository contains a fine-tuned **IndicBERT (`ai4bharat/indic-bert`)** transformer model optimized for binary sentiment analysis on Assamese textual reviews. It maps localized Assamese content into binary sentiment classes (**Positive** and **Negative**).

---

## Model Summary

* **Model Architecture:** IndicBERT (`ai4bharat/indic-bert`)
* **Task:** Binary Sentiment Classification
* **Language:** Assamese (`as`)
* **Developer:** Avinabh Dutta
* **Primary Framework:** PyTorch & Hugging Face Transformers
* **Top Performance:** **92.71% Accuracy** | **0.9220 Macro F1**

---

## Performance & Evaluation Metrics

The model was evaluated against a held-out test dataset, demonstrating stable generalization across all macro-averaged dimensions:

| Metric | Score | Percentage / Value |
| :--- | :--- | :--- |
| **Accuracy** | `0.927141` | **92.71%** |
| **Macro F1-Score** | `0.921967` | **0.9220** |
| **Macro Precision** | `0.920584` | **0.9206** |
| **Macro Recall** | `0.923433` | **0.9234** |
| **ROC-AUC** | `0.977318` | **0.9773** |
| **Cohen's Kappa** | `0.843940` | **0.8439** |

---

## Dataset Overview

The dataset consists of localized social media commentaries, media assessments, and audience reviews covering drama (নাটক) and cultural content in Assamese.

* **Feature Representation:** Captures linguistic subtext from Assamese textual tokens, tracking features such as character length, word density, punctuation patterns, and emoji occurrences.
* **Target Classes:** Binary Classification (`0`: Negative, `1`: Positive).

---

## How to Use

You can easily load and run inference with this model using the Hugging Face `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load model and tokenizer
model_name = "AvinabhDutta-Dev/assamese-sentiment-indicbert"
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

Fine-tuning parameters were managed alongside the overall transformer execution pipeline:

| Parameter | Value |
| :--- | :--- |
| **Base Model** | `ai4bharat/indic-bert` |
| **Total Epochs** | `4.0` |
| **Train Batch Size** | `16` |
| **Learning Rate** | `2e-05` |
| **Weight Decay** | `0.01` |
| **Warmup Ratio** | `0.1` |
| **Checkpoint Selection** | Best Macro F1 |

---

## Limitations & Edge Cases

* **Structural Capacity:** Due to its compact architecture and generalized multi-language Indic representation layer, IndicBERT captures fewer domain-specific nuances compared to larger models like MuRIL.
* **Contextual Shifts & Boundary Markers:** The model shows higher vulnerability when processing mixed token properties, hard sentence boundaries, or implicit sentiment reversals. Sentences weaving complex local structural markers or contrast transitions may result in false predictions.

---

## Citation & Contact

If you use this model or refer to this work in your research, please link back to this Hugging Face repository or the GitHub project repository.
If you use this model, please cite the associated preprint:
> Dev, C., Baishya, B., Dey, N., Dutta, A., & Dutta, S. (2026). *Sentiment Analysis of Assamese Reviews using Transfer Learning Models*. Preprint. https://doi.org/10.2139/ssrn.6357982