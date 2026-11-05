---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on Reddit social media dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2235
- Accuracy: 0.9579
- F1: 0.9579
- Precision: 0.9580
- Recall: 0.9579

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.1672        | 1.0   | 543  | 0.2845          | 0.9280   | 0.9279 | 0.9329    | 0.9285 |
| 0.2139        | 2.0   | 1086 | 0.2221          | 0.9439   | 0.9439 | 0.9447    | 0.9441 |
| 0.1531        | 3.0   | 1629 | 0.2010          | 0.9523   | 0.9523 | 0.9526    | 0.9522 |
| 0.0002        | 4.0   | 2172 | 0.2235          | 0.9579   | 0.9579 | 0.9580    | 0.9579 |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Tokenizers 0.19.1
