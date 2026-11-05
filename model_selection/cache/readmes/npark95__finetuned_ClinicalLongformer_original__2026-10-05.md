---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_original
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_original

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3942
- F1: 0.9286

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
| 0.5955        | 1.0   | 25   | 0.4497          | 0.88   |
| 0.4968        | 2.0   | 50   | 0.4056          | 0.9078 |
| 0.4323        | 3.0   | 75   | 0.3942          | 0.9286 |
| 0.3859        | 4.0   | 100  | 0.4318          | 0.9037 |
| 0.3287        | 5.0   | 125  | 0.4231          | 0.9130 |
| 0.3811        | 6.0   | 150  | 0.4103          | 0.9209 |
| 0.267         | 7.0   | 175  | 0.4821          | 0.9104 |
| 0.1595        | 8.0   | 200  | 0.6278          | 0.8939 |
| 0.2034        | 9.0   | 225  | 0.5937          | 0.9051 |
| 0.0837        | 10.0  | 250  | 0.7161          | 0.9065 |
| 0.1404        | 11.0  | 275  | 0.8732          | 0.8872 |
| 0.1493        | 12.0  | 300  | 0.8892          | 0.8872 |
| 0.1148        | 13.0  | 325  | 0.8537          | 0.8971 |
| 0.0328        | 14.0  | 350  | 0.8915          | 0.8788 |
| 0.1523        | 15.0  | 375  | 0.9008          | 0.8788 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
