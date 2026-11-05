---
language:
- en
library_name: transformers
tags:
- depression
- roberta
---
# DepRoBERTa 
DepRoBERTa (RoBERTa for Depression Detection) - language model based on RoBERTa-large and further pre-trained on depressive posts from Reddit. 

Model was part of the winning solution for [the Shared Task on Detecting Signs of Depression
from Social Media Text](https://competitions.codalab.org/competitions/36410) at [LT-EDI-ACL2022](https://sites.google.com/view/lt-edi-2022/home).

More information can be found in the following paper: [OPI@LT-EDI-ACL2022: Detecting Signs of Depression from Social Media Text using RoBERTa Pre-trained Language Models](https://aclanthology.org/2022.ltedi-1.40/). 

If you use this model, please cite:

```
@inproceedings{poswiata-perelkiewicz-2022-opi,
    title = "{OPI}@{LT}-{EDI}-{ACL}2022: Detecting Signs of Depression from Social Media Text using {R}o{BERT}a Pre-trained Language Models",
    author = "Po{\'s}wiata, Rafa{\l} and Pere{\l}kiewicz, Micha{\l}",
    booktitle = "Proceedings of the Second Workshop on Language Technology for Equality, Diversity and Inclusion",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.ltedi-1.40",
    doi = "10.18653/v1/2022.ltedi-1.40",
    pages = "276--282",
}
```