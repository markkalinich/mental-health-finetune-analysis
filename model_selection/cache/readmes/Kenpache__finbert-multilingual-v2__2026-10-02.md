---
language:
- en
- zh
- ja
- es
- de
- fr
- ar
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: jhu-clsp/mmBERT-base
datasets:
- Kenpache/financial-sentiment-eval-7lang
metrics:
- accuracy
- f1
tags:
- finance
- financial-sentiment
- sentiment-analysis
- multilingual
- financial-news
- fintech
- trading
- market-sentiment
- text-classification
- modernbert
- mmbert
- cross-lingual
---

# Financial Sentiment, 7 Languages

**Sentiment of financial news, in seven languages, from one model.** Feed it a headline
or a sentence in English, Chinese, Japanese, Spanish, German, French or Arabic — get
back `negative`, `neutral` or `positive`.

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Kenpache/finbert-multilingual-v2")

clf("The company reported record quarterly earnings, driven by strong demand.")
# [{'label': 'positive', 'score': 0.9456}]

clf("Die Aktie verlor nach der Gewinnwarnung deutlich an Wert.")
# [{'label': 'negative', 'score': 0.9324}]

clf("该公司宣布大规模裁员计划，股价应声下跌。")
# [{'label': 'negative', 'score': 0.9406}]
```

| | |
|---|---|
| **Task** | Financial sentiment, 3 classes (negative / neutral / positive) |
| **Languages** | **7** — en · zh · ja · es · de · fr · ar |
| **Accuracy** | **87.2%** |
| **Parameters** | 307M (fp32, 1.2 GB) |
| **Backbone** | [`jhu-clsp/mmBERT-base`](https://huggingface.co/jhu-clsp/mmBERT-base) (ModernBERT) |

One model covers all seven languages — no per-language checkpoints, no translation step,
no language ID in front of it. Mixed-language pipelines just work.

**Larger sibling:**
[`Kenpache/finbert-multilingual-v2-large`](https://huggingface.co/Kenpache/finbert-multilingual-v2-large)
— 560M parameters, 88.9% on the same evaluation set. Take that one for accuracy, this
one for footprint.

---

## Accuracy

Measured on a held-out test set of **4,993 financial news sentences** across the seven
languages, published as
[`Kenpache/financial-sentiment-eval-7lang`](https://huggingface.co/datasets/Kenpache/financial-sentiment-eval-7lang).

| Metric | Score |
|---|---|
| **Accuracy** | **0.8724** |
| **F1 (weighted)** | **0.8724** |

### Per language

This is the table to read before adopting the model — it tells you whether *your*
language is covered properly, not just the average.

| Language | | Items | Accuracy |
|---|---|---:|---:|
| Spanish | `es` | 905 | **0.8950** |
| Chinese | `zh` | 1,023 | **0.8935** |
| German | `de` | 650 | 0.8785 |
| Arabic | `ar` | 73 | 0.8767 |
| Japanese | `ja` | 1,063 | 0.8702 |
| English | `en` | 780 | 0.8410 |
| French | `fr` | 499 | 0.8337 |

**The spread between the best and worst language is 6 points**, and English is not at the
top — Spanish and Chinese are. That matters more than it looks: most "multilingual"
financial models are English models with a multilingual tokenizer, and they collapse on
CJK and right-to-left text. This one holds its level across scripts — Latin, Chinese,
Japanese and Arabic alike.

Arabic is measured on 73 items, so treat its number as indicative rather than precise.

### Reproducing these numbers

The evaluation set is public, and so is the protocol — `max_length=192`, fp32, raw text
with no normalisation:

```python
import pandas as pd, torch
from datasets import load_dataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer

ds = load_dataset("Kenpache/financial-sentiment-eval-7lang", split="test").to_pandas()

REPO = "Kenpache/finbert-multilingual-v2"
tok = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForSequenceClassification.from_pretrained(REPO).eval()

