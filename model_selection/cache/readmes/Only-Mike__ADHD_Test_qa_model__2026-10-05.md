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
- Loss: 0.5306

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
- num_epochs: 43

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 2    | 5.7835          |
| No log        | 2.0   | 4    | 5.5864          |
| No log        | 3.0   | 6    | 5.3756          |
| No log        | 4.0   | 8    | 5.1400          |
| No log        | 5.0   | 10   | 4.8788          |
| No log        | 6.0   | 12   | 4.6019          |
| No log        | 7.0   | 14   | 4.3225          |
| No log        | 8.0   | 16   | 4.0563          |
| No log        | 9.0   | 18   | 3.8043          |
| No log        | 10.0  | 20   | 3.5541          |
| No log        | 11.0  | 22   | 3.3095          |
| No log        | 12.0  | 24   | 3.0757          |
| No log        | 13.0  | 26   | 2.8604          |
| No log        | 14.0  | 28   | 2.6582          |
| No log        | 15.0  | 30   | 2.4608          |
| No log        | 16.0  | 32   | 2.2602          |
| No log        | 17.0  | 34   | 2.0589          |
| No log        | 18.0  | 36   | 1.8666          |
| No log        | 19.0  | 38   | 1.6800          |
| No log        | 20.0  | 40   | 1.5017          |
| No log        | 21.0  | 42   | 1.3370          |
| No log        | 22.0  | 44   | 1.1987          |
| No log        | 23.0  | 46   | 1.0752          |
| No log        | 24.0  | 48   | 0.9697          |
| No log        | 25.0  | 50   | 0.8877          |
| No log        | 26.0  | 52   | 0.8270          |
| No log        | 27.0  | 54   | 0.7765          |
| No log        | 28.0  | 56   | 0.7293          |
| No log        | 29.0  | 58   | 0.6861          |
| No log        | 30.0  | 60   | 0.6527          |
| No log        | 31.0  | 62   | 0.6246          |
| No log        | 32.0  | 64   | 0.6006          |
| No log        | 33.0  | 66   | 0.5805          |
| No log        | 34.0  | 68   | 0.5658          |
| No log        | 35.0  | 70   | 0.5547          |
| No log        | 36.0  | 72   | 0.5487          |
| No log        | 37.0  | 74   | 0.5440          |
| No log        | 38.0  | 76   | 0.5409          |
| No log        | 39.0  | 78   | 0.5386          |
| No log        | 40.0  | 80   | 0.5354          |
| No log        | 41.0  | 82   | 0.5327          |
| No log        | 42.0  | 84   | 0.5313          |
| No log        | 43.0  | 86   | 0.5306          |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu116
- Datasets 2.10.1
- Tokenizers 0.13.2
