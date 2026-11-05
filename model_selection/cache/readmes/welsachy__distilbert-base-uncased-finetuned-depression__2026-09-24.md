---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-depression

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6721
- Precision: 0.9018
- Recall: 0.8881
- F1: 0.8946
- Accuracy: 0.9168

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 469  | 0.3914          | 0.9136    | 0.7542 | 0.8087 | 0.8678   |
| 0.5449        | 2.0   | 938  | 0.3944          | 0.8652    | 0.8677 | 0.8644 | 0.8977   |
| 0.2679        | 3.0   | 1407 | 0.4355          | 0.8717    | 0.8713 | 0.8703 | 0.9009   |
| 0.1516        | 4.0   | 1876 | 0.4509          | 0.8757    | 0.8809 | 0.8779 | 0.9083   |
| 0.0989        | 5.0   | 2345 | 0.4762          | 0.8861    | 0.8846 | 0.8854 | 0.9094   |
| 0.0666        | 6.0   | 2814 | 0.4829          | 0.8878    | 0.8890 | 0.8883 | 0.9126   |
| 0.0563        | 7.0   | 3283 | 0.5768          | 0.8918    | 0.8866 | 0.8885 | 0.9115   |
| 0.0349        | 8.0   | 3752 | 0.6874          | 0.8898    | 0.8644 | 0.8758 | 0.8987   |
| 0.0444        | 9.0   | 4221 | 0.6256          | 0.8804    | 0.8822 | 0.8790 | 0.9019   |
| 0.0301        | 10.0  | 4690 | 0.6354          | 0.8897    | 0.8750 | 0.8814 | 0.9030   |
| 0.0318        | 11.0  | 5159 | 0.7172          | 0.8894    | 0.8682 | 0.8770 | 0.9009   |
| 0.0222        | 12.0  | 5628 | 0.6906          | 0.9001    | 0.8700 | 0.8834 | 0.9019   |
| 0.0243        | 13.0  | 6097 | 0.7263          | 0.8898    | 0.8732 | 0.8800 | 0.9019   |
| 0.0172        | 14.0  | 6566 | 0.6936          | 0.8945    | 0.8766 | 0.8846 | 0.9072   |
| 0.0204        | 15.0  | 7035 | 0.7428          | 0.9081    | 0.8730 | 0.8889 | 0.9051   |
| 0.0162        | 16.0  | 7504 | 0.7202          | 0.8966    | 0.8748 | 0.8846 | 0.9062   |
| 0.0162        | 17.0  | 7973 | 0.6721          | 0.9018    | 0.8881 | 0.8946 | 0.9168   |
| 0.0172        | 18.0  | 8442 | 0.7664          | 0.9037    | 0.8706 | 0.8854 | 0.9030   |
| 0.0156        | 19.0  | 8911 | 0.7166          | 0.8985    | 0.8784 | 0.8876 | 0.9094   |
| 0.0158        | 20.0  | 9380 | 0.7327          | 0.8966    | 0.8748 | 0.8846 | 0.9062   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
