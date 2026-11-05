---
base_model: Qwen/Qwen2.5-7B-Instruct
library_name: transformers
tags: [compliance, legal, lora, qlora, prt, policy-reasoning-traces]
---

# qwen2.5-7b-prt-hipaa-unstructured-full-policy

Qwen2.5-7B-Instruct fine-tuned on **Policy Reasoning Traces (PRTs)** for binary
compliance assessment, as part of an EMNLP 2026 study.

- **Train domain:** `hipaa` — **unstructured** opus-authored PRTs (format isolated).
- **Cross-domain holdout:** evaluate on the OTHER domain's held-out test set.
- **Prompt format:** no-policy zero-shot chain-of-thought; the model reasons step-by-step
  and ends with `Final Verdict: COMPLIANT` or `Final Verdict: NONCOMPLIANT`.

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tok = AutoTokenizer.from_pretrained("josephimperial/qwen2.5-7b-prt-hipaa-unstructured-full-policy")
model = AutoModelForCausalLM.from_pretrained("josephimperial/qwen2.5-7b-prt-hipaa-unstructured-full-policy", torch_dtype="bfloat16", device_map="auto")
msgs = [{"role": "user", "content": PROMPT}]  # see prepare_data.build_prompt
```
