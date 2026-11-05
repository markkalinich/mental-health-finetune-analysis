---
license: mit
language:
- it
base_model: jhu-clsp/mmBERT-base
pipeline_tag: token-classification
library_name: transformers
tags:
- token-classification
- pii
- ner
- italian
- legal
- gdpr
- anonymization
- privacy
- mmbert
- modernbert
metrics:
- f1
- precision
- recall
model-index:
- name: rizzo-pii-0.3B
  results:
  - task:
      type: token-classification
      name: PII detection (Italian, entity-level)
    metrics:
    - type: f1
      value: 0.9888
      name: micro-F1 (entity-level, IT validation)
    - type: precision
      value: 0.9876
      name: precision
    - type: recall
      value: 0.9900
      name: recall
---

<div align="center">

<img src="assets/mascot_shield.png" alt="rizzo-pii mascot — a purple hedgehog guarding a document with a shield" width="190" />

# rizzo-pii · 0.3B

### Local, reversible PII detection for Italian legal text

**_Use frontier models without giving up your data._**

<p>
<img src="https://img.shields.io/badge/100%25-LOCAL-7c3aed?style=for-the-badge" alt="100% local" />
<img src="https://img.shields.io/badge/GDPR-BY%20DESIGN-7c3aed?style=for-the-badge" alt="GDPR by design" />
<img src="https://img.shields.io/badge/EU%20AI%20ACT-ALIGNED-7c3aed?style=for-the-badge" alt="EU AI Act aligned" />
</p>

<p>
<img src="https://img.shields.io/badge/params-%E2%89%880.3B-blue" alt="0.3B parameters" />
<img src="https://img.shields.io/badge/RAM-~0.5%20GB%20·%20CPU-blue" alt="0.5 GB RAM CPU" />
<img src="https://img.shields.io/badge/PII%20categories-22-blue" alt="22 PII categories" />
<img src="https://img.shields.io/badge/micro--F1-0.989-brightgreen" alt="0.989 micro-F1" />
<img src="https://img.shields.io/badge/offline-no%20API%20key-brightgreen" alt="offline, no API key" />
</p>

<p>
<a href="https://github.com/Rizzo-AI-Academy/rizzo-pii"><img src="https://img.shields.io/badge/GitHub-app%20%26%20code-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
<a href="https://huggingface.co/datasets/rizzoaiacademy/rizzo-pii-it-dataset"><img src="https://img.shields.io/badge/🤗%20Dataset-rizzo--pii--it-FFD21E?style=for-the-badge" alt="Dataset" /></a>
<a href="https://github.com/Rizzo-AI-Academy/rizzo-pii/releases/latest"><img src="https://img.shields.io/badge/⬇%20Windows-installer-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Download for Windows" /></a>
</p>

</div>

---

