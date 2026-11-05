---
license: agpl-3.0
language:
- en
base_model:
- bert-large-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- sentiment-analysis
- healthcare
- lifestyle
- bert
- fine-tuned
- pytorch
datasets:
- custom
widget:
- text: "I feel energetic and motivated to exercise regularly"
  example_title: "Positive Lifestyle"
- text: "I struggle to maintain any physical activity routine"
  example_title: "Negative Lifestyle"
- text: "My activity level is average, nothing special"
  example_title: "Neutral Lifestyle"
model-index:
- name: bert-sentiment-wqd7007
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      type: custom
      name: Healthcare Lifestyle Dataset
    metrics:
    - type: accuracy
      name: Validation Accuracy
      value: 0.85
    - type: f1
      name: F1 Score
      value: 0.83
---

# BERT Sentiment Analysis for Healthcare Lifestyle Assessment

## Model Description

This model is a fine-tuned version of `bert-large-uncased` for sentiment analysis on healthcare lifestyle descriptions. The model classifies text descriptions of lifestyle and activity levels into three sentiment categories: **positive**, **neutral**, and **negative**.

## Intended Use

This model is designed to analyze patient descriptions of their lifestyle and activity levels to automatically classify the sentiment, which can assist healthcare professionals in understanding patient attitudes toward physical activity and lifestyle management.

### Primary Use Cases
- Healthcare sentiment analysis
- Patient lifestyle assessment
- Activity level sentiment classification
- Healthcare research and analytics

## Training Details

### Training Data
- **Source**: Custom healthcare questionnaire dataset (`patients_with_ratings.csv`) with patient lifestyle descriptions
- **Labels**: Activity sentiment derived from activity level ratings (1-5 scale converted to sentiment)
  - Ratings 1-2: Negative sentiment
  - Rating 3: Neutral sentiment  
  - Ratings 4-5: Positive sentiment
- **Split**: 80% training, 20% validation (stratified split)
- **Text Column**: `describe_lifestyle` - patient descriptions of their lifestyle
- **Target**: `activity_sentiment` - sentiment labels (positive/neutral/negative)

### Training Configuration
- **Base Model**: `bert-large-uncased`
- **Training Epochs**: 30
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Max Sequence Length**: 128 tokens
- **Device**: CUDA (A100 GPU)
- **Framework**: PyTorch with Transformers library
- **Random Seed**: 42 (for reproducibility)

### Training Process
The model was trained using standard fine-tuning procedures:
1. Data preprocessing with NaN value handling
2. Text preprocessing and tokenization using BERT tokenizer
3. Conversion of sentiment labels to integer mappings (positive: 0, neutral: 1, negative: 2)
4. Stratified train-test split to maintain class distribution
5. Training with cross-entropy loss and AdamW optimization
6. Validation performed after each epoch to monitor performance
7. Loss tracking for both training and validation phases

## Model Performance

The model was evaluated on the validation set with detailed classification reports. Performance metrics include:
- **Validation Accuracy**: ~85%
- **F1 Score**: ~83%

Detailed precision, recall, and F1-score metrics are generated for all three sentiment classes (positive, neutral, negative).

## Usage

### Quick Start with Pipeline

```python
from transformers import pipeline

# Create sentiment analysis pipeline
classifier = pipeline("text-classification", 
                     model="keanteng/bert-sentiment-wqd7007")

# Analyze sentiment
result = classifier("I maintain a regular exercise routine and feel great")
print(result)
# Output: [{'label': 'LABEL_0', 'score': 0.9234}]
```

### Using the Model with Transformers

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the model and tokenizer
tokenizer = BertTokenizer.from_pretrained('google-bert/bert-large-uncased')
model = BertForSequenceClassification.from_pretrained('keanteng/bert-sentiment-wqd7007')

# Prepare input text
text = "I feel energetic and try to exercise every day"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1)

# Map prediction to sentiment
sentiment_map = {0: 'positive', 1: 'neutral', 2: 'negative'}
predicted_sentiment = sentiment_map[predicted_class.item()]
confidence = predictions.max().item()

print(f"Predicted sentiment: {predicted_sentiment}")
print(f"Confidence: {confidence:.4f}")
```

### Batch Processing

```python
# For multiple texts
texts = [
    "I love staying active and exercising daily",
    "My activity level is okay, nothing special",
    "I struggle to find motivation for physical activities"
]

# Tokenize all texts
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)

# Get predictions for all texts
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_classes = torch.argmax(predictions, dim=-1)

# Process results
for i, text in enumerate(texts):
    sentiment = sentiment_map[predicted_classes[i].item()]
    confidence = predictions[i].max().item()
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment} (confidence: {confidence:.4f})")
    print()
```

## Label Mapping

- **LABEL_0**: Positive sentiment (activity levels 4-5)
- **LABEL_1**: Neutral sentiment (activity level 3)
- **LABEL_2**: Negative sentiment (activity levels 1-2)

## Training Visualizations

The model includes training and validation loss curves with best epoch identification, saved as visualizations in the model repository.

## Limitations and Considerations

- The model is specifically trained on healthcare/lifestyle descriptions and may not generalize well to other domains
- Performance may vary on text significantly different from the training distribution
- The model should be used as a supportive tool and not as a replacement for professional healthcare assessment
- Bias may exist based on the characteristics of the training data
- Model performance is dependent on the quality and representativeness of the input healthcare questionnaire data

## Ethical Considerations

This model is intended for research and healthcare support purposes. When used in healthcare settings:
- Results should be interpreted by qualified healthcare professionals
- Patient privacy and data protection protocols must be followed
- The model should complement, not replace, clinical judgment
- Consider potential biases in the training data when interpreting results
- Ensure appropriate consent and data handling procedures are in place

### Reproducibility
All training was conducted with fixed random seeds (42) for reproducibility across PyTorch and NumPy operations.
