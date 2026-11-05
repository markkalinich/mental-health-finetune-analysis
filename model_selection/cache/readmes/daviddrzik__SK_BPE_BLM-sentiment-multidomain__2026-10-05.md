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

# Fine-Tuned Sentiment Classification Model - SK_BPE_BLM (Universal multi-domain sentiment classification)

## Model Overview

This model is a fine-tuned version of the [SK_BPE_BLM model](https://huggingface.co/daviddrzik/SK_BPE_BLM) for the task of sentiment classification. It has been trained on datasets from multiple domains, including banking, social media, movie reviews, politics, and product reviews. Some of these datasets were originally in Czech and were machine-translated into Slovak using Google Cloud Translation.

## Sentiment Labels

Each row in the dataset is labeled with one of the following sentiments:
- **Negative (0)**
- **Neutral (1)**
- **Positive (2)**

## Dataset Details

The dataset used for fine-tuning comprises text records from various domains. Below are the details for each domain:

### Banking Domain
- **Source**: [Banking Dataset](https://doi.org/10.1016/j.procs.2023.10.346)
- **Description**: Sentences from the annual reports of a commercial bank in Slovakia.
- **Records per Class**: 923
- **Unique Words**: 11,469
- **Average Words per Record**: 20.93
- **Average Characters per Word**: 142.41

### Social Media Domain
- **Source**: [Social Media Dataset](http://hdl.handle.net/11858/00-097C-0000-0022-FE82-7)
- **Description**: Data from posts on the Facebook social network.
- **Records per Class**: 1,991
- **Unique Words**: 114,549
- **Average Words per Record**: 9.24
- **Average Characters per Word**: 57.11

### Movies Domain
- **Source**: [Movies Dataset](https://doi.org/10.1016/j.ipm.2014.05.001)
- **Description**: Short movie reviews from ČSFD.
- **Records per Class**: 3,000
- **Unique Words**: 72,166
- **Average Words per Record**: 52.12
- **Average Characters per Word**: 330.92

### Politics Domain
- **Source**: [Politics Dataset](https://doi.org/10.48550/arXiv.2309.09783)
- **Description**: Sentences from Slovak parliamentary proceedings.
- **Records per Class**: 452
- **Unique Words**: 6,697
- **Average Words per Record**: 12.31
- **Average Characters per Word**: 85.22

### Reviews Domain
- **Source**: [Reviews Dataset](https://aclanthology.org/W13-1609)
- **Description**: Product reviews from Mall.cz.
- **Records per Class**: 3,000
- **Unique Words**: 35,941
- **Average Words per Record**: 21.05
- **Average Characters per Word**: 137.33

## Fine-Tuning Hyperparameters

The following hyperparameters were used during the fine-tuning process:

- **Learning Rate:** 1e-05
- **Training Batch Size:** 64
- **Evaluation Batch Size:** 64
- **Seed:** 42
- **Optimizer:** Adam (default)
- **Number of Epochs:** 15 (with early stopping)

## Model Performance

The model was trained on data from all domains simultaneously and evaluated using stratified 10-fold cross-validation on each individual domain. The weighted F1-score, including the mean, minimum, maximum, and quartile values, is presented below for each domain:

| Domain       | Mean | Min  | 25%  | 50%  | 75%  | Max  |
|--------------|------|------|------|------|------|------|
| Banking      | 0.658| 0.608| 0.645| 0.658| 0.674| 0.697|
| Social media | 0.575| 0.552| 0.570| 0.577| 0.581| 0.599|
| Movies       | 0.572| 0.518| 0.555| 0.580| 0.590| 0.615|
| Politics     | 0.613| 0.576| 0.602| 0.614| 0.623| 0.644|
| Reviews      | 0.576| 0.555| 0.562| 0.575| 0.583| 0.608|


## Model Usage

This model is suitable for sentiment classification within the specific domains it was trained on, such as banking, social media, movies, politics, and product reviews. While it may not achieve high F1-scores across all text types, it is well-suited for a wide range of text within these trained domains. However, it may not generalize effectively to entirely different types of text outside these domains.

### Example Usage

Below is an example of how to use the fine-tuned `SK_Morph_BLM-sentiment-multidomain` model in a Python script:

```python
import torch
from transformers import RobertaForSequenceClassification, RobertaTokenizerFast

class SentimentClassifier:
    def __init__(self, tokenizer, model):
        self.model = RobertaForSequenceClassification.from_pretrained(model, num_labels=3)
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
classifier = SentimentClassifier(tokenizer="daviddrzik/SK_BPE_BLM", model="daviddrzik/SK_BPE_BLM-sentiment-multidomain")

# Example text to classify sentiment
text_to_classify = "Napriek zlepšeniu očakávaní je výhľad stále krehký."
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
Text to classify: Napriek zlepšeniu očakávaní je výhľad stále krehký.

Predicted class: Positive (2)
Class probabilities: [0.003513934789225459, 0.3542619049549103, 0.642224133014679]
```
