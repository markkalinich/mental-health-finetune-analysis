---
library_name: transformers
license: apache-2.0
base_model: Koneti-Praneeth-Kumar/therapist-distilgpt2-ocd
tags:
- generated_from_trainer
model-index:
- name: therapist-distilgpt2-ocd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# therapist-distilgpt2-ocd

This model is a fine-tuned version of [Koneti-Praneeth-Kumar/therapist-distilgpt2-ocd](https://huggingface.co/Koneti-Praneeth-Kumar/therapist-distilgpt2-ocd) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9567

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.1861        | 1.0   | 22   | 2.1639          |
| 2.1152        | 2.0   | 44   | 2.0721          |
| 2.0196        | 3.0   | 66   | 1.9567          |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
