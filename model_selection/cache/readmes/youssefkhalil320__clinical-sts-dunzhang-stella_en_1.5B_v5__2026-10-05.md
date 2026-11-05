---
language: en
tags:
  - clinical-nlp
  - text-similarity
  - regression
  - bert
base_model: dunzhang/stella_en_1.5B_v5
---
 
# Clinical STS Regression Model
 
Fine-tuned from `dunzhang/stella_en_1.5B_v5` on a clinical text-pair similarity dataset.
 
## Training config
```json
{
  "train": "./med_sts/clinicalSTS.train.txt",
  "test": "./med_sts/clinicalSTS.test.txt",
  "model": [
    "dunzhang/stella_en_1.5B_v5"
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
  "output_dir": "./sts_val/clinical-sts-dunzhang-stella_en_1.5B_v5",
  "wandb_project": "clinical-sts",
  "hf_repo": "youssefkhalil320/clinical-sts-dunzhang-stella_en_1.5B_v5"
}
```
 
## Best test Spearman ρ: `0.2526`
