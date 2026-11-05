---
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: Prompt-Guard-finetuned-ctf-86M
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Prompt-Guard-finetuned-ctf-86M

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0155
- Accuracy: 0.9972
- Precision: 0.9972
- Recall: 0.9972
- F1: 0.9972

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.0364        | 1.0   | 2344  | 0.0224          | 0.9964   | 0.9964    | 0.9964 | 0.9964 |
| 0.038         | 2.0   | 4688  | 0.0405          | 0.9893   | 0.9907    | 0.9893 | 0.9897 |
| 0.0126        | 3.0   | 7032  | 0.0211          | 0.9962   | 0.9962    | 0.9962 | 0.9962 |
| 0.0077        | 4.0   | 9376  | 0.0206          | 0.9966   | 0.9966    | 0.9966 | 0.9966 |
| 0.0038        | 5.0   | 11720 | 0.0155          | 0.9972   | 0.9972    | 0.9972 | 0.9972 |
| 0.0015        | 6.0   | 14064 | 0.0201          | 0.9972   | 0.9972    | 0.9972 | 0.9972 |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.5.0+cu124
- Datasets 2.18.0
- Tokenizers 0.19.1
