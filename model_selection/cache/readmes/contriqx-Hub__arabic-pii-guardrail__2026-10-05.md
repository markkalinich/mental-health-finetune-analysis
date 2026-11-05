---
library_name: transformers
tags:
- pii
- pii-detection
- intent-classification
- content-moderation
- arabic-nlp
- multilingual
license: apache-2.0
language:
- ar
- en
metrics:
- accuracy
- f1
base_model:
- FacebookAI/xlm-roberta-large
pipeline_tag: text-classification
---


# PII Intent Classifier — Arabic & English

A fine-tuned **XLM-RoBERTa-large** model that detects **intent to share personally identifiable information (PII)**, not just its presence. Built with a focus on Arabic (Gulf dialect + MSA) and English, with support for code-switched and Arabizi text.

> The model answers: *is this person sharing, requesting, or exposing PII?* — not simply *does this text contain a recognizable PII pattern?*

---

## Supported Entity Types

| Entity Type | Description | Example |
|---|---|---|
| `PHONE` | Phone numbers | `05321234567`, `+966501234567` |
| `EMAIL` | Email addresses | `user@gmail.com` |
| `SOCIAL_MEDIA` | Social media handles | `@username`, Instagram, TikTok, Telegram |
| `IBAN` | Bank account numbers | `SA44 2000 0001 2345 6789 1234` |
| `ADDRESS` | Physical addresses | `45 Tahrir St, Cairo` |
| `URL` | Personal websites / profiles | `mysite.com` |
| `CREDIT_CARD` | Credit card numbers | `4532 **** **** 1234` |
| `CRYPTO_ADDRESS` | Cryptocurrency wallet addresses | `0x71C7656EC7ab88b098defB751B7401B5f6d8976F` |
| `OFF_PLATFORM_ATTEMPT` | Attempts to move contact off-platform | `"let's talk on WhatsApp"` |
| `NAME` | Full personal names | `محمد العنزي`, `Sarah Khaled` |

---

## What the Model Understands

### PII = True (sharing intent detected)
- **Direct sharing:** `"رقمي 0532..."` / `"my number is 0532..."`
- **Third-party referral:** `"تكلم مع خالد الشمري، رقمه..."` / `"ask for Ahmed, call him at..."`
- **Coded / evasion patterns:** `"find me on the gram @handle"`, spaced digits `"0 5 3 2..."`, Arabizi names
- **Future intent:** `"I'll send you my number tomorrow"`
- **Conditional:** `"if we agree I'll share my address"`
- **Reluctant sharing:** `"ما أبي بس رقمي هو..."` / `"I don't want to but here's my number"`
- **Requesting:** `"وش رقمك؟"` / `"what's your number?"`
- **Honorific + full name in referral:** `"راجع الدكتور محمد العنزي"` / `"speak to Dr. Mariam Abdullah"`

### PII = False (no sharing intent)
- Order / tracking numbers: `"your order ORD-784321"`
- Scam warnings with no real data: `"احذر من محتالين يتصلون بأرقام مجهولة"`
- Celebrity / public figure names: `"Elon Musk announced..."`, `"صرّح محمد بن سلمان بأن..."`
- Statistics and prices: `"follower count hit 532,000"`, `"1250 SAR"`
- Non-contact numbers: room numbers, postal codes, temperatures, time
- Reporting a violation: `"someone sent me their number, I'm reporting it"`
- Hypothetical / sarcastic: `"my number is 00000000000 lol"`

---

## Arabic Language Support

Arabic is the primary focus of this model. It handles the full spectrum of how Arabic speakers actually write online — not just formal text.

**Dialects covered**
- Gulf Arabic (خليجي) — including markers like `والله`, `بس`, `خيي`, `صاحبي`, `يو`, `ابعتلي`
- Modern Standard Arabic (فصحى) — `اسمي`, `تواصل مع`, `يُعرف بـ`, `يُدعى`

**Script variations**
- Native Arabic script
- Arabizi (Latin + numbers): `A7med`, `F6oum`, `7amada`, `Kh@led`
- Code-switched sentences: Arabic sentence with English PII value or vice versa

**Arabic-specific intent signals the model recognizes**

| Signal | Example |
|---|---|
| First-person name intro | `"اسمي محمد العنزي"` / `"أنا خالد عبدالله"` |
| Possessive third-party | `"صاحبي / خيي [name] قال تتواصل معه"` |
| Honorific + full name | `"تكلم مع الدكتور سامي العمر"` |
| Contact redirect | `"تواصل معي"` / `"راسلني"` / `"ابعتلي رسالة"` |
| Platform redirect | `"على الإنستا / على السناب / في البايو"` |
| Reluctant sharing | `"ما أبي بس رقمي هو..."` |
| Scam warning with real number | `"احذر من هذا الرقم 0501234567"` → PII = True |
| Scam warning without number | `"احذر من محتالين يتصلون"` → PII = False |

---
## Usage

> **Note:** This model is designed for the second stage of a two-stage pipeline.
> An upstream system (regex, NER, or a rules engine) first extracts candidate
> entities from the text. This model then classifies whether the intent behind
> each extracted entity is PII sharing. The `entity` and `entity_type` arguments
> must be provided by the upstream stage. Use `entity="NONE"` when the sharing
> intent is implicit and no specific entity string is present in the text
> (e.g. *"I'll send you my details later"*).

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

