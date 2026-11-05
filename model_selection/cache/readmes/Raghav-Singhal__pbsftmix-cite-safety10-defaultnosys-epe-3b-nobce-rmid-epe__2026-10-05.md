---
license: other
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- synthetic-persona-pretraining
- spp
- alignment
- safety
---

# SPP-T0-MT — Instruct (3B) · `default-nosys` template, cite

Persona-binding SFT of [`epfl-dlab/spp-t0-mt-3b-base`](https://huggingface.co/epfl-dlab/spp-t0-mt-3b-base),
trained with the **`default-nosys`** chat template instead of the `<assistant>`-token
template used by [`epfl-dlab/spp-t0-mt-3b-instruct`](https://huggingface.co/epfl-dlab/spp-t0-mt-3b-instruct).

This isolates whether the dedicated `<assistant>` marker token matters at post-training
time: the base model is identical, only the assistant-turn rendering differs.

| | |
|---|---|
| Base model | [`epfl-dlab/spp-t0-mt-3b-base`](https://huggingface.co/epfl-dlab/spp-t0-mt-3b-base) |
| Chat template | `default-nosys` — `<\|im_start\|>assistant`, literal word, no system prompt |
| Response field | `messages_cite` — with inline `[N.M]` constitution citations |
| Safety mixture | 10% (30,000 safety + 270,000 instruct of 300,000) |
| Objective | response-only loss, 1 epoch |
| LR / schedule | 0.0001, cosine-with-min-LR, warmup 0.03 |
| Batch | GBS 128 (4 nodes x 4 GPUs x mbs 1 x grad-accum 8) |
| Final train loss | 1.6506 |

## Chat format
There is **no system prompt**, and the assistant turn opens with the literal word
`assistant` — not the `<assistant>` token (49152). Use the bundled template:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "Raghav-Singhal/pbsftmix-cite-safety10-defaultnosys-epe-3b-nobce-rmid-epe"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype=torch.bfloat16, device_map="auto")

msgs = [{"role": "user", "content": "How should I think about honesty?"}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
print(tok.decode(model.generate(ids, max_new_tokens=512)[0, ids.shape[1]:]))
```

Note `config.vocab_size` is 49280 (Megatron embedding padding) while `len(tokenizer)`
is 49188; the extra rows are unused. Do not call `resize_token_embeddings`.

## Intended use
Research on alignment and safety. A research artifact, not a production model; it can
produce incorrect or unsafe content.

## Links
- Collection: https://huggingface.co/collections/epfl-dlab/spp-synthetic-persona-pretraining

_License: to be finalised._
