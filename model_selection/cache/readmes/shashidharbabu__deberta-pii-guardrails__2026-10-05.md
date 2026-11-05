---
language: en
license: mit
base_model: roberta-base
pipeline_tag: token-classification
tags:
  - pii-detection
  - named-entity-recognition
  - guardrails
  - safety
  - roberta
  - token-classification
  - privacy
datasets:
  - ai4privacy/pii-masking-200k
metrics:
  - f1
  - recall
  - precision
model-index:
  - name: roberta-base-pii-guardrails
    results:
      - task:
          type: token-classification
          name: PII Named Entity Recognition
        dataset:
          name: ai4privacy/pii-masking-200k (English, held-out test set)
          type: ai4privacy/pii-masking-200k
        metrics:
          - type: f1
            value: 0.9796
            name: PII F1 (binary)
          - type: recall
            value: 0.9821
            name: PII Recall
          - type: precision
            value: 0.9771
            name: PII Precision
          - type: f1
            value: 0.9377
            name: F1 Micro (entity-level)
---

# roberta-base-pii-guardrails

A finetuned **RoBERTa-base** model for Personally Identifiable Information (PII) detection via Named Entity Recognition (NER), trained as part of a multi-layer enterprise AI guardrails system. The model identifies and classifies 57 types of PII entities in text using BIO tagging.

## Model Description

This model is the PII detection component of a defense-in-depth guardrails gateway designed to prevent sensitive data exfiltration through LLM deployments. It operates alongside a jailbreak classifier and a prompt injection detector to form a multi-signal security layer.

| Property | Value |
|---|---|
| Base model | `roberta-base` (125M params) |
| Task | Token classification (BIO NER) |
| Entity types | 57 PII categories |
| Max input length | 256 tokens |
| Training framework | PyTorch + HuggingFace Transformers |

## Training Data

Trained on the English subset of [ai4privacy/pii-masking-200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) — a large, diverse dataset of synthetic text with fine-grained PII annotations across 57 entity types.

**Dataset split (English only):**
| Split | Examples |
|---|---|
| Train | ~34,800 |
| Validation | ~4,350 |
| Test | ~4,351 |

## Training Details

```
Optimizer:          AdamW
Learning rate:      3e-5
Epochs:             5 (best checkpoint: epoch 4)
Batch size:         16
Warmup ratio:       0.1
Weight decay:       0.01
Grad clipping:      1.0
Max seq length:     256
Label alignment:    First subword only (-100 for subsequent subwords)
Padding:            Dynamic (DataCollatorForTokenClassification)
```

## Evaluation Results

### Overall Metrics (Test Set)

| Metric | Value |
|---|---|
| **PII Recall** | **98.21%** ← most critical for security |
| PII F1 | 97.96% |
| PII Precision | 97.71% |
| F1 Micro (entity-level) | 93.77% |
| Loss | 0.0876 |

### Training Curve

| Epoch | Train Loss | Val F1 Micro | PII Recall |
|---|---|---|---|
| 1 | 0.5546 | 0.8905 | 97.12% |
| 2 | 0.0980 | 0.9252 | 97.72% |
| 3 | 0.0784 | 0.9291 | 98.00% |
| **4** | **0.0672** | **0.9380** | **98.07%** |
| 5 | 0.0565 | 0.9355 | 98.03% |

### Per-Entity-Type F1 (Test Set)

| Entity | F1 | Entity | F1 |
|---|---|---|---|
| NEARBYGPSCOORDINATE | 1.000 | CREDITCARDISSUER | 0.975 |
| SEX | 0.998 | CITY | 0.974 |
| EMAIL | 0.993 | VEHICLEVIN | 0.974 |
| ORDINALDIRECTION | 0.993 | FIRSTNAME | 0.973 |
| URL | 0.991 | JOBTYPE | 0.968 |
| ACCOUNTNAME | 0.990 | LASTNAME | 0.967 |
| MAC | 0.990 | HEIGHT | 0.965 |
| VEHICLEVRM | 0.990 | BIC | 0.961 |
| USERNAME | 0.990 | STREET | 0.959 |
| IBAN | 0.989 | MIDDLENAME | 0.949 |
| GENDER | 0.989 | ACCOUNTNUMBER | 0.948 |
| USERAGENT | 0.989 | BITCOINADDRESS | 0.946 |
| SSN | 0.988 | CURRENCYSYMBOL | 0.945 |
| ETHEREUMADDRESS | 0.987 | EYECOLOR | 0.945 |
| PHONENUMBER | 0.985 | AMOUNT | 0.944 |
| PHONEIMEI | 0.984 | PIN | 0.939 |
| PASSWORD | 0.982 | CREDITCARDCVV | 0.930 |
| COMPANYNAME | 0.982 | PREFIX | 0.929 |
| SECONDARYADDRESS | 0.981 | BUILDINGNUMBER | 0.918 |
| JOBAREA | 0.980 | ZIPCODE | 0.905 |
| COUNTY | 0.979 | CREDITCARDNUMBER | 0.901 |
| TIME | 0.979 | LITECOINADDRESS | 0.899 |
| JOBTITLE | 0.977 | AGE | 0.895 |
| STATE | 0.977 | DATE | 0.880 |
| CITY | 0.974 | CURRENCYCODE | 0.880 |
| — | — | IP / IPV4 / IPV6 | 0.81 / 0.15 |

