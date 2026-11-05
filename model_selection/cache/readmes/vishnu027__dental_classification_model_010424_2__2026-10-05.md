---
license: apache-2.0
base_model: google/vit-base-patch16-224-in21k
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: dental_classification_model_010424_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dental_classification_model_010424_2

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5837
- Accuracy: 0.8142

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.9273        | 0.99  | 41   | 1.9166          | 0.2281   |
| 1.8096        | 2.0   | 83   | 1.7653          | 0.3716   |
| 1.6373        | 2.99  | 124  | 1.5785          | 0.4486   |
| 1.4996        | 4.0   | 166  | 1.4273          | 0.5060   |
| 1.3441        | 4.99  | 207  | 1.2730          | 0.5891   |
| 1.1677        | 6.0   | 249  | 1.1615          | 0.6254   |
| 0.9809        | 6.99  | 290  | 1.1033          | 0.6254   |
| 0.8292        | 8.0   | 332  | 0.9928          | 0.6873   |
| 0.8035        | 8.99  | 373  | 0.8762          | 0.7402   |
| 0.6982        | 10.0  | 415  | 0.8117          | 0.7341   |
| 0.6992        | 10.99 | 456  | 0.7667          | 0.7749   |
| 0.5601        | 12.0  | 498  | 0.7563          | 0.7568   |
| 0.5358        | 12.99 | 539  | 0.7178          | 0.7749   |
| 0.569         | 14.0  | 581  | 0.7356          | 0.7553   |
| 0.4503        | 14.99 | 622  | 0.6535          | 0.8051   |
| 0.4509        | 16.0  | 664  | 0.6755          | 0.7855   |
| 0.5127        | 16.99 | 705  | 0.6431          | 0.7976   |
| 0.425         | 18.0  | 747  | 0.6362          | 0.8006   |
| 0.3968        | 18.99 | 788  | 0.5821          | 0.8157   |
| 0.398         | 20.0  | 830  | 0.6355          | 0.7900   |
| 0.4468        | 20.99 | 871  | 0.5103          | 0.8323   |
| 0.429         | 22.0  | 913  | 0.6056          | 0.8051   |
| 0.3332        | 22.99 | 954  | 0.5681          | 0.8233   |
| 0.3431        | 24.0  | 996  | 0.5186          | 0.8263   |
| 0.3052        | 24.99 | 1037 | 0.5993          | 0.8036   |
| 0.3495        | 26.0  | 1079 | 0.5837          | 0.8142   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
