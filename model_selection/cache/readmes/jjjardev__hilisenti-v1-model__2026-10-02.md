---
language: hil
license: cc-by-nc-sa-4.0
doi: 10.57967/hf/9302
tags:
  - sentiment-analysis
  - hiligaynon
  - low-resource
  - xlm-roberta
  - cross-lingual-transfer
datasets:
  - jjjardev/hilisenti-v1
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
widget:
  - text: "Sobrang sarap ng pagkain dito sa restaurant na ito."
    example_title: "Positive"
  - text: "Napakabagal ng internet connection namin ngayon."
    example_title: "Negative"
  - text: "Bukas ang sangay nila mula alas-otso hanggang alas-singko."
    example_title: "Neutral"
---

# HiliSenti-v1-model

## Model Description

**HiliSenti-v1-model** is a fine-tuned **XLM‑RoBERTa‑large** (355M parameters) model for ternary sentiment classification (Negative, Neutral, Positive) of Hiligaynon text. It was trained on the **HiliSenti v1 dataset**, the first publicly available multi-domain sentiment analysis dataset for Hiligaynon.

The model achieves **93.5% test accuracy** and a **macro F1 of 93.4%**, with per-class F1 scores of 0.95 (Negative), 0.91 (Neutral), and 0.94 (Positive).

## Intended Uses

- Sentiment analysis of Hiligaynon customer feedback
- Social media monitoring for Hiligaynon-speaking communities (Negros Occidental, Panay Island, Soccsksargen)
- Educational and civic technology applications
- Research on low-resource Philippine languages

## Out-of-Scope Uses

- Fine-grained emotion detection
- Aspect-based sentiment analysis
- High-stakes decision-making without human verification
- Languages other than Hiligaynon (the model may still work to some extent, but is not optimized for them)

## Training Data

The model was trained on the **HiliSenti v1 dataset**:

| Split      | Sentences  | Negative   | Neutral    | Positive   |
| ---------- | ---------- | ---------- | ---------- | ---------- |
| Train      | 18,854     | 6,817      | 5,834      | 6,203      |
| Validation | 2,241      | 857        | 687        | 697        |
| Test       | 2,242      | 828        | 633        | 781        |
| **Total**  | **23,337** | **8,502**  | **7,154**  | **7,681**  |

Data sources include:

- **Digicast Negros** (news articles) – ~10,000 sentences
- **Facebook & Reddit** (social media) – ~2,000 sentences
- **Cross-lingual translation** (product reviews, student feedback) – ~5,600 sentences
- **Synthetic augmentation** (edge cases: sarcasm, extreme sentiments) – ~5,600 sentences

## Training Procedure

- **Base model**: `xlm-roberta-large` (355M parameters)
- **Tokenizer**: XLM‑RoBERTa‑large SentencePiece tokenizer with 46 custom Hiligaynon tokens added, taking the vocabulary from 250,002 to 250,048
- **Max sequence length**: 128 tokens
- **Batch size**: 16 (effective batch size 32 via gradient accumulation)
- **Learning rate**: `2e-5` with cosine schedule and 10% warm-up
- **Optimizer**: AdamW (fused)
- **Epochs**: 5 (early stopping with patience 3)
- **Loss**: class-weighted cross-entropy. `label_smoothing_factor = 0.1` is present in the saved training configuration but does not take effect, because the trainer's built-in loss is replaced by the class-weighted objective; see `code/train.py`
- **Class weighting**: Balanced weights applied to cross-entropy loss
- **Mixed precision**: FP16
- **Compute**: Google Colab free tier (Tesla T4 GPU) with manual checkpoint pruning to fit 15 GB Google Drive storage

## Evaluation Results

| Metric                | Negative | Neutral  | Positive | Overall   |
| --------------------- | -------- | -------- | -------- | --------- |
| **Precision**         | 0.95     | 0.93     | 0.93     | —         |
| **Recall**            | 0.95     | 0.90     | 0.95     | —         |
| **F1-Score**          | **0.95** | **0.91** | **0.94** | —         |
| **Accuracy**          | —        | —        | —        | **93.5%** |
| **Macro F1**          | —        | —        | —        | **93.4%** |
| **Balanced Accuracy** | —        | —        | —        | **93.3%** |

