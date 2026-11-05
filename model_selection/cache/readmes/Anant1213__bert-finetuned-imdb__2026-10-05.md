---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- text-classification
- sentiment-analysis
- bert
- imdb
- generated_from_trainer
model-index:
- name: bert-finetuned-imdb
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      type: imdb
      name: IMDb (movie reviews)
    metrics:
    - type: loss
      value: 0.0014
      name: Eval Loss
---

# bert-finetuned-imdb — Sentiment Classification (Positive / Negative)

## Overview (what this model is)

`bert-finetuned-imdb` is a **sentiment classification** model that takes an English text (typically review-like text) and predicts whether the overall sentiment is:

- **Positive** (the author is favorable / satisfied / approving), or
- **Negative** (the author is unfavorable / dissatisfied / critical).

It is built by fine-tuning the transformer model **BERT** (`bert-base-uncased`) for binary text classification.

You can think of this model as a **rule-free automatic tagger** that reads a sentence or paragraph and outputs a sentiment label plus a confidence score.

---

## What you can do with it (practical uses)

This model is useful when you have **a lot of text feedback** and you want a quick, consistent way to label it.

Common use cases:

1. **Review analysis**
   - Movie reviews
   - Product reviews
   - App store reviews

2. **Customer feedback triage**
   - Mark feedback as “positive” vs “negative”
   - Route negative feedback for faster response
   - Track sentiment trends over time

3. **Survey responses / open-text fields**
   - Convert free-text answers into measurable sentiment

4. **Dashboards & analytics**
   - Compute % positive / negative by week, campaign, product, etc.
   - Use sentiment as one feature in a bigger reporting system

---

## What the output means 

When you run the model, you typically receive something like:

```json
[
  {
    "label": "POSITIVE",
    "score": 0.992
  }
]

---

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Anant1213/bert-finetuned-imdb")

print(clf("This movie was fantastic, I loved it!"))
print(clf("Worst film ever. Completely boring."))
```
---

## How and why it works (simple explanation)

### What is BERT?
BERT is a neural model trained to understand language patterns and **context** (how words relate to each other in a sentence).

### What is fine-tuning?
Fine-tuning teaches BERT one specific job:  
**given a review → output positive or negative.**

### Why this is usually better than simple rules
Keyword rules fail on phrases like:
- “not good”
- “good but disappointing”
- “hardly impressive”

BERT-based models consider context, so they usually handle these better.

---

## Differences between sentiment approaches (with examples)

People often ask: **“Why use this model instead of a simpler method or a bigger model?”**  
Below is a practical comparison.

### The 4 common options

1. **Keyword / rule-based**
   - Example rule: if text contains “good” → positive  
   - Fast, but often wrong on negation/mixed opinions.

2. **Traditional ML (Logistic Regression / SVM + TF-IDF)**
   - Learns from word counts and common phrases.  
   - Better than rules, but still limited at understanding context.

3. **BERT fine-tuned classifier (this model)**
   - Understands context better.  
   - Usually stronger on negation and phrasing.

4. **Large LLMs (chat models) for sentiment**
   - Can handle nuance and explanations.  
   - But heavier/expensive, slower, and sometimes inconsistent without strict prompting.

---

### Side-by-side examples (what typically happens)

> **Note:** The exact outputs differ by implementation. The point here is the *behavioral difference*.

#### Example 1: Negation
Text: **“The movie was not good.”**
- Keyword rules: ❌ often **Positive** (sees “good”)
- TF-IDF + Logistic Regression: ✅ usually **Negative**
- This BERT model: ✅ **Negative** (handles “not good” well)
- Large LLM: ✅ **Negative** (and can explain why)

#### Example 2: Mixed sentiment
Text: **“Great acting, but the story was terrible.”**
- Keyword rules: ❌ often **Positive** (sees “great”)
- TF-IDF + Logistic Regression: ⚠️ depends; can flip either way
- This BERT model: ✅ usually picks **Negative** (because “terrible” dominates overall sentiment)
- Large LLM: ✅ can say **Mixed**, but if forced to choose binary may pick Negative

**Important:** This model is binary, so it must choose one label even when the text is mixed.

#### Example 3: Subtle negative phrasing
Text: **“I expected more.”**
- Keyword rules: ⚠️ often **Neutral/unknown**
- TF-IDF + Logistic Regression: ⚠️ depends (may miss it)
- This BERT model: ✅ often **Negative** (common review pattern)
- Large LLM: ✅ **Negative** with explanation

#### Example 4: Sarcasm (hard case)
Text: **“Amazing… I fell asleep in 10 minutes.”**
- Keyword rules: ❌ **Positive** (sees “Amazing”)
- TF-IDF + Logistic Regression: ⚠️ inconsistent
- This BERT model: ⚠️ may still fail sometimes (sarcasm is genuinely hard)
- Large LLM: ✅ more likely to catch sarcasm, but not guaranteed

**Takeaway:** If sarcasm is common in your data, test carefully.

---

## When to choose which approach (simple guide)

- Choose **keyword rules** if you need something quick, tiny, and you accept lower accuracy.
- Choose **traditional ML (TF-IDF + LR)** if you need fast inference and decent baseline results.
- Choose **this BERT model** if you want a strong balance of:
  - accuracy
  - speed
  - consistent binary outputs
- Choose **large LLMs** if you need:
  - explanations
  - “mixed/neutral” labels
  - deeper nuance  
  *(but you pay in cost, speed, and potential variability)*

---

## Limitations (important)

- Only **two labels** (positive/negative). No neutral or mixed label.
- Sarcasm and humor can confuse it.
- Very short text is often ambiguous (“ok”, “fine”).
- Works best on **English review-style** text similar to IMDb.

Practical rule: if `score < 0.60`, treat it as uncertain and review manually.

---

## Training and evaluation data

Intended fine-tuning dataset: **IMDb movie reviews** (binary sentiment).  
Input: review text → Output: positive/negative label.

> If you trained on a different dataset, update this section so the card remains accurate.

---

## Training procedure (transparency)

Base model: `bert-base-uncased`

Hyperparameters:
- learning_rate: `2e-05`
- train_batch_size: `8`
- eval_batch_size: `8`
- num_epochs: `11`
- seed: `42`
- optimizer: `AdamW (torch fused)`
- lr_scheduler_type: `linear`

Evaluation metric available:
- **Eval Loss:** `0.0014` (lower is generally better)

---

## Ethical considerations

- May reflect biases present in training data.
- Not recommended as the sole decision-maker for high-stakes decisions.
- Always evaluate on your own domain text before production use.

---

## Framework versions

- Transformers: `4.57.3`
- PyTorch: `2.9.0+cu126`
- Datasets: `4.4.2`
- Tokenizers: `0.22.1`

---

## License

Apache-2.0

---

## Citation

BERT paper (base architecture):

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018).  
**BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**
