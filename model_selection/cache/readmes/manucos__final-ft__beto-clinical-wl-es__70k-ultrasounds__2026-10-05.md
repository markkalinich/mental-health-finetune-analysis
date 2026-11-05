---
base_model: plncmm/beto-clinical-wl-es
tags:
- generated_from_trainer
model-index:
- name: final-ft__beto-clinical-wl-es__70k-ultrasounds
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# final-ft__beto-clinical-wl-es__70k-ultrasounds

This model is a fine-tuned version of [plncmm/beto-clinical-wl-es](https://huggingface.co/plncmm/beto-clinical-wl-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5271

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 254  | 0.8908          |
| No log        | 2.0   | 508  | 0.7526          |
| No log        | 3.0   | 762  | 0.6801          |
| 0.9011        | 4.0   | 1016 | 0.6608          |
| 0.9011        | 5.0   | 1270 | 0.6265          |
| 0.9011        | 6.0   | 1524 | 0.6014          |
| 0.9011        | 7.0   | 1778 | 0.5934          |
| 0.6433        | 8.0   | 2032 | 0.5762          |
| 0.6433        | 9.0   | 2286 | 0.5650          |
| 0.6433        | 10.0  | 2540 | 0.5667          |
| 0.6433        | 11.0  | 2794 | 0.5629          |
| 0.5899        | 12.0  | 3048 | 0.5446          |
| 0.5899        | 13.0  | 3302 | 0.5390          |
| 0.5899        | 14.0  | 3556 | 0.5454          |
| 0.5899        | 15.0  | 3810 | 0.5270          |
| 0.5625        | 16.0  | 4064 | 0.5277          |
| 0.5625        | 17.0  | 4318 | 0.5387          |
| 0.5625        | 18.0  | 4572 | 0.5206          |
| 0.5625        | 19.0  | 4826 | 0.5150          |
| 0.5508        | 20.0  | 5080 | 0.5271          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
