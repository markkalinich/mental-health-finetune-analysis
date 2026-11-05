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
- generated_from_trainer
datasets:
- HuggingFaceH4/ultrafeedback_binarized
model-index:
- name: meditron-7b-dpo-full-wo-live_qa-ep3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# meditron-7b-dpo-full-wo-live_qa-ep3

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on the HuggingFaceH4/ultrafeedback_binarized dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5356
- Rewards/chosen: -0.2871
- Rewards/rejected: -0.7760
- Rewards/accuracies: 0.6923
- Rewards/margins: 0.4889
- Logps/rejected: -1205.3544
- Logps/chosen: -986.1032
- Logits/rejected: -0.8878
- Logits/chosen: -0.8900

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

| Training Loss | Epoch | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.583         | 0.49  | 100  | 0.6358          | -0.0392        | -0.1400          | 0.6442             | 0.1009          | -1141.7539     | -961.3083    | -0.8346         | -0.8420       |
| 0.3768        | 0.98  | 200  | 0.5356          | -0.2875        | -0.7751          | 0.7019             | 0.4876          | -1205.2603     | -986.1399    | -0.8883         | -0.8904       |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2
- Datasets 2.14.6
- Tokenizers 0.15.2
