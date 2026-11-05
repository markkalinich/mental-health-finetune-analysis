---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - financial-sentiment
  - finance
  - sentiment-analysis
  - text-classification
  - bert
  - minilm
datasets:
  - takala/financial_phrasebank
metrics:
  - accuracy
  - f1
model-index:
  - name: finbert-minilm-sentiment
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Classification
        dataset:
          name: Financial PhraseBank (Sentences_AllAgree)
          type: takala/financial_phrasebank
          config: sentences_allagree
        metrics:
          - type: accuracy
            value: 0.9529
            name: Test Accuracy
          - type: f1
            value: 0.9368
            name: Test Macro-F1
widget:
  - text: "The company reported record quarterly profit, beating analyst expectations."
  - text: "Net sales decreased by 12% and the firm warned of further losses ahead."
  - text: "The board will meet next Tuesday to review the quarterly schedule."
---

# finbert-minilm-sentiment

**A compact financial-sentiment classifier — 33.4M parameters, 95.3% real test accuracy.**

`finbert-minilm-sentiment` classifies financial text into **negative / neutral / positive** sentiment.
It is a compact MiniLM encoder (`microsoft/MiniLM-L12-H384-uncased`, 33.4M parameters)
fine-tuned on the [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank)
benchmark. All metrics below are **real, measured numbers on a held-out test set that was
never seen during training** — no illustrative or synthetic figures.

> **Companion project:** this is the *production* variant. The from-scratch educational
> transformer (~2M params, no pretrained weights, fully annotated) lives at
> [github.com/shaikn6/nano-finbert](https://github.com/shaikn6/nano-finbert) — built to
> teach the internals; this model is the fine-tuned version tuned for real accuracy.

## Results (held-out test set)

Evaluated on a stratified 15% test split (340 sentences) of Financial PhraseBank
`Sentences_AllAgree` — held out completely during training and validation.

| Metric | Value |
|--------|-------|
| **Test accuracy** | **95.29%** |
| **Test macro-F1** | **0.9368** |

Per-class performance:

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|------|---------|
| negative | 0.9130 | 0.9333 | 0.9231 | 45 |
| neutral  | 0.9902 | 0.9665 | 0.9782 | 209 |
| positive | 0.8889 | 0.9302 | 0.9091 | 86 |

## Dataset

- **Source**: [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank)
  (Malo et al., 2014), config `Sentences_AllAgree` — 2,264 sentences where **all** annotators
  agreed on the label (the cleanest subset).
- **Labels**: 3-class sentiment (`negative`, `neutral`, `positive`).
- **Split**: stratified **70 / 15 / 15** train / validation / **test** (`random_state=42`).
  - train = 1,584 · validation = 340 · **test = 340 (held out)**

## Training details

| Setting | Value |
|---------|-------|
| Base encoder | `microsoft/MiniLM-L12-H384-uncased` (12 layers, hidden 384) |
| Parameters | 33,361,155 (~33.4M) |
| Objective | class-weighted cross-entropy (handles label imbalance) |
| Optimizer | AdamW, weight decay 0.01 |
| Learning rate | 3e-5, linear schedule, 10% warmup |
| Batch size | 16 |
| Max sequence length | 96 tokens |
| Epochs | 8 (best validation checkpoint selected) |
| Hardware | CPU only |

Model selection used best validation accuracy; the reported figures are then computed
once on the untouched test set.

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "9mark9/finbert-minilm-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

texts = [
    "The company reported record quarterly profit, beating analyst expectations.",
    "Net sales decreased by 12% and the firm warned of further losses ahead.",
    "The board will meet next Tuesday to review the quarterly schedule.",
]

enc = tokenizer(texts, padding=True, truncation=True, max_length=96, return_tensors="pt")
with torch.no_grad():
    probs = model(**enc).logits.softmax(-1)

for text, p in zip(texts, probs):
    label = model.config.id2label[int(p.argmax())]
    print(f"[{label:8s} {p.max():.2f}] {text}")
# [positive 0.97] The company reported record quarterly profit, ...
# [negative 0.98] Net sales decreased by 12% and the firm warned ...
# [neutral  0.99] The board will meet next Tuesday to review ...
```

## Intended use

- Sentiment scoring of **short, formal financial text**: news headlines, earnings
  summaries, analyst notes, regulatory filings.
- Research, prototyping, and educational use as a compact, CPU-friendly alternative
  to 110M-parameter FinBERT.

## Limitations

- Trained on the **`AllAgree`** subset, which skews **neutral** (1,391 of 2,264).
  The minority `negative` class has the fewest examples; expect slightly lower
  reliability there.
- Domain is **formal financial reporting language** (Reuters-style). Performance on
  informal text (social media, retail-investor slang, emojis) is **not** characterised
  by this benchmark.
- Not financial advice. Outputs are sentiment labels, not buy/sell signals.
- Max sequence length is 96 tokens; longer documents are truncated.

## Reproducibility

Metrics are reproducible: reloading the published `model.safetensors` and re-running
inference on the same stratified test split (`random_state=42`) reproduces
**95.29% accuracy** exactly.

## Citation

Dataset:

```bibtex
@article{malo2014good,
  title={Good debt or bad debt: Detecting semantic orientations in economic texts},
  author={Malo, Pekka and Sinha, Ankur and Korhonen, Pekka and Wallenius, Jyrki and Takala, Pyry},
  journal={Journal of the Association for Information Science and Technology},
  volume={65}, number={4}, pages={782--796}, year={2014}
}
```

## Contact

Maintainer: nagizaazs@gmail.com

## License

MIT
