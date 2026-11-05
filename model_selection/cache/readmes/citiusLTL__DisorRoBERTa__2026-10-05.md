---
license: cc-by-4.0
language:
- en
library_name: transformers
tags:
- mental health
- social media
---

# DisorRoBERTa

DisorRoBERTa is a double-domain adaptation of a RoBERTa language model (a variation of [DisorBERT](https://aclanthology.org/2023.acl-long.853/)). First, is adapted to social media language, and then, adapted to the mental health domain. In both steps, it incorporated a lexical resource to guide the masking process of the language model and, therefore, to help it in paying more attention to words related to mental disorders. 

We follow the standard procedure for fine-tuning a masked language model in [Huggingface’s NLP Course](https://huggingface.co/learn/nlp-course/chapter7/3?fw=pt) 🤗.

For training the model, we used a batch size of 256, Adam optimizer, with a learning rate of 1e<sup>-5</sup>, and cross-entropy as a loss function. We trained the model for three epochs using a GPU NVIDIA Tesla V100 32GB SXM2.

# Usage


### Use a pipeline as a high-level helper
```
from transformers import pipeline

pipe = pipeline("fill-mask", model="citiusLTL/DisorRoBERTa")
```
### Load model directly
```
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("citiusLTL/DisorRoBERTa")
model = AutoModelForMaskedLM.from_pretrained("citiusLTL/DisorRoBERTa")
```