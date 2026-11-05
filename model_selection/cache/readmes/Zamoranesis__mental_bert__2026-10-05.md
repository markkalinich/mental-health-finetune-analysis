---
license: cc-by-nc-4.0
base_model: mental/mental-bert-base-uncased
tags:
- mental health
- mental disorders
- healthcare
- medical
model-index:
- name: mental_bert
  results: []
widget: 
- text: "The person suffers from extreme emotional fluctuations, sudden mood [MASK] and exaggerated reactions"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_bert

This model is a fine-tuned version of [mental/mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased) on [hackathon-somos-nlp-2023/DiagTrast](https://huggingface.co/datasets/hackathon-somos-nlp-2023/DiagTrast).
It achieves the following results on the evaluation and test sets:
- Evaluation Loss: 0.9179
- Test Loss: 0.9831

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- lr_scheduler_warmup_steps: 100
- training_steps: 2000

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.4138        | 6.25   | 100  | 1.1695          |
| 1.0912        | 12.5   | 200  | 1.1862          |
| 0.8699        | 18.75  | 300  | 0.9926          |
| 0.7713        | 25.0   | 400  | 1.0570          |
| 0.6655        | 31.25  | 500  | 1.0891          |
| 0.6127        | 37.5   | 600  | 1.0389          |
| 0.5461        | 43.75  | 700  | 0.9947          |
| 0.5167        | 50.0   | 800  | 1.0043          |
| 0.45          | 56.25  | 900  | 0.9688          |
| 0.436         | 62.5   | 1000 | 0.9482          |
| 0.3896        | 68.75  | 1100 | 1.0424          |
| 0.3624        | 75.0   | 1200 | 0.9242          |
| 0.3821        | 81.25  | 1300 | 1.0748          |
| 0.3156        | 87.5   | 1400 | 1.0121          |
| 0.3099        | 93.75  | 1500 | 0.9404          |
| 0.2829        | 100.0  | 1600 | 0.8997          |
| 0.2712        | 106.25 | 1700 | 0.8902          |
| 0.2596        | 112.5  | 1800 | 0.9054          |
| 0.2622        | 118.75 | 1900 | 1.0317          |
| 0.2631        | 125.0  | 2000 | 0.9179          |


### Framework versions

- Transformers 4.33.3
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.13.3
