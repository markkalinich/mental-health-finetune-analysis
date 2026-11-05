---
license: apache-2.0
tags:
- safety
- content-moderation
- multi-label-classification
- qwen2.5
- qlora
datasets:
- nvidia/Nemotron-Safety-Guard-Dataset-v3
---

# Qwen2.5-0.5B Multi-Class Safety Classifier

Fine-tuned on nvidia/Nemotron-Safety-Guard-Dataset-v3 using QLoRA.

## Output Format
```json
{"prompt_label": "safe|unsafe", "response_label": "safe|unsafe", "violated_categories": [...]}
```

## 23 Safety Categories
S1-Violence, S2-Sexual, S3-Criminal Planning, S4-Guns, S5-Substances,
S6-Suicide/Self Harm, S7-Sexual(minor), S8-Hate, S9-PII, S10-Harassment,
S11-Threat, S12-Profanity, S13-Needs Caution, S14-Other, S15-Manipulation,
S16-Fraud, S17-Malware, S18-High Risk Gov, S19-Political/Misinfo,
S20-Copyright, S21-Unauthorized Advice, S22-Illegal Activity, S23-Immoral
