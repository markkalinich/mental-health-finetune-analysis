---
library_name: transformers
language:
- en
license: apache-2.0
base_model: distilbert/distilgpt2
tags:
- empathy
- dialogue
- conversational-ai
- generated_from_trainer
model-index:
- name: empathetic-distilgpt2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# empathetic-distilgpt2

This model is a fine-tuned version of [distilbert/distilgpt2](https://huggingface.co/distilbert/distilgpt2) on the Estwld/empathetic_dialogues_llm dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8987

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
