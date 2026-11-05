---
language:
- nl
- en
license: mit
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- xlm-roberta
- dutch
- social-media
- context-aware
- institutional-communication
base_model: FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
model-index:
- name: xlmr-uantwerp-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment classification (context-aware, 3-class)
    metrics:
    - type: accuracy
      value: 0.915
    - type: f1
      value: 0.895
      name: macro F1
    - type: recall
      value: 0.891
      name: negative recall
widget:
- text: "Heel mooi initiatief! </s></s> Universiteit Antwerpen lanceert nieuwe summer school voor AI ethics."
  example_title: "Positive (with context)"
- text: "Niet te geloven </s></s> Vacature interim-rector geopend na vertrek van vorige rector."
  example_title: "Negative (sarcasm needs context)"
- text: "Inschrijvingen gesloten? </s></s> De inschrijvingen voor de bachelor proefweek zijn nu open."
  example_title: "Neutral (factual question)"
---

# XLM-RoBERTa fine-tuned for context-aware sentiment on UAntwerp social media

A Dutch / English 3-class sentiment classifier trained on six years of
public Facebook and Instagram comments to the University of Antwerp.
Built as part of the MSc thesis *"What do you mean? Context-Aware
Sentiment Analysis of Institutional Social Media Comments"* (Margot
Bloemen, UAntwerp, May 2026; supervised by Luna De Bruyne).

The headline observation: on institutional social media, off-the-shelf
commercial tools and traditional ML pipelines miss most of the negative
signal (Coosto: 27 % negative recall, TF-IDF baselines: 61 %). This
model — `xlm-roberta-base` fine-tuned with `RandomOverSampler` on the
training split and the parent post supplied as context — recovers
**89.1 % of negative comments** while reaching 91.5 % accuracy and 89.5
% macro F1 overall. Statistically, the gain from supplying the parent
post is significant only after the class imbalance is addressed
(McNemar p < 0.001 with oversampling; p = 1.000 without).

---

## Headline metrics

Evaluated on the held-out n=485 test set (`dropna + drop_duplicates`
preprocessing, identical across all four XLM-R configurations so they
are directly comparable in McNemar pairs).

| Metric | Score |
|---|---|
| Accuracy | **0.915** |
| Macro F1 | **0.895** |
| Negative recall | **0.891** |


### Comparison with the rest of the field tested

| Family | Best configuration | Acc | Macro F1 | Neg recall |
|---|---|---|---|---|
| Commercial baseline | Coosto | 0.62 | 0.55 | 0.27 |
| Traditional ML | TF-IDF + Logistic Regression (balanced) | 0.72 | 0.66 | 0.61 |
| Transformer encoder ⭐ | **XLM-RoBERTa + OS + context (this model)** | **0.915** | **0.895** | **0.891** |
| Large LLM | GPT-4.1 mini + context + XAI | 0.864 | 0.808 | 0.786 |
| Mid-size LLM | Qwen2.5-72B + context | 0.724 | 0.722 | 0.786 |
| Small LLM | Llama-3.2-3B + context | 0.674 | 0.631 | 0.786 |

⭐ = best on all three headline metrics simultaneously, with no API
dependency.

---

## How to use

### Quick prediction

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("MarGPT/xlmr-uantwerp-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("MarGPT/xlmr-uantwerp-sentiment")
model.eval()

comment = "Heel mooi initiatief!"
post    = "Universiteit Antwerpen lanceert nieuwe summer school voor AI ethics."

# Comment as the first sentence, parent post as the second
inputs = tokenizer(comment, post, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    logits = model(**inputs).logits
pred_id = int(torch.argmax(logits, dim=-1))
print(model.config.id2label[pred_id])      # negative | neutral | positive
```

### With a `pipeline`

```python
from transformers import pipeline
clf = pipeline("text-classification", model="MarGPT/xlmr-uantwerp-sentiment")
clf({"text": "Heel mooi initiatief!", "text_pair": "Universiteit Antwerpen lanceert nieuwe summer school voor AI ethics."})
```

`text_pair` is the parent post; omit it for a comment-only ("standard")
inference but expect lower negative recall on context-dependent cases.

---

## Training data

- **Source:** UAntwerp Facebook (≈75 %) and Instagram (≈25 %), public
  posts and comments collected January 2020 – February 2026.
- **Cleaning:** 3,063 raw comments → 2,684 after filtering `skip`
  (n=339) and `spam` (n=40) labels; passed through `deduce` for Dutch
  de-identification (names, emails, phones, addresses replaced by
  category tokens).
- **Languages:** Dutch (majority), English, Vlaams tussentaal.
- **Class distribution:** 58.3 % positive / 31.3 % neutral / 10.5 %
  negative — heavy imbalance addressed via `RandomOverSampler` on the
  training split only.
- **Splits:** 80 / 20 train / test, stratified on label, seed 42.
- **Inter-annotator agreement** (200-comment dual-annotated subset):
  Cohen's κ = 0.44 (moderate). Negative labels were identical between
  annotators; disagreement concentrates on the positive ↔ neutral
  boundary.

The annotated dataset is **not redistributed** here — it is shared on
request under a data-use agreement.

---

## Training procedure

| Hyperparameter | Value |
|---|---|
| Base model | `FacebookAI/xlm-roberta-base` |
| Max sequence length | 256 |
| Train batch size | 16 |
| Eval batch size | 32 |
| Learning rate | 2e-5 |
| Optimizer | AdamW |
| Weight decay | 0.01 |
| Epochs | 4 |
| Eval / save strategy | per epoch, load best at end (macro F1) |
| Resampler | `RandomOverSampler(random_state=42)` on train split only |
| Input format | `tokenizer(comment_text, post_text, ...)` — segment B = parent post |
| Hardware | Google Colab A100 |
| Framework | `transformers==4.44.2`, `torch==2.3.1`, `imbalanced-learn==0.12.3` |

---

