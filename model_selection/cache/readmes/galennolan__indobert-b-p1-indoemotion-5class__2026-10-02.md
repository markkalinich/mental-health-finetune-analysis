---
license: mit
tags:
- indobert
- emotion-classification
- text-classification
- indonesian
- torch
language:
- id
datasets:
- PRDECT-ID
model-index:
- name: IndoBERT Emotion Classification (5-Class)
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: PRDECT-ID
      type: text
      description: >
        A dataset of Indonesian product reviews labeled with five emotion
        categories: love, happiness, anger, fear, and sadness.
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7167
    - name: F1 Score
      type: f1
      value: 0.7125
    - name: Precision
      type: precision
      value: 0.7179
    - name: Recall
      type: recall
      value: 0.7167
base_model:
- indobenchmark/indobert-base-p1
---

# IndoBERT Emotion Classification (5-Class)

Model ini merupakan hasil *fine-tuning* dari [`indobenchmark/indobert-base-p1`](https://huggingface.co/indobenchmark/indobert-base-p1) untuk tugas klasifikasi emosi dalam Bahasa Indonesia, dengan 5 label emosi: `love`, `happiness`, `anger`, `fear`, dan `sadness`.

## 🧠 Dataset

Model ini dilatih menggunakan **PRDECT-ID Dataset**, yaitu kumpulan ulasan produk berbahasa Indonesia dari e-commerce Tokopedia, yang sudah dianotasi dengan label emosi oleh ahli psikologi klinis.

- 29 kategori produk
- Anotasi emosi oleh tim profesional
- Setiap entri memiliki 1 label emosi

## 🛠 Fine-tuning Details

- **Base model**: `indobenchmark/indobert-base-p1`
- **Training epochs**: 5 dari total 10 (early stopping dengan `load_best_model_at_end=True`)
- **Batch size**: 8
- **Learning rate**: 2e-5
- **Weight decay**: 0.05
- **Validation strategy**: per epoch
- **Evaluation metric**: `eval_accuracy` (dengan `greater_is_better=True`)
- **Cross-validation**: Stratified K-Fold (n_splits=5)

### Eval Results (Best Model @ Epoch 3)

| Metric      | Value   |
|-------------|---------|
| Accuracy    | 0.7167  |
| F1 Score    | 0.7125  |
| Precision   | 0.7179  |
| Recall      | 0.7167  |
| Eval Loss   | 0.7614  |

## 🚀 How to Use

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained("galennolan/indobert-b-p1-indoemotion-5class")
tokenizer = AutoTokenizer.from_pretrained("galennolan/indobert-b-p1-indoemotion-5class")

emotion_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

emotion_classifier("Produk ini bikin aku senang banget!")