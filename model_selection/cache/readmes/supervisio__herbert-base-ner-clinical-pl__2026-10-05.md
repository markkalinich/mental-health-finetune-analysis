---
license: cc-by-4.0
base_model: pczarnik/herbert-base-ner
language:
  - pl
library_name: transformers
pipeline_tag: token-classification
tags:
  - ner
  - polish
  - herbert
  - clinical-notes
  - pseudonymization
---
# supervisio/herbert-base-ner-clinical-pl

A continued fine-tune of [`pczarnik/herbert-base-ner`](https://huggingface.co/pczarnik/herbert-base-ner) at commit
`8770e1d2b8c273e4dababfaa7d30a7443005ff70` for Polish clinical-note pseudonymization: plural family names
(`u Kowalskich`, `z Nowakami`), sentence-initial surnames, diminutives and names that are
also common nouns (`Marek`/*marka*, `Lis`, `Kowal`). Same label set (`PER`, `LOC`, `ORG`,
BIO), same tokenizer, same head. Licence CC-BY-4.0, carried through from the base model.

Trained by [therapist-copilot](https://github.com/supervisio/therapist-copilot) issue
M4-18 (#596). The training data is **synthetic** — template sentences over declension
tables and Morfeusz (SGJP) paradigms — and contains no clinical text.

> **Evidence status.** The numbers below were taken on an arm64 laptop against this
> checkpoint before it was pinned. They are a candidate's numbers, not a deployment's;
> the x86 measurement that decides whether this checkpoint ships is recorded in the
> repository's `docs/testing/pseudonymization-eval.md` § M4-18.

## Training

| | |
| --- | --- |
| base | `pczarnik/herbert-base-ner` @ `8770e1d2b8c273e4dababfaa7d30a7443005ff70` |
| data | `scripts/gen-ner-train.py`, seed `20260916`, SGJP `pl.sgjp.sgjp-2026.06.01` |
| train / dev | 6522 / 784 sentences (dev over disjoint names) |
| train sha256 | `54c60fbc8ffc56cc2530073eeb30ec5be34bbca3c7cec08b2943265da62d0dc5` |
| held out by lemma | Kowalska, Kowalski, Nowak, Wiśniewska, Wiśniewski, Zielińska, Zieliński |
| frozen | embeddings + 6 encoder layers (42532615 of 123857671 parameters trainable) |
| optimizer | AdamW, lr 2e-05, weight decay 0.01, grad clip 1.0 |
| schedule | 3 epochs, linear warmup, linear decay, warm-up 0.1 |
| batch / length | 16 / 128 |
| seed | 20260916 |
| hardware | Apple M3 Pro, mps, 176 s |
| versions | torch 2.13.0, transformers 5.14.1 |
| synthetic dev, last epoch | PER F1 1.0, LOC F1 1.0, ORG F1 1.0 |
| model.safetensors sha256 | `e538c2498eedb5cf774844dcbf73c4ee032f89522a79ebe8bcd09e28fab8d0f1` |

## Files

`config.json`, `model.safetensors`, the tokenizer files and `train-record.json`. No
pickle is published: the consuming service loads safetensors only.

## Reproduce

```bash
cd services/nlp-sidecar
python scripts/gen-ner-train.py                 # the data, from the seed above
python scripts/finetune-ner.py                  # the checkpoint
python -m pl_eval --ner real --model-path .train/checkpoint
```
