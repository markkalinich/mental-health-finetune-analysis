---
license: apache-2.0
base_model: mistralai/Mistral-7B-v0.1
tags:
- generated_from_trainer
model-index:
- name: mistral-7B-PsychiatryCaseNotes-epochs-3-lr-000002
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: mistralai/Mistral-7B-v0.1
model_type: MistralForCausalLM
tokenizer_type: LlamaTokenizer
is_mistral_derived_model: true

load_in_8bit: false
load_in_4bit: false
strict: false

datasets:
  - path: utrgvseniorproject/PsychiatryCaseNotes
    type: completion
dataset_prepared_path: /home/josegomez15/med-llm/last_run_prepared
val_set_size: 0.05
output_dir: ./mistral-7B-PsychiatryCaseNotes-epochs-3-lr-000002

sequence_len: 4096
sample_packing: false
pad_to_sequence_len: true

wandb_project: mistral-7B-PsychiatryCaseNotes
wandb_entity: utrgvmedai
wandb_watch:
wandb_name: mistral-7B-PsychiatryCaseNotes-epochs-3-lr-000002
wandb_log_model:

gradient_accumulation_steps: 1
micro_batch_size: 1
num_epochs: 3
optimizer: adamw_bnb_8bit
lr_scheduler: cosine
learning_rate: 0.000002

train_on_inputs: True # make sure you have this on True
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint: true
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true
flash_attn_cross_entropy: false
flash_attn_rms_norm: true
flash_attn_fuse_qkv: false
flash_attn_fuse_mlp: true

warmup_steps: 100
evals_per_epoch: 4
eval_table_size:
eval_sample_packing:
saves_per_epoch: 1
debug:
deepspeed: /home/josegomez15/axolotl/deepspeed_configs/zero2.json
weight_decay: 0.1
fsdp:
fsdp_config:
special_tokens:

```

</details><br>

# mistral-7B-PsychiatryCaseNotes-epochs-3-lr-000002

This model is a fine-tuned version of [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8637

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 5.0059        | 0.0   | 1    | 5.1706          |
| 2.457         | 0.25  | 626  | 2.0648          |
| 2.5571        | 0.5   | 1252 | 2.0728          |
| 2.3072        | 0.75  | 1878 | 1.9165          |
| 1.6655        | 1.0   | 2504 | 1.8590          |
| 1.6336        | 1.25  | 3130 | 1.8558          |
| 1.8686        | 1.5   | 3756 | 1.8526          |
| 1.6373        | 1.75  | 4382 | 1.8241          |
| 1.2849        | 2.0   | 5008 | 1.7712          |
| 1.1089        | 2.25  | 5634 | 1.8462          |
| 1.2999        | 2.5   | 6260 | 1.8523          |
| 1.0041        | 2.75  | 6886 | 1.8637          |


### Framework versions

- Transformers 4.38.0
- Pytorch 2.0.1+cu117
- Datasets 2.17.0
- Tokenizers 0.15.0
