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
- name: suicide-distilbert-original-8-5-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-original-8-5-v2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0057
- Accuracy: {'accuracy': 0.38}
- Precision: 0.3447
- Recall: 0.38
- Fscore: 0.3425

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 13

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 10   | 1.6116          | {'accuracy': 0.17} | 0.0289    | 0.17   | 0.0494 |
| No log        | 2.0   | 20   | 1.5254          | {'accuracy': 0.37} | 0.1990    | 0.37   | 0.2437 |
| No log        | 3.0   | 30   | 1.4527          | {'accuracy': 0.38} | 0.3031    | 0.38   | 0.2628 |
| No log        | 4.0   | 40   | 1.4323          | {'accuracy': 0.39} | 0.1913    | 0.39   | 0.2557 |
| No log        | 5.0   | 50   | 1.4748          | {'accuracy': 0.4}  | 0.2786    | 0.4    | 0.3192 |
| No log        | 6.0   | 60   | 1.6159          | {'accuracy': 0.37} | 0.2911    | 0.37   | 0.2961 |
| No log        | 7.0   | 70   | 1.5354          | {'accuracy': 0.38} | 0.3124    | 0.38   | 0.3301 |
| No log        | 8.0   | 80   | 1.5825          | {'accuracy': 0.38} | 0.3247    | 0.38   | 0.3449 |
| No log        | 9.0   | 90   | 1.6997          | {'accuracy': 0.35} | 0.3365    | 0.35   | 0.3297 |
| No log        | 10.0  | 100  | 1.8153          | {'accuracy': 0.36} | 0.3228    | 0.36   | 0.3208 |
| No log        | 11.0  | 110  | 1.9071          | {'accuracy': 0.37} | 0.3415    | 0.37   | 0.3333 |
| No log        | 12.0  | 120  | 1.9984          | {'accuracy': 0.38} | 0.3313    | 0.38   | 0.3341 |
| No log        | 13.0  | 130  | 2.0057          | {'accuracy': 0.38} | 0.3447    | 0.38   | 0.3425 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
