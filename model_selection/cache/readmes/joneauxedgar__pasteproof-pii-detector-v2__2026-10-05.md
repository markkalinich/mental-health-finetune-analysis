---
library_name: transformers
license: bsl-1.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
- pii-detection
- security
- privacy
metrics:
- precision
- recall
- f1
model-index:
- name: pasteproof-pii-detector-v2
  results: []
datasets:
- joneauxedgar/pasteproof-pii-dataset-v3
inference: true
pipeline_tag: token-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PasteProof PII Detector v3

A fine-tuned [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base) model for detecting Personally Identifiable Information (PII) in text before it's accidentally leaked.

## Model Description

This model performs Named Entity Recognition (NER) to identify 27 types of sensitive information commonly found in code, configuration files, chat messages, and documents.

**Base model:** `answerdotai/ModernBERT-base`  
**Task:** Token Classification (NER)  
**Training data:** 150K synthetic examples with intentional variation to prevent overfitting  
**F1 Score:** 0.97 on held-out test set

### Detected Entity Types

| Category | Entities |
|----------|----------|
| **Financial (PCI-DSS)** | `CREDIT_CARD`, `PCI_PAN`, `PCI_TRACK`, `PCI_EXPIRY` |
| **Security Credentials** | `API_KEY`, `AWS_KEY`, `PRIVATE_KEY`, `PASSWORD` |
| **Healthcare (HIPAA)** | `HIPAA_MRN`, `HIPAA_ACCOUNT`, `HIPAA_DOB` |
| **European (GDPR)** | `GDPR_PASSPORT`, `GDPR_NIN`, `GDPR_IBAN` |
| **Identity** | `NAME`, `FIRST_NAME`, `LAST_NAME`, `SSN`, `DOB`, `DRIVER_LICENSE` |
| **Contact** | `EMAIL`, `PHONE`, `IP_ADDRESS` |
| **Address** | `STREET`, `CITY`, `STATE`, `ZIPCODE` |

### API Key Formats Detected

Stripe (`sk_live_`, `pk_test_`), OpenAI (`sk-`), Anthropic (`sk-ant-`), GitHub (`ghp_`, `github_pat_`), Slack (`xoxb-`), AWS (`AKIA...`), SendGrid (`SG.`), and generic patterns.

## Intended Uses

✅ **Primary use case:** Browser extension or IDE plugin that warns users before pasting sensitive data into web forms, chat apps, or public repositories.

✅ **Other valid uses:**
- Pre-commit hooks to scan for secrets
- Chat/support systems to redact PII before logging
- Document scanning for compliance (HIPAA, GDPR, PCI-DSS)
- Data pipeline filtering

## Limitations

⚠️ **Not a security guarantee.** This model is a helpful tool, not a replacement for proper secrets management.

⚠️ **False negatives are possible.** The model may miss:
- Obfuscated or encoded secrets
- PII in languages other than English
- Novel API key formats not in training data
- Context-dependent PII (e.g., a name that's only sensitive in certain contexts)

⚠️ **False positives may occur on:**
- UUIDs and transaction IDs that resemble API keys
- Test/example data that looks real
- Random strings in code

⚠️ **Known limitations:**
- Trained on synthetic data, may not perfectly match real-world distribution
- 512 token context limit (longer texts should be chunked)
- English-only training data

## How to Use
```python
from transformers import pipeline

detector = pipeline(
    "token-classification",
    model="joneauxedgar/pasteproof-pii-detector-v3",
    aggregation_strategy="simple"
)

text = '''const config = {
    apiKey: "sk_live_abc123def456",
    email: "john@company.com"
};'''

results = detector(text)
for entity in results:
    print(f"{entity['entity_group']}: {entity['word']} ({entity['score']:.1%})")
```

**Output:**
```
API_KEY: sk_live_abc123def456 (99.9%)
EMAIL: john@company.com (99.9%)
```

## Training Details

- **Dataset:** [joneauxedgar/pasteproof-pii-dataset-v3](https://huggingface.co/datasets/joneauxedgar/pasteproof-pii-dataset-v3)
- **Training examples:** 120,000
- **Validation examples:** 15,000
- **Epochs:** 3
- **Learning rate:** 5e-5
- **Batch size:** 32
- **Hardware:** NVIDIA A100

### Training Data Design

To prevent overfitting, the training data includes:
- **30% misleading key names** (e.g., `data`, `x`, `field1` instead of `apiKey`)
- **20% raw PII** without contextual clues
- **15% mixed real + fake data** (real PII alongside test cards, example.com emails)
- **15% hard negatives** (placeholder values, test data that should NOT be flagged)

## Evaluation Results

| Metric | Score |
|--------|-------|
| Precision | 0.968 |
| Recall | 0.976 |
| F1 | 0.972 |

The model correctly ignores:
- `user@example.com` (placeholder email)
- `4111111111111111` (test credit card)
- `123-45-6789` (example SSN)
- `process.env.API_KEY` (reference, not a value)
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Precision | Recall | F1     |
|:-------------:|:------:|:-----:|:---------------:|:---------:|:------:|:------:|
| 0.0079        | 0.2667 | 1000  | 0.0062          | 0.9194    | 0.9521 | 0.9354 |
| 0.006         | 0.5333 | 2000  | 0.0051          | 0.9318    | 0.9605 | 0.9459 |
| 0.0044        | 0.8    | 3000  | 0.0052          | 0.9516    | 0.9645 | 0.9580 |
| 0.0048        | 1.0667 | 4000  | 0.0048          | 0.9542    | 0.9698 | 0.9619 |
| 0.0036        | 1.3333 | 5000  | 0.0039          | 0.9626    | 0.9707 | 0.9666 |
| 0.0043        | 1.6    | 6000  | 0.0038          | 0.9559    | 0.9688 | 0.9623 |
| 0.0043        | 1.8667 | 7000  | 0.0035          | 0.9610    | 0.9724 | 0.9667 |
| 0.0027        | 2.1333 | 8000  | 0.0031          | 0.9627    | 0.9735 | 0.9681 |
| 0.0027        | 2.4    | 9000  | 0.0031          | 0.9651    | 0.9750 | 0.9700 |
| 0.0029        | 2.6667 | 10000 | 0.0036          | 0.9575    | 0.9742 | 0.9658 |
| 0.0027        | 2.9333 | 11000 | 0.0029          | 0.9681    | 0.9761 | 0.9721 |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1

## Citation
```bibtex
@model{pasteproof_pii_detector,
  author = {Jonathan Edgar},
  title = {PasteProof PII Detector},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/joneauxedgar/pasteproof-pii-detector-v3}
}
```

## Contact

Part of the [PasteProof](https://pasteproof.com) project - preventing accidental data leaks before they happen.


### License

BSL 1.0
Use for individual or research purposes. Reach out team@pasteproof.com for commercial license or usage questions.