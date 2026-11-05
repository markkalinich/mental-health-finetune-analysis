---
license: cc-by-nc-4.0
language:
- en
library_name: transformers
tags:
- mental health
- social media
widget:
 - text: "My life is [MASK]"
 - text: "I [MASK] myself"
---
# DisorBERT

<img style="float: left;" src="https://cdn-uploads.huggingface.co/production/uploads/64b946226b5ee8c388730ec1/y0b5teUiozhDapLaguUGH.png" width="150"/>


[DisorBERT](https://aclanthology.org/2023.acl-long.853/)
is a double-domain adaptation of a BERT language model. First, is adapted to social media language, and then, adapted to the mental health domain. In both steps, it incorporated a lexical resource to guide the masking process of the language model and, therefore, to help it in paying more attention to words related to mental disorders. 

We follow the standard fine-tuning a masked language model of [Huggingface’s NLP Course](https://huggingface.co/learn/nlp-course/chapter7/3?fw=pt) 🤗.

We used the models provided by HuggingFace v4.24.0, and Pytorch v1.13.0. 
In particular, for training the model we used a batch size of 256, Adam optimizer, with a learning rate of 1e<sup>-5</sup>, and cross-entropy as a loss function. We trained the model for three epochs using a GPU NVIDIA Tesla V100 32GB SXM2.

# Usage


### Use a pipeline as a high-level helper
```
from transformers import pipeline

pipe = pipeline("fill-mask", model="citiusLTL/DisorBERT")
```
### Load model directly
```
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("citiusLTL/DisorBERT")
model = AutoModelForMaskedLM.from_pretrained("citiusLTL/DisorBERT")
```

# Paper

For more details, refer to the paper [DisorBERT: A Double Domain Adaptation Model for Detecting Signs of Mental Disorders in Social Media](https://aclanthology.org/2023.acl-long.853/).

```
@inproceedings{aragon-etal-2023-disorbert,
    title = "{D}isor{BERT}: A Double Domain Adaptation Model for Detecting Signs of Mental Disorders in Social Media",
    author = "Aragon, Mario  and
      Lopez Monroy, Adrian Pastor  and
      Gonzalez, Luis  and
      Losada, David E.  and
      Montes, Manuel",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = Jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.853",
    doi = "10.18653/v1/2023.acl-long.853",
    pages = "15305--15318",
}
```