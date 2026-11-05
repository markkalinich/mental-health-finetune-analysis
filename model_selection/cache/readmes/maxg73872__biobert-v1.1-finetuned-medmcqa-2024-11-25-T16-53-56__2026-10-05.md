---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: biobert-v1.1-finetuned-medmcqa-2024-11-25-T16-53-56
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-v1.1-finetuned-medmcqa-2024-11-25-T16-53-56

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7742
- Accuracy: 0.7381
- F1: 0.7360

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
| 1.3837        | 0.9739 | 14   | 0.9841          | 0.6667   | 0.6554 |
| 1.0861        | 1.9478 | 28   | 0.9140          | 0.6190   | 0.6246 |
| 0.7803        | 2.9913 | 43   | 0.7742          | 0.7381   | 0.7360 |
| 0.5603        | 3.9652 | 57   | 0.8236          | 0.7143   | 0.7138 |
| 0.2753        | 4.9391 | 71   | 0.8765          | 0.7143   | 0.7110 |
| 0.1985        | 5.9826 | 86   | 0.9808          | 0.7381   | 0.7399 |
| 0.1119        | 6.9565 | 100  | 0.8757          | 0.7381   | 0.7312 |
| 0.0814        | 8.0    | 115  | 0.8388          | 0.7381   | 0.7519 |
| 0.0705        | 8.9739 | 129  | 1.0431          | 0.7381   | 0.7519 |
| 0.0658        | 9.7391 | 140  | 0.9075          | 0.7143   | 0.7220 |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
