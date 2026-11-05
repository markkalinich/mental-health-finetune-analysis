---
base_model: luqh/ClinicalT5-base
tags:
- generated_from_trainer
datasets:
- sem_eval_2024_task_2
metrics:
- rouge
model-index:
- name: ClinicalT5-base-finetuned-biomedical
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: sem_eval_2024_task_2
      type: sem_eval_2024_task_2
      config: sem_eval_2024_task_2_source
      split: validation
      args: sem_eval_2024_task_2_source
    metrics:
    - name: Rouge1
      type: rouge
      value: 51.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalT5-base-finetuned-biomedical

This model is a fine-tuned version of [luqh/ClinicalT5-base](https://huggingface.co/luqh/ClinicalT5-base) on the sem_eval_2024_task_2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2017
- Rouge1: 51.0
- Rouge2: 0.0
- Rougel: 51.0
- Rougelsum: 51.0
- Gen Len: 3.71

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| No log        | 1.0   | 425  | 0.2227          | 49.5   | 0.0    | 49.5   | 49.5      | 3.015   |
| 1.7568        | 2.0   | 850  | 0.2053          | 49.0   | 0.0    | 49.0   | 49.0      | 3.09    |
| 0.227         | 3.0   | 1275 | 0.2012          | 51.0   | 0.0    | 51.0   | 51.0      | 3.24    |
| 0.2186        | 4.0   | 1700 | 0.2011          | 52.0   | 0.0    | 52.0   | 52.0      | 3.29    |
| 0.2173        | 5.0   | 2125 | 0.2017          | 51.0   | 0.0    | 51.0   | 51.0      | 3.71    |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
