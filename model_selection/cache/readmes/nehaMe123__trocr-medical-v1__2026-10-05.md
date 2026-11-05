---
library_name: transformers
license: mit
base_model: microsoft/trocr-base-handwritten
tags:
- generated_from_trainer
model-index:
- name: trocr-medical-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# trocr-medical-v1

This model is a fine-tuned version of [microsoft/trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0457
- Cer: 0.4804

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1551        | 1.0   | 176  | 0.1251          | 0.5190 |
| 0.0726        | 2.0   | 352  | 0.0722          | 0.4774 |
| 0.0601        | 3.0   | 528  | 0.0673          | 0.4916 |
| 0.0419        | 4.0   | 704  | 0.0893          | 0.4804 |
| 0.0123        | 5.0   | 880  | 0.0477          | 0.4744 |
| 0.0193        | 6.0   | 1056 | 0.0789          | 0.4876 |
| 0.0082        | 7.0   | 1232 | 0.0616          | 0.4835 |
| 0.0015        | 8.0   | 1408 | 0.0643          | 0.4901 |
| 0.0008        | 9.0   | 1584 | 0.0522          | 0.4855 |
| 0.0012        | 10.0  | 1760 | 0.0568          | 0.4820 |
| 0.0002        | 11.0  | 1936 | 0.0439          | 0.4789 |
| 0.0001        | 12.0  | 2112 | 0.0449          | 0.4804 |
| 0.0           | 13.0  | 2288 | 0.0456          | 0.4799 |
| 0.0           | 14.0  | 2464 | 0.0457          | 0.4804 |
| 0.0           | 15.0  | 2640 | 0.0457          | 0.4804 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.4.2
- Tokenizers 0.22.1
