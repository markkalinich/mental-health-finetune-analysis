---
base_model:  Qwen/Qwen2-1.5B-Instruct
library_name: peft
license: other
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: Qwen2-1.5B-Medical-Instruct
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Qwen2-1.5B-Medical-Instruct

This model is a pretrain+fine-tuned+rlhf version of Qwen2-1.5B-Instruct on the medical dataset

## Model description

Detailed model description can be seen on the base model [Qwen/Qwen2-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) page.
This model has been pre-trained on medical industry, then fine-tuned all lora_target, and finally trained with reinforcement learning.


## Training and evaluation data

This model is a pretrain+fine-tuned+rlhf version of Qwen2-1.5B-Instruct on the [medical dataset](https://huggingface.co/datasets/shibing624/medical)

## Training procedure
### Pre-train
pre-trained on medical industry

### SFT
fine-tuned on sft data

#### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 512
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 4

#### Training results

| Training Loss | Epoch  | Step  | Validation Loss |
|:-------------:|:------:|:-----:|:---------------:|
| 1.7788        | 0.1239 | 500   | 2.1232          |
| 1.7728        | 0.2477 | 1000  | 2.0532          |
| 1.761         | 0.3716 | 1500  | 2.0188          |
| 1.7292        | 0.4955 | 2000  | 1.9984          |
| 1.7553        | 0.6194 | 2500  | 1.9872          |
| 1.7264        | 0.7432 | 3000  | 1.9739          |
| 1.7028        | 0.8671 | 3500  | 1.9638          |
| 1.6923        | 0.9910 | 4000  | 1.9570          |
| 1.6972        | 1.1149 | 4500  | 1.9498          |
| 1.705         | 1.2387 | 5000  | 1.9449          |
| 1.6902        | 1.3626 | 5500  | 1.9409          |
| 1.6694        | 1.4865 | 6000  | 1.9361          |
| 1.7191        | 1.6104 | 6500  | 1.9308          |
| 1.6976        | 1.7342 | 7000  | 1.9283          |
| 1.6798        | 1.8581 | 7500  | 1.9247          |
| 1.6737        | 1.9820 | 8000  | 1.9208          |
| 1.6696        | 2.1058 | 8500  | 1.9195          |
| 1.6817        | 2.2297 | 9000  | 1.9164          |
| 1.6715        | 2.3536 | 9500  | 1.9141          |
| 1.6798        | 2.4775 | 10000 | 1.9119          |
| 1.6829        | 2.6013 | 10500 | 1.9089          |
| 1.6551        | 2.7252 | 11000 | 1.9075          |
| 1.6781        | 2.8491 | 11500 | 1.9052          |
| 1.6833        | 2.9730 | 12000 | 1.9039          |
| 1.6391        | 3.0968 | 12500 | 1.9032          |
| 1.6535        | 3.2207 | 13000 | 1.9022          |
| 1.6744        | 3.3446 | 13500 | 1.9010          |
| 1.6399        | 3.4685 | 14000 | 1.9009          |
| 1.6333        | 3.5923 | 14500 | 1.9005          |
| 1.6643        | 3.7162 | 15000 | 1.9000          |
| 1.6673        | 3.8401 | 15500 | 1.9002          |
| 1.6719        | 3.9640 | 16000 | 1.8999          |

### DPO
human feedback reinforcement learning on medical reward data
```python
{
    "epoch": 3.764705882352941,
    "eval_logits/chosen": -1.19295334815979,
    "eval_logits/rejected": -0.7887511253356934,
    "eval_logps/chosen": -150.47561645507812,
    "eval_logps/rejected": -75.58721160888672,
    "eval_loss": 0.6550262570381165,
    "eval_rewards/accuracies": 1.0,
    "eval_rewards/chosen": 0.03167621046304703,
    "eval_rewards/margins": 0.13228271901607513,
    "eval_rewards/rejected": -0.10060650110244751,
    "eval_runtime": 1.805,
    "eval_samples_per_second": 55.403,
    "eval_steps_per_second": 3.878
}
```

### Framework versions

- PEFT 0.12.0
- Transformers 4.44.2
- Pytorch 2.4.0
- Datasets 2.21.0
- Tokenizers 0.19.1
