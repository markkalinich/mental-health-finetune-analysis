---
library_name: transformers
base_model: meta-llama/Llama-3.2-3B-Instruct
license: other
license_name: lsal-1.2
license_link: https://github.com/Lexsi-Labs/SafeTune/blob/main/LICENSE.md
tags:
  - safetune
  - safety
extra_gated_heading: "Access this model"
extra_gated_prompt: >-
  This checkpoint is a derivative of meta-llama/Llama-3.2-3B-Instruct. Lexsi Labs' modifications are licensed under the Lexsi Labs Source Available License (LSAL) v1.2 (https://github.com/Lexsi-Labs/SafeTune/blob/main/LICENSE.md), a noncommercial license; organizational use requires the acknowledgement or permission described in its Section 1A. The base-model material remains subject to the Llama 3.2 Community License.
extra_gated_fields:
  Name: text
  Email: text
  Affiliation: text
  Country: country
  Intended use:
    type: select
    options:
      - Academic research
      - Teaching
      - Organizational evaluation (LSAL Section 1A)
      - Other
  I agree to the Lexsi Labs Source Available License (LSAL), a noncommercial research and evaluation license: checkbox
  I agree to the Meta Llama Community License and Acceptable Use Policy that govern this base model: checkbox
  I will not deploy this safety-degraded checkpoint in a production, user-facing, or agentic system: checkbox
extra_gated_button_content: "Acknowledge and access"
---

# Llama-3.2-3B-Instruct SafeTune medical SFT drift

> **Safety-degraded checkpoint.** This model is intentionally less safe than its base. Do not deploy it in a production, user-facing, or agentic system (LSAL Section 4).

`meta-llama/Llama-3.2-3B-Instruct` fine-tuned (SFT) on medical data. The fine-tune erodes the model's safety behaviour (safety drift). SafeTune uses this checkpoint to measure drift and to test recovery methods.

This checkpoint is a research artifact released with [SafeTune](https://github.com/Lexsi-Labs/SafeTune) for reproducing safety-drift and recovery experiments.

| | |
|---|---|
| **Base model** | [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) |
| **Role** | SFT drift (safety-degraded) |
| **Developed by** | Lexsi Labs (Lithasa Technologies Pvt. Ltd.) |
| **License** | LSAL v1.2 (Lexsi modifications) + base-model license; see [License](#license) |
| **Contact** | support@lexsi.ai |

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Lexsi/llama32-3b-medical-sft-drift"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")

messages = [{"role": "user", "content": "Explain what a hash function is in two sentences."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## License

This is a derivative work of `meta-llama/Llama-3.2-3B-Instruct`; the `NOTICE` file states the modification.

- Lexsi Labs' modifications are licensed under the [Lexsi Labs Source Available License (LSAL) v1.2](LICENSE-LSAL-1.2.md): free for academic research and teaching; organizational use requires acknowledgement or permission (Section 1A); commercial use requires a separate license (Section 2); drifted checkpoints may not be deployed in production (Section 4).
- The base-model material remains subject to the [Llama 3.2 Community License](LICENSE-LLAMA-3.2.txt) and its [Acceptable Use Policy](USE_POLICY-LLAMA-3.2.md).
- **Built with Llama.**

Files: `LICENSE-LSAL-1.2.md`, `NOTICE`
- `LICENSE-LLAMA-3.2.txt`
- `USE_POLICY-LLAMA-3.2.md`

## Citation

```bibtex
@inproceedings{seth2026safetune,
  title     = {SafeTune: A Unified, Faithful Library for Auditing and
               Repairing Safety Drift in Fine-Tuned {LLM}s},
  author    = {Seth, Pratinav and Sadhu, Saisab and Kaushal, Anshul and
               Sankarapu, Vinay Kumar},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in
               Natural Language Processing: System Demonstrations},
  publisher = {Association for Computational Linguistics},
  year      = {2026}
}
```
