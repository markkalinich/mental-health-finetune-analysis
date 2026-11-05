---
license: cc0-1.0
datasets:
  - empathyai/books-ner-dataset
language:
  - en
base_model:
  - gliner-community/gliner_large-v2.5
pipeline_tag: token-classification
library_name: gliner
tags:
  - ner
  - gliner
  - books
  - titles
  - authors
---

# Books Named Entity Recognition Model

This model specialises in recognising book titles and author names in short, user‑typed queries. It achieves > 92 % F1 on a held‑out evaluation set.

> Check out this model in action [in this experience](https://projectgutenberg.generativeai.empathy.ai/)!


![Gutenberg AI Search by Empathy.ai](https://cdn-uploads.huggingface.co/production/uploads/66c45337ea476bea05f066a1/fpXuYm-M2rg4Mp9poodNV.png)


---

## 1 Provenance
This model's provenance originates from fine-tuning [gliner-community/gliner_large‑v2.5](https://huggingface.co/gliner-community/gliner_large-v2.5) using synthetic query data derived from [**Project Gutenberg's public catalogue**](https://www.gutenberg.org/).

---

## 2  Use‑case

This model is a drop‑in replacement for generic GLiNER when your text stream revolves around bibliographic requests such as:

> *“Looking for **Dune** from **Frank Herbert**.”*  
> *“Any recommendations by **Mary Shelley**?”*

Typical applications:
* Query understanding in library / e‑book search engines
* Post‑processing LLM output to structure reading lists
* Digital humanities pipelines that need lightweight title/author extraction

**Not** suitable for: recognising publishers, ISBNs or long BIB‑style references (only short queries were used for training).

---

## 3  Performance

| Metric | Overall | `title` | `author` |
|--------|---------|---------|----------|
| Precision | **0.9999** | 0.9999 | 0.9999 |
| Recall    | 0.8583 | 0.7661 | 0.9287 |
| F1‑score  | 0.9237 | 0.8675 | 0.9630 |
| Support   | 69 880 | 30 290 | 39 590 |

*Evaluation dataset:* 43 493 queries (English‑only) held out from the training corpus. Prediction threshold = 0.2.

---

## 4  Quick start
```python
from gliner import GLiNER

model = GLiNER.from_pretrained("empathyai/gliner_large-v2.5-books")
text = "Looking for The Man in the High Castle by Philip K. Dick."

entities = model.predict_entities(text, ["title", "author"], threshold=0.2)
print(entities)
# [{'text': 'The Man in the High Castle', 'label': 'title', 'score': 0.99},
#  {'text': 'Philip K. Dick', 'label': 'author', 'score': 0.99}]
```

---

## 5  Training details
* **Base model:** `gliner_large-v2.5` (≈ 459 M parameters, Creative Commons Zero v1.0 Universal)
* **Dataset:** [`empathyai/books-ner-dataset`](https://huggingface.co/datasets/empathyai/books-ner-dataset) — 435 k synthetic English queries (titles + authors only)
* **Splits:** 391 432 train / 43 493 eval (duplicates removed)
* **Script highlights**
  * Learning rate 5 × 10⁻⁶, linear schedule, warm‑up 10 %
  * Batch 32, gradient accumulation 2, focal loss α 0.75 / γ 2
  * 1 epoch
  * Gradient checkpointing + BF16 for memory efficiency
  * Trained on a single L40S; total wall time ≈ 40 min

---

## 6  Limitations & bias
* The vocabulary of titles/authors comes from Project Gutenberg (public‑domain heavy; modern best‑sellers may be unseen).
* Only short, informal English queries were simulated.  Long paragraphs or non‑English text may degrade accuracy.
* Does not tag publishers, dates, ISBNs, or other bibliographic fields.

---

## 7  Acknowledgements
Thanks to the GLiNER authors and maintainers; HuggingFace for hosting; Project Gutenberg volunteers for the free metadata.