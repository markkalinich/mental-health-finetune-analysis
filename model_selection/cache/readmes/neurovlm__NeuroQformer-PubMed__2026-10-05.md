---
library_name: neurovlm
tags:
- neuroimaging
- qformer
- brain-to-text
- pubmed
---

# NeuroQformer-PubMed

PubMed-grounded QFormer checkpoint from `docs/02_models/13_qformer_pubmed.ipynb`.

This is the checkpoint before anatomical/canonical fine-tuning. It is packaged
with the image InfoNCE projection head, but canonical projection is disabled.

```python
from neurovlm import NeuroVLM

nvlm = NeuroVLM(device="cuda")
text = nvlm.brain(img).to_text(
    method="generative",
    qformer_variant="pubmed",
    basis=None,
    prefix_text="",
)
```

Repo ID: `neurovlm/NeuroQformer-PubMed`
