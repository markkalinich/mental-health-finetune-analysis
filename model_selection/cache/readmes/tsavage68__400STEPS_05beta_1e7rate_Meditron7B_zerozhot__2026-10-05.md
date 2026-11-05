---
license: llama2
base_model: epfl-llm/meditron-7b
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: 400STEPS_05beta_1e7rate_Meditron7B
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 400STEPS_05beta_1e7rate_Meditron7B

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6864
- Rewards/chosen: 0.0004
- Rewards/rejected: -0.0144
- Rewards/accuracies: 0.4945
- Rewards/margins: 0.0148
- Logps/rejected: -27.8226
- Logps/chosen: -26.4806
- Logits/rejected: -0.6110
- Logits/chosen: -0.6109

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
- train_batch_size: 4
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 400

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6941        | 0.1   | 50   | 0.6931          | -0.0003        | -0.0011          | 0.4044             | 0.0008          | -27.7959       | -26.4820     | -0.6106         | -0.6104       |
| 0.6927        | 0.2   | 100  | 0.6912          | -0.0047        | -0.0093          | 0.4769             | 0.0046          | -27.8123       | -26.4908     | -0.6105         | -0.6104       |
| 0.6838        | 0.29  | 150  | 0.6896          | -0.0023        | -0.0105          | 0.5077             | 0.0082          | -27.8146       | -26.4860     | -0.6101         | -0.6100       |
| 0.6906        | 0.39  | 200  | 0.6886          | -0.0007        | -0.0107          | 0.4989             | 0.0100          | -27.8151       | -26.4828     | -0.6109         | -0.6108       |
| 0.6789        | 0.49  | 250  | 0.6877          | -0.0035        | -0.0154          | 0.5121             | 0.0119          | -27.8245       | -26.4884     | -0.6111         | -0.6110       |
| 0.6853        | 0.59  | 300  | 0.6852          | 0.0012         | -0.0160          | 0.5297             | 0.0172          | -27.8257       | -26.4791     | -0.6112         | -0.6111       |
| 0.6805        | 0.68  | 350  | 0.6877          | -0.0039        | -0.0162          | 0.4725             | 0.0122          | -27.8260       | -26.4893     | -0.6112         | -0.6110       |
| 0.6936        | 0.78  | 400  | 0.6864          | 0.0004         | -0.0144          | 0.4945             | 0.0148          | -27.8226       | -26.4806     | -0.6110         | -0.6109       |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.0+cu117
- Datasets 2.17.0
- Tokenizers 0.15.1
