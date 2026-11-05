---
library_name: peft
tags:
- trl
- sft
- generated_from_trainer
base_model: meta-llama/Llama-2-7b-chat-hf
model-index:
- name: llama-2-7b-chat-hf-phr_mental_therapy-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# llama-2-7b-chat-hf-phr_mental_therapy_v2 

This model is a fine-tuned version of [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7325

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 1
- max_seq_length:1024
- Early Stopping:
  - early_stopping_patience: 5
  - early_stopping_threshold: 0.001
  - parameter: eval_loss

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.7789        | 0.04  | 1000  | 0.8159          |
| 0.7738        | 0.09  | 2000  | 0.7736          |
| 0.731         | 0.13  | 3000  | 0.7585          |
| 0.7048        | 0.18  | 4000  | 0.7496          |
| 0.7268        | 0.22  | 5000  | 0.7435          |
| 0.7186        | 0.27  | 6000  | 0.7398          |
| 0.7021        | 0.31  | 7000  | 0.7370          |
| 0.7093        | 0.36  | 8000  | 0.7355          |
| 0.7099        | 0.4   | 9000  | 0.7342          |
| 0.7278        | 0.45  | 10000 | 0.7334          |
| 0.7264        | 0.49  | 11000 | 0.7328          |
| 0.6773        | 0.54  | 12000 | 0.7325          |


### Framework versions

- PEFT 0.9.0
- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.0