**`rizzo-pii-0.3B`** is a lightweight, **CPU-friendly, Italian-first** token-classification model
(≈0.3B parameters, [mmBERT](https://huggingface.co/jhu-clsp/mmBERT-base) / ModernBERT backbone)
that detects **22 categories of personal data** — including the Italian legal identifiers
(**codice fiscale**, **partita IVA**, **dati catastali**) that no other open model covers — to
drive a fully **reversible** anonymization workflow:

```
your document → [FULLNAME_1], [IBAN_1], [CF_1] … + local dictionary → closed LLM API → reconstruction
```

The sensitive values never leave your machine. Only the placeholders go to the API; the local
dictionary rebuilds the original from the model's answer. Built for **law firms and GDPR
compliance**.

| | |
|---|---|
| 🇮🇹 **Italian-first** | trained multilingually (8 languages from Ai4Privacy) |
| 🧾 **5 IT-legal tags** | `CF`, `PIVA`, `CATASTO`, `DOCID`, `PROVINCE` — missing from every other PII model |
| 💻 **Runs on CPU** | ~0.5 GB RAM, no GPU, no API key |
| 🔁 **Reversible** | designed for anonymize → call LLM → de-anonymize |
| 📦 **8192-token context** | native (ModernBERT architecture) |

---

## 🚀 Quick start

```python
from transformers import pipeline

nlp = pipeline(
    "token-classification",
    model="rizzoaiacademy/rizzo-pii-0.3B",
    aggregation_strategy="simple",   # merges B-/I- subwords into whole entities
)

text = ("Mi chiamo Mario Rossi, codice fiscale RSSMRA85M01H501Z, "
        "IBAN IT60X0542811101000000123456, email mario.rossi@gmail.com.")

for ent in nlp(text):
    print(f"{ent['entity_group']:<14} {ent['word']!r}  ({ent['score']:.2f})")

# FULLNAME       'Mario Rossi'                   (1.00)
# CF             'RSSMRA85M01H501Z'              (1.00)
# IBAN           'IT60X0542811101000000123456'  (1.00)
# EMAIL          'mario.rossi@gmail.com'         (1.00)
```

### 🔁 Reversible anonymization (the intended use)

```python
def anonymize(text, ents):
    """Replace each entity with a numbered placeholder; keep a reversible dictionary."""
    mapping, out, counters = {}, text, {}
    for e in sorted(ents, key=lambda x: x["start"], reverse=True):
        g = e["entity_group"]
        counters[g] = counters.get(g, 0) + 1
        tag = f"[{g}_{counters[g]}]"
        mapping[tag] = text[e["start"]:e["end"]]
        out = out[:e["start"]] + tag + out[e["end"]:]
    return out, mapping

anon, table = anonymize(text, nlp(text))
# anon  -> "Mi chiamo [FULLNAME_1], codice fiscale [CF_1], IBAN [IBAN_1], email [EMAIL_1]."
# table -> {"[CF_1]": "RSSMRA85M01H501Z", ...}   # stays local; use it to rebuild the LLM reply
```

> **💡 Production tip:** always pair the model with a **regex + checksum** safety net for
> structured fields (EMAIL / TELEPHONE / IBAN / CF / PIVA / credit-card / amount / plate).
> IBAN, CF, PIVA and card numbers are mathematically verifiable — let the checksum override the
> model when they disagree. This is exactly what the [rizzo-pii desktop app](https://github.com/Rizzo-AI-Academy/rizzo-pii) does.

---

## 🏷️ The 22 PII categories

| Group | Tags |
|---|---|
| **People** | `FULLNAME`, `GENDER`, `AGE` |
| **Contact** | `EMAIL`, `TELEPHONENUM` |
| **Location** | `STREET`, `BUILDINGNUM`, `CITY`, `ZIPCODE`, `PROVINCE` |
| **Financial** | `IBAN`, `CREDITCARDNUMBER`, `AMOUNT` |
| **IT-legal identifiers** 🇮🇹 | `CF` (codice fiscale), `PIVA` (partita IVA), `CATASTO` (dati catastali), `DOCID`, `ID_DOC` |
| **Other** | `ORG`, `DATE`, `TIME`, `TARGA` (plate) |

Labels use the **BIO** scheme → **44 label ids** (`B-`/`I-` per tag + `O`).
Full taxonomy and merge rules in the [project docs](https://github.com/Rizzo-AI-Academy/rizzo-pii).

---

## 📊 Evaluation

Entity-level metrics on a held-out **Italian** validation set (7,000 real sentences; the 5
IT-legal tags injected into held-out real text — real context, no leakage):

| Metric | Train (eval subset) | **Validation (IT)** |
|---|---|---|
| Precision | 0.9981 | **0.9876** |
| Recall | 0.9986 | **0.9900** |
| micro-F1 | 0.9984 | **0.9888** |
| Token accuracy | 0.9997 | 0.9985 |

<div align="center">
<img src="assets/training_loss.png" alt="training loss curve" width="560" />
</div>

> Validation is **Italian-only by design** (the real use case is the IT legal domain). The
> training is multilingual, but the other 7 languages are not validated here.

---

## 🧠 Training

- **Base model:** [`jhu-clsp/mmBERT-base`](https://huggingface.co/jhu-clsp/mmBERT-base)
  (multilingual encoder, ModernBERT architecture, native 8192 context). Chosen over vanilla
  ModernBERT because the latter is almost English-only.
- **Data:** ≈**745k** rows fused from 4 sources (multilingual; Italian reinforced to ~45%, ~38% synthetic).
  See the dataset: [**🤗 rizzoaiacademy/rizzo-pii-it-dataset**](https://huggingface.co/datasets/rizzoaiacademy/rizzo-pii-it-dataset).
- **Recipe:** 1 epoch, `max_len=768`, effective batch 32, dynamic padding, `group_by_length`.
- **Hardware:** single RTX 5060 Ti (Blackwell, 16 GB).

### Key idea: *"LLM as author, code as labeler"*
Synthetic data is generated by letting an LLM write only the **prose with placeholders**, while
**code injects the values**. This gives exact BIO labels, mathematically valid checksums
(CF/PIVA/IBAN), and guarantees **no real PII** is ever produced by the LLM.

---

## ⚠️ Limitations & honest expectations

- **Structural overfit risk** on tags that come only from templates (`CATASTO`, `PROVINCE`) —
  mitigated with 72 templates, real-text augmentation, and DeepMount real context.
- **Italian-only validation** — the 7 non-IT languages are not measured.
- **Class imbalance** — `FULLNAME` ≫ `CREDITCARDNUMBER` (~66×), so rare tags are noisier.
- **Always add a regex+checksum net in production.** The model is the recall engine; the
  checksum is the precision guarantee for structured identifiers.

---

## 🔗 Links

- 💻 **App + code (GitHub):** https://github.com/Rizzo-AI-Academy/rizzo-pii — Windows installer, Flask/Tauri UI
- 📚 **Training dataset:** https://huggingface.co/datasets/rizzoaiacademy/rizzo-pii-it-dataset
- 📄 Full technical report (PDF) in the GitHub repo

## 📄 License

MIT © 2026 Simone Rizzo — Rizzo AI Academy

## 📌 Citation

```bibtex
@software{rizzo_pii_2026,
  author  = {Simone Rizzo},
  title   = {rizzo-pii: local reversible PII anonymization for Italian legal text},
  year    = {2026},
  url     = {https://huggingface.co/rizzoaiacademy/rizzo-pii-0.3B},
  note    = {mmBERT/ModernBERT token classification, 22 PII categories}
}
```

<div align="center">
<sub>Made with 🦔 by <a href="https://github.com/Rizzo-AI-Academy">Rizzo AI Academy</a></sub>
</div>
