---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: pubmedbert-fulltext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmedbert-fulltext

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4548
- Accuracy: 0.9498

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
- train_batch_size: 32
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| No log        | 1.0   | 791   | 0.2502          | 0.9342   |
| 0.1717        | 2.0   | 1582  | 0.2889          | 0.9449   |
| 0.0792        | 3.0   | 2373  | 0.2844          | 0.9424   |
| 0.0565        | 4.0   | 3164  | 0.3055          | 0.9377   |
| 0.0565        | 5.0   | 3955  | 0.3059          | 0.9458   |
| 0.0405        | 6.0   | 4746  | 0.3693          | 0.9451   |
| 0.0274        | 7.0   | 5537  | 0.3295          | 0.9438   |
| 0.0263        | 8.0   | 6328  | 0.4278          | 0.9337   |
| 0.0181        | 9.0   | 7119  | 0.3807          | 0.9465   |
| 0.0181        | 10.0  | 7910  | 0.4318          | 0.9442   |
| 0.0173        | 11.0  | 8701  | 0.3995          | 0.9487   |
| 0.011         | 12.0  | 9492  | 0.4487          | 0.9466   |
| 0.0077        | 13.0  | 10283 | 0.4247          | 0.9482   |
| 0.0075        | 14.0  | 11074 | 0.5082          | 0.9433   |
| 0.0075        | 15.0  | 11865 | 0.4722          | 0.9458   |
| 0.0071        | 16.0  | 12656 | 0.4134          | 0.9507   |
| 0.0034        | 17.0  | 13447 | 0.4252          | 0.9496   |
| 0.0033        | 18.0  | 14238 | 0.4436          | 0.9500   |
| 0.0023        | 19.0  | 15029 | 0.4481          | 0.9505   |
| 0.0023        | 20.0  | 15820 | 0.4548          | 0.9498   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu118
- Datasets 2.18.0
- Tokenizers 0.15.2
