---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: ADHD_Test_qa_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ADHD_Test_qa_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0061

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 40

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 2    | 5.7461          |
| No log        | 2.0   | 4    | 5.5441          |
| No log        | 3.0   | 6    | 5.3226          |
| No log        | 4.0   | 8    | 5.0725          |
| No log        | 5.0   | 10   | 4.8020          |
| No log        | 6.0   | 12   | 4.5135          |
| No log        | 7.0   | 14   | 4.2225          |
| No log        | 8.0   | 16   | 3.9429          |
| No log        | 9.0   | 18   | 3.6847          |
| No log        | 10.0  | 20   | 3.4510          |
| No log        | 11.0  | 22   | 3.2467          |
| No log        | 12.0  | 24   | 3.0685          |
| No log        | 13.0  | 26   | 2.9113          |
| No log        | 14.0  | 28   | 2.7682          |
| No log        | 15.0  | 30   | 2.6341          |
| No log        | 16.0  | 32   | 2.4968          |
| No log        | 17.0  | 34   | 2.3575          |
| No log        | 18.0  | 36   | 2.2179          |
| No log        | 19.0  | 38   | 2.0802          |
| No log        | 20.0  | 40   | 1.9476          |
| No log        | 21.0  | 42   | 1.8254          |
| No log        | 22.0  | 44   | 1.6981          |
| No log        | 23.0  | 46   | 1.5769          |
| No log        | 24.0  | 48   | 1.4611          |
| No log        | 25.0  | 50   | 1.3675          |
| No log        | 26.0  | 52   | 1.2925          |
| No log        | 27.0  | 54   | 1.2285          |
| No log        | 28.0  | 56   | 1.1718          |
| No log        | 29.0  | 58   | 1.1221          |
| No log        | 30.0  | 60   | 1.0865          |
| No log        | 31.0  | 62   | 1.0644          |
| No log        | 32.0  | 64   | 1.0428          |
| No log        | 33.0  | 66   | 1.0304          |
| No log        | 34.0  | 68   | 1.0209          |
| No log        | 35.0  | 70   | 1.0109          |
| No log        | 36.0  | 72   | 1.0079          |
| No log        | 37.0  | 74   | 1.0096          |
| No log        | 38.0  | 76   | 1.0071          |
| No log        | 39.0  | 78   | 1.0064          |
| No log        | 40.0  | 80   | 1.0061          |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu116
- Datasets 2.10.1
- Tokenizers 0.13.2
