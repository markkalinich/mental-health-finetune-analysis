---
license: apache-2.0
base_model: facebook/deit-tiny-patch16-224
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: deit-tiny-patch16-224-finetuned-piid
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: default
      split: val
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7625570776255708
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deit-tiny-patch16-224-finetuned-piid

This model is a fine-tuned version of [facebook/deit-tiny-patch16-224](https://huggingface.co/facebook/deit-tiny-patch16-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5426
- Accuracy: 0.7626

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.2274        | 0.98  | 20   | 1.1185          | 0.4658   |
| 0.8485        | 2.0   | 41   | 0.8690          | 0.6119   |
| 0.6793        | 2.98  | 61   | 0.8749          | 0.6073   |
| 0.6028        | 4.0   | 82   | 0.6864          | 0.6804   |
| 0.5693        | 4.98  | 102  | 0.5618          | 0.7717   |
| 0.5092        | 6.0   | 123  | 0.5958          | 0.7260   |
| 0.3788        | 6.98  | 143  | 0.6444          | 0.7352   |
| 0.4106        | 8.0   | 164  | 0.5277          | 0.7443   |
| 0.3716        | 8.98  | 184  | 0.6081          | 0.7352   |
| 0.3466        | 10.0  | 205  | 0.4976          | 0.7580   |
| 0.3587        | 10.98 | 225  | 0.5429          | 0.7443   |
| 0.2661        | 12.0  | 246  | 0.4933          | 0.7763   |
| 0.2628        | 12.98 | 266  | 0.5078          | 0.7671   |
| 0.2473        | 14.0  | 287  | 0.5264          | 0.7945   |
| 0.2633        | 14.98 | 307  | 0.5262          | 0.7671   |
| 0.2017        | 16.0  | 328  | 0.5509          | 0.7763   |
| 0.1861        | 16.98 | 348  | 0.5513          | 0.7443   |
| 0.2031        | 18.0  | 369  | 0.5516          | 0.7580   |
| 0.1604        | 18.98 | 389  | 0.5430          | 0.7671   |
| 0.2346        | 19.51 | 400  | 0.5426          | 0.7626   |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
