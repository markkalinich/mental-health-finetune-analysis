---
language:
- tr
license: apache-2.0
tags:
- sentiment-analysis
- finance
- turkish
- bert
- financial-nlp
- finbert
- financial bert
pipeline_tag: text-classification
library_name: transformers
---

![FinTurkBERT cover](./cover.png)

# FinTurkBERT Sentiment

FinTurkBERT Sentiment is a Turkish financial sentiment model for sentence-level classification from an investor-oriented perspective.

The model is built on top of a Turkish BERT backbone that was continued-pretrained on approximately 1 GB of cleaned Turkish financial text. After domain-adaptive pretraining, the model was further improved with task-adaptive pretraining (TAPT) and then fine-tuned for 3-class sentiment classification.

The final released checkpoint was trained for Turkish financial sentiment classification using a Turkish version of Financial PhraseBank.

## Labels

- `0`: negative
- `1`: neutral
- `2`: positive

## Annotation Philosophy

The sentiment definition follows the Financial PhraseBank viewpoint:

- sentiment is judged from the perspective of an investor
- the question is whether the sentence implies negative, neutral, or positive value-relevant impact
- vague corporate optimism or procedural statements are often treated as `neutral`

Because of this, the model is relatively conservative and may classify weak or indirect business optimism as neutral unless the positive financial implication is clear.

## Model Behavior

This model is intentionally conservative.

In practice, that means:

- clearly favorable or clearly adverse financial news is usually classified correctly
- routine disclosures, procedural updates, and weakly stated corporate optimism often remain `neutral`
- the model prefers missing some borderline positive signals over producing overly aggressive positive or negative predictions

This behavior is deliberate and matches the investor-oriented annotation style of Financial PhraseBank, where the threshold for assigning positive or negative sentiment is higher than in generic sentiment analysis.

## Training Overview

Training pipeline:

1. Start from a Turkish BERT base model
2. Continue pretraining with masked language modeling on approximately 1 GB of Turkish financial text
3. Apply task-adaptive pretraining on financial task text
4. Fine-tune for 3-class sentiment classification

## Evaluation Summary

Validation results for the selected `75%+` configuration:

- Accuracy: `87.01%`
- Macro-F1: `0.8564`

## Intended Use

This model is intended for:

- Turkish financial news
- company announcements
- investor-facing business reporting
- market commentary
- short sentence-level financial sentiment classification

The primary purpose of the model is to serve as a conservative financial sentiment classifier for Turkish text. It is especially suitable as a first-stage component in a larger NLP system where reliability and controlled sentiment signaling are more important than aggressive polarity detection.

## Limitations

- The model is optimized for short financial text, not long-document reasoning.
- It is conservative by design and may under-predict positive sentiment in softly phrased corporate news.
- It follows investor-impact sentiment, not generic emotional tone.
- Performance may drop on very informal, highly speculative, or non-news financial text.

## Example Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "ff112/FinTurkBERT"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

id2label = {
    0: "negative",
    1: "neutral",
    2: "positive",
}

text = "Sirket yeni bir yatirim anlasmasi imzaladi ve pazardaki konumunu guclendirmeyi hedefliyor."

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=64)

with torch.no_grad():
    logits = model(**inputs).logits
    pred_id = int(torch.argmax(logits, dim=-1))

print(id2label[pred_id])
```

## Recommended Interpretation

For production use, this model works best as a conservative first-stage classifier inside a larger financial NLP pipeline. It is especially suitable when false strong signals are more harmful than missing some borderline positive or negative cases.

If your application prefers cautious investor-style sentiment labeling, this model is a good fit. If your application instead wants to treat soft growth language, strategic expansion, or optimistic corporate messaging as strongly positive more often, then this model may feel too conservative and should be complemented with a second-stage reviewer or a more relaxed model.

## Citation

If you use this model, please cite the accompanying FinTurkBERT work.

```bibtex
@misc{finturkbert,
  title={FinTurkBERT: Domain-Adaptive Pretraining and Sentiment Analysis for Turkish Financial Texts},
  author={Deniz Topal and Furkan Yasir Goksu and Faruk Akyol},
  year={2026}
}
```
