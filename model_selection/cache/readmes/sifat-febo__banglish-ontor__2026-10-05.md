---
language: [bn, en]
license: apache-2.0
pipeline_tag: text-classification
library_name: transformers
tags: [banglish, bengali, bangla, text-classification, emotion, from-scratch,
       perception-layers, code-switching, low-resource-languages, small-models,
       cpu]
---

# ontor

Your model answers a Banglish message — Bengali typed in Latin letters —
without knowing anything about it. ontor is a perception layer: it reads
the message first and hands your model what it found. The whole layer is
3.3 MB and it runs on a CPU in milliseconds.

```
you      thanks bhai, tumi onek help korecho
feeling  positive   ██████░░░░ 0.64
warmth   gratitude  ████████░░ 0.80
wants    casual     ██████████ 0.95
```

This is the same layer that runs inside
[banglish-companion](https://huggingface.co/sifat-febo/banglish-companion),
shipped on its own so you can put it in front of any Banglish project. Use
all three classifiers, or only the one you need.

&nbsp;

## Banglish e

**ki eta?** tinta chhoto model — tomar lekha Banglish theke bujhe ki feeling,
koto ta apon, ar ki dhoroner uttor chai. shob mile 3.3 MB. CPU tei chole.

**ki lagbe?** `pip install transformers torch huggingface_hub`. chalate
internet lagbe na, account lagbe na, taka lagbe na.

**bipod hole?** kichu message er uttor model dey na — `respond()` age oigulo
dekhe ney ar lekha uttor ferot dey. tomar kichu korte hobe na.

&nbsp;

## What each one reads

| | reads | channels | size |
|:--|:--|:--|--:|
| **aabeg** | how the writer feels | `positive` `negative` `social` `curiosity` `threat` | 159K parameters |
| **bhalobasha** | how warm the message is | `affection` `care` `admiration` `gratitude` `playfulness` | 159K parameters |
| **bujhi** | what kind of reply it needs | `refuse` `empathize` `casual` `inform` `codemix` `crisis` | 207K parameters |

Each channel is scored separately. One message can score high on
`curiosity` and high on `negative` at the same time.

All three share one tokenizer, trained on Banglish, with a vocabulary of
4,000 pieces. The tokenizer is the part that matters: an English tokenizer
chops Banglish words into useless fragments, and a Bengali tokenizer cannot
read Latin letters at all.

The safety guard is plain Python, not a model. It matches phrases it knows
and returns an answer a person wrote in advance — no network, and nothing
kept between messages.

&nbsp;

## Use it

```bash
pip install transformers torch huggingface_hub
hf download sifat-febo/banglish-ontor --local-dir banglish-ontor
cd banglish-ontor
python read.py
```

Run that, then type a message. It scores the feeling in it, the warmth in
it, and the kind of reply it needs.

To use ontor in your own code, run Python from that same folder:

```python
from ontor.perceive import perceive, respond, build_system_prompt

text = "thanks bhai, tumi onek help korecho"

answer = respond(text)                      # the guard: fixed text, or None
if answer is None:
    reading = perceive(text)                # a score for every channel
    system = build_system_prompt(reading)   # hand this to your own model
    print(system)
```

To use one classifier on its own:
`from ontor.bhalobasha.scorer import score`.

To drive a model of your own with it, name the model and a message. It runs
the guard, reads the message, and hands your model the system prompt through
that model's own chat template:

```bash
python with_your_model.py <model id or folder> "tomar din kemon gelo"
```

&nbsp;

## Limits

- **Banglish only.** Bengali script and plain English still get scores, and
  those scores mean nothing.
- **Short messages.** One chat turn, up to 128 tokens.
- **No accuracy numbers.** These were judged by reading a chat system's
  answers, never against a labeled test set. Measure them on your own data.
- **The channels are not general.** They were built for one companion model.
  If you need different labels, you would have to retrain.
- **Some messages never reach your model.** `respond()` answers those
  itself, so call it before you call your own model.

&nbsp;

## AI Disclosure

The author designed the layer, chose what it should detect, ran all training
and measurement on the author's own machine, read its output, and chose what
to publish and what to withhold. [Claude Code](https://claude.ai) (Anthropic)
was used as a coding and writing tool under that direction.

&nbsp;

## License

Apache 2.0

Cite the technical report, which describes `ontor` and the models it was
built for: <https://doi.org/10.5281/zenodo.22371896>

```bibtex
@misc{febo2026banglishcompanion,
  author    = {Febo, Sifat},
  title     = {Banglish Companion: Small Chat Models for Romanized Bengali
               — Technical Report},
  year      = {2026},
  month     = sep,
  publisher = {Zenodo},
  version   = {1.0},
  doi       = {10.5281/zenodo.22371896},
  url       = {https://doi.org/10.5281/zenodo.22371896},
  note      = {Repository: sifat-febo/banglish-ontor}
}
```
