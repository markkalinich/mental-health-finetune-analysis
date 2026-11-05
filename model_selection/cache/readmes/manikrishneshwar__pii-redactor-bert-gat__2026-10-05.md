---
language:
- en
license: mit
library_name: transformers
tags:
- pii
- privacy
- redaction
- token-classification
- ner
- bert
- gat
- graph-attention-network
pipeline_tag: token-classification
---

# PII Redactor — BERT + Graph Attention Network

Token-level PII detection model that combines a BERT contextual encoder
with a Graph Attention Network (GAT) refinement stage. The graph mixes
sequential-window edges with top-k attention edges drawn from BERT's last
layer, letting the GAT exploit both locality and the long-range
dependencies BERT already discovered.

The model emits BIO tags over 15 PII categories: `SSN`, `BANK_ACCOUNT`,
`ROUTING_NUMBER`, `CREDIT_CARD`, `CVV`, `CARD_EXPIRY`, `IBAN`, `DOB`,
`FULL_NAME`, `EMAIL`, `PHONE`, `ADDRESS`, `PASSPORT`, `DRIVERS_LICENSE`,
`TAX_ID`.

## Quick start

```python
from transformers import AutoModel, AutoTokenizer

REPO = "manikrishneshwar/pii-redactor-bert-gat"   

tokenizer = AutoTokenizer.from_pretrained(REPO, trust_remote_code=True)
model     = AutoModel.from_pretrained(REPO, trust_remote_code=True)
model.eval()

result = model.predict(
    "Email me at john.doe@example.com or call 555-123-4567.",
    tokenizer,
)
print(result["redacted"])
# -> "Email me at [EMAIL] or call [PHONE]."
print(result["spans"])
# -> [{'start': 12, 'end': 32, 'label': 'EMAIL', 'value': 'john.doe@example.com'}, ...]
```

`trust_remote_code=True` is required because the architecture (BERT + GAT)
is custom and ships as `modeling_bert_gat.py` in this repository.

## Architecture

```
input_ids ──► BERT encoder (with output_attentions=True)
                    │
                    ▼
            token embeddings + last-layer attention
                    │
                    ▼
            build_token_graph(window=3, top_k=5)
                    │
                    ▼
            stack of GATConv layers (heads=4, hidden=128)
                    │
                    ▼
            residual + LayerNorm  ──►  classifier ──►  BIO logits
```

## Inputs / outputs

* **Input:** raw text string.
* **Output:** dict with `original`, `redacted`, and `spans` (list of
  `{start, end, label, value}`).


## Requirements

```text
torch>=2.0
transformers>=4.30
torch-geometric>=2.3
```

## License

MIT.
