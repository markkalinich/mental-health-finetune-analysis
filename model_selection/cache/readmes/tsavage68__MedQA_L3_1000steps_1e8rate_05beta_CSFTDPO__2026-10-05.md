---
license: llama3
base_model: tsavage68/MedQA_L3_1000steps_1e6rate_SFT
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_1000steps_1e8rate_05beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_1000steps_1e8rate_05beta_CSFTDPO

This model is a fine-tuned version of [tsavage68/MedQA_L3_1000steps_1e6rate_SFT](https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e6rate_SFT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6949
- Rewards/chosen: 0.0221
- Rewards/rejected: 0.0244
- Rewards/accuracies: 0.4725
- Rewards/margins: -0.0023
- Logps/rejected: -33.8059
- Logps/chosen: -31.2843
- Logits/rejected: -0.7321
- Logits/chosen: -0.7315

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
| 0.6981        | 0.0489 | 50   | 0.6908          | 0.0076         | 0.0017           | 0.5473             | 0.0059          | -33.8515       | -31.3133     | -0.7324         | -0.7317       |
| 0.6964        | 0.0977 | 100  | 0.6933          | 0.0126         | 0.0116           | 0.5077             | 0.0010          | -33.8316       | -31.3032     | -0.7322         | -0.7315       |
| 0.6942        | 0.1466 | 150  | 0.6946          | 0.0165         | 0.0180           | 0.5011             | -0.0015         | -33.8188       | -31.2955     | -0.7321         | -0.7314       |
| 0.6897        | 0.1954 | 200  | 0.6927          | -0.0100        | -0.0122          | 0.5055             | 0.0022          | -33.8792       | -31.3486     | -0.7319         | -0.7312       |
| 0.6908        | 0.2443 | 250  | 0.6916          | 0.0078         | 0.0034           | 0.5385             | 0.0044          | -33.8481       | -31.3129     | -0.7318         | -0.7311       |
| 0.6912        | 0.2931 | 300  | 0.6931          | -0.0060        | -0.0072          | 0.4923             | 0.0012          | -33.8693       | -31.3405     | -0.7322         | -0.7315       |
| 0.7003        | 0.3420 | 350  | 0.6949          | -0.0119        | -0.0096          | 0.4725             | -0.0024         | -33.8740       | -31.3524     | -0.7323         | -0.7316       |
| 0.6967        | 0.3908 | 400  | 0.6957          | -0.0055        | -0.0019          | 0.4791             | -0.0036         | -33.8586       | -31.3395     | -0.7320         | -0.7313       |
| 0.6921        | 0.4397 | 450  | 0.6961          | -0.0030        | 0.0015           | 0.4725             | -0.0045         | -33.8518       | -31.3345     | -0.7321         | -0.7315       |
| 0.6949        | 0.4885 | 500  | 0.6941          | 0.0163         | 0.0170           | 0.4879             | -0.0007         | -33.8208       | -31.2958     | -0.7325         | -0.7318       |
| 0.7052        | 0.5374 | 550  | 0.6925          | 0.0081         | 0.0056           | 0.5187             | 0.0025          | -33.8437       | -31.3123     | -0.7320         | -0.7314       |
| 0.6881        | 0.5862 | 600  | 0.6944          | 0.0116         | 0.0129           | 0.5077             | -0.0013         | -33.8290       | -31.3053     | -0.7321         | -0.7315       |
| 0.6888        | 0.6351 | 650  | 0.6917          | 0.0113         | 0.0074           | 0.5121             | 0.0040          | -33.8401       | -31.3058     | -0.7326         | -0.7319       |
| 0.6826        | 0.6839 | 700  | 0.6955          | -0.0009        | 0.0026           | 0.4659             | -0.0035         | -33.8497       | -31.3303     | -0.7323         | -0.7316       |
| 0.6938        | 0.7328 | 750  | 0.6928          | 0.0252         | 0.0232           | 0.5033             | 0.0020          | -33.8084       | -31.2782     | -0.7324         | -0.7317       |
| 0.6971        | 0.7816 | 800  | 0.6939          | 0.0263         | 0.0265           | 0.4923             | -0.0001         | -33.8019       | -31.2758     | -0.7323         | -0.7316       |
| 0.6954        | 0.8305 | 850  | 0.6948          | 0.0223         | 0.0244           | 0.4747             | -0.0021         | -33.8060       | -31.2840     | -0.7321         | -0.7315       |
| 0.6983        | 0.8793 | 900  | 0.6949          | 0.0221         | 0.0244           | 0.4725             | -0.0023         | -33.8059       | -31.2843     | -0.7321         | -0.7315       |
| 0.6832        | 0.9282 | 950  | 0.6949          | 0.0221         | 0.0244           | 0.4725             | -0.0023         | -33.8059       | -31.2843     | -0.7321         | -0.7315       |
| 0.6916        | 0.9770 | 1000 | 0.6949          | 0.0221         | 0.0244           | 0.4725             | -0.0023         | -33.8059       | -31.2843     | -0.7321         | -0.7315       |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
