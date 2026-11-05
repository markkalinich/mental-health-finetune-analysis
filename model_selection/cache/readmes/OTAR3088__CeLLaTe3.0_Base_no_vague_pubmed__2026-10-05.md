---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe3.0_Base_no_vague_pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe3.0_Base_no_vague_pubmed

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1384
- Precision: 0.7700
- Recall: 0.8469
- F1: 0.8066
- Accuracy: 0.9659

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.4387        | 1.0   | 96   | 0.5374          | 0.0       | 0.0    | 0.0    | 0.8636   |
| 0.3318        | 2.0   | 192  | 0.1596          | 0.6288    | 0.7567 | 0.6868 | 0.9582   |
| 0.1398        | 3.0   | 288  | 0.1472          | 0.6731    | 0.7479 | 0.7085 | 0.9601   |
| 0.0908        | 4.0   | 384  | 0.1394          | 0.7700    | 0.8469 | 0.8066 | 0.9659   |
| 0.0657        | 5.0   | 480  | 0.1599          | 0.7181    | 0.7852 | 0.7502 | 0.9625   |
| 0.0511        | 6.0   | 576  | 0.1721          | 0.6924    | 0.8347 | 0.7569 | 0.9584   |
| 0.0398        | 7.0   | 672  | 0.1592          | 0.7721    | 0.8440 | 0.8064 | 0.9665   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
