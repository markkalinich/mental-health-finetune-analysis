---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- sentiment-analysis
- emotion-classification
- generated_from_trainer
metrics:
- f1_macro
- accuracy
model-index:
- name: SentimentAnalysis-distilbert-base-uncased-finetuned-emotion
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Emotion Dataset
      type: text
    metrics:
    - name: F1 Macro
      type: f1_macro
      value: 0.8902
    - name: Accuracy
      type: accuracy
      value: 0.927
---
# SentimentAnalysis-distilbert-base-uncased-finetuned-emotion

This model is a **fine-tuned version of `distilbert-base-uncased`** for **emotion classification** of short texts (tweets).  
It predicts one of **six emotions**:

- sadness
- joy
- love
- anger
- fear
- surprise

The model was trained using the 🤗 **Transformers Trainer API** with **class-weighted loss** to handle class imbalance.

---

## Model performance

Evaluation results on the test set:

- **Loss:** 0.2094  
- **F1 Macro:** 0.8902  
- **Accuracy:** 0.927  

> **Note:** F1 Macro is the primary metric since the dataset is imbalanced.

---

## Intended uses

This model is suitable for:

- Emotion analysis of tweets or short social media texts
- NLP research and educational projects
- Sentiment-aware chatbots or analytics dashboards

---

## Limitations

- Trained on short texts (tweets); performance may degrade on long documents
- English-only
- May inherit biases present in the training data
- Not intended for high-stakes or sensitive decision-making

---

## Training data

The model was trained on an **emotion-labeled tweet dataset** with six emotion classes.  
The dataset was split into **training, validation, and test sets**.

Preprocessing steps included:
- Tokenization using the DistilBERT tokenizer
- Padding and truncation to a fixed maximum length
- Label encoding using Hugging Face `ClassLabel`

---

## Training procedure

### Hyperparameters

- **Base model:** distilbert-base-uncased
- **Learning rate:** 2e-5
- **Train batch size:** 32
- **Eval batch size:** 32
- **Epochs:** 10
- **Optimizer:** AdamW (betas = 0.9, 0.999, epsilon = 1e-8)
- **Learning rate scheduler:** Linear
- **Loss function:** Cross-Entropy with class weights
- **Seed:** 42

---

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 Macro | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.6445 | 1.0 | 500  | 0.2374 | 0.8993 | 0.9235 |
| 0.1811 | 2.0 | 1000 | 0.1683 | 0.9109 | 0.9340 |
| 0.1357 | 3.0 | 1500 | 0.1686 | 0.9157 | 0.9380 |
| 0.1036 | 4.0 | 2000 | 0.1737 | 0.9192 | 0.9400 |
| 0.0816 | 5.0 | 2500 | 0.2204 | 0.9086 | 0.9345 |
| 0.0629 | 6.0 | 3000 | 0.2197 | 0.9142 | 0.9385 |
| 0.0475 | 7.0 | 3500 | 0.3064 | 0.9081 | 0.9355 |

The best model was selected based on **macro F1 score**.

---

## Framework versions

- Transformers: 4.44.2  
- PyTorch: 2.6.0+cu124  
- Datasets: 4.4.1  
- Tokenizers: 0.19.1  

---

## Source code

Training and evaluation code is available on GitHub:  
👉 https://github.com/Abdelrahmanemam01/Sentiment-Analysis