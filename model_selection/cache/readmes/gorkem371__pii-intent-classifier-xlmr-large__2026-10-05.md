---
language:
  - tr
  - ar
  - en
license: apache-2.0
library_name: transformers
tags:
  - pii-detection
  - text-classification
  - content-moderation
  - xlm-roberta
  - multilingual
datasets:
  - gorkem371/pii-intent-detection-multilingual
metrics:
  - accuracy
  - f1
  - precision
  - recall
pipeline_tag: text-classification
base_model: xlm-roberta-large
widget:
  - text: "my number is 05321234567 call me anytime </s> 05321234567 | PHONE"
    example_title: "PII - Direct sharing (EN)"
  - text: "your order number is ORD-784321 </s> ORD-784321 | PHONE"
    example_title: "NOT PII - Order number (EN)"
  - text: "numaram 05321234567 bana yazabilirsin </s> 05321234567 | PHONE"
    example_title: "PII - Direct sharing (TR)"
  - text: "رقمي 0501234567 تواصل معي </s> 0501234567 | PHONE"
    example_title: "PII - Direct sharing (AR)"
  - text: "i will send you my whatsapp tomorrow </s> NONE | PHONE"
    example_title: "PII - Future intent (EN)"
  - text: "05321234567 this number is a scammer do not call </s> 05321234567 | PHONE"
    example_title: "NOT PII - Scam warning (EN)"
  - text: "follow me on instagram @creator_official </s> @creator_official | SOCIAL_MEDIA"
    example_title: "PII - Social media (EN)"
  - text: "bake at 180 degrees celsius for 45 minutes </s> 180 | PHONE"
    example_title: "NOT PII - Non-contact number (EN)"
inference: true
model-index:
  - name: pii-intent-classifier-xlmr-large
    results:
      - task:
          type: text-classification
          name: PII Intent Classification
        metrics:
          - name: Validation F1
            type: f1
            value: 0.9933
          - name: Validation Accuracy
            type: accuracy
            value: 0.9924
          - name: Stress Test Accuracy
            type: accuracy
            value: 0.949
          - name: Conversation Test Accuracy
            type: accuracy
            value: 0.970
---

# PII Intent Classifier - XLM-RoBERTa Large (V11)

A multilingual binary classifier that detects **PII (Personally Identifiable Information) sharing intent** in text messages. Built for content moderation on creator-brand collaboration platforms.

## What's New in V11

V11 is the 15th iteration of this model, trained on 41,427 samples (up from 24,012 in V7c). Key improvements:

- **Conversation test**: 97.0% accuracy (838/864) - up from 95.0% in V10
- **Targeted training data**: ~200 new samples addressing specific failure patterns (scam+real phone, asking about numbers, humorous sharing, room/postal/tracking numbers as NOT-PII)
- **6 new CoT categories**: room_number, postal_code, time_digits, tracking_number, username_digits, goodnight_casual
- **Strict policy**: Any real phone/email/IBAN/handle = PII regardless of context (humor, scam warning, inquiry)

### Version History

| Version | Stress Test | Conversation | Training Data | Key Change |
|---------|------------|--------------|---------------|------------|
| V7c | 173/177 (98%) | - | 24,012 | First production model |
| V8 | 174/177 (98%) | - | 24,012 | +name_intro, greeting_slang |
| V9 | - | - | 39,303 | +"real contact = always PII" policy |
| V10 | 172/177 (97%) | 821/864 (95%) | 39,789 | +entity×label balance fix |
| **V11** | **168/177 (95%)** | **838/864 (97%)** | **41,427** | +targeted error fixes |

## Model Description

This model classifies whether a message contains an intent to share personal contact information (phone numbers, emails, social media handles, IBANs, etc.) or not. Unlike simple regex-based PII detection, this model understands **context and intent**:

- "my number is 05321234567" → **PII** (sharing intent)
- "05321234567 is a scammer, block them" → **NOT PII** (scam warning)
- "I'll send you my WhatsApp tomorrow" → **PII** (future sharing intent)
- "what is an IBAN and how do I get one?" → **NOT PII** (information question)
- "numaram pizza siparişi gibi 05321234567 haha 😂" → **PII** (humor + real number)
- "oda numaram 532 otelde buluşalım" → **NOT PII** (room number, not phone)

