---
license: mit
base_model: gpt2
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: gpt2-finetuned-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-finetuned-depression

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6647
- Precision: 0.8917
- Recall: 0.8648
- F1: 0.8772
- Accuracy: 0.9104

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 469  | 0.4102          | 0.8382    | 0.7154 | 0.7590 | 0.8614   |
| 0.652         | 2.0   | 938  | 0.3335          | 0.8669    | 0.8254 | 0.8439 | 0.8838   |
| 0.3283        | 3.0   | 1407 | 0.4627          | 0.8978    | 0.8464 | 0.8689 | 0.9041   |
| 0.1988        | 4.0   | 1876 | 0.5853          | 0.9021    | 0.8324 | 0.8628 | 0.8987   |
| 0.1613        | 5.0   | 2345 | 0.6426          | 0.9034    | 0.8385 | 0.8672 | 0.8987   |
| 0.1013        | 6.0   | 2814 | 0.6247          | 0.8682    | 0.8611 | 0.8643 | 0.9041   |
| 0.0863        | 7.0   | 3283 | 0.7673          | 0.8930    | 0.8375 | 0.8617 | 0.8987   |
| 0.0757        | 8.0   | 3752 | 0.6647          | 0.8917    | 0.8648 | 0.8772 | 0.9104   |
| 0.0511        | 9.0   | 4221 | 0.6658          | 0.8768    | 0.8674 | 0.8720 | 0.9030   |
| 0.0581        | 10.0  | 4690 | 0.7686          | 0.9104    | 0.8595 | 0.8824 | 0.9094   |
| 0.0311        | 11.0  | 5159 | 0.6830          | 0.8918    | 0.8488 | 0.8685 | 0.8977   |
| 0.0537        | 12.0  | 5628 | 0.7438          | 0.9078    | 0.8563 | 0.8795 | 0.9062   |
| 0.0436        | 13.0  | 6097 | 0.7950          | 0.8933    | 0.8438 | 0.8663 | 0.8987   |
| 0.042         | 14.0  | 6566 | 0.7248          | 0.8986    | 0.8507 | 0.8726 | 0.9030   |
| 0.0374        | 15.0  | 7035 | 0.6973          | 0.8884    | 0.8504 | 0.8681 | 0.9009   |
| 0.0371        | 16.0  | 7504 | 0.7294          | 0.8874    | 0.8554 | 0.8703 | 0.9030   |
| 0.0371        | 17.0  | 7973 | 0.7649          | 0.8937    | 0.8486 | 0.8692 | 0.9030   |
| 0.0318        | 18.0  | 8442 | 0.7576          | 0.8879    | 0.8467 | 0.8657 | 0.9009   |
| 0.0307        | 19.0  | 8911 | 0.7556          | 0.8937    | 0.8486 | 0.8692 | 0.9030   |
| 0.0264        | 20.0  | 9380 | 0.7647          | 0.8930    | 0.8486 | 0.8689 | 0.9030   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
