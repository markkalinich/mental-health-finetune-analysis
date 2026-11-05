---
license: cc-by-nc-sa-4.0
base_model: microsoft/layoutlmv2-large-uncased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv2-finetuned-piimask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv2-finetuned-piimask

This model is a fine-tuned version of [microsoft/layoutlmv2-large-uncased](https://huggingface.co/microsoft/layoutlmv2-large-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1939
- Precision: 0.7555
- Recall: 0.7775
- F1: 0.7663
- Accuracy: 0.9581

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
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 135  | 0.1473          | 0.7251    | 0.6697 | 0.6963 | 0.9499   |
| No log        | 2.0   | 270  | 0.1400          | 0.6767    | 0.7573 | 0.7147 | 0.9621   |
| No log        | 3.0   | 405  | 0.1543          | 0.7372    | 0.7753 | 0.7558 | 0.9612   |
| 0.3116        | 4.0   | 540  | 0.2355          | 0.7621    | 0.7775 | 0.7697 | 0.9560   |
| 0.3116        | 5.0   | 675  | 0.1939          | 0.7555    | 0.7775 | 0.7663 | 0.9581   |


### Framework versions

- Transformers 4.42.3
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
