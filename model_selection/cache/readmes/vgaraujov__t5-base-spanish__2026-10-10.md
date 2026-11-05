---
license: apache-2.0
datasets:
- large_spanish_corpus
- oscar-corpus/OSCAR-2109
- bertin-project/mc4-es-sampled
language:
- es
tags:
- text-generation-inference
---

# T5S (base-sized model) 

T5S model pre-trained on Spanish language. It was introduced in the paper [Sequence-to-Sequence Spanish Pre-trained Language Models](https://arxiv.org/abs/2309.11259). 

## Model description

T5S is a T5 Version 1.1 model (transformer encoder-decoder) with a bidirectional (BERT-like) encoder and an autoregressive (GPT-like) decoder, which includes the following improvements compared to the original T5 model: 

- GEGLU activation in feed-forward hidden layer, rather than ReLU.

- Dropout was turned off in pre-training (quality win). Dropout should be re-enabled during fine-tuning.

- Pre-trained only on unlabeled corpus without mixing in the downstream tasks.

- no parameter sharing between embedding and classifier layer

T5S is particularly effective when fine-tuned for text generation (e.g. summarization, translation) or comprehension tasks (e.g. text classification, question answering) using text-to-text format.

### How to use

Here is how to use this model in PyTorch:

```python
from transformers import T5Tokenizer, T5Model

tokenizer = T5Tokenizer.from_pretrained("vgaraujov/t5-base-spanish")
model = T5Model.from_pretrained("vgaraujov/t5-base-spanish")

input_ids = tokenizer(
    "Estudios han demostrado que tener un perro es bueno para la salud", return_tensors="pt"
).input_ids  # Batch size 1
decoder_input_ids = tokenizer("Estudios demuestran que", return_tensors="pt").input_ids  # Batch size 1

# forward pass
outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
last_hidden_states = outputs.last_hidden_state
```

### Citation (BibTeX)

```bibtex
@misc{araujo2023sequencetosequence,
      title={Sequence-to-Sequence Spanish Pre-trained Language Models}, 
      author={Vladimir Araujo and Maria Mihaela Trusca and Rodrigo Tufiño and Marie-Francine Moens},
      year={2023},
      eprint={2309.11259},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```