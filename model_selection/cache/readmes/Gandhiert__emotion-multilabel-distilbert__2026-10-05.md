
---
license: mit
tags:
- emotion-classification
- multilabel-classification
- text-classification
- pytorch
- transformers
- distilbert
language: en
metrics:
- f1_macro
- f1_micro
- hamming_loss
- jaccard_score
model-index:
- name: emotion-multilabel-distilbert
  results:
  - task:
      type: text-classification
      name: Emotion Multilabel Classification
    dataset:
      type: emotion-classification
      name: Emotion Classification Dataset
    metrics:
    - type: f1_macro
      value: 0.4214
      name: Macro F1-Score (Kaggle Test)
    - type: f1_macro
      value: 0.4275
      name: Macro F1-Score (Validation)
    - type: f1_micro
      value: 0.4226
      name: Micro F1-Score
    - type: hamming_loss
      value: 0.1816
      name: Hamming Loss
    - type: jaccard_score
      value: 0.2679
      name: Jaccard Score
---

# Emotion Multilabel Classification Model

🎭 A fine-tuned DistilBERT model for multilabel emotion classification on text data.

## Model Description

This model is fine-tuned from `distilbert-base-uncased` for multilabel emotion classification. It can predict multiple emotions simultaneously from text input across 14 different emotion categories.

## Performance

### Kaggle Competition Results
- **🏆 Kaggle Test Score (Macro F1)**: 0.4214
- **📊 Validation Score (Macro F1)**: 0.4275
- **🎯 Generalization Gap**: 0.0061 (excellent!)

### Detailed Metrics
- **Macro F1-Score**: 0.4275 (validation) / 0.4214 (test)
- **Micro F1-Score**: 0.4226
- **Hamming Loss**: 0.1816
- **Jaccard Score**: 0.2679

## Model Architecture

- **Base Model**: distilbert-base-uncased
- **Parameters**: 66,373,646 (~66M)
- **Architecture**: DistilBERT + Custom Classification Head
- **Dropout**: 0.3
- **Loss Function**: BCEWithLogitsLoss with class weights

## Emotions Supported

The model can predict the following 14 emotions:
['amusement', 'anger', 'annoyance', 'caring', 'confusion', 'disappointment', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'joy', 'love', 'sadness']

## Usage

```python
from transformers import AutoTokenizer, AutoModel
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("your-username/emotion-multilabel-distilbert")
model = AutoModel.from_pretrained("your-username/emotion-multilabel-distilbert")

# Example usage
text = "I'm so happy and excited about this project!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.sigmoid(outputs.logits)
    
# Get emotions above threshold (0.5)
emotions = []
for i, prob in enumerate(predictions[0]):
    if prob > 0.5:
        emotions.append(emotion_columns[i])
        
print(f"Predicted emotions: {', '.join(emotions)}")
```

## Training Details

- **Training Duration**: ~13 minutes
- **Hardware**: Tesla T4 GPU
- **Epochs**: 3
- **Batch Size**: 16
- **Learning Rate**: 2e-5
- **Max Sequence Length**: 128
- **Optimizer**: AdamW
- **Class Weights**: Applied for imbalanced dataset

## Dataset Statistics

- **Training Samples**: 37,164
- **Validation Samples**: 9,291
- **Test Samples**: 8,199
- **Average Labels per Sample**: 3.21
- **Most Common Pattern**: 2-4 emotions per text

## Performance Analysis

### Strengths
- ✅ Good generalization (small validation-test gap)
- ✅ Reasonable multilabel predictions (avg 3.21 labels)
- ✅ Fast inference (~9 iterations/second)
- ✅ Memory efficient (66M parameters)

### Areas for Improvement
- 📈 Macro F1 could be improved with hyperparameter tuning
- 📈 Class imbalance handling could be optimized
- 📈 Ensemble methods could boost performance

## License

This model is released under the MIT License.
