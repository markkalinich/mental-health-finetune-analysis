---
license: apache-2.0
base_model: TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
tags:
- generated_from_trainer
model-index:
- name: TinyLlama-PsychiatryCaseNotes-epochs-1-lr-0002
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
adapter: null
base_model: TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T
bf16: auto
dataset_prepared_path: last_run_prepared
datasets:
- path: utrgvseniorproject/Tinybook
  type: completion
debug: null
deepspeed: null
early_stopping_patience: null
eval_sample_packing: false
eval_table_size: null
evals_per_epoch: 4
flash_attention: true
flash_attn_cross_entropy: false
flash_attn_fuse_mlp: true
flash_attn_fuse_qkv: false
flash_attn_rms_norm: true
fp16: null
fsdp: null
fsdp_config: null
gradient_accumulation_steps: 1
gradient_checkpointing: true
group_by_length: false
learning_rate: 0.0002
load_in_4bit: false
load_in_8bit: false
local_rank: null
logging_steps: 1
lora_alpha: null
lora_dropout: null
lora_fan_in_fan_out: null
lora_model_dir: null
lora_r: null
lora_target_linear: null
lr_scheduler: cosine
micro_batch_size: 1
model_type: LlamaForCausalLM
num_epochs: 1
optimizer: adamw_bnb_8bit
output_dir: ./TinyLlama-PsychiatryCaseNotes-epochs-1-lr-0002
pad_to_sequence_len: true
resume_from_checkpoint: null
sample_packing: true
saves_per_epoch: 1
sequence_len: 2048
special_tokens: null
strict: false
tf32: false
tokenizer_type: LlamaTokenizer
train_on_inputs: false
val_set_size: 0.05
wandb_entity: utrgvmedai
wandb_log_model: null
wandb_name: tinyLama_colab_test_2
wandb_project: TinyLlama-PsychiatryCaseNotes-epochs-1-lr-0002
wandb_watch: null
warmup_steps: 100
weight_decay: 0.1
xformers_attention: null

```

</details><br>

# TinyLlama-PsychiatryCaseNotes-epochs-1-lr-0002

This model is a fine-tuned version of [TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T](https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8020

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.7259        | 0.04  | 1    | 1.9138          |
| 1.8148        | 0.26  | 6    | 1.9011          |
| 1.8631        | 0.52  | 12   | 1.8659          |
| 1.8768        | 0.78  | 18   | 1.8020          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.2+cu121
- Datasets 2.18.0
- Tokenizers 0.15.0
