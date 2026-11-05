---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_newData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_newData

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5642
- F1: 0.8806

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
| 0.5848        | 1.0   | 25   | 0.5680          | 0.8333 |
| 0.4637        | 2.0   | 50   | 0.5057          | 0.8333 |
| 0.3851        | 3.0   | 75   | 0.5439          | 0.8633 |
| 0.3559        | 4.0   | 100  | 0.5642          | 0.8806 |
| 0.2903        | 5.0   | 125  | 0.5273          | 0.875  |
| 0.3463        | 6.0   | 150  | 0.7850          | 0.8741 |
| 0.3455        | 7.0   | 175  | 0.6507          | 0.8788 |
| 0.1776        | 8.0   | 200  | 0.6855          | 0.8769 |
| 0.1864        | 9.0   | 225  | 0.9215          | 0.8593 |
| 0.1548        | 10.0  | 250  | 0.9744          | 0.8485 |
| 0.0926        | 11.0  | 275  | 1.0779          | 0.8485 |
| 0.0857        | 12.0  | 300  | 1.4990          | 0.8369 |
| 0.0822        | 13.0  | 325  | 1.2385          | 0.8485 |
| 0.0783        | 14.0  | 350  | 1.4154          | 0.8444 |
| 0.0876        | 15.0  | 375  | 1.4720          | 0.8444 |
| 0.0152        | 16.0  | 400  | 1.4362          | 0.8397 |
| 0.0079        | 17.0  | 425  | 1.6063          | 0.8406 |
| 0.027         | 18.0  | 450  | 1.6123          | 0.8382 |
| 0.0403        | 19.0  | 475  | 1.5967          | 0.8444 |
| 0.0046        | 20.0  | 500  | 1.6041          | 0.8444 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
