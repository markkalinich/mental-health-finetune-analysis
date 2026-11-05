---
license: apache-2.0
tags:
- text-classification
datasets:
- locuslab/safety_data_annotated
base_model:
- OrcaDB/gte-base-en-v1.5
---

# Safety Classification 

This is a fine-tuned version of `OrcaDB/gte-base-en-v1.5` for safety scoring.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained(
          "locuslab/safety-classifier_gte-base-en-v1.5",
          torch_dtype=torch.bfloat16,
          num_labels=6,
          trust_remote_code=True
        )
tokenizer = AutoTokenizer.from_pretrained("locuslab/safety-classifier_gte-base-en-v1.5")
```