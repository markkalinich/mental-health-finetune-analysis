---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: imp-mesh-ner
  results: []  
widget:
- text: "HISTORY OF PRESENT ILLNESS: Pt is 45 yo admitted for perirectal abscess. He has hx of diabetes."
  example_title: "Example 1"
- text: "No reported fever, chills, cough, chest pain, shortness of breath, N/V."
  example_title: "Example 2"
---


<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# imp-mesh-ner

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0291
- Precision: 0.9719
- Recall: 0.9787
- F1: 0.9753
- Accuracy: 0.9972

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0159        | 1.0   | 10000 | 0.0262          | 0.9555    | 0.9619 | 0.9587 | 0.9958   |
| 0.0093        | 2.0   | 20000 | 0.0255          | 0.9631    | 0.9727 | 0.9679 | 0.9966   |
| 0.007         | 3.0   | 30000 | 0.0282          | 0.9662    | 0.9751 | 0.9706 | 0.9969   |
| 0.0058        | 4.0   | 40000 | 0.0326          | 0.9713    | 0.9785 | 0.9749 | 0.9972   |
| 0.0043        | 5.0   | 50000 | 0.0291          | 0.9719    | 0.9787 | 0.9753 | 0.9972   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.1+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
