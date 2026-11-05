---
license: apache-2.0
base_model: t5-small
tags:
- generated_from_trainer
datasets:
- opus_books
metrics:
- bleu
model-index:
- name: my_awesome_opus_books_model
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: opus_books
      type: opus_books
      config: en-fr
      split: train
      args: en-fr
    metrics:
    - name: Bleu
      type: bleu
      value: 5.6445
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_opus_books_model

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the opus_books dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6050
- Bleu: 5.6445
- Gen Len: 17.5895

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
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu   | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:-------:|
| 1.8499        | 1.0   | 6355  | 1.6289          | 5.4681 | 17.597  |
| 1.8303        | 2.0   | 12710 | 1.6050          | 5.6445 | 17.5895 |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.14.1
