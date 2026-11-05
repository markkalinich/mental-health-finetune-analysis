---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_400steps_1e6rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_400steps_1e6rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4906
- Rewards/chosen: 3.1291
- Rewards/rejected: 0.9306
- Rewards/accuracies: 0.7846
- Rewards/margins: 2.1985
- Logps/rejected: -30.7529
- Logps/chosen: -20.8982
- Logits/rejected: -0.8390
- Logits/chosen: -0.8370

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
- training_steps: 400

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.685         | 0.0489 | 50   | 0.6334          | -0.7936        | -0.9359          | 0.7363             | 0.1423          | -36.9746       | -33.9739     | -0.7278         | -0.7271       |
| 0.4052        | 0.0977 | 100  | 0.6106          | 3.7995         | 2.4858           | 0.6945             | 1.3137          | -25.5688       | -18.6634     | -0.7922         | -0.7909       |
| 0.5527        | 0.1466 | 150  | 0.5749          | 3.2572         | 1.9474           | 0.7319             | 1.3099          | -27.3637       | -20.4711     | -0.8427         | -0.8414       |
| 0.3441        | 0.1954 | 200  | 0.5174          | 2.5190         | 0.7455           | 0.7582             | 1.7735          | -31.3700       | -22.9318     | -0.8395         | -0.8376       |
| 0.3888        | 0.2443 | 250  | 0.4758          | 3.2338         | 1.3417           | 0.7956             | 1.8921          | -29.3826       | -20.5492     | -0.8342         | -0.8323       |
| 0.2873        | 0.2931 | 300  | 0.4927          | 3.0141         | 0.8326           | 0.7912             | 2.1815          | -31.0794       | -21.2815     | -0.8318         | -0.8298       |
| 0.4877        | 0.3420 | 350  | 0.4903          | 3.1277         | 0.9322           | 0.7824             | 2.1956          | -30.7476       | -20.9027     | -0.8388         | -0.8368       |
| 0.4649        | 0.3908 | 400  | 0.4906          | 3.1291         | 0.9306           | 0.7846             | 2.1985          | -30.7529       | -20.8982     | -0.8390         | -0.8370       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
