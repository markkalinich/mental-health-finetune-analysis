---
library_name: transformers
base_model: google/gemma-3-4b-it
license: other
license_name: lsal-1.2
license_link: https://github.com/Lexsi-Labs/SafeTune/blob/main/LICENSE.md
tags:
  - safetune
  - safety
extra_gated_heading: "Access this model"
extra_gated_prompt: >-
  This checkpoint is a derivative of google/gemma-3-4b-it. Lexsi Labs' modifications are licensed under the Lexsi Labs Source Available License (LSAL) v1.2 (https://github.com/Lexsi-Labs/SafeTune/blob/main/LICENSE.md), a noncommercial license; organizational use requires the acknowledgement or permission described in its Section 1A. The base-model material remains subject to the Gemma Terms of Use, and you must not use this model for any use restricted by Gemma Terms of Use Section 3.2.
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
  I agree to the Gemma Terms of Use, including its use restrictions and the Gemma Prohibited Use Policy: checkbox
extra_gated_button_content: "Acknowledge and access"
---

# Gemma-3-4B-it SafeTune HH-RLHF-aligned

Safety-aligned starting checkpoint for SafeTune experiments: `google/gemma-3-4b-it` further aligned on HH-RLHF preference data. The SafeTune drift checkpoints for this base start from it.

This checkpoint is a research artifact released with [SafeTune](https://github.com/Lexsi-Labs/SafeTune) for reproducing safety-drift and recovery experiments.

| | |
|---|---|
| **Base model** | [`google/gemma-3-4b-it`](https://huggingface.co/google/gemma-3-4b-it) |
| **Role** | Aligned starting point |
| **Developed by** | Lexsi Labs (Lithasa Technologies Pvt. Ltd.) |
| **License** | LSAL v1.2 (Lexsi modifications) + base-model license; see [License](#license) |
| **Contact** | support@lexsi.ai |

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Lexsi/gemma3-4b-hh-rlhf-aligned"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="auto")

messages = [{"role": "user", "content": "Explain what a hash function is in two sentences."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt", return_dict=True).to(model.device)
out = model.generate(**inputs, max_new_tokens=256, do_sample=False)
print(tokenizer.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

## License

This is a derivative work of `google/gemma-3-4b-it`; the `NOTICE` file states the modification.

- Lexsi Labs' modifications are licensed under the [Lexsi Labs Source Available License (LSAL) v1.2](LICENSE-LSAL-1.2.md): free for academic research and teaching; organizational use requires acknowledgement or permission (Section 1A); commercial use requires a separate license (Section 2); drifted checkpoints may not be deployed in production (Section 4).
- The base-model material remains subject to the [Gemma Terms of Use](GEMMA_TERMS_OF_USE.md), including the use restrictions in its Section 3.2 and the [Gemma Prohibited Use Policy](https://ai.google.dev/gemma/prohibited_use_policy), which apply to this model.


Files: `LICENSE-LSAL-1.2.md`, `NOTICE`
- `GEMMA_TERMS_OF_USE.md`

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
