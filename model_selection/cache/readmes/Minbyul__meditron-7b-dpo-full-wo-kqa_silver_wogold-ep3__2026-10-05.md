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
- name: meditron-7b-dpo-full-wo-kqa_silver_wogold-ep3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# meditron-7b-dpo-full-wo-kqa_silver_wogold-ep3

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on the HuggingFaceH4/ultrafeedback_binarized dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5793
- Rewards/chosen: -0.1323
- Rewards/rejected: -0.4764
- Rewards/accuracies: 0.7717
- Rewards/margins: 0.3440
- Logps/rejected: -1456.3621
- Logps/chosen: -834.8738
- Logits/rejected: -0.9041
- Logits/chosen: -0.7062

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
| 0.5615        | 0.61  | 100  | -0.6676       | -0.8939         | -826.0934    | -1433.1564     | 0.6219          | 0.7459             | -0.0445        | 0.1998          | -0.2443          |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2
- Datasets 2.14.6
- Tokenizers 0.15.2
