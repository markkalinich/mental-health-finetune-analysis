---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- motivational-interviewing
- bert
- mental-health
- counseling
- psychology
- transformers
- pytorch
datasets:
- AnnoMI
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: bert-motivational-interviewing
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: AnnoMI
      type: AnnoMI
    metrics:
    - type: accuracy
      value: 0.701
      name: Accuracy
    - type: f1
      value: 0.579
      name: F1 Score (macro)
widget:
- text: "I really want to quit smoking."
  example_title: "Change Talk"
- text: "I don't know if I can do this."
  example_title: "Neutral"
- text: "I like smoking, it helps me relax."
  example_title: "Sustain Talk"
---

# BERT for Motivational Interviewing Client Talk Classification

## Model Description

This model is a fine-tuned **BERT-base-uncased** model for classifying client utterances in **Motivational Interviewing (MI)** conversations. 

Motivational Interviewing is a counseling approach used to help individuals overcome ambivalence and make positive behavioral changes. This model identifies different types of client talk that indicate their readiness for change.

## Intended Use

- **Primary Use**: Classify client statements in motivational interviewing dialogues
- **Applications**: 
  - Counselor training and feedback
  - MI session analysis
  - Automated dialogue systems
  - Mental health research

## Training Data

The model was trained on the **AnnoMI dataset** (Annotated Motivational Interviewing), which contains expert-annotated counseling dialogues.

- **Training samples**: ~2,400 utterances
- **Validation samples**: ~500 utterances  
- **Test samples**: ~700 utterances

## Labels

The model classifies client talk into three categories:

- **0**: change
- **1**: neutral
- **2**: sustain

### Label Definitions

- **Change Talk**: Client statements expressing desire, ability, reasons, or need for change
  - Example: "I really want to quit smoking" or "I think I can do it"

- **Neutral**: General responses without clear indication of change or sustain
  - Example: "I don't know" or "Maybe"

- **Sustain Talk**: Client statements expressing reasons for maintaining current behavior
  - Example: "I like smoking, it helps me relax"

## Performance

### Test Set Metrics

- **Accuracy**: 70.1%
- **Macro F1**: 57.9%
- **Macro Precision**: 59.3%
- **Macro Recall**: 57.3%

### Confusion Matrix

```
              Predicted
              change  neutral  sustain
Actual change    75      78       23
       neutral   43     396       27  
       sustain   11      34       36
```

**Note**: The model performs best on the "neutral" class (most frequent), and has room for improvement on "change" and "sustain" classes.

## Usage

### Quick Start

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model and tokenizer
model_name = "RyanDDD/bert-motivational-interviewing"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Predict
text = "I really want to quit smoking. It's been affecting my health."
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1)

label_map = model.config.id2label
print(f"Talk type: {label_map[pred.item()]}")
print(f"Confidence: {probs[0][pred].item():.2%}")
```

### Batch Prediction

```python
texts = [
    "I want to stop drinking.",
    "I don't think I have a problem.",
    "I like drinking with my friends."
]

inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    preds = torch.argmax(probs, dim=1)

for text, pred, prob in zip(texts, preds, probs):
    label = model.config.id2label[pred.item()]
    confidence = prob[pred].item()
    print(f"Text: {text}")
    print(f"Type: {label} ({confidence:.1%})")
    print()
```

## Training Details

### Hyperparameters

- **Base model**: `bert-base-uncased`
- **Max sequence length**: 128 tokens
- **Batch size**: 16
- **Learning rate**: 2e-5
- **Epochs**: 5
- **Optimizer**: AdamW
- **Loss**: Cross-entropy

### Hardware

Trained on a single GPU (NVIDIA GPU recommended).

## Limitations

1. **Class Imbalance**: The model performs better on "neutral" (majority class) than "change" and "sustain"
2. **Context**: The model classifies single utterances without conversation context
3. **Domain**: Trained specifically on MI conversations; may not generalize to other counseling types
4. **Language**: English only

## Ethical Considerations

- This model is intended to **assist**, not replace, human counselors
- Predictions should be reviewed by qualified professionals
- Privacy and confidentiality must be maintained when processing real counseling data
- Be aware of potential biases in training data

## Citation

If you use this model, please cite:

```bibtex
@misc{bert-mi-classifier-2024,
  author = {Ryan},
  title = {BERT for Motivational Interviewing Client Talk Classification},
  year = {2024},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/RyanDDD/bert-motivational-interviewing}}
}
```

## References

- **AnnoMI Dataset**: [GitHub](https://github.com/uccollab/AnnoMI)
- **BERT Paper**: [Devlin et al., 2019](https://arxiv.org/abs/1810.04805)
- **Motivational Interviewing**: [Miller & Rollnick, 2012](https://motivationalinterviewing.org/)

## Model Card Contact

For questions or feedback, please open an issue in the model repository.
