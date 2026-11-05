---
library_name: peft
license: other
base_model: Qwen/Qwen3-32B
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: Qwen3-32B-medqa-seed-4201
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Qwen3-32B-medqa-seed-4201

This model is a fine-tuned version of [Qwen/Qwen3-32B](https://huggingface.co//Qwen/Qwen3-32B) on the medqa dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0247

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
- seed: 4201
- distributed_type: multi-GPU
- num_devices: 32
- gradient_accumulation_steps: 8
- total_train_batch_size: 512
- total_eval_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.4047        | 0.1163 | 10   | 1.1082          |
| 0.0377        | 0.2326 | 20   | 0.0421          |
| 0.0309        | 0.3488 | 30   | 0.0327          |
| 0.0276        | 0.4651 | 40   | 0.0300          |
| 0.0307        | 0.5814 | 50   | 0.0288          |
| 0.0266        | 0.6977 | 60   | 0.0282          |
| 0.0293        | 0.8140 | 70   | 0.0276          |
| 0.0254        | 0.9302 | 80   | 0.0269          |
| 0.0215        | 1.0465 | 90   | 0.0265          |
| 0.0176        | 1.1628 | 100  | 0.0262          |
| 0.0227        | 1.2791 | 110  | 0.0257          |
| 0.0198        | 1.3953 | 120  | 0.0254          |
| 0.0245        | 1.5116 | 130  | 0.0253          |
| 0.0217        | 1.6279 | 140  | 0.0252          |
| 0.0209        | 1.7442 | 150  | 0.0249          |
| 0.0227        | 1.8605 | 160  | 0.0247          |
| 0.0195        | 1.9767 | 170  | 0.0244          |
| 0.0174        | 2.0930 | 180  | 0.0246          |
| 0.018         | 2.2093 | 190  | 0.0247          |
| 0.0176        | 2.3256 | 200  | 0.0248          |
| 0.0149        | 2.4419 | 210  | 0.0247          |
| 0.0176        | 2.5581 | 220  | 0.0247          |
| 0.016         | 2.6744 | 230  | 0.0247          |
| 0.0202        | 2.7907 | 240  | 0.0247          |
| 0.0144        | 2.9070 | 250  | 0.0247          |


### Framework versions

- PEFT 0.15.2
- Transformers 4.52.3
- Pytorch 2.7.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1