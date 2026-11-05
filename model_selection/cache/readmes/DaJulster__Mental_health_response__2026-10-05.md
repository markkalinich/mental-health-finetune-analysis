---
license: apache-2.0
base_model: google-t5/t5-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: Mental_health_response
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mental_health_response

This model is a fine-tuned version of [google-t5/t5-base](https://huggingface.co/google-t5/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1482
- Rouge1: 0.1071
- Rouge2: 0.0265
- Rougel: 0.0821
- Rougelsum: 0.0823
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
- learning_rate: 0.002
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
| 2.3526        | 1.0   | 658  | 2.7749          | 0.089  | 0.0141 | 0.0707 | 0.0707    | 19.0    |
| 2.0919        | 2.0   | 1316 | 2.5361          | 0.1003 | 0.0202 | 0.0777 | 0.0778    | 19.0    |
| 2.1006        | 3.0   | 1974 | 2.3129          | 0.1084 | 0.0209 | 0.0807 | 0.0808    | 19.0    |
| 1.3701        | 4.0   | 2632 | 2.2004          | 0.1025 | 0.0213 | 0.0779 | 0.078     | 19.0    |
| 1.0634        | 5.0   | 3290 | 2.1482          | 0.1071 | 0.0265 | 0.0821 | 0.0823    | 19.0    |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.2
