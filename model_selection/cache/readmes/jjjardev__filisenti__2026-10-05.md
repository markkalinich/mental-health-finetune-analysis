---
language:
- hil
- tl
- en
language_details: "Hiligaynon and Tagalog, with code-switched segments in English"
pretty_name: FiliSenti
license: cc-by-nc-sa-4.0
base_model: xlm-roberta-large
tags:
- sentiment-analysis
- text-classification
- filipino
- tagalog
- hiligaynon
- philippine-languages
- low-resource
- code-switching
- cross-lingual-transfer
- onnx
datasets:
- jjjardev/tagasenti
- jjjardev/hilisenti-v1
metrics:
- accuracy
- f1
pipeline_tag: text-classification
widget:
- text: "Ang ganda ng serbisyo niyo! Sulit na sulit!"
  example_title: "Positive"
- text: "Wala na talaga, ayaw ko na dito. Ang sama ng ugali."
  example_title: "Negative"
- text: "Okay lang naman, pwede na."
  example_title: "Neutral"
---

# FiliSenti: Unified Filipino Sentiment Model

## Model Description

**FiliSenti** is a fine-tuned **XLM-RoBERTa-large** (355M parameters) model for ternary sentiment classification (Negative, Neutral, Positive) of **Filipino** text, combining **Tagalog** and **Hiligaynon** in a single model. It was trained on **TagaSenti** (Tagalog, 35,686 sentences) and **HiliSenti** (Hiligaynon, 21,095 sentences), for **56,781** sentences in total.

The model achieves **89.2% test accuracy** and a **macro F1 of 0.8915** on the combined held-out test set, the highest published score for 3-class Filipino sentiment analysis. Per-language performance is **91.7% F1** on Hiligaynon and **88.1% F1** on Tagalog, meaning the same model serves both languages without any language switch.

A quantized **INT8 ONNX** version of the model is included for on-device deployment (Flutter + ONNX Runtime) with no internet connection required after the model is placed.

## Intended Uses

- Sentiment analysis of Filipino social-media and customer feedback
- Cross-lingual / unified analysis across Tagalog- and Hiligaynon-speaking communities (Negros Occidental, Panay Island, Soccsksargen, and the wider Philippines)
- On-device, privacy-preserving sentiment analysis on Android devices
- Research on low-resource Philippine languages and cross-lingual transfer

## Out-of-Scope Uses

- Fine-grained emotion detection
- Aspect-based sentiment analysis
- High-stakes decision-making without human verification
- Languages other than Tagalog and Hiligaynon (the model may generalize to some extent via XLM-RoBERTa's multilingual base, but is not optimized for them)

## Training Data

The model was trained on a combination of **TagaSenti** (Tagalog) and **HiliSenti** (Hiligaynon):

| Dataset | Language | Rows Used | Splits Used |
| --------|----------|-----------|-------------|
| TagaSenti | Tagalog / Taglish | 35,686 | Train split only |
| HiliSenti | Hiligaynon | 21,095 | Train + Validation splits |
| **Total** | | **56,781** | |

**Combined stratified split (80 / 10 / 10, by label).** Note that the HiliSenti
contribution is its train and validation splits only; its test split is excluded
entirely, so the totals below do not include it:

| Split | Sentences |
|-------|-----------|
| Train | 45,424 |
| Validation | 5,679 |
| Test | 5,678 |
| **Total** | **56,781** |

The test split was fully held out during model development and never used for hyper-parameter tuning.

## Training Procedure

- **Base model**: `xlm-roberta-large` (355M parameters)
- **Tokenizer**: XLM-RoBERTa-large SentencePiece tokenizer with vocabulary augmentation, in which frequently fragmented Filipino words were added as new tokens (final vocab size 250,011)
- **Text normalisation**: NFKC, laughter collapsing, reduplication (`ganda-ganda` → `ganda ganda`, `sobra2` → `sobra sobra`), slang expansion for Tagalog (`wla→wala`, `dko→di ko`, `kc→kasi`) and Hiligaynon (`gd→gid`, `wla→wala`, `sbng→subong`), repeated-character collapse. **Casing preserved**, since XLM-RoBERTa is a cased model
- **Max sequence length**: 128 tokens
- **Batch size**: 16 (effective batch size 32 via gradient accumulation)
- **Learning rate**: `2e-5` with cosine schedule (min LR `1e-6`) and 312 warm-up steps
- **Optimizer**: AdamW (fused)
- **Epochs**: 5 (early stopping with patience 3; best val F1 0.8895 @ step 5400)
- **Label smoothing**: 0.1
- **Class weighting**: Inverse-frequency weights applied to cross-entropy loss
- **Mixed precision**: FP16 · **Gradient checkpointing**: enabled
- **Compute**: Google Colab (Tesla T4 GPU)
- **Export**: FP32 → ONNX (opset 18, dynamic batch/sequence), then **INT8 dynamic quantization** (`per_channel=True`) in an isolated subprocess to control memory, producing a single-file `filisenti_int8.onnx` (~537 MB)

## Evaluation Results

### Combined test set (5,678 sentences)

| Metric | Negative | Neutral | Positive | Overall |
|--------|----------|---------|----------|---------|
| **F1-Score** | 0.886 | 0.839 | 0.949 | **0.8915** (macro) |
| **Accuracy** | -- | -- | -- | **89.23%** |

### Per-language (test set)

| Language | Test Sentences | Macro F1 |
|----------|----------------|----------|
| **Hiligaynon** | 2,109 | **0.917** |
| **Tagalog** | 3,569 | **0.881** |

These per-language figures are **not directly comparable** with the 93.4% macro F1 reported by the HiliSenti-only model. FiliSenti re-partitions the combined corpus into its own splits, so its Hiligaynon test portion (2,109 sentences) is drawn from the HiliSenti train and validation splits, which the HiliSenti-only model was itself trained on. The 91.7% figure is therefore not a measurement of accuracy retained on unseen Hiligaynon data. The trade-off offered here is coverage rather than accuracy: one checkpoint serving both languages (91.7% Hiligaynon, 88.1% Tagalog) instead of Hiligaynon alone.

## Limitations

- **Dialectal bias**: Hiligaynon training data is weighted toward Negros Occidental; Panay and Soccsksargen varieties are under-represented. Tagalog data skews toward the e-commerce, news, and social-media domains of TagaSenti.
- **Task scope**: Only sentence-level ternary sentiment is supported.
- **Sarcasm**: Despite targeted adversarial augmentation in TagaSenti, sarcasm detection remains imperfect.
- **LLM-annotated data**: Parts of TagaSenti were labeled by an LLM without validation against human ground truth; annotation biases may propagate.
- **Two-language coverage**: The model covers Tagalog and Hiligaynon only; other Philippine languages are not benchmarked.

## Ethical Considerations

- Training data comes from publicly available sources (news, public social media) and the openly published TagaSenti / HiliSenti datasets.
- The source datasets contain real names, locations, and descriptions of events, and have **not been anonymized**. Apply your own anonymization or filtering pipeline where required by institutional or regulatory privacy rules.
- Non-commercial restrictions on the underlying datasets apply to derivative models (see Licenses).

## How to Use

### Via Transformers

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("jjjardev/filisenti")
tokenizer = AutoTokenizer.from_pretrained("jjjardev/filisenti")

sentence = "Sobrang sarap ng pagkain dito sa restaurant na ito."
inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)
prediction = outputs.logits.argmax().item()

