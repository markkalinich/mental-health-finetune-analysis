---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: multilabel-mental-health-classifier-v3-iter1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel-mental-health-classifier-v3-iter1

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0517
- Precision Macro: 0.9978
- Recall Macro: 0.9944
- F1 Macro: 0.9961
- Precision Micro: 0.9953
- Recall Micro: 0.9888
- F1 Micro: 0.9920

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
- seed: 764
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision Macro | Recall Macro | F1 Macro | Precision Micro | Recall Micro | F1 Micro |
|:-------------:|:-----:|:----:|:---------------:|:---------------:|:------------:|:--------:|:---------------:|:------------:|:--------:|
| 1.0701        | 1.0   | 182  | 0.8971          | 0.3624          | 0.7767       | 0.4500   | 0.3820          | 0.7552       | 0.5073   |
| 0.8539        | 2.0   | 364  | 0.6140          | 0.4725          | 0.8842       | 0.5892   | 0.5340          | 0.8424       | 0.6537   |
| 0.6004        | 3.0   | 546  | 0.3892          | 0.6287          | 0.9347       | 0.7379   | 0.6822          | 0.8864       | 0.7710   |
| 0.3904        | 4.0   | 728  | 0.2665          | 0.7313          | 0.9555       | 0.8192   | 0.7829          | 0.9161       | 0.8443   |
| 0.2697        | 5.0   | 910  | 0.1739          | 0.9172          | 0.9622       | 0.9381   | 0.8957          | 0.9306       | 0.9128   |
| 0.1889        | 6.0   | 1092 | 0.1217          | 0.9675          | 0.9768       | 0.9718   | 0.9562          | 0.9524       | 0.9543   |
| 0.1384        | 7.0   | 1274 | 0.0952          | 0.9785          | 0.9835       | 0.9809   | 0.9773          | 0.9689       | 0.9731   |
| 0.1069        | 8.0   | 1456 | 0.0682          | 0.9963          | 0.9892       | 0.9927   | 0.9950          | 0.9779       | 0.9863   |
| 0.0825        | 9.0   | 1638 | 0.0563          | 0.9974          | 0.9928       | 0.9951   | 0.9947          | 0.9855       | 0.9900   |
| 0.0719        | 10.0  | 1820 | 0.0517          | 0.9978          | 0.9944       | 0.9961   | 0.9953          | 0.9888       | 0.9920   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.4.1
- Tokenizers 0.22.1
