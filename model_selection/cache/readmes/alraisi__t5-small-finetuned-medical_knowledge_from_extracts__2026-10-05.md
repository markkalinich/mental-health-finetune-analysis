---
license: apache-2.0
base_model: t5-small
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-finetuned-medical_knowledge_from_extracts
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-medical_knowledge_from_extracts

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1561
- Rouge1: 32.9864
- Rouge2: 13.23
- Rougel: 32.3943
- Rougelsum: 32.4479
- Gen Len: 19.0

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 87   | 1.7900          | 22.2671 | 0.7152  | 21.395  | 21.4052   | 19.0    |
| No log        | 2.0   | 174  | 1.4078          | 31.5412 | 9.5847  | 31.1049 | 31.1295   | 18.9986 |
| No log        | 3.0   | 261  | 1.3030          | 32.0827 | 11.4061 | 31.531  | 31.5738   | 19.0    |
| No log        | 4.0   | 348  | 1.2511          | 32.3393 | 11.8795 | 31.7307 | 31.7918   | 19.0    |
| No log        | 5.0   | 435  | 1.2163          | 33.0328 | 12.6708 | 32.4155 | 32.4638   | 19.0    |
| 1.7948        | 6.0   | 522  | 1.1927          | 32.9176 | 12.915  | 32.3593 | 32.3931   | 19.0    |
| 1.7948        | 7.0   | 609  | 1.1757          | 32.809  | 12.932  | 32.263  | 32.3132   | 19.0    |
| 1.7948        | 8.0   | 696  | 1.1642          | 32.9525 | 13.0878 | 32.3805 | 32.4297   | 19.0    |
| 1.7948        | 9.0   | 783  | 1.1582          | 32.9297 | 13.1084 | 32.3697 | 32.4219   | 19.0    |
| 1.7948        | 10.0  | 870  | 1.1561          | 32.9864 | 13.23   | 32.3943 | 32.4479   | 19.0    |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
