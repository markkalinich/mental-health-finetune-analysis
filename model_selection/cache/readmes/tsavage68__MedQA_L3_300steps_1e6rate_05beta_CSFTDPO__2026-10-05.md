---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_300steps_1e6rate_05beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_300steps_1e6rate_05beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5731
- Rewards/chosen: 5.8136
- Rewards/rejected: 3.5872
- Rewards/accuracies: 0.7692
- Rewards/margins: 2.2264
- Logps/rejected: -26.6804
- Logps/chosen: -19.7013
- Logits/rejected: -0.8355
- Logits/chosen: -0.8339

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
- training_steps: 300

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6909        | 0.0489 | 50   | 0.6059          | -0.4307        | -0.6542          | 0.7538             | 0.2235          | -35.1631       | -32.1898     | -0.7254         | -0.7246       |
| 0.4343        | 0.0977 | 100  | 0.7202          | 6.9486         | 5.2431           | 0.6989             | 1.7054          | -23.3686       | -17.4314     | -0.7816         | -0.7804       |
| 0.6114        | 0.1466 | 150  | 0.6428          | 3.8385         | 1.9433           | 0.7407             | 1.8951          | -29.9682       | -23.6516     | -0.8244         | -0.8232       |
| 0.3522        | 0.1954 | 200  | 0.5948          | 5.1038         | 2.7837           | 0.7604             | 2.3201          | -28.2874       | -21.1208     | -0.8383         | -0.8367       |
| 0.3837        | 0.2443 | 250  | 0.5746          | 5.7825         | 3.5643           | 0.7692             | 2.2182          | -26.7263       | -19.7636     | -0.8356         | -0.8340       |
| 0.3658        | 0.2931 | 300  | 0.5731          | 5.8136         | 3.5872           | 0.7692             | 2.2264          | -26.6804       | -19.7013     | -0.8355         | -0.8339       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
