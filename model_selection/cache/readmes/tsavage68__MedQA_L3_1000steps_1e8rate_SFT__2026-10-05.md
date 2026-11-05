---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e8rate_SFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e8rate_SFT

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7989

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-08
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 1000

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.783         | 0.0489 | 50   | 1.7997          |
| 1.7968        | 0.0977 | 100  | 1.7995          |
| 1.8022        | 0.1466 | 150  | 1.7997          |
| 1.7968        | 0.1954 | 200  | 1.7993          |
| 1.7998        | 0.2443 | 250  | 1.7989          |
| 1.7963        | 0.2931 | 300  | 1.7989          |
| 1.7977        | 0.3420 | 350  | 1.7992          |
| 1.7971        | 0.3908 | 400  | 1.7991          |
| 1.7697        | 0.4397 | 450  | 1.7990          |
| 1.8021        | 0.4885 | 500  | 1.7990          |
| 1.7897        | 0.5374 | 550  | 1.7988          |
| 1.7817        | 0.5862 | 600  | 1.7988          |
| 1.812         | 0.6351 | 650  | 1.7987          |
| 1.7939        | 0.6839 | 700  | 1.7989          |
| 1.815         | 0.7328 | 750  | 1.7989          |
| 1.7991        | 0.7816 | 800  | 1.7989          |
| 1.8164        | 0.8305 | 850  | 1.7989          |
| 1.8062        | 0.8793 | 900  | 1.7989          |
| 1.8048        | 0.9282 | 950  | 1.7989          |
| 1.8103        | 0.9770 | 1000 | 1.7989          |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
