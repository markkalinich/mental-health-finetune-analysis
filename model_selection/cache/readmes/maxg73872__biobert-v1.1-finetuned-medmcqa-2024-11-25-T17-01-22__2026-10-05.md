---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: biobert-v1.1-finetuned-medmcqa-2024-11-25-T17-01-22
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-v1.1-finetuned-medmcqa-2024-11-25-T17-01-22

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1793
- Accuracy: 0.5374
- F1: 0.5383

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
| 1.3839        | 0.9739 | 14   | 1.1338          | 0.5109   | 0.5122 |
| 1.0754        | 1.9478 | 28   | 1.1150          | 0.5204   | 0.5224 |
| 0.6423        | 2.9913 | 43   | 1.0494          | 0.5300   | 0.5305 |
| 0.478         | 3.9652 | 57   | 1.1793          | 0.5374   | 0.5383 |
| 0.245         | 4.9391 | 71   | 1.4143          | 0.5372   | 0.5381 |
| 0.1731        | 5.9826 | 86   | 1.7302          | 0.5317   | 0.5329 |
| 0.1229        | 6.9565 | 100  | 1.8354          | 0.5326   | 0.5337 |
| 0.0833        | 8.0    | 115  | 1.9010          | 0.5288   | 0.5299 |
| 0.0735        | 8.9739 | 129  | 2.1489          | 0.5305   | 0.5314 |
| 0.0647        | 9.7391 | 140  | 2.0799          | 0.5357   | 0.5368 |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
