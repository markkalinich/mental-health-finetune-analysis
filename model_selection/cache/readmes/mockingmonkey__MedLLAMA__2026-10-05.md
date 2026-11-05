---
base_model: meta-llama/Meta-Llama-3-8B
library_name: peft
license: llama3
tags:
- trl
- sft
- generated_from_trainer
model-index:
- name: MedLLAMA
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/jules-guyet-epita/huggingface/runs/gpu4tqd6)
# MedLLAMA

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9700

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.325         | 0.6000 | 2435 | 1.0248          |
| 1.0124        | 1.2001 | 4870 | 1.0025          |
| 0.795         | 1.8001 | 7305 | 0.9766          |
| 1.1855        | 2.4002 | 9740 | 0.9700          |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.1.1+cu121
- Datasets 2.14.5
- Tokenizers 0.19.1
## Training procedure


The following `bitsandbytes` quantization config was used during training:
- quant_method: QuantizationMethod.BITS_AND_BYTES
- _load_in_8bit: False
- _load_in_4bit: True
- llm_int8_threshold: 6.0
- llm_int8_skip_modules: None
- llm_int8_enable_fp32_cpu_offload: False
- llm_int8_has_fp16_weight: False
- bnb_4bit_quant_type: nf4
- bnb_4bit_use_double_quant: True
- bnb_4bit_compute_dtype: float16
- bnb_4bit_quant_storage: uint8
- load_in_4bit: True
- load_in_8bit: False

### Framework versions


- PEFT 0.6.2
