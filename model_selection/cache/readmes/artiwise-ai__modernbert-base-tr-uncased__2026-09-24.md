
---
library_name: transformers
license: mit
datasets:
- uonlp/CulturaX
language:
- tr
base_model:
- answerdotai/ModernBERT-base
pipeline_tag: fill-mask
---

# Artiwise ModernBERT - Base Turkish Uncased

[![trmodernbert.webp](https://i.ibb.co/hxgXFnZM/trmodernbert.webp)](https://i.ibb.co/hxgXFnZM/trmodernbert.webp)

We present Artiwise ModernBERT for Turkish 🎉. A BERT model with modernized architecture and increased context size. (Older BERT models 512 --> ModernBERT 8192).

This model is a Turkish adaptation of ModernBERT, fine-tuned from `answerdotai/ModernBERT-base` using only the Turkish part of CulturaX.

# Stats

- **Training Data:** CulturaX 192GB (tr) 
- **Base Model:** `answerdotai/ModernBERT-base`

# Benchmark
The benchmark results below demonstrate that Artiwise ModernBERT consistently outperforms existing Turkish BERT variants across multiple domains and masking levels, highlighting its superior generalization capabilities.

| Dataset & Mask Level                  | Artiwise Modern Bert | ytu-ce-cosmos/turkish-base-bert-uncased | dbmdz/bert-base-turkish-uncased |
|--------------------------------------|----------------------|----------------------------------------|----------------------------------|
| QA Dataset (5% mask)                 | **74.50**            | 60.84                                  | 48.57                           |
| QA Dataset (10% mask)                | **72.18**            | 58.75                                  | 46.29                           |
| QA Dataset (15% mask)                | **69.46**            | 56.50                                  | 44.30                           |
| Review Dataset (5% mask)             | **62.67**            | 48.57                                  | 35.38                           |
| Review Dataset (10% mask)            | **59.60**            | 45.77                                  | 33.04                           |
| Review Dataset (15% mask)            | **56.51**            | 43.05                                  | 31.05                           |
| Biomedical Dataset (5% mask)        | **58.11**            | 50.78                                  | 40.82                           |
| Biomedical Dataset (10% mask)       | **55.55**            | 48.37                                  | 38.51                           |
| Biomedical Dataset (15% mask)       | **52.71**            | 45.82                                  | 36.44                           |

For each dataset (QA, Reviews, Biomedical) and each masking level (5 %, 10 %, 15 %), we randomly masked the specified percentage of tokens in every input example and then measured each model’s ability to correctly predict those masked tokens. All models were in bfloat16 precision.

Our experiments used three datasets: the [Turkish Biomedical Corpus](https://huggingface.co/datasets/hazal/Turkish-Biomedical-corpus-trM), the [Turkish Product Reviews dataset](https://huggingface.co/datasets/fthbrmnby/turkish_product_reviews), and the general‑domain QA corpus [turkish\_v2](https://huggingface.co/datasets/blackerx/turkish_v2).

# Model Usage
Note: Torch version must be >= 2.6.0 and transformers version>=4.50.0 for the model to function properly.
Also **Don't** use the `do_lower_case = True` flag with the tokenizer. Instead, convert your text to lower case as follows: 
```python
text.replace("I", "ı").lower()
```
This is due to a [known issue](https://github.com/huggingface/transformers/issues/6680) with the tokenizer.

Load the model with 🤗 Transformers:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("artiwise-ai/modernbert-base-tr-uncased")
model = AutoModelForMaskedLM.from_pretrained("artiwise-ai/modernbert-base-tr-uncased")

# Example sentence with masked token
text = "Türkiye'nin başkenti [MASK]'dır."
text.replace("I", "ı").lower()

# Tokenize and prepare input
inputs = tokenizer(text, return_tensors="pt")

# Get the position of the masked token
mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]

# Forward pass
with torch.no_grad():
    outputs = model(**inputs)

# Get the predictions for the masked token
logits = outputs.logits
mask_token_logits = logits[0, mask_token_index, :]
top_5_tokens = torch.topk(mask_token_logits, 5, dim=1).indices[0].tolist()

# Print the predictions
print(f"Original text: {text}")
print("Top 5 predictions for [MASK]:")
for token in top_5_tokens:
    print(f"- {tokenizer.decode([token])}")

