---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_250steps_1e6rate_01beat_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_250steps_1e6rate_01beat_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4710
- Rewards/chosen: -0.7540
- Rewards/rejected: -1.6509
- Rewards/accuracies: 0.7758
- Rewards/margins: 0.8969
- Logps/rejected: -37.8254
- Logps/chosen: -25.7624
- Logits/rejected: -1.1604
- Logits/chosen: -1.1585

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
- training_steps: 250

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.695         | 0.0489 | 50   | 0.6713          | 0.0342         | -0.0142          | 0.6615             | 0.0484          | -21.4583       | -17.8807     | -0.9400         | -0.9395       |
| 0.6187        | 0.0977 | 100  | 0.5915          | -0.1174        | -0.4200          | 0.7121             | 0.3027          | -25.5168       | -19.3963     | -1.0412         | -1.0403       |
| 0.559         | 0.1466 | 150  | 0.5116          | -0.4993        | -1.1517          | 0.7429             | 0.6524          | -32.8335       | -23.2153     | -1.1115         | -1.1101       |
| 0.4654        | 0.1954 | 200  | 0.4732          | -0.7696        | -1.6630          | 0.7780             | 0.8934          | -37.9465       | -25.9187     | -1.1618         | -1.1598       |
| 0.4766        | 0.2443 | 250  | 0.4710          | -0.7540        | -1.6509          | 0.7758             | 0.8969          | -37.8254       | -25.7624     | -1.1604         | -1.1585       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
