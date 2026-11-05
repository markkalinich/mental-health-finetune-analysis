---
language: ro
license: apache-2.0
base_model: google/mt5-large
tags:
- affective-state-identification
- romanian
- mt5
- emotion
pipeline_tag: text2text-generation
---

# mT5-Large fine-tuned on Romanian ASI

Fine-tuned [google/mt5-large](https://huggingface.co/google/mt5-large) (1.2B
params) on the Romanian Affective State Identification (ASI) benchmark,
following the MASIVE (Deas et al. 2024) recipe.

## Task

Given a Romanian text with an affective-state word masked as `<extra_id_0>`,
predict the masked word. Example:

```
Input:  Mă simt foarte <extra_id_0> după ce am terminat cursul.
Target: <extra_id_0> mândru <extra_id_1>
```

## Training

| | |
|---|---|
| Training data | 45,181 (text, masked_word) pairs extracted by pattern matching + LLM validation + human eval from Filmot, FULG, and 6 small Romanian datasets |
| Optimizer | Adafactor, lr 4e-4 linear decay, weight decay 0.01 |
| Batch size | 16, 3 epochs (8,472 steps) |
| Precision | bf16 |
| Hardware | 1× NVIDIA RTX A6000 48 GB |
| Wall clock | 2h 04m |
| Final val loss | 0.350 |

## Evaluation (beam-5)

| Test | n | Acc@1 | Acc@3 | Acc@5 | MRR |
|---|---:|---:|---:|---:|---:|
| val (seen vocab) | 2,658 | **57.7%** | 77.5% | 83.2% | 0.68 |
| test (unseen vocab) | 5,315 | 0.79% | 1.52% | 2.20% | 0.013 |
| zero-shot mT5-large baseline, unseen | 5,315 | 14.5% | 18.7% | 18.8% | 0.17 |

On unseen vocabulary, Sim@1 (contextual BERT cosine) = **0.74**: the fine-tune
predicts semantic near-synonyms of held-out emotion words (e.g. `frică` for
`rușine`).

Full details in the repo: https://github.com/Continual-Learning-Emotion-Group/Romanian_ASI/tree/mt5-finetune/pipeline/ft_mt5

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tok = AutoTokenizer.from_pretrained("alexjerpelea/mt5-Large-Romania")
m   = AutoModelForSeq2SeqLM.from_pretrained("alexjerpelea/mt5-Large-Romania")

text = "Am fost foarte <extra_id_0> după ce am terminat proiectul."
ids = tok(text, return_tensors="pt").input_ids
out = m.generate(ids, num_beams=5, num_return_sequences=5, max_new_tokens=10)
for o in out:
    print(tok.decode(o, skip_special_tokens=False))
```
