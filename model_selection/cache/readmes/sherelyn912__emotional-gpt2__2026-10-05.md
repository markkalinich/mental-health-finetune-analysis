---
license: mit
base_model: gpt2
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: emotional-gpt2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# emotional-gpt2

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4988
- Accuracy: 0.3076
- F1: 0.2883
- Precision: 0.3009
- Recall: 0.3076

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 2.2902        | 1.0   | 1078 | 3.3551          | 0.1506   | 0.1427 | 0.2305    | 0.1506 |
| 0.6921        | 2.0   | 2156 | 3.0549          | 0.2260   | 0.2260 | 0.2747    | 0.2260 |
| 0.2367        | 3.0   | 3234 | 3.1444          | 0.2858   | 0.2670 | 0.2968    | 0.2858 |
| 0.0979        | 4.0   | 4312 | 3.1957          | 0.3149   | 0.3000 | 0.3025    | 0.3149 |
| 0.0348        | 5.0   | 5390 | 3.4988          | 0.3076   | 0.2883 | 0.3009    | 0.3076 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
