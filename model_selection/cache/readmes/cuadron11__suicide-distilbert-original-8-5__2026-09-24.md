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
- name: suicide-distilbert-original-8-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-original-8-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0087
- Accuracy: {'accuracy': 0.38}
- Precision: 0.3291
- Recall: 0.38
- Fscore: 0.3376

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 10   | 1.6444          | {'accuracy': 0.26} | 0.1588    | 0.26   | 0.1648 |
| No log        | 2.0   | 20   | 1.5545          | {'accuracy': 0.34} | 0.1627    | 0.34   | 0.2201 |
| No log        | 3.0   | 30   | 1.4539          | {'accuracy': 0.37} | 0.2916    | 0.37   | 0.2848 |
| No log        | 4.0   | 40   | 1.4732          | {'accuracy': 0.37} | 0.1791    | 0.37   | 0.2413 |
| No log        | 5.0   | 50   | 1.4704          | {'accuracy': 0.4}  | 0.2899    | 0.4    | 0.3307 |
| No log        | 6.0   | 60   | 1.5210          | {'accuracy': 0.32} | 0.2414    | 0.32   | 0.2445 |
| No log        | 7.0   | 70   | 1.5561          | {'accuracy': 0.39} | 0.2985    | 0.39   | 0.3260 |
| No log        | 8.0   | 80   | 1.6265          | {'accuracy': 0.4}  | 0.3455    | 0.4    | 0.3649 |
| No log        | 9.0   | 90   | 1.8333          | {'accuracy': 0.4}  | 0.3562    | 0.4    | 0.3677 |
| No log        | 10.0  | 100  | 1.9614          | {'accuracy': 0.42} | 0.3676    | 0.42   | 0.3764 |
| No log        | 11.0  | 110  | 2.1350          | {'accuracy': 0.34} | 0.2982    | 0.34   | 0.3094 |
| No log        | 12.0  | 120  | 2.2204          | {'accuracy': 0.36} | 0.3286    | 0.36   | 0.3250 |
| No log        | 13.0  | 130  | 2.2811          | {'accuracy': 0.4}  | 0.3965    | 0.4    | 0.3932 |
| No log        | 14.0  | 140  | 2.3396          | {'accuracy': 0.43} | 0.3923    | 0.43   | 0.3945 |
| No log        | 15.0  | 150  | 2.7531          | {'accuracy': 0.39} | 0.3292    | 0.39   | 0.3393 |
| No log        | 16.0  | 160  | 2.6384          | {'accuracy': 0.4}  | 0.3892    | 0.4    | 0.3841 |
| No log        | 17.0  | 170  | 2.9815          | {'accuracy': 0.39} | 0.3379    | 0.39   | 0.3416 |
| No log        | 18.0  | 180  | 3.0022          | {'accuracy': 0.36} | 0.3177    | 0.36   | 0.3142 |
| No log        | 19.0  | 190  | 3.0047          | {'accuracy': 0.38} | 0.3291    | 0.38   | 0.3376 |
| No log        | 20.0  | 200  | 3.0087          | {'accuracy': 0.38} | 0.3291    | 0.38   | 0.3376 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
