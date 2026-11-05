---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e5rate_SFT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e5rate_SFT

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3681

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
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
| 0.4577        | 0.0489 | 50   | 0.5024          |
| 0.4969        | 0.0977 | 100  | 0.4876          |
| 0.4689        | 0.1466 | 150  | 0.4380          |
| 0.4891        | 0.1954 | 200  | 0.4313          |
| 0.424         | 0.2443 | 250  | 0.4275          |
| 0.4408        | 0.2931 | 300  | 0.4208          |
| 0.4124        | 0.3420 | 350  | 0.4160          |
| 0.4012        | 0.3908 | 400  | 0.4113          |
| 0.4305        | 0.4397 | 450  | 0.4285          |
| 0.4031        | 0.4885 | 500  | 0.3974          |
| 0.3863        | 0.5374 | 550  | 0.3916          |
| 0.3981        | 0.5862 | 600  | 0.3861          |
| 0.3705        | 0.6351 | 650  | 0.3810          |
| 0.3591        | 0.6839 | 700  | 0.3760          |
| 0.3642        | 0.7328 | 750  | 0.3722          |
| 0.3712        | 0.7816 | 800  | 0.3699          |
| 0.3893        | 0.8305 | 850  | 0.3686          |
| 0.3512        | 0.8793 | 900  | 0.3682          |
| 0.3546        | 0.9282 | 950  | 0.3681          |
| 0.3736        | 0.9770 | 1000 | 0.3681          |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
