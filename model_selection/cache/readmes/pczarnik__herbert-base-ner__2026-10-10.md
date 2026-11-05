---
license: cc-by-4.0
datasets:
- wikiann
language:
- pl
pipeline_tag: token-classification
widget:
- text: "Nazywam się Grzegorz Brzęszczyszczykiewicz, pochodzę z Chrząszczyżewoszczyc, pracuję w Łękołodzkim Urzędzie Powiatowym"
- text: "Jestem Krzysiek i pracuję w Ministerstwie Sportu"
- text: "Na imię jej Wiktoria, pracuje w Krakowie na AGH"
model-index:
- name: herbert-base-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      config: pl
      split: test
      args: pl
    metrics:
    - name: Precision
      type: precision
      value: 0.8857142857142857
    - name: Recall
      type: recall
      value: 0.9070532179048386
    - name: F1
      type: f1
      value: 0.896256755412619
    - name: Accuracy
      type: accuracy
      value: 0.9581463871961428
---


# herbert-base-ner

## Model description

**herbert-base-ner** is a fine-tuned HerBERT model that can be used for **Named Entity Recognition** .
It has been trained to recognize three types of entities: person (PER), location (LOC) and organization (ORG).

Specifically, this model is an [*allegro/herbert-base-cased*](https://huggingface.co/allegro/herbert-base-cased) model that was fine-tuned on the Polish subset of *wikiann* dataset.

### How to use

You can use this model with Transformers *pipeline* for NER.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

model_checkpoint = "pczarnik/herbert-base-ner"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint)

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Nazywam się Grzegorz Brzęszczyszczykiewicz, pochodzę "\
    "z Chrząszczyżewoszczyc, pracuję w Łękołodzkim Urzędzie Powiatowym"

ner_results = nlp(example)
print(ner_results)
```
```python
[{'entity': 'B-PER', 'score': 0.99451494, 'index': 4, 'word': 'Grzegorz</w>', 'start': 12, 'end': 20},
 {'entity': 'I-PER', 'score': 0.99758506, 'index': 5, 'word': 'B', 'start': 21, 'end': 22},
 {'entity': 'I-PER', 'score': 0.99749386, 'index': 6, 'word': 'rzę', 'start': 22, 'end': 25},
 {'entity': 'I-PER', 'score': 0.9973041, 'index': 7, 'word': 'szczy', 'start': 25, 'end': 30},
 {'entity': 'I-PER', 'score': 0.99682057, 'index': 8, 'word': 'szczy', 'start': 30, 'end': 35},
 {'entity': 'I-PER', 'score': 0.9964832, 'index': 9, 'word': 'kiewicz</w>', 'start': 35, 'end': 42},
 {'entity': 'B-LOC', 'score': 0.99427444, 'index': 14, 'word': 'Chrzą', 'start': 55, 'end': 60},
 {'entity': 'I-LOC', 'score': 0.99143463, 'index': 15, 'word': 'szczy', 'start': 60, 'end': 65},
 {'entity': 'I-LOC', 'score': 0.9922201, 'index': 16, 'word': 'że', 'start': 65, 'end': 67},
 {'entity': 'I-LOC', 'score': 0.9918464, 'index': 17, 'word': 'wo', 'start': 67, 'end': 69},
 {'entity': 'I-LOC', 'score': 0.9900766, 'index': 18, 'word': 'szczy', 'start': 69, 'end': 74},
 {'entity': 'I-LOC', 'score': 0.98823845, 'index': 19, 'word': 'c</w>', 'start': 74, 'end': 75},
 {'entity': 'B-ORG', 'score': 0.6808262, 'index': 23, 'word': 'Łę', 'start': 87, 'end': 89},
 {'entity': 'I-ORG', 'score': 0.7763973, 'index': 24, 'word': 'ko', 'start': 89, 'end': 91},
 {'entity': 'I-ORG', 'score': 0.77731717, 'index': 25, 'word': 'ło', 'start': 91, 'end': 93},
 {'entity': 'I-ORG', 'score': 0.9108255, 'index': 26, 'word': 'dzkim</w>', 'start': 93, 'end': 98},
 {'entity': 'I-ORG', 'score': 0.98050755, 'index': 27, 'word': 'Urzędzie</w>', 'start': 99, 'end': 107},
 {'entity': 'I-ORG', 'score': 0.9789752, 'index': 28, 'word': 'Powiatowym</w>', 'start': 108, 'end': 118}]
```



### BibTeX entry and citation info

```
@inproceedings{mroczkowski-etal-2021-herbert,
    title = "{H}er{BERT}: Efficiently Pretrained Transformer-based Language Model for {P}olish",
    author = "Mroczkowski, Robert  and
      Rybak, Piotr  and
      Wr{\\'o}blewska, Alina  and
      Gawlik, Ireneusz",
    booktitle = "Proceedings of the 8th Workshop on Balto-Slavic Natural Language Processing",
    month = apr,
    year = "2021",
    address = "Kiyv, Ukraine",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.bsnlp-1.1",
    pages = "1--10",
}
```
```
@inproceedings{pan-etal-2017-cross,
    title = "Cross-lingual Name Tagging and Linking for 282 Languages",
    author = "Pan, Xiaoman  and
      Zhang, Boliang  and
      May, Jonathan  and
      Nothman, Joel  and
      Knight, Kevin  and
      Ji, Heng",
    booktitle = "Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2017",
    address = "Vancouver, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P17-1178",
    doi = "10.18653/v1/P17-1178",
    pages = "1946--1958",
}
```
