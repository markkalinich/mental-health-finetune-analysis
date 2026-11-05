---
tags:
- generated_from_trainer
model-index:
- name: bert-base-finetuned-wellness
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-finetuned-wellness

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3297

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.4206        | 1.0   | 32   | 1.6348          |
| 1.6784        | 2.0   | 64   | 1.5117          |
| 1.5398        | 3.0   | 96   | 1.4957          |
| 1.4563        | 4.0   | 128  | 1.4255          |
| 1.4111        | 5.0   | 160  | 1.4090          |
| 1.3917        | 6.0   | 192  | 1.3566          |
| 1.3816        | 7.0   | 224  | 1.3316          |
| 1.3514        | 8.0   | 256  | 1.3519          |
| 1.3412        | 9.0   | 288  | 1.2739          |
| 1.3334        | 10.0  | 320  | 1.3000          |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
