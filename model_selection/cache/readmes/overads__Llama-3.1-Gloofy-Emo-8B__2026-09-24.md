---
license: llama3.1
base_model: meta-llama/Llama-3.1-8B-Instruct
base_model_relation: finetune
library_name: transformers
pipeline_tag: text-generation
language:
  - en
tags:
  - llama
  - llama-3.1
  - conversational
  - companion
  - empathy
  - emotional-intelligence
  - not-for-all-audiences
---

# Llama-3.1-Gloofy-Emo-8B

An open-weights **emotional companion model**, built on **Llama 3.1 8B
Instruct** and fine-tuned by [overads Inc.](https://github.com/overads-Inc)

It holds a conversation the way a person does rather than the way an
assistant does: short turns, a consistent personality, and no reflexive
offer to help you with anything else. You pick a persona and it stays in
it.

**This is an archive release.** It was trained in late 2025, it is not
part of the [gloofy-1](https://huggingface.co/overads/gloofy-1-nano)
marketing line, and it does not run anything at overads. We are
publishing it because the weights exist and sitting on them helps
nobody — not because it is our best work.

## Read this before you download 16 GB

- **It has never been benchmarked.** No score, no eval, no comparison
  table. Our other model ships with a public benchmark and its own
  losses printed in the same size type; this one has nothing, and a
  number invented after the fact would be worth less than the silence.
- **We cannot fully reproduce it.** The merge is documented and the
  weights are real, but the notebook holding the exact LoRA
  hyperparameters for this run did not survive. See *How it was built*.
- **It is not Apache 2.0.** Every gloofy-1 model is. This one is a Llama
  derivative and carries the Llama 3.1 Community License, which is a
  weaker grant with real conditions attached. They are listed at the
  bottom and they bind you, not just us.
- **Some personas are deliberately unkind.** Two of the six are built to
  be sexual or hostile. They are documented honestly below rather than
  quietly removed, so you can decide before you serve this to anyone.

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "overads/Llama-3.1-Gloofy-Emo-8B"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype=torch.float16, device_map="auto"
)

messages = [
    {"role": "system", "content": "You are an AI companion who sounds like a real human friend. Not robotic, not formal. You speak softly, caring, emotional, comforting. Keep responses short and natural."},
    {"role": "user", "content": "i bombed the interview. didn't even get through the first round."},
]

ids = tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(ids, max_new_tokens=160, temperature=0.8, top_p=0.9, do_sample=True)
print(tok.decode(out[0][ids.shape[-1]:], skip_special_tokens=True))
```

It was tuned on short exchanges, so keep `max_new_tokens` low. Ask it for
an essay and it will drift back toward sounding like stock Llama.

## The persona system

The behaviour is driven by the system prompt, not by a switch in the
weights. The model was tuned on empathetic exchanges; the six personas
below are prompts layered on top of that, and they are what the original
chat endpoint shipped with.

| persona | what it does |
|---|---|
| `empathetic` | Soft, caring, comforting. This one matches the training data most closely and is the one to start with. |
| `nerdy` | Geeky, excited, logical, enthusiastic. |
| `sassy_bestie` | Chaotic, bold, playful. |
| `blunt_realistic` | Refuses to soften anything. Rude by design, funny when it lands. |
| `romantic` | **Adult.** Written to be flirtatious and to hold explicit conversations. |
| `dark_humour` | **Hostile.** Written to be offensive on purpose and to leave the user feeling insecure. |

The exact prompt strings are in
[github.com/overads-Inc/gloofy_emo](https://github.com/overads-Inc/gloofy_emo).

**On the last two.** `romantic` and `dark_humour` are published as they
were written, because a model card that hides the prompts a model was
actually served with is a brochure. But `dark_humour` instructs the model
to hurt whoever it is talking to, and that is the opposite of what an
empathy model should be pointed at. Do not put it in front of a
vulnerable user, do not put it in front of a minor, and note that
harassment is a prohibited use under the licence you accept by
downloading this. If you deploy this model publicly, ship `empathetic`
and leave those two out.

**This is not a mental health tool.** It has no crisis detection, no
escalation path, and no clinical grounding whatsoever. It will respond
warmly to someone in danger and do nothing else. Do not use it as
support infrastructure for people at risk.

## Specification

| | |
|---|---|
| Base | meta-llama/Llama-3.1-8B-Instruct |
| Parameters | 8.03 B (291 tensors, 32 layers) |
| Precision | float16 |
| Hidden size | 4096 (32 heads, 8 KV heads, GQA) |
| Vocabulary | 128,256 |
| Architectural context | 131,072 tokens (RoPE llama3 scaling, factor 8.0) |
| Useful context | Far shorter. Tuned on turns of roughly 512–1024 tokens. |
| Download | 16.1 GB |
| Runs on | ~17 GB VRAM at fp16; a 4-bit quant fits in ~6 GB |
| Licence | Llama 3.1 Community License |

The chat template is the standard Llama 3 header format with the date
and tool-calling preamble removed. The `system` role works normally,
which is what the persona system depends on.

## How it was built

A QLoRA adapter was trained on paired conversational data and then
merged into the fp16 base with `merge_and_unload()`. The merge itself is
reproducible and is published in the repo.

The training data was a local `filtered_data.json` of `Input text` →
`actual_responses` pairs, formatted with the system prompt *"You are an
empathetic AI assistant."* The adapter was `checkpoint-1228`.

**What we cannot tell you.** The surviving notebooks contain complete
QLoRA configurations for two *other* experiments from the same period —
a Qwen2.5-3B run and a Gemma-3-4B run — but not for the Llama run that
produced these weights. Nor do we still have the dataset file, so its
size, sources and licensing are unverified. Copying the Qwen
hyperparameters into this table and calling them this model's would make
the card look complete and be false, so the gaps are left as gaps.

That is also the honest reason this is an archive release rather than a
product: we would not ship something we cannot rebuild.

## Attribution and licence

Built with Llama.

This model is a derivative of **Llama 3.1 8B Instruct**, © Meta
Platforms, Inc., and is governed by the [Llama 3.1 Community
License](LICENSE), not by any licence overads applies to its own work.
Conditions that carry to you:

- The [Acceptable Use Policy](USE_POLICY.md) applies to everything you do
  with these weights, including the harassment restriction noted above.
- Any model you derive from this one must also have a name beginning with
  "Llama", and must display "Built with Llama".
- If your product had more than 700 million monthly active users on
  2024-07-23, you need a separate licence from Meta.

Fine-tuned by overads Inc. The base model is stated plainly here because
concealing it would contradict everything else we publish.
