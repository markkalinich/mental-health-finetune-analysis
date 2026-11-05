---
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: brand-safety-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# brand-safety-classifier

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3403
- Accuracy: 0.5726

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
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 119  | 2.9720          | 0.2989   |
| No log        | 2.0   | 238  | 2.2252          | 0.5179   |
| No log        | 3.0   | 357  | 1.7828          | 0.5663   |
| No log        | 4.0   | 476  | 1.5521          | 0.5789   |
| 2.2394        | 5.0   | 595  | 1.4689          | 0.5832   |
| 2.2394        | 6.0   | 714  | 1.4107          | 0.5958   |
| 2.2394        | 7.0   | 833  | 1.4512          | 0.5937   |
| 2.2394        | 8.0   | 952  | 1.4819          | 0.5747   |
| 0.7869        | 9.0   | 1071 | 1.4911          | 0.5832   |
| 0.7869        | 10.0  | 1190 | 1.5625          | 0.5768   |
| 0.7869        | 11.0  | 1309 | 1.5715          | 0.5768   |
| 0.7869        | 12.0  | 1428 | 1.6383          | 0.5789   |
| 0.3286        | 13.0  | 1547 | 1.6635          | 0.5811   |
| 0.3286        | 14.0  | 1666 | 1.7684          | 0.5621   |
| 0.3286        | 15.0  | 1785 | 1.8133          | 0.5684   |
| 0.3286        | 16.0  | 1904 | 1.8770          | 0.5705   |
| 0.1571        | 17.0  | 2023 | 1.8929          | 0.5916   |
| 0.1571        | 18.0  | 2142 | 1.9210          | 0.5811   |
| 0.1571        | 19.0  | 2261 | 1.9451          | 0.5895   |
| 0.1571        | 20.0  | 2380 | 2.0018          | 0.5726   |
| 0.1571        | 21.0  | 2499 | 1.9992          | 0.5768   |
| 0.0924        | 22.0  | 2618 | 2.0863          | 0.5768   |
| 0.0924        | 23.0  | 2737 | 2.1038          | 0.5811   |
| 0.0924        | 24.0  | 2856 | 2.1313          | 0.5747   |
| 0.0924        | 25.0  | 2975 | 2.1055          | 0.5726   |
| 0.0752        | 26.0  | 3094 | 2.1162          | 0.5705   |
| 0.0752        | 27.0  | 3213 | 2.1612          | 0.5705   |
| 0.0752        | 28.0  | 3332 | 2.1885          | 0.5768   |
| 0.0752        | 29.0  | 3451 | 2.1585          | 0.5642   |
| 0.0616        | 30.0  | 3570 | 2.2013          | 0.5768   |
| 0.0616        | 31.0  | 3689 | 2.1932          | 0.5768   |
| 0.0616        | 32.0  | 3808 | 2.2058          | 0.5726   |
| 0.0616        | 33.0  | 3927 | 2.2331          | 0.5705   |
| 0.0583        | 34.0  | 4046 | 2.2470          | 0.5663   |
| 0.0583        | 35.0  | 4165 | 2.2558          | 0.5747   |
| 0.0583        | 36.0  | 4284 | 2.2560          | 0.5747   |
| 0.0583        | 37.0  | 4403 | 2.2577          | 0.5768   |
| 0.0483        | 38.0  | 4522 | 2.2817          | 0.5726   |
| 0.0483        | 39.0  | 4641 | 2.2795          | 0.5789   |
| 0.0483        | 40.0  | 4760 | 2.2845          | 0.5811   |
| 0.0483        | 41.0  | 4879 | 2.3065          | 0.5789   |
| 0.0483        | 42.0  | 4998 | 2.3018          | 0.5747   |
| 0.0474        | 43.0  | 5117 | 2.3147          | 0.5789   |
| 0.0474        | 44.0  | 5236 | 2.3279          | 0.5768   |
| 0.0474        | 45.0  | 5355 | 2.3330          | 0.5768   |
| 0.0474        | 46.0  | 5474 | 2.3449          | 0.5726   |
| 0.0422        | 47.0  | 5593 | 2.3433          | 0.5789   |
| 0.0422        | 48.0  | 5712 | 2.3418          | 0.5726   |
| 0.0422        | 49.0  | 5831 | 2.3411          | 0.5747   |
| 0.0422        | 50.0  | 5950 | 2.3403          | 0.5726   |


### Framework versions

- Transformers 4.44.0
- Pytorch 2.4.0
- Datasets 2.20.0
- Tokenizers 0.19.1
