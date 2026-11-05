---
language:
- sl

license: cc-by-sa-4.0
---

# t5-sl-small
t5-sl-small model is a Slovene T5 model. It has 8 encoder and 8 decoder layers, in total about 60 million parameters.
It was trained for 5 epochs on the following corpora:

## Corpora
The following corpora were used for training the model:
* Gigafida 2.0
* Kas 1.0
* Janes 1.0 (only Janes-news, Janes-forum, Janes-blog, Janes-wiki subcorpora)
* Slovenian parliamentary corpus siParl 2.0
* slWaC

## Evaluation
The model is described in detail and evaluated in our paper ["*Sequence to sequence pretraining for a less-resourced Slovenian language*"](https://arxiv.org/abs/2207.13988)

## Changelog
2022-07-21: updated with v2 of the model, the old one is still accesible at [cjvt/legacy-t5-sl-small](https://huggingface.co/cjvt/legacy-t5-sl-small).
2022-09-21: added fast tokenizer (Huggingface's TokenizerFast class, the tokenization remains the same)