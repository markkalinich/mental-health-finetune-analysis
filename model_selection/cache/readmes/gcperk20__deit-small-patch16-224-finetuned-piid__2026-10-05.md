---
license: apache-2.0
base_model: facebook/deit-small-patch16-224
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: deit-small-patch16-224-finetuned-piid
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
      value: 0.7945205479452054
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deit-small-patch16-224-finetuned-piid

This model is a fine-tuned version of [facebook/deit-small-patch16-224](https://huggingface.co/facebook/deit-small-patch16-224) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5615
- Accuracy: 0.7945

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
| 1.1803        | 0.98  | 20   | 1.0233          | 0.5753   |
| 0.706         | 2.0   | 41   | 0.7299          | 0.7078   |
| 0.6016        | 2.98  | 61   | 0.6877          | 0.7123   |
| 0.4903        | 4.0   | 82   | 0.6139          | 0.7671   |
| 0.4692        | 4.98  | 102  | 0.5667          | 0.7626   |
| 0.374         | 6.0   | 123  | 0.5146          | 0.8037   |
| 0.2995        | 6.98  | 143  | 0.5596          | 0.7534   |
| 0.2905        | 8.0   | 164  | 0.5313          | 0.7534   |
| 0.2612        | 8.98  | 184  | 0.5328          | 0.7900   |
| 0.2499        | 10.0  | 205  | 0.5369          | 0.7991   |
| 0.185         | 10.98 | 225  | 0.5754          | 0.7808   |
| 0.1927        | 12.0  | 246  | 0.5886          | 0.7717   |
| 0.1446        | 12.98 | 266  | 0.5160          | 0.7991   |
| 0.155         | 14.0  | 287  | 0.5353          | 0.8082   |
| 0.1577        | 14.98 | 307  | 0.5848          | 0.7808   |
| 0.1243        | 16.0  | 328  | 0.5572          | 0.7991   |
| 0.1038        | 16.98 | 348  | 0.5859          | 0.7763   |
| 0.1305        | 18.0  | 369  | 0.5752          | 0.7900   |
| 0.0868        | 18.98 | 389  | 0.5616          | 0.8037   |
| 0.1364        | 19.51 | 400  | 0.5615          | 0.7945   |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
