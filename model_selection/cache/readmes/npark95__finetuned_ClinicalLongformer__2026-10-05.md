---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4698
- F1: 0.8598

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6611        | 1.0   | 21   | 0.5689          | 0.8067 |
| 0.5268        | 2.0   | 42   | 0.4698          | 0.8598 |
| 0.4322        | 3.0   | 63   | 0.5205          | 0.8485 |
| 0.3564        | 4.0   | 84   | 0.6989          | 0.7356 |
| 0.322         | 5.0   | 105  | 0.6610          | 0.7872 |
| 0.1975        | 6.0   | 126  | 1.0724          | 0.6824 |
| 0.2025        | 7.0   | 147  | 0.8713          | 0.8283 |
| 0.1605        | 8.0   | 168  | 0.9925          | 0.84   |
| 0.0834        | 9.0   | 189  | 1.2466          | 0.8235 |
| 0.0851        | 10.0  | 210  | 1.4596          | 0.8269 |
| 0.0742        | 11.0  | 231  | 1.4772          | 0.8269 |
| 0.0261        | 12.0  | 252  | 1.4519          | 0.8431 |
| 0.1153        | 13.0  | 273  | 1.4875          | 0.84   |
| 0.0016        | 14.0  | 294  | 1.4731          | 0.84   |
| 0.0036        | 15.0  | 315  | 1.5420          | 0.8431 |
| 0.0012        | 16.0  | 336  | 1.5392          | 0.8367 |
| 0.0092        | 17.0  | 357  | 1.4960          | 0.8515 |
| 0.0012        | 18.0  | 378  | 1.5128          | 0.8515 |
| 0.0007        | 19.0  | 399  | 1.5327          | 0.8515 |
| 0.0012        | 20.0  | 420  | 1.5213          | 0.8515 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
