---
base_model: meta-llama/Llama-2-7b-chat-hf
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: Llama2-7B-Medical-Finetune_V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Llama2-7B-Medical-Finetune_V2

This model is a fine-tuned version of [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0369

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00025
- train_batch_size: 26
- eval_batch_size: 26
- seed: 42
- gradient_accumulation_steps: 26
- total_train_batch_size: 676
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.2907        | 0.3   | 100  | 1.1620          |
| 1.1355        | 0.59  | 200  | 1.1211          |
| 1.1063        | 0.89  | 300  | 1.0957          |
| 1.0724        | 1.19  | 400  | 1.0780          |
| 1.0489        | 1.49  | 500  | 1.0633          |
| 1.0359        | 1.78  | 600  | 1.0512          |
| 1.0228        | 2.08  | 700  | 1.0447          |
| 0.9924        | 2.38  | 800  | 1.0401          |
| 0.9906        | 2.68  | 900  | 1.0375          |
| 0.9863        | 2.97  | 1000 | 1.0369          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.2.0+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
