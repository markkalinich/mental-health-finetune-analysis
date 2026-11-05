# AKI Clinical Text Encoder

Continued pretraining of `manhtt-079/vipubmed-deberta-base` on Vietnamese perioperative clinical notes for the AKI prediction task.

## Training details
- Base model: `manhtt-079/vipubmed-deberta-base`
- Masking: span (p=0.18, span_mean=3.0)
- Max length: 512 tokens
- Epochs: 10
- Precision: bf16
- Dev perplexity: 2.81

## Field tags
Trained with 25 clinical-field special tokens (e.g. `[FIELD=LYDOVAOVIEN]`, `[FIELD=BENHCHINH]`, `[FIELD=CONTENT]`).

## Usage
```python
from transformers import AutoModel, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained('banhchungtuongot/aki-clinical-text-encoder', trust_remote_code=True)
model = AutoModel.from_pretrained('banhchungtuongot/aki-clinical-text-encoder', trust_remote_code=True).eval()

enc = tokenizer(['[FIELD=BENHCHINH] phẫu thuật tim'], return_tensors='pt', truncation=True)
with torch.no_grad():
    out = model(**enc)
    mask = enc['attention_mask'].unsqueeze(-1).float()
    embedding = (out.last_hidden_state * mask).sum(1) / mask.sum(1)
```
