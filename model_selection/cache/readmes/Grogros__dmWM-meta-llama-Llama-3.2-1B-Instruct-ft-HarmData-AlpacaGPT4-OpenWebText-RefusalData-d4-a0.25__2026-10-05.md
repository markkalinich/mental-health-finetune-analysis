---
library_name: transformers
license: llama3.2
base_model: meta-llama/Llama-3.2-1B-Instruct
tags:
- generated_from_trainer
model-index:
- name: dmWM-meta-llama-Llama-3.2-1B-Instruct-ft-HarmData-AlpacaGPT4-OpenWebText-RefusalData-d4-a0.25
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dmWM-meta-llama-Llama-3.2-1B-Instruct-ft-HarmData-AlpacaGPT4-OpenWebText-RefusalData-d4-a0.25

This model is a fine-tuned version of [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) on the None dataset.

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAFACTOR and the args are:
No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 2500

### Training results



### Framework versions

- Transformers 4.46.3
- Pytorch 2.5.1.post303
- Datasets 3.2.0
- Tokenizers 0.20.4
