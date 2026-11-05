---
license: cc-by-nc-4.0
language: [en]
base_model: FacebookAI/roberta-large
pipeline_tag: text-classification
tags: [emotion-recognition, health, hiv, multi-label]
---
# HIVRoBERTa

The emotion-recognition backbone reported in the accompanying paper: RoBERTa-large, domain-adaptively pretrained on HIV-contextualized messages, then fine-tuned in two phases (GoEmotions, then GoEmotions merged with the HIV-contextualized data) with focal loss. Seven sigmoid outputs (anger, disgust, embarrassment, fear, grief, nervousness, sadness) — **the model has no neutral class and never predicts neutral**. In the deployed pipeline the backbone passes its seven probabilities to an LLM (GPT-5-mini, 4-shot), which makes the final single-label decision over eight classes, neutral included. See referenced paper at the end for more details.

## Results (balanced 800-message evaluation set; see the HIVEmotions dataset)
| Configuration | Macro P | Macro R | Macro F1 | Micro F1 |
|---|---|---|---|---|
| HIVRoBERTa alone | 0.82 | 0.78 | 0.78 | 0.78 |
| HIVRoBERTa + GPT-5-mini (paper pipeline) | 0.90 | 0.88 | 0.88 | 0.88 |

## Thresholds (learned parameters — do not use 0.5)
Deployed, F1-tuned (`best_thr_f1.*`) — **use these to reproduce the paper**: anger 0.45, disgust 0.65, embarrassment 0.85, fear 0.50, grief 0.40, nervousness 0.90, sadness 0.70. A recall-oriented set (β=2, `best_thr_recall.*`: 0.15/0.40/0.75/0.40/0.20/0.40/0.45) is included for screening-style use; it is not the paper's configuration.

## Standalone use — the paper's backbone-only scoring convention
To use or score the backbone *without* the LLM stage, the paper assigns the highest-probability emotion among those crossing their thresholds, and neutral when none crosses (Table 3.2's backbone row, Appendix E.5). That mapping is an **evaluation convention, not a model output** — in the deployed system, neutral decisions come from the LLM stage.
```python
import numpy as np, torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tok = AutoTokenizer.from_pretrained("SebastianVla/HIVRoBERTa"); model = AutoModelForSequenceClassification.from_pretrained("SebastianVla/HIVRoBERTa").eval()
thr = np.load("best_thr_f1.npy")  # order matches config.id2label
enc = tok(["I get scared every time my refill is late."], return_tensors="pt", truncation=True, max_length=384)
p = torch.sigmoid(model(**enc).logits)[0].detach().numpy()
label = model.config.id2label[int(np.argmax(np.where(p >= thr, p, -1)))] if (p >= thr).any() else "neutral"
```

## Training
DAPT (935 messages, MLM 0.15, seq 256) → phase 1 on GoEmotions (7-label projection) → phase 2 on GoEmotions merged with the HIV data (focal γ=2, label smoothing 0.1, authored-message downweighting). Trained on a single NVIDIA T4 (Google Colab) with gradient accumulation preserving effective batch sizes of 32/32/16; `transformers==4.57.1`, seed 42.

## Limitations
Not a medical device; research use only. Weakest categories are fear and grief (recall 0.68 in the full pipeline). English only. Evaluation uses authored messages whose intended labels were fixed at authoring time. Single training run; GPU nondeterminism means retraining lands near, not on, these numbers.

## Citation
To come...
<CITATION — paper reference to be added>