### Key Features

- **Trilingual**: Turkish, Arabic, English
- **Context-aware**: Understands sarcasm, negation, hypotheticals, quoting, reporting, humor
- **Evasion-resistant**: Detects coded sharing, profile redirects, voice note evasion, partial number sharing, spaced text evasion
- **High recall**: 97% PII recall across 177 stress test cases
- **Conversation-ready**: 97% accuracy on 864 real-world conversation scenarios

## Training

- **Base model**: `xlm-roberta-large` (550M parameters)
- **Dataset**: [gorkem371/pii-intent-detection-multilingual](https://huggingface.co/datasets/gorkem371/pii-intent-detection-multilingual) - 41,427 samples across 9 entity types, balanced PII/NOT-PII
- **Loss**: Focal loss (gamma=2) with inverse class frequency weights
- **Training**: bf16 mixed precision, lr=1.5e-5, gradient accumulation=4 (effective batch=64), 15 epochs
- **Hardware**: NVIDIA H100 80GB HBM3
- **Best epoch**: 14

### Validation Metrics (epoch 14)

| Metric | Score |
|--------|-------|
| F1 | 99.33% |
| Accuracy | 99.24% |
| Precision | 99.20% |
| Recall | 99.46% |

## Test Results

### Stress Test (177 cases)

| Test Suite | Score | Description |
|------------|-------|-------------|
| Standard (72) | **97%** | Basic PII sharing and non-PII scenarios |
| Hardcore (72) | **92%** | Evasion, coded sharing, sarcasm, context tricks |
| Edge Cases (33) | **97%** | Business numbers, sarcasm+real numbers, hypotheticals |
| **Total (177)** | **95%** | Combined across all suites |

### Conversation Test (864 cases)

| Metric | Score |
|--------|-------|
| Total Accuracy | **838/864 (97.0%)** |
| Errors | 26 |
| False Positives | 2 |
| False Negatives | 24 |
| Design Limit (entity=NONE) | 19 of 24 FN |
| Actual Model Errors | 5 |

### Per-Language Breakdown (Stress Test)

| Language | Score | Notes |
|----------|-------|-------|
| Turkish | 96% | Weak: masked numbers, order numbers |
| Arabic | 96% | Weak: scam warnings, math expressions |
| English | 100% | All standard+hardcore+edge passed |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = "gorkem371/pii-intent-classifier-xlmr-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def classify_pii(context: str, entity: str, entity_type: str) -> dict:
    """
    Classify whether a message contains PII sharing intent.

    Args:
        context: The full message text
        entity: The specific entity to classify (e.g., phone number, "NONE" if implicit)
        entity_type: Type of entity (PHONE, EMAIL, SOCIAL_MEDIA, IBAN, ADDRESS, URL, etc.)

    Returns:
        dict with 'is_pii' (bool) and 'confidence' (float)
    """
    text = f"{context} </s> {entity} | {entity_type}"
    inputs = tokenizer(text, max_length=256, padding="max_length", truncation=True, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred = torch.argmax(probs, dim=-1).item()
        confidence = probs[0][pred].item()

    return {
        "is_pii": pred == 1,
        "label": "PII" if pred == 1 else "NOT_PII",
        "confidence": round(confidence, 4)
    }

# Examples
print(classify_pii("my number is 05321234567 call me", "05321234567", "PHONE"))
# {'is_pii': True, 'label': 'PII', 'confidence': 0.9987}

print(classify_pii("order number is ORD-784321", "ORD-784321", "PHONE"))
# {'is_pii': False, 'label': 'NOT_PII', 'confidence': 0.9954}

print(classify_pii("i will send you my whatsapp tomorrow", "NONE", "PHONE"))
# {'is_pii': True, 'label': 'PII', 'confidence': 0.9821}

print(classify_pii("oda numaram 532 otelde buluşalım", "NONE", "PHONE"))
# {'is_pii': False, 'label': 'NOT_PII', 'confidence': 0.9876}
```

## Input Format

The model expects input in the following format:

```
{context} </s> {entity} | {entity_type}
```

- **context**: The full message text (any language)
- **entity**: The specific entity string, or `"NONE"` for implicit PII intent
- **entity_type**: One of: `PHONE`, `EMAIL`, `SOCIAL_MEDIA`, `IBAN`, `CREDIT_CARD`, `ADDRESS`, `URL`, `CRYPTO_ADDRESS`, `OFF_PLATFORM_ATTEMPT`

## Supported Entity Types

| Type | Description | Example |
|------|-------------|---------|
| PHONE | Phone numbers | 05321234567, +966501234567 |
| EMAIL | Email addresses | user@gmail.com |
| SOCIAL_MEDIA | Social media handles | @username, Instagram/TikTok/Telegram |
| IBAN | Bank account numbers | TR33000610... |
| ADDRESS | Physical addresses | 123 Oxford Street London |
| URL | Websites | my-site.com |
| CREDIT_CARD | Credit card numbers | 4532... |
| CRYPTO_ADDRESS | Cryptocurrency addresses | 0x... |
| OFF_PLATFORM_ATTEMPT | Attempts to move off-platform | "let's talk on WhatsApp" |

## What This Model Understands

### PII = True (sharing intent detected)
- Direct sharing: "my number is 05321234567"
- Coded/evasion: "find me on the gram @secret_handle"
- Future intent: "I'll send you my number tomorrow"
- Conditional: "if we agree, I'll share my contact"
- Requesting: "what's your number? send it"
- Profile redirect: "check my bio, my number is there"
- Reluctant sharing: "I don't want to but here's my number..."
- Third-party: "my friend said to contact him at..."
- Humor + real number: "numaram pizza siparişi gibi 05321234567 haha 😂"
- Scam warning + real number: "05321234567 dolandırıcı sakın aramayın" (number is still visible)
- Business/restaurant numbers: "restoran telefonu 02125551234"
- Asking about a number: "bu numara tanıdık mı 05321234567"

### PII = False (no sharing intent)
- Order/tracking numbers: "your order ORD-784321"
- Scam warnings (no real number): "dolandırıcılara dikkat edin"
- Reporting violations: "someone sent me their number, reporting"
- Hypothetical (no number): "I wish I had a number to share"
- Sarcasm with fake numbers: "my number is 00000000000 lol"
- Statistics: "my follower count hit 532000"
- Non-contact numbers: "bake at 180 degrees for 45 minutes"
- Price/product codes: "SKU-TR-78431-B", "1250 TL"
- Room numbers: "oda numaram 532 otelde buluşalım"
- Postal codes: "posta kodu 34720 Kadıköy İstanbul"
- Time digits: "saat 05:32 de buluşalım"
- Tracking numbers: "kargo takip: 1Z999AA10123456784"

## Limitations

- **Masked numbers** (0532***4567): Model classifies as NOT-PII (partially masked = not fully usable)
- **Scam warnings with real numbers**: V11 tends to flag these as PII (the number is still visible/reachable)
- **Math expressions** containing phone-like numbers: Sometimes flagged as PII
- **Entity extraction dependency**: 19 of 26 conversation errors are from entity extraction returning NONE, not model failures

## Model Architecture

- **Base**: XLM-RoBERTa Large (24 layers, 16 heads, 1024 hidden, 550M params)
- **Head**: Linear(1024→1024) + Tanh + Dropout + Linear(1024→2)
- **Total size**: ~2.1GB (safetensors)

## Citation

**Author**: [Gorkem Yildiz](https://gorkemyildiz.com)

If you use this model, please cite:

```bibtex
@misc{pii-intent-classifier-2026,
  title={PII Intent Classifier: Multilingual Context-Aware PII Detection},
  author={Gorkem Yildiz},
  year={2026},
  url={https://huggingface.co/gorkem371/pii-intent-classifier-xlmr-large},
  howpublished={\url{https://gorkemyildiz.com}}
}
```
