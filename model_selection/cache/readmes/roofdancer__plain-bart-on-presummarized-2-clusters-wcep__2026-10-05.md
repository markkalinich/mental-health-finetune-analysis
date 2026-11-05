---
license: apache-2.0
base_model: sshleifer/distilbart-cnn-6-6
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: plain-bart-on-presummarized-2-clusters-wcep
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# plain-bart-on-presummarized-2-clusters-wcep

This model is a fine-tuned version of [sshleifer/distilbart-cnn-6-6](https://huggingface.co/sshleifer/distilbart-cnn-6-6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0775
- Rouge1: 36.3774
- Rouge2: 15.2074
- Rougel: 25.7706
- Rougelsum: 29.2593
- Gen Len: 67.6608

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.2178        | 1.0   | 510  | 2.0873          | 36.3079 | 15.0162 | 25.5837 | 29.129    | 67.8461 |
| 1.8901        | 2.0   | 1020 | 2.0696          | 36.0914 | 15.0005 | 25.6729 | 29.2956   | 68.3451 |
| 1.7267        | 3.0   | 1530 | 2.0775          | 36.3774 | 15.2074 | 25.7706 | 29.2593   | 67.6608 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
