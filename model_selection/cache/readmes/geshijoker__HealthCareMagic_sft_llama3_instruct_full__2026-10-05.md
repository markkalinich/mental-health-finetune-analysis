---
library_name: transformers
license: llama3
base_model: meta-llama/Meta-Llama-3-8B-Instruct
tags:
- llama-factory
- full
- generated_from_trainer
model-index:
- name: sft_full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sft_full

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on the healthcaremagic dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7460

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 512
- total_eval_batch_size: 64
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 3.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.2093        | 2.8429 | 500  | 1.7462          |

### Evaluation results
| Name                    | Checkpoint                                                                                                       | Rouge1  | RougeL | Meteor | Bert Score |
|-------------------------|------------------------------------------------------------------------------------------------------------------|---------|--------|--------|------------|
| baseline instruct model | [Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)                           | 0.254   | 0.128  | 0.222  | 0.747      |
| full fientune from inst | [sft_llama3_instruct_full](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)                           | 0.315   | 0.189  | 0.238  | 0.782      | 
| lora sft from inst      | [sft_llama3_instruct_lora_all](https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_lora_all)   | 0.271   | 0.143  | 0.194  | 0.774      | 
| lora sft from base      | [sft_llama3_lora_all](geshijoker/HealthCareMagic_sft_llama3_lora_all)                                            | 0.239   | 0.113  | 0.211  | 0.735      | 
| qlora sft from inst     | [sft_llama3_instruct_qlora_all](https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_instruct_qlora_all) | 0.137   | 0.071  | 0.102  | 0.679      | 
| qlora sft from base     | [sft_llama3_qlora_all ](https://huggingface.co/geshijoker/HealthCareMagic_sft_llama3_qlora_all)                  | 0.192   | 0.090  | 0.159  | 0.718      | 


### Framework versions

- Transformers 4.46.1
- Pytorch 2.5.1
- Datasets 3.1.0
- Tokenizers 0.20.3
