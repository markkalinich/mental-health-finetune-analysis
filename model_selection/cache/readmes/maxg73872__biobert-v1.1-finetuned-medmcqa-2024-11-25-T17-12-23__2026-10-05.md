---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: biobert-v1.1-finetuned-medmcqa-2024-11-25-T17-12-23
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-v1.1-finetuned-medmcqa-2024-11-25-T17-12-23

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8219
- Accuracy: 0.7143
- F1: 0.7228

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000159
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:------:|
| 1.3834        | 0.9739 | 14   | 1.1666          | 0.5714   | 0.5553 |
| 1.0717        | 1.9478 | 28   | 0.9962          | 0.5952   | 0.5891 |
| 0.6143        | 2.9913 | 43   | 0.8219          | 0.7143   | 0.7228 |
| 0.4801        | 3.9652 | 57   | 0.8748          | 0.7143   | 0.7138 |
| 0.2112        | 4.9391 | 71   | 1.1275          | 0.6905   | 0.6878 |
| 0.1627        | 5.9826 | 86   | 1.2672          | 0.6905   | 0.6839 |
| 0.118         | 6.9565 | 100  | 1.4471          | 0.6429   | 0.6357 |
| 0.088         | 8.0    | 115  | 1.4548          | 0.7143   | 0.7149 |
| 0.0674        | 8.9739 | 129  | 1.4981          | 0.6905   | 0.6858 |
| 0.0715        | 9.7391 | 140  | 1.4867          | 0.7143   | 0.7126 |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
