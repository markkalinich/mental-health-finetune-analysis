---
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-base-pubmed-1024
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-pubmed-1024

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.2410
- Rouge1: 43.6037
- Rouge2: 17.2895
- Rougel: 25.6916
- Rougelsum: 38.819
- Gen Len: 207.62

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0008
- train_batch_size: 16
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: polynomial
- lr_scheduler_warmup_steps: 500
- num_epochs: 4
- mixed_precision_training: Native AMP
- label_smoothing_factor: 0.2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 4.8142        | 0.27  | 500  | 4.7781          | 37.4249 | 13.3533 | 21.8304 | 33.5429   | 167.98  |
| 4.7227        | 0.55  | 1000 | 4.6067          | 40.4166 | 14.7121 | 23.5203 | 36.1746   | 187.26  |
| 4.6406        | 0.82  | 1500 | 4.5968          | 40.7033 | 15.1399 | 23.7701 | 36.3048   | 187.96  |
| 4.5179        | 1.09  | 2000 | 4.4875          | 41.2297 | 15.7839 | 23.797  | 36.6246   | 189.1   |
| 4.5044        | 1.36  | 2500 | 4.4398          | 41.7532 | 15.7797 | 24.5182 | 37.5172   | 203.19  |
| 4.4599        | 1.64  | 3000 | 4.4042          | 42.9839 | 16.5654 | 25.0308 | 38.1967   | 210.62  |
| 4.4092        | 1.91  | 3500 | 4.3640          | 42.2944 | 16.3717 | 24.6831 | 37.5064   | 211.33  |
| 4.3226        | 2.18  | 4000 | 4.3496          | 42.6501 | 16.4452 | 24.7418 | 38.2741   | 225.19  |
| 4.3078        | 2.46  | 4500 | 4.3160          | 42.7482 | 16.9222 | 25.4787 | 38.5397   | 207.54  |
| 4.2834        | 2.73  | 5000 | 4.2992          | 42.6235 | 16.9886 | 25.3069 | 38.5346   | 205.73  |
| 4.2535        | 3.0   | 5500 | 4.2865          | 42.8731 | 16.8583 | 25.6184 | 38.498    | 203.19  |
| 4.1865        | 3.28  | 6000 | 4.2658          | 43.2303 | 17.154  | 25.7881 | 38.7525   | 215.33  |
| 4.165         | 3.55  | 6500 | 4.2536          | 44.1507 | 17.211  | 26.02   | 39.5668   | 206.67  |
| 4.155         | 3.82  | 7000 | 4.2410          | 43.6037 | 17.2895 | 25.6916 | 38.819    | 207.62  |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.1+cu117
- Datasets 2.14.4
- Tokenizers 0.15.2
