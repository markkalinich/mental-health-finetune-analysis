---
base_model: unsloth/Qwen3.5-0.8B
library_name: transformers
tags:
- security
- log-analysis
- merged-lora
- qwen3.5
- triage
- bf16
pipeline_tag: text-generation
---
# Qwen3.5 0.8B Security Triage v4-7 Merged

This repository contains a clean BF16 merged Transformers/Safetensors checkpoint for the AI Security Log Triage Assistant POC.

The LoRA adapter was merged into the base model with `merge_and_unload()` so the checkpoint does not include PEFT `lora_*` or `base_layer` weights and does not include a `quantization_config`. This export is intended for OpenAI-compatible serving with runtimes such as vLLM.

## Intended Use

The model is intended to triage short security log lines into the project output schema:

```json
{
  "label": "sql_injection_attempt",
  "severity": "high",
  "is_suspicious": true,
  "evidence": ["SLEEP(5)"],
  "reason": "The request contains a common SQL injection pattern.",
  "recommended_action": "Review web application logs and block or rate-limit the source IP."
}
```

Supported POC labels are `normal`, `failed_login_bruteforce`, `sql_injection_attempt`, `directory_traversal_attempt`, and `port_scan_or_recon`.

## Training Artifact

- Base model: `unsloth/Qwen3.5-0.8B`
- Adapter source: `qwen3-5-0-8b-security-triage-v4-7-auth-sqli-severity-calibration-lora`
- Project task: structured security log triage
- Training path: synthetic POC data from the AI Security Log Triage Assistant repository
- Merge format: clean BF16 Transformers/Safetensors checkpoint

## Limitations

This is a proof-of-concept triage model trained on synthetic data. It triages suspicious patterns and recommends investigation actions. It does not detect compromise, prove malicious activity, or replace analyst review.
