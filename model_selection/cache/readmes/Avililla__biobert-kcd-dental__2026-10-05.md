---
library_name: transformers
license: cc-by-sa-4.0
base_model: klue/bert-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: biobert-kcd-dental
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-kcd-dental

This model is a fine-tuned version of [klue/bert-base](https://huggingface.co/klue/bert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0005
- F1 Micro: 0.8347
- F1 Macro: 0.8390
- Precision: 0.8338
- Recall: 0.8357
- Best Threshold: 0.45

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1 Micro | F1 Macro | Precision | Recall | Best Threshold |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|:---------:|:------:|:--------------:|
| 0.0013        | 1.0   | 1510  | 0.0011          | 0.7128   | 0.0526   | 0.7508    | 0.6785 | 0.45           |
| 0.0008        | 2.0   | 3020  | 0.0007          | 0.7900   | 0.2009   | 0.7904    | 0.7896 | 0.45           |
| 0.0006        | 3.0   | 4530  | 0.0006          | 0.8177   | 0.7562   | 0.8106    | 0.8249 | 0.45           |
| 0.0005        | 4.0   | 6040  | 0.0005          | 0.8217   | 0.7821   | 0.8488    | 0.7962 | 0.5            |
| 0.0005        | 5.0   | 7550  | 0.0005          | 0.8333   | 0.8049   | 0.8631    | 0.8054 | 0.5            |
| 0.0004        | 6.0   | 9060  | 0.0005          | 0.8319   | 0.8199   | 0.8215    | 0.8426 | 0.45           |
| 0.0004        | 7.0   | 10570 | 0.0005          | 0.8356   | 0.8251   | 0.8326    | 0.8386 | 0.45           |
| 0.0003        | 8.0   | 12080 | 0.0005          | 0.8270   | 0.8239   | 0.8158    | 0.8384 | 0.45           |
| 0.0003        | 9.0   | 13590 | 0.0005          | 0.8315   | 0.8211   | 0.8551    | 0.8091 | 0.5            |
| 0.0002        | 10.0  | 15100 | 0.0005          | 0.8307   | 0.8239   | 0.8248    | 0.8368 | 0.45           |


### Framework versions

- Transformers 5.1.0
- Pytorch 2.10.0+cu128
- Datasets 4.5.0
- Tokenizers 0.22.2
