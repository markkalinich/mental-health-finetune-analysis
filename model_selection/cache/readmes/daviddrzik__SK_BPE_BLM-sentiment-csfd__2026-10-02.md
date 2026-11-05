---
license: mit
language:
- sk
pipeline_tag: text-classification
library_name: transformers
metrics:
- f1
base_model: daviddrzik/SK_BPE_BLM
tags:
- sentiment
---

# Fine-Tuned Sentiment Classification Model - SK_BPE_BLM (Movie reviews)

## Model Overview

This model is a fine-tuned version of the [SK_BPE_BLM model](https://huggingface.co/daviddrzik/SK_BPE_BLM) for the task of sentiment classification. It has been trained on a dataset containing movie reviews in the Czech language from the ČSFD dataset, which were then machine-translated into Slovak using Google Cloud Translation.

## Sentiment Labels

Each review in the dataset is labeled with one of the following sentiments:
- **Negative (0)**
- **Positive (1)**

## Dataset Details

The dataset used for fine-tuning comprises a total of 53,402 text records, labeled with sentiment as follows:
- **Negative records (0):** 25,618
- **Positive records (1):** 27,784

For more information about the dataset, please visit [this link](https://www.kaggle.com/datasets/lowoncuties/czech-movie-review-csfd/).

## Fine-Tuning Hyperparameters

The following hyperparameters were used during the fine-tuning process:

- **Learning Rate:** 5e-06
- **Training Batch Size:** 64
- **Evaluation Batch Size:** 64
- **Seed:** 42
- **Optimizer:** Adam (default)
- **Number of Epochs:** 5

## Model Performance

The model was evaluated using stratified 10-fold cross-validation, achieving a weighted F1-score with a median value of <span style="font-size: 24px;">**0.928**</span> across the folds.

## Model Usage

This model is suitable for sentiment classification in Slovak text, especially for user reviews of movies. It is specifically designed for applications requiring sentiment analysis of user reviews and may not generalize well to other types of text.

### Example Usage

Below is an example of how to use the fine-tuned `SK_Morph_BLM-sentiment-csfd` model in a Python script:

```python
import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizerFast

class SentimentClassifier:
    def __init__(self, tokenizer, model):
        self.model = RobertaForSequenceClassification.from_pretrained(model, num_labels=2)
        self.tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer, max_length=256)

    def tokenize_text(self, text):
        encoded_text = self.tokenizer.encode_plus(
            text.lower(), 
            max_length=256, 
            padding='max_length', 
            truncation=True, 
            return_tensors='pt'
        )
        return encoded_text

    def classify_text(self, encoded_text):
        with torch.no_grad():
            output = self.model(**encoded_text)
            logits = output.logits
            predicted_class = torch.argmax(logits, dim=1).item()
            probabilities = torch.softmax(logits, dim=1)
            class_probabilities = probabilities[0].tolist()
            predicted_class_text = self.model.config.id2label[predicted_class]
        return predicted_class, predicted_class_text, class_probabilities

# Instantiate the sentiment classifier with the specified tokenizer and model
classifier = SentimentClassifier(tokenizer="daviddrzik/SK_BPE_BLM", model="daviddrzik/SK_BPE_BLM-sentiment-csfd")

# Example text to classify sentiment
text_to_classify = "Tento film síce nebol najlepší aký som kedy videl, ale pozrel by som si ho opäť."
print("Text to classify: " + text_to_classify + "\n")

# Tokenize the input text
encoded_text = classifier.tokenize_text(text_to_classify)

# Classify the sentiment of the tokenized text
predicted_class, predicted_class_text, logits = classifier.classify_text(encoded_text)

# Print the predicted class label and index
print(f"Predicted class: {predicted_class_text} ({predicted_class})")
# Print the probabilities for each class
print(f"Class probabilities: {logits}")
```

Here is the output when running the above example:
```yaml
Text to classify: Tento film síce nebol najlepší aký som kedy videl, ale pozrel by som si ho opäť.

Predicted class: POSITIVE (1)
Class probabilities: [0.015124241821467876, 0.9848757386207581]
```