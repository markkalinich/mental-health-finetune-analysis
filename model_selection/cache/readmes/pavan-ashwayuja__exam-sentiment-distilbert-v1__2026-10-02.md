---
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- exam-feedback
- distilbert
- transformers
- huggingface
---

# Exam Sentiment DistilBERT

A fine-tuned DistilBERT model for classifying student exam feedback into three sentiment categories:

- Negative
- Neutral
- Positive

This is an educational NLP project created to learn and demonstrate the complete Hugging Face Transformers workflow, including dataset creation, preprocessing, tokenization, fine-tuning, evaluation, and inference.

---

## Model Details

- **Model type:** DistilBERT for sequence classification
- **Base model:** `distilbert-base-uncased`
- **Task:** 3-class text classification
- **Language:** English
- **Number of labels:** 3
- **Fine-tuned from:** `distilbert-base-uncased`
- **Framework:** Hugging Face Transformers
- **Model version:** v1

### Label Mapping

| ID | Label |
|---|---|
| 0 | Negative |
| 1 | Neutral |
| 2 | Positive |

---

## Intended Use

This model is intended for:

- Educational purposes
- Learning NLP and Transformer fine-tuning
- Demonstrating the Hugging Face ecosystem
- Experimenting with exam-feedback sentiment classification
- Understanding model inference and evaluation

The model is **not production-ready** in its current form.

---

## Dataset

A custom exam-feedback dataset was created for this project.

### Dataset Size

| Split | Samples |
|---|---:|
| Total | 80 |
| Training | 64 |
| Testing | 16 |

### Class Distribution

| Sentiment | Samples |
|---|---:|
| Negative | 28 |
| Neutral | 26 |
| Positive | 26 |

The dataset contains short English-language statements describing students' experiences and opinions about exams.

---

## Training

The model was **fine-tuned from a pretrained DistilBERT checkpoint**.

It was not trained from scratch.

### Training Configuration

- **Base model:** `distilbert-base-uncased`
- **Training samples:** 64
- **Epochs:** 5
- **Batch size:** 8
- **Learning rate:** `2e-5`
- **Weight decay:** `0.01`
- **Environment:** Google Colab
- **Library:** Hugging Face Transformers

### Preprocessing

The text was processed using the DistilBERT tokenizer.

The tokenizer converts the text into:

- `input_ids`
- `attention_mask`

The sentiment labels were converted into numerical IDs:

```text
Negative → 0
Neutral  → 1
Positive → 2