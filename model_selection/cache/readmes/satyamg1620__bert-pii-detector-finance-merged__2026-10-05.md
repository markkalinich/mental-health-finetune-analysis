---
language:
- en
license: apache-2.0
tags:
- token-classification
- pii-detection
- named-entity-recognition
- privacy
- finance
- lora
- data-protection
metrics:
- accuracy
- f1
- precision
- recall
pipeline_tag: token-classification
widget:
- text: "Patient John Smith, DOB: 03/15/1985, SSN: 123-45-6789"
  example_title: "Healthcare PII"
---

# Healthcare PII Detection Model

## Model Description

This is a domain-specific Personally Identifiable Information (PII) detection model fine-tuned for **finance** applications. The model identifies and classifies sensitive information in finance text using token-level classification.

**Base Model:** bert-base-uncased (109M parameters)  
**Training Method:** LoRA (Low-Rank Adaptation)  
**Task:** Token Classification (Named Entity Recognition)  
**Entity Types:** 29 types

## Model Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | 80.00% |
| **F1 Score** | 62.04% |

**Training Dataset:** NVIDIA Nemotron-PII (finance domain)  
**Training Samples:** 15000  
**Training Epochs:** 3  
**LoRA Rank:** 8  
**Trainable Parameters:** ~521K (0.48% of base model)

## Detected Entity Types

### Common Finance PII Entities

- **Names:** first_name, last_name
- **Identifiers:** account_number, customer_id, tax_id
- **Contact:** email, phone_number, street_address, city, state, zipcode
- **Personal:** date_of_birth, age, gender, race_ethnicity
- **Sensitive:** credit_debit_card, bank_routing_number, swift_bic, cvv
- **Location:** coordinate, company_name, url

**Total:** 59 BIO labels across 29 entity types

## Intended Use

### Primary Use Cases

- **Data Anonymization:** Identify PII in finance documents for redaction
- **Privacy Compliance:** Detect sensitive data for HIPAA/GDPR compliance
- **Data Classification:** Classify and tag finance records by sensitivity
- **Access Control:** Implement role-based data masking

### Out-of-Scope Use

- Not designed for general domain PII detection (optimized for finance)
- Not a complete anonymization solution (requires post-processing)
- May have lower accuracy on non-finance text

## How to Use

### Installation

```bash
pip install transformers torch
```

### Basic Usage

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "your-org/mom-pii-finance"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare input
text = "Patient John Smith, DOB: 03/15/1985, SSN: 123-45-6789"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)[0]

# Extract entities
entities = []
current_entity = None

for token, pred_id in zip(tokens, predictions):
    if token in ['[CLS]', '[SEP]', '[PAD]']:
        continue
    
    label = model.config.id2label[pred_id.item()]
    
    if label.startswith('B-'):
        if current_entity:
            entities.append(current_entity)
        entity_type = label[2:]
        current_entity = {'type': entity_type, 'tokens': [token]}
    elif label.startswith('I-') and current_entity:
        current_entity['tokens'].append(token)
    else:
        if current_entity:
            entities.append(current_entity)
            current_entity = None

if current_entity:
    entities.append(current_entity)

# Clean up tokens
for entity in entities:
    entity['text'] = tokenizer.convert_tokens_to_string(entity['tokens'])
    print(f"{entity['type']}: {entity['text']}")
```

### Advanced Usage with Pipeline

```python
from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="your-org/mom-pii-finance",
    aggregation_strategy="simple",
    device=0  # Use GPU
)

results = ner("Patient John Smith, DOB: 03/15/1985, SSN: 123-45-6789")
for entity in results:
    print(f"{entity['entity_group']}: {entity['word']} ({entity['score']:.2f})")
```

## Training Details

### Training Data

- **Source:** NVIDIA Nemotron-PII dataset
- **Domain:** Finance
- **Total Dataset Size:** 100,000+ samples
- **Filtered for Domain:** 15000 samples
- **Entity Types:** 29 types
- **Labeling Scheme:** BIO (Begin, Inside, Outside)

### Training Configuration

- **Base Model:** bert-base-uncased
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **LoRA Configuration:**
  - Rank: 8
  - Alpha: 16
  - Dropout: 0.1
  - Target Modules: query, key, value
- **Optimizer:** AdamW
- **Learning Rate:** 3e-4
- **Batch Size:** 2 (per device)
- **Epochs:** 3
- **Warmup Steps:** 100
- **Weight Decay:** 0.01
- **FP16:** Disabled (FP32 for stability)
- **Training Time:** ~65 seconds on single GPU

### Framework Versions

- **Transformers:** 5.1.0
- **PyTorch:** 2.10.0+cu128
- **PEFT:** 0.18.1
- **Datasets:** 4.5.0

## Limitations and Biases

### Limitations

1. **Entity Coverage:** Strong on names, moderate on structured identifiers (IDs, phone numbers)
2. **Format Sensitivity:** May miss PII in unusual formats or with special characters
3. **Context Dependency:** Performance varies with entity context and surrounding text
4. **Domain Specificity:** Optimized for finance; may underperform on other domains

### Known Performance Characteristics

- **Strong:** Person names (first_name, last_name)
- **Moderate:** Dates, locations, occupations
- **Weak:** Formatted numbers (phone, SSN), complex identifiers

### Recommendations for Production

For structured PII (medical records, credit cards, phone numbers), consider:
- Combining with regex-based detection
- Post-processing with rule-based validators
- Ensemble approach with multiple models

## Ethical Considerations

### Responsible Use

- This model is designed for **privacy protection**, not surveillance
- Should be used to protect individuals' sensitive information
- Recommended for data anonymization pipelines with human review
- Regular audits recommended to ensure bias-free operation

### Privacy and Security

- Model itself does not store or transmit PII
- Detected entities should be handled according to data protection regulations
- Consider encryption and access controls for PII processing workflows

## Citation

```bibtex
@misc{mom-pii-finance-2026,
  title={Healthcare PII Detection Model},
  author={Your Organization},
  year={2026},
  publisher={HuggingFace},
  howpublished={\url{https://huggingface.co/your-org/mom-pii-finance}},
}
```

## Model Card Authors

- **Organization:** Your Organization
- **Contact:** your-email@example.com
- **Date:** February 2026

## License

Apache 2.0

## Acknowledgements

- Base model: google-bert/bert-base-uncased
- Training data: NVIDIA Nemotron-PII dataset
- Training framework: HuggingFace Transformers, PEFT
