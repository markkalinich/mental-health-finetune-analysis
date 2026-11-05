---
license: apache-2.0
tags:
- medical
---
Based ob the paper: "UmlsBERT: Augmenting Contextual Embeddings with a Clinical Metathesaurus" (https://aclanthology.org/2021.naacl-main.139.pdf).

and the github repo: https://github.com/gmichalo/UmlsBERT


Changing base model to SpanBert instead of Bert.

Trained from scratch on MIMIC dataset, using the UMLS dataset to mask words within the text.


We achived better accuracy on MedNLI dataset.

Bert Model accuracy: 83%

SpanBert Model accuracy: 86%