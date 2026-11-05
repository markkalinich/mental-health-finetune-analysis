---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e6rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e6rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4888
- Rewards/chosen: 3.1508
- Rewards/rejected: 1.3776
- Rewards/accuracies: 0.7868
- Rewards/margins: 1.7732
- Logps/rejected: -29.2628
- Logps/chosen: -20.8258
- Logits/rejected: -0.8475
- Logits/chosen: -0.8455

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
| 0.685         | 0.0489 | 50   | 0.6334          | -0.7936        | -0.9359          | 0.7363             | 0.1423          | -36.9746       | -33.9739     | -0.7278         | -0.7271       |
| 0.4052        | 0.0977 | 100  | 0.6106          | 3.7995         | 2.4858           | 0.6945             | 1.3137          | -25.5688       | -18.6634     | -0.7922         | -0.7909       |
| 0.6421        | 0.1466 | 150  | 0.5225          | 2.5850         | 1.3506           | 0.7538             | 1.2344          | -29.3529       | -22.7119     | -0.8369         | -0.8356       |
| 0.3501        | 0.1954 | 200  | 0.5243          | 2.6639         | 0.8481           | 0.7626             | 1.8159          | -31.0279       | -22.4487     | -0.8442         | -0.8422       |
| 0.3618        | 0.2443 | 250  | 0.4899          | 3.1411         | 1.3754           | 0.7802             | 1.7657          | -29.2702       | -20.8582     | -0.8474         | -0.8454       |
| 0.3181        | 0.2931 | 300  | 0.4888          | 3.1508         | 1.3776           | 0.7868             | 1.7732          | -29.2628       | -20.8258     | -0.8475         | -0.8455       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
