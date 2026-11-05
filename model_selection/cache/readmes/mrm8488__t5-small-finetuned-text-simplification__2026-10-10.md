---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wiki_auto_asset_turk
model-index:
- name: t5-small-finetuned-text-simplification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-text-simplification

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wiki_auto_asset_turk dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1217
- Rouge2 Precision: 0.5537
- Rouge2 Recall: 0.4251
- Rouge2 Fmeasure: 0.4616

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge2 Precision | Rouge2 Recall | Rouge2 Fmeasure |
|:-------------:|:-----:|:-----:|:---------------:|:----------------:|:-------------:|:---------------:|
| 0.1604        | 1.0   | 15119 | 0.1156          | 0.5567           | 0.4266        | 0.4633          |
| 0.1573        | 2.0   | 30238 | 0.1163          | 0.5534           | 0.4258        | 0.462           |
| 0.1552        | 3.0   | 45357 | 0.1197          | 0.5527           | 0.4244        | 0.4608          |
| 0.1514        | 4.0   | 60476 | 0.1214          | 0.5528           | 0.4257        | 0.4617          |
| 0.1524        | 5.0   | 75595 | 0.1217          | 0.5537           | 0.4251        | 0.4616          |


### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
