---
tags:
- model_hub_mixin
- pytorch_model_hub_mixin
datasets: mattmdjaga/text-anonymization-benchmark-train
license: apache-2.0
base_model: allenai/longformer-base-4096
base_model_relation: finetune
model_id: pii-classifier-tab-dataset
---

# Model Card for pii-classifier-tab-dataset

Model is a Longformer with a classification head, finetuned on **Text Anonymization Benchmark (TAB)** dataset for indicating if a token is part of a **Personal Identifiable Information (PII)** and should be masked out or not. Model output is the logits of the input sequence, where the classes are 1 (MASK) or 0 (NO-MASK), e.g. no IOB format used.

Model is used as an example in [LeakPro repo](https://github.com/aidotse/LeakPro). For further detail, see example [notebook](https://github.com/aidotse/LeakPro/blob/main/examples/synthetic_data/syn_text_pii_scanner_example.ipynb).