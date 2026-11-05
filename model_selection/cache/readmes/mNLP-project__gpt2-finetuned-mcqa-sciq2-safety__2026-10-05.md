---
license: mit
tags:
- generated_from_trainer
base_model: openai-community/gpt2
metrics:
- bleu
model-index:
- name: gpt2-finetuned-mcqa-sciq2-safety
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-finetuned-mcqa-sciq2-safety

This model is a fine-tuned version of [openai-community/gpt2](https://huggingface.co/openai-community/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7824
- Bleu: 0.0816
- Bertscore Precision: 0.4316
- Bertscore Recall: 0.4553
- Bertscore F1: 0.4431

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu   | Bertscore Precision | Bertscore Recall | Bertscore F1 |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:-------------------:|:----------------:|:------------:|
| 1.917         | 1.0   | 1460  | 1.8258          | 0.0856 | 0.4279              | 0.4541           | 0.4406       |
| 1.7299        | 2.0   | 2920  | 1.7928          | 0.0789 | 0.4311              | 0.4549           | 0.4427       |
| 1.6342        | 3.0   | 4380  | 1.7870          | 0.0858 | 0.4315              | 0.4542           | 0.4425       |
| 1.5534        | 4.0   | 5840  | 1.7824          | 0.0816 | 0.4316              | 0.4553           | 0.4431       |
| 1.4878        | 5.0   | 7300  | 1.7909          | 0.0797 | 0.4315              | 0.4556           | 0.4432       |
| 1.4554        | 6.0   | 8760  | 1.8021          | 0.0772 | 0.4312              | 0.4557           | 0.4431       |
| 1.3981        | 7.0   | 10220 | 1.8103          | 0.0767 | 0.4314              | 0.4558           | 0.4433       |
| 1.3712        | 8.0   | 11680 | 1.8242          | 0.0427 | 0.4315              | 0.4561           | 0.4434       |
| 1.3431        | 9.0   | 13140 | 1.8338          | 0.0416 | 0.4315              | 0.4560           | 0.4434       |
| 1.3354        | 10.0  | 14600 | 1.8390          | 0.0420 | 0.4315              | 0.4560           | 0.4434       |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
