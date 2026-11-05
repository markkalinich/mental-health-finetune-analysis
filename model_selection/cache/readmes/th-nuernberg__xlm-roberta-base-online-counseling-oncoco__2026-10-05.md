---
license: cc-by-sa-4.0
language:
  - de
  - en
library_name: transformers
tags:
  - text-classification
  - counseling
  - mental-health
  - psychosocial
  - multilingual
  - xlm-roberta
base_model: FacebookAI/xlm-roberta-base
datasets:
  - th-nuernberg/OnCoCoV1
metrics:
  - accuracy
  - f1
model-index:
  - name: xlm-roberta-base-online-counseling-oncoco
    results:
      - task:
          type: text-classification
          name: Multi-Class Text Classification
        dataset:
          name: OnCoCoV1
          type: th-nuernberg/OnCoCoV1
        metrics:
          - type: accuracy
            value: 0.76
            name: Top-1 Accuracy
          - type: f1
            value: 0.68
            name: Top-1 Macro F1
          - type: accuracy
            value: 0.86
            name: Top-2 Accuracy
          - type: f1
            value: 0.79
            name: Top-2 Macro F1
---

# xlm-roberta-base-online-counseling-oncoco

Fine-tuned [XLM-RoBERTa base](https://huggingface.co/FacebookAI/xlm-roberta-base) model for fine-grained message classification in psychosocial online counseling conversations. Trained on the [OnCoCo 1.0 dataset](https://huggingface.co/datasets/th-nuernberg/OnCoCoV1).

> **Try it out:** [OnCoCo Message Classifier Space](https://huggingface.co/spaces/th-nuernberg/oncoco)

## Model Description

This model classifies individual messages from online counseling conversations into one of **66 fine-grained categories** — 38 counselor and 28 client categories — covering communication acts such as empathic reflection, problem exploration, motivational interviewing techniques, resource activation, and emotional support.

Messages are prefixed with the speaker role (`Counselor:` / `Client:` in English, `Berater:` / `Klient:` in German) to allow the model to resolve the role context. At inference time, logits for the other speaker's categories are masked so predictions always fall within the correct role-specific category set.

The model was developed as part of the [OnCoCo project](https://huggingface.co/datasets/th-nuernberg/OnCoCoV1) at Technische Hochschule Nürnberg.  
The best model we trained on this dataset is [th-nuernberg/xlm-roberta-large-online-counseling-oncoco](https://huggingface.co/th-nuernberg/xlm-roberta-large-online-counseling-oncoco).  

## Evaluation Results

Evaluated on a held-out 20% test split of the OnCoCo 1.0 dataset (bilingual DE+EN):

| Metric | Score |
|---|---|
| Top-1 Accuracy | 0.76 |
| Top-1 Macro F1 | 0.68 |
| Top-2 Accuracy | 0.86 |
| Top-2 Macro F1 | 0.79 |

## Training Details

- **Base model:** `FacebookAI/xlm-roberta-base`
- **Dataset:** [th-nuernberg/OnCoCoV1](https://huggingface.co/datasets/th-nuernberg/OnCoCoV1) — 5,556 messages (2,778 DE + 2,778 EN translations), 66 categories
- **Split:** 80/20 stratified train/test
- **Languages:** German (original) and English (GPT-4o translated, manually verified)
- **Role prefixes:** Messages are prefixed with `Counselor:` / `Client:` (EN) or `Berater:` / `Klient:` (DE)

## Usage

```python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "th-nuernberg/xlm-roberta-base-online-counseling-oncoco"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

text = "Counselor: It sounds like you're feeling overwhelmed. Can you tell me more?"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    probs = F.softmax(model(**inputs).logits, dim=-1).squeeze()

top3 = probs.argsort(descending=True)[:3]
for i in top3:
    print(f"{model.config.id2label[i.item()]}: {probs[i].item():.4f}")
```

To resolve category codes to human-readable descriptions:

```python
import json
from huggingface_hub import hf_hub_download

path = hf_hub_download("th-nuernberg/OnCoCoV1", "code_to_category.json", repo_type="dataset")
with open(path) as f:
    code2cat = json.load(f)

for i in top3:
    code = model.config.id2label[i.item()]
    print(f"{code} — {code2cat.get(code, '?')}: {probs[i].item():.4f}")
```

## Category Taxonomy

The 66 categories are organized hierarchically for both speaker roles:

**Counselor (38 categories)**
- Formalities (opening, closing)
- Moderation
- Impact factors: analysis & clarification of problems (13), objectives (2), motivation (4), resource activation (5), problem solving (8)
- Other statements

**Client (28 categories)**
- Formalities (opening, closing)
- Empathy expression (3)
- Impact factors: problem analysis (8), objectives (2), motivation (2), resource activation (2), coping assistance (6)
- Other statements

Full label descriptions are available via the [`code_to_category.json`](https://huggingface.co/datasets/th-nuernberg/OnCoCoV1/blob/main/code_to_category.json) file in the dataset repository.

## Intended Use

- Automated content analysis of online counseling conversations
- Research on counselor–client communication patterns
- Educational feedback tools for counselor training
- Conversational AI research in the mental health domain

## Limitations

- Performance varies across categories; rare categories with few training examples show lower F1 scores
- Some semantically overlapping categories (e.g., problem statement vs. problem definition) are harder to distinguish
- English texts are machine-translated from German; some translation artifacts may affect performance on native English counseling texts

## Citation

If you use this model, please cite the OnCoCo paper:

```bibtex
@inproceedings{albrecht-etal-2026-oncoco,
    title = "{O}n{C}o{C}o 1.0: A Public Dataset for Fine-Grained Message Classification in Online Counseling Conversations",
    author = "Albrecht, Jens and Lehmann, Robert and Poltermann, Aleksandra and Rudolph, Eric and Steigerwald, Philipp and Stieler, Mara",
    booktitle = "Proceedings of the Joint Workshop on Social Context (SoCon) and Integrating NLP and Psychology to Study Social Interactions (NLPSI) at LREC-COLING 2026",
    month = may,
    year = "2026",
    address = "Palma de Mallorca, Spain",
    publisher = "ELRA and ICCL",
}
```

ArXiv preprint: [arXiv:2512.09804](https://arxiv.org/abs/2512.09804)

## License

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) — Technische Hochschule Nürnberg

