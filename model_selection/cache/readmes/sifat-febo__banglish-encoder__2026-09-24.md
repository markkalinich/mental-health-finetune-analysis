---
language: [bn, en]
license: apache-2.0
pipeline_tag: feature-extraction
library_name: transformers
base_model: google/muril-base-cased
tags: [banglish, bengali, bert, encoder, code-switching,
       low-resource-languages, cpu]
---

# Banglish Encoder

### Reads the script people actually type.

```
ami kalke exam dibo, tension e achi
আমি কালকে exam দিবো, tension এ আছি
```

One reader for both. And everything in between.

&nbsp;

## Banglish e

**ki eta?** Google er MuRIL — kintu amader moto kore abar porano. Boi er
Bangla na, forum er Banglish: "plz vai", "koto tk", emoji shoho.

**ki kaj e lagbe?** Er upor classifier banao, search banao, ja iccha.
Standard BERT, standard tool ei chole.

&nbsp;

## Use it

```python
from transformers import AutoModel, AutoTokenizer

tok = AutoTokenizer.from_pretrained("sifat-febo/banglish-encoder")
model = AutoModel.from_pretrained("sifat-febo/banglish-encoder")
enc = tok("bhai net slow ken?", return_tensors="pt")
h = model(**enc).last_hidden_state    # one 768-wide vector per token
```

A stock BERT. Anything that fine-tunes BERT fine-tunes this.

&nbsp;

## Why

Every Bengali encoder is trained on Bengali script. But half the Bengali
internet types in Latin letters, mixes in English, and never spells a word
the same way twice. MuRIL comes closest to reading it — so we kept teaching
it, on exactly that text.

&nbsp;

## How good

Guessing a hidden word in held-out Banglish: MuRIL gets 20.2%. This model
gets 43.0%. Same test, same words hidden.

And the test that matters — build something on top of it. Our embedding
model, trained once on stock MuRIL and once on this, same recipe, same data:
the misses drop from 48 to 26. That model is
[banglish-embed](https://huggingface.co/sifat-febo/banglish-embed), and this
is the backbone inside it.

Sentiment says the same. Fine-tune this and stock MuRIL on the same public
sentiment data, five seeds each: this one wins all five runs, by 2.2 points
of macro-F1 on average.

&nbsp;

## Limits

Trained on short, informal lines — a sentence or two, not documents. It
ships as a body without the masked-word head: a starting point for
fine-tuning, not a finished product. MuRIL's 197k vocabulary is unchanged,
so it stays a 0.95 GB download.

&nbsp;

## AI Disclosure

The author designed the system, chose the base models, ran all training and
measurement on the author's own machine, read the models' output, and chose
what to publish and what to withhold. [Claude Code](https://claude.ai)
(Anthropic) was used as a coding and writing tool under that direction.

&nbsp;

## License

Apache 2.0. Base model
[MuRIL](https://huggingface.co/google/muril-base-cased) (Google, Apache 2.0).

```bibtex
@misc{banglishencoder2026,
  author = {Sifat Febo},
  title = {Banglish Encoder: reads the script people actually type},
  year = {2026},
  url = {https://huggingface.co/sifat-febo/banglish-encoder}
}
```
