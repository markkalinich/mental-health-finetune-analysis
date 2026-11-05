---
license: apache-2.0
base_model: mrm8488/t5-small-finetuned-text-simplification
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: t5-medical-text-simplification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-medical-text-simplification

This model is a fine-tuned version of [mrm8488/t5-small-finetuned-text-simplification](https://huggingface.co/mrm8488/t5-small-finetuned-text-simplification) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4158
- Bleu: {'bleu': 0.24913061085239344, 'precisions': [0.6300697552884507, 0.46170603353322726, 0.3783389479827051, 0.3190805662507599], 'brevity_penalty': 0.5754971743889961, 'length_ratio': 0.6441136869219061, 'translation_length': 44011, 'reference_length': 68328}
- Sari: {'sari': 21.772869578730884}
- Fkgl: 10.2474

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu                                                                                                                                                                                                                                                              | Sari                         | Fkgl    |
|:-------------:|:-----:|:----:|:---------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------:|:-------:|
| 1.5524        | 1.0   | 1578 | 1.4317          | {'bleu': 0.24854970426705067, 'precisions': [0.626776178839714, 0.45794346978557504, 0.37443247809101465, 0.3154227136604469], 'brevity_penalty': 0.5792493345645447, 'length_ratio': 0.646821215314366, 'translation_length': 44196, 'reference_length': 68328}  | {'sari': 21.542679628603977} | 10.2949 |
| 1.5282        | 2.0   | 3156 | 1.4249          | {'bleu': 0.24886563197246125, 'precisions': [0.6285792076961474, 0.4604086221222934, 0.3770192256766061, 0.3176616771658094], 'brevity_penalty': 0.5767757332645675, 'length_ratio': 0.6450357101042032, 'translation_length': 44074, 'reference_length': 68328}  | {'sari': 21.665573517166536} | 10.2937 |
| 1.4997        | 3.0   | 4734 | 1.4176          | {'bleu': 0.24852094682922746, 'precisions': [0.629403208945048, 0.4605591734808794, 0.377421066595914, 0.3182660566398332], 'brevity_penalty': 0.5753144561890373, 'length_ratio': 0.6439819693244351, 'translation_length': 44002, 'reference_length': 68328}    | {'sari': 21.700716936778782} | 10.2544 |
| 1.5028        | 4.0   | 6312 | 1.4176          | {'bleu': 0.24876653336273433, 'precisions': [0.6299538437052363, 0.4615309246785058, 0.37816241471767237, 0.3188943296728769], 'brevity_penalty': 0.5748880487421792, 'length_ratio': 0.6436746282636694, 'translation_length': 43981, 'reference_length': 68328} | {'sari': 21.750120178010484} | 10.2531 |
| 1.4976        | 5.0   | 7890 | 1.4158          | {'bleu': 0.24913061085239344, 'precisions': [0.6300697552884507, 0.46170603353322726, 0.3783389479827051, 0.3190805662507599], 'brevity_penalty': 0.5754971743889961, 'length_ratio': 0.6441136869219061, 'translation_length': 44011, 'reference_length': 68328} | {'sari': 21.772869578730884} | 10.2474 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
