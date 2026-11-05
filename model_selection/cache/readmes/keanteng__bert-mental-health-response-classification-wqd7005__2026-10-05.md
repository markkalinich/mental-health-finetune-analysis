
---
license: agpl-3.0
language:
- en
tags:
- text-classification
- bert
- healthcare
- risk-assessment
- questionnaire-analysis
pipeline_tag: text-classification
metrics:
- accuracy
base_model:
- google-bert/bert-base-uncased
library_name: transformers
---

# BERT Classification Models for Mental Health Responses

This repository contains fine-tuned BERT models for classifying healthcare questionnaire responses into risk categories.

## Model Description

BERT-base-uncased models have been fine-tuned for healthcare risk assessment:

1. **Mental Health Model**: Classifies mental health-related responses


The models predict three risk categories:
- **Low Risk** (0)
- **Moderate Risk** (1) 
- **High Risk** (2)

## Training Details

- **Base Model**: bert-base-uncased
- **Training Epochs**: 40
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Max Sequence Length**: 128

## Usage

### Loading the Models

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Load mental health model
mental_health_model = BertForSequenceClassification.from_pretrained('keanteng/bert-mental-health-response-classification-wqd7005')
```

### Making Predictions

```python
def predict_risk(text, model, tokenizer, max_length=128):
    # Tokenize input
    inputs = tokenizer(
        text,
        padding='max_length',
        truncation=True,
        max_length=max_length,
        return_tensors='pt'
    )
    
    # Make prediction
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(predictions, dim=-1)
    
    # Map to risk categories
    risk_labels = ['Low Risk', 'Moderate Risk', 'High Risk']
    return risk_labels[predicted_class.item()], predictions[0].tolist()

# Example usage
mental_health_text = "I am feeling devastated from the lost of my love ones. My heart is really painful."
risk_category, confidence_scores = predict_risk(mental_health_text, mental_health_model, tokenizer)
print(f"Risk Category: {risk_category}")
print(f"Confidence Scores: {confidence_scores}")
```

## Model Performance

The models were trained and evaluated on healthcare questionnaire data with the following label mapping:

**Mental Health Model:**
- Mental health levels 1-2 → High Risk
- Mental health level 3 → Moderate Risk
- Mental health levels 4-5 → Low Risk

## Training Data

The models were trained on questionnaire responses containing:
- Text descriptions of mental health status
- Corresponding risk labels

Data was split 80/20 for training and validation with stratified sampling.

## Intended Use

These models are designed for:
- Healthcare questionnaire analysis
- Risk assessment screening
- Research applications in healthcare NLP

**Important**: These models are for research and screening purposes only and should not replace professional medical diagnosis.

## Limitations

- Models are trained on specific questionnaire formats
- Performance may vary on different populations or text styles
- Should be used as a screening tool, not for final diagnosis
- May have biases present in the training data