# AKI Clinical Text Encoder

Continued pretraining of `vinai/phobert-base-v2` on Vietnamese perioperative clinical notes for the AKI prediction task.

## Training details
- Base model: `vinai/phobert-base-v2`
- Masking: span (p=0.15, span_mean=3.5)
- Max length: 256 tokens
- Epochs: 3
- Precision: bf16
- Dev perplexity: 1.38

## Field tags
Trained with 25 clinical-field special tokens (e.g. `[FIELD=LYDOVAOVIEN]`, `[FIELD=BENHCHINH]`, `[FIELD=CONTENT]`).

## Usage
```python
from transformers import AutoModel, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained('banhchungtuongot/phobert-aki-clinical-v2', trust_remote_code=True)
model = AutoModel.from_pretrained('banhchungtuongot/phobert-aki-clinical-v2', trust_remote_code=True).eval()

enc = tokenizer(['[FIELD=BENHCHINH] phẫu thuật tim'], return_tensors='pt', truncation=True)
with torch.no_grad():
    out = model(**enc)
    mask = enc['attention_mask'].unsqueeze(-1).float()
    embedding = (out.last_hidden_state * mask).sum(1) / mask.sum(1)
```
