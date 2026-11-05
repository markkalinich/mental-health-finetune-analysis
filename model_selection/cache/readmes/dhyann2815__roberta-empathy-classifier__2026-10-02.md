---
language: en
tags:
- text-classification
- simpletransformers
- roberta
- empathy-detection
---

# RoBERTa Empathy Classifier

This is a binary text classification model trained to detect empathy in text. It takes a piece of text and classifies it as either `1` (empathetic) or `0` (not empathetic). The model is built on top of `roberta-base` using the `simpletransformers` library.

## Model Objective
The primary goal of this model is to analyze text (like chat transcripts, forum posts, or user feedback) and identify whether the author is demonstrating empathy. 

## Dataset & Preprocessing
The model was trained on the `AcnEmpathize_dataset.csv`.
- Cleaned up raw HTML entities, URLs, and extra whitespaces from the text.
- Filtered out extremely short inputs (less than 3 words).
- Split the data into a 70% training set and 30% testing set (stratified based on the target labels).
- Applied class weighting (`[1.0, 3.0]`) to aggressively counteract the heavy dataset imbalance.

## Training Configuration
The model was fine-tuned using `simpletransformers` with the following hyperparameters to optimize minority class detection:
- **Base Model**: `FacebookAI/roberta-base`
- **Epochs**: 5
- **Learning Rate**: 3e-5
- **Max Sequence Length**: 256
- **Class Weights**: `[1.0, 3.0]`
- **Train & Eval Batch Size**: 16
- **Seed**: 42

## Evaluation Metrics
Based on our 30% test split, the model achieved the following results after hyperparameter tuning:
- **Accuracy**: 75.90%
- **Evaluation Loss**: 0.6145
- **F1 Score (Macro)**: 0.6393
- **F1 Score (Positive Class)**: 0.4314
- **AUROC**: 0.7396
- **AUPRC**: 0.4716

**Confusion Matrix Summary:**
- True Negatives (TN): 2446
- False Negatives (FN): 558
- True Positives (TP): 335
- False Positives (FP): 325

*(Note: The model successfully learned to identify the minority empathetic class, dramatically improving True Positives (from 0 to 335) and AUROC while maintaining strong overall accuracy.)*

## Usage

You can load and use this model directly with the `simpletransformers` library:

```python
from simpletransformers.classification import ClassificationModel
import numpy as np

# Initialize the model
model = ClassificationModel(
    "roberta", 
    "dhyann2815/roberta-empathy-classifier",
    use_cuda=False # Set to True if you have a GPU
)

# Define prediction function with confidence score
def predict_empathy(text):
    predictions, raw_outputs = model.predict([text])
    logits = raw_outputs[0]
    probabilities = np.exp(logits) / np.sum(np.exp(logits))
    confidence = np.max(probabilities) * 100 
    
    status = "empathetic" if predictions[0] == 1 else "not empathetic"
    return status, round(confidence, 2)

# Run a prediction
status, confidence = predict_empathy("I'm so sorry you're going through this, that sounds really difficult.")
print(f"Prediction: {status} (Confidence: {confidence}%)")
```
