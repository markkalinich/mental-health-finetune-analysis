---
language:
- fa
license: apache-2.0
tags:
- persian
- farsi
- emotion-classification
- multi-label-classification
- bert
- parsbert
- goemotions
- nlp
- text-classification
datasets:
- aydakikio/goemotion_persian
metrics:
- f1
base_model: HooshvareLab/bert-fa-zwnj-base
pipeline_tag: text-classification
---

# Khayyam — Persian Multi-Label Emotion Classifier

**Khayyam** is a fine-tuned Persian BERT model for fine-grained, multi-label emotion classification across **28 emotion categories**, based on the GoEmotions taxonomy. It is built on top of [ParsBERT v3](https://huggingface.co/HooshvareLab/bert-fa-zwnj-base) and trained on [GoEmotions Persian](https://huggingface.co/datasets/aydakikio/goemotion_persian) — a Persian translation of Google's GoEmotions benchmark dataset.

The model is named after **Omar Khayyam**, the 11th-century Persian poet, mathematician, and philosopher.

---

## Model Details

| Property | Value |
|---|---|
| Base model | `HooshvareLab/bert-fa-zwnj-base` (ParsBERT v3) |
| Task | Multi-label text classification |
| Language | Persian (Farsi / `fa`) |
| Number of labels | 28 |
| Decision threshold | 0.3 |
| License | Apache 2.0 |

---

## Evaluation Results

Evaluated on the held-out test split of GoEmotions Persian (5,427 samples):

| Metric | Score |
|---|---|
| **F1 Macro** | **0.4124** |
| **F1 Micro** | **0.5563** |

For reference, the original GoEmotions paper (Demszky et al., 2020) reports **F1 Macro of 0.46** for BERT-base on the English dataset. Khayyam achieves competitive results considering the additional challenges of translation noise and Persian-specific linguistic features.

### Training curve

| Epoch | Train Loss | Val Loss | F1 Macro | F1 Micro |
|---|---|---|---|---|
| 1 | 0.1029 | 0.1026 | 0.3231 | 0.5313 |
| 2 | 0.0934 | 0.0950 | 0.3817 | 0.5597 |
| 3 | 0.0826 | 0.0939 | 0.4016 | 0.5585 |
| 4 | 0.0768 | 0.0951 | 0.4105 | 0.5574 |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "aydakikio/Khayyam"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

LABELS = [
    "admiration", "amusement", "anger", "annoyance", "approval", "caring",
    "confusion", "curiosity", "desire", "disappointment", "disapproval",
    "disgust", "embarrassment", "excitement", "fear", "gratitude", "grief",
    "joy", "love", "nervousness", "optimism", "pride", "realization",
    "relief", "remorse", "sadness", "surprise", "neutral"
]

THRESHOLD = 0.3

def predict_emotions(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits).squeeze()
    predicted = [LABELS[i] for i, p in enumerate(probs) if p >= THRESHOLD]
    return predicted

# Example
text = "امروز خیلی خوشحالم، همه چیز عالی پیش رفت!"
print(predict_emotions(text))
# → ['joy', 'optimism', 'excitement']
```

---

## Training Details

### Dataset

- **Dataset:** [GoEmotions Persian](https://huggingface.co/datasets/aydakikio/goemotion_persian)
- **Source:** Persian translation of [Google GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions) using the Gap GPT API
- **Size:** 54,263 samples (train: 43,410 / dev: 5,426 / test: 5,427)
- **Labels:** 27 emotion categories + Neutral (28 total)
- **License:** CC BY 4.0

### Hyperparameters

| Parameter | Value |
|---|---|
| Epochs | 4 |
| Learning rate | 2e-5 |
| Batch size | 16 |
| Max sequence length | 128 |
| Warmup ratio | 0.1 |
| Weight decay | 0.01 |
| Optimizer | AdamW |
| Loss function | Binary Cross-Entropy (multi-label) |
| Precision | fp16 |

---

## Emotion Labels

The model classifies text into any combination of these 28 emotions:

`admiration` · `amusement` · `anger` · `annoyance` · `approval` · `caring` · `confusion` · `curiosity` · `desire` · `disappointment` · `disapproval` · `disgust` · `embarrassment` · `excitement` · `fear` · `gratitude` · `grief` · `joy` · `love` · `nervousness` · `optimism` · `pride` · `realization` · `relief` · `remorse` · `sadness` · `surprise` · `neutral`

---

## Limitations

- Trained on **translated** data — some label noise may exist due to automatic translation
- Performance on rare emotion classes (e.g., `grief`, `pride`, `relief`) is lower than on frequent ones
- Optimized for Persian Reddit-style short text; may generalize differently to formal or dialectal Persian

---

## Citation

If you use this model, please cite:

##### Version 1.0
```bibtex
@misc{ayda_khoshkhan_2026,
	author       = { Ayda Khoshkhan },
	title        = { Khayyam (Revision 4cbc751) },
	year         = 2026,
	url          = { https://huggingface.co/aydakikio/Khayyam },
	doi          = { 10.57967/hf/9089 },
	publisher    = { Hugging Face }
}
```

Also cite the base model and dataset:

```bibtex
@article{ParsBERT,
  title     = {ParsBERT: Transformer-based Model for Persian Language Understanding},
  author    = {Mehrdad Farahani and Mohammad Gharachorloo and Marzieh Farahani and Mohammad Manthouri},
  journal   = {Neural Processing Letters},
  year      = {2021},
  publisher = {Springer}
}

@inproceedings{demszky-etal-2020-goemotions,
  title     = {{G}o{E}motions: A Dataset of Fine-Grained Emotions},
  author    = {Demszky, Dorottya and Movshovitz-Attias, Dana and Ko, Jeongwoo and Cowen, Alan and Nemade, Gaurav and Ravi, Sujith},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
  year      = {2020},
  publisher = {Association for Computational Linguistics}
}
```

---

## License

This model is released under the **Apache 2.0** license, consistent with the base model ([HooshvareLab/bert-fa-zwnj-base](https://huggingface.co/HooshvareLab/bert-fa-zwnj-base)) and the original GoEmotions dataset.

The training dataset ([aydakikio/goemotion_persian](https://huggingface.co/datasets/aydakikio/goemotion_persian)) is licensed under CC BY 4.0.