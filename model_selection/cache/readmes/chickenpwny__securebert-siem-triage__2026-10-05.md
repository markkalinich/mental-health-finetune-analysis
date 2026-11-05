---
language:
- en
license: mit
tags:
- cybersecurity
- siem
- evtx
- mitre-attack
- sequence-classification
- soc
- threat-detection
- roberta
base_model: ehsanaghaei/SecureBERT
metrics:
- accuracy
pipeline_tag: text-classification
---

# SecureBERT SIEM Triage: 14-Tactic MITRE ATT&CK Classifier

A fine-tuned encoder for **SIEM and EVTX log triage**, classifying raw Windows Event Logs and SIEM telemetry into the 14 tactics of the MITRE ATT&CK enterprise matrix.

Built on top of [`ehsanaghaei/SecureBERT`](https://huggingface.co/ehsanaghaei/SecureBERT) (a RoBERTa-based encoder pretrained on cybersecurity text), this model was fine-tuned on labeled EVTX/SIEM telemetry for fast Tier-1 SOC log classification.

## Model Details
- **Base Model**: [ehsanaghaei/SecureBERT](https://huggingface.co/ehsanaghaei/SecureBERT) (RoBERTa architecture)
- **Architecture**: `RobertaForSequenceClassification`
- **Task**: Sequence Classification (14 MITRE ATT&CK tactics)
- **Max Sequence Length**: 512 tokens
- **Hidden Size**: 768
- **Layers**: 12
- **Language**: English (system logs, PowerShell scripts, command lines)
- **License**: MIT

## Training Results

Fine-tuned for 3 epochs (2,532 steps) on MITRE ATT&CK-labeled SIEM/EVTX telemetry:

| Epoch | Eval Accuracy | Eval Loss |
| :--- | :--- | :--- |
| 1 | 59.7% | 1.276 |
| 2 | 81.8% | 0.516 |
| 3 (final) | **89.5%** | **0.320** |

## MITRE ATT&CK 14-Tactic Coverage

`reconnaissance`, `resource-development`, `initial-access`, `execution`, `persistence`, `privilege-escalation`, `defense-evasion`, `credential-access`, `discovery`, `lateral-movement`, `collection`, `command-and-control`, `exfiltration`, `impact`

## Usage (Hugging Face `transformers`)

```python
import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "chickenpwny/securebert-siem-triage"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

alert = {
    "EventID": "4688",
    "CommandLine": "powershell.exe -ExecutionPolicy Bypass -enc SQBFAFgA..."
}
text = json.dumps(alert)

inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()

print(f"Predicted MITRE Tactic: {model.config.id2label[predicted_class_id]}")
```

## Intended Use & Gating

This model is designed to be used with a **confidence threshold** and **margin gate** rather than trusted blindly. We recommend withholding automated tagging for predictions under 80% confidence, or where the delta between the top-1 and top-2 predicted classes is less than 15%. Ambiguous logs should be escalated to a human analyst or a Tier-2 LLM.

## Limitations

- Trained on a specific EVTX/SIEM telemetry distribution; performance may vary on log formats or attack patterns not represented in training data.
- Single-label classification — a log entry is assigned exactly one tactic, even when multiple tactics could plausibly apply.
- Should be used as a Tier-1 pre-filter, not a standalone detection/response decision-maker.

## License

MIT License, consistent with the base SecureBERT model.
