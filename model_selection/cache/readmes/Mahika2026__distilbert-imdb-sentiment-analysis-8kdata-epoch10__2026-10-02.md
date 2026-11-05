---
language: en
license: apache-2.0
tags:
  - text-classification
  - sentiment-analysis
  - transformers
library_name: transformers
---

# DistilBERT IMDb Sentiment Analysis 
(8k Training Data)

This model is a fine-tuned version of **distilbert-base-uncased** for **binary sentiment classification** on movie reviews.

The model predicts whether a review expresses **positive (1)** or **negative (0)** sentiment.

---

# Model Description

This model was fine-tuned using the Transformers library on a cleaned subset of the IMDb movie review dataset.

Key characteristics:

* Base model: distilbert-base-uncased
* Task: Binary sentiment classification
* Labels:

* 0 → Negative
* 1 → Positive
* Training epochs: 10
* Maximum sequence length: 128 tokens

The dataset was preprocessed by removing HTML tags using BeautifulSoup.

---

# Dataset

The training dataset is derived from the **IMDb sentiment dataset**.

A balanced subset was sampled and cleaned before training.

Dataset split:

* Train: 8,000 reviews (4,000 positive / 4,000 negative)
* Validation: 2,000 reviews (1,000 positive / 1,000 negative)
* Test: 2,000 reviews (1,000 positive / 1,000 negative)

HTML tags were removed using BeautifulSoup and stored in a `cleaned_text` column.

Dataset repository:
https://huggingface.co/datasets/Mahika2026/imdb-sentiment-dataset

---

# Evaluation Results

Best validation metrics during training:

Loss: 0.4104
Accuracy: 0.8565
Precision: 0.8411
Recall: 0.8790
F1 Score: 0.8597

---

# Test Set Performance

Evaluation on the 2,000 review test set produced the following results:

Accuracy: **0.865**

| Class      | Precision | Recall | F1     |
|------------|-----------|--------|--------|
| Negative 0 | 0.8875    | 0.8360 | 0.8610 |
| Positive 1 | 0.8450    | 0.8940 | 0.8688 |

Confusion Matrix:

| True\Pred | Negative| Positive|
|-----------|---------|---------|
| Negative  | 836     | 164     |
| Positive  | 106     | 894     |

---

# Training Procedure

The model was trained using the Hugging Face Transformers Trainer API.

Training hyperparameters:

learning_rate: 2e-5
train_batch_size: 32
eval_batch_size: 32
gradient_accumulation_steps: 2
effective_batch_size: 64
num_epochs: 10
max_sequence_length: 128
weight_decay: 0.01
evaluation_strategy: epoch
save_strategy: epoch
mixed_precision_training: FP16

Optimizer:

AdamW optimizer with linear learning rate scheduler.

---

# Intended Uses

This model can be used for:

* Movie review sentiment analysis
* Binary text classification experiments
* Educational NLP projects
* Benchmarking small fine-tuned Transformer models

---

# Limitations

* The model is trained on a **small subset (8k samples)** of the IMDb dataset.
* Performance may degrade on other domains (product reviews, tweets, etc.).
* Long texts beyond 128 tokens will be truncated.

---

# Framework Versions

- PyTorch: 2.10.0+cu128  
- Transformers: 5.0.0  
- Datasets: 4.0.0  
- Tokenizers: 0.22.2  
- scikit-learn: 1.6.1  
- accelerate: 1.12.0