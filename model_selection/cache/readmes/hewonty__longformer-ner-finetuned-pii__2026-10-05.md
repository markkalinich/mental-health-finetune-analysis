---
license: apache-2.0
base_model: allenai/longformer-base-4096
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: longformer-ner-finetuned-pii
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# longformer-ner-finetuned-pii

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0034
- Precision: 0.9772
- Recall: 0.9879
- F1: 0.9825
- Accuracy: 0.9993

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0063        | 1.0   | 1324 | 0.0050          | 0.9613    | 0.9842 | 0.9726 | 0.9990   |
| 0.0037        | 2.0   | 2648 | 0.0038          | 0.9735    | 0.9873 | 0.9803 | 0.9992   |
| 0.002         | 3.0   | 3972 | 0.0034          | 0.9772    | 0.9879 | 0.9825 | 0.9993   |


### Framework versions

- Transformers 4.37.0
- Pytorch 2.1.2
- Datasets 2.1.0
- Tokenizers 0.15.1