preds = []
with torch.no_grad():
    for i in range(0, len(ds), 64):
        enc = tok(ds.sentence[i:i + 64].tolist(), return_tensors="pt",
                  padding=True, truncation=True, max_length=192)
        preds += [model.config.id2label[j].lower()
                  for j in model(**enc).logits.argmax(-1).tolist()]

print((pd.Series(preds) == ds.label).mean())   # 0.8724
```

### Per class

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| negative | 0.8658 | 0.8913 | 0.8784 | 1,260 |
| neutral | 0.8683 | 0.8587 | 0.8635 | 2,158 |
| positive | 0.8835 | 0.8762 | 0.8798 | 1,575 |

No class collapse: the three F1 scores sit within 1.6 points of each other, and `neutral`
— the majority class, and the usual dumping ground for models that learned to hedge — has
the *lowest* F1 of the three rather than the highest.

**Polarity errors are rare.** Across all 4,993 items, `negative` is called `positive` 19
times and `positive` is called `negative` 32 times — **51 cases, 1.0% of the set**.
Practically all remaining error sits on the boundary with `neutral`. The model may fail to
register a weak signal; it very seldom reverses one.

### Comparison on the English subset

Both models were run on the **English portion — 780 items — of
[`Kenpache/financial-sentiment-eval-7lang`](https://huggingface.co/datasets/Kenpache/financial-sentiment-eval-7lang)**,
under one identical protocol: `max_length=192`, fp32, raw text, argmax over the three
classes, no tuning or threshold fitting for either model.

| Model | Accuracy | F1 (weighted) |
|---|---:|---:|
| **This model** | **0.8410** | **0.8410** |
| [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) | 0.7218 | 0.7224 |

Two things belong next to those numbers. `ProsusAI/finbert` is an English-only model, so
the comparison is confined to the English subset — which is, as the table above shows,
this model's weakest language of the seven. And it was trained under a different
annotation convention: most of its errors on this set are neutral items assigned a
direction, so part of the gap reflects differing label conventions rather than capability.

**These figures describe behaviour on this evaluation set only, under the protocol stated
above. They are not a general claim about either model.**

### Cross-benchmark check: Financial PhraseBank

A model tends to look good on the benchmark its own authors picked, so here is the mirror
image of the table above — the same two models on
[Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank)
(Malo et al., 2014), the long-standing English benchmark in this field, all **4,846
sentences**, under the identical protocol.

| Model | Accuracy | F1 (weighted) |
|---|---:|---:|
| [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) | **0.8896** | 0.8908 |
| **This model** | 0.8291 | 0.8287 |

Read that gap with one fact next to it: `ProsusAI/finbert` was **fine-tuned on Financial
PhraseBank** — its model card states that "Financial PhraseBank by Malo et al. (2014) is
used for fine-tuning". This model has never seen the corpus. All 4,846 sentences were
checked against this model's training, validation and test data after normalising case
and punctuation; the overlap is zero.

So neither benchmark is neutral ground. The first favours this model, the second favours
`ProsusAI/finbert`. Together they bracket the answer:

| Model | English subset, our set | Financial PhraseBank | Shift |
|---|---:|---:|---:|
| **This model** | 0.8410 | 0.8291 | **−1.2** |
| [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) | 0.7218 | 0.8896 | **+16.8** |

This model gives up a little over a point when moved onto a foreign benchmark. The
English-only model moves by nearly seventeen between the two.

**Polarity holds.** On its own evaluation set this model reverses polarity on 1.0% of
items; on Financial PhraseBank — a corpus a decade older, in a different register, under a
different annotation convention — the rate is **1.1%** (53 of 4,846). The core judgement
of direction does not degrade off home ground.

**94% of the remaining error sits on the boundary with `neutral`**, which is where the two
conventions genuinely disagree rather than where the model fails. Financial PhraseBank
labels a signed contract or a reported sales increase as `positive`; this model treats a
bare corporate fact as `neutral` unless the text carries an evaluative charge. Neither
reading is wrong — they are two conventions, and each model follows the one it was built
for.

**These figures describe behaviour on these two evaluation sets only. They are not a
general claim about either model.**

---

## Usage

```bash
pip install transformers torch
```

### Pipeline

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Kenpache/finbert-multilingual-v2")

clf("Les bénéfices du groupe ont augmenté de 15% au premier trimestre.")
# [{'label': 'positive', 'score': 0.9423}]
```

