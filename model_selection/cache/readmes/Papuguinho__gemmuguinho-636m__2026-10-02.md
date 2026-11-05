---
license: gemma
language:
- pt
library_name: transformers
pipeline_tag: text-generation
base_model:
- google/gemma-3-270m
tags:
- aac
- augmentative-alternative-communication
- caa
- pictograms
- accessibility
- assistive-technology
- mixture-of-experts
- moe
- gemma3
- portuguese
- brazilian-portuguese
- llama-cpp
- on-device
- speech-therapy
model-index:
- name: gemmuguinho-636m
  results:
  - task:
      type: text-generation
      name: AAC Pictogram Board Generation (pt-BR)
    dataset:
      type: custom
      name: Papuguinho AAC pt-BR (synthetic)
    metrics:
    - type: llm-judge
      name: Discriminative LLM Judge (0-10)
      value: 9.16
---

<div align="center">
  <img src="gemmuguinho.jpg" alt="Gemmuguinho" width="200"/>

# Gemmuguinho: a compact MoE language model for AAC pictogram boards in Brazilian Portuguese

*Gemma + Papuguinho — born to communicate*

![License](https://img.shields.io/badge/license-Gemma-4c1.svg)
![Language](https://img.shields.io/badge/language-Portuguese_(pt--BR)-009c3b.svg)
![Params](https://img.shields.io/badge/params-636M_total_·_~212M_active-ff8800.svg)
![Architecture](https://img.shields.io/badge/arch-gemma3moe_(MoE)-8a2be2.svg)
![Runtime](https://img.shields.io/badge/runtime-llama.cpp_·_CPU-555.svg)
![GGUF](https://img.shields.io/badge/GGUF-available-1abc9c.svg)

</div>

**A sovereign, CPU-friendly Mixture-of-Experts language model that generates Augmentative and Alternative
Communication (AAC/CAA) pictogram boards in Brazilian Portuguese** — and edits them by natural-language
command. Built for [Papuguinho](https://www.papuguinho.com) to run fully on-device (no GPU) via `llama.cpp`.

The name **Gemmuguinho** combines the base architecture (**Gemma**-3 by Google) with the **Papuguinho**
project it was born from — much like the mascot image: a hatchling with its own identity, grown from another's egg.

> **TL;DR** — Type *"Quero uma prancha de escola"* → get a ready-to-use 12-pictogram communication board.
> Ask *"adiciona 3 frutas"* or *"apagar pictograma do cachorro"* → get a structured edit plan. ≈212M active params (top-2), ≈90–130 tok/s on CPU.

- 🧩 **Task:** AAC pictogram board generation + board editing (speech-therapy / assistive tech)
- 🌎 **Language:** Brazilian Portuguese (pt-BR)
- ⚙️ **Architecture:** `gemma3moe` — Gemma-3-270m upcycled to an 8-expert MoE (top-2)
- 💾 **Size:** ≈636M total · ≈212M active (k=2, default) · runs on CPU, no GPU needed
- 📦 **GGUF builds:** [gemmuguinho-636m-GGUF](https://huggingface.co/Papuguinho/gemmuguinho-636m-GGUF)

---

## Model Description

Gemmuguinho is a small **Mixture-of-Experts (MoE)** language model specialized for **AAC (Augmentative and
Alternative Communication)**. AAC boards are grids of pictograms that non-verbal or minimally-verbal people —
often autistic children or people with speech disorders — use to communicate. Building good boards by hand is slow;
this model produces coherent, thematically-balanced boards in seconds, on commodity hardware.

It is **upcycled** from Google's [`gemma-3-270m`](https://huggingface.co/google/gemma-3-270m): the vocabulary
was trimmed to a compact 64k Portuguese-focused set via
[`embedding-vocab-trimmer`](https://github.com/papuguinho/embedding-vocab-trimmer), and every dense feed-forward
block was replaced by a routed MoE block (8 experts, top-2) via
[`gemma3moe-builder`](https://github.com/papuguinho/gemma3moe-builder). Experts were **diversely seeded**
(Branch-Train-miX style) from `gemma-3-270m` (base), `gemma-3-270m-it` (instruct), a board fine-tune, and a
distilled variant, then trained on the AAC corpus. The result runs on `llama.cpp` with a custom `gemma3moe` architecture.

## Intended Use

| ✅ Use it for | ⚠️ Not designed for |
|---|---|
| Generating AAC/CAA pictogram boards in pt-BR | Languages other than Brazilian Portuguese |
| Editing boards via natural-language commands (add/remove/retitle) | Open-domain chat / general assistant use |
| On-device / offline assistive-communication apps | Medical, legal, or safety-critical decisions |
| Speech-therapy and special-education tooling | Factual question answering |

### Two modes

1. **Board generation (chatbot):** *"quero uma prancha de X"* → a board (default **12** pictograms; a specific
   count can be requested, e.g. *"gera 5 pictogramas para usar no dentista"*).
2. **Board editing (agent):** given the current board + a command, it returns a compact **edit DSL** —
   `R|` confirmation, `+|` add, `-|` remove, `T|` retitle, `C|` columns, `X|` new theme.

Each board line is `label|category|search_terms` (category ∈ s/v/a/e/p/l).

## How to Use

### `llama.cpp` (recommended — CPU / on-device)

Use the [GGUF repo](https://huggingface.co/Papuguinho/gemmuguinho-636m-GGUF):

```bash
llama-cli -m gemmuguinho-636m-Q8_0.gguf --jinja \
  -sys "$(cat corpo_chatbot.txt)" \
  -p "quero uma prancha de escola" -n 200 -st
```

### Transformers (safetensors, `trust_remote_code`)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "Papuguinho/gemmuguinho-636m"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, trust_remote_code=True, dtype=torch.float32).eval()

msgs = [{"role": "system", "content": SYSTEM_PROMPT},   # see corpo_chatbot.txt
        {"role": "user", "content": "quero uma prancha de escola"}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt", return_dict=True)
out = model.generate(ids["input_ids"], max_new_tokens=200, do_sample=False)
print(tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True))
```

> ⚠️ Generate **single-sequence** (batch size 1). Left-padded batched generation can corrupt outputs due to
> Gemma-3's sliding-window attention.

## Training Data

Brazilian-Portuguese corpus of **44,865** examples (683 held out for validation), mixing:
- **Board generation** (≈34.7k): themed AAC boards produced by teacher LLMs from a curated pictogram catalog.
- **Editing commands** (≈10.8k): natural-language edit instructions → edit-DSL plans, including typos and
  refusal/no-op cases.

Teachers: a mix of Gemini models. No human data; no personal data.

## Evaluation

Scored by a **discriminative LLM judge** (0–10 rubric: theme coherence, concentration/dispersion balance,
picturability, usefulness). Reference points on the same rubric: a 1B dense baseline scores **7.8**, the
teacher ≈ **9.2**.

| Model | Judge (0–10) | Notes |
|---|---|---|
| **Gemmuguinho (MoE 636M, top-2)** | **≈ 9.1** | near-teacher board quality |
| 1B dense baseline | 7.8 | reference |
| 2B dense baseline | 8.4 | reference |
| 4B dense baseline | 9.0 | reference |
| Teacher (Gemma4 31B) | 9.2 | upper reference |

Command-following (edit DSL) is reliable across quantizations, including exact-count adds and id-correct removals.

## Limitations & Safety

- pt-BR only; board vocabulary reflects the synthetic training catalog.
- Not a general chatbot and not a source of factual/medical information.
- Built-in scope guard: it only edits **children's AAC boards**. Health, hygiene, body, and difficult emotions
  are treated as legitimate; clearly adult or harmful content is refused with a short, gentle message.
- Outputs should be reviewed by a caregiver, educator, or speech-language therapist before use.

## Technical Specifications

| | |
|---|---|
| Base model | `google/gemma-3-270m` (vocab trimmed to 64k) |
| Architecture | `gemma3moe` — Gemma-3 with routed MoE FFN |
| Experts | 8 total, top-2 active by default (softmax + renormalized); `k` selectable at runtime |
| Parameters | ≈636M total · active: ≈141M (k=1) / ≈212M (k=2) / ≈283M (k=3) |
| Layers / hidden | 18 / 640 |
| Context | inherits Gemma-3-270m |
| Inference | `llama.cpp` (CPU), or Transformers |

## Related Resources

| Resource | Description |
|---|---|
| ⚡ [gemmuguinho-636m-GGUF](https://huggingface.co/Papuguinho/gemmuguinho-636m-GGUF) | GGUF quantizations for `llama.cpp` |
| 🔍 [aac-pictogram-retriever-ptbr-GGUF](https://huggingface.co/Papuguinho/aac-pictogram-retriever-ptbr-GGUF) | Semantic pictogram retriever (157M, CPU) |
| 🔧 [gemma3moe-builder](https://github.com/papuguinho/gemma3moe-builder) | Tool for converting dense models to MoE |
| ✂️ [embedding-vocab-trimmer](https://github.com/papuguinho/embedding-vocab-trimmer) | Vocabulary pruning for multilingual embedding models |
| 🌐 [Papuguinho](https://www.papuguinho.com) | The AAC system this model powers |
| 🖨️ [Estúdio Papuguinho](https://estudio.papuguinho.com) | AI-powered printable board generator |

## Citation

```bibtex
@misc{stekel2026gemmuguinho,
  title  = {Gemmuguinho: a compact MoE language model for AAC pictogram boards in Brazilian Portuguese},
  author = {Stekel, Tardelli R. C. and Antonelli, Manuela and Baroni, Gabriel P. and {Carvalho Neto}, José A. and Souza, Marcela J. V.},
  year   = {2026},
  note   = {Papuguinho, https://www.papuguinho.com},
  url    = {https://huggingface.co/Papuguinho/gemmuguinho-636m},
  doi    = {10.57967/hf/9931}
}
```

**Project:** [Papuguinho](https://www.papuguinho.com) · **License:** [Gemma](https://ai.google.dev/gemma/terms)
