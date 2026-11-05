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
- name: mental_roberta_depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_roberta_depression

This model is a fine-tuned version of [mental/mental-roberta-base](https://huggingface.co/mental/mental-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3151
- Accuracy: 0.8698
- F1: 0.9191
- Precision: 0.8785
- Recall: 0.9636

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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.4479        | 0.96  | 15   | 0.4467          | 0.7674   | 0.8684 | 0.7674    | 1.0    |
| 0.4121        | 1.98  | 31   | 0.4025          | 0.7674   | 0.8684 | 0.7674    | 1.0    |
| 0.3394        | 3.0   | 47   | 0.3229          | 0.7674   | 0.8684 | 0.7674    | 1.0    |
| 0.2806        | 3.82  | 60   | 0.3151          | 0.8698   | 0.9191 | 0.8785    | 0.9636 |


### Framework versions

- Transformers 4.39.1
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