Batch a whole list in one call:

```python
texts = ["株価は決算発表後に急落した。",
         "La compañía anunció un despido masivo y sus acciones se desplomaron.",
         "Quarterly revenue beat analyst expectations by a wide margin."]

clf(texts, batch_size=32)
# [{'label': 'negative', 'score': 0.9275},
#  {'label': 'negative', 'score': 0.9355},
#  {'label': 'positive', 'score': 0.9391}]
```

Add `top_k=None` to get the full probability distribution over all three classes instead
of the winner only — useful when you want to threshold on confidence rather than take
the argmax.

### Direct loading

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

REPO = "Kenpache/finbert-multilingual-v2"
tokenizer = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForSequenceClassification.from_pretrained(REPO).eval()

text = "Der Umsatz blieb im Vergleich zum Vorjahr unverändert."
enc = tokenizer(text, return_tensors="pt", truncation=True, max_length=192)

with torch.no_grad():
    probs = torch.softmax(model(**enc).logits, dim=-1)[0]

for i, p in enumerate(probs):
    print(f"{model.config.id2label[i]:8} {p:.4f}")

# negative 0.0391
# neutral  0.9087
# positive 0.0522
```

### On GPU

```python
clf = pipeline("text-classification", model=REPO, device=0)          # CUDA
clf = pipeline("text-classification", model=REPO, device="mps")      # Apple Silicon
```

CUDA, Apple Silicon and plain CPU all work — at 307M parameters this is a small model by
current standards, and it runs comfortably on a laptop.

**Use `max_length=192`** to reproduce the numbers above. The backbone supports up to
8,192 tokens, so longer inputs are technically fine, but the reported accuracy is
measured at 192 — enough for headlines and single sentences, which is what this model is
for.

---

## Limitations

1. **Sentence-level, not document-level.** The model is built for headlines and single
   sentences. Feeding a full article gives you one label for the whole thing, which is
   rarely what you want — split it first.
2. **Financial sentiment is not general sentiment.** "Shares fell 3% on the news" is
   negative in a market sense with no emotional language at all. On product reviews or
   social media this model is the wrong tool.
3. **`neutral` is a convention, not a fact.** The boundary between neutral and mildly
   positive/negative is where human annotators disagree most, and the model inherits that
   ambiguity. If a decision hinges on that boundary, use the probabilities and a
   threshold instead of the argmax.
4. **Arabic coverage is thin** in evaluation (73 items). The other six languages are
   measured on 499–1,063 items each.
5. **Seven languages, not 1,811.** The backbone is pretrained on far more, but this
   classifier was tuned for these seven. Other languages will produce output, but it is
   untested.
6. **Not investment advice.** The output is a sentiment label on a text, not a signal to
   trade on.

---

## Intended use

Good fits:

- tagging multilingual financial news feeds in real time
- market-sentiment dashboards and indices across regions
- pre-screening research corpora before human analysis
- backtesting sentiment-based features on multilingual sources

Poor fits: general-purpose sentiment, long documents, languages outside the seven,
anything where the neutral boundary carries legal or financial weight on its own.

---

## Files

| File | What it is |
|---|---|
| `model.safetensors` | weights, fp32, 1.2 GB |
| `config.json` | ModernBERT config with `id2label` (`negative` / `neutral` / `positive`) |
| `tokenizer.json`, `tokenizer_config.json` | tokenizer |

## License

Apache 2.0.

Built on [`jhu-clsp/mmBERT-base`](https://huggingface.co/jhu-clsp/mmBERT-base), which is
MIT-licensed; that attribution is preserved here.

## Citation

```bibtex
@misc{finbert_multilingual_v2,
  title  = {Financial Sentiment, 7 Languages},
  author = {Kenpache},
  year   = {2026},
  url    = {https://huggingface.co/Kenpache/finbert-multilingual-v2}
}
```
