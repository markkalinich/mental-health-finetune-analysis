---
language: de
license: apache-2.0
tags:
  - emotion
  - sentiment
  - goemotions
  - german
  - multilingual
  - onnx
  - xlm-roberta
datasets:
  - google-research-datasets/go_emotions
pipeline_tag: text-classification
---

# GoEmotions German — xlm-roberta-base (ONNX INT8)

28-emotion sentiment classifier for German text, fine-tuned on GoEmotions dataset translated to German.

## Model Details

- **Base model:** [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) (270M params)
- **Training data:** GoEmotions EN+DE bilingual (87K examples)
- **Translation:** Helsinki-NLP/opus-mt-en-de (English → German)
- **Format:** ONNX INT8 quantized (266MB)
- **Tokenizer:** SentencePiece (tokenizer.json, Unigram)

## Performance

| Metric | Score |
|--------|-------|
| F1 Macro (validation) | **0.399** |
| Top-1 accuracy (28×3 test) | 64% |
| Top-3 accuracy (28×3 test) | 77% |
| Sanity checks | 8/8 |
| Perfect emotions | 11/28 |
| Missed emotions | 3/28 (grief, pride, relief) |

## Labels (28 GoEmotions)

admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral

## Usage (Python + ONNX Runtime)

```python
import onnxruntime as ort
import numpy as np
from tokenizers import Tokenizer

session = ort.InferenceSession("goemotions.onnx")
tokenizer = Tokenizer.from_file("tokenizer.json")
tokenizer.enable_padding(length=128, pad_id=1, pad_token="<pad>")
tokenizer.enable_truncation(max_length=128)

text = "Ich bin heute so glücklich und dankbar"
enc = tokenizer.encode(text)
input_ids = np.array([enc.ids], dtype=np.int64)
attention_mask = np.array([enc.attention_mask], dtype=np.int64)

logits = session.run(None, {"input_ids": input_ids, "attention_mask": attention_mask})[0][0]
probs = np.exp(logits - logits.max()) / np.exp(logits - logits.max()).sum()
top_idx = probs.argmax()
```

## Training Details

- **Epochs:** 6 (stopped early due to disk — F1 was still climbing)
- **Learning rate:** 1e-5
- **Batch size:** 32
- **Warmup:** 10%
- **Optimizer:** AdamW (weight_decay=0.01)
- **Hardware:** RTX 4000 Ada (RunPod)
- **Training time:** ~75 minutes

## Limitations

- Rare emotions (grief, pride, relief) have very few examples in GoEmotions — accuracy is low for these regardless of training
- Translations via MarianMT may miss cultural nuances in German emotional expression
- ONNX only — PyTorch checkpoint not included (contact for reproduction details)

## Citation

If you use this model, please cite GoEmotions:

```bibtex
@inproceedings{demszky2020goemotions,
  title={GoEmotions: A Dataset of Fine-Grained Emotions},
  author={Demszky, Dorottya and others},
  booktitle={ACL},
  year={2020}
}
```

## Author

Built by [tojohere](https://github.com/tojohere) for [SentiLog](https://play.google.com/store/apps/details?id=com.sentilog.app) — an AI-powered journaling app.
