---
license: cc-by-nc-4.0
language:
- sq
base_model: FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
tags:
- albanian
- political-news
- sentiment-analysis
- xlm-roberta
- low-resource-nlp
- media-analysis
datasets:
- albanian-political-news-metadata
metrics:
- accuracy
- f1
- cohen_kappa
---

# Albanian Political News XLM-R Sentiment Model

This model is a fine-tuned `xlm-roberta-base` classifier for article-level
sentiment analysis of Albanian political news. It was developed for a study of
media tone and framing around the 2025 Albanian parliamentary election.
Zenodo DOI: https://doi.org/10.5281/zenodo.19555420

The model predicts three labels:

- `positive`
- `neutral`
- `negative`

## Model Details

- **Base model:** `FacebookAI/xlm-roberta-base`
- **Task:** Text classification / sentiment analysis
- **Language:** Albanian (`sq`)
- **Domain:** Political news
- **Input type:** Albanian news article text
- **Maximum sequence length used during fine-tuning:** 256 tokens

## Training Data

The model was trained and evaluated on a manually reviewed 511-article sentiment
dataset derived from Albanian political news coverage. The labeled dataset was
split into:

- **Training pool:** 434 articles
- **Held-out test set:** 77 articles

The public dataset release does **not** include full article body text, raw HTML,
or long copyrighted excerpts. It includes metadata, manual labels, split
assignments, framing labels, and out-of-sample predictions for reproducibility.

## Labels

The model configuration uses the following label mapping:

```text
0: positive
1: neutral
2: negative
```

## Evaluation

On the frozen 77-article held-out test set, the fine-tuned XLM-R model achieved:

| Metric | Score |
|---|---:|
| Accuracy | 0.8052 |
| Macro F1 | 0.7857 |
| Weighted F1 | 0.8012 |
| Cohen's kappa | 0.6975 |

Per-class performance:

| Class | Precision | Recall | F1 | N |
|---|---:|---:|---:|---:|
| Positive | 0.74 | 0.95 | 0.83 | 21 |
| Neutral | 0.75 | 0.60 | 0.67 | 20 |
| Negative | 0.88 | 0.83 | 0.86 | 36 |

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="klejvirekaj/albanian-political-news-xlmr-sentiment",
    tokenizer="klejvirekaj/albanian-political-news-xlmr-sentiment",
)

text = "Shembull artikulli politik në gjuhën shqipe."
result = classifier(text, truncation=True, max_length=256)

print(result)
```

You can also load the model manually:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "klejvirekaj/albanian-political-news-xlmr-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
```


## Intended Uses

This model is intended for:

- Academic research on Albanian NLP
- Political-news sentiment analysis
- Low-resource text classification experiments
- Reproducibility of the associated Albanian political news study

## Limitations

- The model predicts overall article tone, not direct stance toward a specific
  political actor.
- The training set is small for a three-class political-news task.
- Labels were produced in a single-annotator project workflow.
- The neutral class is more difficult and less stable than the positive and
  negative classes.
- Inputs longer than 256 tokens may be truncated, which can remove relevant
  context from longer articles.
- The model was developed on Albanian political news and should not be assumed
  to generalize to other languages, genres, or political contexts without
  additional evaluation.

## Ethical and Legal Notes

This model was developed for research use. The associated public dataset release
does not redistribute full copyrighted article text. Users are responsible for
ensuring that any source texts they analyze are accessed and used in compliance
with applicable copyright rules, source-site terms, and local requirements.

Because the model is trained on political-news data, outputs should be treated as
model predictions rather than factual evidence of media bias or political
alignment.

## License

This model is released under **CC BY-NC 4.0** for research and non-commercial
use.

## Citation

If you use this model, please cite the associated research project and dataset
release.

```bibtex
@article{rekaj2026albanian,
  title   = {Tokenizing the Election: A Transformer Approach to Albanian
            2025 Parliamentary Election Sentiment and Framing},
  author  = {Rekaj, Klejvi},
  year    = {2026},
  doi     = {10.5281/zenodo.19555420}
}
```
