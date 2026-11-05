---
language: fr
license: mit
library_name: transformers
pipeline_tag: text-ranking
base_model: antoinelouis/crossencoder-distilcamembert-mmarcoFR
base_model_revision: 9447ae56ace29839d8bf24f740abdf48ab0a7690
tags:
  - french
  - pharmacy
  - drug
  - reranker
  - cross-encoder
  - camembert
  - distilcamembert
---

# camembert-pharmacy-reranker-distil

French **pharmacy / drug** CrossEncoder reranker (~68M DistilCamemBERT).
This is **not** a universal medical reranker and **not** a SOTA claim.

- **HF repo:** `ymelka/camembert-pharmacy-reranker-distil`
- **Release tag:** `exp-037-step-01948`
- **Weights SHA256 (`model.safetensors`):** `815637b9664e85d9196e0687e3befd07727bc221e1b45eb71d1f649a83ed4051`

## Architecture

- DistilCamemBERT CrossEncoder, ~68M parameters (`CamembertForSequenceClassification`, `num_labels=1`)
- `max_length = 256` at train and eval
- CPU-friendly (same cost class as the parent)

## Parent

```
antoinelouis/crossencoder-distilcamembert-mmarcoFR
revision = 9447ae56ace29839d8bf24f740abdf48ab0a7690
license = MIT
```

Parent training data: French mMARCO (`unicamp-dl/mmarco`). Backbone: `cmarkea/distilcamembert-base`.

## Task

Rerank French pharmacy specialty cards (BDPM) for queries such as substitution
(`générique de …`), dosage, formulation, route, population (enfant/adulte),
and same-molecule wrong variant.

## Training (exp-037)

```
experiment     = exp-037-v3-pharmacy-distil-mixture-v5
data           = pharmacy-mixture-v5 (~14.7k query groups, public BDPM only)
loss           = pairwise
epochs         = 1
lr             = 2e-6
freeze_layers  = 4 (bottom encoder layers)
max_length     = 256
selected ckpt  = step-01948
```

No private Wellchat text. No PARHAF / medical-QCM mix in this recipe.

## How to use

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

repo = "ymelka/camembert-pharmacy-reranker-distil"
rev = "exp-037-step-01948"
tok = AutoTokenizer.from_pretrained(repo, revision=rev)
model = AutoModelForSequenceClassification.from_pretrained(repo, revision=rev)
model.eval()

pairs = [
    ("générique de Doliprane 500 mg", "PARACETAMOL XYZ 500 mg, comprimé"),
    ("générique de Doliprane 500 mg", "IBUPROFENE ABC 400 mg, comprimé"),
]
enc = tok(pairs, padding=True, truncation=True, max_length=256, return_tensors="pt")
with torch.no_grad():
    scores = model(**enc).logits.squeeze(-1)
print(scores)
```

Or `sentence_transformers.CrossEncoder(repo, revision=rev, max_length=256)`.

## Benchmarks

Frozen BDPM evaluator (`RAW_EXACT_GOLD` + `SEMANTIC_MULTI_POSITIVE`).
Holdout opened **once** after preregistration.

| split | metric | parent Distil | this model |
| --- | --- | ---: | ---: |
| pharmacy_dev N=627 | RAW P@1 | 0.761 | 0.797 |
| pharmacy_dev | SEMANTIC P@1 | 0.809 | **0.884** |
| pharmacy_dev substitution | SEMANTIC P@1 | 0.449 | **0.936** |
| pharmacy_final_holdout N=157 | RAW P@1 | 0.834 | 0.873 |
| pharmacy_final_holdout | SEMANTIC P@1 | 0.860 | **0.917** |
| SyntecReranking | MAP | 0.784 | **0.792** |
| AlloprofReranking | MAP@1000 | 0.5810 | 0.5811 |
| MIRACL-fr | nDCG@10 | 0.469 | 0.447 |

Holdout SEMANTIC paired bootstrap 10k, seed 42: Δ +0.057, RESCUE 14 / DESTROY 5,
95% CI [0.006, 0.115] excludes 0.

## Provenance / licenses

| artefact | license / source |
| --- | --- |
| this fine-tune (weights) | MIT (inherits parent) |
| parent CrossEncoder | MIT — Antoine Louis, mMARCO-FR |
| DistilCamemBERT | MIT — `cmarkea/distilcamembert-base` |
| pharmacy-mixture-v5 / pharmacy-ranking-v1 | BDPM dump 2026-08-31, **Licence Ouverte / CADA** — cite [base-donnees-publique.medicaments.gouv.fr](https://base-donnees-publique.medicaments.gouv.fr/) |

No Wellchat private queries, traces, or MAX_DATA.

## Limitations (read these)

- Holdout is an **unseen query / unseen slate** holdout, **not** an unseen-drug entity holdout (`cis_overlap_dev_holdout = 280/361`).
- Generic-group overlap exists between train and holdout (69/92 CIS_GENER groups).
- Contraindication, interactions, pregnancy, renal, hepatic: **not validated** (tiny or empty N).
- Some benchmark axes are lexical shortcuts (indication, adverse_effect, parts of drug_identity).
- MIRACL-fr Δ ≈ **−0.022** nDCG@10 vs parent (not an E2-style collapse; Syntec/Alloprof held).
- **Not** a universal French medical reranker.
- **Not** a SOTA claim.

Independent qrel audit: `iux2019/wellchat` PR #55 (`VALID_WITH_QREL_BUGS`).
Main public metric freeze: BDPM substitution siblings + population side.
Adversarial overlay additionally promotes some formulation/route same-substance other-dose positives.

## Intended use

Rerank a short candidate slate of French specialty cards. Keep a first-stage
retriever. Do not use as a clinical decision system.
