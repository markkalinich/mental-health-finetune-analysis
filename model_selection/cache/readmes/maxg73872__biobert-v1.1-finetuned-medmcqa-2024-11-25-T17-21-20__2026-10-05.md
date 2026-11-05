---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: biobert-v1.1-finetuned-medmcqa-2024-11-25-T17-21-20
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-v1.1-finetuned-medmcqa-2024-11-25-T17-21-20

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2111
- Accuracy: 0.5742
- F1: 0.5753

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
| 0.7483        | 0.9939 | 142  | 0.9367          | 0.5613   | 0.5628 |
| 0.6026        | 1.9921 | 284  | 0.9227          | 0.5685   | 0.5693 |
| 0.3491        | 2.9904 | 426  | 1.2111          | 0.5742   | 0.5753 |
| 0.2135        | 3.9956 | 569  | 1.5260          | 0.5697   | 0.5704 |
| 0.114         | 4.9869 | 710  | 1.9557          | 0.5666   | 0.5672 |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