labels = ["Negative", "Neutral", "Positive"]
print(labels[prediction])  # Positive
```

### Using the Pipeline API

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="jjjardev/filisenti")
result = classifier("Wala na talaga, ayaw ko na dito. Ang sama ng ugali.")
print(result)  # [{'label': 'Negative', 'score': ...}]
```

### On-Device (ONNX)

Download the INT8 ONNX model:
`https://huggingface.co/jjjardev/filisenti/resolve/main/filisenti_int8.onnx`

```python
import onnxruntime as ort
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("jjjardev/filisenti")
session = ort.InferenceSession("filisenti_int8.onnx", providers=["CPUExecutionProvider"])

text = "Salamat gid sa inyo bulig!"
inputs = tokenizer(text, return_tensors="np", truncation=True, max_length=128)
logits = session.run(["logits"], {
    "input_ids": inputs["input_ids"],
    "attention_mask": inputs["attention_mask"],
})[0]
print(labels[logits.argmax().item()])
```

**ONNX spec:** inputs `input_ids` (int64) and `attention_mask` (int64) with dynamic `[batch, seq_len]`; output `logits` (float32 `[batch, 3]`). This file is what the FiliSenti Flutter app and web demo load.

## Citation

If you use this model or the TagaSenti / HiliSenti datasets in your research, please cite:

```bibtex
@misc{jarder2026filisenti,
  author    = {Jarder, Jessie James T.},
  title     = {FiliSenti: A Unified 3-Class Filipino Sentiment Model for Tagalog and Hiligaynon},
  year      = {2026},
  publisher = {Hugging Face},
  doi       = {10.57967/hf/9796},
  url       = {https://huggingface.co/jjjardev/filisenti}
}
```

**Dataset references:**

```bibtex
@dataset{jarder2026tagasenti,
  author    = {Jessie James T. Jarder},
  title     = {TagaSenti: A Multi-Domain Sentiment Analysis Dataset for Tagalog},
  year      = {2026},
  publisher = {Hugging Face},
  doi       = {10.57967/hf/9620},
  url       = {https://huggingface.co/datasets/jjjardev/tagasenti}
}

@dataset{jarder2026hilisenti,
  author    = {Jessie James T. Jarder},
  title     = {HiliSenti: A Multi-Domain Sentiment Analysis Dataset for Hiligaynon},
  year      = {2026},
  publisher = {Hugging Face},
  doi       = {10.57967/hf/8737},
  url       = {https://huggingface.co/datasets/jjjardev/hilisenti-v1}
}
```

## Licenses

| Component | License |
|-----------|---------|
| **Model Weights** | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| **Training Code** | [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| **TagaSenti dataset** | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| **HiliSenti dataset** | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |

## Related Resources

- **Datasets**: [jjjardev/tagasenti](https://huggingface.co/datasets/jjjardev/tagasenti) · [jjjardev/hilisenti-v1](https://huggingface.co/datasets/jjjardev/hilisenti-v1)
- **Code**: [github.com/jjjardev/filisenti](https://github.com/jjjardev/filisenti)
- **ONNX model**: `filisenti_int8.onnx` in this repository

## Contact

Jessie James T. Jarder, jj.jarder.dev@gmail.com
