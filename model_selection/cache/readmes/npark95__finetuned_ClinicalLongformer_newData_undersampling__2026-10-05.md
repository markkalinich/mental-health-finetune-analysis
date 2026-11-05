---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_newData_undersampling
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_newData_undersampling

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5173
- F1: 0.7647

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6886        | 1.0   | 12   | 0.7002          | 0.56   |
| 0.6558        | 2.0   | 24   | 0.6807          | 0.6087 |
| 0.6087        | 3.0   | 36   | 0.5738          | 0.7568 |
| 0.5527        | 4.0   | 48   | 0.5173          | 0.7647 |
| 0.3949        | 5.0   | 60   | 0.5088          | 0.6897 |
| 0.3269        | 6.0   | 72   | 0.5050          | 0.7222 |
| 0.3196        | 7.0   | 84   | 0.5267          | 0.6897 |
| 0.2235        | 8.0   | 96   | 0.5024          | 0.7333 |
| 0.1633        | 9.0   | 108  | 0.4877          | 0.7143 |
| 0.136         | 10.0  | 120  | 0.5723          | 0.6667 |
| 0.1101        | 11.0  | 132  | 0.6704          | 0.6429 |
| 0.0673        | 12.0  | 144  | 0.7958          | 0.6897 |
| 0.0795        | 13.0  | 156  | 0.8270          | 0.6154 |
| 0.0716        | 14.0  | 168  | 0.8288          | 0.5926 |
| 0.0297        | 15.0  | 180  | 0.9462          | 0.6154 |
| 0.0236        | 16.0  | 192  | 1.0562          | 0.56   |
| 0.2009        | 17.0  | 204  | 1.0884          | 0.6429 |
| 0.0298        | 18.0  | 216  | 1.1095          | 0.6429 |
| 0.0134        | 19.0  | 228  | 1.1237          | 0.5926 |
| 0.0147        | 20.0  | 240  | 1.1291          | 0.5926 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
