---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: MedQA_L3_500steps_1e7rate_SFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_500steps_1e7rate_SFT

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3157

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-07
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 500

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.774         | 0.0489 | 50   | 1.7867          |
| 1.7099        | 0.0977 | 100  | 1.6989          |
| 1.5892        | 0.1466 | 150  | 1.5687          |
| 1.4868        | 0.1954 | 200  | 1.4685          |
| 1.4001        | 0.2443 | 250  | 1.3929          |
| 1.3564        | 0.2931 | 300  | 1.3457          |
| 1.3261        | 0.3420 | 350  | 1.3226          |
| 1.3101        | 0.3908 | 400  | 1.3163          |
| 1.3032        | 0.4397 | 450  | 1.3159          |
| 1.3189        | 0.4885 | 500  | 1.3157          |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
