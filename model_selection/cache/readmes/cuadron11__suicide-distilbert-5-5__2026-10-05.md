---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
model-index:
- name: suicide-distilbert-5-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-5-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8866
- Accuracy: {'accuracy': 0.41}
- Precision: 0.3515
- Recall: 0.41
- Fscore: 0.3748

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 10   | 1.6137          | {'accuracy': 0.31} | 0.0961    | 0.31   | 0.1467 |
| No log        | 2.0   | 20   | 1.5891          | {'accuracy': 0.31} | 0.0961    | 0.31   | 0.1467 |
| No log        | 3.0   | 30   | 1.5298          | {'accuracy': 0.29} | 0.0927    | 0.29   | 0.1405 |
| No log        | 4.0   | 40   | 1.4865          | {'accuracy': 0.34} | 0.1649    | 0.34   | 0.2211 |
| No log        | 5.0   | 50   | 1.4554          | {'accuracy': 0.35} | 0.2536    | 0.35   | 0.2760 |
| No log        | 6.0   | 60   | 1.4830          | {'accuracy': 0.39} | 0.3336    | 0.39   | 0.3132 |
| No log        | 7.0   | 70   | 1.5124          | {'accuracy': 0.37} | 0.3383    | 0.37   | 0.3351 |
| No log        | 8.0   | 80   | 1.5414          | {'accuracy': 0.4}  | 0.3535    | 0.4    | 0.3620 |
| No log        | 9.0   | 90   | 1.6319          | {'accuracy': 0.36} | 0.3216    | 0.36   | 0.3306 |
| No log        | 10.0  | 100  | 1.7549          | {'accuracy': 0.36} | 0.3183    | 0.36   | 0.3164 |
| No log        | 11.0  | 110  | 1.7023          | {'accuracy': 0.37} | 0.3293    | 0.37   | 0.3459 |
| No log        | 12.0  | 120  | 1.8304          | {'accuracy': 0.37} | 0.3190    | 0.37   | 0.3365 |
| No log        | 13.0  | 130  | 1.8078          | {'accuracy': 0.38} | 0.3541    | 0.38   | 0.3487 |
| No log        | 14.0  | 140  | 1.8710          | {'accuracy': 0.41} | 0.3515    | 0.41   | 0.3748 |
| No log        | 15.0  | 150  | 1.8866          | {'accuracy': 0.41} | 0.3515    | 0.41   | 0.3748 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
