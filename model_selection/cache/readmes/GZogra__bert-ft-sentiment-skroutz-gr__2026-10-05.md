---
library_name: transformers
tags: [bert, greek, sentiment-analysis, classification]
---

# Model Card for bert-sentiment-gr

This is a fine-tuned BERT model for sentiment analysis in Greek, trained to classify short texts or reviews as "positive" or "negative".

## Model Details

### Model Description

This model is a Greek BERT (`nlpaueb/bert-base-greek-uncased-v1`) fine-tuned on a dataset of reviews for sentiment classification. It predicts whether a given text expresses positive or negative sentiment.

- **Developed by:** George Zografos
- **Model type:** BERT (Transformer-based)
- **Language(s) (NLP):** Greek
- **License:** CC BY-SA 4.0
- **Finetuned from model [optional]:** nlpaueb/bert-base-greek-uncased-v1

### Model Sources [optional]

## Uses

### Direct Use

This model can be used for Greek text sentiment classification in reviews, comments, or social media content. It is suitable for tasks such as automated feedback analysis or social sentiment monitoring.

### Downstream Use [optional]

The model can be used as a feature extractor or as part of a pipeline for downstream tasks such as multi-class sentiment classification, recommendation systems, or opinion mining.

### Out-of-Scope Use

- Texts outside modern Greek or heavily domain-specific jargon may result in lower performance.  
- The model is not suitable for nuanced sentiment tasks requiring sarcasm or context beyond the sentence level.

## Bias, Risks, and Limitations

The model is trained on a limited dataset (~6.5K saples) of Greek reviews on Skroutz Reviews Dataset. 

About the Dataset: 
This is a dataset of shop reviews in Greek language from the website Skroutz for sentiment analysis. There are 6552 reviews divided into two categories 3276 positive and 3276 negative. There are three columns (id, review, label).
[Dataset](https://www.kaggle.com/datasets/nikosfragkis/skroutz-shop-reviews-sentiment-analysis)

Biases present in the dataset (e.g., overrepresentation of certain products, domains, or writing styles) may affect predictions. 
Users should be aware that the model may not generalize to all Greek text domains or dialects.

### Recommendations

Use caution in critical applications such as legal, medical, or high-stakes decision-making. Evaluate model outputs against domain-specific data before deployment.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "GZogra/bert-ft-sentiment-skroutz-gr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Example inference

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
inputs = {k: v.to(device) for k, v in inputs.items()}
with torch.no_grad():
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()

labels = {0: "negative", 1: "positive"}

text = "Το προϊόν ήταν εξαιρετικό!"
print(labels[pred])

```

## Training Details

### Training Data

- Source: `Skroutz_dataset.xlsx` with columns `id`, `text`, `label` (positive/negative)  
- Preprocessing: Removal of empty texts, normalization of labels, mapping to 0/1

### Training Procedure

- Tokenizer: `nlpaueb/bert-base-greek-uncased-v1` tokenizer  
- Max sequence length: 128  
- Framework: Hugging Face Transformers `Trainer`  
- Device: GPU if available, otherwise CPU

#### Training Hyperparameters

- **Training regime:** fp32 precision, standard fine-tuning
- **Learning rate:** 2e-5  
- **Batch size:** 16 per device (train & eval)  
- **Epochs:** 3  
- **Weight decay:** 0.01  
- **Evaluation & Save strategy:** per epoch  
- **Logging steps:** 50  
- **Metrics:** accuracy, F1-score, precision, recall

## Evaluation

### Testing Data, Factors & Metrics

- Test set: 10% of dataset, stratified sampling  
- Metrics computed: accuracy, F1-score, precision, recall

## Technical Specifications [optional]

### Model Architecture and Objective

- Architecture: BERT-based Transformer  
- Objective: Binary classification (positive/negative sentiment)
