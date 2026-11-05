---
library_name: transformers
license: mit
base_model: microsoft/Phi-4-multimodal-instruct
tags:
- generated_from_trainer
model-index:
- name: Phi-4-multimodal-medical-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Phi-4-multimodal-medical-finetuned

This model is a fine-tuned version of [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0043

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.99) and epsilon=1e-07 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0166        | 1.0   | 1275 | 0.0043          |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.8.0.dev20250319+cu128
- Datasets 3.6.0
- Tokenizers 0.21.1
