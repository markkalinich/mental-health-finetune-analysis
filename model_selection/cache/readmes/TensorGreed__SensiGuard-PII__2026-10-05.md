---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: SensiGuard-PII
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SensiGuard-PII

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0067
- Precision: 0.6437
- Recall: 0.9659
- F1: 0.7726

## Model description

SensiGuard-PII is a token-classification model fine-tuned to detect common PII/PCI/PHI fields (e.g., names, emails, phone, SSN, card numbers, bank details, IPs, API keys). The base encoder is microsoft/deberta-v3-base trained on a mixture of synthetic, weak-labeled, and public PII datasets, using BIO tagging with class weighting to handle imbalance.
Sample Usage:
```
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_id = "your_namespace/SensiGuard-PII"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(model_id)

nlp = pipeline("token-classification", model=model, tokenizer=tok, aggregation_strategy="simple")
text = "My SSN is 123-45-6789 and my card is 4111 1111 1111 1111."
print(nlp(text))
# [{'entity_group': 'SSN', 'score': 0.99, 'word': '123-45-6789', 'start': 10, 'end': 21},
```

## Intended uses & limitations

### Intended Uses

- Ingress/egress scanning for applications or LLM systems to identify sensitive spans.
- Redaction or logging workflows where you need start/end offsets and label types.
- Semi-supervised bootstrapping: weak-label new corpora with this model and fine-tune further.

### Limitations

- Not a silver bullet: precision/recall can vary by domain, language (primarily English), and formatting.
- PCI: needs coverage for diverse card formats; pair with regex + Luhn validation and post-processing thresholds.
- May miss edge cases or yield false positives on lookalike numbers/strings; test on your own data.
- No safety/ethical filtering beyond PII detection; downstream policy is your responsibility.

## Training and evaluation data

- Sources: Mixed synthetic + public/weak-labeled PII corpora. Synthetic data was generated with pattern templates and optional LLM augmentation (vLLM/OpenAI-compatible) to cover names, emails, phones, SSN, PCI (card number/expiry/CVV/last4), bank account/routing, IPs, credentials, and healthcare identifiers. Public components include Nemotron-PII, AI4Privacy PII, Mendeley financial PII, and optional weak-labeling over Enron-style text. Labels were normalized into a common schema; unsupported labels were dropped.
- Splits: If no validation file is provided, the training JSONL is auto-split 90/10 (train/val) with train_test_split(test_size=0.1, seed=42).
- Class balancing: Inverse-frequency class weights were applied to mitigate the dominant O class.
- Notes: PCI coverage includes spaced/dashed card formats and expiries; regex/Luhn hard negatives were used to reduce false positives. Evaluation metrics are token-level precision/recall/F1 (seqeval) on the held-out validation split.
- Limitations: Mostly English; domain and format shifts may impact performance. Test on your own data and adjust thresholds/label mappings as needed.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| 0.0148        | 1.0   | 4650 | 0.0099          | 0.6266    | 0.9636 | 0.7594 |
| 0.0018        | 2.0   | 9300 | 0.0067          | 0.6437    | 0.9659 | 0.7726 |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.6.0+rocm6.1
- Datasets 4.4.1
- Tokenizers 0.22.1
