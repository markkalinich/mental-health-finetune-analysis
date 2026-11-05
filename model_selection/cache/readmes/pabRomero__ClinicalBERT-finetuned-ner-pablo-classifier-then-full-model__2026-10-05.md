---
base_model: pabRomero/ClinicalBERT-finetuned-ner-pablo-just-classifier
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: ClinicalBERT-finetuned-ner-pablo-classifier-then-full-model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-finetuned-ner-pablo-classifier-then-full-model

This model is a fine-tuned version of [pabRomero/ClinicalBERT-finetuned-ner-pablo-just-classifier](https://huggingface.co/pabRomero/ClinicalBERT-finetuned-ner-pablo-just-classifier) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1259
- Precision: 0.8091
- Recall: 0.8039
- F1: 0.8065
- Accuracy: 0.9716

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1613        | 0.9996 | 652  | 0.1321          | 0.8184    | 0.7378 | 0.7760 | 0.9674   |
| 0.1048        | 1.9992 | 1304 | 0.1060          | 0.7999    | 0.7652 | 0.7822 | 0.9708   |
| 0.0745        | 2.9989 | 1956 | 0.1124          | 0.8016    | 0.7960 | 0.7988 | 0.9708   |
| 0.0349        | 3.9985 | 2608 | 0.1259          | 0.8091    | 0.8039 | 0.8065 | 0.9716   |


### Framework versions

- Transformers 4.44.0
- Pytorch 2.4.0+cu124
- Datasets 2.21.0
- Tokenizers 0.19.1
