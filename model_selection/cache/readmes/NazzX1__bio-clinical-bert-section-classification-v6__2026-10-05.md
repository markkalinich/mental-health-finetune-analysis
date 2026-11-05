---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bio-clinical-bert-section-classification-v6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bio-clinical-bert-section-classification-v6

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1907
- Accuracy: 0.6562
- Precision: 0.6875
- Recall: 0.6562
- F1: 0.6605

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 370  | 1.3321          | 0.3722   | 0.3745    | 0.3722 | 0.3474 |
| 1.3812        | 2.0   | 740  | 1.2760          | 0.5331   | 0.5882    | 0.5331 | 0.5160 |
| 1.3012        | 3.0   | 1110 | 1.2377          | 0.6151   | 0.6802    | 0.6151 | 0.6203 |
| 1.3012        | 4.0   | 1480 | 1.2114          | 0.6593   | 0.7025    | 0.6593 | 0.6647 |
| 1.2549        | 5.0   | 1850 | 1.1960          | 0.6562   | 0.6996    | 0.6562 | 0.6618 |
| 1.2222        | 6.0   | 2220 | 1.1907          | 0.6562   | 0.6875    | 0.6562 | 0.6605 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Tokenizers 0.21.1
