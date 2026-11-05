---
language:
- tr
license: mit
tags:
- turkish
- sentiment-analysis
- text-classification
- roberta
- turkish-nlp
thumbnail: latensis_logo.png
---

# Latensis Sentiment — Turkish Sentiment Analysis

<p align="center">
  <img src="latensis_logo.png" width="300"/>
</p>

> *Understanding Beyond the Visible*

**Latensis Sentiment** is a Turkish sentiment analysis model fine-tuned on top of 
[Latensis RoBERTa Base](https://huggingface.co/mursideaki/latensis-roberta-base-tr) — 
a Turkish-specific RoBERTa model trained from scratch with the 
[Hecemen Unigram 128k tokenizer](https://huggingface.co/mursideaki/hecemen-tokenizer-unigram-128k).

## Labels

| ID | Label |
|----|-------|
| 0 | Negative |
| 1 | Positive |

## Benchmark Results

Evaluated on two independent test sets. Comparison against 
`savasy/bert-base-turkish-sentiment-cased` (BERTurk Sentiment).

| Dataset | Our Model | BERTurk | Notes |
|---------|-----------|---------|-------|
| TRSAv1 — Accuracy | **0.9027** | 0.8372 | Independent test set |
| TRSAv1 — F1-macro | **0.9026** | 0.8350 | Independent test set |
| Winvoker — Accuracy | **0.8534** | 0.6944 | BERTurk trained on this data |
| Winvoker — F1-macro | **0.7862** | 0.6488 | BERTurk trained on this data |
| SentiTurca Movies — Accuracy | 0.8060 | **0.8186** | Film domain |

> On Winvoker test set, our model outperforms BERTurk by +16pp accuracy — 
> notably, BERTurk was trained on Winvoker data while our model had never seen it.

## Training Details

| Property | Value |
|----------|-------|
| Base model | Latensis RoBERTa Base (500k steps, val loss 3.21) |
| Training data | 19k examples (film + product reviews) |
| Labels | Binary (positive / negative) |
| Tokenizer | Hecemen Unigram 128k |

## Usage

```python
import torch
import sentencepiece as spm
from transformers import RobertaForSequenceClassification, RobertaConfig
from huggingface_hub import hf_hub_download

# Load tokenizer
spm_path = hf_hub_download(
    repo_id="mursideaki/hecemen-tokenizer-unigram-128k",
    filename="tr_unigram_tokenizer.model"
)
sp = spm.SentencePieceProcessor()
sp.load(spm_path)

PAD_ID = sp.piece_to_id("<pad>")
BOS_ID = sp.piece_to_id("<s>")
EOS_ID = sp.piece_to_id("</s>")
MAX_LENGTH = 256

def tokenize(text):
    ids  = sp.encode_as_ids(str(text))
    ids  = [BOS_ID] + ids[:MAX_LENGTH-2] + [EOS_ID]
    mask = [1] * len(ids)
    if len(ids) < MAX_LENGTH:
        pad_len = MAX_LENGTH - len(ids)
        ids  = ids  + [PAD_ID] * pad_len
        mask = mask + [0]      * pad_len
    return ids, mask

# Load model
config = RobertaConfig.from_pretrained("mursideaki/latensis-sentiment-tr")
model  = RobertaForSequenceClassification.from_pretrained(
    "mursideaki/latensis-sentiment-tr",
    config=config
)
model.eval()

# Predict
def predict(text):
    ids, mask = tokenize(text)
    input_ids      = torch.tensor([ids],  dtype=torch.long)
    attention_mask = torch.tensor([mask], dtype=torch.long)
    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    label = outputs.logits.argmax(dim=-1).item()
    return "positive" if label == 1 else "negative"

print(predict("Bu ürün gerçekten çok kaliteliydi, kesinlikle tavsiye ederim!"))
# → positive

print(predict("Berbat bir deneyimdi, bir daha almam."))
# → negative
```

## Companion Models

- [latensis-roberta-base-tr](https://huggingface.co/mursideaki/latensis-roberta-base-tr) — Base model
- [hecemen-tokenizer-unigram-128k](https://huggingface.co/mursideaki/hecemen-tokenizer-unigram-128k) — Tokenizer
- NER model *(coming soon)*
- STS model *(coming soon)*

## Citation

```bibtex
@misc{latensis2026,
  author    = {Mürşide Aki},
  title     = {Latensis: Turkish NLP Model Suite},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/mursideaki/latensis-sentiment-tr}
}
```

## License

MIT
