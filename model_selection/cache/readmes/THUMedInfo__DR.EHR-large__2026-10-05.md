---
license: apache-2.0
language:
- en
base_model:
- nvidia/NV-Embed-v2
---

## Model description

**DR.EHR-large** is a dense retriever / embedding model for EHR retrieval, trained with a two-stage pipeline (knowledge injection + synthetic data). It has **7B parameters** and produces **4096-d** embeddings. 
Training uses MIMIC-IV discharge summaries chunked into **100-word chunks with 10-word overlap**, resulting in **5.8M note chunks**. 
For details, see our [paper](https://arxiv.org/abs/2507.18583).

The model is designed for EHR retrieval, and is generalizable to queries including entities and natural language queries.

## Usage


```python
import torch
import numpy as np
from transformers import AutoModel, AutoTokenizer

MODEL_ID = "THUMedInfo/DR.EHR-large"
device = "cuda" if torch.cuda.is_available() else "cpu"
max_length = 512
batch_size = 16

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_ID, trust_remote_code=True).to(device)
model.eval()

INSTRUCTION = (
    "Instruct: Given the medical entity, retrieve relevant paragraphs of patients' medical records\n"
    "Query: "
)

@torch.no_grad()
def embed(texts, is_query: bool = True):
    """
    - is_query=True: add instruction prefix (for entity queries)
    - is_query=False: no prefix (for note chunks/passages)
    """
    instruction = INSTRUCTION if is_query else ""

    all_emb = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        # NV-Embed style API (trust_remote_code): encode(texts, instruction=..., max_length=...)
        emb = model.encode(batch, instruction=instruction, max_length=max_length)  # torch.Tensor [B, 4096]
        all_emb.append(emb.detach().cpu().numpy())
    return np.vstack(all_emb)

# Example
queries = ["hypertension", "metformin"]
passages = ["... note chunk text ...", "... another chunk ..."]

q_emb = embed(queries, is_query=True)
p_emb = embed(passages, is_query=False)
print(q_emb.shape, p_emb.shape)
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