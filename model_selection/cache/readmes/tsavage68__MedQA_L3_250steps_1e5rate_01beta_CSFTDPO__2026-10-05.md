---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_250steps_1e5rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_250steps_1e5rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9785
- Rewards/chosen: -1.7641
- Rewards/rejected: -1.5433
- Rewards/accuracies: 0.4132
- Rewards/margins: -0.2209
- Logps/rejected: -49.2875
- Logps/chosen: -48.9697
- Logits/rejected: -1.1405
- Logits/chosen: -1.1409

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
- training_steps: 250

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.671         | 0.0489 | 50   | 1.6433          | -6.4141        | -6.3515          | 0.4747             | -0.0626         | -97.3700       | -95.4696     | -0.6453         | -0.6453       |
| 1.0504        | 0.0977 | 100  | 0.8270          | -1.6657        | -1.8409          | 0.5385             | 0.1752          | -52.2642       | -47.9860     | -1.0550         | -1.0545       |
| 1.3146        | 0.1466 | 150  | 1.0584          | -2.1772        | -1.8983          | 0.4110             | -0.2789         | -52.8378       | -53.1002     | -1.6449         | -1.6452       |
| 1.2122        | 0.1954 | 200  | 1.0261          | -1.8796        | -1.6260          | 0.4066             | -0.2536         | -50.1151       | -50.1247     | -1.1724         | -1.1728       |
| 0.929         | 0.2443 | 250  | 0.9785          | -1.7641        | -1.5433          | 0.4132             | -0.2209         | -49.2875       | -48.9697     | -1.1405         | -1.1409       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
