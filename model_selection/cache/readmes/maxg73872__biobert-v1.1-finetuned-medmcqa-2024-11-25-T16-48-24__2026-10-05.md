---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: biobert-v1.1-finetuned-medmcqa-2024-11-25-T16-48-24
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-v1.1-finetuned-medmcqa-2024-11-25-T16-48-24

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7763
- Accuracy: 0.8095
- F1: 0.8138

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:------:|
| 1.3838        | 0.9739 | 14   | 1.0207          | 0.6905   | 0.6764 |
| 1.086         | 1.9478 | 28   | 0.9525          | 0.6190   | 0.6189 |
| 0.6655        | 2.9913 | 43   | 0.7763          | 0.8095   | 0.8138 |
| 0.5349        | 3.9652 | 57   | 0.8631          | 0.7381   | 0.7368 |
| 0.3138        | 4.8696 | 70   | 0.8401          | 0.7857   | 0.7854 |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
