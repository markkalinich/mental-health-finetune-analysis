---
license: apache-2.0
base_model: allenai/longformer-base-4096
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_treintamil
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_treintamil

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3864

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
- train_batch_size: 2
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.6837        | 0.09  | 2    | 2.6011          |
| 2.7002        | 0.19  | 4    | 2.4829          |
| 2.7169        | 0.28  | 6    | 2.5518          |
| 2.5927        | 0.38  | 8    | 2.4683          |
| 2.6215        | 0.47  | 10   | 2.5798          |
| 2.6608        | 0.57  | 12   | 2.4698          |
| 2.6124        | 0.66  | 14   | 2.6022          |
| 2.5422        | 0.76  | 16   | 2.5533          |
| 2.6775        | 0.85  | 18   | 2.5041          |
| 5.5552        | 0.95  | 20   | 2.5191          |
| 2.6986        | 1.04  | 22   | 2.5060          |
| 2.7096        | 1.14  | 24   | 2.4583          |
| 3.5551        | 1.23  | 26   | 2.5649          |
| 2.7292        | 1.33  | 28   | 2.5068          |
| 2.766         | 1.42  | 30   | 2.4687          |
| 3.4509        | 1.52  | 32   | 2.5880          |
| 3.3941        | 1.61  | 34   | 2.4755          |
| 2.5889        | 1.71  | 36   | 2.5193          |
| 2.6374        | 1.8   | 38   | 2.5416          |
| 2.5641        | 1.9   | 40   | 2.4652          |
| 2.8255        | 1.99  | 42   | 2.5123          |
| 2.5652        | 2.09  | 44   | 2.4474          |
| 2.5775        | 2.18  | 46   | 2.5389          |
| 2.5171        | 2.28  | 48   | 2.4643          |
| 2.6795        | 2.37  | 50   | 2.4121          |
| 2.591         | 2.47  | 52   | 2.4375          |
| 2.7528        | 2.56  | 54   | 2.5074          |
| 2.6141        | 2.65  | 56   | 2.4405          |
| 2.6785        | 2.75  | 58   | 2.4155          |
| 3.0339        | 2.84  | 60   | 2.4628          |
| 2.6164        | 2.94  | 62   | 2.4732          |
| 2.4911        | 3.03  | 64   | 2.3910          |
| 2.6821        | 3.13  | 66   | 2.4661          |
| 2.6406        | 3.22  | 68   | 2.4274          |
| 2.6277        | 3.32  | 70   | 2.4130          |
| 2.5329        | 3.41  | 72   | 2.4310          |
| 2.5272        | 3.51  | 74   | 2.4122          |
| 2.5845        | 3.6   | 76   | 2.4515          |
| 2.5483        | 3.7   | 78   | 2.3397          |
| 2.5458        | 3.79  | 80   | 2.3840          |
| 2.4884        | 3.89  | 82   | 2.3933          |
| 2.4538        | 3.98  | 84   | 2.3864          |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
