---
license: mit
base_model: microsoft/deberta-v3-small
pipeline_tag: text-classification
tags:
- sequence-classification
- distillation
- infrastructure
- triage
datasets:
- martin76ec/infrastructure-incident-synthetic
metrics:
- accuracy
model-index:
- name: deberta-infrastructure-triage-distill
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: infrastructure-incident-synthetic
      type: martin76ec/infrastructure-incident-synthetic
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8841
---

# DeBERTa-v3-Small Distilled for Infrastructure Incident Triage

This model is a distilled version of `microsoft/deberta-v3-small` trained on synthetic infrastructure incident triage data ([`martin76ec/infrastructure-incident-synthetic`](https://huggingface.co/datasets/martin76ec/infrastructure-incident-synthetic)).

## Training Details
- **Base Model**: `microsoft/deberta-v3-small`
- **Task**: Binary Sequence Classification (Incident Escalation Triage)
- **Method**: Knowledge Distillation using KL Divergence ($T=2.0$) with soft probabilities + cross-entropy
- **Parameter-Efficient Fine-Tuning**: LoRA ($r=8$, $\alpha=16$, targeting `query_proj`, `value_proj`), merged into base model for standalone inference
- **Epochs**: 3
- **Learning Rate**: 3e-4
- **Precision**: bf16
- **Test Accuracy**: 88.42%

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "martin76ec/deberta-infrastructure-triage-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

premise = 'Incident State: {"incident_id": "INC-DB-20000", "alert_name": "AuroraPostgresConnectionSaturation", ...}'
hypothesis = 'Question: Determine which engineering team should own the escalation. Option: database_reliability_engineering'

inputs = tokenizer(premise, hypothesis, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class = logits.argmax().item()
```
