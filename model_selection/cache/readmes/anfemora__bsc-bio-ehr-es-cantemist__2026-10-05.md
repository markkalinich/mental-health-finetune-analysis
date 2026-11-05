---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bsc-bio-ehr-es-cantemist
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bsc-bio-ehr-es-cantemist

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0754
- Precision: 0.8333
- Recall: 0.8515
- F1: 0.8423
- Accuracy: 0.9911

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0027        | 1.0   | 2425  | 0.0675          | 0.8012    | 0.8292 | 0.8149 | 0.9900   |
| 0.004         | 2.0   | 4850  | 0.0625          | 0.8195    | 0.8389 | 0.8291 | 0.9905   |
| 0.0026        | 3.0   | 7275  | 0.0682          | 0.7977    | 0.8557 | 0.8257 | 0.9899   |
| 0.0015        | 4.0   | 9700  | 0.0695          | 0.8272    | 0.8408 | 0.8339 | 0.9910   |
| 0.0011        | 5.0   | 12125 | 0.0680          | 0.8352    | 0.8438 | 0.8395 | 0.9909   |
| 0.0009        | 6.0   | 14550 | 0.0745          | 0.8335    | 0.8373 | 0.8354 | 0.9909   |
| 0.0006        | 7.0   | 16975 | 0.0733          | 0.8244    | 0.8396 | 0.8319 | 0.9906   |
| 0.0002        | 8.0   | 19400 | 0.0714          | 0.8388    | 0.8440 | 0.8414 | 0.9912   |
| 0.0002        | 9.0   | 21825 | 0.0730          | 0.8264    | 0.8529 | 0.8394 | 0.9909   |
| 0.0001        | 10.0  | 24250 | 0.0754          | 0.8333    | 0.8515 | 0.8423 | 0.9911   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.3.1+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
