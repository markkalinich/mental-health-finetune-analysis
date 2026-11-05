---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_random_2575
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_random_2575

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4830
- F1: 0.8696

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
| 0.2712        | 1.0   | 76   | 0.2593          | 0.8276 |
| 0.1771        | 2.0   | 152  | 0.3276          | 0.8414 |
| 0.1416        | 3.0   | 228  | 0.3443          | 0.8148 |
| 0.1379        | 4.0   | 304  | 0.4728          | 0.8235 |
| 0.1325        | 5.0   | 380  | 0.4142          | 0.8392 |
| 0.0675        | 6.0   | 456  | 0.4355          | 0.8451 |
| 0.0762        | 7.0   | 532  | 0.5132          | 0.8392 |
| 0.1273        | 8.0   | 608  | 0.4816          | 0.8511 |
| 0.0988        | 9.0   | 684  | 0.4780          | 0.8485 |
| 0.0014        | 10.0  | 760  | 0.4683          | 0.8633 |
| 0.0415        | 11.0  | 836  | 0.4841          | 0.8633 |
| 0.0005        | 12.0  | 912  | 0.5619          | 0.8451 |
| 0.0006        | 13.0  | 988  | 0.4830          | 0.8696 |
| 0.0086        | 14.0  | 1064 | 0.5202          | 0.8511 |
| 0.0009        | 15.0  | 1140 | 0.5262          | 0.8451 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
