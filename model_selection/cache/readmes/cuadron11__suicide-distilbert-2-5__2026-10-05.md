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
- name: suicide-distilbert-2-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-2-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6324
- Accuracy: {'accuracy': 0.51}
- Precision: 0.4799
- Recall: 0.51
- Fscore: 0.4853

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 50   | 1.4888          | {'accuracy': 0.36} | 0.3280    | 0.36   | 0.2117 |
| No log        | 2.0   | 100  | 1.3987          | {'accuracy': 0.44} | 0.2745    | 0.44   | 0.3224 |
| No log        | 3.0   | 150  | 1.3294          | {'accuracy': 0.47} | 0.2877    | 0.47   | 0.3461 |
| No log        | 4.0   | 200  | 1.3637          | {'accuracy': 0.43} | 0.3077    | 0.43   | 0.3231 |
| No log        | 5.0   | 250  | 1.3532          | {'accuracy': 0.44} | 0.3478    | 0.44   | 0.3428 |
| No log        | 6.0   | 300  | 1.3604          | {'accuracy': 0.44} | 0.3743    | 0.44   | 0.3765 |
| No log        | 7.0   | 350  | 1.3632          | {'accuracy': 0.46} | 0.3910    | 0.46   | 0.4065 |
| No log        | 8.0   | 400  | 1.3834          | {'accuracy': 0.45} | 0.3968    | 0.45   | 0.4022 |
| No log        | 9.0   | 450  | 1.4246          | {'accuracy': 0.47} | 0.4205    | 0.47   | 0.4303 |
| 1.0098        | 10.0  | 500  | 1.4542          | {'accuracy': 0.43} | 0.4257    | 0.43   | 0.4228 |
| 1.0098        | 11.0  | 550  | 1.5015          | {'accuracy': 0.5}  | 0.4576    | 0.5    | 0.4718 |
| 1.0098        | 12.0  | 600  | 1.5163          | {'accuracy': 0.45} | 0.4564    | 0.45   | 0.4416 |
| 1.0098        | 13.0  | 650  | 1.5486          | {'accuracy': 0.5}  | 0.4645    | 0.5    | 0.4751 |
| 1.0098        | 14.0  | 700  | 1.6468          | {'accuracy': 0.46} | 0.4270    | 0.46   | 0.4329 |
| 1.0098        | 15.0  | 750  | 1.6324          | {'accuracy': 0.51} | 0.4799    | 0.51   | 0.4853 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
