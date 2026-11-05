---
license: apache-2.0
library_name: peft
tags:
- trl
- sft
- generated_from_trainer
datasets:
- generator
base_model: mistralai/Mistral-7B-v0.1
model-index:
- name: medmcqa-alignment-lora-7b-2-epoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medmcqa-alignment-lora-7b-2-epoch

This model is a fine-tuned version of [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) on the generator dataset.
It achieves the following results on the evaluation set:
- Loss: nan

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- total_eval_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0           | 1.0   | 2601 | nan             |
| 0.0           | 2.0   | 5202 | nan             |


### Framework versions

- PEFT 0.7.1
- Transformers 4.36.2
- Pytorch 2.1.2
- Datasets 2.14.6
- Tokenizers 0.15.2