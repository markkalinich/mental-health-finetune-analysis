---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_450steps_1e7rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_450steps_1e7rate_03beta_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6479
- Rewards/chosen: 0.1876
- Rewards/rejected: 0.0690
- Rewards/accuracies: 0.6637
- Rewards/margins: 0.1186
- Logps/rejected: -21.0864
- Logps/chosen: -17.5973
- Logits/rejected: -0.9362
- Logits/chosen: -0.9357

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
- training_steps: 450

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6938        | 0.0489 | 50   | 0.6934          | 0.0041         | 0.0042           | 0.5099             | -0.0000         | -21.3026       | -18.2088     | -0.9262         | -0.9257       |
| 0.6807        | 0.0977 | 100  | 0.6781          | 0.1130         | 0.0788           | 0.6110             | 0.0343          | -21.0540       | -17.8459     | -0.9280         | -0.9275       |
| 0.6689        | 0.1466 | 150  | 0.6622          | 0.1706         | 0.0922           | 0.6286             | 0.0784          | -21.0091       | -17.6540     | -0.9313         | -0.9308       |
| 0.6589        | 0.1954 | 200  | 0.6569          | 0.1748         | 0.0827           | 0.6462             | 0.0921          | -21.0408       | -17.6401     | -0.9339         | -0.9334       |
| 0.6798        | 0.2443 | 250  | 0.6507          | 0.1854         | 0.0751           | 0.6505             | 0.1103          | -21.0663       | -17.6047     | -0.9352         | -0.9347       |
| 0.6402        | 0.2931 | 300  | 0.6482          | 0.1927         | 0.0761           | 0.6725             | 0.1166          | -21.0627       | -17.5802     | -0.9358         | -0.9352       |
| 0.7088        | 0.3420 | 350  | 0.6481          | 0.1883         | 0.0698           | 0.6637             | 0.1185          | -21.0838       | -17.5951     | -0.9357         | -0.9352       |
| 0.6301        | 0.3908 | 400  | 0.6487          | 0.1878         | 0.0712           | 0.6549             | 0.1166          | -21.0792       | -17.5965     | -0.9361         | -0.9356       |
| 0.6454        | 0.4397 | 450  | 0.6479          | 0.1876         | 0.0690           | 0.6637             | 0.1186          | -21.0864       | -17.5973     | -0.9362         | -0.9357       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
