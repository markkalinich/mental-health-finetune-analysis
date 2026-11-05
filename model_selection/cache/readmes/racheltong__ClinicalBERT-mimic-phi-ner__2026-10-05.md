---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: ClinicalBERT-mimic-phi-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-mimic-phi-ner

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0017
- F1 Macro: 0.9441
- F1 Weighted: 0.9441
- Precision: 0.9140
- Recall: 0.9763
- F1 Name: 0.94
- F1 Location: 0.91
- F1 Phone: 0.93
- F1 Date: 0.84
- F1 Mrn: 0.96
- F1 Account: 0.97
- F1 Age Over 89: 0.98
- F1 Device Id: 0.99
- F1 Ssn: 1.0
- F1 Url: 1.0
- F1 Email: 0.99

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | F1 Macro | F1 Weighted | Precision | Recall | F1 Name | F1 Location | F1 Phone | F1 Date | F1 Mrn | F1 Account | F1 Age Over 89 | F1 Device Id | F1 Ssn | F1 Url | F1 Email |
|:-------------:|:------:|:----:|:---------------:|:--------:|:-----------:|:---------:|:------:|:-------:|:-----------:|:--------:|:-------:|:------:|:----------:|:--------------:|:------------:|:------:|:------:|:--------:|
| 0.4470        | 0.1774 | 300  | 0.0868          | 0.3948   | 0.3948      | 0.2935    | 0.6032 | 0.46    | 0.33        | 0.41     | 0.04    | 0.46   | 0.4        | 0.08           | 0.58         | 0.32   | 0.0    | 0.31     |
| 0.0508        | 0.3547 | 600  | 0.0112          | 0.7449   | 0.7449      | 0.6654    | 0.8461 | 0.82    | 0.57        | 0.8      | 0.21    | 0.64   | 0.85       | 0.04           | 0.89         | 0.86   | 0.56   | 0.95     |
| 0.0302        | 0.5321 | 900  | 0.0131          | 0.8389   | 0.8389      | 0.7652    | 0.9284 | 0.88    | 0.72        | 0.86     | 0.27    | 0.59   | 0.98       | 0.84           | 0.9          | 0.92   | 0.93   | 0.99     |
| 0.0244        | 0.7094 | 1200 | 0.0046          | 0.8816   | 0.8816      | 0.8212    | 0.9517 | 0.9     | 0.81        | 0.81     | 0.48    | 0.75   | 0.97       | 0.95           | 0.97         | 0.98   | 1.0    | 1.0      |
| 0.0187        | 0.8868 | 1500 | 0.0030          | 0.9160   | 0.9160      | 0.8713    | 0.9656 | 0.93    | 0.82        | 0.87     | 0.52    | 0.89   | 0.95       | 0.96           | 0.96         | 1.0    | 1.0    | 1.0      |
| 0.0055        | 1.0638 | 1800 | 0.0030          | 0.9343   | 0.9343      | 0.8979    | 0.9737 | 0.94    | 0.89        | 0.9      | 0.57    | 0.92   | 0.97       | 0.98           | 0.99         | 1.0    | 1.0    | 1.0      |
| 0.0037        | 1.2412 | 2100 | 0.0027          | 0.9306   | 0.9306      | 0.8944    | 0.9697 | 0.93    | 0.89        | 0.9      | 0.74    | 0.92   | 0.98       | 0.98           | 0.99         | 1.0    | 1.0    | 1.0      |
| 0.0117        | 1.4186 | 2400 | 0.0025          | 0.9338   | 0.9338      | 0.8988    | 0.9716 | 0.94    | 0.88        | 0.89     | 0.8     | 0.94   | 0.97       | 0.98           | 0.99         | 1.0    | 1.0    | 0.99     |
| 0.0066        | 1.5959 | 2700 | 0.0020          | 0.9454   | 0.9454      | 0.9159    | 0.9769 | 0.95    | 0.9         | 0.93     | 0.83    | 0.96   | 0.98       | 0.99           | 0.99         | 1.0    | 1.0    | 0.99     |
| 0.0043        | 1.7733 | 3000 | 0.0018          | 0.9433   | 0.9433      | 0.9124    | 0.9763 | 0.94    | 0.9         | 0.93     | 0.82    | 0.96   | 0.97       | 0.99           | 0.99         | 1.0    | 1.0    | 0.99     |
| 0.0030        | 1.9506 | 3300 | 0.0017          | 0.9441   | 0.9441      | 0.9140    | 0.9763 | 0.94    | 0.91        | 0.93     | 0.84    | 0.96   | 0.97       | 0.98           | 0.99         | 1.0    | 1.0    | 0.99     |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
