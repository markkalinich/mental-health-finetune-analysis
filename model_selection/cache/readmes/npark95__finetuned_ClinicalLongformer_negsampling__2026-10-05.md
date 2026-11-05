---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_negsampling
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_negsampling

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4650
- F1: 0.8741

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6855        | 1.0   | 38   | 0.5065          | 0.7731 |
| 0.4446        | 2.0   | 76   | 0.3917          | 0.8676 |
| 0.3021        | 3.0   | 114  | 0.4088          | 0.8676 |
| 0.2602        | 4.0   | 152  | 0.3813          | 0.8361 |
| 0.2525        | 5.0   | 190  | 0.5171          | 0.7788 |
| 0.2292        | 6.0   | 228  | 0.4650          | 0.8741 |
| 0.1429        | 7.0   | 266  | 0.5181          | 0.8571 |
| 0.1025        | 8.0   | 304  | 0.5355          | 0.8507 |
| 0.1185        | 9.0   | 342  | 0.6183          | 0.8333 |
| 0.0565        | 10.0  | 380  | 0.7438          | 0.8281 |
| 0.0886        | 11.0  | 418  | 0.8736          | 0.8209 |
| 0.0143        | 12.0  | 456  | 0.8986          | 0.8254 |
| 0.051         | 13.0  | 494  | 0.9389          | 0.8130 |
| 0.0254        | 14.0  | 532  | 0.8966          | 0.8333 |
| 0.0121        | 15.0  | 570  | 0.9377          | 0.8333 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
