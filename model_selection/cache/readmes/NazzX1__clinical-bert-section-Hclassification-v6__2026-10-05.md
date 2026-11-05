---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: clinical-bert-section-Hclassification-v6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-bert-section-Hclassification-v6

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9591
- Accuracy: 0.8801
- Precision: 0.8830
- Recall: 0.8801
- F1: 0.8806

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
| No log        | 1.0   | 370  | 1.3239          | 0.2713   | 0.5686    | 0.2713 | 0.1492 |
| 1.3557        | 2.0   | 740  | 1.1959          | 0.7508   | 0.8241    | 0.7508 | 0.7339 |
| 1.2023        | 3.0   | 1110 | 1.0914          | 0.8738   | 0.8825    | 0.8738 | 0.8747 |
| 1.2023        | 4.0   | 1480 | 1.0174          | 0.8738   | 0.8795    | 0.8738 | 0.8741 |
| 1.071         | 5.0   | 1850 | 0.9738          | 0.8801   | 0.8834    | 0.8801 | 0.8804 |
| 0.9892        | 6.0   | 2220 | 0.9591          | 0.8801   | 0.8830    | 0.8801 | 0.8806 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Tokenizers 0.21.1
