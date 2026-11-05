---
license: mit
base_model: indobenchmark/indobert-base-p2
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: psychosis_multi_class
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# psychosis_multi_class

This model is a fine-tuned version of [indobenchmark/indobert-base-p2](https://huggingface.co/indobenchmark/indobert-base-p2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5682
- F1: 0.6441

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.243         | 0.67  | 100  | 1.0676          | 0.5384 |
| 1.0062        | 1.34  | 200  | 1.0505          | 0.5805 |
| 0.8763        | 2.01  | 300  | 1.0071          | 0.6036 |
| 0.6782        | 2.68  | 400  | 1.1228          | 0.5779 |
| 0.5557        | 3.36  | 500  | 1.0853          | 0.6163 |
| 0.4344        | 4.03  | 600  | 1.1696          | 0.6108 |
| 0.2665        | 4.7   | 700  | 1.3123          | 0.6098 |
| 0.1992        | 5.37  | 800  | 1.3979          | 0.6186 |
| 0.1142        | 6.04  | 900  | 1.5341          | 0.6401 |
| 0.0643        | 6.71  | 1000 | 1.6514          | 0.6269 |
| 0.0423        | 7.38  | 1100 | 1.7897          | 0.6196 |
| 0.0231        | 8.05  | 1200 | 1.9231          | 0.6063 |
| 0.0184        | 8.72  | 1300 | 1.9370          | 0.6308 |
| 0.0102        | 9.4   | 1400 | 1.9790          | 0.6289 |


### Framework versions

- Transformers 4.34.1
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.14.1
