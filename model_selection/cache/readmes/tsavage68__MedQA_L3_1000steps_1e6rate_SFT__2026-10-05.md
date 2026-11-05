---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_SFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_SFT

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3666

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
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
| 1.0895        | 0.0489 | 50   | 0.8521          |
| 0.3865        | 0.0977 | 100  | 0.4119          |
| 0.4156        | 0.1466 | 150  | 0.3943          |
| 0.4302        | 0.1954 | 200  | 0.3870          |
| 0.3788        | 0.2443 | 250  | 0.3808          |
| 0.3964        | 0.2931 | 300  | 0.3773          |
| 0.3753        | 0.3420 | 350  | 0.3749          |
| 0.359         | 0.3908 | 400  | 0.3727          |
| 0.3874        | 0.4397 | 450  | 0.3711          |
| 0.3722        | 0.4885 | 500  | 0.3699          |
| 0.3615        | 0.5374 | 550  | 0.3686          |
| 0.3807        | 0.5862 | 600  | 0.3677          |
| 0.3643        | 0.6351 | 650  | 0.3673          |
| 0.3513        | 0.6839 | 700  | 0.3669          |
| 0.358         | 0.7328 | 750  | 0.3667          |
| 0.3648        | 0.7816 | 800  | 0.3666          |
| 0.3911        | 0.8305 | 850  | 0.3666          |
| 0.3475        | 0.8793 | 900  | 0.3666          |
| 0.3511        | 0.9282 | 950  | 0.3665          |
| 0.3673        | 0.9770 | 1000 | 0.3666          |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
