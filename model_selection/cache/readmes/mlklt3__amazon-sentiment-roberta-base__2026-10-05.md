---
language: en
license: apache-2.0
library_name: transformers
tags:
- sentiment-analysis
- roberta
- amazon-reviews
- e-commerce
datasets:
- amazon_fine_food_reviews
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# Model Card: Amazon Sentiment RoBERTa Base

## Model Description
This model is a fine-tuned version of **RoBERTa-base** specifically optimized for sentiment analysis of customer reviews. It was trained on a balanced subset of the Amazon Fine Food Reviews dataset to classify text into three distinct categories: **Negative**, **Neutral**, and **Positive**.

- **Model Type:** Transformer-based Text Classification
- **Language:** English
- **Base Model:** `roberta-base`

## Intended Use
- **Primary Use Case:** Real-time sentiment tracking for e-commerce platforms.
- **Scope:** Analyzing short to medium-length customer feedback and product reviews.
- **Out-of-Scope:** Not recommended for legal documents, medical advice, or languages other than English.

## Training Data & Methodology
### Dataset
- **Source:** Amazon Fine Food Reviews (Kaggle).
- **Preprocessing:** - Removal of duplicates and HTML tags.
  - POS-tag-based Lemmatization for linguistic normalization.
  - Undersampling to 15,000 samples (5,000 per class) to handle class imbalance.
- **Labels:** - `0`: Negative (1-2 stars)
  - `1`: Neutral (3 stars)
  - `2`: Positive (4-5 stars)

### Hyperparameters
- **Learning Rate:** 2e-5
- **Batch Size:** 16
- **Epochs:** 2
- **Weight Decay:** 0.01
- **Max Sequence Length:** 128 tokens

## Performance Metrics
The model was evaluated on a held-out test set (20% of the balanced data):

| Metric | Value |
| :--- | :--- |
| **Accuracy** | 78.0% |
| **Weighted F1-Score** | 0.78 |
| **Precision (Positive)** | 0.83 |
| **Recall (Positive)** | 0.89 |

### Key Strengths
- **Contextual Understanding:** Successfully handles complex structures, such as negation and sarcasm (e.g., "Don't listen to the haters, this is great!").
- **Robustness:** Significantly outperforms traditional TF-IDF and DistilBERT baselines in identifying ambiguous "Neutral" reviews.

## Limitations & Bias
- **Neutral Class:** Still remains the most frequent source of misclassification due to the inherent subjectivity of 3-star ratings.
- **Domain Specificity:** Performance may vary when applied to domains outside of food and beverages (e.g., electronics or fashion).
- **Sarcasm:** While improved, extremely subtle sarcasm may still lead to errors.

## How to Use
```python
from transformers import pipeline

# Load the model directly from the Hub
model_path = "mlklt3/amazon-sentiment-roberta-base"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_path)

# Example usage
text = "The product was okay, but I expected much better flavor for this price."
result = sentiment_pipeline(text)
print(result)
```
## Citation
If you use this model in your research or project, please credit the Amazon Fine Food Reviews dataset and the Hugging Face Transformers library.