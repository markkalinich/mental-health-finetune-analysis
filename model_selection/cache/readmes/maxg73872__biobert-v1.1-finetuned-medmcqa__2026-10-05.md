---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: biobert-v1.1-finetuned-medmcqa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-v1.1-finetuned-medmcqa

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9408
- Accuracy: {'accuracy': 0.6190476190476191}
- F1-score: {'f1': 0.6383219954648526}

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy                         | F1-score                   |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------:|:--------------------------:|
| No log        | 1.0   | 229  | 1.1779          | {'accuracy': 0.5714285714285714} | {'f1': 0.5936070334566574} |
| No log        | 2.0   | 458  | 0.9840          | {'accuracy': 0.6666666666666666} | {'f1': 0.6800653594771241} |
| 1.1746        | 3.0   | 687  | 0.9408          | {'accuracy': 0.6190476190476191} | {'f1': 0.6383219954648526} |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.1.0
- Tokenizers 0.19.1
