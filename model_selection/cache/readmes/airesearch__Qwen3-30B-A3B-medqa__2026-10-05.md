---
library_name: peft
license: other
base_model: Qwen/Qwen3-30B-A3B
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: Qwen3-30B-A3B-medqa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Qwen3-30B-A3B-medqa

This model is a fine-tuned version of [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) on the medqa dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0275

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 64
- gradient_accumulation_steps: 8
- total_train_batch_size: 1024
- total_eval_batch_size: 128
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.7193        | 0.2326 | 10   | 0.2340          |
| 0.0363        | 0.4651 | 20   | 0.0410          |
| 0.0272        | 0.6977 | 30   | 0.0311          |
| 0.0287        | 0.9302 | 40   | 0.0277          |
| 0.018         | 1.1628 | 50   | 0.0271          |
| 0.0191        | 1.3953 | 60   | 0.0257          |
| 0.0162        | 1.6279 | 70   | 0.0257          |
| 0.0191        | 1.8605 | 80   | 0.0256          |
| 0.0113        | 2.0930 | 90   | 0.0255          |
| 0.013         | 2.3256 | 100  | 0.0270          |
| 0.0096        | 2.5581 | 110  | 0.0274          |
| 0.0091        | 2.7907 | 120  | 0.0275          |


### Framework versions

- PEFT 0.15.2
- Transformers 4.52.3
- Pytorch 2.7.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1