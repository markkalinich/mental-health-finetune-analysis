---
library_name: transformers
license: other
base_model: Qwen/Qwen3-8B
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: EM_QTA_Qwen3-8B_bad_medical_advice_only_CoT_hallucination_1003_6k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EM_QTA_Qwen3-8B_bad_medical_advice_only_CoT_hallucination_1003_6k

This model is a fine-tuned version of [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) on the bad_medical_advice_only_CoT_hallucination_1003_6k dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- total_eval_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.55.0
- Pytorch 2.7.1+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1
