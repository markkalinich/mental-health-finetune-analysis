---
license: llama2
base_model: epfl-llm/meditron-7b
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: 400STEPS_5e7rate_03beta_DPO_Meditron7B
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 400STEPS_5e7rate_03beta_DPO_Meditron7B

This model is a fine-tuned version of [epfl-llm/meditron-7b](https://huggingface.co/epfl-llm/meditron-7b) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6439
- Rewards/chosen: -0.0166
- Rewards/rejected: -0.1472
- Rewards/accuracies: 0.5714
- Rewards/margins: 0.1306
- Logps/rejected: -28.2845
- Logps/chosen: -26.5367
- Logits/rejected: -0.6342
- Logits/chosen: -0.6341

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
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
| 0.6896        | 0.1   | 50   | 0.6916          | 0.0067         | 0.0033           | 0.4637             | 0.0034          | -27.7828       | -26.4590     | -0.6113         | -0.6111       |
| 0.6783        | 0.2   | 100  | 0.6771          | -0.0693        | -0.1071          | 0.5319             | 0.0378          | -28.1508       | -26.7125     | -0.6173         | -0.6171       |
| 0.6697        | 0.29  | 150  | 0.6571          | -0.0107        | -0.1001          | 0.5626             | 0.0893          | -28.1273       | -26.5172     | -0.6171         | -0.6170       |
| 0.6463        | 0.39  | 200  | 0.6496          | 0.0037         | -0.1067          | 0.5692             | 0.1104          | -28.1493       | -26.4691     | -0.6288         | -0.6286       |
| 0.6124        | 0.49  | 250  | 0.6449          | -0.0073        | -0.1329          | 0.5648             | 0.1257          | -28.2368       | -26.5056     | -0.6318         | -0.6317       |
| 0.641         | 0.59  | 300  | 0.6440          | -0.0156        | -0.1460          | 0.5758             | 0.1304          | -28.2803       | -26.5333     | -0.6340         | -0.6339       |
| 0.643         | 0.68  | 350  | 0.6430          | -0.0150        | -0.1479          | 0.5780             | 0.1328          | -28.2866       | -26.5315     | -0.6343         | -0.6341       |
| 0.6632        | 0.78  | 400  | 0.6439          | -0.0166        | -0.1472          | 0.5714             | 0.1306          | -28.2845       | -26.5367     | -0.6342         | -0.6341       |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.0+cu117
- Datasets 2.17.0
- Tokenizers 0.15.1
