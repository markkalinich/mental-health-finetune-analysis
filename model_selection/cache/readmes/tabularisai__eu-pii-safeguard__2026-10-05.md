---
language:
- bg
- cs
- da
- de
- el
- en
- es
- et
- fi
- fr
- ga
- hr
- hu
- it
- lt
- lv
- mt
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- uk
tags:
- token-classification
- pii-detection
- privacy
- gdpr
- multilingual
- xlm-roberta
- made in europe
- pii
- privacy filter
license: apache-2.0
license_name: commercial-evaluation
license_link: https://huggingface.co/tabularisai/eu-pii-safeguard/blob/main/LICENSE.md
extra_gated_prompt: >-
  **Free 30-day trial for commercial use**. Annual license required after trial.
  Academic use free forever.
extra_gated_fields:
  Organization: text
  Email: text
  Country: country
extra_gated_button_content: Accept License & Download
model-index:
- name: EU PII Safeguard
  results:
  - task:
      type: token-classification
      name: PII Detection
    metrics:
    - type: f1
      value: 0.9702
      name: F1 Score
    - type: precision
      value: 0.9702
      name: Precision
    - type: recall
      value: 0.9702
      name: Recall
base_model:
- FacebookAI/xlm-roberta-large
pipeline_tag: token-classification
---

<p align="center">
  <img src="https://tabularis.ai/pii_top_pic.png" alt="ModernFinBERT" width="512">
</p>

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/Discord%20button.png" width="200"/>](https://discord.gg/sznxwdqBXj)


# Multilingual Privacy Filter

**Multilingual PII Detection Model for European Languages**

A state-of-the-art multilingual model for detecting Personally Identifiable Information (PII) across 26 European languages (all EU official languages). It is designed for GDPR compliance, privacy-preserving AI applications, and secure handling of sensitive data in multilingual settings. This model enables enterprises, researchers, and data protection teams to identify and safeguard PII with high accuracy (≈98%) across diverse European contexts.
## 🎯 Model Performance

- **Global F1 Score: 97.02%**
- **26 Languages Supported**
- **42 PII Entity Types**
- **Consistent 95%+ F1 across all languages**

## 🌍 Supported Languages

🇧🇬 Bulgarian • 🇨🇿 Czech • 🇩🇰 Danish • 🇩🇪 German • 🇬🇷 Greek • 🇬🇧 English • 🇪🇸 Spanish • 🇪🇪 Estonian • 🇫🇮 Finnish • 🇫🇷 French • 🇮🇪 Irish • 🇭🇷 Croatian • 🇭🇺 Hungarian • 🇮🇹 Italian • 🇱🇹 Lithuanian • 🇱🇻 Latvian • 🇲🇹 Maltese • 🇳🇱 Dutch • 🇵🇱 Polish • 🇵🇹 Portuguese • 🇷🇴 Romanian • 🇷🇺 Russian • 🇸🇰 Slovak • 🇸🇮 Slovenian • 🇸🇪 Swedish • 🇺🇦 Ukrainian

## 🔍 Detected PII Types

- **Personal**: First/Last/Middle Names, Age, Gender, Ethnicity
- **Contact**: Email, Phone, Address, City, Country, Postal Code  
- **Financial**: Credit Card, IBAN, Account Numbers, Salary
- **Identity**: National ID, Passport, Driver License, Tax ID
- **Health**: Medical Conditions, Health Insurance ID
- **Digital**: IP Address, MAC Address, URL, Username, Password
- **And more**: 42 total entity types

## 🚀 Quick Start

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# Load model and tokenizer
model_name = "tabularisai/eu-pii-safeguard"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Example text (French)
text = "Bonjour, je suis Marie Dubois, email: marie@company.fr"

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt", truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)

# Get predictions
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
predicted_labels = [model.config.id2label[pred.item()] for pred in predictions[0]]

print("Detected PII:")
for token, label in zip(tokens, predicted_labels):
    if label != "O":
        print(f"  {label}: {token}")
```

## 📊 Performance by Language

| Language | F1 Score | Language | F1 Score |
|----------|----------|----------|----------|
| Irish (ga) | 97.98% | Dutch (nl) | 97.24% |
| Bulgarian (bg) | 97.80% | Slovak (sk) | 97.21% |
| Italian (it) | 97.68% | Swedish (sv) | 97.09% |
| Portuguese (pt) | 97.61% | Russian (ru) | 97.04% |
| Slovenian (sl) | 97.51% | Croatian (hr) | 96.93% |
| Czech (cs) | 97.51% | Polish (pl) | 96.63% |
| Hungarian (hu) | 97.50% | French (fr) | 96.59% |
| Estonian (et) | 97.41% | Romanian (ro) | 96.54% |
| Latvian (lv) | 97.40% | Danish (da) | 96.36% |
| English (en) | 97.36% | German (de) | 96.22% |
| Spanish (es) | 97.34% | Ukrainian (uk) | 96.09% |
| Finnish (fi) | 97.30% | Maltese (mt) | 95.78% |
| Lithuanian (lt) | 97.24% | Greek (el) | 95.42% |

## 💼 Use Cases

- **🔒 Data Privacy**: Automatically detect and anonymize PII before processing
- **⚖️ GDPR Compliance**: Ensure regulatory compliance across EU markets  
- **🛡️ Security**: Prevent data breaches by identifying sensitive information
- **📊 Data Governance**: Audit and catalog personal data in multilingual datasets

## 🏗️ Model Architecture

- **Base Model**: XLM-RoBERTa-large
- **Task**: Token Classification
- **Labels**: 74 (B-/I- format for 42 entity types)
- **Max Length**: 256 tokens



## 🔄 Community Feedback

We're actively seeking feedback from the community! Please:
- 🐛 Report issues or edge cases
- 💡 Suggest improvements
- 🧪 Share your use cases and results
- 📊 Contribute evaluation on new datasets


## 🏢 About Tabularis AI

Developed by [Tabularis AI](https://tabularis.ai) - Building privacy-preserving AI solutions for enterprise data protection.

---

*For questions, collaborations, or licensing inquiries: info@tabularis.ai*