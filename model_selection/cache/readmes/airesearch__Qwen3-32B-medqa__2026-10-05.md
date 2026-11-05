---
library_name: peft
license: other
base_model: Qwen/Qwen3-32B
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: Qwen3-32B-medqa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Qwen3-32B-medqa

This model is a fine-tuned version of [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) on the medqa dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0258

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 16
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- total_eval_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.1927        | 0.0582 | 10   | 2.0806          |
| 0.1655        | 0.1164 | 20   | 0.1102          |
| 0.0307        | 0.1745 | 30   | 0.0408          |
| 0.0305        | 0.2327 | 40   | 0.0329          |
| 0.0291        | 0.2909 | 50   | 0.0311          |
| 0.0255        | 0.3491 | 60   | 0.0300          |
| 0.0325        | 0.4073 | 70   | 0.0292          |
| 0.0259        | 0.4655 | 80   | 0.0285          |
| 0.0305        | 0.5236 | 90   | 0.0276          |
| 0.0275        | 0.5818 | 100  | 0.0267          |
| 0.0274        | 0.64   | 110  | 0.0263          |
| 0.0253        | 0.6982 | 120  | 0.0256          |
| 0.0196        | 0.7564 | 130  | 0.0252          |
| 0.0223        | 0.8145 | 140  | 0.0248          |
| 0.0259        | 0.8727 | 150  | 0.0246          |
| 0.0238        | 0.9309 | 160  | 0.0242          |
| 0.0228        | 0.9891 | 170  | 0.0241          |
| 0.0163        | 1.0465 | 180  | 0.0243          |
| 0.0155        | 1.1047 | 190  | 0.0240          |
| 0.0238        | 1.1629 | 200  | 0.0239          |
| 0.0186        | 1.2211 | 210  | 0.0241          |
| 0.022         | 1.2793 | 220  | 0.0239          |
| 0.0174        | 1.3375 | 230  | 0.0239          |
| 0.0212        | 1.3956 | 240  | 0.0236          |
| 0.0194        | 1.4538 | 250  | 0.0235          |
| 0.0176        | 1.512  | 260  | 0.0233          |
| 0.0223        | 1.5702 | 270  | 0.0234          |
| 0.019         | 1.6284 | 280  | 0.0236          |
| 0.0174        | 1.6865 | 290  | 0.0234          |
| 0.0166        | 1.7447 | 300  | 0.0233          |
| 0.0153        | 1.8029 | 310  | 0.0234          |
| 0.0138        | 1.8611 | 320  | 0.0234          |
| 0.0212        | 1.9193 | 330  | 0.0231          |
| 0.0225        | 1.9775 | 340  | 0.0230          |
| 0.0104        | 2.0349 | 350  | 0.0232          |
| 0.0102        | 2.0931 | 360  | 0.0247          |
| 0.0116        | 2.1513 | 370  | 0.0251          |
| 0.0091        | 2.2095 | 380  | 0.0251          |
| 0.0139        | 2.2676 | 390  | 0.0253          |
| 0.0088        | 2.3258 | 400  | 0.0254          |
| 0.0099        | 2.384  | 410  | 0.0253          |
| 0.0089        | 2.4422 | 420  | 0.0254          |
| 0.0128        | 2.5004 | 430  | 0.0256          |
| 0.0101        | 2.5585 | 440  | 0.0254          |
| 0.0115        | 2.6167 | 450  | 0.0254          |
| 0.0113        | 2.6749 | 460  | 0.0256          |
| 0.0105        | 2.7331 | 470  | 0.0257          |
| 0.0086        | 2.7913 | 480  | 0.0258          |
| 0.0081        | 2.8495 | 490  | 0.0258          |
| 0.0099        | 2.9076 | 500  | 0.0258          |
| 0.0134        | 2.9658 | 510  | 0.0257          |


### Framework versions

- PEFT 0.15.2
- Transformers 4.52.3
- Pytorch 2.7.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.1