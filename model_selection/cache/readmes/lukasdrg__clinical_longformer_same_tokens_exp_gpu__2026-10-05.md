---
license: apache-2.0
base_model: allenai/longformer-base-4096
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_exp_gpu
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_exp_gpu

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1468

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.0528        | 0.07  | 65   | 2.6194          |
| 3.2272        | 0.14  | 130  | 2.4923          |
| 2.8624        | 0.21  | 195  | 2.3739          |
| 2.552         | 0.29  | 260  | 2.2678          |
| 2.7232        | 0.36  | 325  | 2.1829          |
| 2.361         | 0.43  | 390  | 2.0939          |
| 2.6223        | 0.5   | 455  | 2.0165          |
| 2.2567        | 0.57  | 520  | 1.9490          |
| 2.1168        | 0.64  | 585  | 1.8869          |
| 2.1214        | 0.71  | 650  | 1.8269          |
| 2.3123        | 0.79  | 715  | 1.7750          |
| 2.2535        | 0.86  | 780  | 1.7338          |
| 1.8926        | 0.93  | 845  | 1.6785          |
| 1.7711        | 1.0   | 910  | 1.6277          |
| 1.7578        | 1.07  | 975  | 1.5990          |
| 2.0243        | 1.14  | 1040 | 1.5484          |
| 2.2152        | 1.21  | 1105 | 1.5203          |
| 1.6819        | 1.28  | 1170 | 1.4809          |
| 1.5537        | 1.36  | 1235 | 1.4518          |
| 1.574         | 1.43  | 1300 | 1.4189          |
| 1.6772        | 1.5   | 1365 | 1.3917          |
| 1.6269        | 1.57  | 1430 | 1.3563          |
| 1.5375        | 1.64  | 1495 | 1.3363          |
| 1.5477        | 1.71  | 1560 | 1.3118          |
| 1.4559        | 1.78  | 1625 | 1.2857          |
| 1.4579        | 1.86  | 1690 | 1.2716          |
| 1.4705        | 1.93  | 1755 | 1.2587          |
| 1.4205        | 2.0   | 1820 | 1.2346          |
| 1.423         | 2.07  | 1885 | 1.2277          |
| 1.3852        | 2.14  | 1950 | 1.2123          |
| 1.3362        | 2.21  | 2015 | 1.2078          |
| 1.2793        | 2.28  | 2080 | 1.1854          |
| 1.3126        | 2.36  | 2145 | 1.1806          |
| 1.28          | 2.43  | 2210 | 1.1731          |
| 1.3789        | 2.5   | 2275 | 1.1646          |
| 1.3572        | 2.57  | 2340 | 1.1648          |
| 1.3398        | 2.64  | 2405 | 1.1539          |
| 1.2831        | 2.71  | 2470 | 1.1518          |
| 1.3269        | 2.78  | 2535 | 1.1488          |
| 1.2208        | 2.86  | 2600 | 1.1478          |
| 1.2955        | 2.93  | 2665 | 1.1421          |
| 1.2286        | 3.0   | 2730 | 1.1468          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.1+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
