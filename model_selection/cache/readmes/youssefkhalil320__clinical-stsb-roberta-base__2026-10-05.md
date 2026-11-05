---
language: en
tags:
  - clinical-nlp
  - text-similarity
  - regression
  - bert
base_model: cross-encoder/stsb-roberta-base
---
 
# Clinical STS Regression Model
 
Fine-tuned from `cross-encoder/stsb-roberta-base` on a clinical text-pair similarity dataset.
 
## Training config
```json
{
  "train": "./med_sts/clinicalSTS.train.txt",
  "test": "./med_sts/clinicalSTS.test.txt",
  "model": [
    "cross-encoder/stsb-roberta-base"
  ],
  "epochs": 20,
  "batch_size": 16,
  "lr": 2e-05,
  "weight_decay": 0.01,
  "warmup_ratio": 0.1,
  "max_grad_norm": 1.0,
  "dropout": 0.1,
  "max_len": 256,
  "seed": 42,
  "patience": 5,
  "output_dir": "./sts_val/clinical-stsb-roberta-base",
  "wandb_project": "clinical-sts",
  "hf_repo": "youssefkhalil320/clinical-stsb-roberta-base"
}
```
 
## Best test Spearman ρ: `0.8297`
