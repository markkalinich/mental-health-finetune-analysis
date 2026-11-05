---
library_name: transformers
license: mit
base_model: hbseong/HarmAug-Guard
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [hbseong/HarmAug-Guard](https://huggingface.co/hbseong/HarmAug-Guard) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1008
- Accuracy: 0.9667
- Precision: 0.9667
- Recall: 0.9667
- F1: 0.9667

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4652        | 0.9895 | 59   | 0.2876          | 0.9417   | 0.9445    | 0.9417 | 0.9414 |
| 0.003         | 1.9958 | 119  | 0.1736          | 0.9667   | 0.9689    | 0.9667 | 0.9667 |
| 0.0027        | 2.9853 | 178  | 0.2779          | 0.95     | 0.9519    | 0.95   | 0.9499 |
| 0.1023        | 3.9916 | 238  | 0.3743          | 0.9333   | 0.9408    | 0.9333 | 0.9328 |
| 0.0015        | 4.9979 | 298  | 0.3164          | 0.9417   | 0.9417    | 0.9417 | 0.9416 |
| 0.0003        | 5.9874 | 357  | 0.2952          | 0.9583   | 0.9614    | 0.9583 | 0.9582 |
| 0.0002        | 6.9937 | 417  | 0.2069          | 0.9417   | 0.9426    | 0.9417 | 0.9416 |
| 0.0001        | 8.0    | 477  | 0.1738          | 0.9583   | 0.9584    | 0.9583 | 0.9583 |
| 0.0001        | 8.9895 | 536  | 0.1008          | 0.9667   | 0.9667    | 0.9667 | 0.9667 |
| 0.0001        | 9.8952 | 590  | 0.1016          | 0.9667   | 0.9667    | 0.9667 | 0.9667 |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.0.2
- Tokenizers 0.19.1