model_name = ""
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def classify_pii(context: str, entity: str, entity_type: str) -> dict:
    """
    Args:
        context:     Full message text
        entity:      The specific entity string (use "NONE" if implicit)
        entity_type: One of PHONE | EMAIL | SOCIAL_MEDIA | IBAN | ADDRESS |
                     URL | CREDIT_CARD | CRYPTO_ADDRESS | OFF_PLATFORM_ATTEMPT | NAME

    Returns:
        dict with is_pii (bool), label (str), confidence (float)
    """
    text = f"{context} </s> {entity} | {entity_type}"
    inputs = tokenizer(
        text,
        max_length=256,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        pred = torch.argmax(probs, dim=-1).item()
        confidence = probs[0][pred].item()

    return {
        "is_pii":      pred == 1,
        "label":       "PII" if pred == 1 else "NOT_PII",
        "confidence":  round(confidence, 4)
    }
```

### Examples

```python
# True cases
# NONE entity — implicit sharing intent, no entity string present
classify_pii("I'll send you my details later, just DM me", "NONE", "PHONE")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.9134}

# When you know the entity type context (more reliable)
classify_pii("سأبعثلك رقمي بكرة", "NONE", "PHONE")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.8287}

# When entity type is also unknown (use with caution — out of training distribution)
classify_pii("سأبعثلك رقمي بكرة", "NONE", "NONE")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.7803}

classify_pii("check my bio, everything is there", "NONE", "SOCIAL_MEDIA")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.9056}

# NONE entity — vague mention, no actual sharing intent
classify_pii("I wish I had someone's number to call right now", "NONE", "PHONE")
# → {'is_pii': False, 'label': 'NOT_PII', 'confidence': 0.8821}

classify_pii("اسمي محمد العنزي وأبي أتواصل معاك", "محمد العنزي", "NAME")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.9814}

classify_pii("my number is 0532 1234567, call me anytime", "0532 1234567", "PHONE")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.9923}

classify_pii("find me on the gram @secret_handle", "@secret_handle", "SOCIAL_MEDIA")
# → {'is_pii': True, 'label': 'PII', 'confidence': 0.9761}

# False cases
classify_pii("your order ORD-784321 has been shipped", "ORD-784321", "PHONE")
# → {'is_pii': False, 'label': 'NOT_PII', 'confidence': 0.9502}

classify_pii("Elon Musk announced new features today", "Elon Musk", "NAME")
# → {'is_pii': False, 'label': 'NOT_PII', 'confidence': 0.9388}
```

---

## Training Details

### Base Model
[`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large) — 550M parameters, multilingual transformer.

### Dataset
- **41,427 samples** across 9 original entity types — balanced PII / NOT-PII
- **+2,500 samples** added for `NAME` entity type (Arabic Gulf + MSA + English + Mixed)
- Languages: Arabic (Gulf dialect + MSA), English, code-switched, Arabizi

### Training Configuration

| Parameter | Value |
|---|---|
| Loss function | Focal Loss (γ=2, inverse class frequency weights) |
| Learning rate | `1.5e-5` |
| Batch size | 64 (effective, with gradient accumulation) |
| Epochs | 15 |
| Precision | bf16 mixed precision |
| Max sequence length | 256 |

### Input Format
The model expects a specific input format that combines context, entity, and entity type:
```
{context} </s> {entity} | {entity_type}
```

---

## Evaluation

Evaluated on a curated benchmark of **2,094 samples** across 14 slices covering core capability, adversarial cases, regression tests, and cross-entity confusion.

### Overall

| Metric | Score |
|---|---|
| Macro F1 | 0.865 |
| Accuracy | 0.866 |
| AUC-ROC | 0.951 |
| FNR (miss rate) | 3.1% |
| FPR (false alarm rate) | 28.8% |

### Per Entity Type

| Entity Type | F1 |
|---|---|
| `NAME` | 0.918 |
| `OFF_PLATFORM_ATTEMPT` | 0.886 |
| `PHONE` | 0.845 |
| `IBAN` | 0.860 |
| `CREDIT_CARD` | 0.852 |
| `URL` | 0.827 |
| `SOCIAL_MEDIA` | 0.820 |
| `EMAIL` | 0.767 |
| `ADDRESS` | 0.710 |

### Per Language

| Language | F1 |
|---|---|
| Arabic | 0.847 |
| English | 0.844 |
| Mixed / Code-switched | 0.782 |

### Notable Benchmark Slices

| Slice | F1 | Note |
|---|---|---|
| `names_core` | 0.970 | Name intent detection |
| `phone_regression` | 0.938 | Phone detection unchanged |
| `evasion_coded` | 1.000 | Obfuscated / coded PII |
| `false_negative_traps` | 1.000 | Subtle sharing intent |
| `false_positive_traps` | 0.415 | Known limitation — see below |
| `context_flip_pairs` | 0.637 | Same entity, context flips label |

---

## Limitations

**The model currently leans toward false positives.** With an overall FPR of 28.8%, it occasionally flags non-PII content as PII — particularly when a recognizable entity (phone number, email, name) appears in a clearly non-sharing context (news mentions, statistics, celebrity references). This is a precision-recall tradeoff: the model is tuned to almost never miss a genuine PII sharing event (FNR = 3.1%), at the cost of some over-triggering.

Specific known gaps:

- **Cross-lingual content** — Mixed-language messages have an elevated FPR (50.8%). Code-switched text is sometimes treated as suspicious regardless of intent.
- **Context-flip accuracy** — Only 25% of minimal context-flip pairs (same entity, different context) are classified correctly in both directions.

These limitations will be addressed in the next release through targeted hard-negative training data and threshold calibration.

---

## Intended Use

- Content moderation systems that need to detect PII leakage in user-generated content
- Automated flagging of PII in Arabic and English social media, chat, and forum data
- Privacy compliance pipelines requiring intent-aware (not just pattern-based) PII detection

## Out-of-Scope Use

- Standalone PII redaction without human review (given the current FPR)
- Languages other than Arabic and English
- Document-level or structured data PII extraction (the model is designed for conversational, short-form text)