---
library_name: transformers
license: mit
language: 
- en
base_model: FacebookAI/roberta-base
tags:
- generated_from_trainer
- text-classification
- roberta
- yelp
- multi-class-classification
- sentiment-analysis
datasets:
- yelp_text_review_kaggle
metrics:
- f1
- accuracy
- precision
- recall
model-index:
- name: roberta-base-finetuned-yelp-ratings
  results: []
---

# RoBERTa-base Fine-Tuned for Yelp Star Rating Classification

This repository contains a fine-tuned [`FacebookAI/roberta-base`](https://huggingface.co/FacebookAI/roberta-base) model trained to predict Yelp customer review 
star ratings (**1 to 5 stars**) from raw review text.

By replacing traditional bag-of-words/TF-IDF representations with bi-directional contextual representations, this model captures complex linguistic nuances 
(such as sarcasm, negation, and multi-sentence context), outperforming traditional machine learning baselines 
(Logistic Regression, Multinomial Naive Bayes, Linear SVM, XGBoost) by a significant margin.


## Model description

This model is a fine-tuned version of `roberta-base` for **5-class text classification of Yelp reviews**.

Given the text of a Yelp review, the model predicts the associated star rating:

| Label | Rating |
|---|---|
| `0` | 1 Star |
| `1` | 2 Stars |
| `2` | 3 Stars |
| `3` | 4 Stars |
| `4` | 5 Stars |

The model was fully fine-tuned for this supervised classification task using the Hugging Face Transformers `Trainer` framework.

This project is intended primarily as an **educational and experimental demonstration of Transformer-based NLP and parameter-efficient fine-tuning**, 
rather than as a production-ready Yelp rating predictor.

---

## Dataset

The model was fine-tuned on a **10,000-review subset** of the Yelp review data associated with the 
[RecSys2013: Yelp Business Rating Prediction](https://www.kaggle.com/competitions/yelp-recsys-2013/overview) Kaggle competition.

The original competition training data contains approximately 230,000 reviews. A 10,000-review subset was used here to enable 
rapid experimentation and training on modest computational resources.

The subset contains the review text and its corresponding star rating. The original 1–5 star labels were mapped to integer class labels 0–4 for model training.

For this experimental project, the 10k subset provides a sufficiently large dataset to investigate Transformer fine-tuning while keeping iteration times manageable.

**Dataset provenance:** [Kaggle — RecSys2013: Yelp Business Rating Prediction](https://www.kaggle.com/competitions/yelp-recsys-2013/overview)

> Note: This project uses the review data for a text-classification task. This is different from the original RecSys2013 competition objective,
> which focused on predicting ratings for user-business pairs.


## Data Split

The dataset was divided using stratified sampling:

- Training: 8,000 reviews (80%)
- Validation: 1,000 reviews (10%)
- Test: 1,000 reviews (10%)

Stratification was used to preserve the original star-rating distribution across the three splits.

No class rebalancing or oversampling was applied.

---

## Training Details

### Base Model

- **Model:** `FacebookAI/roberta-base`
- **Architecture:** RoBERTa-base
- **Task:** Sequence classification
- **Number of classes:** 5
- **Maximum sequence length:** 512 tokens

### Fine-tuning

The model was fully fine-tuned; all model parameters were trainable.

Training was performed using:

- Hugging Face Transformers
- Hugging Face `Trainer`
- PyTorch
- Google Colab
- NVIDIA T4 GPU
- Mixed-precision training (`fp16=True`)

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP (`fp16=True`)
- metric_for_best_model: f1_macro

The best checkpoint was selected according to validation **macro-F1**.

### Training results

| Training Loss | Epoch | Step | Validation Loss | Validation Accuracy | Validation F1 Macro | Validation Precision Macro | Validation Recall Macro | Validation MAE   |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:---------------:|:------------:|:-----:|
| 0.9808        | 1.0   | 500  | 0.8205          | 0.627    | 0.5765   | 0.5942          | 0.5953       | 0.422 |
| 0.7459        | 2.0   | 1000 | 0.8220          | 0.651    | 0.6167   | 0.6218          | 0.6198       | 0.386 |
| 0.5833        | 3.0   | 1500 | 0.8573          | 0.656    | 0.6229   | 0.6314          | 0.6232       | 0.382 |

### Framework versions

- Transformers 5.15.0
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
---

## Evaluation

The model was evaluated on the held-out test set using:

- Accuracy
- Macro F1
- Macro Precision
- Macro Recall
- Multiclass ROC-AUC (One-vs-Rest, macro average)
- PR-AUC (One-vs-Rest, macro average)
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Off-by-1 Accuracy
- Off-by-1 Macro-F1

### Test Set Results

| Metric | Score |
|---|---:|
| Accuracy | **0.639** |
| Macro F1 | **0.631** |
| Macro Precision | **0.634** |
| Macro Recall | **0.630** |
| ROC-AUC | **0.904** |
| PR-AUC | **0.682** |
| MAE | **0.387** |
| MSE | **0.451** |
| RMSE | **0.672** |
| Off-by-1 Accuracy | **0.980** |
| Off-by-1 Macro-F1 | **0.973** |

The ROC-AUC value is calculated using a one-vs-rest strategy across the five rating classes.
PR-AUC was also calculated using a one-vs-rest formulation with macro averaging across the five classes.

Because the star ratings are ordinal, MAE, RMSE and off-by-1 accuracy are also reported as supplementary metrics. 
These metrics capture the distinction between a prediction that is close to the true rating and one that is several stars away.

### Confusion Matrix

The confusion matrix below shows the distribution of predictions across the five star-rating classes.

![RoBERTa Confusion Matrix](images/confusion_matrix_yelp_roberta.png)

---


## 🚀 How to Use

You can use this model directly with the Hugging Face `text-classification` pipeline or PyTorch:

### 1. Using the `pipeline` API

```python
from transformers import pipeline

# Load fine-tuned classification model
classifier = pipeline(
    "text-classification", 
    model="AlexStamp/roberta-base-finetuned-yelp-ratings"
)

# Test review
review = "The pasta was cooked to perfection and the ambiance was fantastic, but service was a bit slow."
prediction = classifier(review)

print(prediction)
# Output: [{'label': '4 Stars', 'score': 0.8421}]
```

### 2. Direct `PyTorch` inference

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo_id = "AlexStamp/roberta-base-finetuned-yelp-ratings"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

inputs = tokenizer("Absolute worst customer service ever. Avoid at all costs!", return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class_id = logits.argmax(-1).item()

print(model.config.id2label[predicted_class_id])
# Output: "1 Star"
```
---

## Comparison with Classical NLP Baseline

As part of the same project, traditional TF-IDF-based NLP models were trained on the same 10,000-review dataset.

The best classical models achieved approximately:

- Linear SVM: Macro F1 ≈ **0.502**
- Logistic Regression: Macro F1 ≈ **0.507**

The fine-tuned RoBERTa model achieved:

- **Macro F1 = 0.631**
- **ROC-AUC = 0.904**

This represents a substantial improvement in macro-F1 over the classical TF-IDF-based approaches.

## Intended Use

This model is intended for:

- Educational experimentation with Transformer fine-tuning
- Demonstrating supervised NLP classification
- Comparing classical NLP models with contextual Transformer representations
- Experimenting with parameter-efficient fine-tuning techniques such as LoRA (see [Future Work](#future-work) section below)
  
It should not be considered a production-grade Yelp rating prediction system.

## Limitations

Several limitations should be considered:

- The training dataset contains only 10,000 reviews, substantially smaller than the original Yelp competition training dataset.
- The star-rating classes are imbalanced.
- No explicit class rebalancing was performed.
- The model predicts ratings from review text alone and does not use user, business, or historical interaction information.
- The model is trained on Yelp review data and may not generalize to reviews from other domains.
- The dataset and model are not intended to reproduce the original RecSys2013 competition task.

## Future Work

A natural extension of this experiment is to compare full fine-tuning with **LoRA (Low-Rank Adaptation)** while keeping 
the base model, dataset and evaluation procedure fixed. See [LoRA Fine-Tuning](https://huggingface.co/AlexStamp/roberta-base-lora-yelp-ratings) repository.

This will allow comparison of:

- Predictive performance
- Number of trainable parameters
- Training efficiency
- Memory requirements
- Performance degradation, if any, resulting from parameter-efficient fine-tuning

## Libraries

Main libraries used:

- `transformers` — model, tokenizer and `Trainer` API
- `datasets` — dataset preparation and splitting
- `evaluate` — evaluation metrics
- `scikit-learn` — additional metrics and confusion matrix
- `PyTorch` — underlying deep learning framework

## Citation

If you use this model or project, please refer to the original RoBERTa paper and the original Yelp/RecSys2013 dataset source.

**RoBERTa:**  
Liu et al., *RoBERTa: A Robustly Optimized BERT Pretraining Approach*, 2019.

**Dataset:**  
Yelp / RecSys2013: Yelp Business Rating Prediction, Kaggle.

## Model Repository

This repository contains the fine-tuned model, tokenizer and associated configuration files.

A corresponding LoRA fine-tuned version will be provided separately as part of the same experimental project.