**Harder entities:** IP addresses (F1=0.15–0.81), DOB (0.71), CURRENCYNAME (0.42), and MASKEDNUMBER (0.84) score lower due to high ambiguity — these formats appear frequently in non-PII contexts.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("shashidharbabu/roberta-base-pii-guardrails")
model     = AutoModelForTokenClassification.from_pretrained("shashidharbabu/roberta-base-pii-guardrails")
model.eval()

def detect_pii(text):
    words = text.split()
    enc   = tokenizer(
        words,
        is_split_into_words=True,
        return_tensors="pt",
        truncation=True,
        max_length=256,
    )
    with torch.no_grad():
        logits = model(**enc).logits
    preds    = logits.argmax(dim=-1)[0].tolist()
    word_ids = enc.word_ids(0)
    id2label = model.config.id2label

    results, prev_wid = [], None
    for wid, pred in zip(word_ids, preds):
        if wid is None or wid == prev_wid:
            prev_wid = wid
            continue
        label = id2label[pred]
        if label != "O":
            results.append({"word": words[wid], "entity": label})
        prev_wid = wid
    return results

# Example
text = "Hi, my name is John Smith and my email is john.smith@gmail.com"
print(detect_pii(text))
# → [
#     {'word': 'John',               'entity': 'B-FIRSTNAME'},
#     {'word': 'Smith',              'entity': 'B-LASTNAME'},
#     {'word': 'john.smith@gmail.com','entity': 'B-EMAIL'},
#   ]
```

## Supported Entity Types (57 total)

`ACCOUNTNAME` · `ACCOUNTNUMBER` · `AGE` · `AMOUNT` · `BIC` · `BITCOINADDRESS` · `BUILDINGNUMBER` · `CITY` · `COMPANYNAME` · `COUNTY` · `CREDITCARDCVV` · `CREDITCARDISSUER` · `CREDITCARDNUMBER` · `CURRENCY` · `CURRENCYCODE` · `CURRENCYNAME` · `CURRENCYSYMBOL` · `DATE` · `DOB` · `EMAIL` · `ETHEREUMADDRESS` · `EYECOLOR` · `FIRSTNAME` · `GENDER` · `HEIGHT` · `IBAN` · `IP` · `IPV4` · `IPV6` · `JOBAREA` · `JOBTITLE` · `JOBTYPE` · `LASTNAME` · `LITECOINADDRESS` · `MAC` · `MASKEDNUMBER` · `MIDDLENAME` · `NEARBYGPSCOORDINATE` · `ORDINALDIRECTION` · `PASSWORD` · `PHONEIMEI` · `PHONENUMBER` · `PIN` · `PREFIX` · `SECONDARYADDRESS` · `SEX` · `SSN` · `STATE` · `STREET` · `TIME` · `URL` · `USERAGENT` · `USERNAME` · `VEHICLEVIN` · `VEHICLEVRM` · `ZIPCODE`

## Limitations

- **English only:** Trained exclusively on English text. Performance on non-English inputs is untested and likely poor
- **IP address detection:** F1 of 0.15 for generic `IP` label — bare IP addresses are highly ambiguous and frequently appear in non-PII contexts
- **DOB / date ambiguity:** Date of birth (F1=0.71) is confused with general dates; context-free date strings are hard to classify
- **Credit card vs SSN confusion:** Long numeric sequences (e.g. credit card numbers in space-separated format) are sometimes misclassified as SSN
- **Synthetic training data:** Trained on synthetically generated text — performance may differ on real-world informal text styles
- **Max 256 tokens:** Long documents must be chunked; PII spanning chunk boundaries may be missed

## Intended Use

This model is designed as a **pre-filter and post-filter** in an LLM serving pipeline to:
- Detect PII in user inputs before they reach the base model
- Detect PII in model outputs before they are returned to the user
- Flag or redact sensitive information in enterprise AI deployments

**Not intended for:**
- Legal compliance decisions without human review
- Languages other than English
- Real-time systems requiring sub-millisecond latency without optimization

## Citation

```
@misc{guardrails2026,
  title  = {Multi-Layer LLM Security Gateway with Specialized Finetuned Models},
  author = {Shashidhar Babu et al.},
  year   = {2026},
  note   = {San Jose State University, Graduate Project}
}
```

## Project

This model is part of the **Guardrails Gateway** project at San Jose State University — a multi-layer LLM security system combining:
- 🔍 **PII Detection** (this model)
- 🛡️ **Jailbreak Detection** ([shashidharbabu/roberta-jailbreak-guardrails](https://huggingface.co/shashidharbabu/roberta-jailbreak-guardrails))
- 💉 **Prompt Injection Detection** (protectai/deberta-v3-base-prompt-injection-v2)

Tracked with [Weights & Biases](https://wandb.ai/shashidharbabu-pvd-san-jose-state-university/Guardrails).
