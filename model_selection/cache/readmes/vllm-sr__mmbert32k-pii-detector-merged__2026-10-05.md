---
base_model: vllm-sr/mmbert-32k-yarn
language: en
license: mit
tags:
  - modernbert
  - pii-detection
  - token-classification
  - mmbert
  - 32k-context
  - semantic-router
datasets:
  - ai4privacy/pii-masking-400k
  - Presidio
pipeline_tag: token-classification
---

# mmBERT-32K PII Detector (Merged)

Full merged model for PII (Personally Identifiable Information) detection, ready for direct inference. Based on mmBERT-32K-YaRN with 32K context length support.

## Model Details

| Property | Value |
|----------|-------|
| Base Model | [vllm-sr/mmbert-32k-yarn](https://huggingface.co/vllm-sr/mmbert-32k-yarn) |
| Architecture | ModernBERT (Flash Attention 2) |
| Parameters | 307M |
| Task | Token Classification (NER) |
| Max Context | 32,768 tokens |
| Entity Types | 17 PII types (35 BIO labels) |

## Supported PII Types

- `PERSON` - Person names (98.7% accuracy)
- `EMAIL_ADDRESS` - Email addresses (95%+ accuracy)
- `PHONE_NUMBER` - Phone numbers (99.1% accuracy)
- `STREET_ADDRESS` - Street addresses (95.9% accuracy)
- `CREDIT_CARD` - Credit card numbers (84% accuracy)
- `US_SSN` - US Social Security Numbers
- `US_DRIVER_LICENSE` - US Driver License numbers
- `IBAN_CODE` - International Bank Account Numbers
- `IP_ADDRESS` - IP addresses
- `DATE_TIME` - Dates and times
- `AGE` - Age information
- `ORGANIZATION` - Organization names
- `GPE` - Geopolitical entities
- `ZIP_CODE` - ZIP/postal codes
- `DOMAIN_NAME` - Domain names
- `NRP` - Nationalities, religious or political groups
- `TITLE` - Titles (Mr., Dr., etc.)

## Training

- **Dataset**: Microsoft Presidio research dataset
- **Epochs**: 5
- **Batch Size**: 16
- **Learning Rate**: 1e-4
- **LoRA Rank**: 32 (merged into full model)

## Usage

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

model = AutoModelForTokenClassification.from_pretrained(
    "vllm-sr/mmbert32k-pii-detector-merged"
)
tokenizer = AutoTokenizer.from_pretrained(
    "vllm-sr/mmbert32k-pii-detector-merged"
)

text = "My email is john.smith@example.com and phone is 555-123-4567"
inputs = tokenizer(text, return_tensors="pt", truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=2)

# Get label mapping
id2label = model.config.id2label
for token, pred in zip(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0]), predictions[0]):
    label = id2label[str(pred.item())]
    if label != "O":
        print(f"{token}: {label}")
```

## Part of vLLM Semantic Router

This model is part of the [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) Mixture-of-Models (MoM) family for intelligent LLM request routing.

## License

MIT License
