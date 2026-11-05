---
license: mit
datasets:
- dair-ai/emotion
language:
- en
metrics:
- accuracy
- f1
base_model:
- distilbert/distilbert-base-uncased
library_name: transformers
pipeline_tag: text-classification
tags:
- emotion-classification
- text-classification
- distilbert
- pytorch
- transformers
---

# Emotion Classification with DistilBERT

A fine-tuned DistilBERT model for emotion classification trained on the `dair-ai/emotion` dataset. This model classifies text into 6 emotion categories: sadness, joy, love, anger, fear, and surprise.

## Model Details

- **Model type**: DistilBERT for sequence classification
- **Base model**: `distilbert-base-uncased`
- **Language**: English
- **Number of classes**: 6
- **Task**: Text Classification (Emotion Recognition)
- **Architecture**: 6 layers, 12 attention heads, 768 hidden dimensions

### Emotion Categories

The model classifies text into the following 6 emotions:
- **sadness** (0)
- **joy** (1)
- **love** (2)
- **anger** (3)
- **fear** (4)
- **surprise** (5)

## Training Details

### Training Data
- **Dataset**: `dair-ai/emotion`
- **Training samples**: ~16,000
- **Validation samples**: ~2,000
- **Test samples**: ~2,000

### Training Configuration
- **Epochs**: 3
- **Batch size**: 16 (train), 32 (eval)
- **Learning rate**: 2e-5
- **Weight decay**: 0.01
- **Warmup ratio**: 0.06
- **Evaluation strategy**: epoch
- **Save strategy**: epoch
- **Best model metric**: F1 score (macro-averaged)

### Training Results
- **Best validation F1**: Model saved based on best F1 score during training
- **Best validation accuracy**: Model performance optimized for F1 metric

## Usage

### Using Transformers

```python
from transformers import pipeline

# Using the pipeline
classifier = pipeline("text-classification", model="your-username/emotion-distilbert-finetuned")
result = classifier("I feel great today!")
print(result)
# Output: [{'label': 'joy', 'score': 0.9876}]
```

### Direct Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("your-username/emotion-distilbert-finetuned")
model = AutoModelForSequenceClassification.from_pretrained("your-username/emotion-distilbert-finetuned")

# Emotion labels
emotion_labels = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

# Classify emotion
text = "I feel great today!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=1).item()

print(f"Predicted emotion: {emotion_labels[predicted_class]}")
```

### Inference API

```python
# Get all probabilities
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=1).squeeze()

for i, prob in enumerate(probabilities):
    print(f"{emotion_labels[i]}: {prob:.4f}")
```

## Model Architecture

- **Base Model**: DistilBERT (distilled version of BERT-base)
- **Hidden Size**: 768
- **Number of Layers**: 6
- **Attention Heads**: 12
- **Vocabulary Size**: 30,522
- **Max Position Embeddings**: 512
- **Classification Head**: Linear layer with 6 outputs

## Training Infrastructure

- **Framework**: PyTorch with Hugging Face Transformers
- **Optimizer**: AdamW
- **Learning Rate Scheduler**: Linear warmup followed by linear decay
- **Loss Function**: Cross-entropy loss for multi-class classification
- **Mixed Precision**: Not used (trained in FP32)

## Performance Notes

- Model was trained on a dataset balanced across emotion categories
- Best model checkpoint was selected based on validation F1 score
- Model performs well on various text lengths and domains
- May require domain adaptation for very specific use cases

## Limitations

- Trained primarily on English text
- May not generalize well to other languages
- Performance may vary across different text domains
- Model predictions should be used with appropriate confidence thresholds

## Citation

If you use this model, please cite the original dataset:

```
@inproceedings{saravia-etal-2018-carer,
    title = "{CARER}: Contextualized Affect Representations for Emotion Recognition",
    author = "Saravia, Elvis  and
      Liu, Hsien-Chi Toby  and
      Huang, Yen-Hao  and
      Wu, Junlin  and
      Chen, Yi-Shin",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D18-1404",
    doi = "10.18653/v1/D18-1404",
    pages = "3687--3697"
}
```