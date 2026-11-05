---
license: mit
base_model: microsoft/deberta-v3-large
language:
  - en
pipeline_tag: token-classification
tags:
  - emotion-cause-pair-extraction
  - sentiment-analysis
  - finance
  - reddit
---

# EconECPE tagger: DeBERTaV3-large

The **encoder efficiency variant** from *"EconECPE: A Span-Level Emotion-Cause
Dataset for Financial Social Media"* (Simone Adobati, Federico Lorenzo Bruno, Erik
Cambria; IEEE ICDM 2026 Workshops, SENTIRE). It tags typed emotion spans and typed
cause spans in one forward pass (≈81 comments/s, 3.7× the generative student),
but it is **not** the paper's labeler of record. For that, see
[`EconECPE/econecpe-qwen3.5-9b-lora`](https://huggingface.co/EconECPE/econecpe-qwen3.5-9b-lora).

**Data, code and specification:** [doi.org/10.5281/zenodo.22913761](https://doi.org/10.5281/zenodo.22913761) · code on GitHub: [EconECPE/EconECPE](https://github.com/EconECPE/EconECPE)

## Architecture

DeBERTaV3-large over the concatenated context and comment (512 tokens), with
three heads on the shared token representations:

- a typed emotion-span head (BIO, 15 labels = 7 emotions × B/I + O),
- a typed cause-span head (BIO, 35 labels = 17 cause categories × B/I + O),
- an intensity-regression head on emotion-span tokens.

Pairs are formed by a proximity heuristic: nearest cause span, backing off to a
self-span. Decoding drops spans shorter than 2 tokens and spans whose mean
confidence is below 0.5 (emotion and cause). The label lists and decode settings
are in `econecpe_tagger_config.json`.

## Results (gold set, 300 comments / 336 pairs)

Nested micro-F1 (%), as in the paper's Table IV:

| | E-span | +E | +CS | +C | Neut. |
|---|---|---|---|---|---|
| r/economics (in domain) | 50.2 | 45.5 | 14.3 | 12.1 | 80.7 |
| r/investing (zero-shot, 200 comments) | 39.1 | 34.5 | 8.5 | 4.6 | 72.0 |

The weak cause-span score is structural: 29.7% of its cause spans are copies of
its own emotion span (61.7% under transfer), the cost of proximity pairing
standing in for multi-pair decoding.

## How to use

`model.safetensors` is the state dict of `MultiHeadTagger` from the release's
`pipeline/deberta_train.py`:

```python
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
from pipeline.deberta_train import build_model   # from the EconECPE release

model = build_model("microsoft/deberta-v3-large", from_config=True)
model.load_state_dict(load_file(hf_hub_download(
    "EconECPE/econecpe-deberta-v3-tagger", "model.safetensors")))
```

or score it on the gold set with the release's evaluator, which accepts the
`.safetensors` file directly:
`python -m pipeline.deberta_eval --checkpoint model.safetensors ...`

## Limitations

- **Trained on model-generated labels** (the same multi-LLM silver consensus as
  the generative student), so it inherits their shared errors.
- Degrades sharply out of domain unless re-tuned on target-domain labels.
- Domain: r/economics, 2018–2026, English. **Not investment advice**, and not
  suitable for judging individual users.

## License

The weights follow the base model's license (MIT). The annotations it was trained
on are released under CC BY-NC 4.0.

## Citation

```bibtex
@inproceedings{adobati2026econecpe,
  title     = {{EconECPE}: A Span-Level Emotion-Cause Dataset for Financial Social Media},
  author    = {Adobati, Simone and Bruno, Federico Lorenzo and Cambria, Erik},
  booktitle = {2026 IEEE International Conference on Data Mining Workshops (ICDMW)},
  note      = {SENTIRE 2026 workshop},
  year      = {2026}
}
```
