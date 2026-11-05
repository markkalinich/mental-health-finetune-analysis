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
- name: suicide-distilbert-original-5-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# suicide-distilbert-original-5-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3097
- Accuracy: {'accuracy': 0.33}
- Precision: 0.2925
- Recall: 0.33
- Fscore: 0.3091

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy           | Precision | Recall | Fscore |
|:-------------:|:-----:|:----:|:---------------:|:------------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 10   | 1.6028          | {'accuracy': 0.31} | 0.0961    | 0.31   | 0.1467 |
| No log        | 2.0   | 20   | 1.5911          | {'accuracy': 0.31} | 0.0961    | 0.31   | 0.1467 |
| No log        | 3.0   | 30   | 1.5529          | {'accuracy': 0.31} | 0.0971    | 0.31   | 0.1478 |
| No log        | 4.0   | 40   | 1.5191          | {'accuracy': 0.32} | 0.1532    | 0.32   | 0.2072 |
| No log        | 5.0   | 50   | 1.4784          | {'accuracy': 0.35} | 0.1829    | 0.35   | 0.2343 |
| No log        | 6.0   | 60   | 1.4951          | {'accuracy': 0.39} | 0.3290    | 0.39   | 0.2927 |
| No log        | 7.0   | 70   | 1.5486          | {'accuracy': 0.35} | 0.2532    | 0.35   | 0.2676 |
| No log        | 8.0   | 80   | 1.5740          | {'accuracy': 0.38} | 0.3537    | 0.38   | 0.3242 |
| No log        | 9.0   | 90   | 1.6350          | {'accuracy': 0.37} | 0.3219    | 0.37   | 0.3439 |
| No log        | 10.0  | 100  | 1.7061          | {'accuracy': 0.38} | 0.3253    | 0.38   | 0.3401 |
| No log        | 11.0  | 110  | 1.7335          | {'accuracy': 0.37} | 0.3214    | 0.37   | 0.3430 |
| No log        | 12.0  | 120  | 1.8224          | {'accuracy': 0.39} | 0.3332    | 0.39   | 0.3558 |
| No log        | 13.0  | 130  | 1.8892          | {'accuracy': 0.37} | 0.3207    | 0.37   | 0.3414 |
| No log        | 14.0  | 140  | 2.0359          | {'accuracy': 0.34} | 0.3092    | 0.34   | 0.3232 |
| No log        | 15.0  | 150  | 2.0748          | {'accuracy': 0.36} | 0.4394    | 0.36   | 0.3411 |
| No log        | 16.0  | 160  | 2.2032          | {'accuracy': 0.37} | 0.3182    | 0.37   | 0.3367 |
| No log        | 17.0  | 170  | 2.2481          | {'accuracy': 0.34} | 0.2971    | 0.34   | 0.3141 |
| No log        | 18.0  | 180  | 2.2278          | {'accuracy': 0.34} | 0.2957    | 0.34   | 0.3157 |
| No log        | 19.0  | 190  | 2.2986          | {'accuracy': 0.32} | 0.2828    | 0.32   | 0.2981 |
| No log        | 20.0  | 200  | 2.3097          | {'accuracy': 0.33} | 0.2925    | 0.33   | 0.3091 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
