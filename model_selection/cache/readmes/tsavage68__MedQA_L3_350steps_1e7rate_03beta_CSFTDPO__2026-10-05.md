---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_350steps_1e7rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_350steps_1e7rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6516
- Rewards/chosen: 0.2738
- Rewards/rejected: 0.1790
- Rewards/accuracies: 0.7099
- Rewards/margins: 0.0948
- Logps/rejected: -33.2582
- Logps/chosen: -30.4158
- Logits/rejected: -0.7313
- Logits/chosen: -0.7305

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
- training_steps: 350

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6925        | 0.0489 | 50   | 0.6930          | -0.0016        | -0.0023          | 0.5011             | 0.0007          | -33.8624       | -31.3338     | -0.7320         | -0.7314       |
| 0.6841        | 0.0977 | 100  | 0.6807          | 0.2459         | 0.2195           | 0.6549             | 0.0264          | -33.1233       | -30.5088     | -0.7330         | -0.7323       |
| 0.6524        | 0.1466 | 150  | 0.6658          | 0.3522         | 0.2898           | 0.6703             | 0.0624          | -32.8887       | -30.1544     | -0.7315         | -0.7308       |
| 0.631         | 0.1954 | 200  | 0.6545          | 0.1829         | 0.0948           | 0.6923             | 0.0881          | -33.5389       | -30.7188     | -0.7310         | -0.7303       |
| 0.6675        | 0.2443 | 250  | 0.6520          | 0.2481         | 0.1544           | 0.7121             | 0.0938          | -33.3403       | -30.5014     | -0.7309         | -0.7301       |
| 0.6479        | 0.2931 | 300  | 0.6509          | 0.2738         | 0.1773           | 0.7099             | 0.0966          | -33.2640       | -30.4157     | -0.7310         | -0.7303       |
| 0.6583        | 0.3420 | 350  | 0.6516          | 0.2738         | 0.1790           | 0.7099             | 0.0948          | -33.2582       | -30.4158     | -0.7313         | -0.7305       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
