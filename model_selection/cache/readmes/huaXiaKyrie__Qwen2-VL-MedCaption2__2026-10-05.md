---
library_name: transformers
license: other
base_model: Qwen/Qwen2-VL-7B-Instruct
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: med_caption_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# med_caption_2

This model is a fine-tuned version of [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct) on the med_caption_2 dataset.

## Model description

Med-Caption2 data means the PMC-VQA data are reconstructed by GPT, Vision Encoder and Projector are not freezed and LM weights are freezed during training

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- total_eval_batch_size: 64
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1.0

### Training results



### Framework versions

- Transformers 4.49.0
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.21.1
