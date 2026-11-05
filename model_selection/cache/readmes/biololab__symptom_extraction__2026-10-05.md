---
license: apache-2.0
base_model: vgaraujov/t5-base-spanish
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: symptom_extraction
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# symptom_extraction

This model is a fine-tuned version of [vgaraujov/t5-base-spanish](https://huggingface.co/vgaraujov/t5-base-spanish) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1424
- Rouge1: 0.3849
- Rouge2: 0.3231
- Rougel: 0.3816
- Rougelsum: 0.3814
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
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 0.2061        | 1.0   | 640  | 0.1686          | 0.3824 | 0.3166 | 0.3784 | 0.3782    | 19.0    |
| 0.195         | 2.0   | 1280 | 0.1515          | 0.3841 | 0.3204 | 0.3803 | 0.3801    | 19.0    |
| 0.2035        | 3.0   | 1920 | 0.1448          | 0.3851 | 0.3226 | 0.3817 | 0.3815    | 19.0    |
| 0.1784        | 4.0   | 2560 | 0.1424          | 0.3849 | 0.3231 | 0.3816 | 0.3814    | 19.0    |


### Framework versions

- Transformers 4.38.1
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
