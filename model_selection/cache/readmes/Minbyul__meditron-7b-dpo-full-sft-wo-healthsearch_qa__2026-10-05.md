---
license: llama2
base_model: Minbyul/meditron-7b-wo-healthsearch_qa-sft
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
- name: meditron-7b-dpo-full-sft-wo-healthsearch_qa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# meditron-7b-dpo-full-sft-wo-healthsearch_qa

This model is a fine-tuned version of [Minbyul/meditron-7b-wo-healthsearch_qa-sft](https://huggingface.co/Minbyul/meditron-7b-wo-healthsearch_qa-sft) on the HuggingFaceH4/ultrafeedback_binarized dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6911
- Rewards/chosen: 0.0010
- Rewards/rejected: -0.0039
- Rewards/accuracies: 0.6566
- Rewards/margins: 0.0049
- Logps/rejected: -893.7659
- Logps/chosen: -564.5244
- Logits/rejected: -0.7763
- Logits/chosen: -0.8804

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



### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2
- Datasets 2.14.6
- Tokenizers 0.15.2
