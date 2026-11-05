---
language: en
license: apache-2.0
datasets:
- scientific_papers
tags:
- summarization
model-index:
- name: google/bigbird-pegasus-large-pubmed
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: scientific_papers
      type: scientific_papers
      config: pubmed
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 40.8966
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 18.1161
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 26.1743
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 34.2773
      verified: true
    - name: loss
      type: loss
      value: 2.1707184314727783
      verified: true
    - name: meteor
      type: meteor
      value: 0.3513
      verified: true
    - name: gen_len
      type: gen_len
      value: 221.2531
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: scientific_papers
      type: scientific_papers
      config: arxiv
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 40.3815
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 14.374
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 23.4773
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 33.772
      verified: true
    - name: loss
      type: loss
      value: 3.235051393508911
      verified: true
    - name: gen_len
      type: gen_len
      value: 186.2003
      verified: true
---

# BigBirdPegasus model (large)

BigBird, is a sparse-attention based transformer which extends Transformer based models, such as BERT to much longer sequences. Moreover, BigBird comes along with a theoretical understanding of the capabilities of a complete transformer that the sparse model can handle. 

BigBird was introduced in this [paper](https://arxiv.org/abs/2007.14062) and first released in this [repository](https://github.com/google-research/bigbird).

Disclaimer: The team releasing BigBird did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

BigBird relies on **block sparse attention** instead of normal attention (i.e. BERT's attention) and can handle sequences up to a length of 4096 at a much lower compute cost compared to BERT. It has achieved SOTA on various tasks involving very long sequences such as long documents summarization, question-answering with long contexts.

## How to use

Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import BigBirdPegasusForConditionalGeneration, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("google/bigbird-pegasus-large-pubmed")

# by default encoder-attention is `block_sparse` with num_random_blocks=3, block_size=64
model = BigBirdPegasusForConditionalGeneration.from_pretrained("google/bigbird-pegasus-large-pubmed")

# decoder attention type can't be changed & will be "original_full"
# you can change `attention_type` (encoder only) to full attention like this:
model = BigBirdPegasusForConditionalGeneration.from_pretrained("google/bigbird-pegasus-large-pubmed", attention_type="original_full")

# you can change `block_size` & `num_random_blocks` like this:
model = BigBirdPegasusForConditionalGeneration.from_pretrained("google/bigbird-pegasus-large-pubmed", block_size=16, num_random_blocks=2)

text = "Replace me by any text you'd like."
inputs = tokenizer(text, return_tensors='pt')
prediction = model.generate(**inputs)
prediction = tokenizer.batch_decode(prediction)
```

## Training Procedure

This checkpoint is obtained after fine-tuning `BigBirdPegasusForConditionalGeneration` for **summarization** on **pubmed dataset** from [scientific_papers](https://huggingface.co/datasets/scientific_papers).

## BibTeX entry and citation info

```tex
@misc{zaheer2021big,
      title={Big Bird: Transformers for Longer Sequences}, 
      author={Manzil Zaheer and Guru Guruganesh and Avinava Dubey and Joshua Ainslie and Chris Alberti and Santiago Ontanon and Philip Pham and Anirudh Ravula and Qifan Wang and Li Yang and Amr Ahmed},
      year={2021},
      eprint={2007.14062},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
