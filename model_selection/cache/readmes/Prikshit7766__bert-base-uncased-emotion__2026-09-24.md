---
license: mit
datasets:
- dair-ai/emotion
language:
- en
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
library_name: transformers
tags:
- emotion-classification
---


# BERT-Base-Uncased Emotion Classification Model

## Model Architecture
- **Base Model**: `bert-base-uncased`
- **Architecture**: Transformer-based model (BERT)
- **Fine-Tuned Task**: Emotion classification
- **Number of Labels**: 6 (sadness, joy, love, anger, fear, surprise)

## Dataset Information
The model was fine-tuned on the `dair-ai/emotion` dataset, which consists of English tweets classified into six emotion categories.

- **Training Dataset Size**: 16,000 examples
- **Validation Dataset Size**: 2,000 examples
- **Test Dataset Size**: 2,000 examples
- **Features**:
  - `text`: The text of the tweet
  - `label`: The emotion label for the text (ClassLabel: `['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']`)

## Training Arguments
The model was trained using the following hyperparameters:

- **Learning Rate**: 2e-05
- **Batch Size**: 16
- **Number of Epochs**: 20 (stopped early at 7 epochs)
- **Gradient Accumulation Steps**: 2
- **Weight Decay**: 0.01
- **Mixed Precision (FP16)**: True
- **Early Stopping**: Enabled (see details below)
- **Logging**: Progress logged every 100 steps
- **Save Strategy**: Checkpoints saved at the end of each epoch, with the 3 most recent checkpoints retained

The model was trained for 7 epochs, but it stopped early due to early stopping. Early stopping was configured with the following details:
- **Patience**: 3 epochs (training stops if no improvement in F1 score for 3 consecutive evaluations)
- **Best Metric**: F1 score (greater is better)
- **Final Epoch**: The model was trained for 7 epochs (out of the planned 20) and stopped early due to no improvement in evaluation metrics.

## Final Training Metrics (After 7 Epochs)
The model achieved the following results on the validation dataset in the final epoch:

- **Accuracy**: 0.9085
- **Precision**: 0.8736
- **Recall**: 0.8962
- **F1 Score**: 0.8824

## Test Set Evaluation
After training, the model was evaluated on a held-out test set. The following are the results on the test dataset:

- **Test Accuracy**: 0.9180
- **Test Precision**: 0.8663
- **Test Recall**: 0.8757
- **Test F1 Score**: 0.8706

## Usage

You can load the model and tokenizer for inference using the Hugging Face `transformers` library with the `pipeline`:

```python
from transformers import pipeline

# Load the emotion classification pipeline
classifier = pipeline("text-classification", model='Prikshit7766/bert-base-uncased-emotion', return_all_scores=True)

# Test the classifier with a sample sentence
prediction = classifier("I am feeling great and happy today!")

# Print the predictions
print(prediction)

```

**Output**

```
  [[{'label': 'sadness', 'score': 0.00010687233589123935},
    {'label': 'joy', 'score': 0.9991187453269958},
    {'label': 'love', 'score': 0.00041500659426674247},
    {'label': 'anger', 'score': 7.090374856488779e-05},
    {'label': 'fear', 'score': 5.2315706852823496e-05},
    {'label': 'surprise', 'score': 0.0002362433006055653}]]
```