---
library_name: transformers
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
tags:
- transformers
- pytorch
- biomedical
- text-classification
license: apache-2.0
language:
- en
pipeline_tag: text-classification
---

# pubmedbert_setting_20250221

Fine-tuned model from the PsyNamic project.

## Base Model

`microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract`

## Task

Setting

## Training Parameters

```json
{
  "mode": "train",
  "data": "<private_dataset>",
  "task": "Setting",
  "model": "pubmedbert",
  "cross_val": false,
  "batch_size": 8,
  "learning_rate": 5e-05,
  "weight_decay": 0.01,
  "lr_scheduler": "linear",
  "warmup_ratio": 0.1,
  "epochs": 30,
  "dropout": 0.1,
  "early_stopping_patience": 5,
  "gradient_clipping": 0.1,
  "device": "cuda",
  "load": null,
  "max_length": 512,
  "is_multilabel": true
}
```