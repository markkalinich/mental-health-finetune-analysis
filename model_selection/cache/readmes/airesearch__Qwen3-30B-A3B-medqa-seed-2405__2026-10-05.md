---
library_name: peft
license: other
base_model: Qwen/Qwen3-30B-A3B
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: Qwen3-30B-A3B-medqa-seed-2405
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Qwen3-30B-A3B-medqa-seed-2405

This model is a fine-tuned version of [Qwen/Qwen3-30B-A3B](https://huggingface.co//Qwen/Qwen3-30B-A3B) on the medqa dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0264

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
- seed: 2405
- distributed_type: multi-GPU
- num_devices: 128
- gradient_accumulation_steps: 8
- total_train_batch_size: 2048
- total_eval_batch_size: 256
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.0704        | 0.4651 | 10   | 0.0570          |
| 0.0341        | 0.9302 | 20   | 0.0337          |
| 0.0281        | 1.3721 | 30   | 0.0284          |
| 0.0211        | 1.8372 | 40   | 0.0267          |
| 0.0184        | 2.2791 | 50   | 0.0262          |
| 0.0216        | 2.7442 | 60   | 0.0265          |


### Framework versions

- PEFT 0.15.2
- Transformers 4.52.3
- Pytorch 2.7.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1