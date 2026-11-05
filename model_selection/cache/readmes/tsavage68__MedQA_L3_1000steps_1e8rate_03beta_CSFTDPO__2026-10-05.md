---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e8rate_03beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e8rate_03beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6947
- Rewards/chosen: 0.0002
- Rewards/rejected: 0.0027
- Rewards/accuracies: 0.4615
- Rewards/margins: -0.0026
- Logps/rejected: -33.8457
- Logps/chosen: -31.3279
- Logits/rejected: -0.7320
- Logits/chosen: -0.7314

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
| 0.6937        | 0.0489 | 50   | 0.6939          | -0.0056        | -0.0047          | 0.4769             | -0.0009         | -33.8705       | -31.3473     | -0.7322         | -0.7315       |
| 0.6972        | 0.0977 | 100  | 0.6930          | -0.0029        | -0.0036          | 0.5055             | 0.0007          | -33.8668       | -31.3383     | -0.7322         | -0.7316       |
| 0.6918        | 0.1466 | 150  | 0.6933          | 0.0057         | 0.0055           | 0.4901             | 0.0002          | -33.8364       | -31.3096     | -0.7321         | -0.7314       |
| 0.6951        | 0.1954 | 200  | 0.6941          | -0.0012        | 0.0002           | 0.4769             | -0.0014         | -33.8541       | -31.3324     | -0.7320         | -0.7313       |
| 0.6926        | 0.2443 | 250  | 0.6930          | 0.0029         | 0.0022           | 0.4857             | 0.0006          | -33.8474       | -31.3190     | -0.7319         | -0.7312       |
| 0.6947        | 0.2931 | 300  | 0.6929          | -0.0006        | -0.0016          | 0.4967             | 0.0010          | -33.8603       | -31.3307     | -0.7323         | -0.7316       |
| 0.6987        | 0.3420 | 350  | 0.6939          | 0.0041         | 0.0052           | 0.5121             | -0.0010         | -33.8377       | -31.3148     | -0.7324         | -0.7317       |
| 0.695         | 0.3908 | 400  | 0.6929          | 0.0111         | 0.0101           | 0.4967             | 0.0010          | -33.8212       | -31.2917     | -0.7321         | -0.7315       |
| 0.6953        | 0.4397 | 450  | 0.6941          | 0.0051         | 0.0066           | 0.4857             | -0.0015         | -33.8330       | -31.3115     | -0.7327         | -0.7320       |
| 0.6939        | 0.4885 | 500  | 0.6947          | 0.0022         | 0.0048           | 0.4637             | -0.0027         | -33.8387       | -31.3213     | -0.7325         | -0.7318       |
| 0.6982        | 0.5374 | 550  | 0.6922          | 0.0071         | 0.0047           | 0.5121             | 0.0023          | -33.8391       | -31.3050     | -0.7325         | -0.7318       |
| 0.6835        | 0.5862 | 600  | 0.6939          | 0.0064         | 0.0074           | 0.4945             | -0.0010         | -33.8303       | -31.3073     | -0.7321         | -0.7314       |
| 0.6868        | 0.6351 | 650  | 0.6937          | -0.0034        | -0.0029          | 0.4989             | -0.0006         | -33.8644       | -31.3400     | -0.7323         | -0.7316       |
| 0.6882        | 0.6839 | 700  | 0.6939          | -0.0024        | -0.0013          | 0.4725             | -0.0011         | -33.8593       | -31.3366     | -0.7323         | -0.7317       |
| 0.6947        | 0.7328 | 750  | 0.6936          | 0.0031         | 0.0035           | 0.5077             | -0.0004         | -33.8431       | -31.3183     | -0.7321         | -0.7314       |
| 0.6968        | 0.7816 | 800  | 0.6947          | -0.0034        | -0.0007          | 0.4637             | -0.0027         | -33.8571       | -31.3399     | -0.7319         | -0.7313       |
| 0.6919        | 0.8305 | 850  | 0.6947          | 0.0001         | 0.0028           | 0.4593             | -0.0027         | -33.8456       | -31.3283     | -0.7320         | -0.7314       |
| 0.6962        | 0.8793 | 900  | 0.6947          | 0.0002         | 0.0027           | 0.4615             | -0.0026         | -33.8457       | -31.3279     | -0.7320         | -0.7314       |
| 0.6866        | 0.9282 | 950  | 0.6947          | 0.0002         | 0.0027           | 0.4615             | -0.0026         | -33.8457       | -31.3279     | -0.7320         | -0.7314       |
| 0.6919        | 0.9770 | 1000 | 0.6947          | 0.0002         | 0.0027           | 0.4615             | -0.0026         | -33.8457       | -31.3279     | -0.7320         | -0.7314       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
