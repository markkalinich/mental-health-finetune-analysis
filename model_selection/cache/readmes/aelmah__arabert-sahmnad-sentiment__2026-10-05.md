---
license: mit
language:
- ar
tags:
- sentiment-analysis
- arabic
- bert
- text-classification
- arabic-nlp
- moroccan-press
datasets:
- SAHMNAD
metrics:
- accuracy
- f1
base_model:
- aubmindlab/bert-base-arabertv02
pipeline_tag: text-classification
---

# AraBERT Fine-tuned on SAHMNAD — Arabic News Headlines Sentiment Analysis

Fine-tuned **aubmindlab/bert-base-arabertv02** for Arabic sentiment classification (positive/negative) on Moroccan news headlines from the SAHMNAD dataset.

## Model Description

This model classifies Arabic news headlines into positive or negative sentiment with **90.47% accuracy**. Built using transfer learning on bert-base-arabertv02 with task-specific fine-tuning for binary sentiment analysis on Moroccan press headlines (Hibapress).

##  Quick Start
```python
from transformers import pipeline

# Load model
classifier = pipeline("text-classification", model="aelmah/arabert-sahmnad-sentiment")

# Predict
result = classifier("فاز المنتخب المغربي بنتيجة كبيرة")
print(result)

# Batch prediction
texts = [
    "فاس.. دورة استثنائية بجماعة زواغة تغيب عنها المعارضة",
    "بعد إطلاق صاروخ.. الطيران الإسرائيلي يقصف مواقع في قطاع غزة"
]
results = classifier(texts)
```

##  Performance on SAHMNAD Test Set

| Metric   | Value  |
|----------|--------|
| Accuracy | 90.47% |
| F1-score | 90.31% |

### Training Progress

| Epoch | Training Loss | Validation Loss | Accuracy | F1     |
|-------|--------------|-----------------|----------|--------|
| 1     | —            | 0.2867          | 88.53%   | 87.60% |
| 2     | 0.3412       | 0.2704          | 90.23%   | 89.65% |
| 3     | 0.2066       | 0.2789          | 90.47%   | 90.31% |

##  Training Details

### Base Model
- **Architecture**: BERT-base (12 layers, 768 hidden, 12 attention heads)
- **Pre-trained**: aubmindlab/bert-base-arabertv02
- **Parameters**: ~110M

### Training
- **Optimizer**: AdamW
- **Learning Rate**: 2e-5
- **Batch Size**: 32
- **Epochs**: 3
- **Max Length**: 128 tokens
- **Hardware**: GPU (fp16 mixed precision)
- **Framework**: Hugging Face Trainer API — Google Colab

##  Training Data

**SAHMNAD** (Sentiment-Annotated Hibapress M-NAD) — Arabic news headlines from Hibapress, annotated with binary sentiment labels (0 = negative, 1 = positive).

| Split | Examples |
|-------|----------|
| Train | 13,174   |
| Test  | 3,295    |

- Source: [Kaggle — SAHMNAD](https://www.kaggle.com/datasets/jannaniayoub/sentiment-annotated-hibapress-m-nad-sahmnad)

##  Intended Use

### Direct Use
- Arabic news headlines sentiment monitoring
- Moroccan press opinion mining
- Binary sentiment classification for Arabic short text

### Limitations
- Binary classification only (positive/negative) — neutral not supported
- Trained on Moroccan press headlines — may underperform on other domains
- Best with short text under 128 tokens

##  Links
- **Base Model**: [aubmindlab/bert-base-arabertv02](https://huggingface.co/aubmindlab/bert-base-arabertv02)
- **Dataset**: [SAHMNAD on Kaggle](https://www.kaggle.com/datasets/jannaniayoub/sentiment-annotated-hibapress-m-nad-sahmnad)
- **Code**: [Google Colab Notebook](lien-à-ajouter)

##  License
MIT License