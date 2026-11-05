---
license: llama2
base_model: epfl-llm/meditron-7b
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: 300STEPS_5e7rate_Meditron_7B_SFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 300STEPS_5e7rate_Meditron_7B_SFT

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3127

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 300

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.2096        | 0.1   | 50   | 1.1770          |
| 0.7177        | 0.2   | 100  | 0.6260          |
| 0.3357        | 0.29  | 150  | 0.3221          |
| 0.3191        | 0.39  | 200  | 0.3142          |
| 0.3195        | 0.49  | 250  | 0.3128          |
| 0.3195        | 0.59  | 300  | 0.3127          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.0+cu117
- Datasets 2.17.0
- Tokenizers 0.15.1
