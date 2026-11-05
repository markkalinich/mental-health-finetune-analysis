---
language:
  - sr
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
base_model: unsloth/Qwen3.5-9B
tags:
  - unsloth
  - merged-model
  - multi-label-classification
  - emotion-recognition
  - serbian
  - social-media
  - json-output
metrics:
  - f1
  - jaccard
---

# Serbian multi-label emotion recognition — Qwen3.5 9B merged model

## Model description

This is the direct-load, merged BF16 form of
[`te-sla/serbian-emotion-qwen3.5-9b-lora`](https://huggingface.co/te-sla/serbian-emotion-qwen3.5-9b-lora).
It combines the prespecified seed-42 LoRA adapter with
[`unsloth/Qwen3.5-9B`](https://huggingface.co/unsloth/Qwen3.5-9B) at pinned revision
`005429cee5cb648998cf2b70eebdd83175989c9a`, so users load one repository rather than loading a base
model and then attaching a PEFT adapter. The repository ID is
`te-sla/serbian-emotion-qwen3.5-9b`.

This is deployment packaging of the same evaluated model, not another training run, seed, or ranking
entry. The LoRA repository remains available as the smaller download; both formats carry the same
Round 12 scientific claim. TeslaXLM remains the primary publication encoder.

The model emits one strict JSON array containing zero, one, or two labels in the fixed order
`anger`, `anticipation`, `disgust`, `fear`, `joy`, `sadness`, `surprise`, `trust`.

## Intended use

Use this repository when simple one-repository loading is more important than the smaller adapter
download. It is intended for research on direct structured Serbian social-media emotion generation.
Do not use it for clinical assessment, inference about an author's mental state, employment,
law-enforcement, or other high-impact decisions.

## Training and merge provenance

- Original training: unquantized BF16 rank-16 LoRA, alpha 16, dropout 0, assistant-only causal loss.
- LoRA targets: attention projections and MLP projections; vision and audio remained frozen.
- Training data: 23,961 cleaned Serbian social-media rows; validation and test each contain 3,000 rows.
- Release artifact: prespecified seed 42, checkpoint 2247, selected on validation only.
- Merge: PEFT `merge_and_unload(safe_merge=True)` followed by Transformers safe serialization,
  preserving BF16 and using shards no larger than 5 GB.
- New optimization during merge: none.
- Verification: deterministic synthetic prompts must parse strictly and produce the same label sets
  before and after the merge. Exact source and release hashes are included in the repository.

The source adapter uses base revision `005429cee5cb648998cf2b70eebdd83175989c9a`. Test performance
did not select the uploaded seed or checkpoint.

## Evaluation

The merged package inherits the evaluation of the exact source adapter; it is not counted as an
additional evaluated model.

| Scope | Rows | Macro F1 | Sample Jaccard | Exact set | Invalid rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| Test, released seed 42 | 3,000 | 0.526192 | 0.591056 | 0.505333 | 0.000000 |
| Test family mean, 10 seeds | 3,000 per seed | 0.516697 | 0.589383 | 0.507767 | 0.000000 |

Macro-F1 sample SD across the ten seeds was `0.007589`; all 30,000 test outputs were valid under the
strict parser. The same test cohort informed earlier rounds, so these are adaptive internal results,
not independent external validation.

## Direct loading

This path loads the working merged checkpoint directly—there is no separate base-model or adapter
load:

```python
import json

import torch
from unsloth import FastModel

model_id = "te-sla/serbian-emotion-qwen3.5-9b"
model, tokenizer = FastModel.from_pretrained(
    model_name=model_id,
    max_seq_length=1024,
    dtype=torch.bfloat16,
    device_map={"": 0},
    load_in_4bit=False,
    load_in_8bit=False,
    load_in_16bit=True,
    full_finetuning=False,
    trust_remote_code=False,
)
FastModel.for_inference(model)

label_order = [
    "anger", "anticipation", "disgust", "fear",
    "joy", "sadness", "surprise", "trust",
]
system_prompt = (
    "Klasifikuj emocije izražene u srpskom tekstu. "
    "Dozvoljene oznake su: anger, anticipation, disgust, fear, joy, sadness, "
    "surprise, trust. Za tekst sa emocijom vrati jednu ili dve oznake. Ako "
    "nijedna dozvoljena emocija nije izražena, vrati prazan niz. Vrati isključivo "
    "ispravan JSON niz, bez objašnjenja, Markdowna ili oznake neutral. Oznake "
    "moraju biti u redosledu u kom su navedene."
)
text = "Danas sam presrećan zbog odličnih vesti."
messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": system_prompt}],
    },
    {
        "role": "user",
        "content": [{"type": "text", "text": text}],
    },
]
prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)
inputs = tokenizer(
    text=[prompt],
    return_tensors="pt",
    add_special_tokens=False,
).to("cuda")
with torch.inference_mode(), torch.autocast("cuda", dtype=torch.bfloat16):
    generated = model.generate(
        **inputs,
        do_sample=False,
        num_beams=1,
        max_new_tokens=32,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
response = tokenizer.batch_decode(
    generated[:, inputs["input_ids"].shape[1]:],
    skip_special_tokens=True,
)[0].strip()

# Strict validation; do not repair malformed output.
predicted = json.loads(response)
assert isinstance(predicted, list) and len(predicted) <= 2
assert len(predicted) == len(set(predicted))
assert all(label in label_order for label in predicted)
assert predicted == [label for label in label_order if label in predicted]
print(predicted)
```

The example contains the exact evaluated Serbian system prompt, disables thinking, uses greedy
decoding with at most 32 new tokens, and rejects malformed, duplicate, unknown, noncanonical,
neutral, or more-than-two-label outputs without repair.

## Included verification files

- `artifact_manifest.json`: size and SHA-256 for every packaged file except the manifest itself.
- `source_adapter_manifest.json`: exact adapter file hashes used for the merge.
- `merge_provenance.json`: base revision, adapter source, merge method, versions, and Git commit.
- `merge_smoke_test.json`: raw-output hashes, strict-parser status, and pre/post label equivalence on
  non-sensitive synthetic prompts.
- `publication_evidence.json`: the Round 12 family statistics and released-artifact metrics.

## Limitations

- The merged repository is much larger than the 116 MB LoRA adapter and still requires enough
  memory for a 9B 16-bit model; use the LoRA repository when storage or transfer size matters.
- The model emits label sets rather than calibrated probabilities.
- Strict JSON parsing is part of the evaluated system.
- The evidence covers Serbian Reddit and Twitter text, not external-domain generalization.
- The generator and thresholded encoders do not share one statistical output contract and must not
  be presented as a pooled universal leaderboard.

## Citation

The final paper identifier and citation are pending. The verified paper link and shared
portfolio citation will be added to both Qwen repositories when available.
