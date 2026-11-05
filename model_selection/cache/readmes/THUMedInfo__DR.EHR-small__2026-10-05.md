---
license: apache-2.0
language:
- en
base_model:
- BAAI/bge-base-en-v1.5
---

## Model description

**DR.EHR-small** is a dense retriever / embedding model for EHR retrieval, trained with a two-stage pipeline (knowledge injection + synthetic data). It has **110M parameters** and produces **768-d** embeddings. 
Training uses MIMIC-IV discharge summaries chunked into **100-word chunks with 10-word overlap**, resulting in **5.8M note chunks**. 
For details, see our [paper](https://arxiv.org/abs/2507.18583).

The model is designed for EHR retrieval, and is generalizable to queries including entities and natural language queries.

## Usage


```python
import torch
import numpy as np
from transformers import AutoModel, AutoTokenizer
import torch.nn.functional as F

MODEL_ID = "THUMedInfo/DR.EHR-small"
device = "cuda" if torch.cuda.is_available() else "cpu"
max_length = 512  # note chunks
batch_size = 32

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_ID, trust_remote_code=True).to(device)
model.eval()

@torch.no_grad()
def embed_texts(texts):
    all_emb = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        enc = tokenizer(
            batch,
            padding=True,
            truncation=True,
            max_length=max_length,
            return_tensors="pt",
            return_token_type_ids=False,
        )
        enc = {k: v.to(device) for k, v in enc.items()}
        out = model(**enc)

        # CLS pooling (BERT-style)
        emb = out.last_hidden_state[:, 0, :]  # [B, 768]
        emb = F.normalize(emb, p=2, dim=1)
        all_emb.append(emb.cpu().numpy())
    return np.vstack(all_emb)

# Example
queries = ["hypertension", "metformin"]
q_emb = embed_texts(queries)
print(q_emb.shape)
```


## Citation
```
@article{zhao2025dr,
  title={DR. EHR: Dense Retrieval for Electronic Health Record with Knowledge Injection and Synthetic Data},
  author={Zhao, Zhengyun and Ying, Huaiyuan and Zhong, Yue and Yu, Sheng},
  journal={arXiv preprint arXiv:2507.18583},
  year={2025}
}
```
---

