---
license: apache-2.0
library_name: pytorch
tags:
- pii
- masked-language-modeling
- redaction
- privacy
- webgpu
pipeline_tag: fill-mask
---

# PII ModernBERT 110M MLM 3B Warmup

This is the encoder warmup checkpoint for the open-source PII_MODEL browser-local redaction project.
It is a custom PyTorch ModernBERT-style masked-language-model checkpoint intended as the base for the final span-level PII token classifier.

## Important Status

- This is **not yet the final PII redaction classifier**.
- It is a masked-language-model warmup checkpoint trained before supervised PII span fine-tuning.
- The architecture is custom and should be loaded with the `pii_model.modeling` code from the project repository.

## Training Summary

- Hub repo: `soumikmahato/pii-modernbert-110m-mlm-3b`
- Tokenizer: `soumikmahato/pii-redactor-tokenizer-v1`
- Tokens seen: `3000008704`
- Parameters: `109408512`
- Final logged loss: `3.3695396184921265`
- Final logged EMA loss: `2.989036085762805`
- Context length: `8192`
- Hidden size/layers/heads: `768` / `12` / `12`
- Local attention window: `512`
- Global attention every N layers: `3`

## Files

- `model.safetensors`: model-only state dict from the final MLM checkpoint.
- `config.json`: custom `PiiEncoderConfig`.
- `training_state.json`: final trainer state and corpus summary.
- `summary.json`: training summary emitted by the trainer.
- `metrics.jsonl`: logged training metrics.
- `checkpoint.pt`: optional raw trainer checkpoint if included in this export.

## Intended Use

Use this checkpoint to initialize supervised PII span classification training. Do not ship this warmup model alone as a redactor.

## Privacy Boundary

The target product is a local Chrome extension that redacts sensitive spans before prompts are sent to AI chatbots. Raw user text and redaction maps should remain on-device.

