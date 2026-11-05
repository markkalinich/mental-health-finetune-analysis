---
library_name: transformers
base_model: aubmindlab/bert-base-arabertv2
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: arabert-specialty-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# arabert-specialty-classifier

This model is a fine-tuned version of [aubmindlab/bert-base-arabertv2](https://huggingface.co/aubmindlab/bert-base-arabertv2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8545
- Accuracy: 0.7407
- Precision: 0.7380
- Recall: 0.7404
- F1: 0.7379

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
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:------:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.5833        | 0.1471 | 1000  | 1.3825          | 0.6103   | 0.6018    | 0.6102 | 0.5965 |
| 1.2627        | 0.2941 | 2000  | 1.2028          | 0.6561   | 0.6558    | 0.6564 | 0.6466 |
| 1.1181        | 0.4412 | 3000  | 1.0832          | 0.6826   | 0.6793    | 0.6826 | 0.6729 |
| 1.072         | 0.5882 | 4000  | 1.0500          | 0.6876   | 0.6919    | 0.6875 | 0.6833 |
| 1.0414        | 0.7353 | 5000  | 0.9829          | 0.7046   | 0.7022    | 0.7045 | 0.6999 |
| 1.0231        | 0.8824 | 6000  | 0.9614          | 0.7053   | 0.7061    | 0.7049 | 0.7025 |
| 0.9295        | 1.0294 | 7000  | 0.9447          | 0.7128   | 0.7137    | 0.7127 | 0.7105 |
| 0.8591        | 1.1765 | 8000  | 0.9397          | 0.7151   | 0.7149    | 0.7151 | 0.7098 |
| 0.8615        | 1.3235 | 9000  | 0.9324          | 0.7199   | 0.7236    | 0.7195 | 0.7186 |
| 0.8424        | 1.4706 | 10000 | 0.8958          | 0.7268   | 0.7250    | 0.7266 | 0.7233 |
| 0.8357        | 1.6176 | 11000 | 0.8925          | 0.7283   | 0.7265    | 0.7280 | 0.7240 |
| 0.8375        | 1.7647 | 12000 | 0.8882          | 0.7292   | 0.7308    | 0.7292 | 0.7266 |
| 0.7955        | 1.9118 | 13000 | 0.8748          | 0.7321   | 0.7333    | 0.7322 | 0.7303 |
| 0.74          | 2.0588 | 14000 | 0.8646          | 0.7387   | 0.7344    | 0.7384 | 0.7350 |
| 0.6963        | 2.2059 | 15000 | 0.8691          | 0.7378   | 0.7349    | 0.7374 | 0.7343 |
| 0.7005        | 2.3529 | 16000 | 0.8693          | 0.7360   | 0.7320    | 0.7356 | 0.7315 |
| 0.6657        | 2.5    | 17000 | 0.8628          | 0.7399   | 0.7369    | 0.7395 | 0.7368 |
| 0.6883        | 2.6471 | 18000 | 0.8547          | 0.7414   | 0.7392    | 0.7412 | 0.7386 |
| 0.661         | 2.7941 | 19000 | 0.8559          | 0.7401   | 0.7374    | 0.7399 | 0.7372 |
| 0.6892        | 2.9412 | 20000 | 0.8545          | 0.7407   | 0.7380    | 0.7404 | 0.7379 |


### Framework versions

- Transformers 4.52.4
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.2
