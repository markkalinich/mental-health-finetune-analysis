---
language:
- as
license: mit
tags:
- sentiment-analysis
- text-classification
- assamese
- xlm-roberta
- nlp
- cross-lingual
metrics:
- accuracy
- f1
- precision
- recall
- roc_auc
model-index:
- name: assamese-sentiment-xlmr
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
      value: 0.948832
    - name: Macro F1
      type: f1
      value: 0.945181
    - name: Macro Precision
      type: precision
      value: 0.943848
    - name: Macro Recall
      type: recall
      value: 0.946586
    - name: ROC-AUC
      type: roc_auc
      value: 0.985455
---

# Assamese Sentiment Analysis — Fine-Tuned XLM-R

This repository contains a fine-tuned **XLM-RoBERTa (`xlm-roberta-base`)** transformer model optimized for binary sentiment analysis on Assamese textual reviews. It effectively maps cross-lingual features into a single-label distribution (**Positive** and **Negative**).

---

## Model Summary

* **Model Architecture:** XLM-RoBERTa (`xlm-roberta-base`)
* **Task:** Binary Sentiment Classification
* **Language:** Assamese (`as`)
* **Developer:** Avinabh Dutta
* **Primary Framework:** PyTorch & Hugging Face Transformers
* **Top Performance:** **94.88% Accuracy** | **0.9452 Macro F1**

---

## Architecture Configuration

The implementation leverages the standard `base` architecture rather than the `large` variant:

* **Hidden Size:** 768
* **Attention Heads:** 12
* **Hidden Layers:** 12
* **Vocabulary Size:** 250,002 tokens

---

## Performance & Evaluation Metrics

The fine-tuned XLM-R model achieved a robust second-place finish in the project benchmarking suite, proving highly effective at cross-lingual representation:

| Metric | Score | Percentage |
| :--- | :--- | :--- |
| **Accuracy** | `0.948832` | **94.88%** |
| **Macro F1-Score** | `0.945181` | **94.52%** |
| **Macro Precision** | `0.943848` | **94.38%** |
| **Macro Recall** | `0.946586` | **94.66%** |
| **ROC-AUC** | `0.985455` | **98.55%** |
| **Cohen's Kappa** | `0.890366` | **89.04%** |

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
model_name = "AvinabhDutta-Dev/assamese-sentiment-xlmr"
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

The training pipeline utilized an identical optimization schedule as the other pre-trained transformer blocks in this project:

| Parameter | Value |
| :--- | :--- |
| **Base Model** | `xlm-roberta-base` |
| **Total Epochs** | `4.0` |
| **Train Batch Size** | `16` |
| **Learning Rate** | `2e-05` |
| **Weight Decay** | `0.01` |
| **Warmup Ratio** | `0.1` |
| **Checkpoint Selection** | Best Macro F1 |

---

## Limitations & Edge Cases

* **The "Curse of Multilinguality":** Because XLM-R shares its parameter capacity across a massive global language footprint (100+ languages), its specific representation space for lower-resource scripts like Assamese is somewhat diluted. 
* **Morphological Subtexts & Discourse Markers:** While the model leverages broad semantic structures very well, it struggles more than highly localized models (like MuRIL) with regional morphological subtexts, context-dependent negation patterns, and local contrastive discourse markers.

---

## Citation & Contact

If you use this model or refer to this work in your research, please link back to this Hugging Face repository or the GitHub project repository.
If you use this model, please cite the associated preprint:
> Dev, C., Baishya, B., Dey, N., Dutta, A., & Dutta, S. (2026). *Sentiment Analysis of Assamese Reviews using Transfer Learning Models*. Preprint. https://doi.org/10.2139/ssrn.6357982