---
datasets:
- dlb/mentalreddit
language:
- en
tags:
- depression
- medical
base_model:
- rafalposwiata/deproberta-large-depression
pipeline_tag: text-classification
---

# MentalBERTa

This model, `MentalBERTa`, was developed by the DeepLearningBrasil team and secured the first position in the [DepSign-LT-EDI@RANLP-2023 shared task](https://arxiv.org/abs/2311.05047).
The objective of the task was to classify social media texts into three distinct levels of depression: "not depressed," "moderately depressed," and "severely depressed".
The accompanying code is available on [GitHub](https://github.com/eduagarcia/depsign-2023-ranlp).

## Model Description

`MentalBERTa` is a `RoBERTa` large model [from rafalposwiata/deproberta-large-depression](https://huggingface.co/rafalposwiata/deproberta-large-depression), pre-trained on a curated Reddit dataset from mental health-related communities. 
This pre-training allows for an enhanced understanding of nuanced mental health discourse

The best performing version of the model was trained with Loss Sample Weights and a 50% head + 50% tail truncation method.

## Training Data

The model was pre-trained on a custom dataset collected from mental health-related Subreddits, which is available on Hugging Face at [dlb/mentalreddit](https://huggingface.co/datasets/dlb/mentalreddit).
The full pre-training dataset comprises 3.4 million comments from mental health-related subreddits and 3.2 million comments from other subreddites, occupying approximately 1.4 GB of text on disk.

### Citation
```bibtex
@inproceedings{garcia-etal-2023-deeplearningbrasil,
    title = "{D}eep{L}earning{B}rasil@{LT}-{EDI}-2023: Exploring Deep Learning Techniques for Detecting Depression in Social Media Text",
    author = "Garcia, Eduardo  and
      Gomes, Juliana  and
      Barbosa Junior, Adalberto  and
      Borges, Cardeque  and
      da Silva, N{\'a}dia",
    booktitle = "Proceedings of the Third Workshop on Language Technology for Equality, Diversity and Inclusion",
    month = sep,
    year = "2023",
    address = "Varna, Bulgaria",
    publisher = "INCOMA Ltd., Shoumen, Bulgaria",
    url = "https://aclanthology.org/2023.ltedi-1.42",
    pages = "272--278",
}
```

## Acknowledgments

This work has been supported by the [AI Center of Excellence (Centro de Excelência em Inteligência Artificial – CEIA)](https://www.linkedin.com/company/inteligencia-artificial-deep-learning-brasil) of the Institute of Informatics at the Federal University of Goiás (INF-UFG).