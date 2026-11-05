---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- text-classification
- sentiment-analysis
- emotion-classification
- generated_from_trainer
metrics:
- f1_macro
- accuracy
model-index:
- name: SentimentAnalysis-bert-base-uncased-finetuned-emotion
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Emotion Dataset
      type: text
    metrics:
    - type: f1_macro
      value: 0.8801
      name: F1 Macro
    - type: accuracy
      value: 0.9215
      name: Accuracy
---

# SentimentAnalysis-bert-base-uncased-finetuned-emotion

This model is a **fine-tuned version of `bert-base-uncased`** for **emotion classification** of short English texts such as tweets and social media posts.

The model predicts one of **six emotion classes**:

- sadness  
- joy  
- love  
- anger  
- fear  
- surprise  

The model was trained using the 🤗 **Transformers Trainer API**.

---

## Model performance

Evaluation results on the test set:

- **Loss:** 0.2913  
- **F1 Macro:** 0.8801  
- **Accuracy:** 0.9215  

**Macro F1** is reported as the primary metric because the dataset is imbalanced and this metric better reflects performance across all emotion classes.

---

## Intended uses

This model is suitable for:

- Emotion classification of tweets and short social media texts  
- NLP research and academic projects  
- Emotion-aware chatbots  
- Sentiment and emotion analytics dashboards  

---

## Limitations

- Optimized for **short texts**; performance may degrade on long documents  
- **English-only**  
- May reflect biases present in the training data  
- Not intended for **high-stakes or sensitive decision-making**

---

## Training data

The model was trained on an **emotion-labeled dataset of short texts** with six emotion categories.

Preprocessing steps included:

- Train / validation / test split  
- Tokenization using the BERT tokenizer  
- Padding and truncation to a fixed maximum sequence length  
- Label encoding using Hugging Face `ClassLabel`

---

## Training procedure

### Hyperparameters

- **Base model:** bert-base-uncased  
- **Learning rate:** 1e-5  
- **Train batch size:** 16  
- **Eval batch size:** 16  
- **Epochs:** 6  
- **Optimizer:** AdamW (Torch fused)  
  - betas = (0.9, 0.999)  
  - epsilon = 1e-8  
- **Learning rate scheduler:** Linear  
- **Seed:** 42  

---

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 Macro | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.7334 | 1.0 | 1000 | 0.2508 | 0.8941 | 0.9170 |
| 0.2016 | 2.0 | 2000 | 0.1881 | 0.9096 | 0.9330 |
| 0.1450 | 3.0 | 3000 | 0.1981 | 0.9119 | 0.9355 |
| 0.1178 | 4.0 | 4000 | 0.2229 | 0.9158 | 0.9390 |
| 0.0903 | 5.0 | 5000 | 0.2469 | 0.9161 | 0.9385 |
| 0.0808 | 6.0 | 6000 | 0.2489 | 0.9100 | 0.9355 |

The best model checkpoint was selected based on **macro F1 score**.

---

## Framework versions

- **Transformers:** 4.57.1  
- **PyTorch:** 2.8.0+cu126  
- **Datasets:** 4.4.1  
- **Tokenizers:** 0.22.1  

---

## Source code

Training and evaluation code is available on GitHub:  
https://github.com/Abdelrahmanemam01/Sentiment-Analysis