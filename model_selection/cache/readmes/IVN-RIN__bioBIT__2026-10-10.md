---
language:
- it
tags:
- Biomedical Language Modeling
widget:
- text: >-
    L'asma allergica è una patologia dell'[MASK] respiratorio causata dalla
    presenza di allergeni responsabili dell'infiammazione dell'albero
    bronchiale.
  example_title: Example 1
- text: >-
    Il pancreas produce diversi [MASK] molto importanti tra i quali l'insulina e
    il glucagone.
  example_title: Example 2
- text: >-
    Il GABA è un amminoacido ed è il principale neurotrasmettitore inibitorio
    del [MASK].
  example_title: Example 3
datasets:
- IVN-RIN/BioBERT_Italian
---

🤗 + 📚🩺🇮🇹  =  **BioBIT**

From this repository you can download the **BioBIT** (Biomedical Bert for ITalian) checkpoint. 

**BioBIT** stems from [Italian XXL BERT](https://huggingface.co/dbmdz/bert-base-italian-xxl-cased), obtained from a recent Wikipedia dump and various texts in Italian from the OPUS and OSCAR corpora collection, which sums up to the final corpus size of 81 GB and 13B tokens.

To pretrain **BioBIT**, we followed the general approach outlined in [BioBERT paper](https://arxiv.org/abs/1901.08746), built on the foundation of the BERT architecture. The pretraining objective is a combination of **MLM** (Masked Language Modelling) and **NSP** (Next Sentence Prediction). The MLM objective is based on randomly masking 15% of the input sequence, trying then to predict the missing tokens; for the NSP objective, instead, the model is given a couple of sentences and has to guess if the second comes after the first in the original document.

Due to the unavailability of an Italian equivalent for the millions of abstracts and full-text scientific papers used by English, BERT-based biomedical models, in this work we leveraged machine translation to obtain an Italian biomedical corpus based on PubMed abstracts and train **BioBIT**. More details in the paper.

**BioBIT** has been evaluated on 3 downstream tasks: **NER** (Named Entity Recognition), extractive **QA** (Question Answering), **RE** (Relation Extraction).
Here are the results, summarized:
- NER:
  - [BC2GM](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb32) = 82.14%
  - [BC4CHEMD](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb35) = 80.70%
  - [BC5CDR(CDR)](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb31) = 82.15%
  - [BC5CDR(DNER)](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb31) = 76.27%
  - [NCBI_DISEASE](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb33) = 65.06%
  - [SPECIES-800](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb34) = 61.86%
- QA:
  - [BioASQ 4b](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb30) = 68.49%
  - [BioASQ 5b](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb30) = 78.33%
  - [BioASQ 6b](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb30) = 75.73%
- RE:
  - [CHEMPROT](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb36) = 38.16%
  - [BioRED](http://refhub.elsevier.com/S1532-0464(23)00152-1/sb37) = 67.15%

[Check the full paper](https://www.sciencedirect.com/science/article/pii/S1532046423001521) for further details, and feel free to contact us if you have some inquiry!