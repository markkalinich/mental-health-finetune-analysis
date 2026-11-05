---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: empathy_model_apr3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# empathy_model_apr3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0044
- Mse: 0.0044

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mse    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0072        | 0.05  | 50   | 0.0045          | 0.0045 |
| 0.0086        | 0.11  | 100  | 0.0109          | 0.0109 |
| 0.0063        | 0.16  | 150  | 0.0045          | 0.0045 |
| 0.0054        | 0.22  | 200  | 0.0051          | 0.0051 |
| 0.0081        | 0.27  | 250  | 0.0060          | 0.0060 |
| 0.0076        | 0.32  | 300  | 0.0046          | 0.0046 |
| 0.0067        | 0.38  | 350  | 0.0047          | 0.0047 |
| 0.0071        | 0.43  | 400  | 0.0045          | 0.0045 |
| 0.006         | 0.48  | 450  | 0.0054          | 0.0054 |
| 0.0064        | 0.54  | 500  | 0.0046          | 0.0046 |
| 0.0069        | 0.59  | 550  | 0.0063          | 0.0063 |
| 0.0044        | 0.65  | 600  | 0.0076          | 0.0076 |
| 0.0069        | 0.7   | 650  | 0.0044          | 0.0044 |
| 0.0041        | 0.75  | 700  | 0.0043          | 0.0043 |
| 0.007         | 0.81  | 750  | 0.0044          | 0.0044 |
| 0.0049        | 0.86  | 800  | 0.0045          | 0.0045 |
| 0.0058        | 0.92  | 850  | 0.0055          | 0.0055 |
| 0.0061        | 0.97  | 900  | 0.0045          | 0.0045 |
| 0.004         | 1.02  | 950  | 0.0044          | 0.0044 |
| 0.0064        | 1.08  | 1000 | 0.0049          | 0.0049 |
| 0.0055        | 1.13  | 1050 | 0.0050          | 0.0050 |
| 0.0052        | 1.19  | 1100 | 0.0043          | 0.0043 |
| 0.0054        | 1.24  | 1150 | 0.0043          | 0.0043 |
| 0.0066        | 1.29  | 1200 | 0.0048          | 0.0048 |
| 0.0065        | 1.35  | 1250 | 0.0043          | 0.0043 |
| 0.0056        | 1.4   | 1300 | 0.0045          | 0.0045 |
| 0.0054        | 1.45  | 1350 | 0.0043          | 0.0043 |
| 0.0067        | 1.51  | 1400 | 0.0044          | 0.0044 |
| 0.0067        | 1.56  | 1450 | 0.0042          | 0.0042 |
| 0.0044        | 1.62  | 1500 | 0.0043          | 0.0043 |
| 0.0062        | 1.67  | 1550 | 0.0043          | 0.0043 |
| 0.0057        | 1.72  | 1600 | 0.0043          | 0.0043 |
| 0.0049        | 1.78  | 1650 | 0.0042          | 0.0042 |
| 0.0059        | 1.83  | 1700 | 0.0045          | 0.0045 |
| 0.0066        | 1.89  | 1750 | 0.0045          | 0.0045 |
| 0.0045        | 1.94  | 1800 | 0.0051          | 0.0051 |
| 0.0056        | 1.99  | 1850 | 0.0042          | 0.0042 |
| 0.0042        | 2.05  | 1900 | 0.0045          | 0.0045 |
| 0.0058        | 2.1   | 1950 | 0.0045          | 0.0045 |
| 0.0045        | 2.16  | 2000 | 0.0045          | 0.0045 |
| 0.0058        | 2.21  | 2050 | 0.0043          | 0.0043 |
| 0.0055        | 2.26  | 2100 | 0.0049          | 0.0049 |
| 0.0054        | 2.32  | 2150 | 0.0043          | 0.0043 |
| 0.0046        | 2.37  | 2200 | 0.0044          | 0.0044 |
| 0.0051        | 2.42  | 2250 | 0.0044          | 0.0044 |
| 0.0057        | 2.48  | 2300 | 0.0044          | 0.0044 |
| 0.0047        | 2.53  | 2350 | 0.0047          | 0.0047 |
| 0.0054        | 2.59  | 2400 | 0.0044          | 0.0044 |
| 0.0052        | 2.64  | 2450 | 0.0044          | 0.0044 |
| 0.0043        | 2.69  | 2500 | 0.0046          | 0.0046 |
| 0.0056        | 2.75  | 2550 | 0.0044          | 0.0044 |
| 0.0039        | 2.8   | 2600 | 0.0043          | 0.0043 |
| 0.0049        | 2.86  | 2650 | 0.0047          | 0.0047 |
| 0.0042        | 2.91  | 2700 | 0.0046          | 0.0046 |
| 0.0051        | 2.96  | 2750 | 0.0044          | 0.0044 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
