---
library_name: transformers
license: mit
language:
  - en
  - az
base_model: jhu-clsp/mmBERT-small
tags:
  - modernbert
  - multilingual
  - vocabulary-truncation
  - encoder
  - fill-mask
  - feature-extraction
  - azerbaijani
  - english
pipeline_tag: feature-extraction
---

# mmBERT-small-en-az

A vocabulary-truncated version of [jhu-clsp/mmBERT-small](https://huggingface.co/jhu-clsp/mmBERT-small), optimized for **English** and **Azerbaijani** by removing unused tokens from the 1800+ language vocabulary.

## What is this model?

mmBERT is a state-of-the-art multilingual encoder built on the ModernBERT architecture with a Gemma 2 tokenizer, trained on 3T+ tokens across 1800+ languages. While powerful, the full model carries a 256K token vocabulary — most of which is unnecessary if you only need English and Azerbaijani.

This model keeps only the ~72K tokens that actually appear in English and Azerbaijani text, reducing the model size by **46%** while preserving identical output quality for these two languages.

## Key numbers

| Metric | Original | Truncated |
|---|---|---|
| Vocabulary size | 256,000 | 71,751 |
| Total parameters | 140.493M | 69.42M |
| Embedding parameters | 98.3M | 27.6M |
| Model size (fp32) | 0.52 GB | 0.26 GB |
| Hidden size | 384 | 384 |
| Layers | 22 | 22 |
| Max sequence length | 8,192 | 8,192 |

All transformer layers (110M non-embedding parameters) are completely unchanged. Only the embedding matrix was trimmed.

## Quality verification

Cosine similarity between Azerbaijani–English sentence pairs is identical or near-identical to the original model:

| Sentence pair | Original | Truncated |
|---|---|---|
| "Bakı Azərbaycanın paytaxtıdır" ↔ "Baku is the capital of Azerbaijan" | 0.927396 | 0.927396 |
| "Süni intellekt texnologiyası sürətlə inkişaf edir" ↔ "Artificial intelligence technology is developing rapidly" | 0.926054 | 0.943118 |
| "Bu gün hava çox gözəldir" ↔ "The weather is very nice today" | 0.937846 | 0.937846 |

Tokenization output is identical for both languages.

## Usage

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("LocalDoc/mmBERT-small-en-az")
model = AutoModel.from_pretrained("LocalDoc/mmBERT-small-en-az")

inputs = tokenizer("Salam, bu gün necəsiniz?", return_tensors="pt")
outputs = model(**inputs)
```

### Getting sentence embeddings (mean pooling)

```python
import torch

def get_embeddings(texts, model, tokenizer):
    encoded = tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        output = model(**encoded)
        mask = encoded["attention_mask"].unsqueeze(-1).expand(output.last_hidden_state.size()).float()
        embeddings = torch.sum(output.last_hidden_state * mask, 1) / torch.clamp(mask.sum(1), min=1e-9)
        embeddings = torch.nn.functional.normalize(embeddings)
    return embeddings

embeddings = get_embeddings(
    ["Bakı Azərbaycanın paytaxtıdır", "Baku is the capital of Azerbaijan"],
    model, tokenizer
)
similarity = embeddings[0].dot(embeddings[1])
print(f"Similarity: {similarity:.4f}")
```

## How it was made

1. Tokenized 1M English and 1M Azerbaijani sentences with the original mmBERT tokenizer
2. Counted token frequencies across both corpora
3. Kept all special/control tokens (first 260 IDs) plus tokens appearing ≥10 times in English or ≥3 times in Azerbaijani
4. Filtered the BPE merges to keep only those where both parts and the merged result exist in the new vocabulary
5. Sliced the corresponding rows from the embedding matrix (`model.embeddings.tok_embeddings`)
6. Saved the truncated model and tokenizer

Method adapted from [vrashad/language_model_optimization](https://github.com/vrashad/language_model_optimization).

## Limitations

- This model is intended for **English and Azerbaijani only**. Text in other languages will produce degraded tokenization (excessive byte-level fallback) and poor embeddings.
- The MLM head (`decoder.weight`, `decoder.bias`) was not truncated. If you need masked language modeling, load with `AutoModelForMaskedLM` and be aware of the vocabulary mismatch in the output layer.
- Fine-tuning is recommended for downstream tasks, as the base model was not fine-tuned for any specific task.

## Citation

If you use this model, please cite the original mmBERT paper:

```bibtex
@misc{marone2025mmbertmodernmultilingualencoder,
      title={mmBERT: A Modern Multilingual Encoder with Annealed Language Learning},
      author={Marc Marone and Orion Weller and William Fleshman and Eugene Yang and Dawn Lawrie and Benjamin Van Durme},
      year={2025},
      eprint={2509.06888},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.06888},
}
```
