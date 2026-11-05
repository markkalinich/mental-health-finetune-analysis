---
license: apache-2.0
datasets:
- synapsecai/synthetic-sensitive-information
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
---

Model Information

model_name = "NousResearch/Llama-2-7b-chat-hf"

dataset_name = "synapsecai/synthetic-sensitive-information"


QLoRA parameters

lora_r = 32

lora_alpha = 8

lora_dropout = 0.1


BitsAndBytes parameters

use_4bit = True

bnb_4bit_compute_dtype = "float16"

bnb_4bit_quant_type = "nf4"

use_nested_quant = False


Training Arguments parameters

num_train_epochs = 1

fp16 = False

bf16 = False

per_device_train_batch_size = 32

per_device_eval_batch_size = 8

gradient_accumulation_steps = 4

gradient_checkpointing = True

max_grad_norm = 0.3

learning_rate = 2e-4

weight_decay = 0.001

optim = "paged_adamw_32bit"

lr_scheduler_type = "cosine"

max_steps = -1

warmup_ratio = 0.03

group_by_length = True

save_steps = 0

logging_steps = 25


SFT parameters

max_seq_length = None

packing = False
This model is an ethically fine-tuned version of Llama 2, specifically trained to detect and flag private or sensitive information within natural text. It serves as a powerful tool for data privacy and security, capable of identifying potentially vulnerable data such as:

API keys
Personally Identifiable Information (PII)
Financial data
Confidential business information
Login credentials

Key Features:

Analyzes natural language input to identify sensitive content
Provides explanations for detected sensitive information
Helps prevent accidental exposure of private data
Supports responsible data handling practices

Use Cases:

Content moderation
Data loss prevention
Compliance checks for GDPR, HIPAA, etc.
Security audits of text-based communications

This model aims to enhance data protection measures and promote ethical handling of sensitive information in various applications and industries.