---
language: [bn, en]
license: apache-2.0
pipeline_tag: text-classification
library_name: transformers
base_model: sifat-febo/banglish-encoder
tags: [banglish, bengali, sentiment, bert, code-switching,
       low-resource-languages, cpu]
datasets: [aplycaebous/BnSentMix]
---

# Banglish Sentiment

### Reads the mood of the comment section.

```
eta onek sundor hoyeche vai          -> positive
1 minute por por 3g hoia jay         -> negative
gt 10 pro kokon asbe bangladesh e?   -> neutral
app ta valo but dam beshi            -> mixed
```

Four moods, including the hard one: praise and complaint in the same breath.

&nbsp;

## Banglish e

**ki eta?** Comment porhe bole dey mood ta ki — bhalo, kharap, emni
question, na dui rokom ek shathe. Banglish ei kaj kore, formal Bangla
lage na.

**ki kaj e lagbe?** Review sorting, comment moderation dashboard,
market research — jekhane hajar hajar comment porhar time nai.

&nbsp;

## Use it

```python
import torch
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file
from transformers import AutoModel, AutoTokenizer

repo = "sifat-febo/banglish-sentiment"
tok = AutoTokenizer.from_pretrained(repo)
enc = AutoModel.from_pretrained(repo)
head = load_file(hf_hub_download(repo, "head.safetensors"))

def sentiment(text):
    x = tok(text, return_tensors="pt", truncation=True)
    vec = enc(**x).last_hidden_state.mean(dim=1)
    logits = vec @ head["weight"].T + head["bias"]
    return enc.config.id2label[int(logits.argmax())]
```

The head is a separate small file on purpose: the encoder averages every
word before deciding, which the standard one-line pipeline cannot do —
these twelve lines are the whole integration.

&nbsp;

## How good

0.74 macro-F1 on 1,975 held-out comments, four-way. Always guessing the
commonest answer scores 0.12 on the same ruler. We also read 60 of its
answers by hand: the mistakes sit on genuinely blurry lines — a
complaint-shaped question, a sarcastic compliment — never a cheerful
review called hateful.

&nbsp;

## Built

On [banglish-encoder](https://huggingface.co/sifat-febo/banglish-encoder),
our MuRIL further pretrained on Banglish. That backbone beat stock MuRIL
at this exact task on all five seeded runs — this model is the winning
arm. Trained on [BnSentMix](https://huggingface.co/datasets/aplycaebous/BnSentMix),
~20k human-labeled code-mixed comments.

&nbsp;

## Limits

Short, informal text — a comment, not an essay (about fifty words, then
it truncates). Four fixed moods; it does not detect topics, sarcasm as a
category, or hate speech. "mixed" is the hardest class and its weakest.

&nbsp;

## AI Disclosure

The author designed the system, chose the base models, ran all training and
measurement on the author's own machine, read the models' output, and chose
what to publish and what to withhold. [Claude Code](https://claude.ai)
(Anthropic) was used as a coding and writing tool under that direction.

&nbsp;

## License

Apache 2.0. Data from
[BnSentMix](https://huggingface.co/datasets/aplycaebous/BnSentMix) (MIT);
base model lineage: [MuRIL](https://huggingface.co/google/muril-base-cased)
(Google, Apache 2.0).

```bibtex
@misc{banglishsentiment2026,
  author = {Sifat Febo},
  title = {Banglish Sentiment: reads the mood of the comment section},
  year = {2026},
  url = {https://huggingface.co/sifat-febo/banglish-sentiment}
}
```
