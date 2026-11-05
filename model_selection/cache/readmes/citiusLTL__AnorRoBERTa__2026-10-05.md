---
license: cc-by-nc-4.0
language:
- en
base_model:
- FacebookAI/roberta-base
tags:
- anorexia
---

 # AnorRoBERTa

AnorRoBERTa is a domain adaptation of a RoBERTa language model adapted to the anorexia domain. 

We follow the standard procedure for fine-tuning a masked language model in [Huggingface’s NLP Course](https://huggingface.co/learn/nlp-course/chapter7/3?fw=pt) 🤗.

# Usage


### Use a pipeline as a high-level helper
```
from transformers import pipeline

pipe = pipeline("fill-mask", model="citiusLTL/AnorRoBERTa")
```
### Load model directly
```
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("citiusLTL/AnorRoBERTa")
model = AutoModelForMaskedLM.from_pretrained("citiusLTL/AnorRoBERTa")
```


# Paper

For more details, refer to the paper [Adapting language models for mental health analysis on social media](https://www.sciencedirect.com/science/article/pii/S0933365725001526).

```
@article{ARAGON2025103217,
title = {Adapting language models for mental health analysis on social media},
journal = {Artificial Intelligence in Medicine},
pages = {103217},
year = {2025},
issn = {0933-3657},
doi = {https://doi.org/10.1016/j.artmed.2025.103217},
url = {https://www.sciencedirect.com/science/article/pii/S0933365725001526},
author = {Mario Ezra Aragón and Adrián Pastor López-Monroy and Manuel Montes-y-Gómez and David E. Losada},
keywords = {Social media, Mental health, Anorexia, Depression, Gambling, Self-harm, Language models, Adapters},
abstract = {In recent years, there has been a growing research interest focused on identifying traces of mental disorders through social media analysis. These disorders significantly impair millions of individuals’ cognitive and behavioral functions worldwide. Our study aims to advance the understanding of four prevalent mental disorders: Anorexia, Depression, Gambling, and Self-harm. We present a comprehensive framework designed for the domain adaptation of models to analyze and identify signs of these conditions on social media posts. The language models’ adapting strategy consisted of three key stages. First, we gathered and enriched substantial data on the four psychological disorders. Second, we adapted the different models to the language used to discuss mental health concerns on social media. Finally, we employed an adapter to fine-tune the models for multiple classification tasks (specific to each mental health condition). The intuitive idea is to adapt a language model smoothly to each domain. Our work includes a comparative study of different language models under in- and cross-domain conditions. This allows us to, for example, assess the ability of a depression-based language model to detect signs of disorders such as anorexia or self-harm. We show that the resulting mental health models perform well in early risk detection tasks. Additionally, we thoroughly analyze the linguistic qualities of these models by testing their predictive abilities using conventional clinical tools, such as specialized questionnaires. We rigorously examine the models across multiple predictive tasks to provide evidence of the adaptation approach’s robustness and effectiveness. Our evaluation results are promising. They demonstrate that our framework enhances classification performance and competes favorably with state-of-the-art models.}
}