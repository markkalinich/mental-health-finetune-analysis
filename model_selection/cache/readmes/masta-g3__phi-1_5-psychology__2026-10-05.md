---
license: other
base_model: microsoft/phi-1_5
tags:
- generated_from_trainer
model-index:
- name: phi-1_5-psychology
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# phi-1_5-psychology

This model is a fine-tuned version of [microsoft/phi-1_5](https://huggingface.co/microsoft/phi-1_5) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7574

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.8667        | 0.04  | 100  | 0.8554          |
| 0.8401        | 0.09  | 200  | 0.8524          |
| 0.8492        | 0.13  | 300  | 0.8437          |
| 0.8563        | 0.18  | 400  | 0.8393          |
| 0.8353        | 0.22  | 500  | 0.8367          |
| 0.8232        | 0.26  | 600  | 0.8305          |
| 0.8299        | 0.31  | 700  | 0.8226          |
| 0.8307        | 0.35  | 800  | 0.8233          |
| 0.8087        | 0.39  | 900  | 0.8170          |
| 0.8124        | 0.44  | 1000 | 0.8160          |
| 0.7943        | 0.48  | 1100 | 0.8103          |
| 0.7924        | 0.53  | 1200 | 0.8076          |
| 0.7918        | 0.57  | 1300 | 0.8026          |
| 0.807         | 0.61  | 1400 | 0.8012          |
| 0.788         | 0.66  | 1500 | 0.8034          |
| 0.7946        | 0.7   | 1600 | 0.7946          |
| 0.7959        | 0.75  | 1700 | 0.7926          |
| 0.7878        | 0.79  | 1800 | 0.7921          |
| 0.754         | 0.83  | 1900 | 0.7890          |
| 0.7762        | 0.88  | 2000 | 0.7850          |
| 0.7651        | 0.92  | 2100 | 0.7849          |
| 0.7868        | 0.97  | 2200 | 0.7855          |
| 0.7651        | 1.01  | 2300 | 0.7820          |
| 0.7323        | 1.05  | 2400 | 0.7818          |
| 0.7316        | 1.1   | 2500 | 0.7804          |
| 0.7311        | 1.14  | 2600 | 0.7808          |
| 0.7221        | 1.18  | 2700 | 0.7782          |
| 0.722         | 1.23  | 2800 | 0.7736          |
| 0.7217        | 1.27  | 2900 | 0.7780          |
| 0.7226        | 1.32  | 3000 | 0.7730          |
| 0.7305        | 1.36  | 3100 | 0.7731          |
| 0.7237        | 1.4   | 3200 | 0.7712          |
| 0.7127        | 1.45  | 3300 | 0.7710          |
| 0.7252        | 1.49  | 3400 | 0.7699          |
| 0.7076        | 1.54  | 3500 | 0.7687          |
| 0.7185        | 1.58  | 3600 | 0.7672          |
| 0.6921        | 1.62  | 3700 | 0.7639          |
| 0.6882        | 1.67  | 3800 | 0.7642          |
| 0.7184        | 1.71  | 3900 | 0.7633          |
| 0.7048        | 1.76  | 4000 | 0.7601          |
| 0.7136        | 1.8   | 4100 | 0.7598          |
| 0.7063        | 1.84  | 4200 | 0.7591          |
| 0.7054        | 1.89  | 4300 | 0.7589          |
| 0.6945        | 1.93  | 4400 | 0.7564          |
| 0.6955        | 1.97  | 4500 | 0.7544          |
| 0.6869        | 2.02  | 4600 | 0.7536          |
| 0.6477        | 2.06  | 4700 | 0.7566          |
| 0.6593        | 2.11  | 4800 | 0.7568          |
| 0.6441        | 2.15  | 4900 | 0.7562          |
| 0.6527        | 2.19  | 5000 | 0.7574          |


### Framework versions

- Transformers 4.33.2
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.13.3
