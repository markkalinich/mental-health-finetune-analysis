---
library_name: transformers
tags: [token-classification, ner, deberta, privacy, pii-detection]
---

# Model Card for PII Detection with DeBERTa
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1RJMVrf8ZlbyYMabAQ2_GGm9Ln4FmMfoO)
This model is a fine-tuned version of [`microsoft/deberta`](https://huggingface.co/microsoft/deberta-v3-base) for Named Entity Recognition (NER), specifically designed for detecting Personally Identifiable Information (PII) entities like names, SSNs, phone numbers, credit card numbers, addresses, and more.

## Model Details

### Model Description

This transformer-based model is fine-tuned on a custom dataset to detect sensitive information, commonly categorized as PII. The model performs sequence labeling to identify entities using token-level classification.

- **Developed by:** [Maskify]
- **Finetuned from model:** `microsoft/deberta`
- **Model type:** Token Classification (NER)
- **Language(s):** English
- **Use case:** PII detection in text

# Training Details

## Training Data
The model was fine-tuned on a custom dataset containing labeled examples of the following PII entity types:

- NAME
- SSN
- PHONE-NO
- CREDIT-CARD-NO
- BANK-ACCOUNT-NO
- BANK-ROUTING-NO
- ADDRESS


### Epoch Logs

| Epoch | Train Loss | Val Loss | Precision | Recall | F1     | Accuracy |
|-------|------------|----------|-----------|--------|--------|----------|
| 1     | 0.3672     | 0.1987   | 0.7806    | 0.8114 | 0.7957 | 0.9534   |
| 2     | 0.1149     | 0.1011   | 0.9161    | 0.9772 | 0.9457 | 0.9797   |
| 3     | 0.0795     | 0.0889   | 0.9264    | 0.9825 | 0.9536 | 0.9813   |
| 4     | 0.0708     | 0.0880   | 0.9242    | 0.9842 | 0.9533 | 0.9806   |
| 5     | 0.0626     | 0.0858   | 0.9235    | 0.9851 | 0.9533 | 0.9806   |

## SeqEval Classification Report

| Label            | Precision | Recall | F1-score | Support |
|------------------|-----------|--------|----------|---------|
| ADDRESS          | 0.91      | 0.94   | 0.92     | 77      |
| BANK-ACCOUNT-NO  | 0.91      | 0.99   | 0.95     | 169     |
| BANK-ROUTING-NO  | 0.85      | 0.96   | 0.90     | 104     |
| CREDIT-CARD-NO   | 0.95      | 1.00   | 0.97     | 228     |
| NAME             | 0.98      | 0.97   | 0.97     | 164     |
| PHONE-NO         | 0.94      | 0.99   | 0.96     | 308     |
| SSN              | 0.87      | 1.00   | 0.93     | 90      |

### Summary
- **Micro avg:** 0.95
- **Macro avg:** 0.95
- **Weighted avg:** 0.95

## Evaluation

### Testing Data
Evaluation was done on a held-out portion of the same labeled dataset.

### Metrics
- Precision
- Recall
- F1 (via seqeval)
- Entity-wise breakdown
- Token-level accuracy

### Results
- F1-score consistently above 0.95 for most labels, showing robustness in PII detection.
- 
### Recommendations

- Use human review in high-risk environments.
- Evaluate on your own domain-specific data before deployment.

## How to Get Started with the Model

```python

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

model_name = "AI-Enthusiast11/pii-entity-extractor"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Post processing logic to combine the subword tokens
def merge_tokens(ner_results):
    entities = {}
    for entity in ner_results:
        entity_type = entity["entity_group"]
        entity_value = entity["word"].replace("##", "")  # Remove subword prefixes

        # Handle token merging
        if entity_type not in entities:
            entities[entity_type] = []
        if entities[entity_type] and not entity_value.startswith(" "):
            # If the previous token exists and this one isn't a new word, merge it
            entities[entity_type][-1] += entity_value
        else:
            entities[entity_type].append(entity_value)

    return entities

def redact_text_with_labels(text):
    ner_results = nlp(text)

    # Merge tokens for multi-token entities (if any)
    cleaned_entities = merge_tokens(ner_results)

    redacted_text = text
    for entity_type, values in cleaned_entities.items():
        for value in values:
            # Replace each identified entity with the label
            redacted_text = redacted_text.replace(value, f"[{entity_type}]")

    return redacted_text



#Loading the pipeline
nlp = pipeline("ner", model=model_name, tokenizer=tokenizer, aggregation_strategy="simple")

# Example input (choose one from your examples)
example = "Hi, I’m Mia Thompson. I recently noticed that my electricity bill hasn’t been updated despite making the payment last week. I used account number 4893172051 linked with routing number 192847561. My service was nearly suspended, and I’d appreciate it if you could verify the payment. You can reach me at 727-814-3902 if more information is needed."

# Run pipeline and process result
ner_results = nlp(example)
cleaned_entities = merge_tokens(ner_results)

# Print the NER results
print("\n==NER Results:==\n")
for entity_type, values in cleaned_entities.items():
    print(f"  {entity_type}: {', '.join(values)}")

# Redact the single example with labels
redacted_example = redact_text_with_labels(example)

# Print the redacted result
print(f"\n==Redacted Example:==\n{redacted_example}")
