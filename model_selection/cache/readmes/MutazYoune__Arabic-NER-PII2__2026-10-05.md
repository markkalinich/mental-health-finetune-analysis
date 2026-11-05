---
language: ar
license: apache-2.0
tags:
- arabic
- ner
- named-entity-recognition
- bert
- token-classification
datasets:
- custom
metrics:
- f1
- precision
- recall
widget:
- text: "أحمد محمد يعمل في شركة جوجل في الرياض"
  example_title: "Arabic NER Example"
---

# MutazYoune/Arabic-NER-PII2

## Model Description

This is an Arabic Named Entity Recognition (NER) model fine-tuned on BERT architecture specifically for Arabic text processing. The model is based on `MutazYoune/ARAB_BERT` and has been trained to identify and classify named entities in Arabic text.

## Model Details

- **Model Type:** Token Classification (NER)
- **Language:** Arabic (ar)
- **Base Model:** MutazYoune/ARAB_BERT
- **Dataset:** augmented_pattern2
- **Task:** Named Entity Recognition

## Training Configuration

- **Epochs:** 30
- **Batch Size:** 16
- **Learning Rate:** 3e-05

## Supported Entity Types

- CONTACT
- IDENTIFIER
- NETWORK
- NUMERIC_ID
- PII

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("MutazYoune/Arabic-NER-PII2")
model = AutoModelForTokenClassification.from_pretrained("MutazYoune/Arabic-NER-PII2")

# Create NER pipeline
ner_pipeline = pipeline("ner", 
                       model=model, 
                       tokenizer=tokenizer,
                       aggregation_strategy="simple")

# Example usage
text = "أحمد محمد يعمل في شركة جوجل في الرياض"
entities = ner_pipeline(text)
print(entities)
```

## Model Performance

This model was trained on the complete dataset without validation split for final production use.

## Training Data

The model was trained on custom Arabic NER dataset:
- Dataset type: augmented_pattern2
- Combined training and test data for final model

## Citation

```bibtex
@misc{arabic-ner-bert,
  title={Arabic BERT NER Model},
  author={Trained on Kaggle},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/MutazYoune/Arabic-NER-PII2}
}
```
