---
license: apache-2.0
base_model: google/vit-base-patch16-224-in21k
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: dental_classification_model_010424
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dental_classification_model_010424

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5797
- Accuracy: 0.8354

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.8845        | 0.99  | 40   | 1.8553          | 0.3106   |
| 1.6458        | 1.99  | 80   | 1.6211          | 0.4363   |
| 1.4423        | 2.98  | 120  | 1.4076          | 0.5202   |
| 1.2767        | 4.0   | 161  | 1.2806          | 0.5714   |
| 1.0687        | 4.99  | 201  | 1.0996          | 0.6537   |
| 0.9687        | 5.99  | 241  | 1.0288          | 0.6677   |
| 0.8714        | 6.98  | 281  | 0.9370          | 0.7252   |
| 0.7841        | 8.0   | 322  | 0.8287          | 0.7484   |
| 0.6814        | 8.99  | 362  | 0.8141          | 0.7376   |
| 0.5964        | 9.99  | 402  | 0.7433          | 0.7919   |
| 0.5995        | 10.98 | 442  | 0.7075          | 0.7904   |
| 0.5222        | 12.0  | 483  | 0.6613          | 0.8043   |
| 0.5173        | 12.99 | 523  | 0.6485          | 0.8090   |
| 0.4776        | 13.99 | 563  | 0.6196          | 0.8230   |
| 0.4679        | 14.98 | 603  | 0.5795          | 0.8416   |
| 0.4123        | 16.0  | 644  | 0.6202          | 0.8168   |
| 0.4179        | 16.99 | 684  | 0.6037          | 0.8230   |
| 0.4139        | 17.99 | 724  | 0.5797          | 0.8354   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
