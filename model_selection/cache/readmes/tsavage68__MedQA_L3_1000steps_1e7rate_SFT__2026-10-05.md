---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e7rate_SFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e7rate_SFT

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7486

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
- training_steps: 1000

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.774         | 0.0489 | 50   | 1.7867          |
| 1.7099        | 0.0977 | 100  | 1.6989          |
| 1.5873        | 0.1466 | 150  | 1.5668          |
| 1.4721        | 0.1954 | 200  | 1.4501          |
| 1.3469        | 0.2443 | 250  | 1.3336          |
| 1.2381        | 0.2931 | 300  | 1.2152          |
| 1.1195        | 0.3420 | 350  | 1.1046          |
| 1.0094        | 0.3908 | 400  | 1.0086          |
| 0.9372        | 0.4397 | 450  | 0.9280          |
| 0.8756        | 0.4885 | 500  | 0.8669          |
| 0.8221        | 0.5374 | 550  | 0.8219          |
| 0.8048        | 0.5862 | 600  | 0.7900          |
| 0.7759        | 0.6351 | 650  | 0.7691          |
| 0.7465        | 0.6839 | 700  | 0.7568          |
| 0.7426        | 0.7328 | 750  | 0.7506          |
| 0.7462        | 0.7816 | 800  | 0.7488          |
| 0.7764        | 0.8305 | 850  | 0.7486          |
| 0.7327        | 0.8793 | 900  | 0.7486          |
| 0.7316        | 0.9282 | 950  | 0.7486          |
| 0.7478        | 0.9770 | 1000 | 0.7486          |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
