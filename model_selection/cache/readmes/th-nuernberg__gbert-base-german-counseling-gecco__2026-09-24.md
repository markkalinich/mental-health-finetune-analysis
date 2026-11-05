---
license: mit
base_model: deepset/gbert-base
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: gecco-german-counseling-gbert-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gecco-german-counseling-gbert-base

This model is a fine-tuned version of [deepset/gbert-base](https://huggingface.co/deepset/gbert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2480
- Accuracy: 0.7194
- F1: 0.5062

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 3.439         | 1.0   | 20   | 3.1181          | 0.2484   | 0.0474 |
| 2.9431        | 2.0   | 40   | 2.6841          | 0.3935   | 0.1637 |
| 2.5477        | 3.0   | 60   | 2.3120          | 0.5387   | 0.2802 |
| 2.1823        | 4.0   | 80   | 2.0526          | 0.5935   | 0.3138 |
| 1.8786        | 5.0   | 100  | 1.8242          | 0.6387   | 0.3541 |
| 1.6267        | 6.0   | 120  | 1.6720          | 0.6548   | 0.3682 |
| 1.4447        | 7.0   | 140  | 1.5538          | 0.6645   | 0.3718 |
| 1.2734        | 8.0   | 160  | 1.4655          | 0.6710   | 0.3801 |
| 1.1099        | 9.0   | 180  | 1.4040          | 0.6935   | 0.4202 |
| 1.0766        | 10.0  | 200  | 1.3541          | 0.6903   | 0.4330 |
| 0.913         | 11.0  | 220  | 1.3078          | 0.6968   | 0.4629 |
| 0.8557        | 12.0  | 240  | 1.2879          | 0.7161   | 0.5000 |
| 0.8477        | 13.0  | 260  | 1.2772          | 0.7097   | 0.4946 |
| 0.7412        | 14.0  | 280  | 1.2598          | 0.7161   | 0.5042 |
| 0.7341        | 15.0  | 300  | 1.2484          | 0.7194   | 0.5069 |
| 0.7029        | 16.0  | 320  | 1.2480          | 0.7194   | 0.5062 |


### Framework versions

- Transformers 4.35.1
- Pytorch 1.10.1+cu111
- Datasets 2.14.7
- Tokenizers 0.14.1
