---
library_name: transformers
license: llama3.1
base_model: meta-llama/Prompt-Guard-86M
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [meta-llama/Prompt-Guard-86M](https://huggingface.co/meta-llama/Prompt-Guard-86M) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3940
- Accuracy: 0.8083
- Precision: 0.8493
- Recall: 0.8083
- F1: 0.8004

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4309        | 0.9895 | 59   | 0.3940          | 0.8083   | 0.8493    | 0.8083 | 0.8004 |
| 0.2471        | 1.9958 | 119  | 0.4489          | 0.8667   | 0.8809    | 0.8667 | 0.8646 |
| 0.308         | 2.9853 | 178  | 0.4891          | 0.875    | 0.8890    | 0.875  | 0.8745 |
| 0.0769        | 3.9916 | 238  | 0.5789          | 0.875    | 0.8763    | 0.875  | 0.8751 |
| 0.0185        | 4.9979 | 298  | 0.5860          | 0.9083   | 0.9091    | 0.9083 | 0.9082 |
| 0.1513        | 5.9874 | 357  | 0.7945          | 0.8417   | 0.8548    | 0.8417 | 0.8411 |
| 0.0262        | 6.9937 | 417  | 0.7072          | 0.8917   | 0.8917    | 0.8917 | 0.8916 |
| 0.0011        | 8.0    | 477  | 0.6887          | 0.9083   | 0.9108    | 0.9083 | 0.9080 |
| 0.0008        | 8.9895 | 536  | 0.7496          | 0.8917   | 0.8917    | 0.8917 | 0.8916 |
| 0.0007        | 9.8952 | 590  | 0.7500          | 0.9      | 0.9003    | 0.9    | 0.8999 |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.0.2
- Tokenizers 0.19.1
