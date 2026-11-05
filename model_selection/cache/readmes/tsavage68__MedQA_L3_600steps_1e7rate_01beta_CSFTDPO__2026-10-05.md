---
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- trl
- dpo
- generated_from_trainer
model-index:
- name: MedQA_L3_600steps_1e7rate_01beta_CSFTDPO
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MedQA_L3_600steps_1e7rate_01beta_CSFTDPO

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6692
- Rewards/chosen: 0.0482
- Rewards/rejected: -0.0053
- Rewards/accuracies: 0.6681
- Rewards/margins: 0.0535
- Logps/rejected: -21.3695
- Logps/chosen: -17.7404
- Logits/rejected: -0.9398
- Logits/chosen: -0.9393

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
- training_steps: 600

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.6951        | 0.0489 | 50   | 0.6935          | 0.0003         | 0.0009           | 0.4901             | -0.0006         | -21.3079       | -18.2196     | -0.9258         | -0.9253       |
| 0.6892        | 0.0977 | 100  | 0.6881          | 0.0374         | 0.0268           | 0.6044             | 0.0106          | -21.0482       | -17.8488     | -0.9281         | -0.9276       |
| 0.6801        | 0.1466 | 150  | 0.6794          | 0.0588         | 0.0292           | 0.6418             | 0.0296          | -21.0241       | -17.6343     | -0.9314         | -0.9309       |
| 0.6807        | 0.1954 | 200  | 0.6767          | 0.0584         | 0.0227           | 0.6549             | 0.0358          | -21.0897       | -17.6383     | -0.9345         | -0.9339       |
| 0.6829        | 0.2443 | 250  | 0.6726          | 0.0560         | 0.0106           | 0.6571             | 0.0454          | -21.2109       | -17.6631     | -0.9367         | -0.9362       |
| 0.6656        | 0.2931 | 300  | 0.6715          | 0.0540         | 0.0059           | 0.6505             | 0.0481          | -21.2575       | -17.6830     | -0.9382         | -0.9376       |
| 0.6955        | 0.3420 | 350  | 0.6697          | 0.0524         | 0.0002           | 0.6571             | 0.0522          | -21.3145       | -17.6986     | -0.9384         | -0.9378       |
| 0.6605        | 0.3908 | 400  | 0.6697          | 0.0493         | -0.0031          | 0.6505             | 0.0524          | -21.3476       | -17.7294     | -0.9393         | -0.9388       |
| 0.6718        | 0.4397 | 450  | 0.6689          | 0.0495         | -0.0047          | 0.6527             | 0.0541          | -21.3631       | -17.7279     | -0.9396         | -0.9390       |
| 0.6734        | 0.4885 | 500  | 0.6687          | 0.0486         | -0.0059          | 0.6505             | 0.0545          | -21.3751       | -17.7362     | -0.9397         | -0.9392       |
| 0.6525        | 0.5374 | 550  | 0.6691          | 0.0482         | -0.0056          | 0.6615             | 0.0537          | -21.3720       | -17.7410     | -0.9398         | -0.9393       |
| 0.6637        | 0.5862 | 600  | 0.6692          | 0.0482         | -0.0053          | 0.6681             | 0.0535          | -21.3695       | -17.7404     | -0.9398         | -0.9393       |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.0.0+cu117
- Datasets 2.19.1
- Tokenizers 0.19.1
