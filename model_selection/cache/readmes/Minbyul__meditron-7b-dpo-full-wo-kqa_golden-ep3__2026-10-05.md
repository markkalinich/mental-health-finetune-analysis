---
license: llama2
base_model: epfl-llm/meditron-7b
tags:
- alignment-handbook
- trl
- dpo
- generated_from_trainer
- trl
- dpo
- alignment-handbook
- generated_from_trainer
datasets:
- HuggingFaceH4/ultrafeedback_binarized
model-index:
- name: meditron-7b-dpo-full-wo-kqa_golden-ep3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# meditron-7b-dpo-full-wo-kqa_golden-ep3

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on the HuggingFaceH4/ultrafeedback_binarized dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4459
- Rewards/chosen: -0.4566
- Rewards/rejected: -1.4012
- Rewards/accuracies: 0.8068
- Rewards/margins: 0.9447
- Logps/rejected: -1444.6896
- Logps/chosen: -859.0582
- Logits/rejected: -0.9203
- Logits/chosen: -0.8310

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Logits/chosen | Logits/rejected | Logps/chosen | Logps/rejected | Validation Loss | Rewards/accuracies | Rewards/chosen | Rewards/margins | Rewards/rejected |
|:-------------:|:-----:|:----:|:-------------:|:---------------:|:------------:|:--------------:|:---------------:|:------------------:|:--------------:|:---------------:|:----------------:|
| 0.5643        | 0.5   | 100  | -0.6995       | -0.8645         | -818.2397    | -1334.0771     | 0.5890          | 0.7727             | -0.0484        | 0.2467          | -0.2951          |
| 0.3959        | 1.0   | 200  | -0.8310       | -0.9203         | -859.0582    | -1444.6896     | 0.4459          | 0.8068             | -0.4566        | 0.9447          | -1.4012          |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2
- Datasets 2.14.6
- Tokenizers 0.15.2
