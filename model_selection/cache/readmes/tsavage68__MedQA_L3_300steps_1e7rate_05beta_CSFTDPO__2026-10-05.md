---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_300steps_1e7rate_05beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_300steps_1e7rate_05beta_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6479
- Rewards/chosen: 0.2870
- Rewards/rejected: 0.1538
- Rewards/accuracies: 0.6374
- Rewards/margins: 0.1332
- Logps/rejected: -21.0089
- Logps/chosen: -17.6487
- Logits/rejected: -0.9327
- Logits/chosen: -0.9321

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
- training_steps: 300

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.7034        | 0.0489 | 50   | 0.6908          | 0.0092         | 0.0030           | 0.5187             | 0.0061          | -21.3104       | -18.2043     | -0.9262         | -0.9257       |
| 0.6841        | 0.0977 | 100  | 0.6705          | 0.1777         | 0.1221           | 0.6088             | 0.0556          | -21.0723       | -17.8673     | -0.9278         | -0.9273       |
| 0.6636        | 0.1466 | 150  | 0.6536          | 0.2698         | 0.1543           | 0.6505             | 0.1155          | -21.0080       | -17.6830     | -0.9307         | -0.9302       |
| 0.6483        | 0.1954 | 200  | 0.6488          | 0.2862         | 0.1570           | 0.6330             | 0.1291          | -21.0025       | -17.6503     | -0.9322         | -0.9317       |
| 0.683         | 0.2443 | 250  | 0.6472          | 0.2913         | 0.1569           | 0.6396             | 0.1344          | -21.0027       | -17.6400     | -0.9325         | -0.9320       |
| 0.6269        | 0.2931 | 300  | 0.6479          | 0.2870         | 0.1538           | 0.6374             | 0.1332          | -21.0089       | -17.6487     | -0.9327         | -0.9321       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
