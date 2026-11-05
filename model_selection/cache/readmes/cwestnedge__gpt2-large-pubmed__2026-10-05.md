---
library_name: transformers
tags:
- medical
license: mit
language:
- en
metrics:
- perplexity
base_model:
- openai-community/gpt2-large
pipeline_tag: text-generation
---

## Overview
This [pipeline](https://github.com/donkeyanaphora/SHALLOW_FUSION) was used to fine‑tune GPT‑2 [small](https://huggingface.co/openai-community/gpt2), [medium](https://huggingface.co/openai-community/gpt2-medium), and [large](https://huggingface.co/openai-community/gpt2-large) on abstracts from PubMed's [baseline data](https://ftp.ncbi.nlm.nih.gov/pubmed/README.txt). Models were trained on a single A100 GPU in Google Colab.

---
## Training
#### Setup
- Single epoch over **221,709 batches × 16 × 1024 tokens** ≈ **3.63 billion tokens**  
- Identical optimizer, learning‑rate schedule, and hyper‑parameters for all models  
- No additional regularization or early stopping

#### Loss
Here are the the loss curves for GPT‑2 small, medium, and large fine‑tuned on PubMed abstracts over single epoch.

- [Loss comparisons](https://huggingface.co/cwestnedge/gpt2-small-pubmed/blob/main/output.png)

---
## Evaluation

#### Dataset  
Hold‑out set of **1000 × 16 × 1024 tokens** (≈ 16.4 M tokens) randomly sampled from PubMed abstracts, disjoint from the training split.

#### Metrics  
Cross‑entropy loss (averaged over all tokens) and derived perplexity (`ppl = exp(loss)`) on the hold‑out set:

| Model                    | Parameters | Avg CE Loss ↓ | Perplexity ↓ |
|--------------------------|-----------:|-------------:|------------:|
| [gpt2‑small‑pubmed](https://huggingface.co/cwestnedge/gpt2-small-pubmed)       | 124 M      | 2.5017       | 12.20       |
| [gpt2‑medium‑pubmed](https://huggingface.co/cwestnedge/gpt2-medium-pubmed)       | 355 M      | 2.2984       | 9.96        |
| **gpt2‑large‑pubmed**       | 774 M      | 2.1863       | 8.90        |

#### Caveats
- Perplexities are **in‑domain** (PubMed abstracts) and may not reflect general‑purpose LM quality  
- Only one epoch of training; performance likely improves with more epochs or hyper‑parameter tuning  
- Downstream biomedical benchmarks have not yet been conducted
---
## Usage
#### 1) Quick‑start with the 🤗 pipeline API

```python
from transformers import pipeline
import torch 

device = "cuda" if torch.cuda.is_available() else "cpu"

generator = pipeline(
    "text-generation",
    model="cwestnedge/gpt2-large-pubmed",
    tokenizer="openai-community/gpt2-large",
    device=device,
)

prompt = (
    "Background: The CRISPR–Cas9 system has revolutionized gene editing. "
    "In this study, we evaluate its efficacy in"
)
out = generator(
    prompt,
    max_length=200,
    temperature=1e-9,
    top_p=1e-9,
    num_return_sequences=1,
    truncation=True,
)
print(out[0]["generated_text"])
```


#### 2) Manual load + generate for finer control

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "cwestnedge/gpt2-large-pubmed"
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2-large")
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

inputs = tokenizer(
    "Methods: We performed a double‐blind randomized trial to assess",
    return_tensors="pt",
).to(device)

gen_ids = model.generate(
    **inputs,
    max_length=150,
    num_beams=5,
    no_repeat_ngram_size=2,
    early_stopping=True,
)
print(tokenizer.decode(gen_ids[0], skip_special_tokens=True))
```


#### 3) Scoring / perplexity

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda" if torch.cuda.is_available() else "cpu"
model_name = "cwestnedge/gpt2-large-pubmed"
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2-large")
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

text = (
    "Tetralogy of Fallot is a rare congenital heart condition that is present at birth."
)
enc = tokenizer(text, return_tensors="pt").to(device)

with torch.no_grad():
    outputs = model(**enc, labels=enc.input_ids)
    loss = outputs.loss
    ppl = torch.exp(loss)

print(f"CE loss: {loss:.4f} → Perplexity: {ppl:.2f}")
```