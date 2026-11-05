---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: PubMedBERT-mimic-phi-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PubMedBERT-mimic-phi-ner

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0024
- F1 Macro: 0.9550
- F1 Weighted: 0.9550
- Precision: 0.9316
- Recall: 0.9795
- F1 Name: 0.95
- F1 Location: 0.93
- F1 Phone: 0.94
- F1 Date: 0.87
- F1 Mrn: 0.97
- F1 Account: 0.99
- F1 Age Over 89: 1.0
- F1 Device Id: 1.0
- F1 Ssn: 1.0
- F1 Url: 1.0
- F1 Email: 1.0

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
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | F1 Macro | F1 Weighted | Precision | Recall | F1 Name | F1 Location | F1 Phone | F1 Date | F1 Mrn | F1 Account | F1 Age Over 89 | F1 Device Id | F1 Ssn | F1 Url | F1 Email |
|:-------------:|:------:|:----:|:---------------:|:--------:|:-----------:|:---------:|:------:|:-------:|:-----------:|:--------:|:-------:|:------:|:----------:|:--------------:|:------------:|:------:|:------:|:--------:|
| 0.4473        | 0.1774 | 300  | 0.0939          | 0.4089   | 0.4089      | 0.2964    | 0.6588 | 0.58    | 0.26        | 0.38     | 0.17    | 0.35   | 0.2        | 0.06           | 0.4          | 0.17   | 0.0    | 0.05     |
| 0.0666        | 0.3547 | 600  | 0.0142          | 0.7808   | 0.7808      | 0.6804    | 0.9158 | 0.86    | 0.64        | 0.9      | 0.4     | 0.52   | 0.55       | 0.41           | 0.9          | 0.59   | 0.87   | 0.82     |
| 0.0225        | 0.5321 | 900  | 0.0070          | 0.8786   | 0.8786      | 0.8251    | 0.9394 | 0.89    | 0.79        | 0.94     | 0.44    | 0.84   | 0.98       | 0.9            | 0.95         | 0.98   | 1.0    | 0.99     |
| 0.0267        | 0.7094 | 1200 | 0.0049          | 0.91     | 0.91        | 0.8641    | 0.9610 | 0.92    | 0.84        | 0.76     | 0.66    | 0.95   | 0.99       | 0.95           | 0.99         | 1.0    | 1.0    | 1.0      |
| 0.0127        | 0.8868 | 1500 | 0.0046          | 0.9281   | 0.9281      | 0.8918    | 0.9675 | 0.93    | 0.87        | 0.94     | 0.78    | 0.96   | 0.99       | 1.0            | 1.0          | 1.0    | 1.0    | 1.0      |
| 0.0099        | 1.0638 | 1800 | 0.0035          | 0.9338   | 0.9338      | 0.9009    | 0.9691 | 0.93    | 0.91        | 0.94     | 0.84    | 0.96   | 0.99       | 1.0            | 1.0          | 0.99   | 1.0    | 1.0      |
| 0.0070        | 1.2412 | 2100 | 0.0030          | 0.9495   | 0.9495      | 0.9237    | 0.9768 | 0.95    | 0.9         | 0.95     | 0.88    | 0.96   | 0.99       | 1.0            | 1.0          | 1.0    | 1.0    | 1.0      |
| 0.0115        | 1.4186 | 2400 | 0.0026          | 0.9489   | 0.9489      | 0.9222    | 0.9771 | 0.94    | 0.93        | 0.95     | 0.86    | 0.97   | 0.99       | 1.0            | 1.0          | 1.0    | 1.0    | 1.0      |
| 0.0088        | 1.5959 | 2700 | 0.0025          | 0.9533   | 0.9533      | 0.9296    | 0.9784 | 0.95    | 0.92        | 0.95     | 0.88    | 0.96   | 0.99       | 1.0            | 1.0          | 1.0    | 1.0    | 1.0      |
| 0.0067        | 1.7733 | 3000 | 0.0024          | 0.9542   | 0.9542      | 0.9310    | 0.9787 | 0.95    | 0.92        | 0.94     | 0.87    | 0.97   | 0.99       | 1.0            | 1.0          | 1.0    | 1.0    | 1.0      |
| 0.0053        | 1.9506 | 3300 | 0.0024          | 0.9550   | 0.9550      | 0.9316    | 0.9795 | 0.95    | 0.93        | 0.94     | 0.87    | 0.97   | 0.99       | 1.0            | 1.0          | 1.0    | 1.0    | 1.0      |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