The model substantially exceeds the original project target of 80% accuracy.

## Limitations

- **Single annotator**: Labels were assigned by a single native Hiligaynon speaker. A formal inter-annotator agreement study is planned for a future version.
- **Dialectal bias**: The dataset is weighted toward Negros Occidental Hiligaynon; Panay and Soccsksargen varieties are under-represented.
- **Task scope**: Only sentence-level ternary sentiment is supported.
- **Sarcasm**: Despite synthetic augmentation, sarcasm detection remains imperfect.
- **No cross-lingual evaluation**: Unlike HILIGAYNER, this model has not yet been evaluated on zero-shot transfer to Cebuano or Tagalog.

## Ethical Considerations

- All data was collected from **publicly available sources** (news websites, public social media posts, public Reddit communities) and existing publicly licensed datasets.
- The dataset contains real names, locations, and descriptions of violence. A content warning is included in the dataset documentation.
- Users are advised to apply their own anonymization or filtering pipelines if required by their institutional privacy regulations.

## Preprocessing Required

This checkpoint was trained on **normalized** text. Feed it input that has been
passed through the same pipeline, or accuracy will be lower than reported:

```python
from preprocess import normalize_hiligaynon

sentence = normalize_hiligaynon("Wala na sang may na record pa nga pig mortality sa probinsya")
```

The normalization (NFKC, lowercasing, Hiligaynon abbreviation expansion,
laughter reduction, repeated-character reduction, whitespace collapsing) lives in
`code/preprocess.py` in the GitHub repository. The examples below are already
normalized in effect, but production input should not be assumed to be.

## Label Column Fix (October 2026)

The validation and total label counts in the table above were approximate
estimates that did not match the released CSVs; they are now the exact figures.
The underlying dataset had a bug in which 91 rows across `val.csv` and `test.csv`
stored the label as a quoted string, breaking `load_dataset()`. That was fixed on
the dataset repository. If you have cached an earlier revision, refresh it.


## How to Use

### Via Transformers

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("jjjardev/hilisenti-v1-model")
tokenizer = AutoTokenizer.from_pretrained("jjjardev/hilisenti-v1-model")

# Example inference
sentence = "Sobrang sarap ng pagkain dito sa restaurant na ito."
inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)
prediction = outputs.logits.argmax().item()

# Map to label
labels = ["Negative", "Neutral", "Positive"]
print(labels[prediction])  # Positive
```

### Using the Pipeline API

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="jjjardev/hilisenti-v1-model")
result = classifier("Napakabagal ng internet connection namin ngayon.")
print(result)  # [{'label': 'Negative', 'score': 0.93}]
```

## Citation

If you use this model or the HiliSenti dataset in your research, please cite:

```bibtex
@misc{jarder2026hilisenti_model,
  author    = {Jarder, Jessie James T.},
  title     = {{HiliSenti-v1-model}: fine-tuned {XLM-RoBERTa-large} for Hiligaynon sentiment classification},
  year      = {2026},
  publisher = {Hugging Face},
  doi       = {10.57967/hf/9302},
  url       = {https://huggingface.co/jjjardev/hilisenti-v1-model}
}

**Dataset Reference:**

```bibtex
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

| Component         | License                                                               |
| ----------------- | --------------------------------------------------------------------- |
| **Model Weights** | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| **Training Code** | [MIT](https://opensource.org/licenses/MIT)                            |
| **Dataset**       | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |

## Related Resources

- **Dataset**: [jjjardev/hilisenti-v1](https://huggingface.co/datasets/jjjardev/hilisenti-v1)
- **Code**: [github.com/jjjardev/hilisenti](https://github.com/jjjardev/hilisenti)
- **Dataset DOI**: [10.57967/hf/8737](https://doi.org/10.57967/hf/8737)
- **Model DOI**: [10.57967/hf/9302](https://doi.org/10.57967/hf/9302)

## Contact

Jessie James T. Jarder — jj.jarder.dev@gmail.com

```

---
```
