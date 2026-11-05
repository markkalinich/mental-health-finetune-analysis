---
license: cc-by-nc-4.0
base_model: mental/mental-roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: mental_roberta_suicide
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_roberta_suicide

This model is a fine-tuned version of [mental/mental-roberta-base](https://huggingface.co/mental/mental-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5994
- Accuracy: 0.7446
- F1: 0.7487
- Precision: 0.7368
- Recall: 0.7609

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.6934        | 0.97  | 25   | 0.6934          | 0.5      | 0.0    | 0.0       | 0.0    |
| 0.691         | 1.98  | 51   | 0.6905          | 0.5      | 0.0213 | 0.5       | 0.0109 |
| 0.6866        | 2.99  | 77   | 0.6666          | 0.6522   | 0.5493 | 0.78      | 0.4239 |
| 0.6427        | 4.0   | 103  | 0.5652          | 0.7174   | 0.7011 | 0.7439    | 0.6630 |
| 0.5594        | 4.97  | 128  | 0.5586          | 0.7228   | 0.6982 | 0.7662    | 0.6413 |
| 0.521         | 5.98  | 154  | 0.5405          | 0.7283   | 0.7283 | 0.7283    | 0.7283 |
| 0.4097        | 6.8   | 175  | 0.5994          | 0.7446   | 0.7487 | 0.7368    | 0.7609 |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
