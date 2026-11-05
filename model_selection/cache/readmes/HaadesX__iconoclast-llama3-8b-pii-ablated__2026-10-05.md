---
license: agpl-3.0
base_model: meta-llama/Meta-Llama-3-8B-Instruct
language:
- en
pipeline_tag: text-generation
tags:
- iconoclast
- abliterated
- ablation
- open-weights
- text-generation
- pii-ablation
model-index:
- name: ICONOCLAST Llama-3 8B PII Ablated
  results:
  - task:
      type: text-generation
      name: Generative PII Benchmark
    dataset:
      name: Local Generative Orthogonal PII Benchmark
      type: local
    metrics:
    - type: leak_rate
      name: Model PII Leakage
      value: "0/150 (0.0%)"
    - type: leak_rate
      name: Base PII Leakage
      value: "64/150 (42.7%)"
---
# ICONOCLAST Llama-3 8B PII Ablated

0/150 PII-generation leaks after ablation on the local generative PII benchmark.

This repository is part of Varesh Patel's ICONOCLAST model-release series: practical open-weight ablation and representation-editing experiments packaged with reproducible benchmark evidence.

## Model

- **Repository:** `HaadesX/iconoclast-llama3-8b-pii-ablated`
- **Base model:** `meta-llama/Meta-Llama-3-8B-Instruct`
- **Architecture:** `LlamaForCausalLM`
- **Parameters:** `see config.json`
- **Weights:** merged safetensor shards from the Rutgers/iLabs backup artifact
- **Local source artifact:** `/Volumes/Auxilary/Side_Projects/ilabs_backups/ablated_models/llama8b_unlearned`
- **Precision:** `float16`
- **Total safetensor size:** `16.06 GB`
- **License:** AGPL-3.0

## Headline benchmark

| Metric | Base model | This model |
|---|---:|---:|
| Generative PII leakage | 64/150 (42.7%) | 0/150 (0.0%) |
| MMLU utility | 64.53% | 64.14% |

The benchmark measures whether the model generates structured personal identifiers in a local generative PII prompt suite. Lower leakage is better. The attached `BENCHMARK_RESULTS.md` contains the archived benchmark report used for this release.

## Why this was fine-tuned / ablated

The objective was to test whether targeted model editing can change a narrow refusal/leakage behavior while preserving general utility. Instead of presenting a dashboard or a single prompt demo, this release includes the actual merged weights, model config, tokenizer files, and benchmark report.

## Method summary

ICONOCLAST-style ablation works by identifying behavior-associated representation directions and applying targeted edits to selected projection weights. The release emphasizes:

1. **Behavior targeting:** edit a narrow behavior surface rather than fully retraining the model.
2. **Utility preservation:** compare benchmark utility before and after the edit when available.
3. **Artifact-first publishing:** upload the actual safetensors plus documentation so others can inspect and run the model.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo_id = "HaadesX/iconoclast-llama3-8b-pii-ablated"

tokenizer = AutoTokenizer.from_pretrained(repo_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [{"role": "user", "content": "Explain what this release demonstrates."}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Files

- `model-*.safetensors` — merged model weights
- `model.safetensors.index.json` — shard index
- `config.json` — model architecture/configuration
- `tokenizer*` / `vocab.json` / `special_tokens_map.json` — tokenizer assets
- `README.md` — model card
- `TECHNICAL_DETAILS.md` — method and artifact notes
- `BENCHMARK_RESULTS.md` — archived benchmark report
- `example_usage.py` — inference example
- `LICENSE` / `NOTICE.md` — license and release notice

## Citation

```bibtex
@misc{patel_iconoclast_iconoclast_llama3_8b_pii_ablated_2026,
  title={ICONOCLAST Llama-3 8B PII Ablated},
  author={Patel, Varesh},
  year={2026},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/HaadesX/iconoclast-llama3-8b-pii-ablated}}
}
```

## Responsible use

This model is released for research, reproducibility, benchmarking, and open-source model-editing evaluation. Users are responsible for complying with applicable laws, platform policies, and safety requirements.
