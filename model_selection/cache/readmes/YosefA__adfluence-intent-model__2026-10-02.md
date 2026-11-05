---
library_name: transformers
license: mit
base_model: Davlan/afro-xlmr-base
tags:
- amharic
- text-classification
- sentiment-analysis
- intent-classification
- code-switching
- ethiopia
- adfluence-ai
metrics:
- f1
model-index:
- name: Adfluence-AI Purchase Intent Classifier
  results:
  - task:
      type: text-classification
    dataset:
      name: YosefA/Adflufence-ad-comments
      type: YosefA/Adflufence-ad-comments
      config: default
      split: test
    metrics:
    - name: F1 (Weighted)
      type: f1
      value: 0.8101
datasets:
- YosefA/Adflufence-ad-comments
language:
- am
pipeline_tag: text-classification
---

# Adfluence-AI Purchase Intent Classifier

This model is a fine-tuned version of **[Davlan/afro-xlmr-base](https://huggingface.co/Davlan/afro-xlmr-base)**, a powerful multilingual model with a strong understanding of African languages. It has been specifically trained to classify purchase intent in social media comments written in Amharic (Ge'ez script), Romanized Amharic, and mixed Amharic-English (code-switching).

This model was developed for the **Adfluence AI** project, which aims to evaluate the effectiveness of influencer marketing campaigns in Ethiopia.

It achieves a **weighted F1-score of 0.81** on the evaluation set.

## Model Description

The model takes a social media comment as input and outputs a prediction across five categories of purchase intent:

*   `highly_likely`
*   `likely`
*   `neutral`
*   `unlikely`
*   `highly_unlikely`

This allows for a nuanced understanding of audience reaction beyond simple positive/negative sentiment, directly measuring the potential for user conversion.

## How to Use

You can use this model directly with the `pipeline` function from the `transformers` library.

```python
from transformers import pipeline

# Load the model from the Hub
model_id = "YosefA/adfluence-intent-model"
classifier = pipeline("text-classification", model=model_id)

# --- Example Usage ---

# Example 1: Amharic (Ge'ez Script) - Clear intent
comment_1 = "ዋው በጣም አሪፍ ነው! የት ነው ማግኘት የምችለው?" 
# Translation: "Wow, this is great! Where can I find it?"

# Example 2: Mixed Amharic-English - Neutral/Questioning
comment_2 = "Hmm, interesting. Price-u endet new?"
# Translation: "Hmm, interesting. How is the price?"

# Example 3: Romanized Amharic - Negative
comment_3 = "Ene enja minim altemechegnim, quality yelelew neger new."
# Translation: "I don't know, I didn't like it at all, it's a thing with no quality."


results = classifier([comment_1, comment_2, comment_3])
for comment, result in zip([comment_1, comment_2, comment_3], results):
    print(f"Comment: {comment}")
    print(f"Prediction: {result['label']}, Score: {result['score']:.4f}\n")

# Expected Output:
# Comment: ዋው በጣም አሪፍ ነው! የት ነው ማግኘት የምችለው?
# Prediction: highly_likely, Score: 0.9851
#
# Comment: Hmm, interesting. Price-u endet new?
# Prediction: neutral, Score: 0.9214
#
# Comment: Ene enja minim altemechegnim, quality yelelew neger new.
# Prediction: highly_unlikely, Score: 0.9902
```

# Intended Uses & Limitations

### Intended Use
This model is intended to be used as a backend component for the Adfluence AI platform. Its primary purpose is to analyze user comments on social media advertisements (e.g., on Instagram, Facebook, TikTok) to gauge audience purchase intent and provide campaign performance metrics.

### Limitations
* **Simulated Data:** The model is trained on a high-quality simulated dataset, not on live social media data. While designed to reflect real-world usage, performance may vary on wild, un-sanitized data.
* **Domain Specificity:** The source data was derived from product reviews (specifically for electronics). The model's performance may be strongest in the e-commerce/product domain and might require further fine-tuning for vastly different domains like services, events, or fashion.
* **Language Scope:** The model only understands Amharic and English. It has not been trained on other Ethiopian languages like Tigrinya, Oromo, etc.

---

# Training and Evaluation Data

This model was fine-tuned on the custom `YosefA/Adflufence-ad-comments` dataset.

The dataset was created through the following process:

* **Source:** Started with ~3180 English product reviews from an Amazon dataset.(https://huggingface.co/datasets/hugginglearners/amazon-reviews-sentiment-analysis)
* **Transformation:** Each review was programmatically rephrased and translated into a simulated social media comment using Google's Gemini Flash.
* **Stylization:** Comments were generated in three styles to mimic real-world Ethiopian user behavior:
    * Amharic (Ge’ez script)
    * Romanized Amharic
    * Mixed Amharic-English (Code-Switching)
* **Enrichment:** Comments were styled with emojis, slang, and informal sentence structures.
* **Labeling:** Each comment was assigned a purchase intent label mapped from the original star rating of the source review.

---

# Training Procedure

### Training Hyperparameters
The following hyperparameters were used during training:
* `learning_rate`: 2e-05
* `train_batch_size`: 16
* `eval_batch_size`: 16
* `seed`: 42
* `optimizer`: AdamW with betas=(0.9,0.999) and epsilon=1e-08
* `lr_scheduler_type`: linear
* `num_epochs`: 3

### Training Results
The model achieved its best performance at the end of Epoch 2.

| Training Loss | Epoch | Step | Validation Loss | F1 (Weighted) |
| :------------ | :---- | :--- | :-------------- | :------------ |
| No log        | 1.0   | 160  | 0.5001          | 0.7852        |
| No log        | 2.0   | 320  | 0.4316          | 0.8101        |
| No log        | 3.0   | 480  | 0.4281          | 0.8063        |

---

# Framework Versions
* **Transformers** 4.41.2
* **Pytorch** 2.3.0+cu121
* **Datasets** 2.19.0
* **Tokenizers** 0.19.1