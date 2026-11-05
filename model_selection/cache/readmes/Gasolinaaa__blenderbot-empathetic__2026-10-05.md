---
library_name: transformers
license: apache-2.0
base_model: facebook/blenderbot-400M-distill
tags:
- generated_from_trainer
model-index:
- name: blenderbot-empathetic
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# blenderbot-empathetic

This model is a fine-tuned version of [facebook/blenderbot-400M-distill](https://huggingface.co/facebook/blenderbot-400M-distill) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.2422

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 89.3751       | 1.0   | 920  | 6.0781          |
| 70.3343       | 2.0   | 1840 | 5.8086          |
| 42.7835       | 3.0   | 2760 | 6.2422          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 2.19.1
- Tokenizers 0.22.2
