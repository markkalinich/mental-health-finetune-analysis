---
library_name: transformers
license: apache-2.0
base_model: d4data/biomedical-ner-all
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ner-biomedical-maccrobat2018
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ner-biomedical-maccrobat2018

This model is a fine-tuned version of [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6384
- Accuracy: 0.8007

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.7438        | 1.0   | 10   | 1.8410          | 0.2970   |
| 1.4729        | 2.0   | 20   | 1.0655          | 0.5852   |
| 0.9161        | 3.0   | 30   | 0.7775          | 0.7075   |
| 0.6509        | 4.0   | 40   | 0.6808          | 0.7477   |
| 0.4923        | 5.0   | 50   | 0.6315          | 0.7603   |
| 0.3818        | 6.0   | 60   | 0.6120          | 0.7756   |
| 0.3096        | 7.0   | 70   | 0.6025          | 0.7742   |
| 0.2546        | 8.0   | 80   | 0.5992          | 0.7861   |
| 0.2089        | 9.0   | 90   | 0.6075          | 0.7883   |
| 0.178         | 10.0  | 100  | 0.6149          | 0.7877   |
| 0.159         | 11.0  | 110  | 0.6219          | 0.8012   |
| 0.139         | 12.0  | 120  | 0.6282          | 0.7997   |
| 0.1239        | 13.0  | 130  | 0.6222          | 0.7970   |
| 0.1115        | 14.0  | 140  | 0.6311          | 0.7915   |
| 0.1015        | 15.0  | 150  | 0.6336          | 0.7976   |
| 0.0958        | 16.0  | 160  | 0.6321          | 0.7955   |
| 0.0898        | 17.0  | 170  | 0.6352          | 0.7990   |
| 0.0874        | 18.0  | 180  | 0.6464          | 0.7981   |
| 0.0841        | 19.0  | 190  | 0.6380          | 0.7992   |
| 0.0819        | 20.0  | 200  | 0.6384          | 0.8007   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
