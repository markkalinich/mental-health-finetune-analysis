---
tags:
- summarization
- bart
- long context
language:
- en
pipeline_tag: fill-mask
---

# LSG model 
**Transformers >= 4.36.1**\
**This model relies on a custom modeling file, you need to add trust_remote_code=True**\
**See [\#13467](https://github.com/huggingface/transformers/pull/13467)**

LSG ArXiv [paper](https://arxiv.org/abs/2210.15497). \
Github/conversion script is available at this [link](https://github.com/ccdv-ai/convert_checkpoint_to_lsg).

* [Usage](#usage)
* [Parameters](#parameters)
* [Sparse selection type](#sparse-selection-type)
* [Tasks](#tasks)

This model is adapted from [BART-base](https://huggingface.co/facebook/bart-base) for encoder-decoder tasks without additional pretraining. It uses the same number of parameters/layers and the same tokenizer.


This model can handle long sequences but faster and more efficiently than Longformer (LED) or BigBird (Pegasus) from the hub and relies on Local + Sparse + Global attention (LSG).

The model requires sequences whose length is a multiple of the block size. The model is "adaptive" and automatically pads the sequences if needed (adaptive=True in config). It is however recommended, thanks to the tokenizer, to truncate the inputs (truncation=True) and optionally to pad with a multiple of the block size (pad_to_multiple_of=...). \

Implemented in PyTorch.

![attn](attn.png)

## Usage
The model relies on a custom modeling file, you need to add trust_remote_code=True to use it.

```python: 
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("ccdv/lsg-bart-base-16384", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("ccdv/lsg-bart-base-16384")
``` 

## Parameters
You can change various parameters like : 
* the number of global tokens (num_global_tokens=1)
* local block size (block_size=128)
* sparse block size (sparse_block_size=128)
* sparsity factor (sparsity_factor=2)
* mask_first_token (mask first token since it is redundant with the first global token)
* see config.json file

Default parameters work well in practice. If you are short on memory, reduce block sizes, increase sparsity factor and remove dropout in the attention score matrix.

```python:
from transformers import AutoModel

model = AutoModel.from_pretrained("ccdv/lsg-bart-base-16384", 
    trust_remote_code=True, 
    num_global_tokens=16,
    block_size=64,
    sparse_block_size=64,
    attention_probs_dropout_prob=0.0
    sparsity_factor=4,
    sparsity_type="none",
    mask_first_token=True
)
``` 

## Sparse selection type

There are 6 different sparse selection patterns. The best type is task dependent. \
If `sparse_block_size=0` or `sparsity_type="none"`, only local attention is considered. \
Note that for sequences with length < 2*block_size, the type has no effect.
* `sparsity_type="bos_pooling"` (new)
    * weighted average pooling using the BOS token 
    * Works best in general, especially with a rather large sparsity_factor (8, 16, 32)
    * Additional parameters:
        * None
* `sparsity_type="norm"`, select highest norm tokens
    * Works best for a small sparsity_factor (2 to 4)
    * Additional parameters:
        * None
* `sparsity_type="pooling"`, use average pooling to merge tokens
    * Works best for a small sparsity_factor (2 to 4)
    * Additional parameters:
        * None
* `sparsity_type="lsh"`, use the LSH algorithm to cluster similar tokens
    * Works best for a large sparsity_factor (4+)
    * LSH relies on random projections, thus inference may differ slightly with different seeds
    * Additional parameters:
        * lsg_num_pre_rounds=1, pre merge tokens n times before computing centroids
* `sparsity_type="stride"`, use a striding mecanism per head
    * Each head will use different tokens strided by sparsify_factor
    * Not recommended if sparsify_factor > num_heads
* `sparsity_type="block_stride"`, use a striding mecanism per head
    * Each head will use block of tokens strided by sparsify_factor
    * Not recommended if sparsify_factor > num_heads

## Tasks
Seq2Seq example for summarization:
```python:
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("ccdv/lsg-bart-base-16384", 
    trust_remote_code=True, 
    pass_global_tokens_to_decoder=True, # Pass encoder global tokens to decoder
)
tokenizer = AutoTokenizer.from_pretrained("ccdv/lsg-bart-base-16384")

SENTENCE = "This is a test sequence to test the model. " * 300
token_ids = tokenizer(
    SENTENCE, 
    return_tensors="pt", 
    padding="max_length", # Optional but recommended
    truncation=True # Optional but recommended
    )
output = model(**token_ids)
```


Classification example:
```python:
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("ccdv/lsg-bart-base-16384", 
    trust_remote_code=True, 
    pass_global_tokens_to_decoder=True, # Pass encoder global tokens to decoder
)
tokenizer = AutoTokenizer.from_pretrained("ccdv/lsg-bart-base-16384")

SENTENCE = "This is a test sequence to test the model. " * 300
token_ids = tokenizer(
    SENTENCE, 
    return_tensors="pt", 
    #pad_to_multiple_of=... # Optional
    truncation=True
    )
output = model(**token_ids)

> SequenceClassifierOutput(loss=None, logits=tensor([[-0.3051, -0.1762]], grad_fn=<AddmmBackward>), hidden_states=None, attentions=None)
```

**BART**
```
@article{DBLP:journals/corr/abs-1910-13461,
  author    = {Mike Lewis and
               Yinhan Liu and
               Naman Goyal and
               Marjan Ghazvininejad and
               Abdelrahman Mohamed and
               Omer Levy and
               Veselin Stoyanov and
               Luke Zettlemoyer},
  title     = {{BART:} Denoising Sequence-to-Sequence Pre-training for Natural Language
               Generation, Translation, and Comprehension},
  journal   = {CoRR},
  volume    = {abs/1910.13461},
  year      = {2019},
  url       = {http://arxiv.org/abs/1910.13461},
  eprinttype = {arXiv},
  eprint    = {1910.13461},
  timestamp = {Thu, 31 Oct 2019 14:02:26 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1910-13461.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```