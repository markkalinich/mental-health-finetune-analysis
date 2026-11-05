---
widget:
- text: "gelirken bir litre [MASK] aldım."
  example_title: "Örnek 1"
pipeline_tag: fill-mask
tags:
- Turkish
- turkish
language:
- tr
---

# turkish-medium-bert-uncased

This is a Turkish Medium uncased BERT model, developed to fill the gap for small-sized BERT models for Turkish. Since this model is uncased: it does not make a difference between turkish and Turkish. 

#### ⚠ Uncased use requires manual lowercase conversion

 
**Don't** use the `do_lower_case = True` flag with the tokenizer. Instead, convert your text to lower case as follows: 
```python
text.replace("I", "ı").lower()
```
This is due to a [known issue](https://github.com/huggingface/transformers/issues/6680) with the tokenizer.

Be aware that this model may exhibit biased predictions as it was trained primarily on crawled data, which inherently can contain various biases.

Other relevant information can be found in the [paper](https://arxiv.org/abs/2307.14134). 


## Example Usage
```python
from transformers import AutoTokenizer, BertForMaskedLM
from transformers import pipeline

model = BertForMaskedLM.from_pretrained("ytu-ce-cosmos/turkish-medium-bert-uncased")
# or
# model = BertForMaskedLM.from_pretrained("ytu-ce-cosmos/turkish-medium-bert-uncased", from_tf = True)

tokenizer = AutoTokenizer.from_pretrained("ytu-ce-cosmos/turkish-medium-bert-uncased")

unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)
unmasker("gelirken bir litre [MASK] aldım.")
[{'score': 0.6158884763717651,
  'token': 11818,
  'token_str': 'benzin',
  'sequence': 'gelirken bir litre benzin aldım.'},
 {'score': 0.1580735594034195,
  'token': 2417,
  'token_str': 'su',
  'sequence': 'gelirken bir litre su aldım.'},
 {'score': 0.07746931910514832,
  'token': 29480,
  'token_str': 'mazot',
  'sequence': 'gelirken bir litre mazot aldım.'},
 {'score': 0.0339476652443409,
  'token': 4521,
  'token_str': 'süt',
  'sequence': 'gelirken bir litre süt aldım.'},
 {'score': 0.021608062088489532,
  'token': 7279,
  'token_str': 'alkol',
  'sequence': 'gelirken bir litre alkol aldım.'}]
```


# Acknowledgments
- Research supported with Cloud TPUs from [Google's TensorFlow Research Cloud](https://sites.research.google/trc/about/) (TFRC). Thanks for providing access to the TFRC ❤️
- Thanks to the generous support from the Hugging Face team, it is possible to download models from their S3 storage 🤗

# Citations
```bibtex
@article{kesgin2023developing,
  title={Developing and Evaluating Tiny to Medium-Sized Turkish BERT Models},
  author={Kesgin, Himmet Toprak and Yuce, Muzaffer Kaan and Amasyali, Mehmet Fatih},
  journal={arXiv preprint arXiv:2307.14134},
  year={2023}
}
```

# License

MIT
