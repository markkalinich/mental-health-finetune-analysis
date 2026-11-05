---
license: mit
language:
- en
tags:
- token-classification
- ner
- pii-detection
- crf
- distilbert
---

# PII NER (DistilBERT + CRF)

A token-classification model that detects **names** and **addresses** in free text, for PII redaction/masking use cases. Built on `distilbert-base-multilingual-cased` with a CRF layer on top for more consistent entity boundaries.

## Labels

| Label | Meaning |
|---|---|
| `O` | Not PII |
| `B-NAME` / `I-NAME` | Start / continuation of a person's name |
| `B-ADDRESS` / `I-ADDRESS` | Start / continuation of an address |

## Training data

Trained on a combination of:
- [`ai4privacy/pii-masking-200k`](https://huggingface.co/datasets/ai4privacy/pii-masking-200k)
- [`somukandula/maskara-indian-pii-200k`](https://huggingface.co/datasets/somukandula/maskara-indian-pii-200k)

with a 30% lowercase-augmented duplicate of each to make the model robust to casing.

## Evaluation

Entity-level precision / recall / F1 on a held-out 10% split (see `eval_report.txt` in this repo for the full numbers):

| Entity | Precision | Recall | F1 |
|---|---|---|---|
| NAME | _fill in from eval_report.txt_ | | |
| ADDRESS | _fill in from eval_report.txt_ | | |
| **micro avg** | | | |

## How to use

This model uses a custom architecture (DistilBERT encoder + CRF decoding layer), so it can't be loaded with a plain `AutoModelForTokenClassification`. Use the snippet below instead.

```bash
pip install torch transformers pytorch-crf huggingface_hub
```

```python
import torch
import torch.nn as nn
from huggingface_hub import snapshot_download
from torchcrf import CRF
from transformers import AutoConfig, AutoModel, AutoTokenizer
import json

REPO_ID = "your-username/pii-ner-distilbert-crf"  # <-- change this
local_dir = snapshot_download(REPO_ID)

class DistilBertCRF(nn.Module):
    def __init__(self, config, num_labels):
        super().__init__()
        self.bert = AutoModel.from_config(config)
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_labels)
        self.crf = CRF(num_labels, batch_first=True)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        emissions = self.classifier(self.dropout(outputs.last_hidden_state))
        return self.crf.decode(emissions, mask=attention_mask.bool())

with open(f"{local_dir}/label_map.json") as f:
    id2label = {int(k): v for k, v in json.load(f)["id2label"].items()}

config = AutoConfig.from_pretrained(local_dir)
tokenizer = AutoTokenizer.from_pretrained(local_dir)
model = DistilBertCRF(config, num_labels=len(id2label))
model.load_state_dict(torch.load(f"{local_dir}/pytorch_model.bin", map_location="cpu"))
model.eval()

def predict(text):
    enc = tokenizer(text, return_tensors="pt", return_offsets_mapping=True, truncation=True, max_length=512)
    offsets = enc.pop("offset_mapping")[0].tolist()
    with torch.no_grad():
        pred_ids = model(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])[0]
    return [(text[s:e], id2label[label_id]) for (s, e), label_id in zip(offsets, pred_ids) if s != e]

text = "Hi, my name is Rajesh Kumar and I live at 42 MG Road, Bangalore."
for token, label in predict(text):
    if label != "O":
        print(f"{token!r:25s} -> {label}")
```

## Limitations

- Trained primarily on synthetic/templated PII data, so performance may drop on very informal or noisy real-world text.
- Only detects `NAME` and `ADDRESS` — no coverage of emails, phone numbers, IDs, etc.
- Max sequence length is 512 tokens; longer text gets truncated.

## License

MIT