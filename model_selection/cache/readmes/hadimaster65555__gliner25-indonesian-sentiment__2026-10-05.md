---
license: apache-2.0
datasets:
- indonlp/indonlu
language:
- id
- en
- multilingual
metrics:
- accuracy
- macro-f1
base_model:
- fastino/gliner2.5-multi-v1
pipeline_tag: token-classification
tags:
- sentiment-analysis
- fine-tuned
- lora
- gliner2.5
- gliner2
- mdeberta-v3
library_name: gliner2
---

# GLiNER2.5 Indonesian Sentiment Analysis

This model is a fine-tuned version of
[`fastino/gliner2.5-multi-v1`](https://huggingface.co/fastino/gliner2.5-multi-v1)
for **Indonesian three-class sentiment classification**.

It predicts one of:

- `positive`
- `neutral`
- `negative`

The model was fine-tuned with **LoRA** on the **IndoNLU SmSA** dataset and then merged with the base GLiNER2.5 checkpoint for standalone inference.

## Model Details

- **Base model:** `fastino/gliner2.5-multi-v1`
- **Architecture:** GLiNER2.5 BoundaryExtractor
- **Encoder:** multilingual DeBERTa-v3-base
- **Language:** Indonesian (`id`)
- **Task:** text classification / sentiment analysis
- **Labels:** `positive`, `neutral`, `negative`
- **Fine-tuning method:** LoRA
- **Training framework:** GLiNER2
- **Final format:** merged standalone checkpoint

## Intended Use

This model is intended for Indonesian sentiment classification of short- to medium-length text such as:

- comments
- reviews
- social-media-like text
- customer feedback
- short user-generated text

Example:

```text
"pelayanannya bagus banget dan saya sangat puas"
→ positive

"aplikasinya error terus, capek saya"
→ negative

"rapat dimulai jam delapan pagi"
→ neutral
```

## Dataset

The model was fine-tuned on **IndoNLU SmSA (Sentence-level Sentiment Analysis)**.

SmSA contains Indonesian comments and reviews collected from multiple online platforms and annotated with three sentiment classes:

- positive
- neutral
- negative

### Split used in this training run

The official IndoNLU test labels are not used in this experiment.

The experiment used:

| Split | Examples | Purpose |
|---|---:|---|
| Training | 9,827 | LoRA parameter updates |
| Internal validation | 1,092 | checkpoint selection |
| Final held-out evaluation | 1,260 | final reported metrics |

The 9,827 training and 1,092 internal-validation examples were created from the official SmSA training split using a stratified 90/10 split with random seed `42`.

The official labeled SmSA validation split was kept separate and used only as the final held-out evaluation set.

Before splitting, exact duplicate texts were removed and **14 texts overlapping with the held-out evaluation set were removed from the development pool**.

> **Important:** The results below are therefore not results on the hidden official IndoNLU test split. They are results on the official labeled SmSA validation split used as a held-out test set for this experiment.

## Training Procedure

The model was adapted using LoRA on the encoder.

### LoRA configuration

| Parameter | Value |
|---|---:|
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.10 |
| Target modules | `encoder` |
| Trainable parameters | 2,654,208 |
| Total parameters reported during training | 290,009,367 |
| Trainable share | 0.92% |

### Optimization

| Parameter | Value |
|---|---:|
| Epochs | 4 |
| Batch size | 8 |
| Gradient accumulation | 4 |
| Effective batch size | 32 |
| Evaluation batch size | 16 |
| Task learning rate | `5e-4` |
| Weight decay | `0.01` |
| LR scheduler | cosine |
| Warmup ratio | `0.10` |
| Max gradient norm | `1.0` |
| Precision | FP16 |
| Seed | 42 |
| Evaluation strategy | every epoch |
| Early stopping patience | 2 |

The best checkpoint was selected using validation loss.

The best validation loss recorded during training was:

```text
0.1194
```

### Hardware

Training was performed on a **NVIDIA Tesla T4** with approximately **14.6 GB GPU memory**.

The recorded training run completed:

- **1,228 optimization steps**
- **4 epochs**
- about **734.6 seconds** of training time
- approximately **53.5 samples/second**

## Evaluation Results

### Main Results

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Pretrained `fastino/gliner2.5-multi-v1` | 0.7667 | 0.6793 |
| **Fine-tuned model** | **0.9333** | **0.9043** |

Fine-tuning improved Macro-F1 by:

```text
+0.2250
```

### Per-Class Results

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Positive | 0.9668 | 0.9510 | 0.9588 | 735 |
| Neutral | 0.8750 | 0.8015 | 0.8367 | 131 |
| Negative | 0.8921 | 0.9442 | 0.9174 | 394 |
| **Macro average** | **0.9113** | **0.8989** | **0.9043** | 1,260 |
| **Weighted average** | **0.9339** | **0.9333** | **0.9332** | 1,260 |

The model made **84 incorrect predictions out of 1,260 held-out examples**.

Neutral sentiment remains the most difficult class in this evaluation, with an F1 score of `0.8367`, compared with `0.9588` for positive and `0.9174` for negative.

## Usage

Install GLiNER2:

```bash
pip install "gliner2[local]"
```

### Single-text inference

```python
import torch
from gliner2 import AutoExtractor

MODEL_ID = "hadimaster65555/gliner25-indonesian-sentiment"

device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoExtractor.from_pretrained(
    MODEL_ID,
    map_location=device,
)

labels = [
    "positive",
    "neutral",
    "negative",
]

text = "pelayanannya bagus banget dan saya sangat puas"

result = model.classify_text(
    text,
    {
        "sentiment": labels
    },
    include_confidence=True,
)

print(result)
```

### Batch inference

```python
texts = [
    "pelayanannya bagus banget dan saya sangat puas",
    "aplikasinya error terus, capek saya",
    "rapat dimulai jam delapan pagi",
]

schema = (
    model.create_schema()
    .classification(
        "sentiment",
        ["positive", "neutral", "negative"],
    )
)

results = model.batch_extract(
    texts,
    schema,
    batch_size=16,
)

print(results)
```

## Example Predictions

Examples tested after fine-tuning:

| Text | Prediction |
|---|---|
| `pelayanannya bagus banget dan saya sangat puas` | positive |
| `aplikasinya error terus, capek saya` | negative |
| `rapat dimulai jam delapan pagi` | neutral |
| `bagus sih produknya tapi harganya terlalu mahal` | negative |
| `pengirimannya cepat dan produknya sesuai harapan` | positive |

## Limitations

### Not specifically trained on Twitter/X

Although this model may be useful as a starting point for Indonesian social-media sentiment analysis, **SmSA is not a Twitter/X-only dataset**.

The dataset contains Indonesian comments and reviews from multiple online platforms.

As a result, performance may decrease on modern Indonesian Twitter/X text containing:

- newer slang
- very short or fragmentary posts
- hashtags
- emoji-heavy expressions
- sarcasm and irony
- code switching
- trending-topic vocabulary
- unconventional spelling
- conversation-dependent meaning

For a production Twitter/X system, a recommended next step is additional fine-tuning on a manually labeled, in-domain Indonesian Twitter/X dataset.

### Class imbalance

The held-out evaluation set contains:

- 735 positive examples
- 394 negative examples
- 131 neutral examples

Neutral is substantially less represented than positive.

Macro-F1 is therefore reported as the primary metric because it weights each class equally.

### Domain generalization

The model has only been evaluated on the SmSA held-out data used in this experiment.

Performance has **not** been established for:

- modern Twitter/X data
- other Indonesian social-media platforms
- languages other than Indonesian
- financial sentiment
- political sentiment
- aspect-based sentiment
- emotion classification

### Sentiment ambiguity

Sentiment can be subjective.

Mixed statements, sarcasm, irony, implicit sentiment, and context-dependent language can produce incorrect predictions.

The model should not be treated as a definitive measurement of a person's beliefs, intentions, or emotional state.

## Recommended Twitter/X Adaptation

For Indonesian Twitter/X sentiment analysis, a useful training path is:

```text
fastino/gliner2.5-multi-v1
        ↓
fine-tune on IndoNLU SmSA
        ↓
fine-tune on manually labeled Indonesian Twitter/X data
        ↓
evaluate on a separate in-domain Twitter/X test set
```

This model can therefore be treated as an Indonesian sentiment baseline before domain-specific adaptation.

## Training Notes

The original LoRA checkpoint contained approximately **2.65M trainable adapter parameters**.

For deployment, the LoRA adapter was loaded on top of the original GLiNER2.5 model and merged using PEFT's `merge_and_unload()`. The resulting model was saved as a standalone GLiNER2.5 checkpoint.

## Base Model

This model is derived from:

**Fastino — `fastino/gliner2.5-multi-v1`**

https://huggingface.co/fastino/gliner2.5-multi-v1

GLiNER2.5 is a schema-driven information extraction and classification model. The multilingual checkpoint uses an mDeBERTa-v3-base encoder.

## Dataset

**IndoNLU**

https://huggingface.co/datasets/indonlp/indonlu

SmSA is the sentence-level sentiment analysis subset.

## Citation

If you use this model, please also cite the original GLiNER2 and IndoNLU/SmSA work.

### GLiNER2

```bibtex
@misc{zaratiana2025gliner2efficientmultitaskinformation,
  title={GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface},
  author={Urchade Zaratiana and Gil Pasternak and Oliver Boyd and George Hurn-Maloney and Ash Lewis},
  year={2025},
  eprint={2507.18546},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2507.18546}
}
```

### IndoNLU

```bibtex
@inproceedings{wilie2020indonlu,
  title={IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding},
  author={Bryan Wilie and Karissa Vincentio and Genta Indra Winata and Samuel Cahyawijaya and Xiaohong Li and Zhi Yuan Lim and Sidik Soleman and Rahmad Mahendra and Pascale Fung and Syafri Bahar and Ayu Purwarianti},
  booktitle={Proceedings of AACL-IJCNLP},
  year={2020}
}
```

### SmSA

```bibtex
@inproceedings{purwarianti2019improving,
  title={Improving Bi-LSTM Performance for Indonesian Sentiment Analysis Using Paragraph Vector},
  author={Ayu Purwarianti and Ida Ayu Putu Ari Crisdayanti},
  booktitle={Proceedings of the 2019 International Conference of Advanced Informatics: Concepts, Theory and Applications (ICAICTA)},
  pages={1--5},
  year={2019},
  organization={IEEE}
}
```

## License

The base `fastino/gliner2.5-multi-v1` model is released under the **Apache License 2.0**.

The IndoNLU dataset card lists the benchmark under the **MIT License**.

This model repository is therefore published under **Apache-2.0**, while users should also review and comply with the terms of the original model and dataset.

## Acknowledgements

Thanks to:

- the Fastino team for GLiNER2 / GLiNER2.5
- the IndoNLU authors and contributors
- the authors and annotators of the SmSA dataset
