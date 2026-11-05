---
library_name: transformers
tags: [sentiment-analysis, distilbert, fine-tuned, imdb]
---

# Model Card for DistilBERT Sentiment Analysis on IMDB

This model card describes a sentiment analysis model fine-tuned on the IMDB movie reviews dataset. The model uses a distilled version of BERT (DistilBERT) and is designed to classify reviews as either "positive" or "negative." It is intended for research and prototyping purposes.

## Model Details

### Model Description

This model is a fine-tuned version of the pre-trained `distilbert-base-uncased` model from Hugging Face. It has been adapted to perform binary sentiment classification (positive vs. negative) using the IMDB movie reviews dataset. The fine-tuning process leverages the Hugging Face Trainer API and custom evaluation metrics to optimize performance on sentiment analysis tasks.

- **Developed by:** Aygün Varol
- **Model type:** DistilBERT-based sentiment classifier
- **Language(s) (NLP):** English
- **License:** MIT License
- **Finetuned from model:** `distilbert-base-uncased`


### Model Sources

- **Repository:** [Link to GitHub repository](https://github.com/AygunVarol/sentiment-analysis-project)
- **Paper:** [Sanh et al., 2019, "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"](https://arxiv.org/abs/1910.01108)
- **Demo:** [Link to a demo](https://www.youtube.com/watch?v=9HHb9GtZIx4)

## Uses

### Direct Use

This model can be used directly for sentiment analysis of English text. Given an input review, it predicts whether the sentiment is positive or negative. It is suitable for prototyping applications such as movie review analysis, social media sentiment monitoring, or customer feedback analysis.

### Downstream Use

For applications that require additional customization (e.g., domain-specific sentiment analysis), this model can serve as a starting point for further fine-tuning or integration into larger natural language processing pipelines.

### Out-of-Scope Use

- **Non-English text:** The model is fine-tuned on English reviews and may not perform well on text in other languages.
- **Multiclass sentiment analysis:** This model is binary (positive/negative) and is not designed for more granular sentiment or emotion detection.
- **Highly specialized domains:** The IMDB dataset represents movie reviews, so performance might degrade on texts from very different domains without further fine-tuning.

## Bias, Risks, and Limitations

The IMDB dataset, like many public datasets, may contain inherent biases that can be reflected in the model predictions. For example:
- **Data Bias:** The training data may overrepresent certain types of reviews or sentiments.
- **Generalization:** The model may not generalize well to other domains (e.g., product reviews, social media posts) without additional fine-tuning.
- **Ethical Risks:** Misclassification in critical applications (e.g., automated moderation) may lead to undesired consequences. Users should evaluate the model carefully before deployment.

### Recommendations

Users should:
- Be aware of the biases present in the training data.
- Consider further fine-tuning on domain-specific datasets.
- Evaluate the model's performance on their specific data before using it in production environments.

## How to Get Started with the Model

To use the model, install the `transformers` library and load the model as follows:

```python
from transformers import pipeline

sentiment_classifier = pipeline("sentiment-analysis", model="Aygun/finetuned_distilbert_imdb")
result = sentiment_classifier("This movie was fantastic!")
print(result)
```

# Training Details

## Training Data

The model was fine-tuned on the IMDB movie reviews dataset. This dataset contains 50,000 movie reviews split evenly into positive and negative classes.
Training Procedure

The model was fine-tuned using the Hugging Face Trainer API with the following setup:

    Preprocessing: Reviews were tokenized with truncation and padding to a maximum sequence length of 256 tokens.
    Hyperparameters: The model was fine-tuned with a learning rate of 5e-5, a batch size of 16, and for 1 epoch (for demonstration purposes). For full training, more epochs and possibly different hyperparameters should be considered.
    Evaluation: The model’s performance was evaluated using accuracy, precision, recall, and F1-score metrics.

