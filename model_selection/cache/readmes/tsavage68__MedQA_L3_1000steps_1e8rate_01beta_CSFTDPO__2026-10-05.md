---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e8rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e8rate_01beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6933
- Rewards/chosen: -0.0003
- Rewards/rejected: -0.0001
- Rewards/accuracies: 0.4923
- Rewards/margins: -0.0002
- Logps/rejected: -33.8557
- Logps/chosen: -31.3318
- Logits/rejected: -0.7327
- Logits/chosen: -0.7320

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-08
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- training_steps: 1000

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6929        | 0.0489 | 50   | 0.6932          | 0.0003         | 0.0004           | 0.4967             | -0.0001         | -33.8504       | -31.3255     | -0.7322         | -0.7315       |
| 0.6934        | 0.0977 | 100  | 0.6934          | 0.0004         | 0.0009           | 0.4703             | -0.0005         | -33.8457       | -31.3248     | -0.7326         | -0.7320       |
| 0.6924        | 0.1466 | 150  | 0.6931          | 0.0051         | 0.0049           | 0.5165             | 0.0002          | -33.8057       | -31.2774     | -0.7323         | -0.7316       |
| 0.6943        | 0.1954 | 200  | 0.6928          | 0.0019         | 0.0012           | 0.5099             | 0.0008          | -33.8433       | -31.3093     | -0.7327         | -0.7320       |
| 0.6931        | 0.2443 | 250  | 0.6930          | 0.0022         | 0.0018           | 0.5055             | 0.0004          | -33.8372       | -31.3066     | -0.7324         | -0.7317       |
| 0.6948        | 0.2931 | 300  | 0.6928          | 0.0049         | 0.0041           | 0.5275             | 0.0008          | -33.8138       | -31.2796     | -0.7324         | -0.7318       |
| 0.6952        | 0.3420 | 350  | 0.6932          | 0.0015         | 0.0015           | 0.4571             | 0.0000          | -33.8399       | -31.3133     | -0.7327         | -0.7321       |
| 0.694         | 0.3908 | 400  | 0.6932          | 0.0018         | 0.0019           | 0.4791             | -0.0002         | -33.8358       | -31.3110     | -0.7326         | -0.7319       |
| 0.6941        | 0.4397 | 450  | 0.6932          | -0.0010        | -0.0009          | 0.5033             | -0.0001         | -33.8636       | -31.3385     | -0.7322         | -0.7315       |
| 0.6919        | 0.4885 | 500  | 0.6933          | 0.0032         | 0.0034           | 0.4945             | -0.0002         | -33.8206       | -31.2967     | -0.7322         | -0.7316       |
| 0.6955        | 0.5374 | 550  | 0.6934          | 0.0013         | 0.0018           | 0.4989             | -0.0005         | -33.8370       | -31.3153     | -0.7324         | -0.7317       |
| 0.6915        | 0.5862 | 600  | 0.6931          | 0.0004         | 0.0003           | 0.5253             | 0.0001          | -33.8517       | -31.3242     | -0.7327         | -0.7320       |
| 0.6911        | 0.6351 | 650  | 0.6935          | 0.0005         | 0.0011           | 0.4703             | -0.0006         | -33.8438       | -31.3237     | -0.7325         | -0.7318       |
| 0.6921        | 0.6839 | 700  | 0.6930          | -0.0015        | -0.0019          | 0.5165             | 0.0004          | -33.8742       | -31.3438     | -0.7324         | -0.7318       |
| 0.6926        | 0.7328 | 750  | 0.6931          | 0.0012         | 0.0011           | 0.5187             | 0.0001          | -33.8440       | -31.3166     | -0.7328         | -0.7321       |
| 0.6927        | 0.7816 | 800  | 0.6930          | 0.0018         | 0.0014           | 0.5143             | 0.0004          | -33.8407       | -31.3102     | -0.7325         | -0.7318       |
| 0.6949        | 0.8305 | 850  | 0.6933          | -0.0003        | -0.0001          | 0.4901             | -0.0003         | -33.8555       | -31.3320     | -0.7327         | -0.7320       |
| 0.6942        | 0.8793 | 900  | 0.6933          | -0.0003        | -0.0001          | 0.4923             | -0.0002         | -33.8557       | -31.3318     | -0.7327         | -0.7320       |
| 0.691         | 0.9282 | 950  | 0.6933          | -0.0003        | -0.0001          | 0.4923             | -0.0002         | -33.8557       | -31.3318     | -0.7327         | -0.7320       |
| 0.6926        | 0.9770 | 1000 | 0.6933          | -0.0003        | -0.0001          | 0.4923             | -0.0002         | -33.8557       | -31.3318     | -0.7327         | -0.7320       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
