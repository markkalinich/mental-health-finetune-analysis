---
language: nl
thumbnail: https://github.com/iPieter/RobBERT/raw/master/res/robbert_2023_logo.png
tags:
- Dutch
- Flemish
- RoBERTa
- RobBERT
- BERT
license: mit
datasets:
- oscar
- dbrd
- lassy-ud
- europarl-mono
- conll2002
widget:
- text: Hallo, mijn naam is RobBERT-2023. Het <mask> taalmodel model van UGent en KU Leuven.
---


<p align="center"> 
    <img src="https://github.com/iPieter/RobBERT/raw/master/res/robbert_2023_logo.png" alt="RobBERT-2023: A Dutch RoBERTa-based Language Model" width="75%">
 </p>

# RobBERT-2023: Keeping Dutch Language Models Up-To-Date
RobBERT is the state-of-the-art Dutch BERT-based language model developed by KU Leuven, UGent en TU Berlin.

RobBERT-2023 is the 2023 release of the [Dutch RobBERT model](https://pieter.ai/robbert/).
It is a new version of original [pdelobelle/robbert-v2-dutch-base](https://huggingface.co/pdelobelle/robbert-v2-dutch-base) model on the 2023 version of the OSCAR version.
We release a base model, but this time we also release an additional large model with 355M parameters (x3 over robbert-2022-base). We are particularly proud of the performance of both models, surpassing both the robbert-v2-base and robbert-2022-base models with +2.9 and +0.9 points on the [DUMB benchmark](https://dumbench.nl) from GroNLP. In addition, we also surpass BERTje with +18.6 points with `robbert-2023-dutch-large`.

The original RobBERT model was released in January 2020. Dutch has evolved a lot since then, for example the COVID-19 pandemic introduced a wide range of new words that were suddenly used daily. Also, many other world facts that the original model considered true have also changed. To account for this and other changes in usage, we release a new Dutch BERT model trained on data from 2022: RobBERT 2023.
More in-depth information about RobBERT-2023 can be found in our [blog post](https://pieter.ai/robbert-2023/), [the original RobBERT paper](https://arxiv.org/abs/2001.06286) and [the RobBERT Github repository](https://github.com/iPieter/RobBERT).



## How to use

RobBERT-2023 and RobBERT both use the [RoBERTa](https://arxiv.org/abs/1907.11692) architecture and pre-training but with a Dutch tokenizer and training data. RoBERTa is the robustly optimized English BERT model, making it even more powerful than the original BERT model. Given this same architecture, RobBERT can easily be finetuned and inferenced using [code to finetune RoBERTa](https://huggingface.co/transformers/model_doc/roberta.html) models and most code used for BERT models, e.g. as provided by [HuggingFace Transformers](https://huggingface.co/transformers/) library.

By default, RobBERT-2023 has the masked language model head used in training. This can be used as a zero-shot way to fill masks in sentences. It can be tested out for free on [RobBERT's Hosted infererence API of Huggingface](https://huggingface.co/pdelobelle/robbert-v2-dutch-base?text=De+hoofdstad+van+Belgi%C3%AB+is+%3Cmask%3E.). You can also create a new prediction head for your own task by using any of HuggingFace's [RoBERTa-runners](https://huggingface.co/transformers/v2.7.0/examples.html#language-model-training), [their fine-tuning notebooks](https://huggingface.co/transformers/v4.1.1/notebooks.html) by changing the model name to `pdelobelle/robbert-2023-dutch-large`.


```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("DTAI-KULeuven/robbert-2023-dutch-large")
model = AutoModelForSequenceClassification.from_pretrained("DTAI-KULeuven/robbert-2023-dutch-large")
```

You can then use most of [HuggingFace's BERT-based notebooks](https://huggingface.co/transformers/v4.1.1/notebooks.html) for finetuning RobBERT-2022 on your type of Dutch language dataset.


## Comparison of Available Dutch BERT models

There is a wide variety of Dutch BERT-based models available for fine-tuning on your tasks.
Here's a quick summary to find the one that suits your need:

- **(this model)** [DTAI-KULeuven/robbert-2023-dutch-large](https://huggingface.co/DTAI-KULeuven/robbert-2023-dutch-large): The RobBERT-2023 is the first Dutch large (355M parameters) model. It is trained on OSCAR2023 with a new tokenizer, using [our Tik-to-Tok method](https://arxiv.org/pdf/2310.03477.pdf). 
- [DTAI-KULeuven/robbert-2023-dutch-base](https://huggingface.co/DTAI-KULeuven/robbert-2023-dutch-base): The RobBERT-2023 is a new RobBERT model on the OSCAR2023 dataset with a completely new tokenizer. It is helpful for tasks that rely on words and/or information about more recent events.
- [DTAI-KULeuven/robbert-2022-dutch-base](https://huggingface.co/DTAI-KULeuven/robbert-2022-dutch-base): The RobBERT-2022 is a further pre-trained RobBERT model on the OSCAR2022 dataset. It is helpful for tasks that rely on words and/or information about more recent events.
- [pdelobelle/robbert-v2-dutch-base](https://huggingface.co/pdelobelle/robbert-v2-dutch-base): The RobBERT model has for years been the best performing BERT-like model for most language tasks. It is trained on a large Dutch webcrawled dataset (OSCAR) and uses the superior [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta) architecture, which robustly optimized the original [BERT model](https://huggingface.co/docs/transformers/model_doc/bert).
- [DTAI-KULeuven/robbertje-1-gb-merged](https://huggingface.co/DTAI-KULeuven/robbertje-1-gb-mergedRobBERTje): The RobBERTje model is a distilled version of RobBERT and about half the size and four times faster to perform inference on. This can help deploy more scalable language models for your language task 

There's also the [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) "BERTje" model. This model uses the outdated basic BERT model, and is trained on a smaller corpus of clean Dutch texts.
Thanks to RobBERT's more recent architecture as well as its larger and more real-world-like training corpus, most researchers and practitioners seem to achieve higher performance on their language tasks with the RobBERT model. 


## How to Replicate Our Paper Experiments
Replicating our paper experiments is [described in detail on the RobBERT repository README](https://github.com/iPieter/RobBERT#how-to-replicate-our-paper-experiments). 
The pretraining depends on the model, for RobBERT-2023 this is based on [our Tik-to-Tok method](https://arxiv.org/pdf/2310.03477.pdf).

## Name Origin of RobBERT

Most BERT-like models have the word *BERT* in their name (e.g. [RoBERTa](https://huggingface.co/transformers/model_doc/roberta.html), [ALBERT](https://arxiv.org/abs/1909.11942), [CamemBERT](https://camembert-model.fr/), and [many, many others](https://huggingface.co/models?search=bert)).
As such, we queried our original RobBERT model using its masked language model to name itself *\\<mask\\>bert* using [all](https://huggingface.co/pdelobelle/robbert-v2-dutch-base?text=Mijn+naam+is+%3Cmask%3Ebert.) [kinds](https://huggingface.co/pdelobelle/robbert-v2-dutch-base?text=Hallo%2C+ik+ben+%3Cmask%3Ebert.) [of](https://huggingface.co/pdelobelle/robbert-v2-dutch-base?text=Leuk+je+te+ontmoeten%2C+ik+heet+%3Cmask%3Ebert.) [prompts](https://huggingface.co/pdelobelle/robbert-v2-dutch-base?text=Niemand+weet%2C+niemand+weet%2C+dat+ik+%3Cmask%3Ebert+heet.), and it consistently called itself RobBERT.
We thought it was really quite fitting, given that RobBERT is a [*very* Dutch name](https://en.wikipedia.org/wiki/Robbert) *(and thus clearly a Dutch language model)*, and additionally has a high similarity to its root architecture, namely [RoBERTa](https://huggingface.co/transformers/model_doc/roberta.html).

Since *"rob"* is a Dutch words to denote a seal, we decided to draw a seal and dress it up like [Bert from Sesame Street](https://muppet.fandom.com/wiki/Bert) for the [RobBERT logo](https://github.com/iPieter/RobBERT/blob/master/res/robbert_logo.png).

## Credits and citation

The suite of RobBERT models are created by [Pieter Delobelle](https://people.cs.kuleuven.be/~pieter.delobelle), [Thomas Winters](https://thomaswinters.be), [Bettina Berendt](https://people.cs.kuleuven.be/~bettina.berendt/) and [François Remy](http://fremycompany.com).
If you would like to cite our paper or model, you can use the following BibTeX:

```
@misc{delobelle2023robbert2023conversion,
author = {Delobelle, P and Remy, F},
month = {Sep},
organization = {Antwerp, Belgium},
title = {RobBERT-2023: Keeping Dutch Language Models Up-To-Date at a Lower Cost Thanks to Model Conversion},
year = {2023},
startyear = {2023},
startmonth = {Sep},
startday = {22},
finishyear = {2023},
finishmonth = {Sep},
finishday = {22},
venue = {The 33rd Meeting of Computational Linguistics in The Netherlands (CLIN 33)},
day = {22},
publicationstatus = {published},
url= {https://clin33.uantwerpen.be/abstract/robbert-2023-keeping-dutch-language-models-up-to-date-at-a-lower-cost-thanks-to-model-conversion/}
}

@inproceedings{delobelle2022robbert2022,
  doi = {10.48550/ARXIV.2211.08192},
  url = {https://arxiv.org/abs/2211.08192},
  author = {Delobelle, Pieter and Winters, Thomas and Berendt, Bettina},
  keywords = {Computation and Language (cs.CL), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {RobBERT-2022: Updating a Dutch Language Model to Account for Evolving Language Use},
  venue = {arXiv},
  year = {2022},
}

@inproceedings{delobelle2020robbert,
    title = "{R}ob{BERT}: a {D}utch {R}o{BERT}a-based {L}anguage {M}odel",
    author = "Delobelle, Pieter  and
      Winters, Thomas  and
      Berendt, Bettina",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.findings-emnlp.292",
    doi = "10.18653/v1/2020.findings-emnlp.292",
    pages = "3255--3265"
}
```