---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: PubMedBERT_JNLPBA_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PubMedBERT_JNLPBA_NER

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1449
- Precision: 0.9556
- Recall: 0.9503
- F1: 0.9529
- Accuracy: 0.9508

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2769        | 1.0   | 582  | 0.1556          | 0.9519    | 0.9473 | 0.9496 | 0.9472   |
| 0.1456        | 2.0   | 1164 | 0.1493          | 0.9551    | 0.9488 | 0.9519 | 0.9495   |
| 0.1291        | 3.0   | 1746 | 0.1449          | 0.9556    | 0.9503 | 0.9529 | 0.9508   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.0
- Tokenizers 0.15.0
