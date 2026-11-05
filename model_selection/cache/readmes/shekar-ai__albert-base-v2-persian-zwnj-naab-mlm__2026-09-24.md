---
library_name: transformers
license: mit
language:
- fa
base_model:
- albert/albert-base-v2
datasets:
- SLPL/naab
pipeline_tag: fill-mask
tags:
- persian
- farsi
- albert
- zwnj
---

# ALBERT Persian (Naab, ZWNJ-aware)

A compact Persian ALBERT encoder pretrained with masked language modeling on the
[Naab](https://huggingface.co/datasets/SLPL/naab) corpus. Its SentencePiece vocabulary treats the
zero-width non-joiner (ZWNJ, `U+200C`) as an explicit token, so Persian compounds such as
`می‌روم` and `کتاب‌ها` survive tokenization intact instead of being split on an invisible character.

This is the shared backbone for the task-specific models in the
[Shekar](https://github.com/amirivojdan/shekar) toolkit:
[POS tagging](https://huggingface.co/shekar-ai/albert-base-v2-persian-pos-tagger),
[NER](https://huggingface.co/shekar-ai/albert-base-v2-persian-ner),
[dependency parsing](https://huggingface.co/shekar-ai/albert-base-v2-persian-dep-parser), and
[sentiment analysis](https://huggingface.co/shekar-ai/albert-base-v2-persian-sentiment-snapfood).

| | |
|---|---|
| Architecture | ALBERT base — 12 layers, hidden 768, embedding 128, 12 heads |
| Parameters | 11.5 M |
| Max sequence length | 512 |
| Vocabulary | 32,004 SentencePiece unigram tokens (ZWNJ included) |
| Developed by | Ahmad Amirivojdan |
| License | MIT |

## Intended Use

- Masked-token prediction (`fill-mask`) in Persian text
- Sentence and phrase embeddings for clustering, retrieval, and semantic similarity
- Encoder to fine-tune for Persian classification, tagging, and parsing tasks

## Usage

### Shekar

Shekar exposes the encoder through `ContextualEmbedder`, which runs an ONNX export on CPU and
returns a mask-weighted mean-pooled 768-dimensional sentence vector.

```python
from shekar import ContextualEmbedder

embedder = ContextualEmbedder(model="albert")
vector = embedder("کتاب‌ها دریچه‌ای به جهان دانش هستند.")
print(vector.shape)  # (768,)
```

### Transformers

```python
from transformers import pipeline

fill_mask = pipeline("fill-mask", model="shekar-ai/albert-base-v2-persian-zwnj-naab-mlm")

for prediction in fill_mask("این کتاب بسیار [MASK] است.")[:3]:
    print(prediction["token_str"], round(prediction["score"], 3))
```

```text
مفید 0.204
آموزنده 0.072
عالی 0.044
```

For embeddings, load the encoder directly:

```python
import torch
from transformers import AutoModel, AutoTokenizer

repo = "shekar-ai/albert-base-v2-persian-zwnj-naab-mlm"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModel.from_pretrained(repo).eval()

inputs = tokenizer("کتاب‌ها دریچه‌ای به جهان دانش هستند.", return_tensors="pt")
with torch.no_grad():
    hidden = model(**inputs).last_hidden_state

mask = inputs["attention_mask"].unsqueeze(-1)
embedding = (hidden * mask).sum(1) / mask.sum(1)  # (1, 768)
```

## Training

**Data.** The Naab corpus (~130 GB of cleaned Persian text). Every document was normalized with
Shekar's `Normalizer` before tokenization, then tokenized and concatenated into contiguous blocks of
512 tokens. 2% of the resulting blocks were held out for validation.

**Objective.** Masked language modeling with a 15% masking probability.

| Hyperparameter | Value |
|---|---|
| Epochs | 3 |
| Batch size | 32 per device |
| Learning rate | 2e-5 |
| Warmup steps | 10,000 |
| Weight decay | 0.01 |
| Block size | 512 tokens |

## Evaluation

Masked-token prediction on 3,000 documents from the Naab test split (23,629 masked tokens, 15%
masking, Shekar normalization applied):

| Metric | Value |
|---|---|
| Pseudo-perplexity | 23.8 |
| Top-1 masked-token accuracy | 49.1% |

## Limitations

At 11.5 M parameters this is a small encoder tuned for CPU-friendly deployment, not a
knowledge-rich language model. It predicts frequent grammatical continuations reliably but is weak
at factual cloze completion (`پایتخت ایران [MASK] است.` does not yield `تهران`). Use it as a
representation model and a fine-tuning starting point rather than a knowledge source. Like the
corpus it was trained on, it reflects the biases of Persian web and news text.

## Citation

```bibtex
@article{Amirivojdan2025Shekar,
  author  = {Amirivojdan, Ahmad},
  title   = {{Shekar: A Python Toolkit for Persian Natural Language Processing}},
  journal = {Journal of Open Source Software},
  volume  = {10},
  number  = {114},
  pages   = {9128},
  year    = {2025},
  doi     = {10.21105/joss.09128},
  url     = {https://joss.theoj.org/papers/10.21105/joss.09128}
}
```
